# Concurrency

[TOC]



## Res



## Intro
### ⭐️ Concurrency: Foundamental OS Design

> ❗❗❗ This section covers concurrency in multiprogramming (多道程序处理) and multiprocessing（多处理系统）. For distributed processing（分布式系统进程管理） move to ↗ [Distributed Process Management](../../../../../Software%20Engineering/🧠%20System%20Architecture%20Design/Distributed%20Systems/☯️%20Distributed%20Systems%20Design/Distributed%20Process%20Management/Distributed%20Process%20Management.md)

The central themes of operating system design are all concerned with the **management of processes and threads**:
- **Multiprogramming**: The management of multiple processes within a uniprocessor system;

- **Multiprocessing**: The management of multiple processes within a multiprocessor;

- **Distributed processing**: The management of multiple processes executing on multiple, distributed computer systems. The recent proliferation of clusters is a prime example of this type of system.

==Fundamental to all of these areas, and fundamental to OS design, is concurrency.==


### Concurrency Scenarios
Concurrency arises in three different contexts:
1. **Multiple applications**: Multiprogramming was invented to allow processing time to be dynamically shared among a number of active applications.
 
2. **Structured applications**: As an extension of the principles of modular design and structured programming, some applications can be effectively programmed as a set of concurrent processes.

3. **Operating system structure**: The same structuring advantages apply to systems programs, and we have seen that operating systems are themselves often imple- mented as a set of processes or threads.

> 🔦 Two classic problems in concurrency are used to illustrate the concepts and compare the approaches presented in this chapter. 
> 1. The producer/consumer problem 👉 #TODO 
> 2. The readers/writers problem 👉 #TODO 


### Key Terms Related to Concurrency
![](../../../../../../Assets/Pics/Screenshot%202023-04-06%20at%2012.46.42%20PM.png)



## ❤️‍🔥 Principles of Concurrency
> - In the case of a uniprocessor system, the reason we have a problem is that an interrupt can stop instruction execution anywhere in a process. 
> 
> - In the case of a multiprocessor system, we have that same condition and, in addition, a problem can be caused because two processes may be executing simultaneously and both trying to access the same global variable. 
>  
> ==However, the solution to both types of problem is the same: control access to the shared resource.==


### Race Condition
A race condition occurs when multiple processes or threads read and write data items so that the final result depends on the order of execution of instructions in the multiple processes.


### Operating System Concerns
1. The OS must be able to ==keep track of the various processes==.This is done with the use of process control blocks and was described in Chapter 4.
 
2. The OS must ==allocate and deallocate various resources== for each active process. At times, multiple processes want access to the same resource. These resources include
	- **Processor time**: This is the scheduling function, to be discussed in Part Four.
	- **Memory**: Most operating systems use a virtual memory scheme. The topic will be addressed in Part Three.
	- **Files**: To be discussed in Chapter 12
	- **I/O devices**: To be discussed in Chapter 11

3. The OS must ==protect the data and physical resources== of each process against unintended interference by other processes. This involves techniques that relate to memory, files, and I/O devices. A general treatment of protection found in Part Seven.

4. The functioning of a process, and the output it produces, must ==be independent of the speed== at which its execution is carried out relative to the speed of other concurrent processes. This is the subject of this chapter.


### Process Interaction
![](../../../../../../Assets/Pics/Screenshot%202023-04-06%20at%201.09.44%20PM.png)

Conditions will not always be as clear-cut as suggested in Table 5.2. Rather, sev- eral processes may exhibit aspects of both competition and cooperation. Neverthe- less, it is productive to examine each of the three items in the preceding list separately and determine their implications for the OS.


#### Competition for Resources

#### Cooperation by Sharing

#### Cooperation by Communication



## ☯️ Mutual Exclusion (Busy Waiting)
==The basic requirement for support of concurrent processes is the ability to enforce mutual exclusion;== that is, the ability to exclude all other processes from a course of action while one process is granted that ability.


### Mutual Exclusion: Requirements
Any facility or capability that is to provide support for mutual exclusion should meet the following requirements:
1. Mutual exclusion must be enforced: Only one process at a time is allowed into its critical section, among all processes that have critical sections for the same resource or shared object.

2. A process that halts in its noncritical section must do so without interfering with other processes.

3. It must not be possible for a process requiring access to a critical section to be delayed indefinitely: no deadlock or starvation.

4. When no process is in a critical section, any process that requests entry to its critical section must be permitted to enter without delay.

5. Noassumptionsaremadeaboutrelativeprocessspeedsornumberofprocessors.

6. A process remains inside its critical section for a finite time only.


### Mutual Exclusion: Approaches
1. One approach is to leave the responsibility with the processes that wish to execute concurrently. (**process self-discretion**)
2. A second approach involves the use of special-purpose machine instructions. (**hardware level**)
3. A third approach is to provide some level of support within the OS or a programming language. (**system software level**)


#### Mutual exclusion: software approach
##### 1️⃣ Dekker’s Algorithm


##### 2️⃣ Peterson’s Algorithm


#### Mutual exclusion: hardware approach
##### 1️⃣ Interrupt Disabling


##### 2️⃣ Special Machine Instructions


## Concurrency Mechanisms without Busy Waiting
These are down at **OS & programming language level**. To list the most important approaches:

↗ [Semaphore](Semaphore/Semaphore.md)

↗ [Monitors](Monitors/Monitors.md)

↗ [Message Passing](Message%20Passing/Message%20Passing.md)



![](../../../../../../Assets/Pics/Screenshot%202023-04-06%20at%201.50.54%20PM.png)



## Ref

