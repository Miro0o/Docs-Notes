# ARP (Address Resolution Protocol) (LAN, IPv4)

[TOC]



## Res
🔗 【深入浅出计算机网络 - 4.2.5 地址解析协议ARP】 https://www.bilibili.com/video/BV1D24y1Z7Yj/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

↗ [Link-Layer Addressing](../../../0x06%20Link%20Layer/📌%20Link%20Layer%20(Switched%20Network)%20Basics/Link-Layer%20Addressing.md)



## Intro
> 🔗 https://www.techtarget.com/searchnetworking/definition/Address-Resolution-Protocol-ARP

> **ARP** was first proposed and discussed in Request for Comments (RFC) 826, published in November of 1982 by **David C. Plummer**. The problem of address resolution was immediately evident in the early days of the IP suite, because Ethernet quickly became the preferred LAN technology, but Ethernet cables required 48-bit addresses.

> 🤨 ==Is ARP link layer protocol or network layer protocol?==
> ↗ [Link-Layer Addressing](../../../0x06%20Link%20Layer/📌%20Link%20Layer%20(Switched%20Network)%20Basics/Link-Layer%20Addressing.md)


**Address Resolution Protocol (ARP)** is a procedure for mapping a dynamic IP address to a permanent physical machine address in a **local area network (LAN)**. The physical machine address is also known as a **media access control (MAC) address**.

The job of ARP is essentially to translate 32-bit addresses to 48-bit addresses and vice versa. This is necessary because IP addresses in IP version 4 (IPv4) are 32 bits, but MAC addresses are 48 bits.

ARP can also be used for **IP over other LAN technologies**, such as
- token ring;
- fiber distributed data interface ([FDDI](https://www.techtarget.com/searchnetworking/definition/FDDI));
- IP over ATM.

There are a couple of interesting things to note about the ARP protocol. 
- First, the query ARP message is sent within a **broadcast frame**, whereas the response ARP message is sent within a **standard frame**. Before reading on you should think about why this is so. 
- Second, ARP is **plug-and-play**; that is, an ARP table gets built automatically—it doesn’t have to be configured by a system administrator. And if a host becomes disconnected from the subnet, its entry is eventually deleted from the other ARP tables in the subnet.


### RARP (Reverse ARP)
> 🔗 https://www.techtarget.com/searchnetworking/definition/Reverse-Address-Resolution-Protocol)


### ARP + IPv4 🆚 IPv6
While IPv4 addresses are currently more common, the use of IPv6 is increasing. This increase is largely due to the influx of IoT devices that require IP addresses. 

IPv6 addresses, which are 128 bits, use the [Neighbor Discovery protocol](https://www.techtarget.com/searchnetworking/tip/How-to-avoid-IPv6-neighbor-discovery-threats) to acquire configuration information instead of ARP. 

Neighbor Discovery operates in the Layer 2 of the OSI model and uses Internet Control Message Protocol ([ICMP](https://www.techtarget.com/searchnetworking/definition/ICMP)) version 6 to discover neighboring nodes.



## How ARP works
When a new computer joins a LAN, it is assigned a unique IP address to use for identification and communication. 
When an incoming packet destined for a host machine on a particular LAN arrives at a gateway, the gateway 
1. asks the ARP program to find a MAC address that matches the IP address.
	1. A table called the **ARP cache** maintains a record of each IP address and its corresponding MAC address. ARP first check this cache for the requested mac address.
	2. If there's no mac address in ARP cache, ARP then **multicasts the neibouring nodes** for requested mac address.
		1. When mac address retrived successfully, it updates its arp cache table.

![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.22.02%20AM.png)


### ARP Datagram Retrieving 
🔗 【深入浅出计算机网络 微课视频】 https://www.bilibili.com/video/BV1NT411g7n6/?p=55&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.13.29%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.20.20%20AM.png)


### ARP Cache Table (ARP 高速缓存表)
All operating systems in an IPv4 Ethernet network keep an ARP cache. Every time a host requests a MAC address in order to send a packet to another host in the LAN, it checks its ARP cache to see if the IP to MAC address translation already exists. If it does, then a new ARP request is unnecessary. If the translation does not already exist, then the request for network addresses is sent and ARP is performed.

![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.21.35%20AM.png)



## Proxy ARP
Proxy ARP enables a network proxy to answer ARP queries for IP addresses that are outside the network. This enables packets to be successfully transferred from one subnetwork to another.

When an ARP inquiry packet is broadcast, the routing table is examined to find which device on the LAN can reach the destination fastest. This device, which is often a router, acts as a gateway for forwarding packets outside the network to their intended destinations.



## ARP Spoofing & ARP Cache Poisoning
> ↗ [Network Monitoring /ARP Spoofing](../../../../../../CyberSecurity/Network%20Security/Network%20Attacks%20&%20Defends/Network%20Monitoring.md)

LANs that use ARP are vulnerable to ARP spoofing, also called _ARP poison routing_ or _ARP cache poisoning_.

ARP spoofing is a device attack in which a hacker broadcasts false ARP messages over a LAN in order to link an attacker's MAC address with the IP address of a legitimate computer or server within the network. Once a link has been established, the target computer can send frames meant for the original destination to the hacker's computer first as well as any data meant for the legitimate IP address.

ARP spoofing can seriously affect enterprises. When used in their simplest form, ARP spoofing attacks can steal sensitive information. However, the attacks can also facilitate other malicious attacks, including the following:

- [man-in-the-middle attacks](https://internetofthingsagenda.techtarget.com/definition/man-in-the-middle-attack-MitM)
- [denial-of-service attacks](https://www.techtarget.com/searchsecurity/definition/denial-of-service)
- [session hijacking](https://www.techtarget.com/searchsoftwarequality/definition/session-hijacking)



## Ref
[Address Resolution Protocol | Wikipedia]: https://en.wikipedia.org/wiki/Address_Resolution_Protocol

[👍 浅谈ARP欺骗的实现与防御 | Freebuf]: https://www.freebuf.com/articles/network/210852.html

> - [SharpPcap官方文档](http://sharppcap.sourceforge.net/htmldocs/index.html)[PacketDotNet](https://github.com/chmorgan/packetnet)（使用PacketDotNet可以很方便的构造出数据包，只需几个参数）
> - [SharpPcapTool](https://gitee.com/week233/SharpPcapTool_back.git)（实现参考，没有做物理机的虚拟机网卡过滤，当遍历到虚拟机网卡的网关IP时会抛异常，因为VMware的虚拟机网卡没有网关地址）
> - [牢底坐穿工具箱](https://gitee.com/week233/ARPAttack.git)（我的实现，已经过滤掉了VMware的虚拟机网卡）



