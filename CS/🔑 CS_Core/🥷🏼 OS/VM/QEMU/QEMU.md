# [QEMU](https://github.com/qemu/qemu)

## Intro

QEMU is a generic and open source machine & userspace emulator and virtualizer.

> [What is a hypervisor?](https://www.vmware.com/topics/glossary/content/hypervisor.html)
>
> A hypervisor, also known as a virtual machine monitor or VMM, is **software that creates and runs virtual machines (VMs)**. A hypervisor allows one host computer to support multiple guest VMs by virtually sharing its resources, such as memory and processing.

QEMU is capable of emulating a complete machine in software without any need for hardware virtualization support. By using dynamic translation, it achieves very good performance. QEMU can also integrate with the Xen and KVM hypervisors to provide emulated hardware while allowing the hypervisor to manage the CPU. With hypervisor support, QEMU can achieve near native performance for CPUs. When QEMU emulates CPUs directly it is capable of running operating systems made for one machine (e.g. an ARMv7 board) on a different machine (e.g. an x86_64 PC board).

QEMU is also capable of providing userspace API virtualization for Linux and BSD kernel interfaces. This allows binaries compiled against one architecture ABI (e.g. the Linux PPC64 ABI) to be run on a host using a different architecture ABI (e.g. the Linux x86_64 ABI). This does not involve any hardware emulation, simply CPU and syscall emulation.



### 🫣 Resources

📂 [QEMU Documentation](https://www.qemu.org/docs/master/about/index.html)

[Getting started with qemu](https://drewdevault.com/2018/09/10/Getting-started-with-qemu.html)





### 🐕 Get-Started

#### Install qemu

```shell
brew install qemu
qemu-system-x86_64 --version
QEMU emulator version 6.0.0
Copyright (c) 2003-2021 Fabrice Bellard and the QEMU Project developers
```



#### Create Virtual Disk

```shell
qemu-img create -f qcow2 ~/QEMU/ubuntu-desktop-20.04.qcow2 100G
```



#### Create VM

> ⚠️ Note here `accel=hvf` is declared for macOS. Most Linux OS use `KVM` as an accelerator.  [Check out more about KVM here](KVM.md) 

```shell
qemu-system-x86_64 \
  -m 4G \
  -vga virtio \
  -display default,show-cursor=on \
  -usb \
  -device usb-tablet \
  -machine type=q35,accel=hvf \
  -smp 4 \
  -drive file=ubuntu-desktop-20.04.qcow2,if=virtio \
  -cpu Nehalem-v1 \
  -net user,hostfwd=tcp::2222-:22 \
  -net nic \
  -cdrom ubuntu-20.04.2.0-desktop-amd64.iso
```



#### Boot VM (Once an instance had been created)

```shell
qemu-system-x86_64 \
  -m 4G \
  -vga virtio \
  -display default,show-cursor=on \
  -usb \
  -device usb-tablet \
  -machine type=q35,accel=hvf \
  -smp 4 \
  -drive file=ubuntu-desktop-20.04.qcow2,if=virtio \
  -cpu Nehalem-v1 \
  -net user,hostfwd=tcp::2222-:22 \
  -net nic
```



#### 🔗 Refs

[XOS 使用 qemu 创建虚拟机]:https://zhjwpku.com/2021/09/28/OSX-create-vm-using-qemu.html
[使用 qemu 搭建内核开发环境]:https://links.jianshu.com/go?to=https%3A%2F%2Fwww.cnblogs.com%2Fhellogc%2Fp%2F7482066.html



## 🖇 Links:

1. [QEMU简介](https://blog.csdn.net/hunanchenxingyu/article/details/43230229)
2. [Set up a Mac for Qemu with Bridged Network](https://upstreamwithoutapaddle.com/home-lab/bare-metal-bootstrap/)
3. [What is the difference between qemu and kvm](https://www.packetcoders.io/what-is-the-difference-between-qemu-and-kvm/)

![image1](../../../../../../Assets/Pics/image1.png)

