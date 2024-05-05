# Processes Description & Control

[TOC]



## Res



## Intro
### Context Switch
At any point in time, a uniprocessor system can only execute the code for a single process. When the operating system decides to transfer control from the current process to some new process, it performs a context switch by saving the context of the current process, restoring the context of the new process, and hen passing control to the new process. The new process picks up exactly where it left off.

![](../../../../../../Assets/Pics/Screenshot%202023-10-13%20at%208.41.52PM.png)

As Figure 1.12 indicates, the transition from one process to another is man- aged by the operating system kernel. The kernel is the portion of the operating system code that is always resident in memory. When an application program requires some action by the operating system, such as to read or write a file, it executes a special system call instruction, transferring control to the kernel. The kernel then performs the requested operation and returns back to the application program. Note that the kernel is not a separate process. Instead, it is a collection of code and data structures that the system uses to manage all the processes.



## Ref
[进程的状态及转换 两/三/五态模型、挂起、进程控制块]: https://www.orzzone.com/process-state-transition.html
[用户态与内核态之间切换详解「通俗易懂」]: https://cloud.tencent.com/developer/article/2131401
[Java：线程的六种状态及转化]: https://www.cnblogs.com/summerday152/p/12288671.html

[「操作系统」进程管理（二）]: https://www.cnblogs.com/leesf456/p/5413517.html

