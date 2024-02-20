# Fast System Calls

[TOC]



## Res


## Intro
> 🔗 https://blog.packagecloud.io/the-definitive-guide-to-linux-system-calls/

The legacy method seems pretty reasonable, but there are newer ways to trigger a system call which don’t involve a software interrupt and are [much faster](https://lkml.org/lkml/2002/12/9/13) than using a software interrupt.

Each of the two faster methods is comprised of two instructions. One to enter the kernel and one to leave. Both methods are described in the Intel CPU documentation as “Fast System Call”.

Unfortunately, Intel and AMD implementations have some disagreement on which method is valid when a CPU is in 32bit or 64bit mode.

In order to maximize compatibility across both Intel and AMD CPUs:
- On 32bit systems use: `sysenter` and `sysexit`.
- On 64bit systems use: `syscall` and `sysret`.



## Ref

