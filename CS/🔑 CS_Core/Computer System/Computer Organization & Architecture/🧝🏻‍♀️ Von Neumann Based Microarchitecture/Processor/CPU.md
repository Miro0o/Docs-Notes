# CPU

[TOC]



## Res
More about processor at [Microprocessor](../../👶🏽%20Basics/Microprocessor.md). 



## Intro
### CPU in a von Neumann Model
![](../../../../../../Assets/Pics/Pasted%20image%2020230302132111.png)
<small>The Modified von Neumann Architecture</small>

![](../../../../../../Assets/Pics/Screenshot%202023-03-02%20at%204.11.10%20PM.png)
<small>Computer Components: Top-Level View</small>

Figure 1.1 depicts a simplified Von Neumann based compputer top-level components. 

One of the processor’s functions is to exchange data with memory. For this purpose, it typically makes use of two internal (to the processor) registers:
- a memory address register (**MAR**), which specifies the address in memory for the next read or write; 
- and a memory buffer register (**MBR**), which contains the data to be written into memory, or receives the data read from memory. 

Similarly:
- an I/O address register (**I/OAR**) specifies a particular I/O device. 
- an I/O buffer register (**I/OBR**) is used for the exchange of data between an I/O module and the processor.


### CPU Inside
![](../../../../../../Assets/Pics/arch%20(1).jpg)
<small>Simplified CPU Architecture</small>

#TODO 



## Instruction Execution
![](../../../../../../Assets/Pics/Screenshot%202023-03-03%20at%209.05.51%20AM.png)

### Fetch


### Execute 


### Halt


### Interupts

![](../../../../../../Assets/Pics/Screenshot%202023-03-03%20at%209.10.54%20AM.png)

![](../../../../../../Assets/Pics/Screenshot%202023-03-03%20at%209.15.46%20AM.png)

↗ [Interupts](Interupts.md)
