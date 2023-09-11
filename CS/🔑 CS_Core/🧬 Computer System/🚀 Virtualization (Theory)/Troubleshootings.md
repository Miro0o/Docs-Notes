# Troubleshootings

[TOC]



## 👉 [ability to import standalone qemu instances to lima to manage ](https://github.com/lima-vm/lima/issues/881)
#qemu #lima
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
#qemu #network

> 🔗 [How can I share the localhost of my host computer with a QEMU image?](https://stackoverflow.com/questions/67520919/how-can-i-share-the-localhost-of-my-host-computer-with-a-qemu-image)

A QEMU image running the 'user-mode' networking (as in your command line example) already has access to the host machine. It can access it either via any (non-loopback) IP address the host has, or by using the special 'gateway' IP address. If you're using the default 10.0.2.0/24 network setting then the 'gateway' is 10.0.2.2. I haven't confirmed but suspect that for a non-default net setting it will still be on .2, so in this example 192.168.76.2.

You cannot literally make 'localhost' in the guest point to the host PC, because 'localhost' for the guest is the guest itself, and having it point somewhere else would likely confuse software running in the guest.



## 👉 Host & Guest file transmission
#qemu #network 

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
#qemu #windows7

#TODO 


[How to install Windows 7 in QEMU](https://computernewb.com/wiki/QEMU/Guests/Windows_7)



## 👉 QEMU, No bootable device, Windows Subsystem for Linux
#qemu #wsl

The first thing to do is to check whether this command line and ISO image work on a normal Linux host system. That will tell you whether the problem is (a) the Windows Subsystem for Linux not correctly implementing something QEMU relies on or (b) your ISO image actually not being a bootable CDROM.

You might also try booting a known-good ISO image such as one for a Linux distribution.

(The general principle here is to try to do diagnostic tests to split the space of "what might be the problem" into smaller sections and determine which side your problem is.)


[QEMU, No bootable device, Windows Subsystem for Linux]: https://stackoverflow.com/questions/39232676/qemu-no-bootable-device-windows-subsystem-for-linux



## 👉 VGA and other display devices in `qemu` | Set `qemu` for vmware display controller 

#qemu #display #VGA #SVMSVGA 



[👍 VGA and other display devices in qemu]: https://www.kraxel.org/blog/2019/09/display-devices-in-qemu/#VGA

There are alot of emulated display devices available in qemu. This blog post introduces them, explains the differences between them and the use cases they are good for.

[👍 What are differences between VBoxVGA, VMSVGA and VBoxSVGA in VirtualBox?]: https://superuser.com/a/1403131
