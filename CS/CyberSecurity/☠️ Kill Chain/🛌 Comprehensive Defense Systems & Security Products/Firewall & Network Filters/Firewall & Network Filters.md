# Firewall & Network Filters

[TOC]



## Res
### Related Topics
↗ [Access Control](../../../🏰%20Cybersecurity%20Basics%20&%20InfoSec/Identity%20&%20Access%20Management%20(IAM)/Access%20Control/Access%20Control.md)

↗ [WAF (Web Application Firewall) (Web IPS)](../Intrusion%20Prevention%20Systems%20(IPS)/WAF%20(Web%20Application%20Firewall)%20(Web%20IPS)/WAF%20(Web%20Application%20Firewall)%20(Web%20IPS).md)
↗ [Free Software /Firewall & Network Filters](../../../../../🔑%20CS_Core/🥷🏼%20Operating%20System%20(Tech)/Linux%20(Derived%20From%20UNIX%20Family)/🪓%20Free%20Software/Network%20Management/Firewall%20&%20Network%20Filters.md)

↗ [GFW (Great FireWall)](../../../Network%20Security/Anonymous%20&%20Private%20Networks/Proxy/GFW%20(Great%20FireWall).md)
↗ [OpenWRT](../../../../Embedded%20&%20Internet%20of%20Things/🚟%20Embedded%20Computer%20Systems/Embedded%20Operating%20Systems/OpenWRT/OpenWRT.md)

### Learning Resources
【深入浅出计算机网络 - 7.8 防火墙访问控制与入侵检测系统】 https://www.bilibili.com/video/BV1Gr4y1u7oe/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

【网络干货】网络安全之最全防火墙技术详解 - 网络工程师笔记的文章 - 知乎 https://zhuanlan.zhihu.com/p/138100829



## Intro
### Firewall Overview
防火墙（**FireWall**）定义：一种高级访问控制设备，置于不同网络安全域之间，它通过相关的安全策略来控制（允许、拒绝、监视、记录）进出网络的访问行为。
- 在网络间（内部/外部网络、不同信息级别）提供安全连接的设备；用于实现和执行网络之间通信的安全策略

为什么需要防火墙?
- 阻止来自不可信网络的攻击
- 保护关键数据的完整性
- 维护客户对企业或机构的信任

防火墙做什么？过滤
1. 实现一个组织的安全策略
2. 创建阻塞点
3. 记录internet活动记录
4. 限制网络暴露

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%203.47.45%20PM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%203.48.31%20PM.png)
<small>*这里的访问控制只是指对双方的通信过程进行控制</small>

胖/瘦防火墙


### Development of Firewalls
↗ [Development (History) of Firewall](Development%20(History)%20of%20Firewall.md)


### Firewalls Standards
**GB/T 18019-1999** 信息技术包过滤防火墙安全技术要求
**GB/T 18020-1999** 信息技术应用级防火墙安全技术要求
**GB/T 18336-2001** 信息技术安全性评估准则
**GB/T 17900-1999** 网络代理服务器的安全技术要求
**GB/T 18018-1999** 路由器安全技术要求

这些标准从安全环境、安全目标、安全要求、基本原理等方面对防火墙的各种指标进行了规定。



## Types of Firewalls /Firewalls' Filtering Technology
> 🔗 https://en.wikipedia.org/wiki/Firewall_(computing)

Firewalls are categorized as a network-based or a host-based system. 
1. **Network-based firewalls** are **positioned between two or more networks**, typically between the local area network (LAN) and wide area network (WAN). They are either a software appliance running on general-purpose hardware, a hardware appliance running on special-purpose hardware, or a virtual appliance running on a virtual host controlled by a hypervisor. Firewall appliances may also offer non-firewall functionality, such as [DHCP](https://en.wikipedia.org/wiki/DHCP "DHCP") or [VPN](https://en.wikipedia.org/wiki/VPN "VPN") services. 
2. **Host-based firewalls** are **deployed directly on the host** itself to control network traffic or other computing resources. This can be a [daemon](https://en.wikipedia.org/wiki/Daemon_(computing) "Daemon (computing)") or [service](https://en.wikipedia.org/wiki/Windows_service "Windows service") as a part of the [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system") or an [agent application](https://en.wikipedia.org/wiki/Endpoint_security "Endpoint security") for protection.

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.25.39%20PM.png)

防火墙从实现方式上来分，可分为硬件防火墙和软件防火墙两类。
- 硬件防火墙通常部署在内、外部网络之间，通过软、硬件结合的方式来达到隔离内、外部网络的目的；
- 软件防火墙可以在一个独立的机器上运行，通过一定的规则来达到限制非法用户访问的目的。

从技术发展阶段来分看，防火墙可分为包过滤、应用代理和状态检测等几大类型。

防火墙的检测与过滤技术
- 包过滤（**Packet Filtering**）：工作在网络层（**ip**层），仅根据数据包头中的**IP**地址、端口号、协议类型等标志确定是否允许数据包通过。
- 应用代理（**Application Proxy**）：工作在应用层，通过编写不同的应用代理程序，实现对应用层数据的检测和分析。
- 状态检测（**Stateful Inspection**）：工作在**2~4**层，访问控制方式与**1**同，但处理的对象不是单个数据包，而是整个连接，通过规则表和连接状态表，综合判断是否允许数据包通过。
- 完全内容检测（**Compelete Content Inspection**）：工作在**2~7**层，不仅分析数据包头信息、状态信息，而且对应用层协议进行还原和内容分析，有效防范混合型安全威胁


### 🔌 Physical Layer (Frame)
#### 1️⃣ Packet Filter (1G)（分组过滤路由器）
> The first paper published on firewall technology was in 1987 when engineers from [Digital Equipment Corporation](https://en.wikipedia.org/wiki/Digital_Equipment_Corporation "Digital Equipment Corporation") (DEC) developed **filter systems** known as **packet filter firewalls**. At [AT&T Bell Labs](https://en.wikipedia.org/wiki/Bell_Labs "Bell Labs"), [Bill Cheswick](https://en.wikipedia.org/wiki/William_Cheswick "William Cheswick") and [Steve Bellovin](https://en.wikipedia.org/wiki/Steven_M._Bellovin "Steven M. Bellovin") continued their research in packet filtering and developed a working model for their own company based on their original first-generation architecture. In 1992, Steven McCanne and Van Jacobson released paper on [BSD Packet Filter](https://en.wikipedia.org/wiki/Berkeley_Packet_Filter "Berkeley Packet Filter") (BPF) while at [Lawrence Berkeley Laboratory](https://en.wikipedia.org/wiki/Lawrence_Berkeley_Laboratory "Lawrence Berkeley Laboratory")

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.24.18%20PM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.24.33%20PM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.24.47%20PM.png)

- 在网络层检查数据包, 简单包过滤防火墙不检查数据区,
- 前后报文无关
- 简单的拒绝或接受策略模型, 简单包过滤防火墙不建立连接状态表
- 无法识别更高层协议（传输层可以）

优点: 
- 只对数据包的 **IP** 地址、 **TCP/UDP** 协议和端口进行分析，规则简单，处理速度较快
- 易于配置
- 对用户透明用户访问时不需要提供额外的密码或使用特殊的命令
缺点：
- 检查和过滤器只在网络层 - 不能识别应用层协议或维持连接状态
- 安全性薄弱 - 不能防止IP欺骗等
- 静态策略可能成为漏洞

### IP/Network Layer (Packet)

### Transmission Layer (Segment)
#### Stateful Inspection Firewall (状态检测防火墙)


### 📲 Application Layer (Data)
#### 2️⃣ Connection Tracking (Stateful Filter, 2G)
From 1989–1990, three colleagues from [AT&T Bell Laboratories](https://en.wikipedia.org/wiki/AT%26T_Bell_Laboratories "AT&T Bell Laboratories"), Dave Presotto, Janardan Sharma, and Kshitij Nigam, developed the second generation of firewalls, calling them [circuit-level gateways](https://en.wikipedia.org/wiki/Circuit-level_gateway "Circuit-level gateway").

Second-generation firewalls perform the work of their first-generation predecessors but also maintain knowledge of specific conversations between endpoints by remembering which port number the two [IP addresses](https://en.wikipedia.org/wiki/IP_address "IP address") are using at layer 4 ([transport layer](https://en.wikipedia.org/wiki/Transport_layer "Transport layer")) of the [OSI model](https://en.wikipedia.org/wiki/OSI_model "OSI model") for their conversation, allowing examination of the overall exchange between the nodes.

> However, this made data vulnerable to Denial of Service attacks, because the firewall could easily become overwhelmed by fake connection packets, filling its connection-state memory.
#### 3️⃣ FWTK (3G)
To overcome DDoS, an application firewall known as **Firewall Toolkit (FWTK)** was introduced in June 1994 by Marcus Ranum, Wei Xu, and Peter Churchyard. 

> This became the basis for Gauntlet firewall at [Trusted Information Systems](https://en.wikipedia.org/wiki/Trusted_Information_Systems)

This third generation of firewalls could identify whether a communication protocol was being abused or attempted to bypass the firewall on an allowed port. This application-layer filtering allowed the firewall to “perceive” how File Transfer Protocols (FTP) or Hypertext Transfer Protocols (HTTP) work and adapt on the fly to the ways applications made use of these protocols.
#### Socket Filters (Endpoint Specific)
Endpoint-based application firewalls function by determining whether a process should accept any given connection. 
- Application firewalls filter connections by examining the process ID of data packets against a rule set for the local process involved in the data transmission. 
- Application firewalls accomplish their function by hooking into socket calls to filter the connections between the application layer and the lower layers. 
- Application firewalls that hook into socket calls are also referred to as **socket filters**
#### Application Gateway of Proxy /Proxy Server（应用网关）
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.24.58%20PM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.25.11%20PM.png)

- 在应用层检查数据包,能够对应用或内容进行过滤 - 如：禁止FTP的 “put”命令
- 不检查IP、TCP报头
- 不建立连接状态表
- 网络层保护比较弱

优点：
- 可以检查应用层、传输层和网络层的协议特征，对数据包的检测能力比较强
- 提供良好的安全性 **-** 所有数据的有效负载都在应用层进行检查
缺点：
- 支持的应用数量有限，无法很好的支持新的应用、技术和协议
- 对用户不透明度
- 性能表现欠佳

### ⏭️ Next-generation Firewall (4G, Next G)
As of 2012, the [next-generation firewall](https://en.wikipedia.org/wiki/Next-generation_firewall "Next-generation firewall") provides a wider range of inspection at the application layer, extending [deep packet inspection](https://en.wikipedia.org/wiki/Deep_packet_inspection "Deep packet inspection") functionality to include, but is not limited to:
- [Web filtering](https://en.wikipedia.org/wiki/Web_filtering "Web filtering")
- [Intrusion prevention systems](https://en.wikipedia.org/wiki/Intrusion_prevention_system "Intrusion prevention system")
- [User identity management](https://en.wikipedia.org/wiki/Identity_management "Identity management")
- [Web application firewall](https://en.wikipedia.org/wiki/Web_application_firewall "Web application firewall")


### Stateful Inspection Firewalls

### Hybrid firewalls
### Proxy server firewalls

### Application level (gateway) firewalls



## Firewalls Architecture Implementation
There are many factors that come into consideration for architecting a firewall. The major ones are: 
1. Organization‘s ability to implement and develop the architecture
2. The budget allotted by the organization
3. Objectives of the network


### 1️⃣ Packet Filtering Router Firewalls (过滤路由器结构)
> 过滤路由器作为内外网连接的唯一通道，通过**ACL**策略要求所有的报文都必须在此通过检查，实现报文过滤功能。

![](../../../../../Assets/Pics/Pasted%20image%2020231117122317.png)

Most of organizations have a router as the interface to the Internet. This router is placed at the perimeter between the organization‘s internal networks and the internet service provider. These routers can be configured to accept or reject the packets as per the rule of the organization. This is one of the simple and effective ways to lower down the organization‘s risk from the internet.

**Drawbacks**:
- The length and the complexity of the rule sets implemented to filter the packets can grow and degrade network performance. (路由器规则表的长度随着使用时长不断增加，导致性能不断降低) 
- Also, it suffers from a lack of auditing and strong authentication mechanisms. (一旦被攻陷后很难发现，而且没有身份鉴别/ 没有日志记录)


### 2️⃣ Multi-Homed Host Firewalls (多宿主主机结构)
> 多宿主主机具有两个网络适配器的主机系统，采用主机替代路由器执行安全控制功能，性能更高，隔离性更好。

#### Dual-Homed Host Firewalls (双宿主主机/堡垒机（**Dual Homed Gateway**）结构)
![](../../../../../Assets/Pics/Pasted%20image%2020231117122328.png)

This architecture is a more complex implementation of screened host firewalls. In this architectural approach, the bastion host accommodates two NICs (Network Interface Cards) in the bastion host configuration. One of the NIC is connected to the external network, and the other one is connected to the internal network thus providing an additional layer of protection. 

This architecture often makes use of Network Address Translation (NATs). NAT is a method of mapping external IP addresses to internal IP addresses, thus forming a barrier to intrusion from external attackers.

- 双宿主主机优于过滤路由器的地方是：堡垒主机的系统软件可用于维护系统日志。
- 它的致命弱点是：一旦入侵者侵入堡垒主机，则无法保证内部网络的安全


### 3️⃣ Screened Host Firewalls (被屏蔽主机结构)
> 有两道屏障，一是屏蔽路由器，另外一个是堡垒主机（双宿主主机）屏蔽路由器位于网络的最边缘，负责与外网实施连接，并且参与外网的路由堡垒主机存放在内部网络中，是内部网络中唯一可以连接到外部网络的主机
> 通常在路由器上设立ACL过滤规则，并通过堡垒主机进行数据转发，来确保内部网络的安全。

![](../../../../../Assets/Pics/Screenshot%202023-11-17%20at%2012.29.00PM.png)

This firewall combines a packet-filtering router with a discrete firewall such as an application proxy server. In this approach, the router screens the packet before entering the internal network and minimizes the traffic and network load on the internal proxy. The application proxy inspects application layer protocol such as HTTP or HTTPS and performs the proxy services. This separate host is called a bastion host and can be a rich target for external attacks, thus it should be thoroughly secured.

The bastion host stores copies of the internal documents, making it a promising target to the attackers. A bastion host is also commonly referred to as the Sacrificial Host.

**Advantage**
This configuration requires the attacker to hack and compromise two separate systems, before accessing the internal data. In this way, the bastion host and router protects the data and is more effective and secure implementation.

弱点：如果攻击者进入屏蔽主机内，内网中的就会受到很大威胁；这与双宿主主机受攻击时的情形差不多。


### 4️⃣ Screened Subnet Firewalls (with DMZ) (被屏蔽子网结构）
![](../../../../../Assets/Pics/Pasted%20image%2020231117122339.png)

![](../../../../../Assets/Pics/Screenshot%202023-11-17%20at%2012.29.22PM.png)


多宿主主机体系结构和被屏蔽主机体系结构中，堡垒主机都是最主要的安全缺陷。一旦堡垒主机被入侵，则整个内部网络部处于入侵者的威胁之中。为解决这种安全隐患，被屏蔽子网体系结构被提出。
- 这种结构是在内部网络和外部网络之间建立一个被隔离的子网，用两台过滤路由器分别与内部网络和外部网络连接，中间通过堡垒主机进行数据转发。
- 特点：如果攻击者试图进入内网或者子网，他必须攻破过滤路由器和双宿主主机 ，然后才可以进入子网主机，整个过程中将引发警报机制。

Of all the architecture available, Screened Subnet Firewall is widely used and implemented in corporate networks. Screened Subnet Firewalls as the name suggests make use of DMZ and are a combination of dual-homed gateways and screened host firewalls. 

In a screened subnet firewall setup, the network architecture has three components and the setup is as follows: 
- 1st component: This component acts as a public interface and connects to the Internet.
- 2nd component: This component is a middle zone called a demilitarized zone. It acts as a buffer between 1st and 3rd components.
- 3rd component: The system in this component connects to an intranet or other local architecture.

(1) 周边网络（DMZ区）用边网络是位于非安全、不可信的外部网络与安全、可信的内部网络之间的一个附加网络。周边网络与外部网络、内部网络之间都是通过屏蔽路由器实现逻辑隔离的，因此外部用户必须穿越两道屏蔽路由器才能访问内部网络。
(2) 外部路由器的主要作用在于保护周边网络和内部网络，是被屏蔽子网体系结构的第一道屏障。在其上设置了对周边网络和内部网络进行访问的过滤规则，对外部用户访问周边网络和内部。
(3) 内部路由器用于隔离周边网络和内部网络，是被屏蔽子网体系结构的第二道屏障。在其上设置了针对内部用户的访问过滤规划，对内部用户访问周边网络和外部网络进行限制。
(4) 在被屏蔽子网结构中，堡垒主机位于周边网络，可以为外部用户提供www、FTP等服务，接受来自外部网络用户的服务资源访问请求。同时堡垒主机也可以向内部网络用户提供DNS 、电子邮件、www代理、FTP代理等多种服务，提供内部网络用户访问外部资源的接口。

**Advantage** 
The use of an additional "layer" and other aspects of the screened subnet firewall makes it a viable choice for many high-traffic or high-speed traffic sites. Screened subnet firewall also helps with throughput and flexibility.



## Firewalls Services
防火墙需具备五个基本功能/服务：
- 过滤进、出网络的数据；
- 管理进、出网络的访问行为；
- 封堵某些禁止的业务；
- 记录通过防火墙的信息内容和活动；
- 对网络攻击的检测和告警

防火墙的其它功能/服务：
- 控制进出网络的信息流向和数据包，过滤不安全的服务；
	- 数据库长连接应用支持
	- 路由支持
	- **ADSL**拨号功能
	- **SNMP**网管支持
- 隐藏内部**IP**地址及网络结构的细节；
	- 动态**IP**环境支持
- 提供使用和流量的日志和审计功能；
- 部署**NAT**（**Network Address Translation**，网络地址转换）；
- 逻辑隔离内部网段，对外提供**WEB**和**FTP**；
- 实现集中的安全管理；
- 提供**VPN**功能。
	- **IPSEC VPN**
	- **PPTP/L2TP**
- 高可用性
**IPSEC VPN**功能

### NAT

### MAP

### Basic Access Control

### Authentication 

### IP-MAC Binding

### DHCP Support

### Log Audit

### High-Availability

### VPN
#### IPSEC VPN
#### L2TP/PPTP VPN



## Firewall Performance Metrix



## Firewall Operation Modes
### Routing Mode
![|400](../../../../../Assets/Pics/Pasted%20image%2020231117125716.png)

在路由模式中，防火墙的各个安全区域位于不同的网段且防火墙自身有 IP 地址。子网之间的相互访问控制被隔离。


### Transient Mode
![|400](../../../../../Assets/Pics/Pasted%20image%2020231117125755.png)

透明模式即网桥模式，只区分内部网络和外部网络。不需要对防火墙进行 IP 设置，内网用户意识不到防火墙的存在，隐蔽性较好。降低了用户管理的复杂性。


### Hybrid Mode
![|400](../../../../../Assets/Pics/Pasted%20image%2020231117125734.png)

混合模式顾名思义混合了路由模式和透明模式，这种防火墙在实际生活中应用比较广泛，在混合模式中，内网和服务器区域是透明模式，与外网间则是路由模式。



## Firewall Use Cases



## Other Topics
### Firewall Drawbacks
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.26.19%20PM.png)

- 防火墙防外不防内；
	- 首先防火墙不能防范未经过防火墙或绕过防火墙的攻击。例如，如果允许从受保护的网络内部向外拨号，一些用户就可能形成与**Internet**的直接连接。
	- 防火墙很难防范来自于网络内部的攻击或滥用
- 防火墙难于管理和配置，易造成安全漏洞；
- 很难为用户在防火墙内外提供一致的安全策略；
- 防火墙只实现了粗粒度的访问控制；
- 对于某些攻击防火墙也无能为力。
	- 防火墙基于数据包包头信息的检测阻断方式，主要对主机提供或请求的服务进行访问控制，无法阻断通过开放端口流入的有害流量，并不是对蠕虫或者黑客攻击的解决方案。


### Firewall Design Choices
#### 防火墙的“胖”与“瘦”
#### 防火墙的硬件架构之争
在硬件技术中主要包括通用 CPU 架构、ASIC 架构、网络处理器架构。

通用 CPU 架构又被称为 x86 架构，采用通用 CPU 和 PCI 总线接口，可编程性高，更灵活、更易扩展。产品功能主要由软件实现，代表产品包含了大部分的开源/商业软件防火墙（基于*nix 系统）。

ASIC 架构（Application Specific Integrated Circuit），专用集成电路，一种带有逻辑处理的加速处理器，把一些原先由 CPU 完成的经常性和重复工作交给 ASIC 芯片来负责完成，如交换机、路由器、智能 IC 卡，通常配合通用 CPU 单元来完成复杂运算。代表产品为大部分国外的商业硬件防火墙。

NP 架构（Network Processor），网络处理器，通用 CPU 架构和 ASIC 架构的折衷，开发难度较低，性能较好，具有灵活性/可扩展性。代表产品是大部分国内的商业硬件防火墙。

下图为三种硬件架构的横向比较：

|架构类型|X86|NP|ASIC|
|---|---|---|---|
|灵活性|★★★|★★|★|
|扩展性|★★★|★★|★|
|性能|★|★★|★★★|
|安全性|★|★★|★★★|
|价格|低|中等|较高|


## Ref
[The Evolution of Firewalls: Past, Present & Future]: https://www.informationweek.com/partner-perspectives/the-evolution-of-firewalls-past-present-and-future/a/d-id/1318814

[Firewall (Computing) | Wikipedia]: https://en.wikipedia.org/wiki/Firewall_(computing)

[👍 Firewall types and architecture]: https://resources.infosecinstitute.com/topics/network-security-101/firewall-types-and-architecture/

[7 Different Types of Firewalls]: https://securitywing.com/types-of-firewall/

[Firewall Architecture]: https://www.educba.com/firewall-architecture/

[👍 第八章 防火墙 | 中传信安Wiki]: https://c4pr1c3.github.io/cuc-ns/chap0x08/main.html
