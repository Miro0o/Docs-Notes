# Linux Kernel

[TOC]



## Res
### Related Topics
↗ [Linux Kernel Security Mechanism](../../../../CyberSecurity/System%20Security/Operating%20System%20Security/🐏%20Linux%20Kernel%20Security%20Mechanism/Linux%20Kernel%20Security%20Mechanism.md)
↗ [Operating System (Theory)](../../../🧬%20Computer%20System/Operating%20System%20(Theory)/Operating%20System%20(Theory).md)

↗ [System Core Function Libraries & C Standard Library](../../📟%20System%20Level%20Programming/😴%20System%20Components%20&%20Runtime%20Libraries/📌%20System%20Core%20Function%20Libraries%20&%20C%20Standard%20Library/System%20Core%20Function%20Libraries%20&%20C%20Standard%20Library.md)
- ↗ [GNU C Library (glibc)](../../📟%20System%20Level%20Programming/😴%20System%20Components%20&%20Runtime%20Libraries/📌%20System%20Core%20Function%20Libraries%20&%20C%20Standard%20Library/👎%20GNU%20C%20Library%20(glibc)/GNU%20C%20Library%20(glibc).md)

↗ [System Components & Runtime Libraries](../../📟%20System%20Level%20Programming/😴%20System%20Components%20&%20Runtime%20Libraries/System%20Components%20&%20Runtime%20Libraries.md)
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

### Docs
📂 [Linux Kernel Documentation](https://docs.kernel.org)
📂 [The Linux Kernel documentation | v4.18](https://www.kernel.org/doc/html/v4.18/index.html)
📂 [The Linux Kernel Docs | Latest](https://www.kernel.org/doc/html/latest/)
[Embedded Linux Wiki](https://elinux.org/Main_Page)


### The Linux Kernel Organization
🏠 https://www.kernel.org/nonprofit.html

📅 2022-09-20
🤳 In [About](https://www.kernel.org/category/about.html). 
🏠 [The Linux Kernel Archives](https://www.kernel.org/) 
📂 [The Linux Kernel documentation | v4.18](https://www.kernel.org/doc/html/v4.18/index.html)
📂 [The Linux Kernel Docs](https://www.kernel.org/doc/)

The Linux Kernel Organization is a California Public Benefit Corporation established in 2002 to distribute the Linux kernel and other Open Source software to the public without charge. We are recognized by the IRS as a 501(c)3 private operating foundation.
- [IRS determination letter](https://www.kernel.org/static/corporate/irs-nonprofit-ok-redacted.pdf)
- [California determination letter](https://www.kernel.org/static/corporate/state-nonprofit-ok-redacted.pdf)

The Linux Kernel Organization is managed by [The Linux Foundation](http://linuxfoundation.org/), which provides full technical, financial and staffing support for running and maintaining the kernel.org infrastructure.


### 🎗 Other resources
- [Git Trees](https://git.kernel.org/)
- [Documentation](https://docs.kernel.org/)
- [Kernel Mailing Lists](https://lore.kernel.org/)
- [Patchwork](https://patchwork.kernel.org/)
- [Wikis](https://www.wiki.kernel.org/)
- [Bugzilla](https://bugzilla.kernel.org/)
- [Mirrors](https://mirrors.kernel.org/)
- [Linux.com](https://www.linux.com/)
- [Linux Foundation](http://www.linuxfoundation.org/)



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





## Ref
[👍 Linux内核应该怎么去学习？ - 知乎]: https://www.zhihu.com/question/58121772

[我为何放弃 Linux 内核学习]: https://happypeter.github.io/learning-kernel.html
[Linux内核入门之路 (非广告) | 51cto]: https://blog.51cto.com/u_15315240/3211777

[👍 👍 Rust std fs 比 Python 慢！真的吗！？]: https://mp.weixin.qq.com/s/m-IBomxu88DlNcEyOgyOew

[Anatomy of the Linux kernel | IBM Docs]: https://developer.ibm.com/articles/l-linux-kernel/
