# Network Virtualization

[TOC]



## Res
↗ [Virtualization (Theory)](../../🧬%20Computer%20System/🚀%20Virtualization%20(Theory)/Virtualization%20(Theory).md)
↗ [Anonymous & Private Network /VPN](../../../CyberSecurity/Network%20Security/Anonymous%20&%20Private%20Networks/VPN/VPN.md)
↗ [Cloud Native /VPC](../../../System%20Architecture%20Design/☁️%20Cloud%20Native/🌵%20Cloud%20Overview/Cloud%20Platform%20Services%20(Cloud%20Applications)%20&%20Cloud%20Service%20Providers/VPC.md)



## Overview
![](../../../../Assets/Pics/Pasted%20image%2020230412170931.png)

### 1️⃣ Network Virtualization within Server Host
#### I/O Virtualization

#### Virtual Access


### 2️⃣ Network Virtualization in Network Access
#### Infiniband


#### FCOE


### 3️⃣ Network Virtualization in Network Exchange ==(Overlay Transport Protols)==
#### Overlays Networks Overview
Apart from the underlay network(IP network), **network overlays** are virtual networks of interconnected nodes that share an underlying physical network, allowing deployment of applications that require specific network topologies without the need to modify the underlying network.  

1️⃣ With the help of Network overlay, you can optimise the device functions and also reduces the complexity of the network devices.
- In the case of server-based overlays, this function is implemented on the server.
- In the case of network-based overlays, this function is implemented on the first switch (at the top of the rack). 

2️⃣ With the help of Ovelay networks you can achieve and provide **scalable Layer II networks** for a _multitenant cloud_ that extends beyond 4000 VLANs. This capability is very important for private and public cloud hosted environments.  

3️⃣ You can also maintain the fabric scalability and flexibility, because the overlay virtual network no longer needs to be constrained to a single physical location. The overlay encapsulation also allows the underlying infrastructure address space to be administered separately from the tenant address space.


#### OTV (Overlay Transport Virtualization)


#### LISP (Locator/Identifier Separation Protocol)


#### VxLAN (Virtual Extensible LAN)


#### NVGRE (Network Virtualization Using Generic Routing Encapsulation)
NVGRE allows the creation of virtual Layer 2 topologies on top of a physical Layer 3 network. With the help of NVGRE you can achieve by tunneling Ethernet frames inside an IP packet over a physical network. NVGRE supports a 24-bit segment ID or virtual subnet identifier (VSID) similar to VXLAN, providing up to 16 million virtual segments that can uniquely identify a given segment.

The difference between VXLAN and NVGRE is that NVGRE header includes an optional flow ID field. In multi-pathing deployments, network routers and switches that can parse this header can use this field together with the VSID to add flow-based entropy, although this feature requires additional hardware capabilities.


> **Note**: Microsoft is one of the major vendor who uses NVGRE concept and still a lot of vendors are doing their efforts to develop NVGRE like Cisco, VMware and Juniper.


#### STT (Stateless Transport Tunneling)
![](../../../../Assets/Pics/Screenshot%202023-04-16%20at%204.00.25%20PM.png)
<small> STT tunneling</small>


#### 🙌🏻 SDN
↗ [SDN](../🙌🏻%20SDN/SDN.md)



## NFV (Network Function Virtualization)
#TODO 




## Ref
[👍 虚拟化 - 网络虚拟化 | cnblogs]: https://www.cnblogs.com/sammyliu/articles/4390650.html

> 在网络虚拟化方面不仅很多大公司在抢占话语权，很多初创公司也在努力开拓机会，这里把我所知道的中小公司稍微做下总结，供大家参考：
> - Nicira：专注于OpenFlow的神秘公司。
> - [Big Switch](http://gigaom.com/cloud/bigswitch-nets-13-7m-to-become-vmware-of-networking/)：提供基于OpenFlow的网络虚拟化解决方案
> - Juniper Networks：支持OpenFlow
> - Open vSwitch: 一个开源的虚拟switch ，它是一个软件switch能运行在Hypervisor里, 目前已是[XenServer 6.0](http://support.citrix.com/article/CTX130418) 的缺省switch。
> - ConteXtream：借鉴Grid的思想，通过DHT（Distributed Hash Table）在传统的网络之上建立一个虚拟的抽象的网络，解决云主机服务提供商们在网络灵活性，多租户和扩展性方面的挑战。
> - Embrane： 提供一种on-demand的虚拟化网络服务，比如服务的负载均衡，防火墙，VPN。
> - Xsigo:  提供基于Infiniband技术的数据中心全虚拟化方案。
> - NextIO：提供基于PCIe技术 的I/O虚拟化产品。


[Comparison: VXLAN vs NVGRE vs STT vs LISP - Overlay Network Technologies]: https://www.routexp.com/2020/03/comparison-vxlan-vs-nvgre-vs-stt-vs.html

[SDN与网络虚拟化 | SDNLAB]: https://www.sdnlab.com/15475.html#:~:text=网络虚拟化是一种,实现弹性的网络%E3%80%82
> 网络虚拟化是一种重要的网络技术，该技术可在物理网络上虚拟多个相互隔离的虚拟网络，从而使得不同用户之间使用独立的网络资源切片，从而提高网络资源利用率，实现弹性的网络。SDN的出现使得网络虚拟化的实现更加灵活和高效，同时网络虚拟化也成为SDN应用中的重量级应用。
> 本文将介绍SDN与网络虚拟化的关系以及通过SDN实现网络虚拟化的方法，其中第二部分内容将从虚拟化平台，网络资源虚拟化和网络隔离三个方面介绍。

[理解（计算、网络，存储）虚拟化，只需一篇文章]: https://blog.csdn.net/weixin_57726902/article/details/124072149

华为云计算（3）——网络虚拟化 - IT小组的文章 - 知乎 https://zhuanlan.zhihu.com/p/332290846
![](../../../../Assets/Pics/Pasted%20image%2020230413110142.png)

