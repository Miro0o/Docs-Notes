# Systems on Chip (SOC)

[TOC]



## Res
### Related Topics



## Intro
Systems on a chip (SOCs) are distinguished from microcontrollers by their complexity and increased on-chip resources.

- Microcontrollers often require supporting circuits such as signal processors, decoders, and signal converters, to name only a few.

A system on a chip is **a single piece of silicon** that contains all circuits required to deliver a set of functions. A system on a chip can even **consist of more than one processor**. These loosely coupled processors do not necessarily share the same clock or memory space. The individual processor functions can be specialized to the extent that they are provided with ISAs designed specifically for efficient programming in a particular application domain. 

> For example, an Internet router may have several RISC processors that handle communications traffic and a CISC processor for configuration and management of the router itself.

Although microcontroller memory is usually measured in kilobytes, SOCs can include memory on the order of megabytes. With their larger memories, SOCs accommodate full-featured **real-time operating systems**. The great advantage of SOCs is that they are faster, smaller, and more reliable, and they consume less power than the several chips they replace.


### off-the-self SOCs 🆚 Customization of SOCs
Although there are many **off-the-shelf SOCs** available, **customization** is sometimes required to support a particular application.

Rather than absorb the cost of designing an SOC from scratch, a **semi-custom chip** may be assembled from **intellectual property (IP) circuits** licensed from companies that specialize in creating and testing circuit designs. Licensed IP module designs are combined with customized circuits to produce a **circuit mask**. The completed mask is subsequently sent to a circuit fabrication facility (a fab) to be etched in silicon. This process is very expensive. Mask costs are now approaching $1 million (US). The economic benefits of this approach must therefore be considered carefully. If a standard SOC provides the same functionality -- even with lesser performance -- the $1 million expenditure is not justifiable. We return to this idea in a later section.



## SoC Microarchitecture
> 🔗 https://foxsen.github.io/archbase/计算机组成原理和结构.html#soc单片结构

片上系统（System on Chip，简称SoC）是一种单片计算机系统解决方案，它在单个芯片上集成了处理器、内存控制器、GPU以及硬盘、USB、网络等IO接口，使得用户搭建计算机系统时只需要使用单个主要芯片即可，如图[5.10]所示。

![](../../../../../Assets/Pics/Pasted%20image%2020240414144958.png)
<small>图 5.10: SOC单片结构</small>

目前SoC主要应用于移动处理器和工业控制领域，相比上述几种多片结构，单片SoC结构的集成度更高，功耗控制方法更加灵活，有利于系统的小型化和低功耗设计。但也因为全系统都在一个芯片上实现，导致系统的扩展性没有多片结构好，升级的开销也更大。随着技术的发展，封装基板上的互连技术不断发展和成熟。越来越多的处理器利用多片封装技术在单个芯片上集成多个硅片，以扩展芯片的计算能力或IO能力。例如AMD Ryzen系列处理器通过在封装上集成多个处理器硅片和IO硅片，以提供针对不同应用领域的计算能力。龙芯3C5000L处理器则通过在封装上集成4个4核龙芯3A5000硅片来实现单片16核结构。

目前，主流商用处理器中面向中高端领域的处理器普遍采用两片结构，而面向中低端及嵌入式领域的处理器普遍采用单片结构。SoC单片结构最常见的是在手机等移动设备中。



## Ref

