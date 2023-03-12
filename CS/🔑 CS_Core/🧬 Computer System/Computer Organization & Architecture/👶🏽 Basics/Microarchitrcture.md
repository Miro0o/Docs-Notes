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
#TODO 

### Parallel 

> ↗ [von Neumann Model /Multiprocessor and Multicore Orgnization](../🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Processor/Multiprocessor%20and%20Multicore%20Orgnization.md)

#### Flynn's Taxonomy 

![](../../../../../Assets/Pics/Pasted%20image%2020230304154759.png)
<small>Flynn's Taxonomy of Computer Architectures</small>

> 🔗 Further reading: 
> - [Duncan's Taxonomy](https://en.wikipedia.org/wiki/Duncan%27s_taxonomy)
> - [Non-von Neumann Based Microarchitectures](../Non-von%20Neumann%20Based%20Microarchitectures/Non-von%20Neumann%20Based%20Microarchitectures.md)

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


More is at ↗ [von Neumann Based Microarchitecture](../🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/von%20Neumann%20Based%20Microarchitecture.md).


### Non-Von Neumann Models

More is at ↗ [Non-von Neumann Based Microarchitectures](../Non-von%20Neumann%20Based%20Microarchitectures/Non-von%20Neumann%20Based%20Microarchitectures.md).

#### Harvard Based Models
![](../../../../../Assets/Pics/Pasted%20image%2020230302132344.png)



## Microprocessor
Microprocessor (or simple processor) is at the core of a computer system. It provides the very fountaional computing power. 

Though it varies on different computer architectures, microprocessor can be implemented as CPU (a general purpose processors unit), GPU, DSP or the latest SoC (System on a Chip).

More is noted at ↗ [Microprocessor](Microprocessor.md).
Other processors at ↗ [Processor](Processor.md).



## Ref
[漫谈计算机架构]: https://segmentfault.com/a/1190000014885126
[Microarchitecture]: https://en.wikipedia.org/wiki/Microarchitecture#See_also
[Flynn's Taxonomy]: https://en.wikipedia.org/wiki/Flynn%27s_taxonomy