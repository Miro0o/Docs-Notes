# Memory Access

[TOC]



## Res




## Overview
![](../../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2010.19.55%20AM.png)

### Memory Access Implementations
↗ [8086 ASM](../../../../👩‍💻%20Languages%20Programming/ASM/X86%20ISA%20Based%20ASM/8086%20ASM/8086%20ASM.md)


### Memory Notation
#TODO 


### Memory Cards /Chips
![](../../../../../../Assets/Pics/Screenshot%202023-03-01%20at%2011.08.01%20AM.png)
#TODO 



## 🆚 Instructions and Data
Instructions and Data are all values stored in memory. It depends on the CPU to interpret them as what they meant to be useful. 
Flow links above to dive deep, including how they are formatted, how they are accessed and more.


### Instructions Types
↗ [Instruction Types](../../🗣️%20Instruction%20Set%20Architecture%20(ISA)/📌%20ISA%20Basics/Instruction%20Types.md)


### Data Types
↗ [Data Representations & Storage in CS](../../../😤%20Number,%20Data%20and%20Math%20in%20Digital%20Systems/Data%20Representations%20&%20Storage%20in%20CS.md)


### Effective Address 



## 📬 Addressing
### Memory Space Address
![](../../../../../../Assets/Pics/Screenshot%202023-03-01%20at%2011.08.25%20AM.png)


### Addressing Unit
#### Byte Unit
Byte Addressable 
Byte Unit /Address Unit (in most modern computers the address unit equates to byte unit for compatibility reasons)

#### Word Unit
Word Addressable
Word Unit /Memory Unit


### Memory Interleaving
> 🔗 https://www.geeksforgeeks.org/types-of-memory-interleaving/

**Memory interleaving** is an abstraction technique which divides memory into a number of modules such that successive words in the address space are placed in the different module. (This is because, very often, the memory is discrete in physical level but has to be continuous at logical level)

It is also known as **Memory Banking**.


Suppose a 64 MB memory made up of the 4 MB chips as shown in the below:
![](https://media.geeksforgeeks.org/wp-content/uploads/20200422161611/1406-4.png)
We organize the memory into 4 MB banks, each having eight of the 4 MB chips. The memory thus has 16 banks, each of 4 MB.

64 MB memory = 2^26, so 26 bits are used for addressing.  
16 = 2^4, so 4 bits of address select the bank, and 4 MB = 2^22, so 22 bits of address to each chip.

In general, an N-bit address, with N = L + M, is broken into two parts:
1.  L-bit bank select, used to activate one of the 2^L banks of memory, and
2.  M-bit address that is sent to each of the memory banks.

When one of the memory banks is active, the other (2L – 1) are inactive. All banks receive the M-bit address, but the inactive one do not respond to it.


#### High-order Interleaving
In high-order interleaving, the most significant bits of the address select the memory chip. The least significant bits are sent as addresses to each chip. One problem is that consecutive addresses tend to be in the same chip. The maximum rate of data transfer is limited by the memory cycle time.

![](https://media.geeksforgeeks.org/wp-content/uploads/20200422161657/223-1.png)


#### Low-order Interleaving
In low-order interleaving, the least significant bits select the memory bank (module). In this, consecutive memory addresses are in different memory modules. This allows memory access at much faster rates than allowed by the cycle time

![](https://media.geeksforgeeks.org/wp-content/uploads/20200422161737/3164-1.png)



### 📳 Addressing Modes
#### Immediate Addressing
Immediate addressing is so named because the value to be referenced immediately follows the operation code in the instruction. That is to say, the data to be operated on is part of the instruction.

#### Direct Addressing
Direct addressing is so named because the value to be referenced is obtained by specifying its memory address directly in the instruction.

> **Register Addressing**
> 
> In register addressing, a register, instead of memory, is used to specify the operand. This is similar to direct addressing, except that instead of a memory address, the address field contains a register reference. The contents of that register are used as the operand.

#### Indirect Addressing
Indirect addressing is a powerful addressing mode that provides an exceptional level of flexibility. In this mode, the bits in the address field specify a memory address that is to be used as a pointer. The effective address of the operand is found by going to this memory address.

> **Register Indirect Addressing**
> 
> In a variation on this scheme, the operand bits specify a register instead of a memory address. This mode, known as register indirect addressing, works exactly the same way as indirect addressing mode, except that it uses a register instead of a memory address to point to the data.

#### Index Addressing & Based Addressing
1️⃣ In **indexed addressing** mode, an **index register** (either explicitly or implicitly designated) is used to store an offset (or displacement), which is added to the operand, resulting in the effective address of the data.

2️⃣ **Based addressing** mode is similar, except that a **base address register**, rather than an index register, is used. In theory, the difference between these two modes is in how they are used, not how the operands are computed. An index register holds an index that is used as an offset, relative to the address given in the address field of the instruction. A base register holds a base address, where the address field represents a displacement from this base. 

These two addressing modes are quite useful for accessing array elements as well as characters in strings. In fact, most assembly languages provide special index registers that are implied in many string operations. Depending on the instruction-set design, general-purpose registers may also be used in this mode.

#### Stack Addressing 
If stack addressing mode is used, the operand is assumed to be on the stack. We have already seen how this works in Section 5.2.4.


#### 💦 Variations on Above Schemes
> Additional modes exist; however, familiarity with immediate, direct, register, indirect, indexed, and stack addressing modes goes a long way in understanding any addressing mode you may encounter.

##### Indirect Indexed Addressing
indirect indexed addressing uses both indirect and indexed addressing at the same time.

##### Base/Offset Addressing
Base/offset addressing adds an offset to a specific base register and then adds this to the specified operand, resulting in the effective address of the actual operand to be used in the instruction.

##### Self-relative Addressing
Self-relative addressing computes the address of the operand as an offset from the current instruction.



## Ref
