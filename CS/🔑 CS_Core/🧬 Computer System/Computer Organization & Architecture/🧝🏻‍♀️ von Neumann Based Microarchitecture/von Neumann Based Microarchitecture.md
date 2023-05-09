# Von Neumann Based Microarchitecture

[TOC]



## Res
#TODO 

## Overview
The **von Neumann architecture** -- also known as the **von Neumann model** or **Princeton architecture** --- is a computer architecture based on a 1945 description by [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann), and by others, in the _[First Draft of a Report on the EDVAC](https://en.wikipedia.org/wiki/First_Draft_of_a_Report_on_the_EDVAC "First Draft of a Report on the EDVAC")_

The document describes a design architecture for an electronic digital computer with these components:
- A processing unit with both an [arithmetic logic unit](https://en.wikipedia.org/wiki/Arithmetic_logic_unit "Arithmetic logic unit") and [processor registers](https://en.wikipedia.org/wiki/Processor_register "Processor register")
- A control unit that includes an [instruction register](https://en.wikipedia.org/wiki/Instruction_register "Instruction register") and a [program counter](https://en.wikipedia.org/wiki/Program_counter "Program counter")
- Memory that stores data and instructions
- External mass storage
- Input and output mechanisms

Today’s version of the **stored-program machine architecture (von neumann models here)** satisfies at least the following characteristics:

1. Consists of three hardware systems: 
	1. a central processing unit (CPU) with 
		1. a 1️⃣ **control unit**;
		2. an 2️⃣ **arithmetic logic unit (ALU)**;
		3. registers (small storage areas);
		4. a program counter; 
	2. a 3️⃣ **main memory system**, which holds programs that control the computer’s operation; 
	3. an 4️⃣5️⃣ **I/O system**.

3. Has the capacity to carry out **sequential instruction processing**.

4. Contains a **single path (bus system)**, either physically or logically, between the main memory system and the control unit of the CPU, forcing alternation of instruction and execution cycles. This single path is often referred to as the ==von Neumann bottleneck==.


![](../../../../../Assets/Pics/Pasted%20image%2020230302132111.png)
<small>The Modified von Neumann Architecture</small>


![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%204.11.10%20PM.png)


The term "von Neumann architecture" has evolved to refer to any **stored-program computer** in which an **instruction fetch** and a **data operation** cannot occur at the same time (since they share a common bus). This is referred to as the [von Neumann bottleneck](https://en.wikipedia.org/wiki/Von_Neumann_architecture#Von_Neumann_bottleneck), which often limits the performance of the corresponding system

The design of a von Neumann architecture machine is simpler than in a [Harvard architecture](https://en.wikipedia.org/wiki/Harvard_architecture "Harvard architecture") machine -- which is also a stored-program system, yet has one dedicated set of address and data buses for reading and writing to memory, and another set of address and data buses to fetch instructions.



## Ref
[关于冯·诺依曼结构]: https://starashzero.github.io/swi-homework/lab04.html
[一套用了 70 年的计算机架构 —— 冯·诺依曼架构]: https://www.mdnice.com/writing/ba4b3af843a84652adef7fae7380da07

[Von Neumann Architecture | Wikipedia]: https://en.wikipedia.org/wiki/Von_Neumann_architecture
