# FAQ

[TOC]



## 👉 Host Kali on QEMU
#kali #qemu 




[Hosting a Kali Linux virtual machine using KVM on a Ubuntu 20.10 box]: https://heds.nz/posts/hosting-kali-linux-kvm-ubuntu/



## 👉 Boot kali on text mode (CLI only)
#kali #booting #cli

1. Recovery Mode (skip)

   This mode is already on the menu. Moreover, if you boot into **Recovery Mode**, then upon a subsequent reboot, the graphical desktop environment will open (if you do not select Recovery Mode again).

2. Single User (skip)

   In single-user mode its peculiarity is that it is impossible to log in as any user other than root. But then you do not need to enter a password for root – for this reason this mode is usually used to restore a forgotten administrator password, but can also be used for other purposes of system recovery and maintenance

3. Permanently switching to the text interface (in which case i'm in)


Swithcing to text mode permanently: 
```shell
sudo systemctl set-default multi-user.target
reboot
```

Back to GUI for this one:
```shell
sudo systemctl start display-manager.service
reboot
```

Back to GUI permanently:
```shell
sudo systemctl set-default graphical.target
reboot
```

[Boot kali on text mode (CLI only)]: https://miloserdov.org/?p=3343
