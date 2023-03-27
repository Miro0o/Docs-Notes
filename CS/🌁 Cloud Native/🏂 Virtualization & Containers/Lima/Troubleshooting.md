# 🚀 Troubleshootings

## Official Troubleshooting 🎧 List
### Generic

- ["What's my login password?"](https://github.com/lima-vm/lima#whats-my-login-password)
- ["Does Lima work on ARM Mac?"](https://github.com/lima-vm/lima#does-lima-work-on-arm-mac)
- ["Can I run non-Ubuntu guests?"](https://github.com/lima-vm/lima#can-i-run-non-ubuntu-guests)
- ["Can I run other container engines such as Docker and Podman? What about Kubernetes?"](https://github.com/lima-vm/lima#can-i-run-other-container-engines-such-as-docker-and-podman-what-about-kubernetes)
- ["Can I run Lima with a remote Linux machine?"](https://github.com/lima-vm/lima#can-i-run-lima-with-a-remote-linux-machine)
- ["Advantages compared to Docker for Mac?"](https://github.com/lima-vm/lima#advantages-compared-to-docker-for-mac)

### QEMU

- ["QEMU crashes with `HV_ERROR`"](https://github.com/lima-vm/lima#qemu-crashes-with-hv_error)
- ["QEMU is slow"](https://github.com/lima-vm/lima#qemu-is-slow)
- [error "killed -9"](https://github.com/lima-vm/lima#error-killed--9)
- ["QEMU crashes with `vmx_write_mem: mmu_gva_to_gpa XXXXXXXXXXXXXXXX failed`"](https://github.com/lima-vm/lima#qemu-crashes-with-vmx_write_mem-mmu_gva_to_gpa-xxxxxxxxxxxxxxxx-failed)

### SSH

- ["Port forwarding does not work"](https://github.com/lima-vm/lima#port-forwarding-does-not-work)
- [stuck on "Waiting for the essential requirement 1 of X: "ssh"](https://github.com/lima-vm/lima#stuck-on-waiting-for-the-essential-requirement-1-of-x-ssh)
- ["permission denied" for `limactl cp` command](https://github.com/lima-vm/lima#permission-denied-for-limactl-cp-command)

### Networking

- ==["Cannot access the guest IP 192.168.5.15 from the host"](https://github.com/lima-vm/lima#cannot-access-the-guest-ip-192168515-from-the-host)==
- [Ping shows duplicate packets and massive response times](https://github.com/lima-vm/lima#ping-shows-duplicate-packets-and-massive-response-times)

### External projects

- ["I am using Rancher Desktop. How to deal with the underlying Lima?"](https://github.com/lima-vm/lima#i-am-using-rancher-desktop-how-to-deal-with-the-underlying-lima)

- ["Hints for debugging other problems?"](https://github.com/lima-vm/lima#hints-for-debugging-other-problems)



## 👉 vde-2 & vde_vmnet set up netwokd for Lima
#### Overview
VDE enable Lima instance being accessed from outside the vhost (like the original host).  

The default guest IP 192.168.5.15 is not accessible from the host and other guests.

To add another IP address that is accessible from the host and other virtual machines, enable [`vde_vmnet`](https://github.com/lima-vm/vde_vmnet).

> See [`./docs/network.md`](https://github.com/lima-vm/lima/blob/master/docs/network.md).

Activate `vde_vmnet` after installing  `vde` and `vde_vmnet` & modifying the instance's yml file. 

The network daemons are started automatically when the first instance referencing them is started, and will stop automatically once the last instance has stopped. Daemon logs will be stored in the `$LIMA_HOME/_networks` directory.


#### Steps

>  [Set up a Mac for Qemu with Bridged Network](https://upstreamwithoutapaddle.com/home-lab/bare-metal-bootstrap/)

1. isntall tools needed (might require `command-line-tools` installed)
```shell
brew install qemu autoconf automake wolfssl
```

2. install `vde-2`
```shell
mkdir -p ${OKD_LAB_PATH}/work-dir
cd ${OKD_LAB_PATH}/work-dir
git clone https://github.com/virtualsquare/vde-2
cd vde-2
autoreconf -fis
./configure --prefix=/opt/vde
make
sudo make install
```

3. install `vde_vmnet`
```shell
cd ${OKD_LAB_PATH}/work-dir
git clone https://github.com/lima-vm/vde_vmnet
cd vde_vmnet
make PREFIX=/opt/vde
sudo make PREFIX=/opt/vde install
```

4. Config lima instance's `.yml` file.
```yaml
networks:
  # Lima can manage daemons for networks defined in $LIMA_HOME/_config/networks.yaml
  # automatically. Both vde_switch and vde_vmnet binaries must be installed into
  # secure locations only alterable by the "root" user.
  # - lima: shared
  #   # MAC address of the instance; lima will pick one based on the instance name,
  #   # so DHCP assigned ip addresses should remain constant over instance restarts.
  #   macAddress: ""
  #   # Interface name, defaults to "lima0", "lima1", etc.
  #   interface: ""
  
  
  # vnl (virtual network locator) points to the vde_switch socket directory,
  # optionally with vde:// prefix
- vnl: "vde:///var/run/vde.ctl"
  #   # VDE Switch port number (not TCP/UDP port number). Set to 65535 for PTP mode.
  #   # Default: 0
  switchPort: 0
  #   # MAC address of the instance; lima will pick one based on the instance name,
  #   # so DHCP assigned ip addresses should remain constant over instance restarts.
  macAddress: ""
  #   # Interface name, defaults to "lima0", "lima1", etc.
  interface: ""
```

5. Lift privileges for `vde_vmnet` (optional, depending on cases)

   Since the commands to start and stop the `vde_vmnet` daemon requires root, the user either must have password-less `sudo` enabled, or add the required commands to a `sudoers` file. This can be done via:

   ```shell
   limactl sudoers | sudo tee /etc/sudoers.d/lima
   ```

6. See whether instance now is accessable from a guest IP by `httpd` services.
```shell
sudo apt update && sudo apt install appache2
```

#### 🖇 Links
[VMware的三种网络模式]: https://zhuanlan.zhihu.com/p/24758022
[WolfSSL]: https://www.wolfssl.com
[Autoconf]: https://www.gnu.org/software/autoconf/
[👍 automake, autoconf 使用详解]: https://www.laruence.com/2009/11/18/1154.html



## 👉 [Attempting to mount a writable directory under a read-only directory doesn't work#873](https://github.com/lima-vm/lima/issues/873#issue-1256707387)

#### Related issues:
🖕[chown/chmod on mounted directory: Permission denied #231]( https://github.com/lima-vm/lima/issues/231#issue-992099259)

🖕 [PermissionError:\[Errno 13\] Permission denied:]](https://forum.snapcraft.io/t/permissionerror-errno-13-permission-denied-etc-glances-glances-conf/13824)

🖕 [How to fix the read only error on lima vm](https://stackoverflow.com/questions/71581201/how-to-fix-the-read-only-error-on-lima-vm) 

🖕 [Permission denied when running Docker after installing it as a Snap](https://askubuntu.com/questions/941816/permission-denied-when-running-docker-after-installing-it-as-a-snap) 


```yaml
mounts:
- location: "~"					# mount path overlapping not allowed
- location: "/tmp/lima"
  writable: true
- location: "~/dev"
  writable: true
```



#### Description
🐞 Under `sshfs` (see [#302](https://github.com/lima-vm/lima/issues/302)) mount type overlapping mounts do not work properly. Even worse, it has numerous other critical priviledge issues like `chmod` which may be the cause of dockers required persistence storage booting failure. 

🔎 Solusion is changing to `9p` mount type. Though some argure that this causes effiency problem. 🤷🏽‍♂️ Plus i changed mounts config to this:

```yaml
mounts:
# - location: "~"
- location: "/tmp/lima"
#  mountPoint: ""
  writable: true
- location: "~/Desktop/Coding/CloudNative/harbor"
#  mountPoint: ""
  writable: true
```

As a result, i demolished previous instance and reinstalled a new one using `9p` mount type. 😭

Done! 😭😭😭



## 👉 Lima Proxy Issues

> 🔗 [Lima should get proxy and dns settings from SystemConfiguration instead of from System_Profiler #741](https://github.com/lima-vm/lima/issues/741)

#TODO 


