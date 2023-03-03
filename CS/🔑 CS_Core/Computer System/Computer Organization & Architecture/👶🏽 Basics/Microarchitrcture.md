# Microarchitecture

[TOC]



## Overview
![](../../../../../Assets/Pics/Pasted%20image%2020230302132847.png)
<small>Microarchitecture in computer system hierarchy</small>

> 🔗 https://en.wikipedia.org/wiki/Microarchitecture

In computer engineering, ==**microarchitecture**, also called **computer organization**== and sometimes abbreviated as **µarch** or **uarch**, is the way a given [instruction set architecture](https://en.wikipedia.org/wiki/Instruction_set_architecture "Instruction set architecture") (ISA) is implemented in a particular processor. A given ISA may be implemented with different microarchitectures;implementations may vary due to different goals of a given design or due to shifts in technology.

[Computer architecture](https://en.wikipedia.org/wiki/Computer_architecture "Computer architecture") is the combination of microarchitecture and instruction set architecture.

> **微架构（Microarchitecture）是ISA在处理器的实现**，描述处理器是怎样实现功能的，其本质就是一系列硬件实现以满足各种指令集。而Microarchitecture是ISA的具体实现，而且对于同一个ISA，可以使用不同技术的微架构 ，比如单周期、多周期以及流水线。比如说x86 ISA有286，386，486，Pretium，Pretium Pro等实现。目前，微架构涉及以下部分：**流水线、并行、存储系统分层结构**，下面将对这几部分进行详细介绍。



## Von Neumann Based Models
![](../../../../../Assets/Pics/Pasted%20image%2020230302132111.png)

![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%204.11.10%20PM.png)

Today’s version of the stored-program machine architecture satisfies at least the following characteristics:

1. Consists of three hardware systems: 
	1. a central processing unit (CPU) with 
		1. a control unit;
		2. an arithmetic logic unit (ALU);
		3. registers (small storage areas);
		4. a program counter; 
	2. a main memory system, which holds programs that control the computer’s operation; 
	3. an I/O system.

3. Has the capacity to carry out sequential instruction processing.

4. Contains a single path, either physically or logically, between the main memory system and the control unit of the CPU, forcing alternation of instruction and execution cycles. This single path is often referred to as the ==von Neumann bottleneck==.



## Non-Von Neumann Models
Many non–von Neumann machines are **designed for special purposes**.

A number of different subfields fall into the non–von Neumann category, including: 
1. Neural networks (using ideas from models of the brain as a computing paradigm) implemented in silicon, cellular automata, cognitive computers (machines that learn by experience rather than through programming, e.g., IBM’s SyNAPSE computer, a machine that models the human brain);
2. Quantum computation (a combination of computing and quantum physics)
3. Dataflow computation;
4. Parallel computers. 

These all have something in common -- the computation is distributed among different processing units that act in parallel. They differ in how weakly or strongly the various components are connected. 

Ofcourse, parallel computing is currently the most popular.

### Harvard Based Models

![](../../../../../Assets/Pics/Pasted%20image%2020230302132344.png)

### Parallel Processing Computer
#TODO 

### Quantuem Computer
#TODO 



## Microprocessor
Microprocessor is at the core of a computer system. Specifically, it is a processing unit (control purpose mostly) providing the fountaional computing power. 

Though it varies on different computer architectures, microprocessor can be CPU, GPU, DSP or the latest SoC (System on a Chip).

More is noted at ↗ [Microprocessor](Microprocessor.md).



## Ref
[漫谈计算机架构]: https://segmentfault.com/a/1190000014885126
