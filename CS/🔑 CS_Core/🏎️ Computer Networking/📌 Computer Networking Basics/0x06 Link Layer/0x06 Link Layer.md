# Link Layer

[TOC]



## Res
🔗 【深入浅出计算机网络 - 3.1 数据链路层概述】 https://www.bilibili.com/video/BV1WG411b7op/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

↗ [Mobile Network (Cellular Network)](../../Wireless%20&%20Mobile%20Network/Mobile%20Network%20(Cellular%20Network)/Mobile%20Network%20(Cellular%20Network).md)
↗ [Data Link Layer Security](../../../../CyberSecurity/Network%20Security/🏇%20Network%20Security%20Basics%20&%20Protocols/🔌%20Physical%20Layer%20Security/Data%20Link%20Layer%20Security.md)



## Overview
### Two Types of Link-Layer Channels
In discussing the link layer, we’ll see that there are two fundamentally different types of link-layer channels. 

- The first type are **broadcast channels**, which connect multiple hosts in wireless LANs, in satellite networks, and in hybrid fiber-coaxial cable (HFC) access networks. Since many hosts are connected to the same broadcast communication channel, a so-called **medium access protocol (MAC)** is needed to coordinate frame transmission. In some cases, a central controller may be used to coordinate transmissions; in other cases, the hosts themselves coordinate transmissions. 

- The second type of link-layer channel is the **point-to-point communication link**, such as that often found between two routers connected by a long-distance link, or between a user’s office computer and the nearby Ethernet switch to which it is connected. Coordinating access to a point-to-point link is simpler; the reference material on this book’s Web site has a detailed discussion of the **Point-to-Point Protocol (PPP)**, which is used in settings ranging from dial-up service over a telephone line to high-speed point-to-point frame transport over fiber-optic links.


### Services Provided by Link Layer
- **Framing**. Almost all link-layer protocols encapsulate each network-layer datagram within a link-layer frame before transmission over the link. A frame consists of a data field, in which the network-layer datagram is inserted, and a number of header fields. The structure of the frame is specified by the link-layer protocol. We’ll see several different frame formats when we examine specific link-layer protocols in the second half of this chapter.

- **Link access**. A **medium access control (MAC) protocol** specifies the rules by which a frame is transmitted onto the link. For point-to-point links that have a single sender at one end of the link and a single receiver at the other end of the link, the MAC protocol is simple (or nonexistent) -- the sender can send a frame whenever the link is idle. The more interesting case is when multiple nodes share a single broadcast link -- the so-called **multiple access problem**. Here, the MAC protocol serves to coordinate the frame transmissions of the many nodes.

- **Reliable delivery**. When a link-layer protocol provides reliable delivery service, it guarantees to move each network-layer datagram across the link without error. Recall that certain transport-layer protocols (such as TCP) also provide a reliable delivery service. Similar to a transport-layer reliable delivery service, a link-layer reliable delivery service can be achieved with acknowledgments and retransmissions (see Section 3.4). A link-layer reliable delivery service is often used for links that are prone to high error rates, such as a wireless link, with the goal of **correcting an error locally** -- on the link where the error occurs -- rather than forcing an end-to-end retransmission of the data by a transport- or application-layer protocol. However, link-layer reliable delivery can be considered an unnecessary overhead for low bit-error links, including fiber, coax, and many twisted-pair copper links. For this reason, many wired link-layer protocols do not provide a reliable delivery service.
 
- **Error detection and correction**. The link-layer hardware in a receiving node can incorrectly decide that a bit in a frame is zero when it was transmitted as a one, and vice versa. Such bit errors are introduced by **signal attenuation** and **electromagnetic noise**. Because there is no need to forward a datagram that has an error, many link-layer protocols provide a mechanism to detect such bit errors. This is done by having the transmitting node include error-detection bits in the frame, and having the receiving node perform an error check. 

	- Recall from Chapters 3 and 4 that the Internet’s transport layer and network layer also provide a limited form of error detection -- the **Internet checksum**. **Error detection in the link layer is usually more sophisticated and is implemented in hardware**. Error correction is similar to error detection, except that a receiver not only detects when bit errors have occurred in the frame but also determines exactly where in the frame the errors have occurred (and then corrects these errors).


### Implementation of Link Layer
#### Hardware Level Implementation
Figure 6.2 shows a typical host architecture. The Ethernet capabilities are either integrated into the motherboard chipset or implemented via a low-cost dedicated Ethernet chip. For the most part, the link layer is implemented on a chip called the **network adapter**, also sometimes known as a **network interface controller (NIC)**. The network adapter implements many link layer services including framing, link access, error detection, and so on. Thus, much of a link-layer controller’s functionality is implemented in hardware.

> For example, Intel’s 700 series adapters [Intel 2020] implements the **Ethernet protocols** we’ll study in Section 6.5; the Atheros AR5006 [Atheros 2020] controller implements the **802.11 WiFi** protocols we’ll study in Chapter 7.

![](../../../../../Assets/Pics/Screenshot%202023-05-24%20at%209.59.57%20AM.png)

- On the sending side, the controller takes a datagram that has been created and stored in host memory by the higher layers of the protocol stack, encapsulates the datagram in a link-layer frame (filling in the frame’s various fields), and then transmits the frame into the communication link, following the link-access protocol. 

- On the receiving side, a controller receives the entire frame, and extracts the network-layer datagram. If the link layer performs error detection, then it is the sending controller that sets the error-detection bits in the frame header and it is the receiving controller that performs error detection.


#### Software Level Implementation
> Figure 6.2 shows that while most of the link layer is implemented in hardware, part of the link layer is implemented in software that runs on the host’s CPU. 

The software components of the link layer implement higher-level link-layer functionality such as 
1. assembling link-layer addressing information
2. activating the controller hardware. 

On the receiving side, link-layer software responds to controller interrupts (for example, due to the receipt of one or more frames), handling error conditions and passing a datagram up to the network layer. 

Thus, the link layer is a combination of hardware and software—the place in the protocol stack where software meets hardware. [Intel 2020] provides a readable overview (as well as a detailed description) of the XL710 controller from a software-programming point of view.



## Error Control in Link Layer
> A full treatment of the theory and implementation of this topic is itself the topic of many textbooks (e.g., [Schwartz 1980] or [Bertsekas 1991]), and our treatment here is necessarily brief. Our goal here is to develop an intuitive feel for the capabilities that error-detection and -correction techniques pro- vide and to see how a few simple techniques work and are used in practice in the link layer.


![](../../../../../Assets/Pics/Screenshot%202023-05-31%20at%208.45.59%20AM.png)

Generally, more sophisticated error-detection and -correction techniques (that is, those that have a smaller probability of allowing undetected bit errors) incur a larger overhead—more computation is needed to compute and transmit a larger number of error-detection and -correction bits.

---
Let’s now examine three techniques for detecting errors in the transmitted data
- **parity checks** (to illustrate the basic ideas behind error detection and correction)
- **check-summing methods** (which are more typically used in the transport layer)
- **cyclic redundancy checks (CRC)** (which are more typically used in the link layer in an adapter).

This part is noted at ↗ [Error Control](../Error%20Control/Error%20Control.md)



## Ref
