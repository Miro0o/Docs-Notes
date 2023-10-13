# x86 Instruction Encoding

[TOC]



## Res
### Reference Documents for x86-64 Instruction Encoding
Here is a list of references and useful documents I will refer to in this post and you can further check later too to encode more instructions.

- x86-64 (and x86) ISA Reference from Intel and AMD’s [x86-64 (and x86) ISA Reference](https://www.systutorials.com/3024/x86-64-isa-assembly-references/) are the authoritative [document](https://www.systutorials.com/tag/document/ "document") here. Especially,
    - the [Intel 64 and IA-32 Architectures Software Developer’s Manuals](https://www.systutorials.com/go/intel-x86-64-reference-manual/)‘ “CHAPTER 2 INSTRUCTION FORMAT” is a good starting point. There are also references for each instruction.
    - the [Intel 64 and IA-32 Architectures Software Developer’s Manuals](https://www.systutorials.com/go/intel-x86-64-reference-manual/)‘ “APPENDIX B INSTRUCTION FORMATS AND ENCODINGS” is a good reference.
- [x86-64 Instruction Encoding](http://wiki.osdev.org/X86-64_Instruction_Encoding) is another very good page from OSDev as a quick reference.


### Tools
[GNU assembler `as`](https://www.systutorials.com/docs/linux/man/1-as/)

[`objdump` tool](https://www.systutorials.com/docs/linux/man/1-objdump/)


### In Action
↗ [x86 ISA Based ASM](../../../../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/x86%20ISA%20Based%20ASM/x86%20ISA%20Based%20ASM.md)



## Intro
### AT&T Syntax and Intel Syntax
There are AT&T syntax and Intel syntax. In Intel documents, it is usually in Intel syntax. With GNU toolchains on [Linux](https://www.systutorials.com/category/linux/ "Linux"), the default syntax used is usually the AT&T one.

The most significant difference between these 2 syntaxes is that AT&T and Intel syntax use the opposite order for source and destination operands. Intel syntax uses **“dest, source”** while the AT&T syntax uses **“source, dest”**. Note that instructions with more than one source operand, such as the enter instruction, do not have reversed order. For the representation of operands with the SIB or displacement, the formats are different. For example, the Intel syntax is `[rdi+0xa]` for `0xa(%rdi)` in AT&T syntax. For a list of notable differences, please check [AT&T Syntax versus Intel Syntax](http://www.sourceware.org/binutils/docs-2.12/as.info/i386-Syntax.html).


### x86 Instruction Format
![](../../../../../../../Assets/Pics/Pasted%20image%2020230321195343.png)
<small> x86指令格式</small>



## Ref
[x86 指令格式]: https://www.cnblogs.com/QKSword/p/8735119.html

[ Beginners’ Guide to x86-64 Instruction Encoding]: https://www.systutorials.com/beginners-guide-x86-64-instruction-encoding/

[x86 Instruction Format Reference]: http://www.c-jump.com/CIS77/CPU/x86/X77_0030_encoding_format.htm

