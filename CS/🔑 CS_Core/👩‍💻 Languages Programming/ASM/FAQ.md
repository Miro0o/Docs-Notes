# FAQ

[TOC]



## Res


## 👉 word, wordlength, double word, quad word
**字和字长**
64位系统和32位系统中64和32的含义：
64和32指的是CPU中的寄存器(通用)的字长，字长就是一个字的位数。这里说的字的含义是：处理器进行数据处理时，一次存取，加工，和传送的数据长度。

系统中的一个字的大小与CPU寄存器的大小有关，因此，16位，32位系统与64位系统中的字不一样：
16位系统：一个字 = 2Byte
32位系统：一个字 = 4Byte
64位系统：一个字 = 8Byte


**汇编中的字，双字和四字**
汇编中的字，双字，四字其实指的是汇编指令的后缀，与处理器概念中的字和字长是不一样的概念。

汇编中的字，双字和四字是数据格式，见下表:
| C声明 | 数据类型 | 汇编代码后缀 | 大小(字节) |
| - | - | - | - |
| char | 字节 | b | 1 |
| short | 字 | w | 2 |
| int | 双字 | l | 4 |
| long | 四字 | q | 8 |
| char * | 四字	| q	| 8 |
| float	| 单精度	| s	| 4 |
| double | 双精度 | l | 8 |

由于是从16位体系结构扩展成32位的，Intel用术语“字(word)”表示16位数据类型。因此，称32位数为"双字(double word)"，称64位数为"四字(quad word)"。



## 👉 Why do x86-64 instructions on 32-bit registers zero the upper part of the full 64-bit register?

I'm not AMD or speaking for them, but I would have done it the same way. Because zeroing the high half doesn't create a dependency on the previous value, that the CPU would have to wait on. The [register renaming](https://en.wikipedia.org/wiki/Register_renaming) mechanism would essentially be defeated if it wasn't done that way.

This way you can write fast code using 32-bit values in 64-bit mode without having to explicitly break dependencies all the time. Without this behaviour, every single 32-bit instruction in 64-bit mode would have to wait on something that happened before, even though that high part would almost never be used. (Making `int` 64-bit would waste cache footprint and memory bandwidth; [x86-64 most efficiently supports 32 and 64-bit operand sizes](https://stackoverflow.com/questions/38303333/the-advantages-of-using-32bit-registers-instructions-in-x86-64))

The behaviour for 8 and 16-bit operand sizes is the strange one. The dependency madness is one of the reasons that 16-bit instructions are avoided now. x86-64 inherited this from 8086 for 8-bit and 386 for 16-bit, and decided to have 8 and 16-bit registers work the same way in 64-bit mode as they do in 32-bit mode.

---

See also [Why doesn't GCC use partial registers?](https://stackoverflow.com/questions/41573502/why-doesnt-gcc-use-partial-registers) for practical details of how writes to 8 and 16-bit partial registers (and subsequent reads of the full register) are handled by real CPUs.o


[Why do x86-64 instructions on 32-bit registers zero the upper part of the full 64-bit register?]: https://stackoverflow.com/questions/11177137/why-do-x86-64-instructions-on-32-bit-registers-zero-the-upper-part-of-the-full-6



## 👉 Why use 32-bit register when the data type is 64-bit?

The answer lies in Section 3.4.1.1 of the Intel 64 and IA-32 Architectures Software Developer’s Manual Volume 1 (Basic Architecture) which states:

> When in 64-bit mode, operand size determines the number of valid bits in the destination general-purpose register:
> 
> -   64-bit operands generate a 64-bit result in the destination general-purpose register.
> -   32-bit operands generate a 32-bit result, zero-extended to a 64-bit result in the destination general-purpose register.
> -   8-bit and 16-bit operands generate an 8-bit or 16-bit result. The upper 56 bits or 48 bits (respectively) of the destination general-purpose register are not modified by the operation. If the result of an 8-bit or 16-bit operation is intended for 64-bit address calculation, explicitly **sign-extend** the register to the full 64-bits.

See the second bullet.

You can gain some insight as to why this is so by reading: 🔗 [Why do x86-64 instructions on 32-bit registers zero the upper part of the full 64-bit register?](https://stackoverflow.com/questions/11177137/why-do-x86-64-instructions-on-32-bit-registers-zero-the-upper-part-of-the-full-6)



[why use 32-bit register when the data type is 64-bit?]: https://stackoverflow.com/questions/62807400/why-use-32-bit-register-when-the-data-type-is-64-bit



## 👉 Why should I not use __fastcall instead the standard __cdecl?

**The x86 platform is unusual in that it doesn't define a global ABI and calling convention.**

Win32/x86 does, it standardizes on `stdcall`. There are various tradeoffs between calling conventions -- placing parameters in registers is faster, but it forces the caller to spill whatever was previously using those registers. So it's hard to predict which gives better performance.

The important thing is to have a uniform standard calling convention to enable interoperability between different compilers (and even different programming languages).

Other platforms don't have `cdecl`, `stdcall`, or `fastcall` conventions. They don't have the same set of registers. In some cases, they don't even have registers at all. But they still can use C code.

Win32/x86_64 doesn't use `stdcall`, it uses a 64-bit extension of `fastcall`.

Linux/x86 has a convention also.



[Why should I not use __fastcall instead the standard __cdecl?]: https://stackoverflow.com/questions/13089752/why-should-i-not-use-fastcall-instead-the-standard-cdecl



## Ref

