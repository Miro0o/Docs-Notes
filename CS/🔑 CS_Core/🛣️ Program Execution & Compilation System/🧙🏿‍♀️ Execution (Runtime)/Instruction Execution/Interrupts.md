# Interrupts

[TOC]



## Res
### Related Topics
↗ [ASM /Interrupts](../../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/⚡️%20ASM%20Advance/Interrupts/Interrupts.md)
↗ [System Calls](../../../🧬%20Computer%20System/Operating%20System%20(Theory)/Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource)/📌%20Processes%20Description%20&%20Control/System%20Calls.md)



## Overview
![protection_ring.excalidraw | 800](../../../../../../Assets/Illustrations/Computer%20System/protection_ring.excalidraw.md)

Interrupts can be triggered by
1. I/O requests
2. Invalid instruction encountered 
3. Arithmetic errors (e.g., division by 0)  
4. Arithmetic underflow or overflow  
5. Hardware malfunction (e.g., memory parity error)
6. Page faults
7. Miscellaneous

An interrupt 
- can be initiated by the user or the system
- can be maskable (disabled or ignored) or nonmaskable (a high-priority interrupt that cannot be disabled and must be acknowledged)
- can occur within or between instructions
- may be synchronous (occurring at the same place every time a program is executed) or asynchronous (occurring unexpectedly)
- can result in the program terminating or continuing execution once the interrupt is handled



## Ref
操作系统 | 中断 & 系统调用浅析 - 彭旭锐的文章 - 知乎 https://zhuanlan.zhihu.com/p/289410487
