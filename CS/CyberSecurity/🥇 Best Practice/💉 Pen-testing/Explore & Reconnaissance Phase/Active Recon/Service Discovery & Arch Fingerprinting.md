# Service Discovery & Arch Fingerprinting

[TOC]



## Res
↗ [Service & Application Version Detection](../../../../☠️%20Kill%20Chain/🤔%20Pen-testing%20Tools/Reconnaissance%20&%20Exploration/Nmap%20Proj/⭐️%20Nmap%20Machanisms%20&%20Principles/Service%20&%20Application%20Version%20Detection/Service%20&%20Application%20Version%20Detection.md)
↗ [Remote OS Detection](../../../../☠️%20Kill%20Chain/🤔%20Pen-testing%20Tools/Reconnaissance%20&%20Exploration/Nmap%20Proj/⭐️%20Nmap%20Machanisms%20&%20Principles/Remote%20OS%20Detection/Remote%20OS%20Detection.md)

↗ xprobe2.



## Intro
The final goal of the enumeration portion of reconnaissance is to identify the services and applications that are operational on the target system. If possible, the attacker would want to know the **service type**, **vendor**, and **version to facilitate** the identification of any vulnerability.

The following are some of the several techniques used to determine active services:
- **Identify default ports and services**: If the remote system is identified as having a Microsoft operating system with port 80 open (the WWW service), an attacker may assume that a default installation of Microsoft IIS is installed. Additional testing will be used to verify this assumption (nmap). 
- **Banner grabbing**: This is done using tools such as amap, netcat, nmap, and Telnet.
- **Review default web pages**: Some applications install with default administration, error, or other pages. If attackers access these, they will provide guidance on installed applications that may be vulnerable to attack. In the following screenshot, the attacker can easily identify the version of Apache Tomcat that has been installed on the target system.
- **Review source code**: Poorly configured web-based applications may respond to certain HTTP requests such as HEAD or OPTIONS with a response that includes the web server software version, and, possibly, the base operating system or the scripting environment in use.



## Active Directory Domain Servers Discovery
Often during an internal penetration testing activity, penetration testers will be provided with a username and password. In real-world scenarios, the attackers are inside the network and an attack scenario would be what they could do with normal user access and how they elevate the privileges to compromise the enterprise domain.

### 👉 `rpcclient`



## Operating System Fingerprinting
Determining the operating system of a remote system is conducted using two types of scans: active fingerprinting & passive fingerprinting. 

Active fingerprinting is faster and more accurate than passive fingerprinting.

![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%205.02.31%20PM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-04-01%20at%205.02.47%20PM.png)


### Active Fingerprinting
Active fingerprinting: The attacker sends normal and malformed packets to the target and records its response pattern, referred to as the fingerprint. By comparing the fingerprint to a local database, the operating system can be determined.
 
#### 👉 nmap
↗ [Nmap](../../../../☠️%20Kill%20Chain/🤔%20Pen-testing%20Tools/Reconnaissance%20&%20Exploration/Nmap%20Proj/Nmap%20Tools/Nmap.md)


#### 👉 xprobe2


### Passive Fingerprinting
Passive fingerprinting: The attacker sniffs, or records and analyzes the packet stream to determine the characteristics of the packets


#### 👉 Wireshark(?)
↗ [Wireshark](../../../../../🔑%20CS_Core/🥷🏼%20Operating%20System%20(Tech)/Linux%20(Derived%20From%20UNIX%20Family)/🪓%20Free%20Software/Network%20Management/Wireshark/Wireshark.md)



## Web Services Discovery & Fingerprinting
### 👉 sslscan
🏠 https://github.com/rbsec/sslscan

sslscan version 2 has now been released. This includes a major rewrite of the backend scanning code, which means that it is no longer reliant on the version of OpenSSL for many checks. This means that it is possible to support legacy protocols (SSLv2 and SSLv3), as well as supporting TLSv1.3 - regardless of the version of OpenSSL that it has been compiled against. (2023/10)



## Disk Scan
### 👉 dirscan
🚧 https://github.com/j3ers3/Dirscan
目录扫描

🚧 https://github.com/orf/dirscan
Dirscan is a high-performance tool for quickly inspecting the contents of huge (possibly networked) disks. It provides a summary of every single directory on a given disk, complete with the number of files within, their total size, and the latest time a file was created, accessed or modified.

It's designed for disks that are too large to inspect with traditional tools, and it:
- Is many orders of magnitudes faster than tools like `du`, `find` or `tree`
- Can max out any disk you give it, assuming you have enough CPU resources to keep up.
- Produces a simple JSON or CSV output that can be analysed by the built in viewer or other tools
- Supports a customisable number of threads
- Streams results to the output file, keeping relatively constant memory usage with any sized disk.




## Ref

