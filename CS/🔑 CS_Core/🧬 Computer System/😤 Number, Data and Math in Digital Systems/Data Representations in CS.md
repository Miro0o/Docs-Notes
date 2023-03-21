# Data Representaion in CS

[TOC]



## Res
Also go to ↗ [von Neumann Arch /Memory](../Computer%20Organization%20&%20Architecture/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Memory/Memory.md)
and maybe ↗ [8086CPU ASM](../../👩‍💻%20Languages%20Programming/ASM/X86%20ISA%20Based%20ASM/8086CPU%20ASM.md)



## Encoding
More at ↗ [Cryptography /Encoding](../../../../CyberSecurity/🏰%20InfoSec/🤐%20Cryptography/Encoding.md) and ↗ [Encodings in Digital Systems](Encodings%20in%20Digital%20Systems.md)


## Data Storage & Memory
More at ↗ [von Neumann Based Microarchitecture /Memory](../Computer%20Organization%20&%20Architecture/🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Memory/Memory.md)


## Error Control
↗ [Error Control](../../🏎️%20Computer%20Networking/📌%20Basics/Error%20Control/Error%20Control.md)


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