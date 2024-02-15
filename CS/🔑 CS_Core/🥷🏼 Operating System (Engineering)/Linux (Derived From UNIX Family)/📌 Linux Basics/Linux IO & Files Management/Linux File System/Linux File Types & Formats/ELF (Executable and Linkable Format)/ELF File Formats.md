# ELF File Formats

[TOC]



## Res
↗ [Compilers](../../../../../../../👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Program%20Execution%20Related%20Tools%20Chain/Compilers/Compilers.md)
↗ [Compilation Phase](../../../../../../../🛣️%20Program%20Execution%20&%20Compilation%20System/🚮%20Program%20Language%20Translation%20(Compile-time)/Compilation%20Phase/Compilation%20Phase.md)



## Intro
### Program Instruction & Program Data


### Why Separate Instruction & Data
1. Privilege
2. Cache & Locality Principles
3. Share Memory



## ⏬ File Header



## ⏬ Basic Sections/ Segments
### 👉 .text Section/ Segment


### 👉 .data Section/ Segment


### 👉 .bss Section/ Segment (Block Started by Symbol)

#### BSS Etymology
Dennis Ritchie says:

> Actually the acronym (in the sense we took it up; it may have other credible etymologies) is "Block Started by Symbol." It was a pseudo-op in FAP (Fortran Assembly [-er?] Program), an assembler for the IBM 704-709-7090-7094 machines.  It defined its label and set aside space for a given number of words.  There was another pseudo-op, BES, "Block Ended by Symbol" that did the same except that the label was defined by the last assigned word + 1.  (On these machines Fortran arrays were stored backwards in storage and were 1-origin.)
> 
> The usage is reasonably appropriate, because just as with standard Unix loaders, the space assigned didn't have to be punched literally into the object deck but was represented by a count somewhere.

[ What does {some strange unix command name} stand for?]: http://www.faqs.org/faqs/unix-faq/faq/part1/section-3.html



## ⏬ Compiler Specific Sections/ Segments

![](../../../../../../../../../Assets/Pics/Screenshot%202023-10-16%20at%208.24.47PM.png)

### .note.GNU-stack



## ⏬ User Customized Sections/ Segments


## ⏬ Section Header Table



## ⏬ String Tables


## ⏬ Symbol Tables



## Ref

