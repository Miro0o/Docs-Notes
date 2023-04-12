# Transport Layer

[TOC]



## Res
↗ [Transportation Layer Security](../../../../CyberSecurity/Network%20Security/🏇%20Network%20Security%20Basics%20&%20Protocols/🚉%20Transportation%20Layer%20Security/Transportation%20Layer%20Security.md)



## Overview
🔗【深入浅出计算机网络 - 5.1.1 进程间基于网络的通信】 https://www.bilibili.com/video/BV1bD4y117Y8/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d


Transport Layer takes in charge with **port-to-port communication** between **two process**. IP routing is beyond Transport Layer (IP routing lies in Network Layer). 
- A transport layer protocol provides for **logical communication** between **application processes** running on different hosts.

Data processed in transport layer is referred as **Segment**.

> ❗ To simplify terminology, we refer to the transport-layer packet as a **segment**. We mention, however, that ==the Internet literature (for example, the RFCs) also refers to the transport-layer packet for TCP as a segment but often refers to the packet for UDP as a datagram. However, this same Internet literature also uses the term datagram for the network-layer packet!==

More than one transport-layer protocol may be available to network applications. For example, ==**the Internet** has two protocols: TCP and UDP.== Each of these protocols provides a different set of transport-layer services to the invoking application.
- **TCP**: reliable, connection-oriented service
- **UDP**: unreliable, connectionless service

![](../../../../../Assets/Pics/Screenshot%202022-11-26%20at%206.33.36%20PM.png)


### Transport Layer Services
1️⃣ minimal transport-layer services: (provided by UDP)
- **process-to-process data delivery**
	- The most fundamental responsibility of UDP and TCP is to ==extend IP’s delivery service between two end systems to a delivery service between two processes running on the end systems.== Extending host-to-host delivery to process-to-process delivery is called transport-layer **multiplexing** and **demultiplexing**.
		- Communication between app layer and transport layer is implemented by **Socket**. The machenism of Socket is about multiplexing and demultiplexing.
- **error checking**
	- UDP and TCP also provide integrity checking by including error- detection fields in their segments’ headers

2️⃣ On top of UDP, TCP services provide **reliable data transfer service**:
- **flow control**
	- Using flow control, sequence numbers, acknowledgments, and timers, TCP ensures that data is delivered from sending process to receiving process, correctly and in order. TCP thus converts IP’s unreliable service between end systems into a reliable data transport service between processes.
- **congestion control**
	- Congestion control is not so much a service provided to the invoking application as it is a service for the Internet as a whole, a service for the general good;
	- UDP traffic, on the other hand, is unregulated. An application using UDP transport can send at any rate it pleases, for as long as it pleases.

3️⃣ A transport protocol can use **encryption** to guarantee that application messages are not read by intruders, even when the network layer cannot guarantee the confidentiality of transport-layer segments.

![](../../../../../Assets/Pics/Screenshot%202022-11-13%20at%2010.19.36%20AM.png)
![](../../../../../Assets/Pics/Screenshot%202023-04-12%20at%2010.19.12%20AM.png)



## Port Number
![](../../../../../Assets/Pics/Screenshot%202022-11-13%20at%2010.23.06%20AM.png)
The port numbers ranging from 0 to 1023 are called well-known port numbers.

The list of well-known port numbers is given in RFC 1700 and is updated at http://www.iana.org [RFC 3232].



## Multiplexing & Demultiplexing
🔗【深入浅出计算机网络 - 5.1.3 运输层端口号、复用与分用的概念】 https://www.bilibili.com/video/BV1N841147b6/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

> We know that transport-layer multiplexing requires
> 1. that sockets have unique identifiers, and 
> 2. that each segment have special fields that indicate the socket to which the segment is to be delivered. These special fields are the **source port number field** and the **destination port number field.** (The UDP and TCP segments have other fields as well, as discussed in the subsequent sections of this chapter.)

In C/S model, server side has to deal with multiple influx of segments from different clients simotaniously --- this handling uses demultiplexing; the client side has to deal with multiple exflux of segment to different servers simotaniously --- this handling uses multiplexing. 
- **Multiplexing, demultiplexing**: based on segment, datagram header field values

- **UDP (connectionless multiplexing & demultiplexing):** demultiplexing using destination port number (only)
	- or another explanation says it uses 2-tuple: consisting of a destination IP address and a destination port number.

- **TCP (connection-oriented multiplexing & demultiplexing):** demultiplexing using **4-tuple**: source and destination IP addresses, and port numbers

- ==Multiplexing/demultiplexing happen at *all* layers==



## UDP 🆚 TCP in TCP/IP Architecture
🔗【深入浅出计算机网络 - 5.1.2 TCP/IP体系结构运输层中的两个重要协议】 https://www.bilibili.com/video/BV1Zd4y1o7Sv/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d


![](../../../../../Assets/Pics/Screenshot%202022-11-13%20at%2010.20.46%20AM.png)

![](../../../../../Assets/Pics/Screenshot%202022-11-13%20at%2010.21.56%20AM.png)

![](../../../../../Assets/Pics/Screenshot%202022-11-13%20at%2010.25.59%20AM.png)

![](../../../../../Assets/Pics/Screenshot%202022-11-13%20at%2010.27.21%20AM.png)

![](../../../../../Assets/Pics/Screenshot%202022-11-13%20at%2010.28.22%20AM.png)

![](../../../../../Assets/Pics/Screenshot%202022-11-12%20at%2011.55.51%20PM.png)




## Ref
