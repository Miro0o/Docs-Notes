# Host(IP) Enumeration

[TOC]



## Res
[Security Scanners | Linux Gazette](https://linuxgazette.net/issue57/sharma.html)



## Intro
Host enumeration is the process of gaining specific particulars regarding a defined host. It is not enough to know that a server or wireless access point is present; instead, we need to expand the attack surface by identifying open ports, the base operating system, services that are running, and supporting applications.

This is highly intrusive and, unless care is taken, the active reconnaissance will be detected and logged by the target organization.



## Live Host Discovery
The first step is to run network ping sweeps against a target address space and look for responses that indicate that a particular target is live and capable of responding. Historically, pinging is referred to as the use of **ICMP**; however, **TCP**, **UDP**, **ICMP**, and **ARP** traffic can also be used to identify live hosts.

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%204.59.49%20PM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%205.00.16%20PM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%205.00.36%20PM.png)


| Application | Description |
|---|---|
|alive6 and detect-new- ip6|This is for IPv6 host detection. detect-new-ip6 runs on a scripted basis and identifies new IPv6 devices when added.|
|Dnmap and nmap|nmap is the standard network enumeration tool. dnmap is a distributed client-server implementation of the nmap scanner. PBNJ stores nmap results in a database, and then conducts historical analyses to identify new hosts.|
|fping, hping2,<br><br>hping3, and nping|These are packet crafters that respond to targets in various ways to identify live hosts.|



## IPv6 Host Detection
Metasploit can also be utilized for IPv6 host discovery. The auxiliary/scanner/discovery/ipv6_multicast_ping module will discover all of the IPv6-enabled machines with the physical (MAC) address, as shown in the following screenshot:

THC IPv6 suite atk6-alive6 will discover alive addresses in the same segment, as shown in the following screenshot:

### 👉 alive6


### 👉 detect-new-ip6



## Packet Crafters
### 👉 fping


### 👉 hping2


### 👉 hping3


### 👉 nping



## Other Network Enumeration Tools
### 👉 nmap
↗ [Nmap](../../../../../🔑%20CS_Core/🥷🏼%20Operating%20System%20(Tech)/Linux%20(Derived%20From%20UNIX%20Family)/🪓%20Free%20Software/Network%20Management/Nmap%20Proj/Nmap.md)


### 👉 dnmap



## Ref