# Linux Basics

[TOC]



## Res
↗ [Free Software](../🪓%20Free%20Software/Free%20Software.md)



## Intro
### The Origin Of Linux
In August 1991, a Finnish graduate student named Linus Torvalds modestly announced a new Unix-like operating system kernel:
```
From: torvalds@klaava.Helsinki.FI (Linus Benedict Torvalds)
Newsgroups: comp.os.minix
Subject: What would you like to see most in minix?
Summary: small poll for my new operating system

Date: 25 Aug 91 20:57:08 GMT

Hello everybody out there using minix -
I’m doing a (free) operating system (just a hobby, won’t be big and
professional like gnu) for 386(486) AT clones. This has been brewing
since April, and is starting to get ready. I’d like any feedback on
things people like/dislike in minix, as my OS resembles it somewhat
(same physical layout of the file-system (due to practical reasons)
among other things).

I’ve currently ported bash(1.08) and gcc(1.40), and things seem to work.
This implies that I’ll get something practical within a few months, and
I’d like to know what features most people would want. Any suggestions
are welcome, but I won’t promise I’ll implement them :-)

Linus (torvalds@kruuna.helsinki.fi)
```

As Torvalds indicates, his starting point for creating Linux was Minix, an operating system developed by Andrew S. Tanenbaum for educational purposes.

The rest, as they say, is history. Linux has evolved into a technical and cultural phenomenon. By combining forces with the GNU project, the Linux project has developed a complete, Posix-compliant version of the Unix operating system, including the kernel and all of the supporting infrastructure. Linux is available on a wide array of computers, from handheld devices to mainframe computers. A group at IBM has even ported Linux to a wristwatch!


### Linux Development Model
A large part of the success of the Linux Operating System is due to its development model. 

Code contributions are handled by one main mailing list, called LKML (Linux Kernel Mailing List). 
Apart from it, there are many other mailing lists, each dedicated to a Linux kernel subsystem, like
- the netdev mailing list for networking, 
- the linux-pci for the PCI subsystem, 
- the linux-acpi for the ACPI subsystem, 
- and a great many more

The patches which are sent to these mailing lists should adhere to strict rules (primarily the Linux Kernel coding style conventions), and are reviewed by developers all over the world who are subscribed to these mailing lists. Anyone can send patches to these mailing lists.
- Statistics (for example, those published in the lwn.net site from time to time) show that many patches are sent by developers from famous commercial companies like Intel, Red Hat, Google, Samsung, and others. 
- Also, many maintainers are employees of commercial companies (like David Miller, the network maintainer, who works for Red Hat).
- Many times such patches are fixed according to feedback and discussions over the mailing list, and are resent and reviewed again. 

Eventually, the maintainer decides whether to accept or reject patches; and each subsystem maintainer from time to time sends a pull request of his tree to the main kernel tree, which is handled by Linus Torvalds.

Linus himself releases a new kernel version in about every 7–10 weeks, and each such release has about 5–8 release candidates (RC) versions.


### Modular Structure
Linux is structured as a collection of modules, a number of which can be automatically loaded and unloaded on demand. These relatively independent blocks are referred to as **loadable modules** [GOYE99]. In essence, a module is an object file whose code can be linked to and unlinked from the kernel at runtime.

The Linux loadable modules have two important characteristics:
1. **Dynamic linking**: A kernel module can be loaded and linked into the kernel while the kernel is already in memory and executing. A module can also be unlinked and removed from memory at any time.

2. **Stackable modules**: The modules are arranged in a hierarchy. Individual modules serve as libraries when they are referenced by client modules higher up in the hierarchy, and as clients when they reference modules further down.

![](../../../../../Assets/Pics/Screenshot%202023-03-30%20at%2012.42.29%20PM.png)


### 🔩 Linux Kernel Components

> For more at ↗ [🍸 Linux Kernel](../🔩%20Linux%20Kernel/🍸%20Linux%20Kernel.md).

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

• **Interrupts**: Handle interrupts from peripheral devices.



## Ref

