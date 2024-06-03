# Procedure & Function Call

[TOC]



## Res
### Related Topics
↗ [ASM (Assembly Languages)](../../../👩‍💻%20Programming%20Methodology%20and%20Languages/ASM%20(Assembly%20Languages)/ASM%20(Assembly%20Languages).md)
↗ [Instruction Set Architecture (ISA) & Processor Architecture](../../../🧬%20Computer%20System/Computer%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture/Instruction%20Set%20Architecture%20(ISA)%20&%20Processor%20Architecture.md)
↗ [Stack](../../../🦄%20Algorithm%20&%20Data%20Structure/Data%20Structures/Queue%20&%20Stack/Stack.md)
↗ [Address Space](../../../🧬%20Computer%20System/Operating%20System%20(Theory%20Part)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/Address%20Space.md)

↗ [Network Sockets](../../../🧬%20Computer%20System/Operating%20System%20(Theory%20Part)/OS%20IO%20System/IO%20Generality%20(via%20Abstraction)/🛜%20Network%20Sockets/Network%20Sockets.md)
↗ [Network Programming & RPC](../../../🏎️%20Computer%20Networking%20and%20Communication/Network%20Programming%20&%20RPC/Network%20Programming%20&%20RPC.md)
↗ [Internal Sockets](../../../🧬%20Computer%20System/Operating%20System%20(Theory%20Part)/OS%20Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource)/IPC%20(Inter%20Process%20Communication)/🧦%20Sockets/🌉%20Internal%20Sockets/Internal%20Sockets.md)

↗ [System Calls](../../../🧬%20Computer%20System/Operating%20System%20(Theory%20Part)/OS%20Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource)/📌%20Processes%20Description%20&%20Control/System%20Calls/System%20Calls.md)
↗ [System Core Function Libraries & C Standard Library (User Mode)](../../../🥷🏼%20Operating%20System%20(Engineering%20Part)/📟%20System%20Level%20Programming/😴%20Operating%20System%20Components%20&%20Runtime%20Libraries/📌%20System%20Core%20Function%20Libraries%20&%20C%20Standard%20Library%20(User%20Mode)/System%20Core%20Function%20Libraries%20&%20C%20Standard%20Library%20(User%20Mode).md)
↗ [Linux System Calls](../../../🥷🏼%20Operating%20System%20(Engineering%20Part)/Linux%20(Derived%20From%20UNIX%20Family)/🔩%20Linux%20Kernel/👽%20Linux%20System%20Calls/Linux%20System%20Calls.md)

↗ [FAQ /👉 Linux Library Functions Call 🆚 System Call 🆚 Procedure/Function Call](../../../🥷🏼%20Operating%20System%20(Engineering%20Part)/FAQ.md#👉%20Linux%20Library%20Functions%20Call%20🆚%20System%20Call%20🆚%20Procedure/Function%20Call)



## Intro



## 🎯 Local Procedure Call
> ↗ [Internal Sockets](../../../🧬%20Computer%20System/Operating%20System%20(Theory%20Part)/OS%20Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource)/IPC%20(Inter%20Process%20Communication)/🧦%20Sockets/🌉%20Internal%20Sockets/Internal%20Sockets.md)


### Local Process Calls Another Local Process
#### Stack Frame Structure
#### Procedure Call & Return Instruction
#### Register Conventions
#### 🤔 LPC Instance

### Local Process Calls Itself (Iterative Calling)



## 🎯 Remote Procedure Call
> ↗ [Network Sockets](../../../🧬%20Computer%20System/Operating%20System%20(Theory%20Part)/OS%20IO%20System/IO%20Generality%20(via%20Abstraction)/🛜%20Network%20Sockets/Network%20Sockets.md)
> ↗ [Network Programming & RPC](../../../🏎️%20Computer%20Networking%20and%20Communication/Network%20Programming%20&%20RPC/Network%20Programming%20&%20RPC.md)
> ↗ [SE /Middleware /Remote Procedure Call (RPC)](../../../../Software%20Engineering/Web%20Development/🥪%20Middleware/RPC%20Services/RPC%20Services.md)



## Ref
[👍 深入理解计算机系统（3.7）------过程（函数的调用原理）]: https://www.cnblogs.com/ysocean/p/7625917.html

过程在高级语言中也称为函数，方法。一个过程的调用包括将数据（以过程参数和返回值的形式）和控制从代码的一部分传递到另一部分。此外，它还必须在进入时为过程的局部变量分配空间，并在退出时释放空间。大多数机器，包括我们一直讲的 IA32，只提供转移控制到过程和从过程中转移出控制这种简单指令。数据传递和局部变量的分配释放都是通过操纵程序栈来实现。

合理的构建方法并调用，能大大增加代码的复用性，也能使代码结构更加清晰，接下来我们就来详细的介绍。

[系统调用与过程调用 | CSDN]: https://blog.csdn.net/shuyangxiaogou/article/details/5666098
1. 调用形式不同
2. 被调用代码的位置不同
3. 提供方式不同
4. 调用的实现不同
