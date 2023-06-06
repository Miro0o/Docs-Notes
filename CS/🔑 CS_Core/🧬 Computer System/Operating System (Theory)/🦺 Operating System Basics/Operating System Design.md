# Operating System Design

[TOC]



## Res
[Development(History) of Operating Systems](Development(History)%20of%20Operating%20Systems.md)


## Overview
Two operating system components are crucial: the **kernel** and the **system programs**
- As the core of the operating system, the kernel performs scheduling, synchronization, memory management, interrupt handling, and it provides security and protection.

Four main factors drive operating system design: performance, power, cost, and compatibility


### OS System Types
#### Microkernel Systems (微内核系统)
Key features of microkernel design are its smaller size, easy portability, and the array of services that run a layer above the kernel instead of in the kernel itself.

- Microkernels provide **rudimentary operating system functionality**, relying on other **modules** to perform specific tasks, thus moving many typical operating system services into user space. This permits many services to be restarted or reconfigured without restarting the entire operating system. 
- Microkernels provide security, because services running at the user level have restricted access to system resources. 
- Microkernels can be customized and ported to other hardware more easily than monolithic kernels. 
- However, additional communication between the kernel and the other modules is necessary, often resulting in a slower and less efficient system. 

Microkernel development has been significantly encouraged by the growth in SMP and other multiprocessor systems. Examples of microkernel operating systems include MINIX, Mach, and QNX.


#### Monolithic Systems (宏内核系统)
Monolithic kernels provide all their essential functionality through a **single process**. Consequently, they are significantly larger than microkernels. Typically targeted for specific hardware, monolithic kernels interact directly with the hardware, so they can be optimized more easily than can microkernel operating systems. It is for this reason that monolithic kernels are not easily portable. 

Examples of monolithic kernel operating systems include Linux, MacOS, and DOS.



## Developments Leading to Modern Operating Systems

The rate of change in the demands on operating systems requires not just modifications and enhancements to existing architectures, but new ways of organizing the OS. A wide range of different approaches and design elements has been tried in both experimental and commercial operating systems, but much of the work fits into the following categories:

- Microkernel architecture
- Multithreading
- Symmetric multiprocessing
- Distributed operating systems
- Object-oriented design

#TODO 

### Microkernel Architecture (微内核系统)


### Multithreading 


### Symmetric Multiprocessing


### Distributed Operating Systems


### Object-Oriented Design



## OS Design Considerations for Multiprocessor and Multicore
#TODO 







## Ref