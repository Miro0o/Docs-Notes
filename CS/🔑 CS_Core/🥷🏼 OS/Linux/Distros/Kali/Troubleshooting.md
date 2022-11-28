# Troubleshootings

#### 👉 Host Kali on QEMU

[Hosting a Kali Linux virtual machine using KVM on a Ubuntu 20.10 box](https://heds.nz/posts/hosting-kali-linux-kvm-ubuntu/)

TBD..



#### 👉 [Boot kali on text mode (CLI only)](https://miloserdov.org/?p=3343)

1. Recovery Mode (skip)
2. Single User (skip)
3. Permanently switching to the text interface (in which case i'm in)

Boot into GUI, run

```shell
sudo systemctl start display-manager.service
reboot
```

Return to GUI : 

```shell
sudo systemctl set -default graphical.target
```

