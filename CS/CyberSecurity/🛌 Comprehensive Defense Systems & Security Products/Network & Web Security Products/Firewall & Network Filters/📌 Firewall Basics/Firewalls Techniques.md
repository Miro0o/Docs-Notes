# Firewalls Techniques

[TOC]



## Res
### Related Topics
↗ [Development (History) of Firewall](Development%20(History)%20of%20Firewall.md)



## Intro
![](../../../../../../Assets/Pics/Screenshot%202023-12-16%20at%2011.22.58AM.png)



## Current Firewall Techniques (2023)
### 1️⃣ Packet Filter (1G)（分组过滤/包过滤）
![](../../../../../../Assets/Pics/Screenshot%202023-12-16%20at%2011.16.04AM.png)

> The first paper published on firewall technology was in 1987 when engineers from [Digital Equipment Corporation](https://en.wikipedia.org/wiki/Digital_Equipment_Corporation "Digital Equipment Corporation") (DEC) developed **filter systems** known as **packet filter firewalls**. At [AT&T Bell Labs](https://en.wikipedia.org/wiki/Bell_Labs "Bell Labs"), [Bill Cheswick](https://en.wikipedia.org/wiki/William_Cheswick "William Cheswick") and [Steve Bellovin](https://en.wikipedia.org/wiki/Steven_M._Bellovin "Steven M. Bellovin") continued their research in packet filtering and developed a working model for their own company based on their original first-generation architecture. In 1992, Steven McCanne and Van Jacobson released paper on [BSD Packet Filter](https://en.wikipedia.org/wiki/Berkeley_Packet_Filter "Berkeley Packet Filter") (BPF) while at [Lawrence Berkeley Laboratory](https://en.wikipedia.org/wiki/Lawrence_Berkeley_Laboratory "Lawrence Berkeley Laboratory")

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.24.18%20PM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.24.33%20PM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.24.47%20PM.png)

包过滤技术检查数据包的报头信息，依照过滤规则进行过滤，其检查的典型报头信息内容如下：
- IP 数据报的源 IP 地址、目的 IP 地址、协议类型，选项字段等。
- TCP 数据包的源端口、目标端口、标志段等。
- UDP 数据包的源端口、目标端口。
- ICMP 类型。

包过滤特点
- 包过滤技术不需要内部网络用户做任何配置，对用户来说是完全透明的，过滤速度快，效率高。
- 不能进行数据内容级别的访问控制，一些应用协议也并不适合用数据报过滤，并且过滤规则的配置比较复杂，容易产生冲突和漏洞。
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
### 2️⃣ Stateful Inspection Firewall (状态检测防火墙)
![](../../../../../../Assets/Pics/Screenshot%202023-12-16%20at%2011.16.43AM.png)

从收到的数据包中提取状态信息，并根据状态表进行判断，如果该包属于已建立的连接状态，则跳过包过滤的规则检测直接交由内网主机，如果不是已建立的连接状态则对其进行包过滤，依照规则进行操作。如下图:
![](../../../../../../Assets/Pics/Screenshot%202023-12-16%20at%2011.16.58AM.png)

状态检测防火墙特点：
- 内置**TCP/IP**协议状态机，创建状态表用于维护连接上下文，检查每个会话连接的合法性（是否符合**TCP/IP**通信原理和特征）。
- 能够识别和监听常用动态端口应用的协商过程，从而自动为动态应用建立通过防火墙的安全连接。
- 不检查数据区
- 建立连接状态表
- 前后报文相关
- 应用层控制很弱
- 性能大大提高
- 支持大量应用
- 在内核级实现检测过滤
	- 在所有接口对进/出的数据包进行状态检查
- 支持应用层协议检查
	- 在动态状态表中存储连接状态
	- 检查对外的连接并预先计算出将返回的连接

在状态检测技术中，状态表是动态建立的，可以实现对一些复杂协议建立的临时端口进行有效的管理，状态检测技术为每一个会话连接建立状态信息，并对其维护，利用这些状态信息对数据包进行过滤。动态状态表是状态检测防火墙的核心，利用其可以实现比包过滤防火墙更强的控制访问能力。

状态检测技术的缺点是没有对数据包内容进行检测，不能进行数据内容级别的控制。由于允许外网主机与内网主机直接连接，增加了内网主机被外部攻击者直接攻击的风险。
o
![](../../../../../../Assets/Pics/Screenshot%202023-12-16%20at%2011.26.14AM.png)

![](../../../../../../Assets/Pics/Screenshot%202023-12-16%20at%2011.26.22AM.png)

### 2️⃣ Connection Tracking (Stateful Filter, 2G)
From 1989–1990, three colleagues from [AT&T Bell Laboratories](https://en.wikipedia.org/wiki/AT%26T_Bell_Laboratories "AT&T Bell Laboratories"), Dave Presotto, Janardan Sharma, and Kshitij Nigam, developed the second generation of firewalls, calling them [circuit-level gateways](https://en.wikipedia.org/wiki/Circuit-level_gateway "Circuit-level gateway").

Second-generation firewalls perform the work of their first-generation predecessors but also maintain knowledge of specific conversations between endpoints by remembering which port number the two [IP addresses](https://en.wikipedia.org/wiki/IP_address "IP address") are using at layer 4 ([transport layer](https://en.wikipedia.org/wiki/Transport_layer "Transport layer")) of the [OSI model](https://en.wikipedia.org/wiki/OSI_model "OSI model") for their conversation, allowing examination of the overall exchange between the nodes.

> However, this made data vulnerable to Denial of Service attacks, because the firewall could easily become overwhelmed by fake connection packets, filling its connection-state memory.
### 3️⃣ FWTK (3G)
To overcome DDoS, an application firewall known as **Firewall Toolkit (FWTK)** was introduced in June 1994 by Marcus Ranum, Wei Xu, and Peter Churchyard. 

> This became the basis for Gauntlet firewall at [Trusted Information Systems](https://en.wikipedia.org/wiki/Trusted_Information_Systems)

This third generation of firewalls could identify whether a communication protocol was being abused or attempted to bypass the firewall on an allowed port. This application-layer filtering allowed the firewall to “perceive” how File Transfer Protocols (FTP) or Hypertext Transfer Protocols (HTTP) work and adapt on the fly to the ways applications made use of these protocols.
### UTM (Unified Threat Management)
↗ [Fortinet](../../../../../🔑%20CS_Core/Electronic%20&%20Information%20Business%20Fields%20Research/Security%20Industry%20&%20Companies/Fortinet.md)

### Socket Filters (Endpoint Specific)
Endpoint-based application firewalls function by determining whether a process should accept any given connection. 
- Application firewalls filter connections by examining the process ID of data packets against a rule set for the local process involved in the data transmission. 
- Application firewalls accomplish their function by hooking into socket calls to filter the connections between the application layer and the lower layers. 
- Application firewalls that hook into socket calls are also referred to as **socket filters**
### Application Gateway of Proxy /Proxy Server（应用网关防火墙 /代理服务技术）
![](../../../../../../Assets/Pics/Screenshot%202023-12-16%20at%2011.17.30AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.24.58%20PM.png)

当接收到客户端发出的连接请求后，应用代理检查客户的源和目的 IP 地址，并依据事先设定的过滤规则决定是否允许该连接请求。如果允许该连接请求，进行客户身份识别。否则，则阻断该连接请求。通过身份识别后，应用代理建立该连接请求的连接，并根据过滤规则传递和过滤该连接之间的通信数据。当关闭连接后，应用代理关闭对应的另一方连接，并将这次的连接记录在日志内。如下是一个 Telnet 的例子：

![](../../../../../../Assets/Pics/Screenshot%202023-12-16%20at%2011.18.49AM.png)

应用网关防火墙特点：
- 在应用层检查数据包,能够对应用或内容进行过滤 - 如：禁止FTP的 “put”命令
- 不检查IP、TCP报头
- 不建立连接状态表
- 网络层保护比较弱

优点：
- 可以检查应用层、传输层和网络层的协议特征，对数据包的检测能力比较强
- 提供良好的安全性 **-** 所有数据的有效负载都在应用层进行检查
	- 能进行数据内容的检查，实现基于内容的过滤，对通信进行严密的监控。
- 内部网络的拓扑、IP 地址等被代理防火墙屏蔽，能有效实现内外网络的隔离。
- 具有强鉴别和细粒度日志能力，支持用户身份识别，实现用户级的安全。
缺点：
- 支持的应用数量有限，无法很好的支持新的应用、技术和协议
	- 需要为每一种应用服务编写代理软件模块，提供的服务数目有限
- 对用户不透明度
- 性能表现欠佳
	- 代理服务的额外处理请求降低了过滤性能，导致其过滤速度比包过滤器处理速度慢。
- 对操作系统的依赖程度高，容易因操作系统和应用软件的缺陷而受到攻击。

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.25.11%20PM.png)
### (完全内容检测防火墙)
![](../../../../../../Assets/Pics/Screenshot%202024-01-05%20at%2012.56.11PM.png)

- 网络层保护强
- 应用层保护强
- 会话保护很强
- 上下文相关
- 前后报文有联系



## ⏭️ Next-Generation Firewall (4G, Next G)
firewall + UTM = NGFW (next generation firewall )

As of 2012, the [next-generation firewall](https://en.wikipedia.org/wiki/Next-generation_firewall "Next-generation firewall") provides a wider range of inspection at the application layer, extending [deep packet inspection](https://en.wikipedia.org/wiki/Deep_packet_inspection "Deep packet inspection") functionality to include, but is not limited to:
- [Web filtering](https://en.wikipedia.org/wiki/Web_filtering "Web filtering")
- [Intrusion prevention systems](https://en.wikipedia.org/wiki/Intrusion_prevention_system "Intrusion prevention system")
- [User identity management](https://en.wikipedia.org/wiki/Identity_management "Identity management")
- [Web application firewall](https://en.wikipedia.org/wiki/Web_application_firewall "Web application firewall")



## Ref
[网络工程师必知：什么是下一代防火墙NGFW？ - 网络技术联盟站的文章 - 知乎]: https://zhuanlan.zhihu.com/p/460075728

