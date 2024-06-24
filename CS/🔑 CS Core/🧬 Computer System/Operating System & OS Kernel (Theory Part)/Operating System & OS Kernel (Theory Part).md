# Operating System & OS Kernel (Theory Part)

[TOC]



## Res
### Related Topics
↗ [Operating Systems (Engineering Part)](../../🥷🏼%20Operating%20Systems%20(Engineering%20Part)/Operating%20Systems%20(Engineering%20Part).md)

↗ [Operating System Components & Runtime Libraries](../../🥷🏼%20Operating%20Systems%20(Engineering%20Part)/📟%20System%20Level%20Programming/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/Operating%20System%20Components%20&%20Runtime%20Libraries.md)
- ↗ [Operating System Kernel (Kernel Mode)](../../🥷🏼%20Operating%20Systems%20(Engineering%20Part)/📟%20System%20Level%20Programming/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/🫀%20Operating%20System%20Kernel%20(Kernel%20Mode)/Operating%20System%20Kernel%20(Kernel%20Mode).md)
- ↗ [System Core Function Libraries & C Standard Library (User Mode)](../../🥷🏼%20Operating%20Systems%20(Engineering%20Part)/📟%20System%20Level%20Programming/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/📌%20System%20Core%20Function%20Libraries%20&%20C%20Standard%20Library%20(User%20Mode)/System%20Core%20Function%20Libraries%20&%20C%20Standard%20Library%20(User%20Mode).md)


### Learning Resources
#### Courses
🏫 [NJU /操作系统](../../../🏠%20Assets/Courses%20of%20Universities/🇨🇳%20Mainland%20China/NJU/操作系统/操作系统.md)
🏫 [UCB /CS162 Operating System](../../../🏠%20Assets/Courses%20of%20Universities/UC%20Berkeley/CS162%20Operating%20System/CS162%20Operating%20System.md)
🏫 [MIT /6.S081/828/1810 Operating System Engineering](../../../🏠%20Assets/Courses%20of%20Universities/MIT/6.S081(6.828,%206.1810)%20Operating%20System%20Engineering/6.S081(6.828,%206.1810)%20Operating%20System%20Engineering.md)

> Learning in action by ↗ [Operating Systems (Engineering Part)](../../🥷🏼%20Operating%20Systems%20(Engineering%20Part)/Operating%20Systems%20(Engineering%20Part).md)
> Theoretical knowledge begins with ↗ [📌 Operating System Overview](🦺%20Operating%20System%20Basics/📌%20Operating%20System%20Overview.md)

🇨🇳 ↗ [NJU /操作系统](../../../🏠%20Assets/Courses%20of%20Universities/🇨🇳%20Mainland%20China/NJU/操作系统/操作系统.md)
🇨🇳 ↗ [HIT OS /Operating System](../../../🏠%20Assets/Courses%20of%20Universities/🇨🇳%20Mainland%20China/HIT/HIT%20OS%20-%20Operating%20System.md)
#### Books
↗ [Computer System](../Computer%20System.md)
↗ [Computer Architecture](../Computer%20Architecture/Computer%20Architecture.md)

↗ [Linux (Derived From UNIX Family)](../../🥷🏼%20Operating%20Systems%20(Engineering%20Part)/Linux%20(Derived%20From%20UNIX%20Family)/Linux%20(Derived%20From%20UNIX%20Family).md)
↗ [UNIX Family](../../🥷🏼%20Operating%20Systems%20(Engineering%20Part)/UNIX%20Family/UNIX%20Family.md)
↗ [Windows](../../🥷🏼%20Operating%20Systems%20(Engineering%20Part)/Microsoft%20Operating%20Systems/Windows/Windows.md)

📖 [UNIX Network Programming](http://www.unpbook.com) volumn I & II
📖 Advanced Programming in the UNIX® Environment 
📖 The Little Book of Semaphores -- Allen B. Downey

📖 Operating systems principles and practice

👍 📖 Operating Systems: Three Easy Pieces
https://pages.cs.wisc.edu/~remzi/OSTEP/

📖 大话处理器（？偶尔看到，不知道怎么样）

🤔 http://www.harley.com/books/sg3.html
Harley Hahn's Guide to Unix and Linux

👍 https://jyywiki.cn/OS/References.md
1. 编程基础
	1. Brian W. Kernighan and Dennis M. Ritchie. _The C programming language_ (2nd Edition). Prentice Hall, 1998.
	2. [The CERT C Coding Standard: Rules for Developing Safe, Reliable, and Secure Systems](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard). Software Engineering Institute of Carnegie Mellon University, 2016.
	3. [pwn.college: Learn to hack](https://pwn.college/)
2. UNIX/Linux 编程
	1. Jlevy Hollowa. [_The Art of Command Line_](https://github.com/jlevy/the-art-of-command-line).
	2. Gerard Beekmans. [Linux from Scratch](http://linuxfromscratch.org/).
	3. Harley Hahn. _[Harley Hahn's Guide to Unix and Linux](http://www.harley.com/books/sg3.html)_. McGraw-Hill Higher Education, 2008.
	4. Michael Kerrisk. _The Linux Programming Interface: A Linux and UNIX System Programming Handbook_. No Starch Press, 2010.
	5. W. Richard Stevens and Stephen A. Rago. _[Advanced Programming in the UNIX® Environment](http://www.apuebook.com/apue3e.html)_ (3rd Edition). Addison-Wesley, 2013.
3. 操作系统原理
	1. 陈海波、夏虞斌. _[现代操作系统：原理与实现](http://ipads.se.sjtu.edu.cn/mospi/)_. 机械工业出版社, 2020.
	2. Thomas Anderson, Michael Dahlin. _Operating Systems: Principles and Practice_ (2nd Edition). Recursive Books, 2014.
	3. John R. Levine. _[Linkers and Loaders](https://linker.iecc.com/)_. Morgan-Kauffman, 1999.
	4. Robert Love. _Linux Kernel Development: A Thorough Guide to the Design and Implementation of the Linux Kernel_ (3rd Edition). Addison-Wesley, 2010.
	5. Marshall Kirk McKusick, Keith Bostic, Michael J. Karels, and John S. Quarterman. _[The Design and Implementation of the 4.4BSD Operating System](https://www.freebsd.org/doc/en/books/design-44bsd/book.html)_. Addison-Wesley Longman, 1996.
4. Finally, The Friendly Manual
	1. Linux manpages (tldr, man, info, ...): [man7.org](https://www.man7.org/)
	2. [Bourne-Again Shell (bash)](https://www.gnu.org/software/bash/manual/html_node/index.html)
	3. [GNU Compiler Collection (GCC)](https://gcc.gnu.org/onlinedocs/)
	4. [GNU Debugger (gdb)](https://sourceware.org/gdb/documentation/)
	5. [Binutils (ld, as, objdump, and more)](https://sourceware.org/binutils/docs/)
	6. [GNU Make](https://www.gnu.org/software/make/manual/html_node/index.html)
#### Learning by doing!
💻 [Writing an OS in Rust](https://os.phil-opp.com/)
💻 [OSDev - wiki](https://wiki.osdev.org/Main_Page)
#### Other Resources
[CPU Architecture](https://www.tutorialspoint.com/computer_logical_organization/cpu_architecture.htm)

[Programmed Introduction to MIPS Assembly Language](https://chortle.ccsu.edu/assemblytutorial/index.html#part1)
[Simple CPU :) - updated 30/10/2019](http://simplecpudesign.com/simple_cpu_v1/index.html)
[Central Processing Unit (CPU)](https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:computers/xcae6f4a7ff015e7d:computer-components/a/central-processing-unit-cpu)
[Organization of Computer Systems: §4: Processors](https://www.cise.ufl.edu/~mssz/CompOrg/CDA-proc.html)

📄 https://en.wikipedia.org/wiki/Operating_system



## Intro
> 🎬【操作系统概述 (为什么要学操作系统) [南京大学2022操作系统-蒋炎岩-P1]】 https://www.bilibili.com/video/BV1Cm4y1d7Ur/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d


### Computer System Review
![computer_architecture.excalidraw | 800](../../../../Assets/Illustrations/Computer%20System/computer_architecture_and_computer_science.excalidraw.md)
<small>Computer System Overveiw</small>

↗ [Computer Architecture Overview](../Computer%20Architecture/📌%20Computer%20Organization%20&%20Architecture%20Basics/Computer%20Architecture%20Overview.md)


### Operating System Overview
↗ [📌 Operating System Overview](🦺%20Operating%20System%20Basics/📌%20Operating%20System%20Overview.md)



## Operating System Security
↗ [Operating System Security](../../../CyberSecurity/System%20Security/Operating%20System%20Security/Operating%20System%20Security.md)



## Ref
