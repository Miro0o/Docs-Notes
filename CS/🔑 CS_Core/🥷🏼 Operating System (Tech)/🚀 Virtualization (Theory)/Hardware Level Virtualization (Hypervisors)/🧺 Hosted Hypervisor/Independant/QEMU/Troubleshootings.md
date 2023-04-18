# Troubleshootings

[TOC]



## 👉 [ability to import standalone qemu instances to lima to manage ](https://github.com/lima-vm/lima/issues/881)

##### Decription: 
I need to use lima to manage VM instance. And the problem is when i was to create an `mininet` vm (for SDN Lab) the only tutorial i found is how to run `mininet` vm on emu. 

So i need to know how to create instance on lima with equal specs on QEMU.

##### Solusions:
Not exactly what i was looking for...

```shell
images:
- location: ~/some/path/my-vm.qcow2
  arch: "x86_64"
```

TBD.... 



## 👉 Access host from guest

> 🔗 [How can I share the localhost of my host computer with a QEMU image?](https://stackoverflow.com/questions/67520919/how-can-i-share-the-localhost-of-my-host-computer-with-a-qemu-image)

A QEMU image running the 'user-mode' networking (as in your command line example) already has access to the host machine. It can access it either via any (non-loopback) IP address the host has, or by using the special 'gateway' IP address. If you're using the default 10.0.2.0/24 network setting then the 'gateway' is 10.0.2.2. I haven't confirmed but suspect that for a non-default net setting it will still be on .2, so in this example 192.168.76.2.

You cannot literally make 'localhost' in the guest point to the host PC, because 'localhost' for the guest is the guest itself, and having it point somewhere else would likely confuse software running in the guest.



## 👉 Host & Guest file transmission

> 🔗 [How to send/upload a file from Host OS to guest OS in KVM?(not folder sharing)](https://unix.stackexchange.com/questions/207012/how-to-send-upload-a-file-from-host-os-to-guest-os-in-kvmnot-folder-sharing) 

Just hit upon two different ways:

- Transfer files via network. For example you can run httpd on the host and use any web browser or `wget`/`curl` to download files. Probably most easy and handy.

- Build ISO image on the host with files you want to transfer. Then attach it to the guest's CD drive.

  ```
  genisoimage -o image.iso -r /path/to/dir
  virsh attach-disk guest image.iso hdc --driver file --type cdrom --mode readonly
  ```

  - You can use `mkisofs` instead of `genisoimage`.
  - You can use GUI like `virt-manager` instead of `virsh` CUI to attach an ISO image to the guest.
  - You need to create a VM beforehand, supply that VM's ID as `guest`. You can see existing VMs by `virsh list --all`.



## 👉 Install Windows 7 in QEMU

#TODO 


[How to install Windows 7 in QEMU](https://computernewb.com/wiki/QEMU/Guests/Windows_7)
