# Register

[TOC]



## Overview
#TODO 

We saw in Chapter 3 that D flip-flops can be used to implement registers. One D flip-flop is equivalent to a 1-bit register, so a collection of D flip-flops is necessary to store multi-bit values. For example, to build a 16-bit register, we need to connect 16 D flip-flops together. These collections of flip-flops must be clocked to work in unison. At each pulse of the clock, input enters the register and cannot be changed (and thus is stored) until the clock pulses again.

Data processing on a computer is usually done on fixed-size binary words stored in registers. Therefore, most computers have registers of a certain size. Common sizes include 16, 32, and 64 bits. The number of registers in a machine varies from architecture to architecture, but is typically a power of 2, with 16, 32, and 64 being most common. 

Registers contain data, addresses, or control information. Some registers are specified as “special purpose” and may contain only data, only addresses, or only control information. Other registers are more generic and may hold data, addresses, and control information at various times.



## Memory Access
Refer to
↗ [8086 ASM](../../../../../👩‍💻%20Languages%20Programming/ASM/X86%20ISA%20Based%20ASM/8086%20ASM/8086%20ASM.md)
↗ [Memory Access](../../../../Computer%20Organization%20&%20Architecture/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Memory/Memory%20Access.md)


## Word in Register


## Ref

