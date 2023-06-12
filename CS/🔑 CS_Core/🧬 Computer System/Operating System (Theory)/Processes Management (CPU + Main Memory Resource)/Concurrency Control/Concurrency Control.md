# Concurrency Control

[TOC]



## Res



## Intro
### ⭐️ Concurrency: Fundamental OS Design
The central themes of operating system design are all concerned with the **management of processes and threads**:
- **Multiprogramming**: The management of multiple processes within a uniprocessor system;

- **Multiprocessing**: The management of multiple processes within a multiprocessor;

- **Distributed processing**: The management of multiple processes executing on multiple, distributed computer systems. The recent proliferation of clusters is a prime example of this type of system.

==Fundamental to all of these areas, and fundamental to OS design, is concurrency.==

> ❗❗❗ This section covers concurrency in **multiprogramming (多道程序处理)** and **multiprocessing（多处理系统）**. 
> 
> For distributed processing（分布式系统进程管理） move to ↗ [Distributed Process Management](../../../../../../../Software%20Engineering/🧠%20System%20Architecture%20Design/☯️%20Distributed%20Systems%20Design/Distributed%20Process%20Management/Distributed%20Process%20Management.md)


### Concurrency Scenarios
Concurrency arises in three different contexts:
1. **Multiple applications**: Multiprogramming was invented to allow processing time to be dynamically shared among a number of active applications.
 
2. **Structured applications**: As an extension of the principles of modular design and structured programming, some applications can be effectively programmed as a set of concurrent processes.

3. **Operating system structure**: The same structuring advantages apply to systems programs, and we have seen that operating systems are themselves often implemented as a set of processes or threads.

> 🔦 Two classic problems in concurrency are used to illustrate the concepts and compare the approaches presented in this chapter. 
> 
> View at ↗ [Concurrency Control Problem Models](Concurrency%20Control%20Problem%20Models/Concurrency%20Control%20Problem%20Models.md)


### Key Terms Related to Concurrency
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-06%20at%2012.46.42%20PM.png)



## ❤️‍🔥 Principles of Concurrency
> - In the case of a **uniprocessor system**, the reason we have a problem is that an interrupt can stop instruction execution anywhere in a process. 
> 
> - In the case of a **multiprocessor system**, we have that same condition and, in addition, a problem can be caused because two processes may be executing simultaneously and both trying to access the same global variable. 
>  
> ==However, the solution to both types of problem is the same: control access to the shared resource.==


### Race Condition
A race condition occurs when multiple processes or threads read and write data items so that the final result depends on the order of execution of instructions in the multiple processes.


### Operating System Concerns
1. The OS must be able to ==keep track of the various processes==.This is done with the use of **process control blocks** and was described in Chapter 4.
 
2. The OS must ==allocate and deallocate various resources== for each active process. At times, multiple processes want access to the same resource. These resources include
	- **Processor time**: This is the scheduling function, to be discussed in Part Four.
	- **Memory**: Most operating systems use a virtual memory scheme. The topic will be addressed in Part Three.
	- **Files**: To be discussed in Chapter 12
	- **I/O devices**: To be discussed in Chapter 11

3. The OS must ==protect the data and physical resources== of each process against unintended interference by other processes. This involves techniques that relate to memory, files, and I/O devices. A general treatment of protection found in Part Seven.

4. The functioning of a process, and the output it produces, must ==be independent of the speed== at which its execution is carried out relative to the speed of other concurrent processes. This is the subject of this chapter.


### ⭐️ Process Interaction Relations
![](../../../../../../../../Assets/Pics/Screenshot%202023-04-06%20at%201.09.44%20PM.png)

Conditions will not always be as clear-cut as suggested in figure above. Rather, several processes may exhibit aspects of both competition and cooperation. Nevertheless, it is productive to examine each of the three items in the preceding list separately and determine their implications for the OS.


#### 1️⃣ Competition for Resources (Unaware)
Mutual exclusion at ↗ [Mutual Exclusive & Synchronization (互斥与同步)](Mutual%20Exclusive%20&%20Synchronization%20(互斥与同步).md)


#### 2️⃣ Cooperation by Sharing (Indirectly Aware)
Synchronization at ↗ [Mutual Exclusive & Synchronization (互斥与同步)](Mutual%20Exclusive%20&%20Synchronization%20(互斥与同步).md)


#### 3️⃣ Cooperation by Communication (Directly Aware)
A broad topic at ↗ [IPC (Inter Process Communication)](../IPC%20(Inter%20Process%20Communication)/IPC%20(Inter%20Process%20Communication).md)



## Mutual Exclusive & Synchronization (互斥与同步)
To achieve concurrency control, the key is to achieve **mutual exclusive**.

> **Mutual exclusive**: two process A & B mutual exclusively access a shared resource (critical resource)
> 
> **Synchronization**: two process A & B, being mutual exclusively accessing a shared resource, have sequential requirement in accessing & execution. 
>
> 互斥就是不同时访问；同步就是在不同时访问的基础上加入访问顺序的要求。同步可以看作是一种条件互斥。
> 
> 举个例子，有两个进程A 和B 并发访问临界资源C。在互斥的要求下，可以A先访问C，B再访问C，也可以B先访问C，A再访问C；但是在同步的要求下，只能是根据同步的要求，A先访问C，或B先访问，两种情况只有一个是合法的（具体哪个合法取决于同步的要求）
> 
> 同步可以看作是一种条件互斥，此时的互斥额外的条件是要满足时序要求。时序可以是逻辑上的（大象放入冰箱有三步），也可以是物理上的（系统的物理资源的分配）


The cases of synchronization are subset of cases of mutual exclusive. 

↗ [Mutual Exclusive & Synchronization (互斥与同步)](Mutual%20Exclusive%20&%20Synchronization%20(互斥与同步).md)



## IPC
↗ [IPC (Inter Process Communication)](../IPC%20(Inter%20Process%20Communication)/IPC%20(Inter%20Process%20Communication).md)



## Deadlock and Starvation
Deadlock and starvation are two most basic & important issues occurred in concurrency, or in our dealing with concurrency. Specifically, deadlock and starvation and issues alike arise mainly because of the **scheduling algorithms** adopted when addressing such concurrency issues.

↗ [Deadlock & Starvation](Deadlock%20&%20Starvation/Deadlock%20&%20Starvation.md)
↗ [Scheduling & Resource Management](../../Scheduling%20&%20Resource%20Management/Scheduling%20&%20Resource%20Management.md)



## Ref
关于并发中的互斥和同步的关系，我感觉自己没有完全理解；而且IPC和并发两个情景下有一些技术重合了，这让我对他们之间的关系有点困惑。

下面是我的理解：

> 并发的根本问题是对共享有限资源的访问控制。课程中讲的并发属于进程间的并发，而考虑进程间的并发需要首先讨论进程间的关系。进程间有三种关系：unaware； indirectly aware； directly aware。 不同的进程关系下的并发所涉及到的控 制问题是不一样的，我们可以分别考虑这些不同的控制问题，这样就可以解决不同进程关系下的并发问题。
> 
> 在第三种进程关系中（directly aware），进程间直接通讯，这统称为IPC；实现IPC可以有以下方法：<font color="red">消息传递（消息队列，管道，信号）；同步（锁，信号量）</font>；共享内存；RPC。
>  
> 而不论在哪种进程关系下，控制问题可以一共分为以下几类：死锁和饥饿（本周讨论的，有几种解决方案，这里略过）；<font color="red">互斥（互斥锁和条件变量，自旋锁）；同步（信号量，管程）</font>；
> 
> 要解决并发问题，只需要解决对应进程关系下的控制问题既可。

在上面的控制问题和IPC中，互斥和同步的部分有一些重合和矛盾的地方（红色字体标出），这让我困惑。


[生产者消费者问题、读者写者问题、哲学家问题细致讲解 | CSDN]: https://blog.csdn.net/weixin_45488428/article/details/112666217
[消息队列：生产者/消费者模式 | CSDN]: https://blog.csdn.net/qq_39575279/article/details/87940298?ydreferer=aHR0cHM6Ly9jbi5iaW5nLmNvbS8%3D

[并发编程的三大核心问题 -《深入理解高并发编程》| 腾讯云]: https://cloud.tencent.com/developer/article/2050512

