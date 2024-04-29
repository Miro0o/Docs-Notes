# SRE (Software Reverse Engineering)

[TOC]



## Res
### Related Topics
↗ [SCA (Static Code Analysis)](../📌%20SCA%20(Static%20Code%20Analysis)/SCA%20(Static%20Code%20Analysis).md)

↗ [Program Execution & Compilation System](../../../../../🔑%20CS_Core/🛣️%20Program%20Execution%20&%20Compilation%20System/Program%20Execution%20&%20Compilation%20System.md)
↗ [Programming Methodology and Languages](../../../../../🔑%20CS_Core/👩‍💻%20Programming%20Methodology%20and%20Languages/Programming%20Methodology%20and%20Languages.md)
↗ [ASM (Assembly Languages)](../../../../../🔑%20CS_Core/👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/ASM%20(Assembly%20Languages).md)

↗ [Debuggers & Disassemblers & Decompilers](../../../../../🔑%20CS_Core/👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Debuggers%20&%20Disassemblers%20&%20Decompilers/Debuggers%20&%20Disassemblers%20&%20Decompilers.md)
↗ [IDA Pro](../../../../☠️%20Kill%20Chain/Software%20Analysis%20Tools/IDA%20Pro/IDA%20Pro.md)
↗ [Hex & Binary Manipulation](../../../../../🔑%20CS_Core/🥷🏼%20Operating%20System%20(Engineering%20Part)/Linux%20(Derived%20From%20UNIX%20Family)/Linux%20Free%20Software%20&%20OSS%20(Open%20Source%20Software)/Text%20&%20File%20&%20Dir%20Management/Hex%20&%20Binary%20Manipulation.md)



## Intro



## Ref

[反编译和反汇编的区别 反汇编工具有哪些]: https://www.idapro.net.cn/shouqian/ida-fhbfby.html

反编译和反汇编都是软件逆向工程的常用技术，它们之间的区别可以从以下几个方面进行分析。

1.定义
反编译（Decompilation）是将已编译的二进制文件转换为高级语言源代码的过程，以便更好地进行分析和修复。反汇编（Disassembly）是将二进制文件转换为汇编代码的过程，以便更好地进行分析和修复。

2.目的
反编译的目的是将已编译的二进制文件转换为高级语言源代码，以便更好地理解程序的结构和逻辑，并进行相应的分析和修复。反汇编的目的是将二进制文件转换为汇编代码，以便更好地了解程序的执行过程和指令序列，并进行相应的分析和修复。

3.实现方式
反编译通常需要使用特定的反编译工具，这些工具可以解析二进制文件的结构和逻辑，然后将其转换为高级语言源代码。反汇编通常使用反汇编工具进行操作，这些工具可以将二进制文件转换为汇编代码，并且可以将汇编代码转换为C语言代码或者其他高级语言代码。

4.精度
反编译的精度取决于反编译工具的算法和实现，以及原始程序的结构和逻辑。一些特定的结构和逻辑可能无法被正确地反编译出来。反汇编的精度取决于反汇编工具的算法和实现，以及汇编代码的结构和逻辑。反汇编的精度通常比反编译高一些，因为汇编代码更加直观和可读。

总之，反编译和反汇编的主要区别在于它们生成的代码类型以及处理的对象。反编译生成高级编程语言的源代码，易于理解，但可能丢失一些底层细节；反汇编生成汇编语言代码，分析难度较大，但提供了更详细的信息。

