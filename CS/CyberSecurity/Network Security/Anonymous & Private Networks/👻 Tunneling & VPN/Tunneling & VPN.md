# Tunneling & VPN

[TOC]


## Res
### Related Topics
↗ [Netowork Security /IPsec (Internet Protocol Security)](../../🏇%20Network%20Security%20Basics%20&%20Protocols/🫱🏻‍🫲🏿%20Network%20Layer%20Security/IPSec%20(Internet%20Protocol%20Security)%20&%20IPSec%20VPN/IPSec%20(Internet%20Protocol%20Security)%20&%20IPSec%20VPN.md)
↗ [Network Virtualization](../../../../../🔑%20CS_Core/🏎️%20Computer%20Networking%20and%20Communication/👰🏻‍♂️%20Network%20Virtualization/Network%20Virtualization.md)

↗ [VPC](../../../../Software%20Engineering/☁️%20Cloud%20Native/🌵%20Cloud%20Native%20Overview/🗿%20Cloud%20Models/Cloud%20Service%20(Delivery)%20Models/IaaS%20(Infrastructure%20as%20a%20Service)/VPC.md)
↗ [Proxy](../Proxy/Proxy.md)

↗ [IPSec (Internet Protocol Security) & IPSec VPN](../../🏇%20Network%20Security%20Basics%20&%20Protocols/🫱🏻‍🫲🏿%20Network%20Layer%20Security/IPSec%20(Internet%20Protocol%20Security)%20&%20IPSec%20VPN/IPSec%20(Internet%20Protocol%20Security)%20&%20IPSec%20VPN.md)
↗ [SSL VPN](📌%20Tunneling%20Protocols%20&%20Technologies/SSL%20VPN/SSL%20VPN.md)
↗ [Reverse Tunneling](Reverse%20Tunneling.md)

### VPN Providers List
1. [NordVPN](https://bi.cybernews.com/nordvpn/ "NordVPN") – best VPN using WireGuard technology
2. [Surfshark](https://bi.cybernews.com/surfsharkvpn/ "Surfshark VPN") – fast WireGuard VPN with unlimited connections
3. [IPVanish](https://bi.cybernews.com/ipvanish/ "IPVanish") – WireGuard VPN with secure browsing features
4. [Atlas VPN](https://bi.cybernews.com/atlasvpn/ "Atlas VPN") – excellent budget VPN with WireGuard
5. [CyberGhost](https://bi.cybernews.com/cyberghostvpn/ "CyberGhost VPN") – cheap VPN with a fast WireGuard solution
6. [avast](https://www.avast.com/en-us/index) -- 
7. [Private Internet Access (PIA)](https://www.privateinternetaccess.com)
8. [👍 tailscale](https://tailscale.com) 



## VPN Intro
在公用网络上建立专用网络，进行安全通讯。在企业网络中有广泛应用。
**VPN**网关通过对数据包的加密和数据包目标地址的转换实现远程访问

![VPN vs Proxy – Difference Between Them](https://www.guru99.com/images/2/041321_0431_VPNvsProxyW1.png)


---
> 🔗 https://en.wikipedia.org/wiki/Virtual_private_network

![](../../../../../Assets/Pics/Screenshot%202024-04-24%20at%209.37.22%20PM.png)

## VPN Tunneling Establishment
连接分支机构（Intranet VPN）/连接合作伙伴（Extranet VPN）/连接远程用户（Access VPN）
主机对主机/ 主机对VPN网关 /VPN网关对VPN网关 /远程用户对VPN网关

### 1️⃣ Host to Host
该模式要求两边主机都支持IPSec
VPN网关可支持也可不支持IPSec

![](../../../../../Assets/Pics/Screenshot%202023-12-16%20at%204.45.17PM.png)

### 2️⃣ Host to VPN Gateway
该模式要求两边主机都支持IPSec
VPN网关可支持也可不支持IPSec

![](../../../../../Assets/Pics/Screenshot%202024-01-05%20at%2011.55.41AM.png)

### 3️⃣ VPN to VPN
该模式要求两边主机都支持IPSec
VPN网关可支持也可不支持IPSec

![](../../../../../Assets/Pics/Screenshot%202023-12-16%20at%204.44.58PM.png)

![](../../../../../Assets/Pics/Screenshot%202024-01-05%20at%2011.56.18AM.png)

### 4️⃣ Remote User to VPN Gateway
Remote User to VPN 网关
该模式不要求同关内主机支持IPSec

![](../../../../../Assets/Pics/Screenshot%202023-12-16%20at%204.46.04PM.png)



## VPN Working Process
![](../../../../../Assets/Pics/Screenshot%202023-12-16%20at%204.38.17PM.png)



## VPN Implementation
### VPN via IPSec Tunneling
↗ [IPSec (Internet Protocol Security) & IPSec VPN](../../🏇%20Network%20Security%20Basics%20&%20Protocols/🫱🏻‍🫲🏿%20Network%20Layer%20Security/IPSec%20(Internet%20Protocol%20Security)%20&%20IPSec%20VPN/IPSec%20(Internet%20Protocol%20Security)%20&%20IPSec%20VPN.md)

### VPN via SSL Tunneling
↗ [SSL VPN](📌%20Tunneling%20Protocols%20&%20Technologies/SSL%20VPN/SSL%20VPN.md)

### 🆚 Comparing IPsec VPN vs SSL VPN
A Secure Socket Layer ([SSL](https://www.techtarget.com/searchsecurity/definition/Secure-Sockets-Layer-SSL)) VPN is another approach to securing a public network connection. The two can be used together or individually depending on the circumstances and security requirements.

With an IPsec VPN, IP packets are protected as they travel to and from the IPsec gateway at the edge of a private network and remote hosts and networks. An SSL VPN protects traffic as it moves between remote users and an SSL gateway. IPsec VPNs support all IP-based applications, while SSL VPNs only support browser-based applications, though they can support other applications with custom development.

Learn more about [how IPsec VPNs and SSL VPNs differ](https://www.techtarget.com/searchsecurity/feature/Tunnel-vision-Choosing-a-VPN-SSL-VPN-vs-IPSec-VPN)_ _in terms of authentication and access control, defending against attacks and client security. See what is best for your organization and where one type works best over the other.



## VPN设计安全性
### VPN Tunnel Security
保证VPN安全性通过以下手段：
- 隧道和加密：在安全性较高的场合使用加密隧道保护私有数据不被非法窥视和篡改。
- 数据验证：数据验证使接收方识别被篡改的数据，保证数据完整性。
- 身份鉴别：通过AAA，路由器提供用户鉴别、访问级别和访问记录，禁止非法访问。
- 抗重放：防止数据包被捕捉并重新投放到网上。

### Data Confidentiality
![](../../../../../Assets/Pics/Screenshot%202023-12-16%20at%204.42.23PM.png)

### Data Integrity
![](../../../../../Assets/Pics/Screenshot%202023-12-16%20at%204.42.44PM.png)

### Data Source Origin Authenticity
![](../../../../../Assets/Pics/Screenshot%202023-12-16%20at%204.43.06PM.png)

### Relay Attack Protection
![](../../../../../Assets/Pics/Screenshot%202023-12-16%20at%204.43.29PM.png)



## Ref
[Comparison of VPN Services]: https://en.wikipedia.org/wiki/VPN_service#comparison

[Private Internet Access VPN review]: https://cybernews.com/best-vpn/private-internet-access-review/

[🤔 What is VPN? How It Works, Types of VPN]: https://www.kaspersky.com/resource-center/definitions/what-is-a-vpn