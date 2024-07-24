# Linux System Calls

[TOC]



## Res
### Related Topics
↗ [Program Execution /Interrupts](../../../../../../🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Instruction%20Execution/Interrupts%20(Software%20&%20Hardware).md)
↗ [ASM /Interrupts](../../../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/x86%20ISA%20Based%20ASM/⚡️%20ASM%20Advance/Interrupts/Interrupts.md)

↗ [System Calls](../../../../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource)/📌%20Processes%20Description%20&%20Control/System%20Calls/System%20Calls.md)
↗ [Privilege Level & Protection Ring](../../../../../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/📌%20ISA%20Basics/Privilege%20Level%20&%20Protection%20Ring.md)


### Learning Resources
📂 https://linasm.sourceforge.net/docs/index.php



## Intro
> 📎 https://linux-kernel-labs.github.io/refs/heads/master/lectures/syscalls.html




## Ref
[信号集 /信号掩码（阻塞信号传递）]: https://www.cnblogs.com/jingyg/p/5182001.html
[Linux信号（signal) 机制分析]: https://www.cnblogs.com/hoys/archive/2012/08/19/2646377.html

[👍 The Definitive Guide to Linux System Calls]: https://blog.packagecloud.io/the-definitive-guide-to-linux-system-calls/ 

(This article has been archived.)

**TL;DR**
This blog post explains how Linux programs call functions in the Linux kernel. It will outline several different methods of making systems calls, how to handcraft your own assembly to make system calls (examples included), kernel entry points into system calls, kernel exit points from system calls, glibc wrappers, bugs, and much, much more.

Here is a summary of the topics this blog post will cover,
- What is a system call?
- Prerequisite information
    - Hardware and software
    - User programs, the kernel, and CPU privilege levels
    - Interrupts
    - Model Specific Registers (MSRs)
- Calling system calls with assembly is a bad idea - A word of caution about calling system calls with assembly
- **Legacy system calls**
    - Using legacy system calls with your own assembly
    - Kernel-side: `int $0x80` entry point
    - Returning from a legacy system call with iret
- **Fast system calls**
    - 32-bit fast system calls `sysenter`/`sysexit`
        - `__kernel_vsyscall` internals
        - Using `sysenter` system calls with your own assembly
        - Kernel-side: `sysenter` entry point
        - Returning from a `sysenter` system call with `sysexit`
    - 64-bit fast system calls `syscall`/`sysret`
        - `syscall`/`sysret`
        - Using `syscall` system calls with your own assembly
        - Kernel-side: `syscall` entry point
        - Returning from a `syscall` system call with `sysret`
        - Calling a `syscall` semi-manually with `syscall(2)`
        - glibc `syscall` wrapper internals
- **Virtual system calls**
    - vDSO in the kernel
    - Locating the vDSO in memory
    - vDSO in `glibc`
    - `glibc` system call wrappers
- Interesting syscall related bugs
    - CVE-2010-3301
    - Android sysenter ABI breakage
- Conclusion

[👍 Linux syscall过程分析（万字长文）]: https://cloud.tencent.com/developer/article/1492374

[👍 linux系统调用和库函数调用的区别]: https://www.cnblogs.com/yanlingyin/archive/2012/04/23/2466141.html

|   |   |
|---|---|
|函数库调用|系统调用|
|在所有的ANSI C编译器版本中，C库函数是相同的|各个操作系统的系统调用是不同的|
|它调用函数库中的一段程序（或函数）|它调用系统内核的服务|
|与用户程序相联系|是操作系统的一个入口点|
|在用户地址空间执行|在内核地址空间执行|
|它的运行时间属于“用户时间”|它的运行时间属于“系统”时间|
|属于过程调用，调用开销较小|需要在用户空间和内核上下文环境间切换，开销较大|
|在C函数库libc中有大约300个函数|在UNIX中大约有90个系统调用|
|典型的C函数库调用：system fprintf malloc|典型的系统调用：chdir fork write brk；|
