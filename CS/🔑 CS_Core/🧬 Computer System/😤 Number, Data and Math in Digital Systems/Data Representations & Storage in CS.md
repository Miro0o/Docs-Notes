# Data Representaion in CS

[TOC]



## Res
Go to ↗ [von Neumann Arch /Memory](../Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Memory/Memory.md) for more possible info.
And maybe ↗ [8086 ASM](../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/x86%20ISA%20Based%20ASM/8086%20ASM/8086%20ASM.md).

↗ [Instruction Set Architecture (ISA)](../Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)/Instruction%20Set%20Architecture%20(ISA).md)
↗ [Memory Access](../Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Memory/Memory%20Access.md)



## Data Representation Basics 
![](../../../../Assets/Pics/Screenshot%202023-06-24%20at%209.50.38%20PM.png)
![](../../../../Assets/Pics/Screenshot%202023-06-24%20at%209.50.45%20PM.png)

### Unsigned Binary Integer 
#### Excess-M Representation
![](../../../../Assets/Pics/Screenshot%202023-06-24%20at%2010.06.29%20PM.png)


### Signed Binary Integer
#### Signed Magnitude
![](../../../../Assets/Pics/Screenshot%202023-06-24%20at%2010.02.36%20PM.png)


#### 1's Complement 
![](../../../../Assets/Pics/Screenshot%202023-06-24%20at%2010.02.59%20PM.png)


#### 2's Complement
![](../../../../Assets/Pics/Screenshot%202023-06-24%20at%2010.03.07%20PM.png)



## Encodings
More at ↗ [Cryptography /Encoding](../../../CyberSecurity/🚬%20Cryptology/🤐%20Cryptography/Encoding.md) and ↗ [Encodings in Digital Systems](Encodings%20in%20Digital%20Systems.md)



## Error Control
↗ [Computer Network /Error Control](../../🏎️%20Computer%20Networking%20and%20Communication/📌%20Computer%20Networking%20Basics/Error%20Control/Error%20Control.md)



## Data Storage
> Also at ↗ [von Neumann Based Microarchitecture /Memory](../Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Memory/Memory.md)

### Data Storage in Memory: Byte Order
Little Endian 🆚 Big Endian

> These two terms, little and big endian, are from the book Gulliver’s Travels, in which the Lilliputians (the tiny people) were divided into two camps: those who ate their eggs by opening the “big” end (big endians) and those who ate their eggs by opening the “little” end (little endians).

> Most UNIX machines are big endian, whereas most PCs are little endian machines. Most newer RISC architectures are also big endian.
> 
> It is also worth noting that some CPUs can handle both little and big-endian

![](../../../../Assets/Pics/Screenshot%202023-06-24%20at%2010.23.42%20PM.png)

![](../../../../Assets/Pics/Screenshot%202023-06-24%20at%2010.26.04%20PM.png)


### ⭐️ Data Storage in CPU: Stacks 🆚 Registers
#### 1️⃣ Stack Architecture
Stack architectures use a stack to execute instructions, and the operands are (implicitly) found on top of the stack. 

**pros**
Even though stack-based machines have good code density and a simple model for the evaluation of expressions 
**cons**
a stack cannot be accessed randomly, which makes it difficult to generate efficient code. In addition, the stack becomes a bottleneck during execution.

> ↗ [Instruction Formats](../Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)/📌%20Instruction%20Basics/Instruction%20Formats.md) - reverse polish notation

![](../../../../Assets/Pics/Screenshot%202023-06-24%20at%2010.31.50%20PM.png)


#### 2️⃣ Accumulator Architecture
Accumulator architectures such as MARIE, with one operand implicitly in the accumulator, minimize the internal complexity of the machine and allow for very short instructions. But because the accumulator is only temporary storage, memory traffic is very high.

![](../../../../Assets/Pics/Screenshot%202023-06-24%20at%2010.32.32%20PM.png)


#### 3️⃣ GPR (General Purpose Register) Architecture
> ❗❗ Two characters concern GPR metrics the most: instruction length & instruction address modes.
> 
> ↗ [Instruction Formats /Instruction length](../Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)/📌%20Instruction%20Basics/Instruction%20Formats.md)
> ↗ [Memory /Memory Access](../Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Memory/Memory%20Access.md)

General-purpose register architectures, which use sets of general-purpose registers, are the most widely accepted models for machine architectures today. 

**pros**
These register sets are faster than memory and easy for compilers to deal with, and they can be used very effectively and efficiently. In addition, hardware prices have decreased significantly, making it possible to add a large number of registers at a minimal cost.

**cons**
However, because all operands must be named, using registers results in longer instructions, causing longer fetch and decode times. (A very important goal for ISA designers is short instructions.) Designers choosing an ISA must decide which will work best in a particular environment and examine the trade-offs carefully.

> If memory access is fast, a stack-based design may be a good idea; if memory is slow, it is often better to use registers. These are the reasons most computers over the past 10 years have been general-register based.

![](../../../../Assets/Pics/Screenshot%202023-06-24%20at%2010.32.43%20PM.png)

![](../../../../Assets/Pics/Screenshot%202023-06-24%20at%2010.32.53%20PM.png)

##### Memory-Memory
Memory-memory architectures may have two or three operands in memory, allowing an instruction to perform an operation without requiring any operand to be in a register.

##### Memory-Register
Register-memory architectures require a mix, where at least one operand is in a register and one is in memory.

##### Load-Store (Register-Register)
Load-store architectures require data to be moved into registers before any operations on those data are performed.



## Data Types In CS
> 🔗 https://www.ibm.com/docs/en/ibm-mq/7.5?topic=platforms-standard-data-types


![](../../../../Assets/Pics/Screenshot%202023-03-28%20at%204.51.18%20PM.png)

![](../../../../Assets/Pics/Screenshot%202023-03-28%20at%204.51.00%20PM.png)

![](../../../../Assets/Pics/Screenshot%202023-03-28%20at%204.51.45%20PM.png)



## Segment
### Data Segment
> 🔗 https://en.wikipedia.org/wiki/Data_segment

In computing, a **data segment** (often denoted **.data**) is a portion of an [object file](https://en.wikipedia.org/wiki/Object_file "Object file") or the corresponding [address space](https://en.wikipedia.org/wiki/Address_space "Address space") of a program that contains **initialized** [static variables](https://en.wikipedia.org/wiki/Static_variable "Static variable"), that is, [global variables](https://en.wikipedia.org/wiki/Global_variable "Global variable") and [static local variables](https://en.wikipedia.org/wiki/Static_local_variable "Static local variable"). The size of this segment is determined by the size of the values in the program's source code, and does not change at [run time](https://en.wikipedia.org/wiki/Run_time_(program_lifecycle_phase) "Run time (program lifecycle phase)").

**Uninitialized** data, both variables and constants, is instead in the [BSS segment](https://en.wikipedia.org/wiki/BSS_segment "BSS segment").


### Code Segment
> 🔗 https://en.wikipedia.org/wiki/Code_segment

In computing, a **code segment**, also known as a **text segment** or simply as **text**, is a portion of an [object file](https://en.wikipedia.org/wiki/Object_file "Object file") or the corresponding section of the program's [virtual address space](https://en.wikipedia.org/wiki/Virtual_address_space "Virtual address space") that contains executable instructions


### Stack Segment
⏬ See below "Stack" section.



## Stack
![](../../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%201.15.14%20PM.png)

### Stack Segment /Stack Frame
A stack frame is a data structure used to keep track of information about a subroutine call, while a stack segment is a segment of memory used by the operating system to store the call stack.


> 🔗 [汇编中的栈帧理解](https://blog.csdn.net/yhchinabest/article/details/103881857)

> 🔗 [Data Segment](https://en.wikipedia.org/wiki/Data_segment)
> The stack segment **contains the call stack, a LIFO structure, typically located in the higher parts of memory**. A "stack pointer" register tracks the top of the stack; it is adjusted each time a value is "pushed" onto the stack. The set of values pushed for one function call is termed a "stack frame".

>  🔗 [Stack-Based Memory Allocation](https://en.wikipedia.org/wiki/Stack-based_memory_allocation)
>  If a region of memory lies on the thread's stack, that memory is said to have been allocated on the stack, i.e. stack-based memory allocation (SBMA). This is contrasted with a [heap-based memory allocation](https://en.wikipedia.org/wiki/Heap-based_memory_allocation "Heap-based memory allocation") (HBMA). The SBMA is often closely coupled with a [function call stack](https://en.wikipedia.org/wiki/Call_stack#Functions_of_the_call_stack "Call stack").



### Stackoverflow
![](../../../../../Assets/Pics/Screenshot%202023-03-05%20at%201.44.33%20PM.png)



## Ref