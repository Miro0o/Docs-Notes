# Network Layer

[TOC]



## Res
↗ [Network Layer Security](../../../../CyberSecurity/Network%20Security/🏇%20Network%20Security%20Basics%20&%20Protocols/🫱🏻‍🫲🏿%20Network%20Layer%20Security/Network%20Layer%20Security.md)



## Overview
【深入浅出计算机网络 微课视频】 https://www.bilibili.com/video/BV1NT411g7n6/?p=47&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

【深入浅出计算机网络 微课视频】 https://www.bilibili.com/video/BV1NT411g7n6/?p=48&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d


![Screenshot 2022-11-20 at 12.01.39 PM](../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2012.01.39%20PM.png)


### Network Service Models
The Internet’s network layer provides a single service, known as **best-effort service**. This means that IP makes its “best effort” to deliver segments between communicating hosts, but it **makes no guarantees**. 
- it does not guarantee eventual segment delivery;
- it does not guarantee orderly delivery of segments;
- it does not guarantee on the end-to-end delay or minimal bandwidth;
- it does not guarantee the integrity of the data in the segments.

🤣 It might appear that best-effort service is a euphemism for no service at all -- a network that delivered no packets to the destination would satisfy the definition of best-effort delivery service! 

Other network architectures have defined and implemented service models that _go beyond the Internet’s best-effort service_. 
- For example, the ATM network architecture [Black 1995] provides for guaranteed in-order delay, bounded delay, and guaranteed minimal bandwidth. 
There have also been proposed _service model extensions to the Internet architecture_.
- For example, the Intserv architecture [RFC 1633] aims to provide end-end delay guarantees and congestion-free communication. 

Interestingly, in spite of these well-developed alternatives, the Internet’s basic best-effort service model combined with adequate bandwidth provisioning and bandwidth-adaptive application-level protocols such as the DASH protocol we encountered ↗ [Video Streaming](../0x01%20Application%20Layer/Web%20(WWW)/Video%20Streaming/Video%20Streaming.md) have arguably proven to be more than “good enough” to enable an amazing range of applications, including streaming video services such as Netflix and video-over-IP, real-time conferencing applications such as Skype and Facetime.

![](../../../../../Assets/Pics/Screenshot%202023-04-30%20at%2010.56.04%20AM.png)
<small>Network-layer service model</small>

> 💡 **The Network Service Model**
> 
> The network service model defines the characteristics of end-to-end delivery of packets between sending and receiving hosts.
> 
> Let’s now consider some possible services that the network layer could provide. These services could include:
> - **Guaranteed delivery**. This service guarantees that a packet sent by a source host will eventually arrive at the destination host.
> - **Guaranteed delivery with bounded delay**. This service not only guarantees delivery of the packet, but delivery within a specified host-to-host delay bound (for example, within 100 msec).
> - **In-order packet delivery**. This service guarantees that packets arrive at the desti- nation in the order that they were sent.
> - **Guaranteed minimal bandwidth**. This network-layer service emulates the behav- ior of a transmission link of a specified bit rate (for example, 1 Mbps) between sending and receiving hosts. As long as the sending host transmits bits (as part of packets) at a rate below the specified bit rate, then all packets are eventually delivered to the destination host.
> - **Security**. The network layer could encrypt all datagrams at the source and decrypt them at the destination, thereby providing confidentiality to all transport-layer segments.


### Functions & Service Model of IP Layer (Network Layer)
**Forwarding (data plane)** refers to the **router-local action** of transferring a packet from an input link interface of the router to the appropriate output link interface of the router. Forwarding takes place at very **short timescales** (typically a few nanoseconds), and thus is typically implemented in hardware. 

**Routing (control plane)** refers to the **network-wide process** that determines the end-to-end paths that packets take from source to destination. Routing takes place on much **longer timescales** (typically seconds), and as we will see is often implemented in software.

**Data Plane** 
- local, per-router function
- determines how datagram arriving on router input port is forwarded to router output port

**Control Plane**
- network-wide logic
- determines how datagram is routed among routers along end-end path from source host to destination host
- two control-plane approaches:
	- traditional routing algorithms: implemented in routers
	- software-defined networking (SDN): implemented in (remote) servers


![Screenshot 2022-11-26 at 3.35.43 PM](../../../../../Assets/Pics/Screenshot%202022-11-26%20at%203.35.43%20PM.png)


#### 2 Services Provided by Network Layer
![](../../../../../Assets/Pics/Screenshot%202023-04-30%20at%2010.33.29%20AM.png)

很多广域分组交换网都使用面向连接的虚电路服务。例如，曾经的x.25和逐渐过时的帧中继(Frame Relay, FR)，异步传输模式(Asynchronous Transfer Mode, ATM)。然而，因特网使用的是无连接的数据包模式。

![](../../../../../Assets/Pics/Screenshot%202023-04-30%20at%2010.37.40%20AM.png)


#### 2 Control-plane Approaches
![](../../../../../Assets/Pics/Screenshot%202023-04-30%20at%2010.54.04%20AM.png)
![](../../../../../Assets/Pics/Screenshot%202023-04-30%20at%2010.54.12%20AM.png)


### Connecting Heterogeneous Network 
![Screenshot 2022-11-26 at 3.40.20 PM](../../../../../Assets/Pics/Screenshot%202022-11-26%20at%203.40.20%20PM.png)
![](../../../../../Assets/Pics/Screenshot%202023-04-30%20at%2010.43.45%20AM.png)


## Data Plane
### Router
> 🏃‍♂ For more info, check out [Router](Router/Router.md) 


### 👾 IP(Internet Protocol)
> 🏃‍♂ For more info, check out ↗ [Internet Protocols](Data%20Plane/Internet%20Protocols/Internet%20Protocols.md)


### Mobile IP
> 🏃‍♂ For more info, check out ↗ [Mobile IP](Data%20Plane/Internet%20Protocols/Mobile%20IP.md)



## Control Plane
### 🛂 ICMP
↗ [ICMPv4](Control%20Plane/ICMP/ICMPv4.md)
↗ [ICMPv6](Control%20Plane/ICMP/ICMPv6.md)


### IP Multicasting
> 🏃‍♂ For more info, check out  ↗ [Multicasting](Control%20Plane/Multicasting/Multicasting.md).


### SDN
> 🏃‍♂ For more info, check out ↗ [SDN](../../🙌🏻%20SDN/SDN.md) 


🔗 【深入浅出计算机网络 - 4.10 软件定义网络SDN】 https://www.bilibili.com/video/BV19P411J77K/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d



## 🧪 Middleboxes
In the past 20 years, we’ve seen tremendous growth in such middleboxes, which [RFC 3234] defines as:

> "any intermediary box performing functions apart from normal, standard func- tions of an IP router on the data path between a source host and destination host"

We can broadly identify three types of services performed by middleboxes:
- **NAT Translation**. NAT boxes implement private network addressing, rewriting datagram header IP addresses and port numbers.

- **Security Services**. 
	- **Firewalls** block traffic based on header-field values or redirect packets for additional processing, such as **deep packet inspection (DPI)**.
	- **Intrusion Detection Systems (IDS)** are able to detect predetermined patterns and filter packets accordingly. 
	- Application-level e-mail **filters** block e-mails considered to be junk, phishing or otherwise posing a security threat.

- **Performance Enhancement**. These middleboxes perform services such as **compression**, **content caching**, and **load balancing** of service requests (e.g., an HTTP request, or a search engine query) to one of a set of servers that can provide the desired service.

Many other middleboxes [RFC 3234] provide capabilities belonging to these three types of services, in both wired and wireless cellular [Wang 2011] networks.


### Middleboxes: Past /Future
↗ [Network Virtualization](../../👰🏻‍♂️%20Network%20Virtualization/Network%20Virtualization.md)

↗ [NFV](../../👰🏻‍♂️%20Network%20Virtualization/NFV/NFV.md)
↗ [SDN](../../🙌🏻%20SDN/SDN.md)
↗ [Cloud Native](../../../../🌁%20Cloud%20Native/Cloud%20Native.md)


### Middleboxes: Pro /Against
For many years, the Internet architecture had a clear separation between the network layer and the transport/application layers. 

In these “good old days,” the network layer consisted of routers, operating within the network core, to forward datagrams toward their destinations using fields only in the IP datagram header. The transport and application layers were implemented in hosts operating at the network edge. Hosts exchanged packets among themselves in transport-layer segments and application-layer messages. 

Today’s middleboxes clearly violate this separation: a NAT box, sitting between a router and host, rewrites network-layer IP addresses and transport-layer port numbers; an in-network firewall blocks suspect datagrams using application-layer (e.g., HTTP), transport-layer, and network-layer header fields; e-mail security gateways are injected between the e-mail sender (whether malicious or not) and the intended e-mail receiver, filtering application-layer e-mail messages based on whitelisted/blacklisted IP addresses as well as e-mail message content. 

- While there are those who have considered such middleboxes as a bit of an archi- tectural abomination [Garfinkel 2003], 
- others have adopted the philosophy that such middleboxes “exist for important and permanent reasons”—that they fill an important need—and that we’ll have more, not fewer, middleboxes in the future [Walfish 2004]. 


### The IP Hourglass
![](../../../../../Assets/Pics/Screenshot%202023-04-30%20at%2011.28.24%20AM.png)

![](../../../../../Assets/Pics/Screenshot%202023-04-30%20at%2011.28.34%20AM.png)



### ⚧️ NAT /NAPT
🔗 【深入浅出计算机网络 - 4.6 虚拟专用网VPN和网络地址转换NAT】 https://www.bilibili.com/video/BV1mV4y1M7Xs/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d 

Network Address Translation ↗ [NAT](Data%20Plane/NAT/NAT.md)
NAPT, Network Address and Port Translation is at ↗ [NAPT](Data%20Plane/NAT/NAPT.md)


### 👻 VPN
🔗 【深入浅出计算机网络 - 4.6 虚拟专用网VPN和网络地址转换NAT】 https://www.bilibili.com/video/BV1mV4y1M7Xs/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

This notes can be seen on ↗ [Anonymous Networks /VPN](../../../../CyberSecurity/Network%20Security/Anonymous%20&%20Private%20Networks/VPN.md)


### ⛑️ Firewalls /IDS
↗ [Network Security /Intrusion Detection Systems (IDS)](../../../../CyberSecurity/Network%20Security/Network%20Attacks%20&%20Defends/Intrusion%20Detection%20Systems%20(IDS)/Intrusion%20Detection%20Systems%20(IDS).md)

↗ [Network Security /Firewall](../../../../CyberSecurity/Network%20Security/Networking%20Access%20Control/Authentication/Firewall/Firewall.md)



## 🤺 Arugements & Opinions
### Architectural Principles of the Internet


### The End-end Argument




## Ref
