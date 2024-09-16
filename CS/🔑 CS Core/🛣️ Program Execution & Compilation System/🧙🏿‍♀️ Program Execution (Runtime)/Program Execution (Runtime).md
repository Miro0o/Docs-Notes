# Program Execution (Runtime)

[TOC]



## Res
### Related Topics
↗ [Operating System Kernel (Kernel Mode)](../../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/Operating%20System%20Kernel%20(Kernel%20Mode).md)
↗ [Operating System Components & Runtime Libraries](../../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/Operating%20System%20Components%20&%20Runtime%20Libraries.md)

↗ [ASM (Assembly Languages)](../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/ASM%20(Assembly%20Languages).md)
- ↗ [8086 ASM (16 bit)](../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/x86%20ISA%20Based%20ASM/8086%20ASM%20(16%20bit).md)
↗ [Instruction Set Architecture (ISA) & Processor Architecture](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture.md)
↗ [Instruction Basics](../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/📌%20ISA%20Basics/📌%20Instruction%20Basics/Instruction%20Basics.md)
↗ [Instruction Execution](Instruction%20Execution/Instruction%20Execution.md)

↗ [File Types & File Formats /Executable](../../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20IO%20System/IO%20Generality%20(via%20Abstraction)/File%20&%20File%20System/File%20Types%20&%20File%20Formats.md)

↗ [OS Processes & Automata Management (CPU + Main Memory Resource)](../../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Processes%20&%20Automata%20Management%20(CPU%20+%20Main%20Memory%20Resource)/OS%20Processes%20&%20Automata%20Management%20(CPU%20+%20Main%20Memory%20Resource).md)
- ↗ [System Calls](../../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Processes%20&%20Automata%20Management%20(CPU%20+%20Main%20Memory%20Resource)/📌%20Processes%20Description%20&%20Control/System%20Calls/System%20Calls.md)
↗ [OS Memory Management (Main Memory + Secondary Memory Resource)](../../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource).md)
- ↗ [Address Space & Memory Layout](../../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/Address%20Space%20&%20Memory%20Layout.md)


### Other Resources
https://textbook.cs161.org/memory-safety/x86.html
x86 Assembly and Call Stack | UCB CS161 Computer Security Textbook

📃 https://cpu.land
Putting the “You” in CPU
Curious exactly what happens when you run a program on your computer? Read this article to learn how multiprocessing works, what system calls really are, how computers manage memory with hardware interrupts, and how Linux loads executables.
- [Ch. 0 Intro](https://cpu.land/)
- [Ch. 1 Basics](https://cpu.land/the-basics)
- [Ch. 2 Multitasking](https://cpu.land/slice-dat-time)
- [Ch. 3 Exec](https://cpu.land/how-to-run-a-program)
- [Ch. 4 ELF](https://cpu.land/becoming-an-elf-lord)
- [Ch. 5 Paging](https://cpu.land/the-translator-in-your-computer)
- [Ch. 6 Fork-Exec](https://cpu.land/lets-talk-about-forks-and-cows)
- [Ch. 7 Epilogue](https://cpu.land/epilogue)



## Intro
### Program = Automata
↗ [Program, Computer, and Automation](../../../🗺%20CS%20Overview/Program,%20Computer,%20and%20Automation.md)

- (computing resources) CPU
- (storage resources) Register + Address Space

>  Here either register or address space are all conceptual, they are the virtualization of the actual hardware. Register here refers to specific ISA defined registers, not those computer microarchitecture actually has; address space, by the same token, is the virtual memory layout visible to users, not the physical memory layout.

- (program) instructions + data


### Program Execution: Software Perspective
↗ [Procedure (Function) Call & Runtime Memory Layout](Procedure%20(Function)%20Call%20&%20Runtime%20Memory%20Layout/Procedure%20(Function)%20Call%20&%20Runtime%20Memory%20Layout.md)


### Program Execution: Hardware Perspective
↗ [Instruction Execution](Instruction%20Execution/Instruction%20Execution.md)



## Ref

