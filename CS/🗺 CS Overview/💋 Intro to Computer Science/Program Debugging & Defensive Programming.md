# Program Debugging & Defensive Programming

[TOC]



## Res
### Related Topics
↗ [Debuggers & Disassemblers & Decompilers](../../🔑%20CS%20Core/👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Debuggers%20&%20Disassemblers%20&%20Decompilers/Debuggers%20&%20Disassemblers%20&%20Decompilers.md)
- ↗ [gdb (GNU DeBugger)](../../🔑%20CS%20Core/👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Compilation%20&%20Program%20Loading%20Tools/GCC%20(The%20GNU%20Compiler%20Collection)/gdb%20(GNU%20DeBugger)/gdb%20(GNU%20DeBugger).md)
↗ [Code Linters & Formatters](../../🔑%20CS%20Core/👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Code%20Linters%20&%20Formatters/Code%20Linters%20&%20Formatters.md)

↗ [Kernel Debugging](../../🔑%20CS%20Core/🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/🫀%20Operating%20System%20Kernel%20(Kernel%20Mode)/Kernel%20Debugging.md)
↗ [Anti-Debugging](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Binary%20Engineering%20&%20Software%20Analysis/Anti-Reverse%20Engineering%20&%20Software%20Protection/Anti-Debugging/Anti-Debugging.md)

↗ [Software Testing](../../Software%20Engineering/Software%20Maintenance%20&%20Operations%20Management/🧪%20Software%20Testing/Software%20Testing.md)
↗ [Software Security](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/Software%20Security.md)
↗ [Binary Engineering & Software Analysis](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Binary%20Engineering%20&%20Software%20Analysis/Binary%20Engineering%20&%20Software%20Analysis.md)
- ↗ [SCA (Static Code Analysis)](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Binary%20Engineering%20&%20Software%20Analysis/📌%20SCA%20(Static%20Code%20Analysis)/SCA%20(Static%20Code%20Analysis).md)
- ↗ [DCA (Dynamic Code Analysis)](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Binary%20Engineering%20&%20Software%20Analysis/📌%20DCA%20(Dynamic%20Code%20Analysis)/DCA%20(Dynamic%20Code%20Analysis).md)
↗ [Vulnerabilities](../../CyberSecurity/⛈️%20Risk%20Management/🦟%20Vulnerabilities/Vulnerabilities.md)
- ↗ [Vulnerability Disclosure（漏洞挖掘）](../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🐒%20Software%20Vulnerability%20&%20Vulnerability%20Analysis%20(VA)/Vulnerability%20Disclosure（漏洞挖掘）/Vulnerability%20Disclosure（漏洞挖掘）.md)

↗ [QEMU](../../🔑%20CS%20Core/🥷🏼%20Operating%20Systems%20&%20Kernels%20(Engineering%20Part)/🚀%20Virtualization%20Theory/Hardware%20Level%20Virtualization%20&%20Hypervisors/Hypervisors%20Implementation/Hosted%20Hypervisor/Independant/QEMU/QEMU.md)
↗ [JTAG（Joint Test Action Group）Debugger](../../🔑%20CS%20Core/👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Debuggers%20&%20Disassemblers%20&%20Decompilers/JTAG（Joint%20Test%20Action%20Group）Debugger.md)
↗ [Docker](../../Software%20Engineering/☁️%20Cloud%20Computing%20&%20Cloud%20Native/🏂%20OS%20Level%20Virtualization%20&%20Containers%20Technology/🐋%20Container%20Implementations/Docker/Docker.md)


### Learning Resources
【并发 bug 和应对 (死锁/数据竞争/原子性违反；防御性编程和动态分析) [南京大学2022操作系统-P8]】 https://www.bilibili.com/video/BV1sR4y1V7T4/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d



## Intro



## DWARF Debugging Standard
🏠 https://dwarfstd.org
DWARF is a debugging information file format used by many compilers and debuggers to support source level debugging. It addresses the requirements of a number of procedural languages, such as C, C++, and Fortran, and is designed to be extensible to other languages. DWARF is architecture independent and applicable to any processor or operating system. It is widely used on Unix, Linux and other operating systems, as well as in stand-alone environments.



## Ref
