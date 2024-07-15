# Parallel Computing

[TOC]



## Res
### Related Topics
↗ [Multiprocessor Architectures & Parallel Computing](../../../Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/🚦%20Computer%20Processors%20&%20Logic%20Chips/Multiprocessors%20and%20Multicore%20Processors/Multiprocessor%20Architectures%20&%20Parallel%20Computing/Multiprocessor%20Architectures%20&%20Parallel%20Computing.md)
↗ [Multiprocessors and Multicore Processors](../../../Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/🚦%20Computer%20Processors%20&%20Logic%20Chips/Multiprocessors%20and%20Multicore%20Processors/Multiprocessors%20and%20Multicore%20Processors.md)

↗ [Distributed Systems](../../../../../System%20Architecture%20Design/🌌%20Distributed%20Systems/Distributed%20Systems.md)
↗ [Distributed Computing](../../../../../System%20Architecture%20Design/🌌%20Distributed%20Systems/Distributed%20Computing/Distributed%20Computing.md)



## Intro
> 🔗 https://en.wikipedia.org/wiki/Parallel_computing

![](../../../../../../Assets/Pics/Screenshot%202024-03-17%20at%204.49.59%20PM.png)
<small>https://en.wikipedia.org/wiki/Parallel_computing</small>

Parallel computing is a type of computation in which many calculations or processes are carried out simultaneously. Large problems can often be divided into smaller ones, which can then be solved at the same time. There are several different forms of parallel computing: bit-level, instruction-level, data, and task parallelism. Parallelism has long been employed in high-performance computing, but has gained broader interest due to the physical constraints preventing frequency scaling. As power consumption (and consequently heat generation) by computers has become a concern in recent years, parallel computing has become the dominant paradigm in computer architecture, mainly in the form of multi-core processors.

Parallel computing is closely related to concurrent computing—they are frequently used together, and often conflated, though the two are distinct: it is possible to have parallelism without concurrency, and concurrency without parallelism (such as multitasking by time-sharing on a single-core CPU). In parallel computing, a computational task is typically broken down into several, often many, very similar sub-tasks that can be processed independently and whose results are combined afterwards, upon completion. In contrast, in concurrent computing, the various processes often do not address related tasks; when they do, as is typical in distributed computing, the separate tasks may have a varied nature and often require some inter-process communication during execution.

Parallel computers can be roughly classified according to the level at which the hardware supports parallelism, with multi-core and multi-processor computers having multiple processing elements within a single machine, while clusters, MPPs, and grids use multiple computers to work on the same task. Specialized parallel computer architectures are sometimes used alongside traditional processors, for accelerating specific tasks.

In some cases parallelism is transparent to the programmer, such as in bit-level or instruction-level parallelism, but explicitly parallel algorithms, particularly those that use concurrency, are more difficult to write than sequential ones, because concurrency introduces several new classes of potential software bugs, of which race conditions are the most common. Communication and synchronization between the different subtasks are typically some of the greatest obstacles to getting optimal parallel program performance.
A theoretical upper bound on the speed-up of a single program as a result of parallelization is given by Amdahl's law, which states that it is limited by the fraction of time for which the parallelization can be utilised.


### Concurrency & Parallelism
Throughout the history of digital computers, two demands have been constant forces in driving improvements: we want them to do more, and we want them to run faster. Both of these factors improve when the processor does more things at once. We use the term **concurrency** to refer to the general concept of a system with multiple, simultaneous activities, and the term **parallelism** to refer to the use of concurrency to make a system run faster. Parallelism can be exploited at multiple levels of abstraction in a computer system. We highlight three levels here, working from the highest to the lowest level in the system hierarchy.
#### 👉 Process/Thread-level Concurrency
↗ [Operating Systems /Concurrency Control](../../../Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource)/Concurrency%20Control/Concurrency%20Control.md)
↗ [Database Systems /Concurrency Control](../../../../🍕%20Computer%20Storage%20&%20Database%20Systems/Database%20Systems/⚜️%20Database%20System%20Design/📌%20DBMS%20Design/Physical%20Database%20Design%20(Software%20Engineering)/Transaction%20Management/Concurrency%20Control/Concurrency%20Control.md)
↗ [OS Level Programming /Concurrency](../../../../🥷🏼%20Operating%20Systems%20&%20Kernels%20(Engineering%20Part)/📟%20System%20Level%20Programming/OS%20Level%20Programming%20in%20Different%20Languages/OS%20Level%20Programming%20with%20C%20&%20CPP/Process%20Management/Concurrency.md)
#### 👉 Instruction Level Parallelism
↗ [ILP (Instruction Level Parallelism)](../../../../🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Instruction%20Execution/ILP%20(Instruction%20Level%20Parallelism)/ILP%20(Instruction%20Level%20Parallelism).md)
#### 👉 Hardware Level Parallel Computing
↗ [Multiprocessor Architectures & Parallel Computing](../../../Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/🚦%20Computer%20Processors%20&%20Logic%20Chips/Multiprocessors%20and%20Multicore%20Processors/Multiprocessor%20Architectures%20&%20Parallel%20Computing/Multiprocessor%20Architectures%20&%20Parallel%20Computing.md)
↗ [Multiprocessors and Multicore Processors](../../../Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/🚦%20Computer%20Processors%20&%20Logic%20Chips/Multiprocessors%20and%20Multicore%20Processors/Multiprocessors%20and%20Multicore%20Processors.md)



## Ref

