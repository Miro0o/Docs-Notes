# I/O Contorl Methods

[TOC]



## Res


## Overview
Peripheral devices are not connected directly to the CPU. Instead, there is an 🎳**interface** that handles the data transfers. This interface converts the system bus signals to and from a format that is acceptable to the given device. 

Because of the great differences in control methods and transmission modes among various kinds of I/O devices, it is infeasible to try to connect them directly to the system bus. Instead, dedicated I/O modules serve as interfaces between the CPU and its peripherals. 

These modules perform many functions, including
- **controlling device actions**
- **buffering data**
- **performing error detection**
- **communicating with the CPU**.

> Although one method isn’t necessarily better than another, the manner in which a computer controls its I/O greatly influences overall system design and performance. The objective is to know when the I/O method employed by a particular computer architecture is appropriate to how that system will be used.



## Programmed (Instruction-Based) I/O 

> With **instruction-based I/O**, the CPU has specialized instructions that perform the input and output. Although this does not use memory space, it requires specific I/O instructions, which implies that it can be used only by CPUs that can execute these specific instructions
> 
> When the processor is executing a program and encounters an instruction relating to I/O, it executes that instruction by issuing a command to the appropriate I/O module. 


In the case of programmed I/O, the I/O module performs the requested action, then sets the appropriate bits in the I/O status register but takes no further action to alert the processor. In particular, it does not interrupt the processor. Thus, after the I/O instruction is invoked, the processor must take some active role in determining when the I/O instruction is completed. For this purpose, the processor periodically checks (polls, 轮询) the status of the I/O module until it finds that the operation is complete.

With programmed I/O, the processor has to wait a long time for the I/O module of concern to be ready for either reception or transmission of more data. The processor, while waiting, must repeatedly **interrogate** the status of the I/O module. As a result, the performance level of the entire system is severely degraded.

**Pros**

**Cons**



## Interrupt-Driven I/O
An alternative, known as interrupt-driven I/O, is for the processor to issue an I/O command to a module then go on to do some other useful work. The I/O module will then interrupt the processor to request service when it is ready to exchange data with the processor. The processor then executes the data transfer, as before, and resumes its former processing.

Interrupt-driven I/O, though more efficient than simple programmed I/O, still requires the active intervention of the processor to transfer data between memory and an I/O module, and any data transfer must traverse a path through the processor. Thus, both of these forms of I/O suffer from two inherent drawbacks:
1.  The I/O transfer rate is limited by the speed with which the processor can test and service a device.

3.  The processor is tied up in managing an I/O transfer; a number of instructions must be executed for each I/O transfer.

**Pros**

**Cons**



## Memory-Mapped I/O
In **memory-mapped I/O**, the registers in the interface appear in the computer’s memory map, and there is no real difference between accessing memory and accessing an I/O device. Clearly, this is advantageous from the perspective of speed, but it uses up memory space in the system. 


**Pros**

**Cons**



## Direct Memory Access (DMA)
The DMA function can be performed by a separate module on the system bus, or it can be incorporated into an I/O module.

It works by cpu sending DMA modules following commands:
- Whether a read or write is requested
- The address of the I/O device involved
- The starting location in memory to read data from or write data to
- The number of words to be read or written

The processor is hence involved only at the beginning and end of the transfer.

The DMA module needs to take control of the bus to transfer data to and from memory. Because of this competition for bus usage, there may be times when the processor needs the bus and must wait for the DMA module. Note this is not an interrupt; the processor does not save a context and do something else. Rather, the processor pauses for one bus cycle (the time it takes to transfer one word across the bus). The overall effect is to cause the processor to execute more slowly during a DMA transfer when processor access to the bus is required.

**Pros**

**Cons**



## Channel I/O
Use dedicated I/O processors.

**Pros**

**Cons**



## Ref

