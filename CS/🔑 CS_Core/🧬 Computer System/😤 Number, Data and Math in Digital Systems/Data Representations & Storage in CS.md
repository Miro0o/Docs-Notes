# Data Representaion in CS

[TOC]



## Res
Go to ↗ [von Neumann Arch /Memory](../Computer%20Organization%20&%20Architecture/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Memory/Memory.md) for more possible info.
And maybe ↗ [8086CPU ASM](../../👩‍💻%20Languages%20Programming/ASM/X86%20ISA%20Based%20ASM/8086CPU%20ASM.md).



## Encodings
More at ↗ [Cryptography /Encoding](../../../CyberSecurity/Cryptology/🤐%20Cryptography/Encoding.md) and ↗ [Encodings in Digital Systems](Encodings%20in%20Digital%20Systems.md)



## Error Control
↗ [Computer Network /Error Control](../../🏎️%20Computer%20Networking/📌%20Computer%20Networking%20Basics/Error%20Control/Error%20Control.md)



## Data Storage & Memory
> Also at ↗ [von Neumann Based Microarchitecture /Memory](../Computer%20Organization%20&%20Architecture/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Memory/Memory.md)

### Byte Order
Little Endian 🆚 Big Endian

> These two terms, little and big endian, are from the book Gulliver’s Travels, in which the Lilliputians (the tiny people) were divided into two camps: those who ate their eggs by opening the “big” end (big endians) and those who ate their eggs by opening the “little” end (little endians).

> It is also worth noting that some CPUs can handle both little and big-endian


### Internal Storage in the CPU: Stacks 🆚 Registers
#### 1️⃣ Stack Architecture
Stack architectures use a stack to execute instructions, and the operands are (implicitly) found on top of the stack. 

**pros**
Even though stack-based machines have good code density and a simple model for the evaluation of expressions 
**cons**
a stack cannot be accessed randomly, which makes it difficult to generate efficient code. In addition, the stack becomes a bottleneck during execution.

#### 2️⃣ Accumulator Architecture


#### 3️⃣ GPR (General Purpose Register) Architecture
##### Memory-Memory

##### Memory-Register

##### Load-Store (Register-Register)



## Data Types
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