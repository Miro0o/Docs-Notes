# Datapath (Bus)

[TOC]


## Overview

![](../../../../../../../Assets/Pics/Screenshot%202023-03-05%20at%2010.19.55%20AM.png)
![](../../../../../../../Assets/Pics/Pasted%20image%2020230302132111.png)


### 1️⃣ Address Bus
Address lines indicate the location (e.g., in memory) that the data should be either read from or written to.


### 2️⃣ Data Bus
These data lines contain the actual information that must be moved from one location to another.

The number of data lines is the **width of the bus (总线宽度)**


### 3️⃣ Control Bus
Control lines indicate which device has permission to use the bus and for what purpose (reading or writing from memory or from an input/output [I/O] device, for example). Control lines also transfer acknowledgments for bus requests, interrupts, and clock synchronization signals


### 4️⃣ Bus Clock & Bus Cycle
> ⚠ 
> Generally, when we mention the clock, we are referring to the **system clock** or the **master clock** that regulates the CPU and other components. 
> 
> However, certain buses also have their own clocks. **Bus clocks** are one of them. ==Bus clocks are usually slower than CPU clocks, causing bottleneck problems.==


![](../../../../../../../Assets/Pics/Screenshot%202023-06-24%20at%206.57.41%20PM.png)



## Types of Bus
### 1️⃣ Internal Bus (System Bus)
The internal bus connects the CPU, memory, and all other internal components


### 2️⃣ External Bus (Expansion Buses)
External buses connect external devices, peripherals, expansion slots, and I/O ports to the rest of the computer.


### 3️⃣ Local Bus 
Data buses that connect a peripheral device **directly to the CPU**.


### 4️⃣ Backplane Bus
#TODO 


## Specifications of Bus
### ⏰ Synchronous Bus
Synchronous buses are clocked, and things happen only at the clock ticks (a sequence of events is controlled by the clock).

Every device is synchronized by the rate at which the clock ticks, or the clock rate. The bus cycle time mentioned is the reciprocal of the bus clock rate.

#### Clock Skew (drift in the clock)
Because the clock controls the transactions, any clock skew (drift in the clock) has the potential to cause problems, implying that the bus must be kept as short as possible so the clock drift cannot get overly large. 

In addition, the bus cycle time must not be shorter than the length of time it takes information to traverse the bus. The length of the bus, therefore, imposes restrictions on both the bus clock rate and the bus cycle time.


### 👋🏻 Asynchronous Bus
#### C/S Architecture (Client/Server, Master/Slave)
Quite often, devices are divided into master and slave categories; a master device is one that initiates actions, and a slave is one that responds to requests by a master.


#### Other Architectures
> A bus can be point-to-point, connecting two specific components (as seen in Figure 4.1a). Or it can be a common pathway that connects a number of devices, requiring these devices to share the bus (referred to as a multipoint bus and shown in Figure 4.1b).


#### Bus Protocols
#TODO 


#### 🏁 Bus Arbitration
**In a very simple system (such as the one we present in the next section), the processor is the only device allowed to become a bus master**. This is good in terms of avoiding chaos, but bad because the processor now is involved in every transaction that uses the bus.

**In systems with more than one master device, bus arbitration is required**. Bus arbitration schemes must provide priority to certain master devices and, at the same time, make sure lower-priority devices are not starved out.

##### ⭐️ Bus Arbitration Schemes
> ↗ [Multiple Access Links & Protocols](../../../../../🏎️%20Computer%20Networking/📌%20Computer%20Networking%20Basics/0x06%20Data%20Link%20Layer/Switched%20Network%20Channels/Broadcast%20Channels/Multiple%20Access%20Links%20&%20Protocols/Multiple%20Access%20Links%20&%20Protocols.md)

1. **Daisychain arbitration**: This scheme uses a “grant bus” control line that is passed down the bus from the highest-priority device to the lowest-priority device. (Fairness is not ensured, and it is possible that low-priority devices are “starved out” and never allowed to use the bus.) This scheme is simple but not fair.
   
2. **Centralized parallel arbitration**: Each device has a request control line to the bus and a centralized arbiter that selects who gets the bus. Bottlenecks can result from using this type of arbitration.

3. **Distributed arbitration using self-selection**: This scheme is similar to centralized arbitration, but instead of a central authority selecting who gets the bus, the devices themselves determine who has the highest priority and who should get the bus.

4. **Distributed arbitration using collision detection**: Each device is allowed to make a request for the bus. If the bus detects any collisions (multiple simultaneous requests), the device must make another request. (==Ethernet uses this type of arbitration==. ↗ [CSMA with Collision Detection (CSMA-CD)](../../../../../🏎️%20Computer%20Networking/📌%20Computer%20Networking%20Basics/0x06%20Data%20Link%20Layer/Switched%20Network%20Channels/Broadcast%20Channels/Multiple%20Access%20Links%20&%20Protocols/Random%20Access%20Protocols/Carrier%20Sense%20Multiple%20Access%20(CSMA)/CSMA%20with%20Collision%20Detection%20(CSMA-CD)/CSMA%20with%20Collision%20Detection%20(CSMA-CD).md) )



## I/O Buses Operation
### Timing Diagrams
![](../../../../../../../Assets/Pics/Screenshot%202023-06-24%20at%206.26.42%20PM.png)



## Ref