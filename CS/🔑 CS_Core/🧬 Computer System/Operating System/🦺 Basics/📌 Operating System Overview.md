# Operating System Overview

[TOC]



## 🥅 OS Objectives & Functions
An OS is a program that controls the execution of application programs, and acts as an interface between applications and the computer hardware. It can be thought of as having three objectives:

- **Convenience**: An OS makes a computer more convenient to use.  
- **Efficiency**: An OS allows the computer system resources to be used in an efficient manner.
- **Ability to evolve**: An OS should be constructed in such a way as to permit the effective development, testing, and introduction of new system functions without interfering with service.

↗ More is at [Operating System Services](Operating%20System%20Services.md)

🤔 As an engineering project, ↗ **[Fault Tolerance](Fault%20Tolerance.md)** is also an eternal objective pursuing by generations of engineers.



## Development of OS
↗ [Development of OS](Development%20of%20OS.md)



## Main Operating Systems
### Windows
![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%208.35.31%20PM.png)

More of Windows can be found at ↗ [Windows Architecture](../../../🥷🏼%20OS/Windows/Windows%20Basics/Windows%20Architecture.md).


### UNIX

> More of UNIX can be found at ↗ [UNIX Architecture](../../../🥷🏼%20OS/UNIX/UNIX%20Basics/UNIX%20Architecture.md)


![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%2010.06.15%20PM.png)

![](../../../../../Assets/Pics/Pasted%20image%2020230302220507.png)

![](../../../../../Assets/Pics/Pasted%20image%2020230302220447.png)

#### Traditional UNIX Systems
[VAHA96] uses the term "traditional UNIX" to refer to System V Release 3 (SVR3), 4.3BSD, and earlier versions. The following general statements may be made about a traditional UNIX system. 

Traditional UNIX is designed to run on a single processor, and lacks the ability to protect its data structures from concurrent access by multiple processors. Its kernel is not very versatile, supporting a single type of file system, process scheduling policy, and executable file format. The traditional UNIX kernel is not designed to be extensible and has few facilities for code reuse. The result is that, as new features were added to the various UNIX versions, much new code had to be added, yielding a bloated and unmodular kernel.

![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%209.26.30%20PM.png)


#### Modern UNIX Systems
![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%209.28.48%20PM.png)



### Linux

More of Linux can be found at :

[🍸 Linux Kernel](../../../🥷🏼%20OS/Linux/🔩%20Kernel/🍸%20Linux%20Kernel.md)
[Linux](../../../🥷🏼%20OS/Linux/Linux.md)


### MacOS

![[os X archi.jpeg]]

macOS is noted here ↗ [macOS Architecture](../../../🥷🏼%20OS/Apple/macOS/macOS%20Basics/macOS%20Architecture.md).


### Anroid

![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%2010.01.30%20PM.png)

![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%2010.05.49%20PM.png)


Android is noted here ↗ [Android Architecture](../../../🥷🏼%20OS/Android/Android%20Architecture/Android%20Architecture.md).


## Ref
[History of UNIX]: https://en.wikipedia.org/wiki/History_of_Unix
[操作系统原理——第2章 操作系统概述]: https://blog.csdn.net/tangkcc/article/details/114852154
