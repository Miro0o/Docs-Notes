# Computer Memory & Storage

[TOC]



## Res
### Related Topics
↗ [Digital (Logic) Electronics Foundations](../../../⚡️%20Digital%20(Logic)%20Electronics%20Foundations/Digital%20(Logic)%20Electronics%20Foundations.md)

↗ [OS Memory Management (Main Memory + Secondary Memory Resource)](../../../Operating%20System%20(Theory%20Part)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource)/OS%20Memory%20Management%20(Main%20Memory%20+%20Secondary%20Memory%20Resource).md)
↗ [OS Processes Management (CPU + Main Memory Resource)](../../../Operating%20System%20(Theory%20Part)/OS%20Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource)/OS%20Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource).md)



## Overview



## 🪜 Hierarchical Cached Memory (Design Level)
### Why Hierarchical Design (Problems without Hierarchical Design)
As might be expected, there is a trade-off among the ==three key characteristics of memory: **capacity**, **access time**, and **cost**==. A variety of technologies are used to implement memory systems, and across this spectrum of technologies, the following relationships hold:

- Faster access time, greater cost per bit;
- Greater capacity, smaller cost per bit;
- Greater capacity, slower access speed;


### Why Cached Design
> The main idea of a memory hierarchy is that storage at one level serves as a cache for storage at the next lower level. Thus, the register file is a cache for the L1 cache. Caches L1 and L2 are caches for L2 and L3, respectively. The L3 cache is a cache for the main memory, which is a cache for the disk. On some networked systems with distributed file systems, the local disk serves as a cache for data stored on the disks of other systems.


### Memory Hierarchy
The way out of the above dilemma is to not rely on a single memory component or technology but to employ a memory hierarchy. A typical hierarchy is illustrated below. As one goes down the hierarchy, the following occur:

1.  Decreasing cost per bit
2.  Increasing capacity
3.  Increasing access time
4.  Decreasing frequency of access to the memory by the processor

![](../../../../../../../Assets/Pics/Pasted%20image%2020230301122408.png)
<small>Simplified Computer Memory Hierarchy </small>

The base types that normally constitute the hierarchical memory system include **registers**, **cache**, **main memory**, **secondary memory**, and o**ff-line bulk memory**.
#### 0️⃣ Registers
↗ [Register](../🚦%20Computer%20Processors%20&%20Logic%20Chips/Microprocessors%20Unit%20(MPU)/CPU%20(Central%20Processing%20Unit)/📌%20Basic%20CPU%20Components/Register.md)
#### 1️⃣ Cache Memory (高速缓存/ 主存和CPU之间的缓冲内存)
Main memory is usually extended with a higher-speed, smaller cache. The cache is not usually visible to the programmer or, indeed, to the processor. It is a device for staging the movement of data between main memory and processor registers to improve performance.

↗ [CPU Cache](../🚦%20Computer%20Processors%20&%20Logic%20Chips/Microprocessors%20Unit%20(MPU)/CPU%20(Central%20Processing%20Unit)/📌%20Basic%20CPU%20Components/CPU%20Cache.md)
#### 2️⃣ Main Memory (Primary Memory)（主存）
↗ [Primary Storage (Main Memory) Technologies & RAM](Primary%20Storage%20(Main%20Memory)%20Technologies%20&%20RAM/Primary%20Storage%20(Main%20Memory)%20Technologies%20&%20RAM.md)
##### 👻 Virtual Memory
🙈 A hard disk can also be used to provide an extension to main memory known as **virtual memory**, this part is available at ↗ [OS /Memory Virtualization](Primary%20Storage%20(Main%20Memory)%20Technologies%20&%20RAM/Virtual%20Memory%20(Hardware%20and%20Control%20Structure)/Virtual%20Memory%20(Hardware%20and%20Control%20Structure).md).
#### 3️⃣ Auxiliary Memory (Secondary Memory)（辅存，二级存储）
Data are stored more permanently on external mass storage devices, of which the most common are hard disk and removable media, such as removable disk, tape, and optical storage.

External, nonvolatile memory is also referred to as **secondary memory** or **auxiliary memory**. These are used to store program and data files, and are usually visible to the programmer only in terms of files and records, as opposed to individual bytes or words.

↗ [Secondary (Auxiliary) Storage Technologies & DAS (Directly Attached Storage)](Secondary%20(Auxiliary)%20Storage%20Technologies%20&%20DAS%20(Directly%20Attached%20Storage)/Secondary%20(Auxiliary)%20Storage%20Technologies%20&%20DAS%20(Directly%20Attached%20Storage).md)
#### 4️⃣ Off-line Bulk Memory
Off-line bulk memory (which includes tertiary memory and off-line storage) requires either human or robotic intervention before any data can be accessed; the data must be transferred from the storage media to secondary memory. 

1. **Tertiary memory** includes things such as **optical jukeboxes** and **tape libraries**, which are typically under robotic control (a robotic arm mounts and dismounts the tapes and disks). It is used for enterprise storage in large systems and networks and is not something an average computer user sees often. These devices typically have nonuniform access times, as the time to retrieve data depends on whether the device is mounted. 

> An **optical jukebox** (光碟柜) is a robotic data storage device that can automatically load and unload **optical discs**, such as [Compact Disc](Compact_Disc.html "Compact Disc"), [DVD](DVD.html "DVD"), [Ultra Density Optical](Ultra_Density_Optical.html "Ultra Density Optical") or [Blu-ray disc](Blu-ray_disc.html "Blu-ray disc") and can provide terabytes (TB) and petabytes (PB) of tertiary storage. The devices are often called optical disk libraries, robotic drives, or autochangers. Jukebox devices may have up to 2,000 slots for disks, and usually have a picking device that traverses the slots and drives. The arrangement of the slots and picking devices affects performance, depending on the space between a disk and the picking device. Seek times and transfer rates vary depending upon the optical technology.

> In computer storage, a **tape library** (磁带柜), sometimes called a **tape silo**, **tape robot** or **tape jukebox**, is a storage device which contains one or more tape drives, a number of slots to hold tape cartridges, a barcode reader to identify tape cartridges and an automated method for loading tapes (a robot).


3. ==**Off-line storage** includes those devices that are connected, loaded with data, and then disconnected from the system, such as floppy disks, flash memory devices, optical disks, and even removable hard drives.== By using such a hierarchical scheme, one can improve the effective access speed of the memory, using only a small number of fast (and expensive) chips. This allows designers to create a computer with acceptable performance at a reasonable cost.


### Hierarchical Memory Performance Metrics 
- **Hit**: The requested data resides in a given level of memory (typically, we are concerned with the hit rate only for upper levels of memory).
- **Miss**: The requested data is not found in the given level of memory.
- **Hit rate**: The percentage of memory accesses found in a given level of memory.
- **Miss rate**: The percentage of memory accesses not found in a given level of memory. 

> Note: $miss rate = 1 − hit rate$.

- **Hit time**: The time required to access the requested information in a given level of memory.
- **Miss penalty**: The time required to process a miss, which includes replacing a block in an upper level of memory, plus the additional time to deliver the requested data to the processor. (The time to process a miss is typically significantly larger than the time to process a hit.)


### ⭐️ Locality of Reference (访问局限性)
There are three basic forms of locality:
- **Temporal locality** (时间局限性): Recently accessed items tend to be accessed again in the near future.
- **Spatial locality** (空间局限性): Accesses tend to be clustered in the address space (for example, as in arrays or loops).
- **Sequential locality** (时序局限性): Instructions tend to be accessed sequentially.



## 🪠 Types of Memory & Storage (Engineering Level)
### 1️⃣ Volatile Memory (Registers /Cache Memory /Main Memory)
#### Registers
↗ [Register](../🚦%20Computer%20Processors%20&%20Logic%20Chips/Microprocessors%20Unit%20(MPU)/CPU%20(Central%20Processing%20Unit)/📌%20Basic%20CPU%20Components/Register.md)
#### RAM (Random Access Memory)
> RAM is somewhat of a misnomer; a more appropriate name is read-write memory
> 
> ↗ [Primary Storage (Main Memory) Technologies & RAM](Primary%20Storage%20(Main%20Memory)%20Technologies%20&%20RAM/Primary%20Storage%20(Main%20Memory)%20Technologies%20&%20RAM.md)
##### DRAM
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
##### SRAM
The different types of SRAM include asynchronous SRAM, synchronous SRAM, and pipeline-burst SRAM.


### 2️⃣ Non-Volatile Memory (Secondary Memory)
↗ [Secondary (Auxiliary) Storage Technologies & DAS (Directly Attached Storage)](Secondary%20(Auxiliary)%20Storage%20Technologies%20&%20DAS%20(Directly%20Attached%20Storage)/Secondary%20(Auxiliary)%20Storage%20Technologies%20&%20DAS%20(Directly%20Attached%20Storage).md)
#### ROM (Read-Only Memory)
There are five basic types of ROM: ROM, PROM, EPROM, EEPROM, and flash memory. 
- **PROM (programmable read-only memory)** is a variation on ROM. PROMs can be programmed by the user with the appropriate equipment. Whereas ROMs are hardwired, PROMs have fuses that can be blown to program the chip. Once programmed, the data and instructions in PROM cannot be changed. 
- **EPROM (erasable PROM)** is programmable with the added advantage of being reprogrammable (erasing an EPROM requires a special tool that emits ultraviolet light). To reprogram an EPROM, the entire chip must first be erased. 
- **EEPROM (electrically erasable PROM)** removes many of the disadvantages of EPROM: No special tools are required for erasure (this is performed by applying an electric field) and you can erase only portions of the chip, one byte at a time. 
- **Flash memory** is essentially EEPROM with the added benefit that data can be written or erased in blocks, removing the one-byte-at-a-time limitation. This makes flash memory faster than EEPROM. Flash memory has become a very popular type of storage and is used in many different devices, including cell phones, digital cameras, and music players. It is also being used in solid-state disk drives.
#### Memory that can both read /write...



## Memory Organization & Access
As in ↗ [Memory Access](../../../../🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Execution%20(Runtime)/Instruction%20Execution/Memory%20Access.md)



## Real-World Examples of Memory Management
↗ [Real World Examples of Memory Management](Primary%20Storage%20(Main%20Memory)%20Technologies%20&%20RAM/Real%20World%20Examples%20of%20Memory%20Management.md)



## Ref
