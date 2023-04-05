# Memory

[TOC]



## Res


## Overview


## The Memory Hierarchy
### Why Hierarchical Design
As might be expected, there is a trade-off among the three key characteristics of memory: **capacity**, **access time**, and **cost**. A variety of technologies are used to implement memory systems, and across this spectrum of technologies, the following relationships hold:

- Faster access time, greater cost per bit
- Greater capacity, smaller cost per bit
- Greater capacity, slower access speed


### Hierarchy in a nutshell
The way out of the above dilemma is to not rely on a single memory component or technology but to employ a memory hierarchy. A typical hierarchy is illustrated in Figure 1.14. As one goes down the hierarchy, the following occur:

1.  Decreasing cost per bit
2.  Increasing capacity
3.  Increasing access time
4.  Decreasing frequency of access to the memory by the processor

![](../../../../../../Assets/Pics/Pasted%20image%2020230301122408.png)
<small>Simplified Computer Memory Hierarchy </small>

#### Main Memory
↗ [Main Memory](Main%20Memory.md)

A hard disk can also be used to provide an extension to main memory known as **virtual memory**, this part is available at ↗ [OS /Virtual Memory](../../../Operating%20System%20(Theory)/Memory%20Management/Virtual%20Memory/Virtual%20Memory.md).


#### Cache Memory
Main memory is usually extended with a higher-speed, smaller cache. The cache is not usually visible to the programmer or, indeed, to the processor. It is a device for staging the movement of data between main memory and processor registers to improve performance.

↗ [Cache Memory](Cache%20Memory.md)


#### Auxiliary Memory
Data are stored more permanently on external mass storage devices, of which the most common are hard disk and removable media, such as removable disk, tape, and optical storage.

External, nonvolatile memory is also referred to as **secondary memory** or **auxiliary memory**. These are used to store program and data files, and are usually visible to the programmer only in terms of files and records, as opposed to individual bytes or words.

↗ [Auxiliary Memory](Auxiliary%20Memory.md)


### Locality of Reference
There are three basic forms of locality:
- **Temporal locality**: Recently accessed items tend to be accessed again in the near future.

- **Spatial locality**: Accesses tend to be clustered in the address space (for example, as in arrays or loops).

- **Sequential locality**: Instructions tend to be accessed sequentially.



## 🪠 Types of Memory
### ROM, Read-Only Memory
There are five basic types of ROM: ROM, PROM, EPROM, EEPROM, and flash memory. 
- **PROM (programmable read- only memory)** is a variation on ROM. PROMs can be programmed by the user with the appropriate equipment. Whereas ROMs are hardwired, PROMs have fuses that can be blown to program the chip. Once programmed, the data and instructions in PROM cannot be changed. 
- **EPROM (erasable PROM)** is programmable with the added advantage of being reprogrammable (erasing an EPROM requires a special tool that emits ultraviolet light). To reprogram an EPROM, the entire chip must first be erased. 
- **EEPROM (electrically erasable PROM)** removes many of the disadvantages of EPROM: No special tools are required for erasure (this is performed by applying an electric field) and you can erase only portions of the chip, one byte at a time. 
- **Flash memory** is essentially EEPROM with the added benefit that data can be written or erased in blocks, removing the one-byte-at-a-time limitation. This makes flash memory faster than EEPROM. Flash memory has become a very popular type of storage and is used in many different devices, including cell phones, digital cameras, and music players. It is also being used in solid-state disk drives.


### RAM, Random Access Memroy

> RAM is somewhat of a misnomer; a more appropriate name is read-write memory


#### DRAM
The basic operation of all DRAM memories is the same, but there are many flavors, including 
- multibank DRAM (MDRAM)
- fast-page mode (FPM) DRAM
- extended data out (EDO) DRAM
- burst EDO DRAM (BEDO DRAM)
- synchronous dynamic random access memory (SDRAM)
- synchronous-link (SL) DRAM
- double data rate (DDR) SDRAM
- rambus DRAM (RDRAM)
- direct rambus (DR) DRAM


#### SRAM
The different types of SRAM include asynchronous SRAM, synchronous SRAM, and pipeline-burst SRAM.


## Memory Organization & Access
As in ↗ [Memory Access](Memory%20Access.md)


## Ref
