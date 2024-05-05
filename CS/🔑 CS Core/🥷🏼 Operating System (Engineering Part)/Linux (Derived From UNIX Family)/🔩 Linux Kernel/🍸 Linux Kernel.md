# Linux Kernel

[TOC]



## Res
🏠 https://www.kernel.org (**The Linux Kernel Organization**)
📂 https://docs.kernel.org/
📂 https://www.wiki.kernel.org/
- [Git Trees](https://git.kernel.org/)
- [Kernel Mailing Lists](https://lore.kernel.org/)
- [Patchwork](https://patchwork.kernel.org/)
- [Bugzilla](https://bugzilla.kernel.org/)
- [Mirrors](https://mirrors.kernel.org/)
- [Linux.com](https://www.linux.com/)
- [Linux Foundation](http://www.linuxfoundation.org/)

The **Linux Kernel Organization** is a California Public Benefit Corporation established in 2002 to distribute the Linux kernel and other Open Source software to the public without charge. We are recognized by the IRS as a 501(c)3 private operating foundation.
- [IRS determination letter](https://www.kernel.org/static/corporate/irs-nonprofit-ok-redacted.pdf)
- [California determination letter](https://www.kernel.org/static/corporate/state-nonprofit-ok-redacted.pdf)

The Linux Kernel Organization is managed by ↗ [The Linux Foundation](../The%20Linux%20Foundation.md), which provides full technical, financial and staffing support for running and maintaining the kernel.org infrastructure.


### Related Topics
↗ [Linux Kernel Security Mechanism](../../../../CyberSecurity/System%20Security/Operating%20System%20Security/🐏%20Linux%20Kernel%20Security%20Mechanism/Linux%20Kernel%20Security%20Mechanism.md)
↗ [Operating System Kernel](../../📟%20System%20Level%20Programming/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/🫀%20Operating%20System%20Kernel/Operating%20System%20Kernel.md)
↗ [Operating System (Theory Part)](../../../🧬%20Computer%20System/Operating%20System%20(Theory%20Part)/Operating%20System%20(Theory%20Part).md)

↗ [System Core Function Libraries & C Standard Library](../../📟%20System%20Level%20Programming/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/📌%20System%20Core%20Function%20Libraries%20&%20C%20Standard%20Library/System%20Core%20Function%20Libraries%20&%20C%20Standard%20Library.md)
- ↗ [GNU C Library (glibc)](../../📟%20System%20Level%20Programming/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/📌%20System%20Core%20Function%20Libraries%20&%20C%20Standard%20Library/👎%20GNU%20C%20Library%20(glibc)/GNU%20C%20Library%20(glibc).md)

↗ [Operating System Components & Runtime Libraries](../../📟%20System%20Level%20Programming/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/Operating%20System%20Components%20&%20Runtime%20Libraries.md)
↗ [OS Level Programming with C & CPP](../../📟%20System%20Level%20Programming/OS%20Level%20Programming%20with%20C%20&%20CPP/OS%20Level%20Programming%20with%20C%20&%20CPP.md)


### Learning Guides
📂 👍 https://github.com/0voice/linux_kernel_wiki
Linux内核学习资料：200+篇经典内核文章，100+篇内核论文，50+内核项目，500+道内核面试题，80+内核讲解视频

http://kerneltravel.net (Linux 内核之旅 | 西安邮电大学)
Linux内核之旅是一个完全自由和开放的平台，它的建设是在西邮陈莉君教授和在腾讯工作十多年的许振文师兄的指导下完成的，我们的运作方式与国际开源社区一样，所有人都可以共建Linux内核之旅平台，我们都是贡献者，也是受益者。
我们与其他社区合作共同分享内核知识，旨在让更多的人受益。在这里，你可以和我们一起学习Linux内核知识，你可以在Linux内核之旅网站和Linux内核之旅微信公众平台投稿你的学习笔记和心得，你可以在我们的GitHub平台学习和分享内核实验代码，你还可以免费报名陈莉君教授主讲的内核mooc，在讨论区留下你的疑问，就有机会获得陈莉君教授的亲自答疑。

👨‍💻 👍 https://linux-kernel-labs.github.io/refs/heads/master/index.html
Linux Kernel Teaching
This is a collection of lectures and labs Linux kernel topics. The lectures focus on theoretical and Linux kernel exploration.
- This content is based on the [Operatings Systems 2](http://ocw.cs.pub.ro/courses/so2) course from the Computer Science and Engineering Department, the Faculty of Automatic Control and Computers, University POLITEHNICA of Bucharest.
- You can get the latest version at [http://github.com/linux-kernel-labs](http://github.com/linux-kernel-labs).

📖 http://www.kroah.com/lkn/
Linux Kernel in a Nutshell
Professional Linux Kernel Architecture - Wolfgang Mauerer

📂 [Embedded Linux Wiki](https://elinux.org/Main_Page)



## Intro
> 🔗 https://en.wikipedia.org/wiki/Linux_kernel#

![](../../../../../Assets/Pics/Screenshot%202023-04-16%20at%203.49.23%20PM.png)



## Linux Kernel Components & Architecture
> 🔗 https://en.wikipedia.org/wiki/Linux_kernel
> 🔗 https://en.wikipedia.org/wiki/Linux_kernel#Architecture_and_features

![](../../../../../Assets/Pics/Screenshot%202024-02-21%20at%209.18.47PM.png)
<small>Image source from wikipedia: Linux Kernel </small>


### Linux Kernel Components
![](../../../../../Assets/Pics/Screenshot%202023-03-30%20at%2012.48.02%20PM.png)

Briefly, the principal kernel components are the following:
- **Signals**: The kernel uses signals to call into a process. For example, signals are used to notify a process of certain faults, such as division by zero. Table 2.6 gives a few examples of signals.
- **System calls**: The system call is the means by which a process requests a specific kernel service. There are several hundred system calls, which can be roughly grouped into six categories:
	- file system
	- process
	- scheduling
	- interprocess communication
	- socket (networking)
	- miscellaneous
- **Processes and scheduler**: Creates, manages, and schedules processes.
- **Virtual memory**: Allocates and manages virtual memory for processes.
- **File systems**: Provide a global, hierarchical namespace for files, directories, and other file-related objects and provide file system functions.
- **Network protocols**: Support the Sockets interface to users for the TCP/IP protocol suite.
- **Character device drivers**: Manage devices that require the kernel to send or receive data one byte at a time, such as terminals, modems, and printers.
- **Block device drivers**: Manage devices that read and write data in blocks, such as various forms of secondary memory (magnetic disks, CD-ROMs, etc.).
- **Network device drivers**: Manage network interface cards and communications ports that connect to network devices, such as bridges and routers.
- **Traps and faults**: Handle traps and faults generated by the processor, such as a memory fault.
- **Physical memory**: Manages the pool of page frames in real memory and allocates pages for virtual memory.
- **Interrupts**: Handle interrupts from peripheral devices.


### Linux Kernel Subsystems

> 🔗 https://www.kernel.org/doc/html/next/subsystem-apis.html#
#### 1️⃣ Core Subsystems
- [Core API Documentation](https://www.kernel.org/doc/html/next/core-api/index.html)
- [Driver implementer's API guide](https://www.kernel.org/doc/html/next/driver-api/index.html)
- [Memory Management Documentation](https://www.kernel.org/doc/html/next/mm/index.html)
- [Power Management](https://www.kernel.org/doc/html/next/power/index.html)
- [Scheduler](https://www.kernel.org/doc/html/next/scheduler/index.html)
- [Timers](https://www.kernel.org/doc/html/next/timers/index.html)
- [Locking](https://www.kernel.org/doc/html/next/locking/index.html)
#### 2️⃣ Human Interfaces
- [Input Documentation](https://www.kernel.org/doc/html/next/input/index.html)
- [Human Interface Devices (HID)](https://www.kernel.org/doc/html/next/hid/index.html)
- [Sound Subsystem Documentation](https://www.kernel.org/doc/html/next/sound/index.html)
- [GPU Driver Developer's Guide](https://www.kernel.org/doc/html/next/gpu/index.html)
- [Frame Buffer](https://www.kernel.org/doc/html/next/fb/index.html)
- [LEDs](https://www.kernel.org/doc/html/next/leds/index.html)
#### 3️⃣ Networking Interfaces
- [Networking](https://www.kernel.org/doc/html/next/networking/index.html)
- [NetLabel](https://www.kernel.org/doc/html/next/netlabel/index.html)
- [InfiniBand](https://www.kernel.org/doc/html/next/infiniband/index.html)
- [ISDN](https://www.kernel.org/doc/html/next/isdn/index.html)
- [MHI](https://www.kernel.org/doc/html/next/mhi/index.html)
#### 4️⃣ Storage Interfaces
- [Filesystems in the Linux kernel](https://www.kernel.org/doc/html/next/filesystems/index.html)
- [Block](https://www.kernel.org/doc/html/next/block/index.html)
- [CD-ROM](https://www.kernel.org/doc/html/next/cdrom/index.html)
- [SCSI Subsystem](https://www.kernel.org/doc/html/next/scsi/index.html)
- [TCM Virtual Device](https://www.kernel.org/doc/html/next/target/index.html)
#### 5️⃣ Other Subsystems
**Fixme**: much more organizational work is needed here.
- [Accounting](https://www.kernel.org/doc/html/next/accounting/index.html)
- [CPUFreq - CPU frequency and voltage scaling code in the Linux(TM) kernel](https://www.kernel.org/doc/html/next/cpu-freq/index.html)
- [FPGA](https://www.kernel.org/doc/html/next/fpga/index.html)
- [I2C/SMBus Subsystem](https://www.kernel.org/doc/html/next/i2c/index.html)
- [Industrial I/O](https://www.kernel.org/doc/html/next/iio/index.html)
- [PCMCIA](https://www.kernel.org/doc/html/next/pcmcia/index.html)
- [Serial Peripheral Interface (SPI)](https://www.kernel.org/doc/html/next/spi/index.html)
- [1-Wire Subsystem](https://www.kernel.org/doc/html/next/w1/index.html)
- [Watchdog Support](https://www.kernel.org/doc/html/next/watchdog/index.html)
- [Virtualization Support](https://www.kernel.org/doc/html/next/virt/index.html)
- [Hardware Monitoring](https://www.kernel.org/doc/html/next/hwmon/index.html)
- [Compute Accelerators](https://www.kernel.org/doc/html/next/accel/index.html)
- [Security Documentation](https://www.kernel.org/doc/html/next/security/index.html)
- [Crypto API](https://www.kernel.org/doc/html/next/crypto/index.html)
- [BPF Documentation](https://www.kernel.org/doc/html/next/bpf/index.html)
- [USB support](https://www.kernel.org/doc/html/next/usb/index.html)
- [PCI Bus Subsystem](https://www.kernel.org/doc/html/next/PCI/index.html)
- [Assorted Miscellaneous Devices Documentation](https://www.kernel.org/doc/html/next/misc-devices/index.html)
- [PECI Subsystem](https://www.kernel.org/doc/html/next/peci/index.html)
- [WMI Subsystem](https://www.kernel.org/doc/html/next/wmi/index.html)
- [TEE Subsystem](https://www.kernel.org/doc/html/next/tee/index.html)



## Linux API (Developer)
> 🔗 https://www.kernel.org/doc/html/next/index.html

- [Core API Documentation](https://www.kernel.org/doc/html/next/core-api/index.html)
- [Driver implementer's API guide](https://www.kernel.org/doc/html/next/driver-api/index.html)



## Linux Kernel & Hardware
> 🔗 https://www.kernel.org/doc/html/next/index.html

- [The Linux kernel firmware guide](https://www.kernel.org/doc/html/next/firmware-guide/index.html)
- [Open Firmware and Devicetree](https://www.kernel.org/doc/html/next/devicetree/index.html)
- [CPU Architectures](https://www.kernel.org/doc/html/next/arch/index.html)



## Linux Kernel Development
> 🔗 https://www.kernel.org/doc/html/next/index.html

- [A guide to the Kernel Development Process](https://www.kernel.org/doc/html/next/process/development-process.html)
- [Submitting patches: the essential guide to getting your code into the kernel](https://www.kernel.org/doc/html/next/process/submitting-patches.html)
- [Code of conduct](https://www.kernel.org/doc/html/next/process/code-of-conduct.html)
- [Kernel Maintainer Handbook](https://www.kernel.org/doc/html/next/maintainer/index.html)
- [All development-process docs](https://www.kernel.org/doc/html/next/process/index.html)

- [Linux kernel licensing rules](https://www.kernel.org/doc/html/next/process/license-rules.html)
- [How to write kernel documentation](https://www.kernel.org/doc/html/next/doc-guide/index.html)
- [Development tools for the kernel](https://www.kernel.org/doc/html/next/dev-tools/index.html)

- [Kernel Testing Guide](https://www.kernel.org/doc/html/next/dev-tools/testing-overview.html)
- [Kernel Hacking Guides](https://www.kernel.org/doc/html/next/kernel-hacking/index.html)
- [Linux Tracing Technologies](https://www.kernel.org/doc/html/next/trace/index.html)
- [fault-injection](https://www.kernel.org/doc/html/next/fault-injection/index.html)
- [Kernel Livepatching](https://www.kernel.org/doc/html/next/livepatch/index.html)



## 🚂 Rust in the Kernel
> 🔗 https://www.kernel.org/doc/html/next/rust/index.html
> ↗ [Rust](../../../👩‍💻%20Programming%20Methodology%20and%20Languages/Compiled%20Languages/Rust/Rust.md)

To start using Rust in the kernel, please read the [Quick Start](https://www.kernel.org/doc/html/next/rust/quick-start.html)guide.

**The Rust support was merged in v6.1 into mainline in order to help in determining whether Rust as a language was suitable for the kernel, i.e. worth the tradeoffs.**

Currently, the Rust support is primarily intended for kernel developers and maintainers interested in the Rust support, so that they can start working on abstractions and drivers, as well as helping the development of infrastructure and tools.

If you are an end user, please note that there are currently no in-tree drivers/modules suitable or intended for production use, and that the Rust support is still in development/experimental, especially for certain kernel configurations.

This documentation does not include rustdoc generated information.
- [Quick Start](https://www.kernel.org/doc/html/next/rust/quick-start.html)
- [General Information](https://www.kernel.org/doc/html/next/rust/general-information.html)
- [Coding Guidelines](https://www.kernel.org/doc/html/next/rust/coding-guidelines.html)
- [Arch Support](https://www.kernel.org/doc/html/next/rust/arch-support.html)



## 👩‍💻 Linux User & Administrator
> 🔗 https://www.kernel.org/doc/html/next/index.html

- [The Linux kernel user's and administrator's guide](https://www.kernel.org/doc/html/next/admin-guide/index.html)
- [The kernel build system](https://www.kernel.org/doc/html/next/kbuild/index.html)
- [Reporting issues](https://www.kernel.org/doc/html/next/admin-guide/reporting-issues.html)
- [User-space tools](https://www.kernel.org/doc/html/next/tools/index.html)
- [The Linux kernel user-space API guide](https://www.kernel.org/doc/html/next/userspace-api/index.html)



## Other Linux Topics
> 🔗 https://www.kernel.org/doc/html/next/index.html

- [Unsorted Documentation](https://www.kernel.org/doc/html/next/staging/index.html)
- [Reliability, Availability and Serviceability (RAS) features](https://www.kernel.org/doc/html/next/RAS/index.html)



## Ref
[👍 Linux内核应该怎么去学习？ - 知乎]: https://www.zhihu.com/question/58121772

[我为何放弃 Linux 内核学习]: https://happypeter.github.io/learning-kernel.html
[Linux内核入门之路 (非广告) | 51cto]: https://blog.51cto.com/u_15315240/3211777

[👍 👍 Rust std fs 比 Python 慢！真的吗！？]: https://mp.weixin.qq.com/s/m-IBomxu88DlNcEyOgyOew

[Anatomy of the Linux kernel | IBM Docs]: https://developer.ibm.com/articles/l-linux-kernel/
