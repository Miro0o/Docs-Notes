# Program Execution & Compilation System

[TOC]



## Res
### Related Topics
↗ [Instruction Set Architecture (ISA)](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)/Instruction%20Set%20Architecture%20(ISA).md)
↗ [Instruction Basics](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)/📌%20Instruction%20Basics/Instruction%20Basics.md)
↗ [Operating System (Theory)](../../🧬%20Computer%20System/Operating%20System%20(Theory)/Operating%20System%20(Theory).md)

### Learning Resources
📖 CSAPP: Computer System: A Programmer's Perspective
↗ [Intro to CS](../../../🗺%20CS_Overview/💋%20Intro%20to%20CS/Intro%20to%20CS.md)

📖 程序员的自我修养：编译，链接，库



## Intro
### Compilation Systems from Programmers' Perspective
> Quote from CSAPP

However, there are some important reasons why programmers need to understand how compilation systems work:
- **Optimizing program performance**. Modern compilers are sophisticated tools that usually produce good code. As programmers, we do not need to know the inner workings of the compiler in order to write efficient code. However, in order to make good coding decisions in our C programs, we do need a basic understanding of machine-level code and how the compiler translates different C statements into machine code.
	- For example, is a switch statement always more efficient than a sequence of if-else statements? How much overhead is incurred by a function call? Is a while loop more efficient than a for loop? Are pointer references more efficient than array indexes? Why does our loop run so much faster if we sum into a local variable instead of an argument that is passed by reference? How can a function run faster when we simply rearrange the parentheses in an arithmetic expression?
- **Understanding link-time errors**. In our experience, some of the most perplexing programming errors are related to the operation of the linker, especially when you are trying to build large software systems. 
	- For example, what does it mean when the linker reports that it cannot resolve a reference? What is the difference between a static variable and a global variable? What happens if you define two global variables in different C files with the same name? What is the difference between a static library and a dynamic library? Why does it matter what order we list libraries on the command line? And scariest of all, why do some linker-related errors not appear until run time? 
- **Avoiding security holes**. For many years, buffer overflow vulnerabilities have accounted for many of the security holes in network and Internet servers. These vulnerabilities exist because too few programmers understand the need to carefully restrict the quantity and forms of data they accept from untrusted sources. A first step in learning secure programming is to understand the consequences of the way data and control information are stored on the program stack.



## Working Process of Compilation Systems
![](../../../../../../Assets/Pics/Screenshot%202023-05-22%20at%209.50.58%20PM.png)
<small>A examplary illustration of the compilation, linking, loading & execution process</small>

### 0️⃣ Information, Encoding, Computer/Digital System Data Representations & Computer File Formats
↗ [Data Representations & Storage in CS](../../🧬%20Computer%20System/😤%20Number,%20Data%20and%20Math%20in%20Digital%20Systems/Data%20Representations%20&%20Storage%20in%20CS.md)
↗ [Encodings in Digital Systems](../../🧬%20Computer%20System/😤%20Number,%20Data%20and%20Math%20in%20Digital%20Systems/Encodings%20in%20Digital%20Systems.md)
↗ [Cryptograph /Encoding](../../../CyberSecurity/🚬%20Cryptology/🤐%20Cryptography/Encoding.md)

↗ [Reliable Data Transfer (RDT)](../../🏎️%20Computer%20Networking%20and%20Communication/📌%20Computer%20Networking%20Basics/Reliable%20Data%20Transfer%20(RDT)/Reliable%20Data%20Transfer%20(RDT).md)
↗ [Information Theory](../../../🧮%20Math%20&%20Theoretical%20Computer%20Science%20(TCS)/Information%20Theory/Information%20Theory.md)

↗ [OS /File System](../../🧬%20Computer%20System/Operating%20System%20(Theory)/IO%20System/IO%20Generality%20(via%20Abstraction)/File%20System/File%20System.md)
↗ [OS /Linux /Linux File Formats](../../🥷🏼%20Operating%20System%20(Tech)/Linux%20(Derived%20From%20UNIX%20Family)/📌%20Linux%20Basics/Linux%20IO%20&%20Files%20Management/Linux%20File%20System/Linux%20File%20Types%20&%20Formats.md)


### 0️⃣ (Compiled) Programming Languages
↗ [Programming Languages in a Nutshell](../Programming%20Languages%20in%20a%20Nutshell.md)
↗ [Compiled Languages](../Compiled%20Languages/Compiled%20Languages.md)
↗ [Interpreted Languages](../Interpreted%20Languages/Interpreted%20Languages.md)
↗ [ASM (Assembly Languages)](../ASM%20(Assembly%20Languages)/ASM%20(Assembly%20Languages).md)

↗ [DSL(Domain Specific Languages) & GPL(General Purpose Languages)](../DSL(Domain%20Specific%20Languages)%20&%20GPL(General%20Purpose%20Languages)/DSL(Domain%20Specific%20Languages)%20&%20GPL(General%20Purpose%20Languages).md)
↗ [Codec & Media Formats & Standards](../Codec%20&%20Media%20Formats%20&%20Standards/Codec%20&%20Media%20Formats%20&%20Standards.md)

↗ [Automata Theory and Formal Language Theory](../../../🧮%20Math%20&%20Theoretical%20Computer%20Science%20(TCS)/🤼‍♀️%20Mathematical%20Logics/😶‍🌫️%20Theory%20of%20Computation/Automata%20Theory%20and%20Formal%20Language%20Theory/Automata%20Theory%20and%20Formal%20Language%20Theory.md)
↗ [Natural Language Processing (NLP)](../../../Artificial%20Intelligence/Natural%20Language%20Processing%20(NLP)/Natural%20Language%20Processing%20(NLP).md)


### 1️⃣ Compilation (Compile-time)
↗ [Compilation Phase](🚮%20Program%20Language%20Translation%20(Compile-time%20&%20Link-time)/Compilation%20Phase/Compilation%20Phase.md)
↗ [Assembly Phase](🚮%20Program%20Language%20Translation%20(Compile-time%20&%20Link-time)/Assembly%20Phase/Assembly%20Phase.md)

↗ [Reverse Engineering & System & Binary](../../../CyberSecurity/🥇%20Best%20Practice/🪆%20Reverse%20Engineering%20&%20System%20&%20Binary/Reverse%20Engineering%20&%20System%20&%20Binary.md)


### 2️⃣ Link & Library (Link-time)
↗ [Linking Phase](🚮%20Program%20Language%20Translation%20(Compile-time%20&%20Link-time)/Linking%20Phase/Linking%20Phase.md)


### 3️⃣ Load (Loadtime)


### 4️⃣ Execution (Runtime)
↗ [ISA /Instruction Basics](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)/📌%20Instruction%20Basics/Instruction%20Basics.md)
↗ [ISA /Instruction Execution](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)/📌%20Instruction%20Basics/Instruction%20Execution/Instruction%20Execution.md)

↗ [von Neumann Based Microarchitecture /Memory Access](../../🧬%20Computer%20System/Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Main%20Memory/Memory%20Access.md)
↗ [System Security /Memory Attack](../../../CyberSecurity/System%20Security/Operating%20System%20Security/Memory%20Attack/Memory%20Attack.md)

↗ [Execution (Runtime)](🧙🏿‍♀️%20Execution%20(Runtime)/Execution%20(Runtime).md)
↗ [Runtimes & SDKs](../🛠️%20Programming%20Tools%20Chain/🚠%20Runtimes%20&%20SDKs/Runtimes%20&%20SDKs.md)

↗ [Reverse Engineering & System & Binary](../../../CyberSecurity/🥇%20Best%20Practice/🪆%20Reverse%20Engineering%20&%20System%20&%20Binary/Reverse%20Engineering%20&%20System%20&%20Binary.md)
↗ [Anti-Reverse & Anti-Disassembly Engineering](../../../CyberSecurity/🥇%20Best%20Practice/🪆%20Reverse%20Engineering%20&%20System%20&%20Binary/🤺%20Anti-Reverse%20&%20Anti-Disassembly%20Engineering/Anti-Reverse%20&%20Anti-Disassembly%20Engineering.md)
↗ [Malicious Code Analysis](../../../CyberSecurity/🥇%20Best%20Practice/🪆%20Reverse%20Engineering%20&%20System%20&%20Binary/👣%20Malicious%20Code%20Analysis/Malicious%20Code%20Analysis.md)
↗ [Vulnerability Analysis](../../../CyberSecurity/🥇%20Best%20Practice/Vulnerability%20Analysis/Vulnerability%20Analysis.md)

↗ [System Security](../../../CyberSecurity/System%20Security/System%20Security.md)

![](../../../../../../../Assets/Pics/Screenshot%202023-03-03%20at%209.05.51%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-03-21%20at%209.12.25%20PM.png)
<small>Instruction Processing Level</small>



## Ref
[Execution (computing) | Wikipedia]: https://en.wikipedia.org/wiki/Execution_(computing)

程序的编译、装载与链接 - piginzoo的文章 - 知乎 https://zhuanlan.zhihu.com/p/139026433
[《链接、装载与库》 阅读笔记 (1)- 基本概念与静态链接]: https://wulc.me/2020/05/31/《链接、装载与库》阅读笔记(1)-基本概念与静态链接/

[高级语言的编译：链接及装载过程介绍]: https://tech.meituan.com/2015/01/22/linker.html
[《程序员的自我修养》——全书思维导图（上）]: https://www.zhihu.com/tardis/zm/art/111682188?source_id=1003