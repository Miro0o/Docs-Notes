# ASM (Assembly Languages)

[TOC]



## Res
### Related Topics
↗ [Instruction Set Architecture (ISA) & Processor Architecture](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture.md)
↗ [CPU (Central Processing Unit)](../../🧬%20Computer%20System/Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/🚦%20Computer%20Processors%20&%20Logic%20Chips/📌%20Microprocessors%20Unit%20(MPU)/CPU%20(Central%20Processing%20Unit)/CPU%20(Central%20Processing%20Unit).md)
↗ [Register](../../🧬%20Computer%20System/Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/🚦%20Computer%20Processors%20&%20Logic%20Chips/📌%20Microprocessors%20Unit%20(MPU)/CPU%20(Central%20Processing%20Unit)/📌%20Basic%20CPU%20Components/Register.md)

↗ [C-Based Languages](../Compiled%20Languages/👔%20C-Based%20Languages/C-Based%20Languages.md)
↗ [C & CPP](../Compiled%20Languages/👔%20C-Based%20Languages/🥏%20C%20&%20CPP/C%20&%20CPP.md)

↗ [Program Execution (Runtime)](../../🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Program%20Execution%20(Runtime).md)
↗ [Instruction Execution](../../🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Instruction%20Execution/Instruction%20Execution.md)

↗ [Debuggers & Disassemblers & Decompilers](../🛠️%20Programming%20Tools%20Chain/Debuggers%20&%20Disassemblers%20&%20Decompilers/Debuggers%20&%20Disassemblers%20&%20Decompilers.md)
↗ [Compilation & Program Loading Tools](../🛠️%20Programming%20Tools%20Chain/Compilation%20&%20Program%20Loading%20Tools/Compilation%20&%20Program%20Loading%20Tools.md)
- ↗ [Assemblers](../🛠️%20Programming%20Tools%20Chain/Compilation%20&%20Program%20Loading%20Tools/Assemblers.md)

↗ [Cybersecurity - Malicious Code Analysis](../../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Binary%20Engineering%20&%20Software%20Analysis/Malicious%20Code%20Detection%20&%20Software%20Analysis/Malicious%20Code%20Detection%20&%20Software%20Analysis.md)
↗ [CTF - RE&BE](../../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/CTF%20&%20AWD/RE%20&%20BE/RE%20&%20BE.md)
↗ [Cybersecurity - Reverse Engineering](../../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Binary%20Engineering%20&%20Software%20Analysis/Binary%20Engineering%20&%20Software%20Analysis.md)


### Learning Resources
🏫 [Compilation Principles](../../🛣️%20Program%20Execution%20&%20Compilation%20System/🚮%20Program%20Language%20Translation%20&%20Compilation%20Theory%20(Compile-time)/Program%20Language%20Translation%20&%20Compilation%20Theory%20(Compile-time).md)
📖 [汇编语言]: "王爽"
📖 C++反汇编与逆向分析技术揭秘，钱林松，张延清

📖《x86汇编语言：从实模式到保护模式》李忠、王小波、余洁

[阮一峰 一笔而过的入门介绍](http://www.ruanyifeng.com/blog/2018/01/assembly-language-primer.html)
- [Introduction to reverse engineering and Assembly](https://kakaroto.homelinux.net/2017/11/introduction-to-reverse-engineering-and-assembly/)
- [x86 Assembly Guide](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html)

[函数调用](https://zhuanlan.zhihu.com/p/24129384)
[B站，小甲鱼](https://www.bilibili.com/video/BV1zW411n79C?share_source=copy_web)
[W3school](https://www.w3cschool.cn/assembly/assembly-establish.html)

[Assembly Part 1 - Let's Learn Assembly!](https://www.section.io/engineering-education/assembly-part-1/)
[Programming in assembly language tutorial](https://github.com/mschwartz/assembly-tutorial)

🤔 [Welcome to x86asm.net](http://x86asm.net/index.html)



## Intro
![](../../../../Assets/Pics/Pasted%20image%2020230227223106.png)
<small>Assembly Language in the Computer Programming Language Hierarchy</small>

> Assembly language is human-readable characters encoding of binary machine code language!
> ↗ [Instruction Set Architecture (ISA) & Processor Architecture](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture.md)
> ↗ [Machine Code](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/📌%20ISA%20Basics/📌%20Instruction%20Basics/Instruction%20Levels/Machine%20Code.md)
> ↗ [FAQ/ 👉 ISA 🆚 ASM ? Differences & Commons 🤔](../../🧬%20Computer%20System/Computer%20Architecture/FAQ.md#👉%20ISA%20🆚%20ASM%20?%20Differences%20&%20Commons%20🤔)


### What is ASM and why is it?
> ↗ [FAQ/ 👉 ISA 🆚 ASM ? Differences & Commons 🤔](../../🧬%20Computer%20System/Computer%20Architecture/FAQ.md#👉%20ISA%20🆚%20ASM%20?%20Differences%20&%20Commons%20🤔)

> 🤖 Contents below are AI-generated (Chat-gpt4-mini) 

**What is Assembly Language (ASM)?**
- **Assembly Language (ASM)** is a low-level programming language that provides a human-readable representation of the machine code defined by an ISA. Each instruction in an assembly language corresponds directly to a machine instruction supported by the ISA.
- **Key Aspects of ASM:**
	- **Mnemonic Representation**: Assembly language uses mnemonics (e.g., `ADD`, `MOV`, `JMP`) to represent the machine instructions defined by the ISA. These mnemonics are more readable than binary code.
	- **Syntax and Directives**: ASM includes a specific syntax and directives (e.g., `.data`, `.text`) to organize code, declare data sections, and manage assembly-time operations like macros and constants.
	- **Labels and Symbols**: ASM allows the use of labels and symbols to make code more understandable and to manage control flow (e.g., loop labels, function names).
	- **Assembler**: An assembler is a tool that translates assembly language code into the corresponding machine code that the processor can execute.
#### History of ASM


### 🤔 How is High-Level Language Translated into ASM?
↗ [Compilation Phase](../../🛣️%20Program%20Execution%20&%20Compilation%20System/🚮%20Program%20Language%20Translation%20&%20Compilation%20Theory%20(Compile-time)/Compilation%20Phase/Compilation%20Phase.md)
↗ [Debuggers & Disassemblers & Decompilers](../🛠️%20Programming%20Tools%20Chain/Debuggers%20&%20Disassemblers%20&%20Decompilers/Debuggers%20&%20Disassemblers%20&%20Decompilers.md)


### 🤔 How is ASM Translated into Machine Code?
↗ [Instruction Set Architecture (ISA) & Processor Architecture](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture.md)
↗ [8086 ASM (16 bit)](x86%20ISA%20Based%20ASM/8086%20ASM%20(16%20bit).md)
↗ [Assemblers](../🛠️%20Programming%20Tools%20Chain/Compilation%20&%20Program%20Loading%20Tools/Assemblers.md)

**示例：MIPS 指令到机器码**
(MIPS指令集简单，指令长度固定，比较好理解。但是不是所有指令集都是如此。)

MIPS 是一组由 MIPS 技术公司在 80 年代中期设计出来的 CPU 指令集。就在最近，MIPS 公司把整个指令集和芯片架构都完全开源了。MIPS 指令集管网：
https://www.mips.com/mipsopen/

![](../../../../Assets/Pics/Pasted%20image%2020240904105805.png)
<small>MIPS 指令集格式</small>

MIPS 的指令是一个 32 位的整数，高 6 位叫操作码（Opcode），也就是代表这条指令具体是一条什么样的指令，剩下的 26 位有三种格式，分别是 R、I 和 J。
- **R 指令**：一般用来做算术和逻辑操作，里面有读取和写入数据的寄存器的地址。如果是逻辑位移操作，后面还有位移操作的位移量，而最后的功能码，则是在前面的操作码不够的时候，扩展操作码表示对应的具体指令的。
- **I 指令**：则通常是用在数据传输、条件分支，以及在运算的时候使用的并非变量还是常数的时候。这个时候，没有了位移量和操作码，也没有了第三个寄存器，而是把这三部分直接合并成了一个地址值或者一个常数。
- **J 指令**：跳转指令，高 6 位之外的 26 位都是一个跳转后的地址。


**示例：add 指令**
```text
add $t0,$s2,$s1
```

add 对应的 MIPS 指令里 opcode 是 0，rs 代表第一个寄存器 s1 的地址是 17，rt 代表第二个寄存器 s2 的地址是 18，rd 代表目标的临时寄存器 t0 的地址，是 8。因为不是位移操作，所以位移量是 0。把这些数字拼在一起，就变成了一个 MIPS 的加法指令。

为了读起来方便，我们一般把对应的二进制数，用 16 进制表示出来。在这里，也就是 0X02324020。这个数字也就是这条指令对应的机器码。

![](../../../../Assets/Pics/Pasted%20image%2020240904105830.png)
<small>add 指令表示方法</small>

```
000000 10001 10010 01000 00000 100000       // add MIPS指令格式
= 0000 0010 0011 0010 0100 0000 0010 0000   // add 二进制表示
= 0X02324020                                // add 十六进制表示
```



## Ref
