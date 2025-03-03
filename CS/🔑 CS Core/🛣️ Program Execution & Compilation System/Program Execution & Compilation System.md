# Program Execution & Compilation System

[TOC]



## Res
### Related Topics
↗ [ASM (Assembly Languages)](../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/ASM%20(Assembly%20Languages).md)
↗ [Instruction Set Architecture (ISA) & Processor Architecture](../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture.md)
↗ [Instruction Basics](../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/📌%20ISA%20Basics/📌%20Instruction%20Basics/Instruction%20Basics.md)
↗ [Operating System & OS Kernel (Theory Part)](../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part).md)
- ↗ [System Software Engineering](../../Software%20Engineering/👇%20System%20Software%20Engineering/System%20Software%20Engineering.md)

↗ [Program, Computer, and Automation](../../🗺%20CS%20Overview/Program,%20Computer,%20and%20Automation.md)

↗ [SCA (Static Code Analysis)](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Software%20Analysis%20&%20Binary%20Engineering/📌%20Software%20Analysis%20Basics%20Methodologies/📌%20SCA%20(Static%20Code%20Analysis)/SCA%20(Static%20Code%20Analysis).md)
↗ [DCA (Dynamic Code Analysis)](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Software%20Analysis%20&%20Binary%20Engineering/📌%20Software%20Analysis%20Basics%20Methodologies/📌%20DCA%20(Dynamic%20Code%20Analysis)/DCA%20(Dynamic%20Code%20Analysis).md)
↗ [Programming Methodology and Languages](../👩‍💻%20Programming%20Methodology%20and%20Languages/Programming%20Methodology%20and%20Languages.md)
↗ [Application Runtimes & SDKs](../👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/🚠%20Application%20Runtimes%20&%20SDKs/Application%20Runtimes%20&%20SDKs.md)
↗ [Cloud Runtime](../../Software%20Engineering/☁️%20Cloud%20Computing%20&%20Cloud%20Native/Cloud%20Operating%20System%20&%20Platform%20(System%20Level%20Engineering)/Cloud%20Runtime/Cloud%20Runtime.md)

↗ [OS Processes & Automata Management (CPU + Main Memory Resource)](../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Processes%20&%20Automata%20Management%20(CPU%20+%20Main%20Memory%20Resource)/OS%20Processes%20&%20Automata%20Management%20(CPU%20+%20Main%20Memory%20Resource).md)
↗ [Firmware and Computer (OS) Booting](../🧬%20Computer%20System/Firmware%20and%20Computer%20(OS)%20Booting/Firmware%20and%20Computer%20(OS)%20Booting.md)
- ↗ [Computer Bootstrap (Boot)](../🧬%20Computer%20System/Firmware%20and%20Computer%20(OS)%20Booting/🌽%20Computer%20Bootstrap%20(Boot)/Computer%20Bootstrap%20(Boot).md)

↗ [Programming Tools Chain](../👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Programming%20Tools%20Chain.md)
- ↗ [Application Runtimes & SDKs](../👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/🚠%20Application%20Runtimes%20&%20SDKs/Application%20Runtimes%20&%20SDKs.md)
- ↗ [Compilation & Program Loading Tools](../👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Compilation%20&%20Program%20Loading%20Tools/Compilation%20&%20Program%20Loading%20Tools.md)

↗ [IDE (Integrated Development Environment)](../../Software%20Engineering/CASE%20(Computer-Aided%20Software%20Engineering)%20Tools/Lower%20CASE%20Tools/IDE%20(Integrated%20Development%20Environment)/IDE%20(Integrated%20Development%20Environment).md)


### Learning Resources
📖 CSAPP: Computer System: A Programmer's Perspective
↗ [Intro to Computer Science](../../🗺%20CS%20Overview/💋%20Intro%20to%20Computer%20Science/Intro%20to%20Computer%20Science.md)

📖 程序员的自我修养：编译，链接，库

🔥 👍 从裸机启动开始运行一个C++程序
http://t.csdnimg.cn/fpEXy

📖 Compilers: Principles, Techniques, and Tools -- Alfred V.Aho, Ravi Sethi, Jeffrey D.Ullman

📖 Modern Compiler Implementation in C -- Andrew W.Appel, with Jens Palsberg

📖 Advanced Compiler Design and Implementation -- Steven S.Muchnick



## Intro
### What is a Program?
↗ [Program, Computer, and Automation](../../🗺%20CS%20Overview/Program,%20Computer,%20and%20Automation.md)

user's perspective:
system's perspective:
software perspective:
hardware perspective:


### Compilation Systems from Programmers' Perspective (Reasons for Programers to Understand Compilation Systems)
> Quote from CSAPP

However, there are some important reasons why programmers need to understand how compilation systems work:
- **Optimizing program performance**. Modern compilers are sophisticated tools that usually produce good code. As programmers, we do not need to know the inner workings of the compiler in order to write efficient code. However, in order to make good coding decisions in our C programs, we do need a basic understanding of machine-level code and how the compiler translates different C statements into machine code.
	- For example, is a switch statement always more efficient than a sequence of if-else statements? How much overhead is incurred by a function call? Is a while loop more efficient than a for loop? Are pointer references more efficient than array indexes? Why does our loop run so much faster if we sum into a local variable instead of an argument that is passed by reference? How can a function run faster when we simply rearrange the parentheses in an arithmetic expression?
- **Understanding link-time errors**. In our experience, some of the most perplexing programming errors are related to the operation of the linker, especially when you are trying to build large software systems. 
	- For example, what does it mean when the linker reports that it cannot resolve a reference? What is the difference between a static variable and a global variable? What happens if you define two global variables in different C files with the same name? What is the difference between a static library and a dynamic library? Why does it matter what order we list libraries on the command line? And scariest of all, why do some linker-related errors not appear until run time? 
- **Avoiding security holes**. For many years, buffer overflow vulnerabilities have accounted for many of the security holes in network and Internet servers. These vulnerabilities exist because too few programmers understand the need to carefully restrict the quantity and forms of data they accept from untrusted sources. A first step in learning secure programming is to understand the consequences of the way data and control information are stored on the program stack.



## 🤔 Working Process of Compilation Systems
![](../../../Assets/Pics/Screenshot%202024-02-15%20at%207.49.06PM.png)
<small>程序软件从诞生到运行</small>

![](../../../../../../Assets/Pics/Screenshot%202023-05-22%20at%209.50.58%20PM.png)
<small>A examplary illustration of the compilation, linking, loading & execution process</small>


### 0️⃣ Information, Encoding, Computer/Digital System Data Representations & Computer File Formats
↗ [(Text) Data Representations & Storage in Computer](../../🗺%20CS%20Overview/💋%20Intro%20to%20Computer%20Science/😤%20Information,%20Data,%20Number%20and%20Math%20in%20Digital%20Systems/(Text)%20Data%20Representations%20&%20Storage%20in%20Computer.md)
↗ [Encodings](../../🗺%20CS%20Overview/💋%20Intro%20to%20Computer%20Science/😤%20Information,%20Data,%20Number%20and%20Math%20in%20Digital%20Systems/Encodings.md)

↗ [Reliable Data Transfer (RDT)](../🏎️%20Computer%20Networking%20and%20Communication/📌%20Computer%20Networking%20Basics%20(Protocol%20Part)/Reliable%20Data%20Transfer%20(RDT)/Reliable%20Data%20Transfer%20(RDT).md)
↗ [Information Theory](../../../🧮%20Math%20&%20Theoretical%20Computer%20Science%20(TCS)/Information%20Theory/Information%20Theory.md)

↗ [OS /File System](../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20IO%20System/IO%20Generality%20(via%20Abstraction)/File%20&%20File%20System/File%20&%20File%20System.md)
↗ [OS /Linux /Linux File Formats](../🥷🏼%20Operating%20Systems%20&%20Kernels%20(Engineering%20Part)/Linux%20(Derived%20From%20UNIX%20Family)/🔩%20Linux%20Kernel/Linux%20IO%20&%20Files%20Management/🤔%20Linux%20File%20System/Linux%20File%20Types%20&%20Formats/Linux%20File%20Types%20&%20Formats.md)


### 0️⃣ (Compiled) Programming Languages
↗ [Programming Methodology and Languages](../👩‍💻%20Programming%20Methodology%20and%20Languages/Programming%20Methodology%20and%20Languages.md)
- ↗ [Compiled Languages](../👩‍💻%20Programming%20Methodology%20and%20Languages/Compiled%20Languages/Compiled%20Languages.md)
- ↗ [Interpreted Languages](../👩‍💻%20Programming%20Methodology%20and%20Languages/Interpreted%20Languages/Interpreted%20Languages.md)
- ↗ [ASM (Assembly Languages)](../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/ASM%20(Assembly%20Languages).md)
- ↗ [DSL(Domain Specific Languages) & GPL(General Purpose Languages)](../👩‍💻%20Programming%20Methodology%20and%20Languages/🪁%20DSL(Domain%20Specific%20Languages)%20&%20GPL(General%20Purpose%20Languages)/DSL(Domain%20Specific%20Languages)%20&%20GPL(General%20Purpose%20Languages).md)
- ↗ [Codec & Media Formats & Standards](../🦄%20Algorithm%20&%20Data%20Structure/Data%20Compression%20Technologies/Codec%20&%20Media%20Formats%20&%20Standards/Codec%20&%20Media%20Formats%20&%20Standards.md)

↗ [Automata Theory and (Formal) Language Theory](../../🧮%20Math%20&%20Theoretical%20Computer%20Science%20(TCS)/🤼‍♀️%20Mathematical%20Logics/😶‍🌫️%20Theory%20of%20Computation/🍏%20Automata%20Theory%20and%20(Formal)%20Language%20Theory/Automata%20Theory%20and%20(Formal)%20Language%20Theory.md)
↗ [Natural Language Processing (NLP)](../../🧠%20Computing%20Methodologies/👽%20Artificial%20Intelligence/🔥%20Natural%20Language%20Processing%20(NLP)/Natural%20Language%20Processing%20(NLP).md)


### 1️⃣ Compilation (Compile-time)
↗ [Program Language Translation & Compilation Theory (Compile-time)](🚮%20Program%20Language%20Translation%20&%20Compilation%20Theory%20(Compile-time)/Program%20Language%20Translation%20&%20Compilation%20Theory%20(Compile-time).md)
↗ [Compilation Phase](🚮%20Program%20Language%20Translation%20&%20Compilation%20Theory%20(Compile-time)/Compilation%20Phase/Compilation%20Phase.md)
↗ [Assembly Phase](🚮%20Program%20Language%20Translation%20&%20Compilation%20Theory%20(Compile-time)/Assembly%20Phase/Assembly%20Phase.md)

↗ [Software Analysis & Binary Engineering](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Software%20Analysis%20&%20Binary%20Engineering/Software%20Analysis%20&%20Binary%20Engineering.md)


### 2️⃣/3️⃣ Link & Library (Link-time)
↗ [Program Linking & Loading (Link-time & Load-time)](🚽%20Program%20Linking%20&%20Loading%20(Link-time%20&%20Load-time)/Program%20Linking%20&%20Loading%20(Link-time%20&%20Load-time).md)
↗ [Linking Phase](🚽%20Program%20Linking%20&%20Loading%20(Link-time%20&%20Load-time)/Linking%20Phase%20&%20Linking%20Library%20Files/Linking%20Phase.md)


### 2️⃣/3️⃣ Load (Loadtime)
↗ [Program Linking & Loading (Link-time & Load-time)](🚽%20Program%20Linking%20&%20Loading%20(Link-time%20&%20Load-time)/Program%20Linking%20&%20Loading%20(Link-time%20&%20Load-time).md)


### 4️⃣ Execution (Runtime)
↗ [ISA /Instruction Basics](../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/📌%20ISA%20Basics/📌%20Instruction%20Basics/Instruction%20Basics.md)
↗ [ISA /Instruction Execution](🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Instruction%20Execution/Instruction%20Execution.md)

![](../../../../../../../Assets/Pics/Screenshot%202023-03-03%20at%209.05.51%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-03-21%20at%209.12.25%20PM.png)
<small>Instruction Processing Level</small>

↗ [von Neumann Based Microarchitecture /Memory Access](🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Instruction%20Execution/Memory%20Access%20&%20Addressing.md)
↗ [System Security /Memory Attack](../../CyberSecurity/System%20Security/📝%20Memory%20Security/Memory%20Threats%20&%20Attacks/Memory%20Threats%20&%20Attacks.md)

↗ [Program Execution (Runtime)](🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Program%20Execution%20(Runtime).md)
↗ [Application Runtimes & SDKs](../👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/🚠%20Application%20Runtimes%20&%20SDKs/Application%20Runtimes%20&%20SDKs.md)

↗ [Operating System & OS Kernel (Theory Part)](../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part).md)
- ↗ [OS Processes & Automata Management (CPU + Main Memory Resource)](../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Processes%20&%20Automata%20Management%20(CPU%20+%20Main%20Memory%20Resource)/OS%20Processes%20&%20Automata%20Management%20(CPU%20+%20Main%20Memory%20Resource).md)
- ↗ [OS Memory Management (Main Memory + Secondary Memory Resource)](../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource).md)

↗ [System Security](../../../CyberSecurity/System%20Security/System%20Security.md)
- ↗ [Software Analysis & Binary Engineering](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Software%20Analysis%20&%20Binary%20Engineering/Software%20Analysis%20&%20Binary%20Engineering.md)
- ↗ [Anti-Reverse Engineering & Software Protection](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Software%20Analysis%20&%20Binary%20Engineering/Anti-Reverse%20Engineering%20&%20Software%20Protection/Anti-Reverse%20Engineering%20&%20Software%20Protection.md)
- ↗ [Malicious Code Detection & Vulnerability Discovery](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Software%20Analysis%20&%20Binary%20Engineering/Malicious%20Code%20Detection%20&%20Vulnerability%20Discovery/Malicious%20Code%20Detection%20&%20Vulnerability%20Discovery.md)
- ↗ [Software Vulnerability & Weakness](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🐒%20Software%20Vulnerability%20&%20Weakness/Software%20Vulnerability%20&%20Weakness.md)



## Ref
[Execution (computing) | Wikipedia]: https://en.wikipedia.org/wiki/Execution_(computing)

[程序的编译、装载与链接 - piginzoo的文章 - 知乎]: https://zhuanlan.zhihu.com/p/139026433
[《链接、装载与库》 阅读笔记 (1)- 基本概念与静态链接]: https://wulc.me/2020/05/31/《链接、装载与库》阅读笔记(1)-基本概念与静态链接/

[高级语言的编译：链接及装载过程介绍]: https://tech.meituan.com/2015/01/22/linker.html

[《程序员的自我修养》——全书思维导图（上）]: https://www.zhihu.com/tardis/zm/art/111682188?source_id=1003
[【读书】《程序员的自我修养》——全书思维导图（中） - 一尾66的文章 - 知乎]: 
https://zhuanlan.zhihu.com/p/138345701

[编译原理三大经典：龙书 虎书 鲸书 | cnblog]: https://www.cnblogs.com/Arthurian/p/7881889.html
