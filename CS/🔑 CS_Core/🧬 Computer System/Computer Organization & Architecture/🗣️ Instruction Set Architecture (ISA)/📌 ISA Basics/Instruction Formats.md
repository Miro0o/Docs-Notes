# Instruction Formats

[TOC]



## Res


## Intro
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
- Short instructions are typically better because they take up less space in memory and can be fetched quickly. However, this limits the number of instructions, because there must be enough bits in the instruction to specify the number of instructions we need. Shorter instructions also have tighter limits on the size and number of operands.

- Instructions of a fixed length are easier to decode but waste space.

- Memory organization affects instruction format. If memory has, for example, 16- or 32-bit words and is not byte addressable, it is difficult to access a single character. For this reason, even machines that have 16-, 32-, or 64-bit words are often byte addressable, meaning that every byte has a unique address even though words are longer than 1 byte.

- A fixed-length instruction does not necessarily imply a fixed number of operands. We could design an ISA with fixed overall instruction length but allow the number of bits in the operand field to vary as necessary. (This is called an expanding opcode and is covered in more detail in Section 5.2.5.)

- There are many different types of addressing modes. In Chapter 4, MARIE used two addressing modes: direct and indirect. However, we see in this chapter that a large variety of addressing modes exist.

- If words consist of multiple bytes, in what order should these bytes be stored on a byte-addressable machine? Should the least significant byte be stored at the highest or lowest byte address? This little versus big endian debate is discussed in the following section.

- How many registers should the architecture contain, and how should these registers be organized? How should operands be stored in the CPU?


## Instruction vs Data
### Data Organization
↗ [Data Representations & Storage in CS](../../../😤%20Number,%20Data%20and%20Math%20in%20Digital%20Systems/Data%20Representations%20&%20Storage%20in%20CS.md)

memory access
Little-endian/ Big-endian
Stack vs Register
etc.


### Instruction Organization
#### Operands
There can be variable operands for a single instruction.

The following are some common instruction formats based on different operands' numbers:

1. OPCODE only (zero addresses)  
2. OPCODE + 1 address (usually a memory address, e.g. `load x` )
3. OPCODE + 2 addresses (usually registers, or one register and one memory address, e.g. `add x y` )
4. OPCODE + 3 addresses (usually registers, or combinations of registers and memory, e.g. `add result a b` )

##### Stack & RPN (Reverse Polish Notation)
To operate on those variable-length operands, stack and RPN are often applied.

> 💡 **Operators & Operands order in operation expressions**
> 
> **Infix Notation**: x + y
> 
> **Prefix Notation**: + x y 
> 
> **Postfix Notation (RPN)**: x y +


#### Opcodes
We can expand the number of opcodes by lessening the number of operands without changing the length of an instruction:

![](../../../../../../Assets/Pics/Screenshot%202023-03-28%20at%205.32.13%20PM.png)


#### Instruction Length
Instructions on current architectures can be formatted in two ways:

1. **Fixed length**: Wastes space but is fast and results in better performance when instruction-level pipelining is used;

2. **Variable length**: More complex to decode but saves storage space.

> The number of operands has a direct impact on instruction length, as discussed above. However, we can also maintain a fixed instruction length by adding or reducing the number of opcodes according to the number of operands, as discussed above.



## Ref

