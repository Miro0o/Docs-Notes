# IO System

[TOC]



## Res



## Overview


## Interfaces
↗ [Computer System /Interfaces](../../../Microcomputer%20Principles%20&%20Interfaces/Computer%20Interfaces/Computer%20Interfaces.md)
↗ [ASM /Interfaces](../../../../👩‍💻%20Languages%20Programming/ASM/⚡️%20ASM%20Advance/Interfaces/Interfaces.md)



## I/O Devices
External devices that engage in I/O with computer systems can be roughly grouped into three categories:
1. **Human readable**: Suitable for communicating with the computer user. Examples include printers and terminals, the latter consisting of video display, key- board, and perhaps other devices such as a mouse.

2. **Machine readable**: Suitable for communicating with electronic equipment. Examples are disk drives, USB keys, sensors, controllers, and actuators.

3. **Communication**: Suitable for communicating with remote devices. Examples are digital line drivers and modems.

![](../../../../../../Assets/Pics/Screenshot%202023-05-25%20at%202.56.06%20PM.png)


### Metrics
There are great differences across classes and even substantial differences within each class. Among the key differences are the following:
- **Data rate**: There may be differences of several orders of magnitude between the data transfer rates. Figure 11.1 gives some examples.

- **Application**: The use to which a device is put has an influence on the soft- ware and policies in the OS and supporting utilities. For example, a disk used for files requires the support of file management software. A disk used as a backing store for pages in a virtual memory scheme depends on the use of virtual memory hardware and software. Furthermore, these applications have an impact on disk scheduling algorithms (discussed later in this chapter). As another example, a terminal may be used by an ordinary user or a system administrator. These uses imply different privilege levels and perhaps different priorities in the OS.

- **Complexity of control**: A printer requires a relatively simple control interface. A disk is much more complex. The effect of these differences on the OS is filtered to some extent by the complexity of the I/O module that controls the device, as discussed in the next section.

- **Unit of transfer**: Data may be transferred as a stream of bytes or characters (e.g., terminal I/O) or in larger blocks (e.g., disk I/O).

- **Data representation**: Different data encoding schemes are used by different devices, including differences in character code and parity conventions.

- **Error conditions**: The nature of errors, the way in which they are reported, their consequences, and the available range of responses differ widely from one device to another.

This diversity makes a uniform and consistent approach to I/O, both from the point of view of the operating system and from the point of view of user processes, difficult to achieve.



## I/O and Performance
### Amdahl's Law
In 1967, Gene Amdahl recognized the interrelationship of all components with the overall efficiency of a computer system. He quantified his observations in a formula, which is now known as **Amdahl’s Law**. In essence, Amdahl’s Law states that ==the overall speedup of a computer system depends on both the speedup in a particular component and how much that component is used by the system.== In symbols:
$$S = \frac{1}{(1-f)+(f/k)}$$

where
- S is the **overall system speedup**;  
- f is the **fraction of work** performed by the faster component;
- k is the **speedup of a new component**.

#### Different Expressions of 'Speed-up'



## I/O Architectures
We will define input/output as a subsystem of components that moves coded data between external devices and a host system, consisting of a CPU and main memory. I/O subsystems include but are not limited to:
- **Blocks of main memory** that are devoted to I/O functions  
- **Buses** that provide the means of moving data into and out of the system
- **Control modules** in the host and in peripheral devices  
- **Interfaces** to external components such as keyboards and disks  
- **Cabling or communications links** between the host system and its peripherals.


![](../../../../../../Assets/Pics/Screenshot%202023-05-09%20at%202.21.48%20PM.png)


### I/O Protocols
The exact form and meaning of the signals exchanged between a sender and a receiver is called a **protocol**.
Protocols include
- **command signals**, such as “Printer reset”;
- **status signals**, such as “Tape ready”; 
- or **data-passing signals**, such as “Here are the bytes you requested.”

In most data-exchanging protocols, the receiver must acknowledge the commands and data sent to it or indicate that it is ready to receive data. This type of protocol exchange is called a **handshake**.


### I/O Control Methods
↗ [IO Control Methods](IO%20Control%20Methods.md)


### Types of I/O
#### 1️⃣ Character I/O
**Keyboard Input**
Pressing a key on a computer keyboard sets in motion a sequence of activities that process the keystroke as a single event (no matter how fast you type!). The reason for this is found within the mechanics of the keyboard. Each key controls a small switch that closes a connection in a matrix of conductors that runs horizontally and vertically beneath the keys. When a key switch closes, a distinct **scan code** is read by the keyboard circuitry. The scan code is then passed to a **serial interface circuit**, which translates the scan code into a **character code**. The interface places the character code in a keyboard buffer that is maintained in low memory. Immediately afterward, an **I/O interrupt signal** is raised. The characters wait patiently in the buffer until they are retrieved -- one at a time -- by a program (or until the buffer is reset). The keyboard circuits are able to process a new keystroke only after the old one is on its way to the buffer. Although it is certainly possible to press two keys at once, only one of the strokes can be processed at a time.

Because of the random, sequential nature of character I/O as just described, it is best handled through **interrupt-driven I/O processing**.

#### 2️⃣ Block I/O
**Storage I/O**
Magnetic disks and tapes store data in blocks. Consequently, it makes sense to manage disk and tape I/O in block units. 

Blocks can be different sizes, depending on the particular hardware, software, and applications involved. Determining an ideal block size can be an important activity when a system is being tuned for optimum performance. 
- High-performance systems handle large blocks more efficiently than they handle small blocks. 
- Slower systems should manage bytes in smaller blocks; otherwise, the system may become unresponsive to user input during I/O.

Block I/O lends itself to **DMA** or **channel I/O processing**.


### I/O Buses Operation
#### Timing Diagrams


### I/O Buses and Interfaces
↗ [Expansion Bus](../../../Microcomputer%20Principles%20&%20Interfaces/Computer%20Interfaces/Computer%20IO%20Interfaces/Expansion%20Bus/Expansion%20Bus.md)
↗ [Computer IO Interfaces](../../../Microcomputer%20Principles%20&%20Interfaces/Computer%20Interfaces/Computer%20IO%20Interfaces/Computer%20IO%20Interfaces.md)



## Data Transmission Modes
↗ [Data Transmission Modes](Data%20Transmission%20Modes.md)



## Ref
[Amdahl's law | Wikipedia]: https://en.wikipedia.org/wiki/Amdahl%27s_law

[Computer Organization | Amdahl’s law and its proof ---- GeeksforGeeks]: https://www.geeksforgeeks.org/computer-organization-amdahls-law-and-its-proof/

