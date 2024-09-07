# Memory Protection Mechanisms

[TOC]



## Res
### Related Topics
↗ [Win Memory Protection Mechanism](../../Operating%20System%20Security/🪟%20Windows%20Security/Windows%20Security%20Mechanisms/📌%20Win%20Memory%20Protection%20Mechanism/Win%20Memory%20Protection%20Mechanism.md)
↗ [Linux Memory Protection Mechanism](../../Operating%20System%20Security/🐏%20Linux%20Security/Linux%20Kernel%20Security%20Mechanisms/📌%20Linux%20Memory%20Protection%20Mechanism/Linux%20Memory%20Protection%20Mechanism.md)

↗ [Programming Methodology and Languages](../../../../🔑%20CS%20Core/👩‍💻%20Programming%20Methodology%20and%20Languages/Programming%20Methodology%20and%20Languages.md)
↗ [Compilation & Program Loading Tools](../../../../🔑%20CS%20Core/👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Compilation%20&%20Program%20Loading%20Tools/Compilation%20&%20Program%20Loading%20Tools.md)
↗ [Operating System Security](../../Operating%20System%20Security/Operating%20System%20Security.md)



## Intro


## Ref

[缓冲区溢出与攻防博弈]: https://cloud.tencent.com/developer/article/2201574

微软的内存保护机制大致分为以下几种：
1. 堆栈缓冲区溢出检测保护 GS (编译器)
2. 安全结构化异常处理保护 Safe SEH
3. 堆栈 SEH 覆盖保护 SEHOP
4. 地址空间布局随机化保护 ASLR
5. 堆栈数据执行保护 DEP

