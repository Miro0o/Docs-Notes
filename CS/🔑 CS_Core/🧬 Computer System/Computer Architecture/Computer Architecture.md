# Computer Architecture

[TOC]



## Res
### Related Topics
↗ [Processors' Architectures](../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/🏆%20Processors'%20Architectures/Processors'%20Architectures.md)
↗ [ASM (Assembly Languages)](../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/ASM%20(Assembly%20Languages).md)

↗ [Distributed Systems](../../../System%20Architecture%20Design/🌌%20Distributed%20Systems/Distributed%20Systems.md)
↗ [Cloud Platform (System Level Engineering)](../../../Software%20Engineering/☁️%20Cloud%20Native/Cloud%20Platform%20(System%20Level%20Engineering)/Cloud%20Platform%20(System%20Level%20Engineering).md)

↗ [DS Web Services' Architectures](../../🍕%20Database%20System/🪐%20Web%20&%20DBMS/DS%20Web%20Services'%20Architectures.md)
↗ [Web Application Architectures](../../../Software%20Engineering/👾%20Web%20Dev%20&%20Ops/🗄️%20Web%20BackEnd%20Dev/Web%20Application%20Architectures.md)


### Courses
🎬【计算机组成原理（哈工大刘宏伟）135讲（全）高清】 https://www.bilibili.com/video/BV1t4411e7LH/?p=2&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d


🏫 [Intro to CS (CSAPP)](../../../🗺%20CS_Overview/💋%20Intro%20to%20CS/Intro%20to%20CS.md)

🏫 [UCB - CS61C Great Ideas in Computer Architecture](../../../🏠%20Assets/Universities/UC%20Berkeley/CS61C%20Great%20Ideas%20in%20Computer%20Architecture/CS61C%20Great%20Ideas%20in%20Computer%20Architecture.md)
🏫 [ETH - Digital Design and Computer Architecture](../../../🏠%20Assets/Universities/ETH/Digital%20Design%20and%20Computer%20Architecture/Digital%20Design%20and%20Computer%20Architecture.md)

🧑‍🏫 [Computers and Networks | Fall 2014](http://webhotel4.ruc.dk/~keld/teaching/CAN_e14/)
by [Keld Helsgaun](http://www.dat.ruc.dk/~keld/)
(I found this course randomly online and it uses the same textbook as the course I took in SCU, though an older version. I copied the link here for future convenience of its 🔗 [PPT](http://webhotel4.ruc.dk/~keld/teaching/CAN_e14/Slides/index.html))

[Figures from Null & Lobur](http://www.sci.brooklyn.cuny.edu/~jones/cisc3310/Null%20&%20Lobur%20Figures.htm)


🆙 Coursera: Nand2Tetris

> 🔗 https://csdiy.wiki/体系结构/N2T/
> 
>课程资源
> - 课程网站：[Nand2Tetris I](https://www.coursera.org/learn/build-a-computer/home/week/1), [Nand2Tetris II](https://www.coursera.org/learn/nand2tetris2/home/welcome)
> - 课程视频：详见课程网站
> - 课程教材：[计算机系统要素：从零开始构建现代计算机](https://github.com/PKUFlyingPig/NandToTetris/blob/master/%5B%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%B3%BB%E7%BB%9F%E8%A6%81%E7%B4%A0%EF%BC%9A%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E6%9E%84%E5%BB%BA%E7%8E%B0%E4%BB%A3%E8%AE%A1%E7%AE%97%E6%9C%BA%5D.(%E5%B0%BC%E8%90%A8).%E5%91%A8%E7%BB%B4.%E6%89%AB%E6%8F%8F%E7%89%88.pdf)
> - 课程作业：10 个 Project 带你造台计算机，具体要求详见课程网站
>
>资源汇总
>@PKUFlyingPig 在学习这门课中用到的所有资源和作业实现都汇总在 [PKUFlyingPig/NandToTetris - GitHub](https://github.com/PKUFlyingPig/NandToTetris) 中。


### Books
📖 The essence of computer orgnization and architecture, 5ed, Linda Null, Julia Lobour

📖 csapp
📖 Computer Organization and Design

微型计算机系统原理及应用 第六版 周明德

王爽的《汇编语言》
林立的《单片机原理及应用――基于Proteus和Keil C（第4版）》
《手把手教你学DSP 基于TMS320F28335的应用开发及实战 微课视频版》
李正军的《计算机控制系统》


### Other Materials
📄 [GeeksForGeeks - Computer Organization and Architecture Tutorials](https://www.geeksforgeeks.org/computer-organization-and-architecture-tutorials/)
📄 https://foxsen.github.io/archbase/
计算机体系结构基础



## Intro
### Computer Organization & Architecture
![computer_architecture.excalidraw | 800](../../../../Assets/Illustrations/Computer%20System/computer_architecture.excalidraw.md)
<small>Computer System Architecture Hierarchy (von Neumann Model) </small>

![](../../../../../Assets/Pics/Screenshot%202023-05-08%20at%204.26.42%20PM.png)


**Computer organization**, or ↗ [Computer Microarchitectures (Computer Organization)](Computer%20Microarchitectures%20(Computer%20Organization)/Computer%20Microarchitectures%20(Computer%20Organization).md), is the implementation method of a given ISA. 

> ↗ [von Neumann Based Microarchitecture](Computer%20Microarchitectures%20(Computer%20Organization)/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/von%20Neumann%20Based%20Microarchitecture.md)
  ↗ [Non-von Neumann Based Microarchitectures](Computer%20Microarchitectures%20(Computer%20Organization)/🤵%20Non-von%20Neumann%20Based%20Microarchitectures/Non-von%20Neumann%20Based%20Microarchitectures.md)

↗ [Instruction Set Architecture (ISA)](Instruction%20Set%20Architecture%20(ISA)/Instruction%20Set%20Architecture%20(ISA).md) is the designed set of rules of how a CPU /machine can be manipulated.

↗ [ASM (Assembly Languages)](../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/ASM%20(Assembly%20Languages).md) is an encoding of machine code (*binary*, structured under an ISA to be meaningful) to readable language (*english*).

**Computer architecture**, is the combination of microarchitecture and ISA; or, it's the computer from a programmer's (mostly low level) perspective.


🏃 🏃‍♀️🏃‍♂️ Start learning computer organization and architecture from [Computer Architecture Overview](📌%20Computer%20Organization%20&%20Architecture%20Basics/Computer%20Architecture%20Overview.md). 

Enjoy :)

### Microcomputer Principles & Interfaces
**Microcomputer principles & interfaces** is the knowledge about computer **processors** (mostly CPU, a kind of processor) and how it is operating (instruction execution and data transfer, which involves **bus** and **interfaces**). 

Computer Processors strongly relate to **microarchitectures** and **ISA**. Hence a tad pre-knowledge of them is expected.

To control computer processors in a programmable way, knowledge about assembly languages is also expected. 

↗ [ASM (Assembly Languages)](../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/ASM%20(Assembly%20Languages).md)


### ⭐ Importance Themes In Computer Systems
↗ [Importance Themes & Ideaology in CS](../../../🗺%20CS_Overview/💋%20Intro%20to%20CS/Importance%20Themes%20&%20Ideaology%20in%20CS.md)
#### 👉 Concurrency & Parallelism
↗ [Parallel Computing & Multiprocessor Architectures](Computer%20Microarchitectures%20(Computer%20Organization)/Computer%20Processors/Multiprocessor%20and%20Multicore%20Organization/Parallel%20Computing%20&%20Multiprocessor%20Architectures.md)
#### 👉 Abstraction & Encapsulation
↗ [📌 Operating System Overview /🧠 Abstractions Provided by an Operating System (From User Perspective)](../Operating%20System%20(Theory)/🦺%20Operating%20System%20Basics/📌%20Operating%20System%20Overview.md#🧠%20Abstractions%20Provided%20by%20an%20Operating%20System%20(From%20User%20Perspective))
↗ [IO Generality (via Abstraction)](../Operating%20System%20(Theory)/IO%20System/IO%20Generality%20(via%20Abstraction)/IO%20Generality%20(via%20Abstraction).md)
#### 👉 Coupling & Decoupling



## Ref
《微机原理与接口技术》和《计算机组成原理》、《计算机体系结构》三门课程有什么区别？先后修的顺序应该是怎么样的？研究操作系统需要学习哪门课程？ - 知乎 https://www.zhihu.com/question/19954019

> - 组成原理:怎么设计CPU，怎么设计计算机系统中的各个部件;
> - 体系结构:怎么设计CPU性能会高，怎么设计计算机系统性能会高;
> - [微机与接口](https://www.zhihu.com/search?q=%E5%BE%AE%E6%9C%BA%E4%B8%8E%E6%8E%A5%E5%8F%A3&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A427424135%7D):世界上已经设计好的CPU有千千万万，选择一个，怎么进行[汇编语言程序设计](https://www.zhihu.com/search?q=%E6%B1%87%E7%BC%96%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A427424135%7D)和硬件设计应用，在此学习了一种汇编语言。
>
> 曾经，"微型计算机原理"与"计算机接口技术"是两个独立的课，有大神说，要有光，不，要合并，于是就合并出了"微型计算机原理与汇编语言与接口技术"，简称"微机原理与接口技术";
> 也有大神说，要做大，要创新!
> 于是乎，"计算机组成原理"与"计算机体系结构"两课合并出了"[计算机组成原理与体系结构](https://www.zhihu.com/search?q=%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86%E4%B8%8E%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A427424135%7D)"; 于是乎， "模拟电子电路"与"数字逻辑电路"合并出了"[模拟与数字电路](https://www.zhihu.com/search?q=%E6%A8%A1%E6%8B%9F%E4%B8%8E%E6%95%B0%E5%AD%97%E7%94%B5%E8%B7%AF&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A427424135%7D)";
> 
> 更大的创新，在酝酿中，可能叫"[模拟数字与组成原理](https://www.zhihu.com/search?q=%E6%A8%A1%E6%8B%9F%E6%95%B0%E5%AD%97%E4%B8%8E%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A427424135%7D)"。
> 社会巨变，课程也要适应，时代需要所谓大神来推动。


> **Computer Organization** is realisation of what is specified by the computer [architecture](https://www.zhihu.com/search?q=architecture&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A33332592%7D). It deals with how operational [attributes](https://www.zhihu.com/search?q=attributes&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A33332592%7D) are linked together to meet the requirements specified by computer architecture. Some organizational attributes are hardware details, control signals, peripherals.
> 
> **Computer Architecture** deals with giving operational attributes of the computer or Processor to be specific. It deals with details like physical memory, ISA of the processor, the number of bits used to represent the data types, Input Output mechanism and technique for addressing memories.


![](../../../../Assets/Pics/Pasted%20image%2020230313213313.png)


《微机原理与接口技术》和《计算机组成原理》、《计算机体系结构》三门课程有什么区别？先后修的顺序应该是怎么样的？研究操作系统需要学习哪门课程？ - hyper的回答 - 知乎 https://www.zhihu.com/question/19954019/answer/427424135

求推荐微机原理的教材？ - 华东子的回答 - 知乎 https://www.zhihu.com/question/31207854/answer/2787053008
