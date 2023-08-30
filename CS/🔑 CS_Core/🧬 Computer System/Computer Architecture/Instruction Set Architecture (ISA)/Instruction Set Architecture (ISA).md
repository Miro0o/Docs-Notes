# Instruction Set Architecture (ISA)

[TOC]



## Res
Dive deep beginning with ↗ [Instruction Formats](📌%20Instruction%20Basics/Instruction%20Formats.md)

The implementation of an ISA is referred to as "Microprocessor". This part is available at ↗ [Microcomputer Principles & Interfaces /Computer Microarchitectures](../Computer%20Microarchitectures%20(Computer%20Organization)/Computer%20Microarchitectures%20(Computer%20Organization).md).

Instruction in action: ↗ [CPU Under von Neumann Architecture /Instruction Processing](📌%20Instruction%20Basics/Instruction%20Execution/Instruction%20Execution.md)



## Overview
> 👉 quick look at [👧🏽 MARIE](../Computer%20Microarchitectures%20(Computer%20Organization)/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/👧🏽%20MARIE.md) for gists of ISA

The instruction set architecture (ISA) of a machine specifies the instructions that the computer can perform and the format for each instruction. The ISA is essentially an interface between the software and the hardware. Some ISAs include hundreds of instructions.

![](../../../../../../../Assets/Pics/Screenshot%202023-03-21%20at%209.12.25%20PM.png)
<small>Instruction Processing Level</small>


### Instruction & ISA
↗ [Instruction Basics](📌%20Instruction%20Basics/Instruction%20Basics.md)

↗ [ISA Basics](📌%20ISA%20Basics/ISA%20Basics.md)


### Brief History of ISA Development
↗ [History of ISA](📌%20ISA%20Basics/History%20of%20ISA.md)


### ISA Taxonomy
↗ [CISC](CISC/CISC.md)
↗ [RISC](RISC/RISC.md)
↗ [VLIW](VLIW/VLIW.md)




## 🎨 ISA Design Decisions
### ISA Design Principles
Specifically, instruction sets are differentiated by the following features:
1. Operand storage (data can be stored in a stack structure or in registers or both)

2. Number of explicit operands per instruction (zero, one, two, and three being the most common)

3. Operand location (instructions can be classified as register-to-register, register-to-memory, or memory-to-memory, which simply refer to the combinations of operands allowed per instruction)

4. Operations (including not only types of operations but also which instructions can access memory and which cannot)

5. Type and size of operands (operands can be addresses, numbers, or even characters)


### ISA Measure Metrics
Instruction set architectures are measured by several different factors, including 
1. The amount of **space** a program requires;
2. The **complexity** of the instruction set, in terms of the amount of decoding necessary to execute an instruction and the complexity of the tasks performed by the instructions;
3. The **length** of the instructions;
4. The **total number** of instructions.


### ISA Considerations
- **Instruction length.** Short instructions are typically better because they take up less space in memory and can be fetched quickly. However, this limits the number of instructions, because there must be enough bits in the instruction to specify the number of instructions we need. Shorter instructions also have tighter limits on the size and number of operands.
	- Instructions of a fixed length are easier to decode but waste space.

- **Memory organization affects instruction format**. If memory has, for example, 16- or 32-bit words and is not byte addressable, it is difficult to access a single character. For this reason, even machines that have 16-, 32-, or 64-bit words are often byte addressable, meaning that every byte has a unique address even though words are longer than 1 byte.

- **A fixed-length instruction does not necessarily imply a fixed number of operands**. We could design an ISA with fixed overall instruction length but allow the number of bits in the operand field to vary as necessary. (This is called an **expanding opcode** and is covered in more detail in Section 5.2.5.)

- **There are many different types of addressing modes**. In Chapter 4, MARIE used two addressing modes: direct and indirect. However, we see in this chapter that a large variety of addressing modes exist.

- **Byte order**. If words consist of multiple bytes, in what order should these bytes be stored on a byte-addressable machine? Should the least significant byte be stored at the highest or lowest byte address? This little versus big endian debate is discussed in the following section.

- How many registers should the architecture contain, and how should these registers be organized? How should operands be stored in the CPU?



## Ref
[Intel和AMD 与 x86，ARM，MIPS有什么区别？ - 零度君的回答 - 知乎]: https://www.zhihu.com/question/63627218/answer/211243489

[Instructions in ISA and microinstructions?]: https://softwareengineering.stackexchange.com/questions/273870/instructions-in-isa-and-microinstructions

[Comparison of instruction set architectures]: https://en.wikipedia.org/wiki/Comparison_of_instruction_set_architectures

