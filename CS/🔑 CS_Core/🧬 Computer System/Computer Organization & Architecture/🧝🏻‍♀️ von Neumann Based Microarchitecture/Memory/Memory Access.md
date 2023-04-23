# Memory Access

[TOC]



## Res




## Overview
![](../../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2010.19.55%20AM.png)

### Memory Access Implementations
↗ [8086CPU ASM](../../../../👩‍💻%20Languages%20Programming/ASM/X86%20ISA%20Based%20ASM/8086CPU%20ASM.md)


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


### Address Unit
Byte Addressable 
Byte Unit /Address Unit (in most modern computers the address unit equates to byte unit for compatibility reasons)

Word Addressable
Word Unit /Memory Unit

Memory Interleaving
high-order interleaving
low-order interleaving


### 📳 Addressing Modes
#### Immediate Addressing
Immediate addressing is so named because the value to be referenced immediately follows the operation code in the instruction. That is to say, the data to be operated on is part of the instruction.

#### Direct Addressing
Direct addressing is so named because the value to be referenced is obtained by specifying its memory address directly in the instruction.

> **Register Addressing**
> 
> In register addressing, a register, instead of memory, is used to specify the operand. This is similar to direct addressing, except that instead of a memory address, the address field contains a register reference. The contents of that register are used as the operand.

#### Indirect Addressing
Indirect addressing is a powerful addressin mode that provides an exceptional level of flexibility. In this mode, the bits in the address field specify a memory address that is to be used as a pointer. The effective address of the operand is found by going to this memory address.

> **Register Indirect Addressing**
> 
> In a variation on this scheme, the operand bits specify a register instead of a memory address. This mode, known as register indirect addressing, works exactly the same way as indirect addressing mode, except that it uses a register instead of a memory address to point to the data.

#### Index Addressing & Based Addressing
1️⃣ In **indexed addressing** mode, an index register (either explicitly or implicitly designated) is used to store an offset (or displacement), which is added to the operand, resulting in the effective address of the data.

2️⃣ **Based addressing** mode is similar, except that a base address register, rather than an index register, is used. In theory, the difference between these two modes is in how they are used, not how the operands are computed. An index register holds an index that is used as an offset, relative to the address given in the address field of the instruction. A base register holds a base address, where the address field represents a displacement from this base. 

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
