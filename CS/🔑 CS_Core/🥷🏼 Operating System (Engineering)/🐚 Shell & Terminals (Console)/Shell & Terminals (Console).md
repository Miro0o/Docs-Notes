# Shell & Terminals (Console)

[TOC]



## Res
### Lots of notes about CLI & Shell Commands!
↗ [🏫 Missing Semester](../../../🗺%20CS_Overview/💋%20Intro%20to%20CS/🏫%20Missing%20Semester.md)
↗ [🎭 The Art of Command Line](../../../🗺%20CS_Overview/💋%20Intro%20to%20CS/🎭%20The%20Art%20of%20Command%20Line.md)
↗ [🤯 Awesome List](../../../🗺%20CS_Overview/🕶️%20Awesome%20List/🤯%20Awesome%20List.md)
↗ [Free Software](../Linux%20(Derived%20From%20UNIX%20Family)/🪓%20Free%20Software/Free%20Software.md)
↗ [macOS CLI Software](../Apple/macOS%20(Derived%20From%20UNIX%20Family)/🪓%20macOS%20CLI%20Software/macOS%20CLI%20Software.md)
↗ [MacOS cmd Cheatsheet](../../../../🗺%20CS_Overview/MacOS%20cmd%20Cheatsheet.md)
↗ [👍 Vim](../../👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Text%20Editors/Vim/👍%20Vim.md)

🔍 https://ss64.com
Command Line Reference

### Also Lots notes about Shell Script!
↗ [Shell Implementations & Script Programming](🦞%20Shell%20Implementations%20&%20Script%20Programming/Shell%20Implementations%20&%20Script%20Programming.md)
↗ [Shell Helper](Shell%20Helper/Shell%20Helper.md)
- ↗ [Commands CheatCheet & Online Search](Shell%20Helper/Commands%20CheatSheet%20&%20Online%20Search/Commands%20CheatCheet%20&%20Online%20Search.md)
- and more!

📄 https://learnbyexample.github.io/tips/#command-line-tools
useful tips about command line tools !



## Intro
> ↗ [FAQ /👉 Terminal(TTY, PTY, etc.) & Consoles](FAQ.md#👉%20Terminal(TTY,%20PTY,%20etc.)%20&%20Consoles)

> 🔗 https://silaoa.github.io/2019/2019-04-04-Linux%20Cygwin知识库（一）：一文搞清控制台、终端、shell概念.html (This website has been archived under the current directory)


### Overview
**控制台、终端、虚拟终端**是一类输入输出设备的总称，拥有将用户指令输入给操作系统和将操作系统返回结果输出给用户的基本功能，电传打字机（teletypewriter，缩写为tty）是该类设备的具体实例。终端模拟器（Terminal Emulator）是一类应用程序，用来模拟终端设备的功能，未具体说明情况下，“终端”泛指真实终端设备或终端模拟器。伪终端（pseudo tty，缩写为pty）是UNIX/Linux内核中驱动程序模块，是一个软件中间层，用于克服真实终端设备在现代应用场景中的不足。

**Shell**是UNIX/Linux系统中最为重要的应用程序之一，负责解释执行用户指令，打印结果，和用户交互，进行着REPL（Read-Evaluate-Print Loop）。sh、bash、zsh、fish等都是Shell的具体实例。

**系统内核**接管计算机资源，设备和程序**在系统内核的调配下运转**，他们之间的关系可用下图表示。用户实际用到的是具体程序，是难以感知内核的存在的，所以看起来就像是Shell在帮助用户调用程序。

![|300](../../../../Assets/Pics/Screenshot%202024-02-15%20at%2011.47.13PM.png)
<small>终端、Shell、系统内核与用户的关系示意</small>


### 1️⃣ Console, Terminal, Serial Terminal


### 2️⃣ Virtual Terminal, Terminal Emulator, Pseudo tty

![pty_tty_console.excalidraw|800](../../../../Assets/Illustrations/Computer%20System/pty_tty_console.excalidraw.md)

![](../../../../Assets/Pics/Screenshot%202024-02-15%20at%2011.44.58PM.png)
<small>伪终端设备工作原理示意</small>

![](../../../../Assets/Pics/Screenshot%202024-02-15%20at%2011.45.40PM.png)
<small>支持伪终端设备的终端模拟器工作原理示意</small>


### 3️⃣ Shell
> Here "shell" more specifically refers to Linux shell because windows' shells are rarely used in production. But in general shell refers to a kind of software running on whatever platform that interprates user's text commands to the OS.  

终端自身并不执行用户输入的命令，它只是负责把输入的内容传送到主机系统，并把主机系统返回的结果呈现给用户。负责解释执行用户输入的命令并返回结果的，正是Shell！它是沟通用户和系统内核的中间桥梁。

从这个功能讲，广义上的Shell可以是图形界面的也可以是命令行界面的。比如Windows上的Explorer，双击文件名为什么可以让一个程序打开这个文件？其实可以理解为Explorer捕捉到了“鼠标双击文件名”这个事件，然后根据文件名去请求Windows内核启动了一个关联程序，并传入相关参数(文件名等信息)，然后这个程序自己再“打开”用户双击的文件，呈现到屏幕上。Windows上运行“命令提示符”时，在任务管理器中可以看到运行了两个进程：Console Windows Host和cmd，前者是终端模拟器（console host在用户启动cmd的时候由Windows系统自动创建），后者则是Shell程序。除了图形、命令行交互，未来还可能出现更加高级的Shell，比如语音、动作等等。

狭义的Shell仅指字符界面的命令解释器，在UNIX/Linux系统上广泛应用，所做的工作主要是：  
①读入用户输入（Read）；  
②解释执行（Evaluate）；  
③打印执行结果和提示符（Print）；  
④回到①循环（Loop）。

这种工作方式被称为交互式Shell（Interactive Shell），Shell通常还支持批处理方式（Batch），用户提前写好要执行的命令，形成脚本（Shell Script），Shell一次性把脚本中的命令执行完。



## 🍼 Shell Configuration
### Configuration File Loading
> 🔗 https://unix.stackexchange.com/a/3085

`~/.profile` is the right place for environment variable definitions and for non-graphical programs that you want to run when you log in (e.g. `ssh-agent`, `screen -m`). It is executed by your login shell if that is a Bourne-style shell (sh, ksh, bash). Zsh runs `~/.zprofile` instead, and Csh and tcsh run `~/.login`.

If you log in under an X display manager (xdm, gdm, kdm, ...), whether `~/.profile` is run depends on how your display manager and perhaps desktop environment were configured by your distribution. If you log in under a “custom session”, that usually executes `~/.xsession`.

`~/.bashrc` is the right place for bash-specific settings, such as aliases, functions, shell options and prompts. As the name indicates, it is specific to bash; csh has `~/.cshrc`, ksh has `~/.kshrc`, and zsh has \<drumroll\> `~/.zshrc`. 

> ❗ For shell specific configurations go to their specific docs.


🔗 See also: 
- [Difference between `.bashrc` and `.bash_profile`](https://superuser.com/questions/183870/difference-between-bashrc-and-bash-profile)
- [Which setup files should be used for setting up environment variables with bash?](https://superuser.com/questions/183845/which-setup-files-should-be-used-for-setting-up-environment-variables-with-bash)
- [Zsh not hitting `~/.profile`](https://superuser.com/questions/187639/zsh-not-hitting-profile)


### Default Shell
> 🔗 [Default Shell | Fish Doc](https://fishshell.com/docs/current/index.html#default-shell "Permalink to this heading")
> Applys to other shells.

There are multiple ways to switch to fish (or any other shell) as your default.

1️⃣ The simplest method is to set your terminal emulator (eg GNOME Terminal, Apple’s Terminal.app, or Konsole) to start fish directly. See its configuration and set the program to start to `/usr/local/bin/fish` (if that’s where fish is installed - substitute another location as appropriate).

2️⃣ Alternatively, you can set fish as your login shell so that it will be started by all terminal logins, including SSH.

> ⚠ Warning
> 
> Setting fish as your login shell may cause issues, such as an incorrect [`PATH`](https://fishshell.com/docs/current/language.html#envvar-PATH). Some operating systems, including a number of Linux distributions, require the login shell to be Bourne-compatible and to read configuration from `/etc/profile`. fish may not be suitable as a login shell on these systems.

To change your login shell to fish:

1.  Add the shell to `/etc/shells` with:
	```shell
	echo /usr/local/bin/fish | sudo tee -a /etc/shells
	```
1.  Change your default shell with:
	```shell
	chsh -s /usr/local/bin/fish
	```

Again, substitute the path to fish for `/usr/local/bin/fish` - see `command -s fish` inside fish. To change it back to another shell, just substitute `/usr/local/bin/fish` with `/bin/bash`, `/bin/tcsh` or `/bin/zsh` as appropriate in the steps above.



## Ref
[👍 Linux Cygwin知识库（一）：一文搞清控制台、终端、shell概念]: https://silaoa.github.io/2019/2019-04-04-Linux%20Cygwin知识库（一）：一文搞清控制台、终端、shell概念.html 
(This website has been archived under the current directory)

