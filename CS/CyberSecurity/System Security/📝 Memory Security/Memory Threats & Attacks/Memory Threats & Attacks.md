# Memory Threats & Attacks

[TOC]



## Res
### Related Topics



## Intro



## Memory Security Vulnerabilities
### Buffer Overflow (Out-of-bounds Write/Read)


### Use After Free



## Ref
[缓冲区溢出与攻防博弈]: https://cloud.tencent.com/developer/article/2201574

微软的内存保护机制大致分为以下几种：
1. 堆栈缓冲区溢出检测保护 GS (编译器)
2. 安全结构化异常处理保护 Safe SEH
3. 堆栈 SEH 覆盖保护 SEHOP
4. 地址空间布局随机化保护 ASLR
5. 堆栈数据执行保护 DEP

[堆攻击手段整理总结]: https://tina2114.github.io/2020/04/15/堆攻击手段整理总结/

[内存攻击原理]: https://www.cnblogs.com/liuxgcn/p/11172487.html

**内存攻击** 是指攻击者利用软件安全漏洞，构造恶意输入，导致软件在处理数据流是出现非预期错误，将输入数据写入内存中的某些特定位置，从而劫持软件控制流，转而执行外部输入的指令代码，造成目标系统被获取远程控制权限或者被拒绝服务。

**内存攻击的表面原因** 软件编写错误，如过滤输入的条件设置缺陷、变量类型转换错误、逻辑判断错误、指针引用错误等。

**根本原因** 没有在内存中严格区分数据和指令。(不全面啊这概括。。。)

**缓冲区溢出** 程序缺乏对缓冲区的边界条件检查而引起的一种异常行为。通常是程序向缓冲区中写数据，但是内容超过了程序员设定的缓冲区边界，从而覆盖了相邻的内存区域，造成覆盖程序中的其他变量甚至影响控制流的敏感数据，造成程序的非预期行为。

一般根据缓冲区溢出的内存位置不同，将缓冲区溢出分为栈溢出 (Stack Overflow)和堆溢出 (Heap Overfolw)。

![](../../../../../Assets/Pics/Pasted%20image%2020231003142154.png)

[内存攻击小结]: https://blog.werner.wiki/memory-attack-summary/


