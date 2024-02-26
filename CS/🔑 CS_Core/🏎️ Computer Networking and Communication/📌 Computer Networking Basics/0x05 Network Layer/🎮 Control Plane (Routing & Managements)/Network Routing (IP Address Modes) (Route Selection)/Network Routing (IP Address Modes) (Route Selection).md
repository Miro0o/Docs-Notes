# Network Routing (IP Address Modes) (Route Selection)

[TOC]



## Res



## Intro
### Addressing Methods Overview
There are four principal addressing methods in the [Internet Protocol](https://en.wikipedia.org/wiki/Internet_Protocol "Internet Protocol"):
- [Unicast](https://en.wikipedia.org/wiki/Unicast "Unicast") delivers a message to a single specific node using a **one-to-one** association between a sender and destination: each destination address uniquely identifies a single receiver endpoint.

- [Broadcast](https://en.wikipedia.org/wiki/Broadcasting_(networking) "Broadcasting (networking)") delivers a message to all nodes in the network using a **one-to-all** association; a single [datagram](https://en.wikipedia.org/wiki/Datagram "Datagram") (or [packet](https://en.wikipedia.org/wiki/Packet_(information_technology) "Packet (information technology)")) from one sender is routed to all of the possibly multiple endpoints associated with the [broadcast address](https://en.wikipedia.org/wiki/Broadcast_address "Broadcast address"). The network automatically replicates datagrams as needed to reach all the recipients within the scope of the broadcast, which is generally an entire network [subnet](https://en.wikipedia.org/wiki/Subnetwork "Subnetwork").

- [Multicast](https://en.wikipedia.org/wiki/Multicast "Multicast") delivers a message to a group of nodes that have expressed interest in receiving the message using a **one-to-many-of-many** or **many-to-many-of-many** association; datagrams are routed simultaneously in a single transmission to many recipients. Multicast differs from broadcast in that the destination address designates a subset, not necessarily all, of the accessible nodes.

- [Anycast](https://en.wikipedia.org/wiki/Anycast) delivers a message to any one out of a group of nodes, typically the one nearest to the source using a **one-to-one-of-many** association where datagrams are routed to any single member of a group of potential receivers that are all identified by the same destination address. The routing algorithm selects the single receiver from the group based on which is the nearest according to some distance or cost measure.



## IP Datagram Routing Configuration
### 👷🏻 Static Routing Configuration
🔗【深入浅出计算机网络 - 4.3 静态路由配置】 https://www.bilibili.com/video/BV1vB4y1n7pW/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

- 默认路由
- 特定主机路由


![Screenshot 2022-11-26 at 4.09.26 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-26%20at%204.09.26%20PM.png)

![Screenshot 2022-11-26 at 4.09.43 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-26%20at%204.09.43%20PM.png)



### 🕊️ Dynamic Routing Configuration

![Screenshot 2022-11-20 at 2.02.09 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-20%20at%202.02.09%20PM.png)



## Ref

