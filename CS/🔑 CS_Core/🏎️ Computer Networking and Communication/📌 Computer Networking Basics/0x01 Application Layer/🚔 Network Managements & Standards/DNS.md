# DNS (Protocol & Communication)

[TOC]



## Res
【深入浅出计算机网络 - 6.4 域名系统DNS】 https://www.bilibili.com/video/BV1fT411T7NQ/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

📂 [Communication Networks/DNS | wikibooks](https://en.wikibooks.org/wiki/Communication_Networks/DNS)


↗ [Database System /Directory Services /DNS](../../../../🍕%20Database%20System/Directory%20Services/DNS%20Server%20(DNS%20Distributed%20Database)/DNS%20Server%20(DNS%20Distributed%20Database).md)
↗ [Comprehensive Reconnaissance Applications /DNS](../../../../../CyberSecurity/☠️%20Kill%20Chain/🔦%20Reconnaissance/Comprehensive%20Reconnaissance%20Applications/Comprehensive%20Reconnaissance%20Applications.md)



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



## 🎒 DNS Servers Architecture Design
### Why Decentralized DNS Servers Architectures?
Problems that arise when we try to centralize DNS.
1. Single point of failure
2. Increase in traffic volume
3. Distant centralized database
4. Maintenance

As centralized DNS does not scale because of the reasons mentioned above, a need arose to implement DNS in a distributed manner . The DNS is a distributed system, implemented in a hierarchy of many name servers. The decentralized administration is achieved through delegation.


### Structure of DNS Servers
↗ [DNS Servers Architecture](../../../../🍕%20Database%20System/Directory%20Services/DNS%20Server%20(DNS%20Distributed%20Database)/DNS%20Servers%20Architecture.md)


### DNS Caching
![](../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%2010.21.47%20AM.png)

↗ [DNS Caching](../../../../🍕%20Database%20System/Directory%20Services/DNS%20Server%20(DNS%20Distributed%20Database)/DNS%20Caching.md)


### DNS Resource Records
↗ [DNS Resource Record (RR)](../../../../🍕%20Database%20System/Directory%20Services/DNS%20Server%20(DNS%20Distributed%20Database)/DNS%20Resource%20Record%20(RR).md)



## 👨‍🏫 Domain Names Hierarchy
### Domain Name Space
![](../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%2010.18.02%20AM.png)

> “A domain is simply a subtree of the domain name space. The domain name of a domain is the same as the domain name of the node at the very top of the domain.” 

Consider the figure below
![](../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%205.47.50%20PM.png)

As you can see in the figure above that the “sjsu” domain is a part of the edu domain. In the similar fashion there can be many domains in the “sjsu” domain.

![](../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%2010.18.57%20AM.png)

![](../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%2010.19.37%20AM.png)



## ⏳ DNS Working Flow
### 🦆 DNS Query Process
![](../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%2010.20.54%20AM.png)


#### Iterated Queries
![](../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%205.56.19%20PM.png)

#### Recursive Queries
![](../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%205.56.34%20PM.png)


#### Exercise Problems
![](../../../../../../Assets/Pics/Screenshot%202023-06-17%20at%2010.22.39%20AM.png)


### 📣 DNS Dynamic Update / Notify
The update/notify mechanism is design under [RFC 2136](https://tools.ietf.org/html/rfc2136). Many companies and usually all ISP use DHCP (DHCP is covered in section 5.1 in more detail) to assign IP address to the hosts which are connected to them (server). For this DNS is needed to support dynamic addition and deletion of resource records (RR - Resource Records are covered in further sections). This mechanism is called DNS dynamic update.

The dynamic update facility allows authorized updaters to add or delete a RR from a zone where a name server is authoritative. With the help of NS record the authorized update message is sent to the primary node of that zone. If a name server receives any update message and if that name server is not a primary node of that zone then that message is forwarded upstream to its master server. If the server who receives it is also slave then it is again forwarded upstream. This process is called “update forwarding” and it continues till the update message is received to the primary node of that zone. 

The primary master name server holds a writable copy of zone data. The slave nodes are notified when an update is performed either directly or indirectly.



## Ref
盘点国内外优秀公共DNS - 王小叹的文章 - 知乎 https://zhuanlan.zhihu.com/p/53958870


