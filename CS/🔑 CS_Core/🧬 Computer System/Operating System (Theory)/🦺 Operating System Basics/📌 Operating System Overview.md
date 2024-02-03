# Operating System Overview

[TOC]



## OS Intro
The operating system itself is little more than an ordinary piece of software. It differs from most other software in that it is loaded by booting the computer and is then executed directly by the processor. 

The operating system must have control of the processor (as well as other resources), because one of its many tasks is scheduling the processes that use the CPU. It relinquishes control of the CPU to various application programs during the course of their execution. The operating system is dependent on the processor to regain control when the application either no longer requires the CPU or gives up the CPU as it waits for other resources.

### Development (History) of OS
↗ [Development(History) of Operating Systems](Development(History)%20of%20Operating%20Systems.md)



## 🥅 OS Objectives & Functions
An OS is a program that controls the execution of application programs, and acts as an interface between applications and the computer hardware. It can be thought of as having three objectives:
- **Convenience**: An OS makes a computer more convenient to use.  
- **Efficiency**: An OS allows the computer system resources to be used in an efficient manner.
- **Ability to evolve**: An OS should be constructed in such a way as to permit the effective development, testing, and introduction of new system functions without interfering with service.

↗ More is at [Operating System Services](Operating%20System%20Services.md)

🤔 As an engineering project, ↗ **[Fault Tolerance](Fault%20Tolerance.md)** is also an eternal objective pursuing by generations of engineers.


### 🧠 Abstractions Provided by an Operating System (From User Perspective)
> The operating system has two primary purposes: (1) to protect the hardware from misuse by runaway applications and (2) to provide applications with simple and uniform mechanisms for manipulating complicated and often wildly different low-level hardware devices. (CSAPP)

The operating system achieves both goals via the fundamental abstractions shown in Figure 1.11: processes, virtual memory, and files. As this figure suggests
- files are abstractions for I/O devices, 
- virtual memory is an abstraction for both the main memory and disk I/O devices, and 
- processes are abstractions for the processor, main memory, and I/O devices.

![](../../../../../Assets/Pics/Screenshot%202023-10-13%20at%209.33.22PM.png)

#### 1️⃣ Processes
↗ [Processes Management (CPU + Main Memory Resource)](../Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource)/Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource).md)

#### 2️⃣ Virtual Memory Space
↗ [Main Memory](../../Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Main%20Memory/Main%20Memory.md)
↗ [Virtual Memory Space & Address Space](../Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/Virtual%20Memory%20(OS%20Software%20Level)/Virtual%20Memory%20Space%20&%20Address%20Space.md)

#### 3️⃣ Files
↗ [Network Sockets & RPC](../IO%20System/IO%20Generality%20(via%20Abstraction)/🛜%20Network%20Sockets%20&%20RPC/Network%20Sockets%20&%20RPC.md)
↗ [File System](../IO%20System/IO%20Generality%20(via%20Abstraction)/File%20System/File%20System.md)

↗ [IO Generality (via Abstraction)](../IO%20System/IO%20Generality%20(via%20Abstraction)/IO%20Generality%20(via%20Abstraction).md)

#### 4️⃣ Virtual Machine
The idea of a virtual machine was introduced by IBM in the 1960s, but it has become more prominent recently as a way to manage computers that must be able to run programs designed for multiple operating systems (such as Microsoft Windows, Mac OS X, and Linux) or different versions of the same operating system.

↗ [Virtualization Theory](../../🚀%20Virtualization%20Theory/Virtualization%20Theory.md)



## Morden Operating Systems
### 👉 Windows
![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%208.35.31%20PM.png)

More of Windows can be found at ↗ [Windows Architecture](../../../🥷🏼%20Operating%20System%20(Engineering)/Windows/📌%20Windows%20Basics/Windows%20Architecture.md).


### 👉 UNIX
> More of UNIX can be found at ↗ [UNIX Architecture](../../../🥷🏼%20Operating%20System%20(Engineering)/UNIX%20Family/📌%20UNIX%20Basics/UNIX%20Architecture.md)

![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%2010.06.15%20PM.png)


### 👉 Linux
More of Linux can be found at :

↗ [🍸 Linux Kernel](../../../🥷🏼%20Operating%20System%20(Engineering)/Linux%20(Derived%20From%20UNIX%20Family)/🔩%20Linux%20Kernel/🍸%20Linux%20Kernel.md)
↗ [Linux (Derived From UNIX Family)](../../../🥷🏼%20Operating%20System%20(Engineering)/Linux%20(Derived%20From%20UNIX%20Family)/Linux%20(Derived%20From%20UNIX%20Family).md)


### 👉 MacOS
![[../../../../../Assets/Pics/os X archi.jpeg]]

macOS is noted here ↗ [macOS Architecture](../../../🥷🏼%20Operating%20System%20(Engineering)/Apple/macOS%20(Derived%20From%20UNIX%20Family)/📌%20macOS%20Basics/macOS%20Architecture.md).


### 👉 Android
![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%2010.01.30%20PM.png)

![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%2010.05.49%20PM.png)

Android is noted here ↗ [Android Architecture](../../../🥷🏼%20Operating%20System%20(Engineering)/Android%20&%20AOSP/Android%20Architecture/Android%20Architecture.md).



## Ref
[History of UNIX]: https://en.wikipedia.org/wiki/History_of_Unix
[操作系统原理——第2章 操作系统概述]: https://blog.csdn.net/tangkcc/article/details/114852154
