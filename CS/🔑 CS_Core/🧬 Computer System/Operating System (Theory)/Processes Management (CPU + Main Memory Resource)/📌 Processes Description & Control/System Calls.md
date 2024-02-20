# System Calls

[TOC]



## Res
### Related Topics
↗ [Privilege Level & Protection Ring](../../../Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/📌%20ISA%20Basics/Privilege%20Level%20&%20Protection%20Ring.md)
↗ [Instruction Execution/ Interrupts](../../../../🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Execution%20(Runtime)/Instruction%20Execution/Interrupts.md)
↗ [ASM /Interrupts](../../../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/⚡️%20ASM%20Advance/Interrupts/Interrupts.md)

↗ [CPU (Central Processing Unit)](../../../Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)/Computer%20Processors/Microprocessors%20Unit%20(MPU)/CPU%20(Central%20Processing%20Unit)/CPU%20(Central%20Processing%20Unit).md)
↗ [Operating System Kernel](../../../../🥷🏼%20Operating%20System%20(Engineering)/📟%20System%20Level%20Programming/🫀%20Operating%20System%20Kernel/Operating%20System%20Kernel.md)
↗ [Linux System Calls](../../../../🥷🏼%20Operating%20System%20(Engineering)/Linux%20(Derived%20From%20UNIX%20Family)/🔩%20Linux%20Kernel/👽%20Linux%20System%20Calls/Linux%20System%20Calls.md) ⭐



## Intro
![protection_ring.excalidraw | 800](../../../../../../Assets/Illustrations/Computer%20System/protection_ring.excalidraw.md)


### Privilege Levels /Protection Ring
> ↗ [Privilege Level & Protection Ring](../../../Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/📌%20ISA%20Basics/Privilege%20Level%20&%20Protection%20Ring.md)


![](../../../../../../../Assets/Pics/Pasted%20image%2020240217173550.png)
<small>Protection ring of Intel x86 CPU. Usually ring 0 is kernel space, ring 3 is user space.</small>


### System Calls & Interrupts
> ↗ [Program Execution /Interrupts](../../../../🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Execution%20(Runtime)/Instruction%20Execution/Interrupts.md)
> ↗ [ASM /Interrupts](../../../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/⚡️%20ASM%20Advance/Interrupts/Interrupts.md)
> ↗ [Operating System Kernel](../../../../🥷🏼%20Operating%20System%20(Engineering)/📟%20System%20Level%20Programming/🫀%20Operating%20System%20Kernel/Operating%20System%20Kernel.md)

![](../../../../../../../Assets/Pics/Pasted%20image%2020240217141037.png)
<small>System calls in different kernel design.</small>



## Ref
[👍 系统调用和库函数有什么区别？ - 果冻虾仁的回答 - 知乎]: https://www.zhihu.com/question/19930018/answer/1329177990

[👍 The Definitive Guide to Linux System Calls]: https://blog.packagecloud.io/the-definitive-guide-to-linux-system-calls/
[👍 Linux syscall过程分析（万字长文）]: https://cloud.tencent.com/developer/article/1492374
