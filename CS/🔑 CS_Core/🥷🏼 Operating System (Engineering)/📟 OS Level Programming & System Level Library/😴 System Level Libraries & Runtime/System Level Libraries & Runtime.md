# System Level Libraries & Runtime

[TOC]



## Res
### Related Topics
↗ [Program Execution & Compilation System](../../../🛣️%20Program%20Execution%20&%20Compilation%20System/Program%20Execution%20&%20Compilation%20System.md)
↗ [Library Level Virtualization](../../../🧬%20Computer%20System/🚀%20Virtualization%20Theory/Library%20Level%20Virtualization/Library%20Level%20Virtualization.md)


↗ [Computer OS Interfaces](../../../🧬%20Computer%20System/Computer%20Interfaces/Computer%20OS%20Interfaces/Computer%20OS%20Interfaces.md)
- ↗ [POSIX (Portable Operating System Interface)](../../../🧬%20Computer%20System/Computer%20Interfaces/Computer%20OS%20Interfaces/🦶🏽%20POSIX%20(Portable%20Operating%20System%20Interface)/POSIX%20(Portable%20Operating%20System%20Interface).md)

↗ [C-like Runtimes](../../../👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/🚠%20Application%20Runtimes%20&%20SDKs/C-like%20Runtimes/C-like%20Runtimes.md)
↗ [OS Level Programming with C & CPP](../🧱%20OS%20Level%20Programming%20with%20C%20&%20CPP/OS%20Level%20Programming%20with%20C%20&%20CPP.md)

↗ [🍸 Linux Kernel](../../Linux%20(Derived%20From%20UNIX%20Family)/🔩%20Linux%20Kernel/🍸%20Linux%20Kernel.md)



## Intro
> 🔗 https://silaoa.github.io/2019/2019-02-14-Cygwin系列（一）：Cygwin是什么.html

计算机世界里存在各种各样的操作系统，目前通用操作系统有主流的三大类：
- UNIX，通用操作系统鼻祖，发展出特别多衍生系统；
- Windows，微软家根基，桌面市场霸主；
- GNU/Linux，UNIX近亲，有各种发行版如Ubuntu、CentOS等。

这些系统有各自的内核，出于系统稳定性考虑是不允许用户程序直接操作内核，同时也将内核开发和应用软件开发隔离开来，系统将必要的函数封装成库供应用软件调用，约定的规范即为应用软件接口(Application Program Interface，API)。  

![](../../../../../Assets/Pics/Screenshot%202024-02-15%20at%207.26.21PM.png)
<small>软件系统层级关系简要示意图</small>

API函数库是连接用户软件和系统内核桥梁，或者是“协议”，操作系统厂商写好函数库说明书，应用软件开发者不必关心其内部是如何实现的，用的时候对照着API手册查询就够了；应用软件也可以越过系统函数库通过system call（系统调用）直接调用os内核函数，如图中红色虚线所示，当然这种方式并不被推荐。

如果各系统平台都能提供相同的系统函数库，那么开发者在这个系统函数库基础之上编写软件代码，那么就很容易将软件移植到各个系统平台。**然而，这只是个美好的愿望**，IEEE就是为了达成这样的愿望才牵头制定POSIX标准。POSIX标准主要就是针对[UNIX API](http://www.unix.org/apis.html)而制订，**不管函数如何包装、功能如何实现，但API按照标准约定来（比如函数变量等符号名称、数据结构、参数类型与个数、基本工具命令名称等）**，Linux完全兼容POSIX标准（部分函数符合POSIX，部分函数是Linux专有，即是POSIX的超集），微软声称Windows部分兼容POSIX标准。

主流os内核通常是C语言写成，系统函数库通常以一个或多个链接库文件的形式提供，`其中最重要的是C标准库`，其他的链接库往往调用C标准库而实现，当然也可能直接调用系统内核函数，甚至混合。不同系统平台有多种主流的C标准库共存：
- [BSD libc](https://en.wikipedia.org/wiki/BSD_libc)，由BSD系统发布；
- [GNU C Library (glibc)](https://en.wikipedia.org/wiki/GNU_C_Library)，由GNU项目发布，可在Linux、多种UNIX系统上运行；
- [Microsoft C run-time library(MSVCRT.DLL)](https://en.wikipedia.org/wiki/Windows_library_files#MSVCRT.DLL,_MSVCP*.DLL_and_CRTDLL.DLL)，由微软随Windows发布，给Visual C++编辑器链接使用的；
- [Newlib](https://en.wikipedia.org/wiki/Windows_library_files#MSVCRT.DLL,_MSVCP*.DLL_and_CRTDLL.DLL)，由Cygnus Solution公司开发，Cygwin环境中的libc.a正是此版本，目前广泛用在嵌入式系统中
- [dietlibc](https://en.wikipedia.org/wiki/Dietlibc)、[μClibc](https://en.wikipedia.org/wiki/UClibc)等，功能经过适度裁剪的C标准库，主要用在嵌入式系统。



## Ref

