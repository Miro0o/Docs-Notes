# Memory

[TOC]



## Res


## Overview


## The Memory Hierarchy
### Why Hierarchical Design
As might be expected, there is a trade-off among the three key characteristics of memory: **capacity**, **access time**, and **cost**. A variety of technologies are used to implement memory systems, and across this spectrum of technologies, the following relationships hold:

-   Faster access time, greater cost per bit
-   Greater capacity, smaller cost per bit
-   Greater capacity, slower access speed

### Hierarchy in a nutshell

The way out of above dilemma is to not rely on a single memory component or technology, but to employ a memory hierarchy. A typical hierarchy is illustrated in Figure 1.14. As one goes down the hierarchy, the following occur:

1.  Decreasing cost per bit
2.  Increasing capacity
3.  Increasing access time
4.  Decreasing frequency of access to the memory by the processor

![](../../../../../../Assets/Pics/Pasted%20image%2020230301122408.png)
<small>Simplified Computer Memory Hierarchy </small>

#### Main Memory

↗ [Main Memory](Main%20Memory.md)

A hard disk can also be used to provide an extension to main memory known as **virtual memory**, this part is available at ↗ [OS /Virtual Memory](../../../Operating%20System/Memory%20Management/Virtual%20Memory/Virtual%20Memory.md).


#### Cache Memory
Main memory is usually extended with a higher-speed, smaller cache. The cache is not usually visible to the programmer or, indeed, to the processor. It is a device for staging the movement of data between main memory and processor registers to improve performance.

↗ [Cache Memory](Cache%20Memory.md)


#### Auxiliary Memory
Data are stored more permanently on external mass storage devices, of which the most common are hard disk and removable media, such as removable disk, tape, and optical storage.

External, nonvolatile memory is also referred to as **secondary memory** or **auxiliary memory**. These are used to store program and data files, and are usually visible to the programmer only in terms of files and records, as opposed to individual bytes or words.

↗ [Auxiliary Memory](Auxiliary%20Memory.md)


## Memory Orgnization
### Memory Card
![](../../../../../../Assets/Pics/Screenshot%202023-03-01%20at%2011.08.01%20AM.png)


#TODO 

### Memory Space Address
![](../../../../../../Assets/Pics/Screenshot%202023-03-01%20at%2011.08.25%20AM.png)

#### Data Storaging Structure
↗ [Data Representations in CS](../../../😤%20Number,%20Data%20and%20Math/Data%20Representations%20in%20CS.md)

##### LittleEnd & BigEnd

#### Memory Addressing
Byte Addressable 
Byte Unit /Address Unit

Word Addressable
Word Unit /Memory Unit

high-order interleaving
low-order interleaving





## Ref
