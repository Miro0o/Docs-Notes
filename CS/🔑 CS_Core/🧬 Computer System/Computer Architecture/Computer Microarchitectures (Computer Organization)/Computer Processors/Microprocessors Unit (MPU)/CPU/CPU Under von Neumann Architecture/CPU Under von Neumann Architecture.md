# CPU Under von Neumann Architecture

[TOC]



## Res
More about processors at ↗ [Computer Processors](../../../Computer%20Processors.md)



## Overview
### CPU in a von Neumann Model
![](../../../../../../../../../Assets/Pics/Pasted%20image%2020230302132111.png)
<small>The Modified von Neumann Architecture</small>

![](../../../../../../../../../Assets/Pics/Screenshot%202023-03-02%20at%204.11.10%20PM.png)
<small>Computer Components: Top-Level View</small>

Figure 1.1 depicts simplified Von Neumann-based computer top-level components. 

One of the processor’s functions is to exchange data with memory. For this purpose, it typically makes use of two internal (to the processor) registers:
- a memory address register (**MAR**), which specifies the address in memory for the next read or write; 
- and a memory buffer register (**MBR**), which contains the data to be written into memory, or receives the data read from memory. 

Similarly:
- an I/O address register (**I/OAR**) specifies a particular I/O device. 
- an I/O buffer register (**I/OBR**) is used for the exchange of data between an I/O module and the processor.


### CPU Inside
![](../../../../../../../../../Assets/Pics/arch%20(1).jpg)
<small>Simplified von Neumann CPU Architecture</small>

![](../../../../../../../../../Assets/Pics/Pasted%20image%2020230304155503.png)
<small>Early von Neumann model as a SISD architecture</small>

#TODO 

#### 1️⃣ Datapath
For other bus look at ↗ [Datapath (Bus)](../../../../🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Datapath%20(Bus)/Datapath%20(Bus).md)


#### 2️⃣ Control Unit
a module responsible for sequencing operations and making sure the correct data are where they need to be at the correct time.

As in ↗ [Control Unit](Control%20Unit.md) for more.


#### 3️⃣ Arithmetic Unit
↗ [ALU](ALU.md)


### Word Length
>概括地讲，16位结构 (16 位机、字长为 16位等常见说法与16位结构的含义相同) 描述了一个CPU 具有下面几方面的结构特性。
>- 运算器一次最多可以处理16位的数据;
>- 寄存器的最大宽度为16位:
>- 寄存器和运算器之间的通路为16位。
 8086是16位结构的CPU，这也就是说，在8086内部，能够一次性处理、传输、暂时存储的信息的最大长度是16位的。内存单元的地址在送 上地址总线之前，必须在CPU中处理、传输、暂时存放 ，对于16位CPU一次性处理、传输、暂时存储16位的地址。



## Clock 
>⚠ 
>Generally, when we mention the clock, we are referring to the **system clock** or the **master clock** that regulates the CPU and other components.
>
>However, certain buses also have their own clocks. **Bus clocks** are one of them. Bus clocks are usually slower than CPU clocks, causing bottleneck problems.
>
>↗ [Datapath (Bus)](../../../../🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Datapath%20(Bus)/Datapath%20(Bus).md)


### CPU Clock Basics


### 📈 Minimal Clock Cycle Time
Most machines are synchronous: There is a master clock signal, which ticks (changing from 0 to 1 to 0 and so on) at regular intervals. Registers must wait for the clock to tick before new data can be loaded. 

It seems reasonable to assume that if we speed up the clock, the machine will run faster. **However, there are limits on how short we can make the clock cycles**. When the clock ticks and new data are loaded into the registers, the register outputs are likely to change. These changed output values must propagate through all the circuits in the machine until they reach the input of the next set of registers, where they are stored. The clock cycle must be long enough to allow these changes to reach the next set of registers. 

If the clock cycle is too short, we could end up with some values not reaching the registers. This would result in an **inconsistent state** in our machine, which is definitely something we must avoid.

Therefore, the **minimum clock cycle time** must be at least as great as the **maximum propagation delay** of the circuit, from each set of register outputs to register inputs.

>  What if we “shorten” the distance between registers to shorten the propagation delay?
>  
>  We could do this by adding registers between the output registers and the corresponding input registers. But recall that registers cannot change values until the clock ticks, so we have, in effect, increased the number of clock cycles. For example, an instruction that would require two clock cycles might now require three or four (or more, depending on where we locate the additional registers).


### 📉 Maximal Clock Cycle Time
System components have defined performance bounds, indicating the maximum time required for the components to perform their functions. Manufacturers guarantee that their components will run within these bounds in the most extreme circumstances. When we connect all of the components together serially, where one component must complete its task before another can function properly, it is important to be aware of these performance bounds so we are able to synchronize the components properly. 

However, many people push the bounds of certain system components in an attempt to improve system performance. Overclocking is one method people use to achieve this goal.

#### Overclocking
Although many components are potential candidates, one of the most popular components for overclocking is the CPU. The basic idea is to run the CPU at clock and/or bus speeds above the upper bound specified by the manufacturer.

Although this can increase system performance, one must be careful not to create system timing faults or, worse yet, overheat the CPU. The system bus can also be overclocked, which results in overclocking the various components that communicate via the bus. Overclocking the system bus can provide considerable performance improvements, but can also damage the components that use the bus or cause them to perform unreliably.


### Clock Speed 🆚 CPU Time (Processing Time)
Most machine instructions require one or two clock cycles, but some can take 35 or more. We present the following formula to relate seconds to cycles:
$$CPU\ TIME = \frac{seconds}{programs} = \frac{instructions}{programs} \times \frac{average\ cycles}{instructions} \times \frac{seconds}{cycles}$$

i.e.
$$CPU\ TIME = \overline{instructions} \times \overline{cycles} \times  \overline{seconds}$$

It is important to note that the architecture of a machine has a large effect on its performance. ==Two machines with the same clock speed do not necessarily execute instructions in the same number of cycles.==



## Instruction and Data
↗ [Memory Access](../../../../🧝🏻‍♀️%20von%20Neumann%20Based%20Microarchitecture/Memory/Memory%20Access.md)



## Instruction Execution
![](../../../../../../../../../Assets/Pics/Screenshot%202023-03-03%20at%209.05.51%20AM.png)

> Detailed info at ↗ [Instruction Execution](../../../../../Instruction%20Set%20Architecture%20(ISA)/📌%20Instruction%20Basics/Instruction%20Execution/Instruction%20Execution.md)


### Interrupts
![](../../../../../../../../../Assets/Pics/Screenshot%202023-03-03%20at%209.10.54%20AM.png)

![](../../../../../../../../../Assets/Pics/Screenshot%202023-03-03%20at%209.15.46%20AM.png)

More at ↗ [Processor /Interrupts](../../../../../Instruction%20Set%20Architecture%20(ISA)/📌%20Instruction%20Basics/Instruction%20Execution/Interrupts.md)
or ↗ [ASM /Interrupts](../../../../../../../👩‍💻%20Languages%20Programming/ASM%20(Assembly%20Languages)/⚡️%20ASM%20Advance/Interrupts/Interrupts.md)



## Ref