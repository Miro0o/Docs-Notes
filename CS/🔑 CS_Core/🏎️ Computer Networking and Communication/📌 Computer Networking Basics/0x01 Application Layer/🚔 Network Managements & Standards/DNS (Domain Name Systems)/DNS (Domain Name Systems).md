# DNS (Domain Name Systems)

[TOC]



## Res
【深入浅出计算机网络 - 6.4 域名系统DNS】 https://www.bilibili.com/video/BV1fT411T7NQ/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

📂 [Communication Networks/DNS | wikibooks](https://en.wikibooks.org/wiki/Communication_Networks/DNS)

### Related Topics
↗ [Database System /Directory Services /DNS Servers](../../../../../🍕%20Database%20System/Directory%20Services/DNS%20Server%20(DNS%20Distributed%20Database)/DNS%20Server%20(DNS%20Distributed%20Database).md)
↗ [Pen-tensting /DNS Reconnaissance](../../../../../../CyberSecurity/🥇%20Best%20Practice/💉%20Pen-testing/Explore%20&%20Reconnaissance%20Phase/Active%20Recon/DNS%20&%20Domain%20Reconnaissance.md)
↗ [🌏 Global DNS Service Providers](../../../../../🍕%20Database%20System/Directory%20Services/DNS%20Server%20(DNS%20Distributed%20Database)/DNS%20Server%20Implementations/🌏%20Global%20DNS%20Service%20Providers.md)
↗ [Domain Name Providers](Domain%20Name%20Providers.md)



## Intro
### Why DNS Service?
Remembering IP addresses is difficult, as it contains all numbers. To remember IP addresses of more than one host becomes cumbersome. Therefore a **name** has been assigned to almost every IP address which makes it easier for humans to remember. **DNS provides mapping of IP address and Domain name.** 

> A **domain name** identifies the area or domain that an Internet resource resides in. 

### How often is this mapping needed?
Answer. Every time when a host needs to convert a domain name to the IP address, a DNS query is called.


### 🎯 DNS Services
#### Host name to IP address translation
The primary purpose of DNS is to provide translation of host name to IP address and vice versa. The backward facility (translating IP address to domain name) is known as Reverse DNS. 

#### Host aliasing
Host aliasing is referred to another name given to the same machine on the network. It is used because a hostname may have a complicated name instead of that a simple term may be used. E.g. relay.eastcost.rediff.com may have an alias name rediff.com

#### Mail server aliasing
It is highly desirable that an email address should contain simple letters, or should be something that can be easy to remember. E.g. richard@gmail.com can be remembered easily but if the original mail server address, say la4.mail1.google.com, were to be used it would be difficult to remember

#### Load distribution
A set of IP address is provided to one canonical name which prevents the load to be present only on one server. “When the request comes to the DNS server to resolve the domain name, it gives out one of the several canonical names in a rotated order. This redirects the request to one of the several servers in a server group. Once the BIND feature of DNS resolves the domain to one of the servers, subsequent requests from the same client are sent to the same server


### Global DNS Servers /Domani Name Providers
↗ [🌏 Global DNS Service Providers](../../../../../🍕%20Database%20System/Directory%20Services/DNS%20Server%20(DNS%20Distributed%20Database)/DNS%20Server%20Implementations/🌏%20Global%20DNS%20Service%20Providers.md)
↗ [Domain Name Providers](Domain%20Name%20Providers.md)



## 🎒 DNS Servers Architecture Design
↗ [DNS Server (DNS Distributed Database)](../../../../../🍕%20Database%20System/Directory%20Services/DNS%20Server%20(DNS%20Distributed%20Database)/DNS%20Server%20(DNS%20Distributed%20Database).md)



## 👨‍🏫 Domain Names Hierarchy
### Domain Name Space
![](../../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%2010.18.02%20AM.png)

> “A domain is simply a subtree of the domain name space. The domain name of a domain is the same as the domain name of the node at the very top of the domain.” 

Consider the figure below
![](../../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%205.47.50%20PM.png)

As you can see in the figure above that the “sjsu” domain is a part of the edu domain. In the similar fashion there can be many domains in the “sjsu” domain.

![](../../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%2010.18.57%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%2010.19.37%20AM.png)



## ⏳ DNS Working Flow
### 🦆 DNS Query Process
![](../../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%2010.20.54%20AM.png)


#### Iterated Queries
![](../../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%205.56.19%20PM.png)

#### Recursive Queries
![](../../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%205.56.34%20PM.png)


#### Exercise Problems
![](../../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%2010.22.39%20AM.png)


### 📣 DNS Dynamic Update / Notify
The update/notify mechanism is design under [RFC 2136](https://tools.ietf.org/html/rfc2136). Many companies and usually all ISP use DHCP (DHCP is covered in section 5.1 in more detail) to assign IP address to the hosts which are connected to them (server). For this DNS is needed to support dynamic addition and deletion of resource records (RR - Resource Records are covered in further sections). This mechanism is called DNS dynamic update.

The dynamic update facility allows authorized updaters to add or delete a RR from a zone where a name server is authoritative. With the help of NS record the authorized update message is sent to the primary node of that zone. If a name server receives any update message and if that name server is not a primary node of that zone then that message is forwarded upstream to its master server. If the server who receives it is also slave then it is again forwarded upstream. This process is called “update forwarding” and it continues till the update message is received to the primary node of that zone. 

The primary master name server holds a writable copy of zone data. The slave nodes are notified when an update is performed either directly or indirectly.



## Ref
盘点国内外优秀公共DNS - 王小叹的文章 - 知乎 https://zhuanlan.zhihu.com/p/53958870

