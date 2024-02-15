# ASM (Assembly Languages)

[TOC]



## Res
### Background Knowledges
↗ [Instruction Set Architecture (ISA)](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)/Instruction%20Set%20Architecture%20(ISA).md)
↗ [Instruction Execution](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)/📌%20Instruction%20Basics/Instruction%20Execution/Instruction%20Execution.md)


### Where to learn ...
🏫 [Compilation Principles](../../🛣️%20Program%20Execution%20&%20Compilation%20System/🚮%20Program%20Language%20Translation%20(Compile-time)/Program%20Language%20Translation%20(Compile-time).md)
📖 [汇编语言]: "王爽"
📖 C++反汇编与逆向分析技术揭秘，钱林松，张延清

[阮一峰 一笔而过的入门介绍](http://www.ruanyifeng.com/blog/2018/01/assembly-language-primer.html)
- [Introduction to reverse engineering and Assembly](https://kakaroto.homelinux.net/2017/11/introduction-to-reverse-engineering-and-assembly/)
- [x86 Assembly Guide](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html)
	
[函数调用](https://zhuanlan.zhihu.com/p/24129384)
[B站，小甲鱼](https://www.bilibili.com/video/BV1zW411n79C?share_source=copy_web)
[W3school](https://www.w3cschool.cn/assembly/assembly-establish.html)

[Assembly Part 1 - Let's Learn Assembly!](https://www.section.io/engineering-education/assembly-part-1/)
[Programming in assembly language tutorial](https://github.com/mschwartz/assembly-tutorial)

#### Tutorials
[Welcome to x86asm.net](http://x86asm.net/index.html)


### Learn it by doing it!
#### Tools 
↗ [Program Debuggers](../🐛%20Programming%20Tools%20Chain/Program%20Debuggers.md)


#### Projs
↗ [Cybersecurity - Malicious Code Analysis](../../../CyberSecurity/🥇%20Best%20Practice/🪆%20Reverse%20Engineering%20&%20System%20&%20Binary/👣%20Malicious%20Code%20Analysis/Malicious%20Code%20Analysis.md)

↗ [CTF - RE&BE](../../../CyberSecurity/🥇%20Best%20Practice/👻%20CTF/RE%20&%20BE/RE%20&%20BE.md)

↗ [Cybersecurity - Reverse Engineering](../../../CyberSecurity/🥇%20Best%20Practice/🪆%20Reverse%20Engineering%20&%20System%20&%20Binary/Reverse%20Engineering%20&%20System%20&%20Binary.md)



## Intro
![](../../../../Assets/Pics/Pasted%20image%2020230227223106.png)
<small>Assembly Language in the Computer Programming Language Hierarchy</small>


> Assembly language is human-readable characters encoding of binary machine code language!
> ↗ [Machine Code](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)/📌%20Instruction%20Basics/Instruction%20Levels/Machine%20Code.md)


### What is ASM and why is it?
#### History of ASM
#TODO 



### How ASM works?
>💡 A little bit computer organization & architecture knowledge needed!
>
>🔗 check out ↗ [Computer Architecture](../../🧬%20Computer%20System/Computer%20Architecture/Computer%20Architecture.md) for details.
> Pay more look at ↗ [von Neumann Based Microarchitecture](../../🧬%20Computer%20System/Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/von%20Neumann%20Based%20Microarchitecture.md), for it's the basics for leaning deep ASM.
> 
> ASM is running at system software level, so it is implemented at OS. More about this at ↗ [OS Programming Foundation](../../🥷🏼%20Operating%20System%20(Engineering)/📟%20OS%20Level%20Programming%20&%20System%20Level%20Library/OS%20Programming%20Foundation.md).

↗ [OS Programming Foundation](../../🥷🏼%20Operating%20System%20(Engineering)/📟%20OS%20Level%20Programming%20&%20System%20Level%20Library/OS%20Programming%20Foundation.md)
↗ [8086 ASM](x86%20ISA%20Based%20ASM/8086%20ASM/8086%20ASM.md)


### ASM Instructions
> 汇编语言发展至今，由以下 3 类指令组成:
> 
> 1. 汇编指令:机器码的助记符，有对应的机器码。
> 2. 伪指令:没有对应的机器码，由编译器执行，计算机并不执行。
> 3. 其他符号:如 +、-、\*、/ 等，由编译器识别，没有对应的机器码。
> 
> 汇编语言的核心是汇编指令，它决定了汇编语言的特性。



## Ref
