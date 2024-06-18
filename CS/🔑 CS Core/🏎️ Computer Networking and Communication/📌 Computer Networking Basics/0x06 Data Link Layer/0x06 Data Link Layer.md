# Data Link Layer

[TOC]



## Res
### Related Data Link Layer Implementations
↗ [OS IO System](../../../🧬%20Computer%20System/Operating%20System%20(Theory%20Part)/OS%20IO%20System/OS%20IO%20System.md)
↗ [IO Control Methods](../../../🧬%20Computer%20System/Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/Computer%20IO%20System/📌%20IO%20Control%20Methods/IO%20Control%20Methods.md)

↗ [Computer Bus (Datapath) & Interfaces & Protocols](../../../🧬%20Computer%20System/Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/Computer%20Bus%20(Datapath)%20&%20Interfaces%20&%20Protocols/Computer%20Bus%20(Datapath)%20&%20Interfaces%20&%20Protocols.md)
- ↗ [Expansion Bus (Ports & Computer Bus Interfaces)](../../../🧬%20Computer%20System/Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/Computer%20Bus%20(Datapath)%20&%20Interfaces%20&%20Protocols/Expansion%20Bus%20(Ports%20&%20Computer%20Bus%20Interfaces)/Expansion%20Bus%20(Ports%20&%20Computer%20Bus%20Interfaces).md)
- ↗ [Bus Specifications & Communication Control Systems](../../../🧬%20Computer%20System/Computer%20Architecture/Computer%20Microarchitectures%20(Computer%20Organization)%20&%20von%20Neumann%20Model/Computer%20Bus%20(Datapath)%20&%20Interfaces%20&%20Protocols/📌%20Bus%20Specifications%20&%20Communication%20Control%20Systems/Bus%20Specifications%20&%20Communication%20Control%20Systems.md)

↗ [Mobile Network (Cellular Network)](../0x07%20Physical%20Layer/Wireless%20&%20Mobile%20Network/Mobile%20Network%20(Cellular%20Network)/Mobile%20Network%20(Cellular%20Network).md)
↗ [Physical & Link Layer Security](../../../../CyberSecurity/Network%20Security/🏇%20Network%20Security%20Basics%20&%20Protocols/🔌%20Physical%20(Link)%20Layer%20Security/Physical%20&%20Link%20Layer%20Security.md)

↗ [High Performance Network (HPN) & IDC Technologies](../../🚀%20High%20Performance%20Network%20(HPN)%20&%20IDC%20Technologies/High%20Performance%20Network%20(HPN)%20&%20IDC%20Technologies.md)


### Learning Resources
🎬 【深入浅出计算机网络 - 3.1 数据链路层概述】 https://www.bilibili.com/video/BV1WG411b7op/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

[Data Link Layer | Wikipedia](https://en.wikipedia.org/wiki/Data_link_layer)



## Overview
### Link, Data Link, Frame

![](../../../../../Assets/Pics/Screenshot%202023-06-02%20at%201.56.10%20PM.png)

![](../../../../../Assets/Pics/Screenshot%202023-06-02%20at%201.57.59%20PM.png)

![](../../../../../Assets/Pics/Screenshot%202023-06-02%20at%201.58.10%20PM.png)


### Two Types of Link-Layer Channels
In discussing the link layer, we’ll see that there are two fundamentally different types of link-layer channels. 

- The first type are **broadcast channels**, which connect multiple hosts in wireless LANs, in satellite networks, and in hybrid fiber-coaxial cable (HFC) access networks. Since many hosts are connected to the same broadcast communication channel, a so-called **medium access protocol (MAC)** is needed to coordinate frame transmission. In some cases, a central controller may be used to coordinate transmissions; in other cases, the hosts themselves coordinate transmissions. 

- The second type of link-layer channel is the **point-to-point communication link**, such as that often found between two routers connected by a long-distance link, or between a user’s office computer and the nearby Ethernet switch to which it is connected. Coordinating access to a point-to-point link is simpler; the reference material on this book’s Web site has a detailed discussion of the **Point-to-Point Protocol (PPP)**, which is used in settings ranging from dial-up service over a telephone line to high-speed point-to-point frame transport over fiber-optic links.

↗ [Broadcast Channels](Switched%20LAN/Broadcast%20Channels/Broadcast%20Channels.md)
↗ [P2P Channels](Switched%20LAN/P2P%20Channels/P2P%20Channels.md)


### Implementation of Link Layer 
#### 1️⃣ Hardware Level Implementation
Figure 6.2 shows a typical host architecture. The Ethernet capabilities are either integrated into the motherboard chipset or implemented via a low-cost dedicated Ethernet chip. For the most part, the link layer is implemented on a chip called the **network adapter**, also sometimes known as a **network interface controller (NIC)**. The network adapter implements many link layer services including framing, link access, error detection, and so on. Thus, much of a link-layer controller’s functionality is implemented in hardware.

> For example, Intel’s 700 series adapters [Intel 2020] implements the **Ethernet protocols** we’ll study in Section 6.5; the Atheros AR5006 [Atheros 2020] controller implements the **802.11 WiFi** protocols we’ll study in Chapter 7.

![](../../../../../Assets/Pics/Screenshot%202023-05-24%20at%209.59.57%20AM.png)

- On the sending side, the controller takes a datagram that has been created and stored in host memory by the higher layers of the protocol stack, encapsulates the datagram in a link-layer frame (filling in the frame’s various fields), and then transmits the frame into the communication link, following the **link-access protocol**. 

- On the receiving side, a controller receives the entire frame, and extracts the network-layer datagram. If the link layer performs error detection, then it is the sending controller that sets the error-detection bits in the frame header and it is the receiving controller that performs error detection.

↗ [NIC (Network Adapter)](📌%20Link%20Layer%20(Switched%20Network)%20Basics/Link%20Layer%20Network%20Devices/NIC%20(Network%20Adapter).md)
#### 2️⃣ Software Level Implementation
> Figure 6.2 shows that while most of the link layer is implemented in hardware, part of the link layer is implemented in software that runs on the host’s CPU. 

The software components of the link layer implement higher-level link-layer functionality such as 
1. assembling link-layer addressing information
2. activating the controller hardware. 

On the receiving side, link-layer software responds to **controller interrupts** (for example, due to the receipt of one or more frames), handling error conditions and passing a datagram up to the network layer. 

Thus, the link layer is a combination of hardware and software -- the place in the protocol stack where software meets hardware. [Intel 2020] provides a readable overview (as well as a detailed description) of the XL710 controller from a software-programming point of view.


### Services Provided by Link Layer
↗ [Link Layer Services](📌%20Link%20Layer%20(Switched%20Network)%20Basics/Link%20Layer%20Services/Link%20Layer%20Services.md)



## Ref
[串口通信，ttl，uart，usb这些这间的区别是什么? - Frank Stewart的回答 - 知乎]:
https://www.zhihu.com/question/301957174/answer/528945046

[串口通信，ttl，uart，usb这些这间的区别是什么? - 亿佰特物联网应用的回答 - 知乎]: https://www.zhihu.com/question/301957174/answer/3221820354

[🤔 弱电设计——网络安全基础技术扫盲 | 微信公众号]: https://mp.weixin.qq.com/s/MLk_NLV_nQHayR8503jgyQ
1. 网络模块基础
	1. 网络拓扑图
	2. 网络设备
	3. 安全设备
2. 主机模块基础
	1. 服务器
	2. 数据库
	3. 中间件
	4. 应用系统
	5. 终端
3. WEB服务器通信原理基础
	1. IP
	2. 端口
	3. HTTP协议
	4. HTTP状态码
	5. 域名
