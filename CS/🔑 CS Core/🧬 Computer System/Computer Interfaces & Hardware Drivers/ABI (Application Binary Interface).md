# ABI (Application Binary Interface)

[TOC]



## Res
### Related Topics



## Intro
In computer software, an **application binary interface** (**ABI**) is an interface between two binary program modules. Often, one of these modules is a **library** or **operating system facility**, and the other is a program that is being run by a user.
- An **ABI** defines how data structures or computational routines are accessed in **machine code**, which is a low-level, hardware-dependent format. 
- In contrast, an **API** defines this access in **source code**, which is a relatively high-level, hardware-independent, often [human-readable](https://en.wikipedia.org/wiki/Human-readable "Human-readable") format. 

A common aspect of an ABI is the [calling convention](https://en.wikipedia.org/wiki/Calling_convention "Calling convention"), which determines how data is provided as input to, or read as output from, computational routines.

> Examples of this are the [x86 calling conventions](https://en.wikipedia.org/wiki/X86_calling_conventions "X86 calling conventions").

Adhering to an ABI (which may or may not be officially standardized) is usually the job of a **compiler**, **operating system**, or **library** author. However, an application programmer may have to deal with an ABI directly when writing a program in a mix of programming languages, or even compiling a program written in the same language with different compilers.


### Description
Details covered by an ABI include the following:
- **Processor instruction set (ISA)**, with details like register file structure, stack organization, memory access types, etc.

- Sizes, layouts, and [alignments](https://en.wikipedia.org/wiki/Data_structure_alignment "Data structure alignment") of basic **data types** that the processor can directly access

- **Calling convention**, which controls how the arguments of functions are passed, and return values retrieved; for example, it controls the following:
	- Whether all parameters are passed on the stack, or some are passed in registers
    - Which registers are used for which function parameters
    - Whether the first function parameter passed on the stack is pushed first or last
    - Whether the caller or callee is responsible for cleaning up the stack after the function call

- How an application should make **system calls** to the operating system, and if the ABI specifies direct system calls rather than procedure calls to system call [stubs](https://en.wikipedia.org/wiki/Method_stub "Method stub"), the system call numbers.

- In the case of a complete operating system ABI, the **binary format** of object files, program libraries, etc.



## Ref
[ABI | Wikipeida]: https://en.wikipedia.org/wiki/Application_binary_interface

