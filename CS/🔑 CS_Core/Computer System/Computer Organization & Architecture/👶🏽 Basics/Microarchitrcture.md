# Microarchitecture

[TOC]



Also check out this one ↗ [von Neumann Based Microarchitecture](../🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/von%20Neumann%20Based%20Microarchitecture.md) for more info.

## Overview
![](../../../../../Assets/Pics/Pasted%20image%2020230302132847.png)
<small>Microarchitecture in computer system hierarchy</small>

> 🔗 https://en.wikipedia.org/wiki/Microarchitecture

In computer engineering, ==**microarchitecture**, also called **computer organization**== and sometimes abbreviated as **µarch** or **uarch**, is the way a given [instruction set architecture](https://en.wikipedia.org/wiki/Instruction_set_architecture "Instruction set architecture") (ISA) is implemented in a particular processor. A given ISA may be implemented with different microarchitectures;implementations may vary due to different goals of a given design or due to shifts in technology.

[Computer architecture](https://en.wikipedia.org/wiki/Computer_architecture "Computer architecture") is the combination of microarchitecture and instruction set architecture.

> **微架构（Microarchitecture）是ISA在处理器的实现**，描述处理器是怎样实现功能的，其本质就是一系列硬件实现以满足各种指令集。而Microarchitecture是ISA的具体实现，而且对于同一个ISA，可以使用不同技术的微架构 ，比如单周期、多周期以及流水线。比如说x86 ISA有286，386，486，Pretium，Pretium Pro等实现。目前，微架构涉及以下部分：**流水线、并行、存储系统分层结构**.



## Microarchitecture Technologies
### Pipeline


### Parallel 

> ↗ [von Neumann Model /Multiprocessor and Multicore Orgnization](../🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Processor/Multiprocessor%20and%20Multicore%20Orgnization.md)

#### Flynn's Taxonomy 

![](../../../../../Assets/Pics/Pasted%20image%2020230304154759.png)
<small>Flynn's Taxonomy of Computer Architectures</small>

> 🔗 Further reading: [Duncan's Taxonomy](https://en.wikipedia.org/wiki/Duncan%27s_taxonomy)


#### SISD
![](../../../../../Assets/Pics/Pasted%20image%2020230304155503.png)

> 早期的**冯·诺依曼结构**采用的都是SISD，冯·诺依曼结构也称**存储程序计算机**，它有两个重要特性：1. 指令和数据被存储在内存中；2. 指令被顺序执行，在一个时刻只有一条指令在执行，通过PC（Program Counter）识别当前指令。


#### SIMD
![](../../../../../Assets/Pics/Pasted%20image%2020230304155409.png)

> SIMD 就是单指令多数据的缩写，将一个指令广播到多个处理器上，但每个处理器都有自己的数据。也就是说同一份控制指令同时运行不同的数据，如上图所示，这样做的好处就是减轻的控制成本。目前，GPUs(Graphics Processor Units)采用的就是SIMD架构。


#### MISD
Not implemented.


#### MIMD
![](../../../../../Assets/Pics/Pasted%20image%2020230304155426.png)

> MIMD指的是不同时刻不同CPU执行的指令不同，并且数据也不同，如上图所示。目前超级计算机，网络并行计算机集群和“网格”，多处理器SMP计算机，多核PC都属于这一类。而MIMD又可以根据内存结构，可以分为**共享内存和消息驱动**。共享内存就是处理器之间共享内存，通过内存来进行通信，而消息驱动指的是处理器通过消息驱动来进行通信。目前**共享内存有SMP、NUMA两种，消息驱动对应DM**。


### Hierarchical Stroage 

![](../../../../../../Assets/Pics/Pasted%20image%2020230301122408.png)
<small>Simplified Computer Memory Hierarchy </small>



## Microarchitecture Models
### Von Neumann Based Models
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



### Non-Von Neumann Models
Non–von Neumann architectures are those in which the model of computation varies from the characteristics listed for the von Neumann architecture. 
- For example, an architecture that does not store programs and data in memory or does not process a program sequentially would be considered a non–von Neumann machine. 
- Also, a computer that has two buses, one for data and a separate one for instructions, would be considered a non–von Neumann machine.

Many non–von Neumann machines are **designed for special purposes**.


A number of different subfields fall into the non–von Neumann category, including: 
1. Neural networks (using ideas from models of the brain as a computing paradigm) implemented in silicon, cellular automata, cognitive computers (machines that learn by experience rather than through programming, e.g., IBM’s SyNAPSE computer, a machine that models the human brain);
2. Quantum computation (a combination of computing and quantum physics)
3. Dataflow computation;
4. Parallel computers. 
These all have something in common -- the computation is distributed among different processing units that act in parallel. They differ in how weakly or strongly the various components are connected. 

Of these, parallel computing is currently the most popular.


#### Harvard Based Models

![](../../../../../Assets/Pics/Pasted%20image%2020230302132344.png)

Harvard architecture have two buses, thus allowing data and instructions to be transferred simultaneously, but also have separate storage for data and instructions.

Many modern general-purpose computers use a modified version of the
Harvard architecture in which they have separate pathways for data and instructions but not separate storage.

Pure Harvard architectures are typically used in microcontrollers (an entire computer system on a chip), such as those found in embedded systems, as in appliances, toys, and cars.


#### ⭐️ Parallel Processing Computer
Term "parallel" here describes a general conception of how computing is conducted. It concieves a way to improve computing proficiency with limited resources.

The engineering implementation to parallel computing or parallel processing can be roughly ascribed to two level: the hardware and the software.

1. On the hardware level, there are two ways to parallel compute as well:
	1. multiprocessing with multiple processors;
	2. multiprocessing with processors of multiple cores, or multicore processor.

> For more at ↗ [von Neumann Model /Multiprocessor and Multicore Orgnization](../🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Processor/Multiprocessor%20and%20Multicore%20Orgnization.md)
> 

2. On the software level, there are two ways to parallel compute as well:
	1. multiprocessing with multiple processes, or multitasking. It means running multiple process for multiple tasks;
	2. multiprocessing with mnultiple threads, or multithreading. It means running multipe threads for divided sequential steps of tasks.

Very often, designing parallel programs to maximumally utilize the parallel designed hardware is the most difficult part in achieving parallel processing. Hence it's why even when parallel processing architectures is getting more and more complicated it is still not a common standard in daily lives to parallel compute: there are not efficient enough programs to support that set of hardwares.

> For more at ↗ [Operating System Design /OS Design for Multiprocessor and Multicore](../../Operating%20System/🦺%20Basics/Operating%20System%20Design.md)

##### Amdahl’s Law
Even parallel computing has its limits, however. As the number of processors increases, so does the overhead of managing how tasks are distributed to those processors.

No matter how many processors we place in a system, or how many resources we assign to them, somehow, somewhere, a bottleneck is bound to develop. The best we can do, however, is make sure the slowest parts of the system are the ones that are used the least. This is the idea of Amdahl’s Law.

Amdahl’s law states that the performance enhancement possible with a given improvement is limited by the amount that the improved feature is used. The underlying premise is that every algorithm has a sequential part that ultimately limits the speedup that can be achieved by multiprocessor implementation.

#### Quantuem Computer
#TODO 


#### Dataflow Architecture
#TODO 



## Microprocessor
Microprocessor (or simple processor) is at the core of a computer system. It provides the very fountaional computing power. 

Though it varies on different computer architectures, microprocessor can be implemented as CPU (a general purpose processors unit), GPU, DSP or the latest SoC (System on a Chip).

More is noted at ↗ [Microprocessor](Microprocessor.md).
Other processors at ↗ [Processor](Processor.md).



## Ref
[漫谈计算机架构]: https://segmentfault.com/a/1190000014885126
[Microarchitecture]: https://en.wikipedia.org/wiki/Microarchitecture#See_also
[Flynn's Taxonomy]: https://en.wikipedia.org/wiki/Flynn%27s_taxonomy