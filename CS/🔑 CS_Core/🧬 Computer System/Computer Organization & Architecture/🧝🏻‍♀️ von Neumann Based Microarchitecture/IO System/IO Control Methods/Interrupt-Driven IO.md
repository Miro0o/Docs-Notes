# Interrupt-Driven IO

[TOC]



## Res


## Intro

An alternative, known as interrupt-driven I/O, is for the processor to issue an I/O command to a module then go on to do some other useful work. The I/O module will then interrupt the processor to request service when it is ready to exchange data with the processor. The processor then executes the data transfer, as before, and resumes its former processing.

**Pros & Cons**
Interrupt-driven I/O, though more efficient than simple programmed I/O, still requires the active intervention of the processor to transfer data between memory and an I/O module, and any data transfer must traverse a path through the processor. Thus, both of these forms of I/O suffer from two inherent drawbacks:
1.  The I/O transfer rate is limited by the speed with which the processor can test and service a device.

3.  The processor is tied up in managing an I/O transfer; a number of instructions must be executed for each I/O transfer.




## Ref

