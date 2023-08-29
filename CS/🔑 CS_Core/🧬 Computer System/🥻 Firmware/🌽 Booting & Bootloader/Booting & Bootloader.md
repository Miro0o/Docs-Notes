# Booting & Bootloader

[TOC]



## Res



## Intro
### Booting
In [computing](https://en.wikipedia.org/wiki/Computing "Computing"), **booting** is the process of starting a [computer](https://en.wikipedia.org/wiki/Computer "Computer") as initiated via [hardware](https://en.wikipedia.org/wiki/Computer_hardware "Computer hardware")such as a button or by a [software](https://en.wikipedia.org/wiki/Software "Software") command. After it is switched on, a computer's [central processing unit](https://en.wikipedia.org/wiki/Central_processing_unit "Central processing unit") (CPU) has no software in its [main memory](https://en.wikipedia.org/wiki/Main_memory "Main memory"), so some process must load software into memory before it can be executed. This may be done by hardware or [firmware](https://en.wikipedia.org/wiki/Firmware "Firmware") in the CPU, or by a separate processor in the computer system.

**Boot** is short for **[_bootstrap_](https://en.wikipedia.org/wiki/Bootstrapping "Bootstrapping")** or **bootstrap load** and derives from the phrase _[to pull oneself up by one's bootstraps](https://en.wikipedia.org/wiki/Bootstrapping#Etymology "Bootstrapping")_. The usage calls attention to the requirement that, if most software is loaded onto a computer by other software already running on the computer, some mechanism must exist to load the initial software onto the computer. Early computers used a variety of ad-hoc methods to get a small program into memory to solve this problem. The invention of [read-only memory](https://en.wikipedia.org/wiki/Read-only_memory "Read-only memory") (ROM) of various types solved this paradox by allowing computers to be shipped with a start up program that could not be erased. Growth in the capacity of ROM has allowed ever more elaborate start up procedures to be implemented.


### Computer States



## ⭐️ Modern Boot Loader
When a computer is turned off, its software‍—‌including operating systems, application code, and data‍—‌remains stored on [non-volatile memory](https://en.wikipedia.org/wiki/Non-volatile_memory "Non-volatile memory"). When the computer is powered on, it typically does not have an operating system or its loader in [random-access memory](https://en.wikipedia.org/wiki/Random-access_memory "Random-access memory") (RAM). The computer first executes a relatively small program stored in [read-only memory](https://en.wikipedia.org/wiki/Read-only_memory "Read-only memory") (ROM, and later [EEPROM](https://en.wikipedia.org/wiki/EEPROM "EEPROM"), [NOR flash](https://en.wikipedia.org/wiki/NOR_flash "NOR flash")) along with some needed data, to initialize CPU and motherboard, to initialize [RAM](https://en.wikipedia.org/wiki/RAM "RAM") (especially on x86 systems), to access the nonvolatile device (usually [block device](https://en.wikipedia.org/wiki/Block_device "Block device"), e.g. NAND flash) or devices from which the operating system programs and data can be loaded into RAM.

The small program that starts this sequence is known as a **bootstrap loader**, **bootstrap** or **boot loader**. Often, **multiple-stage boot loaders** are used, during which several programs of increasing complexity load one after the other in a process of **[chain loading](https://en.wikipedia.org/wiki/Chain_loading "Chain loading")**.

Some earlier computer systems, upon receiving a boot signal from a human operator or a peripheral device, may load a very small number of fixed instructions into memory at a specific location, initialize at least one CPU, and then point the CPU to the instructions and start their execution. These instructions typically start an input operation from some peripheral device (which may be switch-selectable by the operator). Other systems may send hardware commands directly to peripheral devices or I/O controllers that cause an extremely simple input operation (such as "read sector zero of the system device into memory starting at location 1000") to be carried out, effectively loading a small number of boot loader instructions into memory; a completion signal from the I/O device may then be used to start execution of the instructions by the CPU.

Smaller computers often use less flexible but more automatic boot loader mechanisms to ensure that the computer starts quickly and with a predetermined software configuration. In many desktop computers, for example, the bootstrapping process begins with the CPU executing software contained in ROM (for example, the [BIOS](https://en.wikipedia.org/wiki/BIOS "BIOS") of an [IBM PC](https://en.wikipedia.org/wiki/IBM_PC "IBM PC")) at a predefined address (some CPUs, including the Intel [x86 series](https://en.wikipedia.org/wiki/Intel_8086 "Intel 8086") are designed to execute this software after reset without outside help). This software contains rudimentary functionality to search for devices eligible to participate in booting, and load a small program from a special section (most commonly the [boot sector](https://en.wikipedia.org/wiki/Boot_sector "Boot sector")) of the most promising device, typically starting at a fixed [entry point](https://en.wikipedia.org/wiki/Entry_point "Entry point")such as the start of the sector.

Boot loaders may face peculiar constraints, especially in size; for instance, on the IBM PC and compatibles, the boot code must fit in the [Master Boot Record](https://en.wikipedia.org/wiki/Master_Boot_Record "Master Boot Record") (MBR) and the [Partition Boot Record](https://en.wikipedia.org/wiki/Partition_Boot_Record "Partition Boot Record") (PBR), which in turn are limited to a single sector; on the [IBM System/360](https://en.wikipedia.org/wiki/IBM_System/360 "IBM System/360"), the size is limited by the IPL medium, e.g., [card](https://en.wikipedia.org/wiki/Punched_card "Punched card") size, track size.

On systems with those constraints, the first program loaded into RAM may not be sufficiently large to load the operating system and, instead, must load another, larger program. The first program loaded into RAM is called a first-stage boot loader, and the program it loads is called a second-stage boot loader.

### 1️⃣ First-Stage Boot Loader
↗ [First-Stage Boot Loader](First-Stage%20Boot%20Loader/First-Stage%20Boot%20Loader.md)

### 2️⃣ Second-Stage Boot Loader
↗ [Second-Stage Boot Loader](Second-Stage%20Boot%20Loader/Second-Stage%20Boot%20Loader.md)

### 3️⃣ Network Booting
↗ [Network Booting](Network%20Booting/Network%20Booting.md)



## Ref
[Booting | Wikipedia]: https://en.wikipedia.org/wiki/Booting

👍 电脑基础知识普及：BIOS、EFI与UEFI详解！ - 知乎用户fB10GU的文章 - 知乎 https://zhuanlan.zhihu.com/p/54108702

> [what is UEFI, and how is it different from BIOS?](https://www.howtogeek.com/56958/htg-explains-how-uefi-will-replace-the-bios/)
> both UEFI and BIOS are low-level software that starts when you boot your PC before booting your operating system, but UEFI is a more modern solution, supporting larger hard drives, faster boot times, more security features, and—conveniently—graphics and mouse cursors.
> The BIOS will soon be dead: Intel has announced [plans to completely replace it with UEFI](https://www.anandtech.com/show/12068/intel-to-remove-bios-support-from-uefi-by-2020) on all their [chipsets](https://www.pugetsystems.com/labs/articles/Z97-vs-H97---What-is-the-Difference-562/) by 2020.
