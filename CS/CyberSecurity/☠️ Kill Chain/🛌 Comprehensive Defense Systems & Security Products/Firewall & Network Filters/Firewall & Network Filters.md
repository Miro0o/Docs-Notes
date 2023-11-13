# Firewall & Network Filters

[TOC]



## Res
### Related Topics
↗ [WAF (Web Application Firewall)](WAF%20(Web%20Application%20Firewall)/WAF%20(Web%20Application%20Firewall).md)
↗ [Free Software /Firewall & Network Filters](../../../../../🔑%20CS_Core/🥷🏼%20Operating%20System%20(Tech)/Linux%20(Derived%20From%20UNIX%20Family)/🪓%20Free%20Software/Network%20Management/Firewall%20&%20Network%20Filters.md)

↗ [GFW (Great FireWall)](../../../Network%20Security/Anonymous%20&%20Private%20Networks/Proxy/GFW%20(Great%20FireWall).md)

### Learning Resources
【深入浅出计算机网络 - 7.8 防火墙访问控制与入侵检测系统】 https://www.bilibili.com/video/BV1Gr4y1u7oe/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

【网络干货】网络安全之最全防火墙技术详解 - 网络工程师笔记的文章 - 知乎 https://zhuanlan.zhihu.com/p/138100829



## Intro
### Firewall Overview
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%203.47.45%20PM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%203.48.31%20PM.png)



## Types of Firewalls
> 🔗 https://en.wikipedia.org/wiki/Firewall_(computing)

Firewalls are categorized as a network-based or a host-based system. 
1. Network-based firewalls are **positioned between two or more networks**, typically between the local area network (LAN) and wide area network (WAN). They are either a software appliance running on general-purpose hardware, a hardware appliance running on special-purpose hardware, or a virtual appliance running on a virtual host controlled by a hypervisor. Firewall appliances may also offer non-firewall functionality, such as [DHCP](https://en.wikipedia.org/wiki/DHCP "DHCP") or [VPN](https://en.wikipedia.org/wiki/VPN "VPN") services. 
2. Host-based firewalls are **deployed directly on the host** itself to control network traffic or other computing resources. This can be a [daemon](https://en.wikipedia.org/wiki/Daemon_(computing) "Daemon (computing)") or [service](https://en.wikipedia.org/wiki/Windows_service "Windows service") as a part of the [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system") or an [agent application](https://en.wikipedia.org/wiki/Endpoint_security "Endpoint security") for protection.

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.25.39%20PM.png)


### 🔌 Physical Layer
#### Packet Filter (1G)（分组过滤路由器）
> The first paper published on firewall technology was in 1987 when engineers from [Digital Equipment Corporation](https://en.wikipedia.org/wiki/Digital_Equipment_Corporation "Digital Equipment Corporation") (DEC) developed **filter systems** known as **packet filter firewalls**. At [AT&T Bell Labs](https://en.wikipedia.org/wiki/Bell_Labs "Bell Labs"), [Bill Cheswick](https://en.wikipedia.org/wiki/William_Cheswick "William Cheswick") and [Steve Bellovin](https://en.wikipedia.org/wiki/Steven_M._Bellovin "Steven M. Bellovin") continued their research in packet filtering and developed a working model for their own company based on their original first-generation architecture. In 1992, Steven McCanne and Van Jacobson released paper on [BSD Packet Filter](https://en.wikipedia.org/wiki/Berkeley_Packet_Filter "Berkeley Packet Filter") (BPF) while at [Lawrence Berkeley Laboratory](https://en.wikipedia.org/wiki/Lawrence_Berkeley_Laboratory "Lawrence Berkeley Laboratory")

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.24.18%20PM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.24.33%20PM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.24.47%20PM.png)


### 📲 Application Layer
#### Connection Tracking (Stateful Filter, 2G)
From 1989–1990, three colleagues from [AT&T Bell Laboratories](https://en.wikipedia.org/wiki/AT%26T_Bell_Laboratories "AT&T Bell Laboratories"), Dave Presotto, Janardan Sharma, and Kshitij Nigam, developed the second generation of firewalls, calling them [circuit-level gateways](https://en.wikipedia.org/wiki/Circuit-level_gateway "Circuit-level gateway").

Second-generation firewalls perform the work of their first-generation predecessors but also maintain knowledge of specific conversations between endpoints by remembering which port number the two [IP addresses](https://en.wikipedia.org/wiki/IP_address "IP address") are using at layer 4 ([transport layer](https://en.wikipedia.org/wiki/Transport_layer "Transport layer")) of the [OSI model](https://en.wikipedia.org/wiki/OSI_model "OSI model") for their conversation, allowing examination of the overall exchange between the nodes.

> However, this made data vulnerable to Denial of Service attacks, because the firewall could easily become overwhelmed by fake connection packets, filling its connection-state memory.
#### FWTK (3G)
To overcome DDoS, an application firewall known as **Firewall Toolkit (FWTK)** was introduced in June 1994 by Marcus Ranum, Wei Xu, and Peter Churchyard. 

> This became the basis for Gauntlet firewall at [Trusted Information Systems](https://en.wikipedia.org/wiki/Trusted_Information_Systems)

This third generation of firewalls could identify whether a communication protocol was being abused or attempted to bypass the firewall on an allowed port. This application-layer filtering allowed the firewall to “perceive” how File Transfer Protocols (FTP) or Hypertext Transfer Protocols (HTTP) work and adapt on the fly to the ways applications made use of these protocols.
#### Socket Filters (Endpoint Specific)
Endpoint-based application firewalls function by determining whether a process should accept any given connection. 
- Application firewalls filter connections by examining the process ID of data packets against a rule set for the local process involved in the data transmission. 
- Application firewalls accomplish their function by hooking into socket calls to filter the connections between the application layer and the lower layers. 
- Application firewalls that hook into socket calls are also referred to as **socket filters**
#### Proxy Server（应用网关）
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.24.58%20PM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.25.11%20PM.png)


### ⏭️ Next-generation Firewall (4G, Next G)
As of 2012, the [next-generation firewall](https://en.wikipedia.org/wiki/Next-generation_firewall "Next-generation firewall") provides a wider range of inspection at the application layer, extending [deep packet inspection](https://en.wikipedia.org/wiki/Deep_packet_inspection "Deep packet inspection") functionality to include, but is not limited to:
- [Web filtering](https://en.wikipedia.org/wiki/Web_filtering "Web filtering")
- [Intrusion prevention systems](https://en.wikipedia.org/wiki/Intrusion_prevention_system "Intrusion prevention system")
- [User identity management](https://en.wikipedia.org/wiki/Identity_management "Identity management")
- [Web application firewall](https://en.wikipedia.org/wiki/Web_application_firewall "Web application firewall")



## Firewall Drawbacks
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.26.19%20PM.png) 



## Ref
[The Evolution of Firewalls: Past, Present & Future]: https://www.informationweek.com/partner-perspectives/the-evolution-of-firewalls-past-present-and-future/a/d-id/1318814

[Firewall (Computing) | Wikipedia]: https://en.wikipedia.org/wiki/Firewall_(computing)

