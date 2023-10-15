# UNIX

[TOC]



## Res
📂 [unix system manager's manual (SMM)](https://www.netbsd.org/docs/bsd/lite2/smm.html)



## Intro
### Origin of Unix System
> Quote from CSAPP

The 1960s was an era of huge, complex operating systems, such as IBM’s OS/360 and Honeywell’s Multics systems. While OS/360 was one of the most successful software projects in history, Multics dragged on for years and never achieved wide-scale use. Bell Laboratories was an original partner in the Multics project but dropped out in 1969 because of concern over the complexity of the project and the lack of progress. In reaction to their unpleasant Multics experience, a group of Bell Labs researchers — Ken Thompson, Dennis Ritchie, Doug McIlroy, and Joe Ossanna — began work in 1969 on a simpler operating system for a Digital Equipment Corporation **PDP-7 computer**, written entirely in machine language. Many of the ideas in the new system, such as the hierarchical file system and the notion of a shell as a user-level process, were borrowed from Multics but implemented in a smaller, simpler package. In 1970, Brian Kernighan dubbed the new system “**Unix**” as a pun on the complexity of “Multics.” The kernel was rewritten in C in 1973, and Unix was announced to the outside world in 1974.

Because Bell Labs made the source code available to schools with generous terms, Unix developed a large following at universities. The most influential work was done at the University of California at Berkeley in the late 1970s and early 1980s, with Berkeley researchers adding virtual memory and the Internet protocols in a series of releases called Unix 4.xBSD (Berkeley Software Distribution). Concurrently, Bell Labs was releasing their own versions, which became known as System V Unix. Versions from other vendors, such as the Sun Microsystems Solaris system, were derived from these original BSD and System V versions.

Trouble arose in the mid 1980s as Unix vendors tried to differentiate themselves by adding new and often incompatible features. To combat this trend, **IEEE (Institute for Electrical and Electronics Engineers)** sponsored an effort to standardize Unix, later dubbed “**Posix**” by Richard Stallman. The result was a family of standards, known as the Posix standards, that cover such issues as the C language interface for Unix system calls, shell programs and utilities, threads, and network program- ming. More recently, a separate standardization effort, known as the “**Standard Unix Specification**,” has joined forces with Posix to create a single, unified standard for Unix systems. As a result of these standardization efforts, the differences between Unix versions have largely disappeared.


### Development of UNIX Family

![](../../../../../Assets/Pics/Pasted%20image%2020230302220507.png)
<small>UNIX Family Tree</small>


![](../../../../../Assets/Pics/Pasted%20image%2020230302220447.png)
<small>UNIX Family Tree</small>


### 👴🏿 Traditional UNIX Systems
> For more move to ↗ [Traditional UNIX Systems](📌%20UNIX%20Basics/Traditional%20UNIX%20Systems.md)

[VAHA96] uses the term "traditional UNIX" to refer to **System V Release 3 (SVR3), 4.3BSD, and earlier versions**. The following general statements may be made about a traditional UNIX system. 

Traditional UNIX is designed to 
1. run on a single processor;
2. lacks the ability to protect its data structures from concurrent access by multiple processors;
3. Its kernel is not very versatile, supporting a single type of file system, process scheduling policy, and executable file format;
4. The traditional UNIX kernel is not designed to be extensible and has few facilities for code reuse. The result is that, as new features were added to the various UNIX versions, much new code had to be added, yielding a bloated and unimodular kernel.


![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%209.26.30%20PM.png)


### 🧒🏻 Modern UNIX Systems
![](../../../../../Assets/Pics/Screenshot%202023-03-02%20at%209.28.48%20PM.png)


↗ [System V Family](System%20V%20Family/System%20V%20Family.md)

↗ [BSD Family](BSD%20Family/BSD%20Family.md)



## Ref

