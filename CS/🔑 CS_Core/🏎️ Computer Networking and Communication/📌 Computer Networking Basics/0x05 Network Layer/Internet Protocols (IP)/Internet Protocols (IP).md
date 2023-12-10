# Internet Protocols (IP)

[TOC]



## Res
### Related Topics
[IPSec (Internet Protocol Security) & IPSec VPN](../../../../../CyberSecurity/Network%20Security/🏇%20Network%20Security%20Basics%20&%20Protocols/🫱🏻‍🫲🏿%20Network%20Layer%20Security/IPSec%20(Internet%20Protocol%20Security)%20&%20IPSec%20VPN/IPSec%20(Internet%20Protocol%20Security)%20&%20IPSec%20VPN.md)



## IP Overview



## IP Datagram Format
↗ [IPv4 Datagram Header Format](IPv4/IPv4%20Datagram%20Header%20Format.md)
↗ [IPv6 Datagram Header Format](IPv6/IPv6%20Datagram%20Header%20Format.md)

### IPv4 Header 🆚 IPv6 Header
![](../../../../../../../Assets/Pics/technologies_white_paper0900aecd8054d37d-03.jpg)
<small>IPv4 vs IPv6</small>


![IPv6 features](../../../../../../../Assets/Pics/image44.png)
<small>IPv4 vs IPv6</small>



## IP Address & IP Addressing
![](../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.08.49%20AM.png)

![Screenshot 2022-11-20 at 1.00.50 PM](../../../../../../../../Assets/Pics/Screenshot%202022-11-20%20at%201.00.50%20PM.png)


### 🎰 Limited IP Address & Addressing

> - For Mac Addressing, 🙈 check out  ↗ [Link-Layer Addressing (MAC Addressing)](../../0x06%20Data%20Link%20Layer/📌%20Link%20Layer%20(Switched%20Network)%20Basics/Link-Layer%20Addressing%20(MAC%20Addressing).md)

> ⚠ As for Mac addressing, it can be categorized both as Network Layer or Link Layer. Here it falls on Network Layer.

The number of IPv4 address is very limited. To tackle this problem tons of efforts have been made:
↗ [IPv4 Address Coding & Network Number Assigning](IPv4/IPv4%20Address%20Coding%20&%20Network%20Number%20Assigning.md)
↗ [NAT (Network Address Translation)](../MiddleBoxes/NAT%20(Network%20Address%20Translation)/NAT%20(Network%20Address%20Translation).md)
↗ [IPv6](IPv6/IPv6.md)

Among all of this solusion, IPv6 is deemed to be the ultimate method dealing with "limited number of address" --- because it's unlimited!


### IP Address Assignment
#### 👐🏼 IP address: how to get one? (user)
##### Hard-coded (Static)

##### DHCP (Dynamic)
↗ [DHCP](../../0x01%20Application%20Layer/🚔%20Network%20Managements%20&%20Standards/DHCP.md)


#### 👐🏼 IP address: how to get blocks? (ISP)
##### ICANN
ICANN: Internet Corporation for Assigned  Names and Numbers http://www.icann.org/
- allocates IP addresses, through 5 **regional registries (RRs)** (who may then allocate to local registries)
- manages DNS root zone, including delegation of individual TLD (.com, .edu , …) management

##### NAT
↗ [NAT (Network Address Translation)](../MiddleBoxes/NAT%20(Network%20Address%20Translation)/NAT%20(Network%20Address%20Translation).md)

##### IPv6
↗ [IPv6](IPv6/IPv6.md)



## 🚚 IP Datagram Forwarding /Delivering
↗ [Data Plane (Forwarding)](../🚙%20Data%20Plane%20(Forwarding)/Data%20Plane%20(Forwarding).md)
↗ [IP Datagram Delivery](IP%20Datagram%20Delivery.md)



## 🚏IP Datagram Routing
↗ [Network Routing (IP Address Modes) (Route Selection)](../🎮%20Control%20Plane%20(Routing%20&%20Managements)/Network%20Routing%20(IP%20Address%20Modes)%20(Route%20Selection)/Network%20Routing%20(IP%20Address%20Modes)%20(Route%20Selection).md)



## Ref
