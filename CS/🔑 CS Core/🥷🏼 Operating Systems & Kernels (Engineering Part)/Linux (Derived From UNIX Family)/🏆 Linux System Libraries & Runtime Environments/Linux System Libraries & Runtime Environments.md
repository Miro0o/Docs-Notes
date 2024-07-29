# Linux System Libraries & Runtime Environments

[TOC]



## Res
### Related Topics
↗ [Operating System Components & Runtime Libraries](../../../🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/Operating%20System%20Components%20&%20Runtime%20Libraries.md)
- ↗ [GNU C Library (glibc)](👎%20GNU%20C%20Library%20(glibc)/GNU%20C%20Library%20(glibc).md)



## Intro
![](../../../../../../../../Assets/Pics/Screenshot%202024-02-21%20at%209.18.47PM.png)
<small>Image source from wikipedia: Linux Kernel </small>




## Ref
[What is the role of libc(glibc) in our linux app? | Stackoverflow]: https://stackoverflow.com/q/11372872/16542494

`libc` implements both standard C functions like `strcpy()` and POSIX functions (which may be system calls) like `getpid()`. Note that not all standard C functions are in `libc` - most math functions are in `libm`.

You cannot directly make system calls in the same way that you call normal functions because calls to the kernel aren't normal function calls, so they can't be resolved by the linker. Instead, architecture-specific assembly language thunks are used to call into the kernel - you can of course write these directly in your own program too, but you don't need to because `libc`provides them for you.

Note that in Linux it is the combination of the kernel and `libc` that provides the POSIX API. `libc` adds a decent amount of value - not every POSIX function is necessarily a system call, and for the ones that are, the kernel behaviour isn't always POSIX conforming.

`libc` is a single library file (both `.so` and `.a` versions are available) and in most cases resides in `/usr/lib`. However, the glibc (GNU libc) project provides more than just `libc` - it also provides the `libm` mentioned earlier, and other core libraries like `libpthread`. So `libc`is just one of the libraries provided by glibc - and there are other alternate implementations of `libc` other than glibc.

---
With regard to the first two, glibc is both the C standard library (e.g, "standard C functions") and a wrapper for system calls. You cannot issue system calls directly because the compiler doesn't know how -- glibc contains the "glue" which is necessary to issue system calls, which is written in assembly. (It is possible to reimplement this yourself, but it's far more trouble than it's worth.)

(The C++ standard library is a separate thing; it's called `libstdc++`.)

glibc isn't a single `.so` (dynamic library) file -- there are a bunch, but libc and libm are the most commonly-used two. All of the static and dynamic libraries are stored in `/lib`.

libc is a generic term used to refer to all C standard libraries -- there are several. glibc is the most commonly used one; others include eglibc, uclibc, and dietlibc.

[标准c库函数与Linux下系统函数库 区别 （有无缓冲区引起的效率变化）| CSDN]: https://blog.csdn.net/zpznba/article/details/94356090

我们都知道，C语言在UNIX/Linux系统下有一套系统调用（系统函数），比如文件操作open()、close()、write()、read()等，而标准C语言的库函数中也有一套对文件的操作函数[fopen](https://so.csdn.net/so/search?q=fopen&spm=1001.2101.3001.7020)()、fclose()、fwrite()、fread()等.。那么同样是对文件的操作函数，标C与UC有什么区别呢？是标C效率高还是UC效率高呢？今天就让我们来一探究竟。

