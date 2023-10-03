# Memory Protection Mechanism

[TOC]



## Res


## Intro


## Ref

[缓冲区溢出与攻防博弈]: https://cloud.tencent.com/developer/article/2201574

微软的内存保护机制大致分为以下几种：
1. 堆栈缓冲区溢出检测保护 GS (编译器)
2. 安全结构化异常处理保护 Safe SEH
3. 堆栈 SEH 覆盖保护 SEHOP
4. 地址空间布局随机化保护 ASLR
5. 堆栈数据执行保护 DEP

