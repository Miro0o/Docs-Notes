# Service Discovery

[TOC]



## Res


## Intro
The final goal of the enumeration portion of reconnaissance is to identify the services and applications that are operational on the target system. If possible, the attacker would want to know the **service type**, **vendor**, and **version to facilitate** the identification of any vulnerability.

The following are some of the several techniques used to determine active services:
- **Identify default ports and services**: If the remote system is identified as having a Microsoft operating system with port 80 open (the WWW service), an attacker may assume that a default installation of Microsoft IIS is installed. Additional testing will be used to verify this assumption (nmap). 
- **Banner grabbing**: This is done using tools such as amap, netcat, nmap, and Telnet.
- **Review default web pages**: Some applications install with default administration, error, or other pages. If attackers access these, they will provide guidance on installed applications that may be vulnerable to attack. In the following screenshot, the attacker can easily identify the version of Apache Tomcat that has been installed on the target system.
- **Review source code**: Poorly configured web-based applications may respond to certain HTTP requests such as HEAD or OPTIONS with a response that includes the web server software version, and, possibly, the base operating system or the scripting environment in use.



## Active Directory Domain Servers
Often during an internal penetration testing activity, penetration testers will be provided with a username and password. In real-world scenarios, the attackers are inside the network and an attack scenario would be what they could do with normal user access and how they elevate the privileges to compromise the enterprise domain.

### 👉 `rpcclient`



## Ref

