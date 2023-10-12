# Operating System Services 

[TOC]



## Res



## Overview
As we have mentioned, the operating system is an important interface to the underlying hardware, both for users and for application programs. In addition to its role as an interface, it has three principal tasks. Process management is perhaps the most interesting of these three. The other two are system resource management and protection of those resources from errant processes.



## 🥺 The Operating System as an Interface
### 1️⃣ User Interface
#### CLI


#### GUI



### 2️⃣ System Interface
#### Program Development

#### Program Execution

#### Access to I/O Devices

#### Controlled Access to Files

#### System Access

#### Error Detection and Response

#### Accounting



### Three Key Interfaces in a Typical Computer System
#### ISA
↗ [Instruction Set Architecture (ISA)](../../Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)/Instruction%20Set%20Architecture%20(ISA).md)

#### ABI
↗ [ABI (Application Binary Interface)](../../Computer%20Interfaces/ABI%20(Application%20Binary%20Interface)/ABI%20(Application%20Binary%20Interface).md)

#### API



## 🦮 The Operating System as a Resource Manager
![](../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2012.25.57%20AM.png)

### Resource Management in General
↗ [Processes Management (CPU + Main Memory Resource)](../Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource)/Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource).md)
↗ [Memory Management (Main Memory + Secondary Memory Resource)](../Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource).md)
↗ [IO System](../IO%20System/IO%20System.md)


### Resource Scheduling
↗ [Scheduling & Resource Management](../Scheduling%20&%20Resource%20Management/Scheduling%20&%20Resource%20Management.md)


### Resource Security & Protection
#### 📜 Protected Environments and the Evolution of Systems Architectures
##### Server Farm


##### Server Consolidation Product


#### Virtual Machines
↗ [Virtualization Theory](../../🚀%20Virtualization%20Theory/Virtualization%20Theory.md)


#### Subsystems & Partitions
Although subsystems and partitions are different from each other in how they define their constituent resources, you can think of both as being mini-models of the layered system architecture of a computer system.
- In the case of a partitioned environment, the levels would look like adjacent layered birthday cakes, extending from the hardware level to the application level. 
- Subsystems, on the other hand, are not so distinct from one another, with most of the differences taking place at the system software level.

##### Subsystems


##### LPARs (Logical Partition)
In very large computer systems, subsystems do not go far enough in segmenting the machine and its resources.

Sometimes a more sophisticated barrier is required to facilitate security and resource management. In these instances, a system may be broken up into logical partitions, sometimes called LPARs, as illustrated in Figure 8.4. LPARs create distinct machines within one physical system, with nothing implicitly shared between them. The resources of one partition are no more accessible to another partition than if the partitions were running on physically separate systems. For example, if a system has two partitions, A and B, partition A can read a file from partition B only if both partitions agree to establish a mutually shared resource, such as a pipe or message queue. Generally speaking, files can be copied between partitions only through the use of a file transfer protocol or a utility written for this purpose by the system vendor.

Logical partitions are especially useful in creating “sandbox” environments for user training or testing new programs. Sandbox environments get their name from the idea that anyone using these environments is free to “play around” to his or her heart’s content, as long as this playing is done within the confines of the sandbox. Sandbox environments place strict limits on the accessibility of system resources. Processes running in one partition can never intentionally or inadvertently access data or processes resident in other partitions. Partitions thus raise the level of security in a system by isolating resources from processes that are not entitled to use them.




## Ref
[操作系统原理——第2章 操作系统概述]: https://blog.csdn.net/tangkcc/article/details/114852154
