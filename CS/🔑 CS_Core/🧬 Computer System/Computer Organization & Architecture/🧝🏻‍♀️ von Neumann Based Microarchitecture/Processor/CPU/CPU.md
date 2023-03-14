# CPU

[TOC]



## Res
More about processor at [Computer Microprocessor](../../../../Microcomputer%20Principles%20&%20Interfaces/Computer%20Microprocessor.md). 



## Overview
### CPU in a von Neumann Model
![](../../../../../../../Assets/Pics/Pasted%20image%2020230302132111.png)
<small>The Modified von Neumann Architecture</small>

![](../../../../../../../Assets/Pics/Screenshot%202023-03-02%20at%204.11.10%20PM.png)
<small>Computer Components: Top-Level View</small>

Figure 1.1 depicts a simplified Von Neumann based compputer top-level components. 

One of the processor’s functions is to exchange data with memory. For this purpose, it typically makes use of two internal (to the processor) registers:
- a memory address register (**MAR**), which specifies the address in memory for the next read or write; 
- and a memory buffer register (**MBR**), which contains the data to be written into memory, or receives the data read from memory. 

Similarly:
- an I/O address register (**I/OAR**) specifies a particular I/O device. 
- an I/O buffer register (**I/OBR**) is used for the exchange of data between an I/O module and the processor.


### CPU Inside
![](../../../../../../../Assets/Pics/arch%20(1).jpg)
<small>Simplified von Neumann CPU Architecture</small>

![](../../../../../../../Assets/Pics/Pasted%20image%2020230304155503.png)
<small>Early von Neumann model as an SISD architecture</small>

#TODO 

#### ALU

#### Controller

#### Register


#### Inner Bus


## Word Length
>概括地讲，16位结构 (16 位机、字长为 16位等常见说法与16位结构的含义相同) 描述了一个CPU 具有下面几方面的结构特性。
>- 运算器一次最多可以处理16位的数据;
>- 寄存器的最大宽度为16位:
>- 寄存器和运算器之间的通路为16位。
 8086是16位结构的CPU，这也就是说，在8086内部，能够一次性处理、传输、暂时存储的信息的最大长度是16位的。内存单元的地址在送 上地址总线之前，必须在CPU中处理、传 输、暂时存放 ，对于16位CPU一次性处理、传输、暂时存储16位的地址。



## Clock
### Clock Speed 🆚 CPU Time (CPU Performance)



## Instruction and Data



## Instruction Execution
![](../../../../../../../Assets/Pics/Screenshot%202023-03-03%20at%209.05.51%20AM.png)

> Detailed info at ↗ [Instruction Processing](../Instruction%20Processing/Instruction%20Processing.md)


### Interupts
![](../../../../../../../Assets/Pics/Screenshot%202023-03-03%20at%209.10.54%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-03-03%20at%209.15.46%20AM.png)

↗ [Interupts](../Instruction%20Processing/Interupts.md)

