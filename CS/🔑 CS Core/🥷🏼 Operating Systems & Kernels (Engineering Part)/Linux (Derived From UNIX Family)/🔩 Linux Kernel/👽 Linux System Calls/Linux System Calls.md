# Linux System Calls

[TOC]



## Res
### Related Topics
↗ [Program Execution /Interrupts](../../../../../../🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Instruction%20Execution/Interrupts%20(Software%20&%20Hardware).md)
↗ [ASM /Interrupts](../../../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/⚡️%20ASM%20Advance/Interrupts/Interrupts.md)

↗ [System Calls](../../../../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Processes%20&%20Automata%20Management%20(CPU%20+%20Main%20Memory%20Resource)/📌%20Processes%20Description%20&%20Control/System%20Calls/System%20Calls.md)
↗ [Privilege Level & Protection Ring](../../../../../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/📌%20ISA%20Basics/Privilege%20Level%20&%20Protection%20Ring.md)
↗ [System Core Function Libraries & C Standard Library (User Mode)](../../../../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/System%20Core%20Function%20Libraries%20&%20C%20Standard%20Library%20(User%20Mode).md)


### Learning Resources
📂 https://linasm.sourceforge.net/docs/index.php



## Intro
> 📎 https://linux-kernel-labs.github.io/refs/heads/master/lectures/syscalls.html

> 🔍 `man 2 syscalls`
> 🔍 `man 2 intro`


### System Calls and Library Wrapper Functions
> 🔍 `man 2 syscalls`
> 🔍 `man 2 intro`

A system call is an entry point into the Linux kernel. Usually, system calls are not invoked directly: instead, most system calls  have  corresponding  C  library  wrapper functions in `glibc` (or perhaps some other library) which  perform  the  steps  required  (e.g., trapping to kernel mode) in order to invoke the system call. Thus, making a system call looks the same as invoking a normal library function. Often, but not always, the name of the wrapper function is the same as the name of the system call that it invokes.  For example, `glibc` contains a function chdir() which invokes the underlying "chdir" system call.

Often the `glibc` wrapper function is quite thin, doing little work other than:
- copying arguments and the unique system call number to the registers where the kernel expects them;
- trapping to kernel mode, at which point the kernel does the real work of the system call;
- setting errno if the system call returns an error number when the kernel returns the CPU to user mode.

> Note: system calls indicate a failure by returning a negative error number to the caller on architectures without a separate error register/flag, as noted in `syscall(2)`; when this happens, the wrapper function negates the returned error number (to make it positive), copies it to errno, and returns -1 to the caller of the wrapper.
 
However, in a few cases, a wrapper function may do rather more than this, for example, performing some preprocessing of the  arguments  before  trapping to kernel mode, or post-processing of values returned by the system call.  Where this is the case, the manual pages in Section 2 generally try to note the details of both the (usually  GNU)  C  library API interface and the raw system call.  Most commonly, the main DESCRIPTION will focus on the C library interface, and differences for the system call are covered in the NOTES section.

> For example, nowadays there are (for reasons described below) two related system calls, truncate(2) and truncate64(2), and the `glibc` truncate() wrapper function checks which of those system calls are provided by the kernel and determines which should be employed.


### Linux System Calls List
> 🔍 `man 2 syscalls`


### 🤔 `syscall()` -- A Wrapper Function Invoking System Calls
> 🔍 `man syscall`

`syscall()` is a small library function that invokes the system call whose assembly language interface has the specified number with the specified arguments.  Employing `syscall()` is useful, for example, when invoking a  system  call that has no wrapper function in the C library. 

`syscall()` saves  CPU  registers  before  making the system call, restores the registers upon return from the system call, and stores any error returned by the system call in `errno(3)`.

Symbolic constants for system call numbers can be found in the header file `<sys/syscall.h>`.



## Linux System Calls on Different ISA Architecture & ABI
> ↗ [Procedure (Function) Call & Runtime Memory Layout](../../../../🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Procedure%20(Function)%20Call%20&%20Runtime%20Memory%20Layout/Procedure%20(Function)%20Call%20&%20Runtime%20Memory%20Layout.md)
> 🔍 `man syscall`



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

|                                 |                               |
| ------------------------------- | ----------------------------- |
| 函数库调用                           | 系统调用                          |
| 在所有的ANSI C编译器版本中，C库函数是相同的       | 各个操作系统的系统调用是不同的               |
| 它调用函数库中的一段程序（或函数）               | 它调用系统内核的服务                    |
| 与用户程序相联系                        | 是操作系统的一个入口点                   |
| 在用户地址空间执行                       | 在内核地址空间执行                     |
| 它的运行时间属于“用户时间”                  | 它的运行时间属于“系统”时间                |
| 属于过程调用，调用开销较小                   | 需要在用户空间和内核上下文环境间切换，开销较大       |
| 在C函数库libc中有大约300个函数             | 在UNIX中大约有90个系统调用              |
| 典型的C函数库调用：system fprintf malloc | 典型的系统调用：chdir fork write brk； |
