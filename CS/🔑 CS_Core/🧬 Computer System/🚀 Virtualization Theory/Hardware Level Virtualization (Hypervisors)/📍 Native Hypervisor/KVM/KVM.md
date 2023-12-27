# KVM

[TOC]



## Res
🏠 https://www.linux-kvm.org/page/Main_Page


### KVM Docs & Support
📂 👥 https://help.ubuntu.com/community/KVM (Ubuntu Community wiki) (quick guide)

> Ubuntu uses [KVM](http://www.linux-kvm.org/page/Main_Page) as the back-end virtualization technology _primarily for non-graphic servers_ and [libvirt](http://libvirt.org/) as its toolkit/API. Libvirt front ends for managing VMs include [virt-manager](http://virt-manager.et.redhat.com/) (GUI) or virsh (CLI).

📂 https://ubuntu.com/server/docs/virtualization-introduction (Ubuntu Official docs)



## Intro
![](../../../../../../../../Assets/Pics/Pasted%20image%2020230308135949.png)

KVM (for Kernel-based Virtual Machine) is a **full virtualization solution for Linux on x86 hardware containing virtualization extensions (Intel VT or AMD-V)**. It consists of a loadable kernel module, kvm.ko, that provides the core virtualization infrastructure and a processor specific module, kvm-intel.ko or kvm-amd.ko.

Using KVM, one can run multiple virtual machines running unmodified Linux or Windows images. Each virtual machine has private virtualized hardware: a network card, disk, graphics adapter, etc.

KVM is open source software. The kernel component of KVM is included in mainline Linux, as of 2.6.20. The userspace component of KVM is included in mainline QEMU, as of 1.3.

Blogs from people active in KVM-related virtualization development are syndicated at http://planet.virt-tools.org/



## Architecture
![](../../../../../../../../Assets/Pics/Pasted%20image%2020230308140735.png)




## Res
👍 [KVM 学习笔记](https://blog.opskumu.com/kvm-notes.html#orgc40e54b)

[QEMU-KVM基本操作](https://www.cnblogs.com/wujuntian/p/16295818.html) 

[使用 qemu 搭建内核开发环境](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.cnblogs.com%2Fhellogc%2Fp%2F7482066.html) 

