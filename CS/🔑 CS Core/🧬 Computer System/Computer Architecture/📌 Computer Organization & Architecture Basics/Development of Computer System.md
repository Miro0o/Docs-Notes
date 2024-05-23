# Development of Computer System

[TOC]



## Res



## Intro
![](../../../../../Assets/Pics/Screenshot%202023-05-08%20at%204.26.42%20PM.png)



## Computer System Theory Development
### 0️⃣ Theory of Computation
↗ [Theory of Computation](../../../../🧮%20Math%20&%20Theoretical%20Computer%20Science%20(TCS)/🤼‍♀️%20Mathematical%20Logics/😶‍🌫️%20Theory%20of%20Computation/Theory%20of%20Computation.md)


### 0️⃣ Mathematical Model of General Computation and Turing Machine
↗ [Turing Machine](../../../../🧮%20Math%20&%20Theoretical%20Computer%20Science%20(TCS)/🤼‍♀️%20Mathematical%20Logics/😶‍🌫️%20Theory%20of%20Computation/🍏%20Turing%20Machine/Turing%20Machine.md)


### 1️⃣ Stored-Program Computer and Von Neumann Architecture
![|250](../../../../../Assets/Pics/Screenshot%202023-05-08%20at%204.45.36%20PM.png)

↗ [Computer Microarchitectures (Computer Organization) & von Neumann Model](../Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model.md)

**冯·诺依曼架构（Von Neumann Architecture）** 是冯诺依曼参与第一台电子计算机ENIAC的设计并与团队讨论下一代计算机EDVAC的结构时总结而成的，因此冯诺依曼结构严格来说并不是由冯诺依曼独自完成的，而是他首先发表（因为这事，冯诺依曼与EDVAC团队决裂，当然，这是后话了）。 

冯·诺依曼架构将通用计算机定义为以下 3 个基本原则：
1. **采用二进制：** 指令和数据均采用二进制格式；
2. **存储程序：** 一个计算机程序，不可能只有一条指令，而是由成千上万条指令组成的。指令和数据均存储在存储器中，而不是早期的插线板中，计算机按需从存储器中取指令和取数据；
3. **计算机由 5 个硬件组成：** 运算器、控制器、存储器、输入设备和输出设备。在最开始的计算机中，五个部件是围绕着运算器运转的，这使得存储器和 I/O 设备之间的数据传送也需要经过运算器。 **而现代计算机中，五个部件是围绕着存储器运转的，这使得存储器和 I/O 设备可以直接完成数据传送，而不需要经过 CPU。**

> 更加细致地说冯诺依曼结构
> 1. 采用存储程序方式，指令和数据不加区别混合存储在同一个存储器中，即指令与数据在内存中主要通过控制器的指针进行操作（例如像X86里的SP,IP等寄存器），且在每个内存段中包含了读写权限等信息。
> 2. 存储器是按地址访问的线性编址的一维结构，每个单元的位数是固定的。在我们编程时，一般是将内存作为一段一段的使用，而对于计算机而言，其实就是一条直线。
> 3. 指令由操作码和地址组成。操作码指明本指令的操作类型,地址码指明操作数和地址。操作数本身无数据类型的标志，它的数据类型由操作码确定。
> 4. 通过执行指令直接发出控制信号控制计算机的操作。指令在存储器中按其执行顺序存放，由指令计数器指明要执行的指令所在的单元地址。指令计数器只有一个，一般按顺序递增，但执行顺序可按运算结果或当时的外界条件而改变。
> 5. 以运算器为中心，I/O设备与存储器间的数据传送都要经过运算器。
> 6. 数据以二进制表示，大大提高了存储效率。


### 3️⃣ Other Architectures
↗ [Non-von Neumann Based Microarchitectures](../Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/🤵%20Non-von%20Neumann%20Based%20Microarchitectures/Non-von%20Neumann%20Based%20Microarchitectures.md)


### 4️⃣ Quantum Computer
↗ [Quantum Computing](../../Computing%20Systems/Quantum%20Computing/Quantum%20Computing.md)



## Computer System Hardware Development
↗ [Computer System Hardware Development](Computer%20System%20Hardware%20Development.md)



## Computer System Software Development
↗ [Development(History) of Operating Systems](../../Operating%20System%20(Theory%20Part)/🦺%20Operating%20System%20Basics/Development(History)%20of%20Operating%20Systems.md)

↗ [History of Computer Networks](../../../🏎️%20Computer%20Networking%20and%20Communication/📌%20Computer%20Networking%20Basics/0x00%20Computer%20Network%20and%20Communication%20Introduction%20&%20Overview/History%20of%20Computer%20Networks.md)



## Ref
[Turing machine | WikiPedia]: https://en.wikipedia.org/wiki/Turing_machine
[Von Neumann Architecture | Wikipedia]: https://en.wikipedia.org/wiki/Von_Neumann_architecture


