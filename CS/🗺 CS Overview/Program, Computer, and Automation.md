# Program, Computer, and Automation

[TOC]



## Res
### Related Topics
↗ [Theory of Computation](../../🧮%20Math%20&%20Theoretical%20Computer%20Science%20(TCS)/🤼‍♀️%20Mathematical%20Logics/😶‍🌫️%20Theory%20of%20Computation/Theory%20of%20Computation.md)
- ↗ [Automata Theory and (Formal) Language Theory](../🧮%20Math%20&%20Theoretical%20Computer%20Science%20(TCS)/🤼‍♀️%20Mathematical%20Logics/😶‍🌫️%20Theory%20of%20Computation/Computability%20Theory/🍏%20Automata%20Theory%20and%20(Formal)%20Language%20Theory/Automata%20Theory%20and%20(Formal)%20Language%20Theory.md)
- ↗ [Formal Semantics and Programming Language](../🧮%20Math%20&%20Theoretical%20Computer%20Science%20(TCS)/🤼‍♀️%20Mathematical%20Logics/😶‍🌫️%20Theory%20of%20Computation/Computability%20Theory/🍏%20Automata%20Theory%20and%20(Formal)%20Language%20Theory/Formal%20Semantics%20and%20Programming%20Language.md) (程序语言的形式语义)

↗ [Programming Methodology and Languages](../🔑%20CS%20Core/👩‍💻%20Programming%20Methodology%20and%20Languages/Programming%20Methodology%20and%20Languages.md)
↗ [Program Language Translation & Compilation Theory (Compile-time)](🚮%20Program%20Language%20Translation%20&%20Compilation%20Theory%20(Compile-time)/Program%20Language%20Translation%20&%20Compilation%20Theory%20(Compile-time).md)

↗ [OS Memory Management (Main Memory + Secondary Memory Resource)](../🔑%20CS%20Core/🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource).md)
↗ [Computer Memory & Storage](../🔑%20CS%20Core/🧬%20Computer%20System/Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/Computer%20Memory%20&%20Storage/Computer%20Memory%20&%20Storage.md)
↗ [Address Space & Memory Layout](../🔑%20CS%20Core/🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/Address%20Space%20&%20Memory%20Layout.md)
↗ [Procedure (Function) Call & Runtime Memory Layout](🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Procedure%20(Function)%20Call%20&%20Runtime%20Memory%20Layout/Procedure%20(Function)%20Call%20&%20Runtime%20Memory%20Layout.md)

↗ [Operating System & OS Kernel (Theory Part)](../🔑%20CS%20Core/🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part).md)
↗ [Operating Systems & Kernels (Engineering Part)](../🔑%20CS%20Core/🥷🏼%20Operating%20Systems%20&%20Kernels%20(Engineering%20Part)/Operating%20Systems%20&%20Kernels%20(Engineering%20Part).md)


### Other Resources
🔥 🎬【操作系统上的程序 (什么是程序和编译器) [南京大学2022操作系统-P2]】 https://www.bilibili.com/video/BV12L4y1379V/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d



## Intro: Concepts Review
![Automata_Formal_Lan.excalidraw | 800](../../../Assets/Illustrations/Math/Automata_Formal_Lan.excalidraw.md)
<small>Automata and Formal Language</small>
↗ [Automata Theory and (Formal) Language Theory](../🧮%20Math%20&%20Theoretical%20Computer%20Science%20(TCS)/🤼‍♀️%20Mathematical%20Logics/😶‍🌫️%20Theory%20of%20Computation/Computability%20Theory/🍏%20Automata%20Theory%20and%20(Formal)%20Language%20Theory/Automata%20Theory%20and%20(Formal)%20Language%20Theory.md)

![computer_architecture.excalidraw | 800](../../../Assets/Illustrations/Computer%20System/computer_architecture_and_computer_science.excalidraw.md)
<small>Computer System & Computer Science Overview</small>
↗ [Computer Architecture](../🔑%20CS%20Core/🧬%20Computer%20System/Computer%20Architecture/Computer%20Architecture.md)

![](../../../../../../../Assets/Pics/Screenshot%202023-03-21%20at%209.12.25%20PM.png)
<small>Instruction Processing Level</small>
↗ [Instruction Levels](../🔑%20CS%20Core/🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/📌%20ISA%20Basics/📌%20Instruction%20Basics/Instruction%20Levels/Instruction%20Levels.md)

![](../../../../../../Assets/Pics/Screenshot%202023-05-22%20at%209.50.58%20PM.png)
<small>A examplary illustration of the compilation, linking, loading & execution process</small>
↗ [Program Execution & Compilation System /🤔 Working Process of Compilation Systems](Program%20Execution%20&%20Compilation%20System.md#🤔%20Working%20Process%20of%20Compilation%20Systems)



## 😆 Program, Computer, and Automation
🔥 🎬【操作系统上的程序 (什么是程序和编译器) [南京大学2022操作系统-P2]】 https://www.bilibili.com/video/BV12L4y1379V/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d


### Digital Circuits and State Machine (Automaton)
状态 = 寄存器保存的值 (flip-flop)
初始状态 = RESET (implementation dependent)
迁移 = 组合逻辑电路计算寄存器下一周期的值


### Program's State Machine Model (Programming Languages Semantics)
> ↗ [Formal Semantics and Programming Language](../🧮%20Math%20&%20Theoretical%20Computer%20Science%20(TCS)/🤼‍♀️%20Mathematical%20Logics/😶‍🌫️%20Theory%20of%20Computation/Computability%20Theory/🍏%20Automata%20Theory%20and%20(Formal)%20Language%20Theory/Formal%20Semantics%20and%20Programming%20Language.md)
> Push-Down Automaton (PDA)
#### 1️⃣ Program's State Machine: Application Perspective
C 程序的状态机模型 (语义，semantics)
- 状态 = 堆 + 栈
- 初始状态 = `main` 的第一条语句
- 迁移 = 执行一条简单C语句
    - 任何 C 程序都可以改写成 “非复合语句” 的 C 代码
    - [真的有这种工具](https://cil-project.github.io/cil/) (C Intermediate Language) 和[解释器](https://gitlab.com/zsaleeba/picoc)

C 程序的状态机模型 (语义，semantics)
- 状态 = stack frame 的列表 (每个 frame 有 PC) + 全局变量
- 初始状态 = main(argc, argv), 全局变量初始化
- 迁移 = 执行 top stack frame PC 的语句; PC++
    - 函数调用 = push frame (frame.PC = 入口)
    - 函数返回 = pop frame

应用：将任何递归程序就地转为非递归
#### 2️⃣ Program's State Machine: CPU(Computer) Perspective
C 程序的状态机模型 (语义，semantics)
- 状态 = 内存 MM + 寄存器 RR
- 初始状态 = (稍后回答)
- 迁移 = 执行一条指令
#### Application Program and OS Program
> ↗ [Operating System & OS Kernel (Theory Part)](../🔑%20CS%20Core/🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part).md)
> ↗ [Operating Systems & Kernels (Engineering Part)](../🔑%20CS%20Core/🥷🏼%20Operating%20Systems%20&%20Kernels%20(Engineering%20Part)/Operating%20Systems%20&%20Kernels%20(Engineering%20Part).md)
> ↗ [Operating System Kernel (Kernel Mode)](../🔑%20CS%20Core/🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/Operating%20System%20Kernel%20(Kernel%20Mode).md)
> ↗ [System Calls](../🔑%20CS%20Core/🧬%20Computer%20System/Operating%20System%20&%20OS%20Kernel%20(Theory%20Part)/OS%20Processes%20&%20Automata%20Management%20(CPU%20+%20Main%20Memory%20Resource)/📌%20Processes%20Description%20&%20Control/System%20Calls/System%20Calls.md)
> ↗ [Interrupts (Software & Hardware)](../🔑%20CS%20Core/🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Program%20Execution%20(Runtime)/Instruction%20Execution/Interrupts%20(Software%20&%20Hardware).md)

操作系统上的程序:
- 所有的指令都只能计算
	- deterministic: `mov`, `add`, `sub`, `call`, ...
	- non-deterministic: `rdrand`, ...
	- 但这些指令甚至都无法使程序停下来 (NEMU: 加条 `trap` 指令)
- 调用操作系统 `syscall`
	- 把 `(M,R)`完全交给操作系统，任其修改
	    - 一个有趣的问题：如果程序不打算完全信任操作系统？
	- 实现与操作系统中的其他对象交互
	    - 读写文件/操作系统状态 (例如把文件内容写入 MM)
	    - 改变进程 (运行中状态机) 的状态，例如创建进程/销毁自己

==操作系统上的应用程序 = 计算 + `syscall`==
- 程序 = 计算 → `syscall` → 计算 → ...
	- 被操作系统加载
		- 通过另一个进程执行 `execve` 设置为初始状态
	- 状态机执行
		- 进程管理：`fork`, `execve`, `exit`, ...
		- 文件/设备管理：`open`, `close`, `read`, `write`, ...
		- 存储管理：`mmap`, `brk`, ...
	- 直到 `_exit (exit_group)` 退出
- 💀 问题：怎么构造一个最小的 Hello, World？
- 💀 问题：一个普通的、人畜无害的 Hello World C 程序执行的第一条指令在哪里？ /“二进制程序状态机的初始状态是什么？” (↗ [Intro to Computer Science /Questions Leading my CS Study](💋%20Intro%20to%20Computer%20Science/Intro%20to%20Computer%20Science.md#Questions%20Leading%20my%20CS%20Study))

==操作系统上的应用程序：都在操作系统 API (syscall) 和操作系统中的对象上构建==
- 编译器 (gcc)，代表其他工具程序
	- 主要的系统调用：execve, read, write
	- `strace -f gcc a.c` (gcc 会启动其他进程)
		- 可以管道给编辑器 `vim -`
		- 编辑器里还可以 `%!grep` (细节/技巧)
- 图形界面程序 (xedit)，代表其他图形界面程序 (例如 vscode)
	- 主要的系统调用：`poll`, `recvmsg`, `writev`
	- `strace xedit`
	    - 图形界面程序和 X-Window 服务器按照 X11 协议通信
	    - 虚拟机中的 `xedit` 将 X11 命令通过 ssh (X11 forwarding) 转发到 Host
- 窗口管理器
    - 管理设备和屏幕 (`read`/`write`/`mmap`)
    - 进程间通信 (`send`, `recv`)
- 任务管理器
    - 访问操作系统提供的进程对象 (`readdir`/`read`)
    - 参考 gdb 里的 `info proc *`
- 杀毒软件
    - 文件静态扫描 (`read`)
    - 主动防御 (`ptrace`)
    - 其他更复杂的安全机制……


### Compilation: Switch /Transfer Between Program's State Machine
> ↗ [Formal Semantics and Programming Language](../🧮%20Math%20&%20Theoretical%20Computer%20Science%20(TCS)/🤼‍♀️%20Mathematical%20Logics/😶‍🌫️%20Theory%20of%20Computation/Computability%20Theory/🍏%20Automata%20Theory%20and%20(Formal)%20Language%20Theory/Formal%20Semantics%20and%20Programming%20Language.md)
> ↗ [Program Execution & Compilation System](../🔑%20CS%20Core/🛣️%20Program%20Execution%20&%20Compilation%20System/Program%20Execution%20&%20Compilation%20System.md)
> ↗ [Compilation Phase](../🔑%20CS%20Core/🛣️%20Program%20Execution%20&%20Compilation%20System/🚮%20Program%20Language%20Translation%20&%20Compilation%20Theory%20(Compile-time)/Compilation%20Phase/Compilation%20Phase.md)
> ↗ [Compilation & Program Loading Tools](../🔑%20CS%20Core/👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Compilation%20&%20Program%20Loading%20Tools/Compilation%20&%20Program%20Loading%20Tools.md)

编译器：源代码 $S$ (状态机) → 二进制代码 $C$ (状态机)
$$C=compile(S)$$

编译 (优化) 的正确性 (Soundness): 
- $S$ 与 $C$ 的可观测行为严格一致
    - system calls; volatile variable loads/stores; termination
- Trivially 正确 (但低效) 的实现
    - 解释执行/直接翻译 $S$ 的语义

现代 (与未来的) 编译优化: 
- 在保证观测一致性 (sound) 的前提下改写代码 (rewriting)
	- Inline assembly 也可以参与优化
	    - 其他优化可能会跨过不带 barrier 的 `asm volatile`
	- Eventual memory consistency
	- Call to external CU = write back visible memory
- 这给了我们很多想象的空间
	- Semantic-based compilation (synthesis)
	- AI-based rewriting
	- Fine-grained semantics & system call fusion

> [An executable formal semantics of C with applications](https://dl.acm.org/doi/10.1145/2103621.2103719) (POPL'12)
> [CompCert C verified compiler](https://compcert.org/motivations.html) and a [paper](https://xavierleroy.org/publi/compcert-backend.pdf) (POPL'06, Most Influential Paper Award 🏅)
> [Copy-and-patch compilation](https://dl.acm.org/doi/10.1145/3485513) (OOPSLA'21, Distinguished Paper 🏅)



## Ref
