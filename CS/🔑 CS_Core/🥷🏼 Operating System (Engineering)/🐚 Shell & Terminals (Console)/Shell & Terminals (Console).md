# Shell & Terminals (Console)

[TOC]



## Res



## Intro
> ↗ [FAQ /👉 Terminal(TTY, PTY, etc.) & Consoles](FAQ.md#👉%20Terminal(TTY,%20PTY,%20etc.)%20&%20Consoles)

> 🔗 https://silaoa.github.io/2019/2019-04-04-Linux%20Cygwin知识库（一）：一文搞清控制台、终端、shell概念.html (This website has been archived under the current directory)
> 🔗 https://silaoa.github.io/2019/2019-12-29-Cygwin系列（十）：折腾终端1.html
> 🔗 https://silaoa.github.io/2020/2020-01-13-Cygwin系列（十一）：折腾终端2.html

 > Here "shell" more specifically refers to Linux shell. But in general shell refers to a kind of software that interprates user's text commands to the OS.


### Overview
**控制台、终端、虚拟终端**是一类输入输出设备的总称，拥有将用户指令输入给操作系统和将操作系统返回结果输出给用户的基本功能，电传打字机（teletypewriter，缩写为tty）是该类设备的具体实例。终端模拟器（Terminal Emulator）是一类应用程序，用来模拟终端设备的功能，未具体说明情况下，“终端”泛指真实终端设备或终端模拟器。
- 伪终端（pseudo tty，缩写为pty）是UNIX/Linux内核中驱动程序模块，是一个软件中间层，用于克服真实终端设备在现代应用场景中的不足。
- 由于设计理念不同，Windows内核不支持 [Single Unix Specification](http://pubs.opengroup.org/onlinepubs/009695399/nfindex.html) 中规定的终端、伪终端设备，也不支持ANSI转义序列，但提供了 [Windows Console组件](https://zh.wikipedia.org/wiki/Win32%E6%8E%A7%E5%88%B6%E5%8F%B0)和相应配套的API。

**Shell**是UNIX/Linux系统中最为重要的应用程序之一，负责解释执行用户指令，打印结果，和用户交互，进行着REPL（Read-Evaluate-Print Loop）。sh、bash、zsh、fish等都是Shell的具体实例。

**系统内核**接管计算机资源，设备和程序**在系统内核的调配下运转**，他们之间的关系可用下图表示。用户实际用到的是具体程序，是难以感知内核的存在的，所以看起来就像是Shell在帮助用户调用程序。

![|300](../../../../../Assets/Pics/Screenshot%202024-02-15%20at%2011.47.13PM.png)
<small>终端、Shell、系统内核与用户的关系示意</small>


### 1️⃣ Console, Terminal, Serial Terminal


### 2️⃣ Virtual Terminal, Terminal Emulator | Pseudo tty (Unix/Linux) & Windows Console (Windows)

![pty_tty_console.excalidraw|800](../../../../../Assets/Illustrations/Computer%20System/pty_tty_console.excalidraw.md)

![](../../../../../Assets/Pics/Screenshot%202024-02-15%20at%2011.44.58PM.png)
<small>伪终端设备工作原理示意</small>

![](../../../../../Assets/Pics/Screenshot%202024-02-15%20at%2011.45.40PM.png)
<small>支持伪终端设备的终端模拟器工作原理示意</small>

![](../../../../../Assets/Pics/Screenshot%202024-02-16%20at%2011.50.46AM.png)
<small>Win10 1803上的Console架构 图片来源：微软博客</small>


### 3️⃣ Shell
↗ [Shell & Script Programming](🦞%20Shell%20&%20Script%20Programming/Shell%20&%20Script%20Programming.md)



## Ref
[👍 Linux Cygwin知识库（一）：一文搞清控制台、终端、shell概念]: https://silaoa.github.io/2019/2019-04-04-Linux%20Cygwin知识库（一）：一文搞清控制台、终端、shell概念.html 

(This website has been archived under the current directory)
