# Non-von Neumann Based Microarchitectures

[TOC]



## Res
↗ [Computer Microarchitectures (Computer Organization)](../Computer%20Microarchitectures%20(Computer%20Organization).md)



## Overview
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



## Harvard Based Models
![](../../../../../Assets/Pics/Pasted%20image%2020230302132344.png)

Harvard architecture have two buses, thus allowing data and instructions to be transferred simultaneously, but also have separate storage for data and instructions.

Many modern general-purpose computers use a modified version of the
Harvard architecture in which they have separate pathways for data and instructions but not separate storage.

Pure Harvard architectures are typically used in microcontrollers (an entire computer system on a chip), such as those found in embedded systems, as in appliances, toys, and cars.



## ⭐️ Parallel Processing Computer
Term "parallel" here describes a general conception of how computing is conducted. It concieves a way to improve computing proficiency with limited resources.

The engineering implementation to parallel computing or parallel processing can be roughly ascribed to two level: the hardware and the software.

1. On the hardware level, there are two ways to parallel compute as well:
	1. multiprocessing with multiple processors;
	2. multiprocessing with processors of multiple cores, or multicore processor.

> For more at ↗ [von Neumann Model /Multiprocessor and Multicore Orgnization](../Computer%20Processors/Multiprocessor%20and%20Multicore%20Organization/Multiprocessor%20and%20Multicore%20Organization.md)
> 

2. On the software level, there are two ways to parallel compute as well:
	1. multiprocessing with multiple processes, or multitasking. It means running multiple process for multiple tasks;
	2. multiprocessing with mnultiple threads, or multithreading. It means running multipe threads for divided sequential steps of tasks.

🌻 🌻 Very often, designing parallel programs to maximumally utilize the parallel designed hardware is the most difficult part in achieving parallel processing. Hence it's why even when parallel processing architectures is getting more and more complicated it is still not a common standard in daily lives to parallel compute: there are not efficient enough programs to support that set of hardwares.

> 💡 For more of parallelism at system software level, go to ↗ [Operating System Design /OS Design for Multiprocessor and Multicore](../../Operating%20System%20(Theory)/🦺%20Operating%20System%20Basics/Operating%20System%20Design.md).

### Amdahl’s Law
Even parallel computing has its limits, however. As the number of processors increases, so does the overhead of managing how tasks are distributed to those processors.

No matter how many processors we place in a system, or how many resources we assign to them, somehow, somewhere, a bottleneck is bound to develop. The best we can do, however, is make sure the slowest parts of the system are the ones that are used the least. This is the idea of Amdahl’s Law.

Amdahl’s law states that the performance enhancement possible with a given improvement is limited by the amount that the improved feature is used. The underlying premise is that every algorithm has a sequential part that ultimately limits the speedup that can be achieved by multiprocessor implementation.

### Flynn's Taxonomy 

![](../../../../../Assets/Pics/Pasted%20image%2020230304154759.png)
<small>Flynn's Taxonomy of Computer Architectures</small>

> 🔗 Further reading: [Duncan's Taxonomy](https://en.wikipedia.org/wiki/Duncan%27s_taxonomy)



### Superscalar and VLIW

#TODO 


### Vector Processors


### Interconnection Networks


### Shared Memory Multiprocessors


### Distributed Computing


### 💦 Alternative Parallel Processing Approaches

#### Dataflow Computing
#TODO 


#### Neural Network


#### Systolic Arrays



## Quantuem Computer
#TODO 






## Ref
