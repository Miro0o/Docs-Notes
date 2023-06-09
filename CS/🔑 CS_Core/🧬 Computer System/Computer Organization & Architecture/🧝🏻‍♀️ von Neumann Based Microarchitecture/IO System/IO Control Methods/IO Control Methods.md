# I/O Contorl Methods

[TOC]



## Res


## Overview
Peripheral devices are not connected directly to the CPU. Instead, there is an 🎳**interface** that handles the data transfers. This interface converts the system bus signals to and from a format that is acceptable to the given device. 

Because of the great differences in control methods and transmission modes among various kinds of I/O devices, it is infeasible to try to connect them directly to the system bus. Instead, ==**dedicated I/O modules** serve as interfaces between the CPU and its peripherals. ==

These modules perform many functions, including
- **controlling device actions**
- **buffering data**
- **performing error detection**
- **communicating with the CPU**.

> Although one method isn’t necessarily better than another, the manner in which a computer controls its I/O greatly influences overall system design and performance. The objective is to know when the I/O method employed by a particular computer architecture is appropriate to how that system will be used.


![](../../../../../../../Assets/Pics/Screenshot%202023-06-08%20at%201.38.09%20PM.png)


## Types of I/O Control Methods
### 1️⃣ Programmed (Instruction-Based) I/O 
↗ [Programmed (Instruction-Based) IO](Programmed%20(Instruction-Based)%20IO.md)


### 2️⃣ Interrupt-Driven I/O
↗ [Interrupt-Driven IO](Interrupt-Driven%20IO.md)


### 3️⃣ Memory-Mapped I/O
In **memory-mapped I/O**, the registers in the interface appear in the computer’s memory map, and there is no real difference between accessing memory and accessing an I/O device. 

**Pros & Cons**
Clearly, this is advantageous from the perspective of speed, but it uses up memory space in the system. 



### 4️⃣ Direct Memory Access (DMA)
↗ [Direct Memory Access (DMA)](Direct%20Memory%20Access%20(DMA).md)


### 5️⃣ Channel I/O
Use dedicated I/O processors.

**Pros**

**Cons**



## Ref

