# Linking Phase

[TOC]



## Res
↗ [Linkers](../../../👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Compiling%20&%20Assembling%20&%20Linking%20Tools/Linkers/Linkers.md)



## Intro
On most systems, program compiler output must pass through a link editor (or linker) before it can be executed on the target system. Linking is the process of matching the external symbols of a program with all exported symbols from other files, producing a single binary file with no unresolved external symbols. The principal job of a link editor, as shown in Figure 8.6, is to combine related program files into a unified loadable module. (The example in the figure uses file extensions characteristic of a DOS/Windows environment.) The constituent binary files can be entirely user-written, or they can be combined with standard system routines, depending on the needs of the application. Moreover, the binary linker input can be produced by any compiler. Among other things, this permits various sections of a program to be written in different languages, so part of a program could be written in C++ for ease of coding, and another part might be written in assembly language to speed up execution in a particularly slow section of the code.



As with assemblers, most link editors require two passes to produce a complete load module comprising all of the external input modules.
- During its first pass, the linker produces a global external symbol table containing the names of each of the external modules and their relative starting addresses with respect to the beginning of the total linked module.
- During the second pass, all references between the (formerly separate and external) modules are replaced with displacements for those modules from the symbol table. During the second pass of the linker, platform-dependent code can also be added to the combined module, producing a unified and loadable binary program file.



## Ref

