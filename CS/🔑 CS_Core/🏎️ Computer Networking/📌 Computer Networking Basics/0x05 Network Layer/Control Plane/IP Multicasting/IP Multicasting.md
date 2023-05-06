# IP Multicasting

[TOC]



## Res
🔗 【深入浅出计算机网络 - 4.7.1~4.7.2 IP多播技术的相关基本概念、IP多播地址和多播组】 https://www.bilibili.com/video/BV16f4y1Z7bS/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

↗ [Routing Protocols for Multicasting](../Routing%20Protocols%20for%20Multicasting/Routing%20Protocols%20for%20Multicasting.md)



## Overview
- Multicasting Group
- Multicasting Address

![Screenshot 2022-11-26 at 5.07.13 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-26%20at%205.07.13%20PM.png)

![Screenshot 2022-11-26 at 5.06.15 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-26%20at%205.06.15%20PM.png)



## Multicasting on LAN
![Screenshot 2022-11-26 at 5.13.42 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-26%20at%205.13.42%20PM.png)



## Multicasting on Internet
![Screenshot 2022-11-26 at 5.16.55 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-26%20at%205.16.55%20PM.png)

To be able to multicast on Internet, within each router it uses **IGMP (IPv4) or MLD (IPv6)** to be informed synchronically of its subnet hosts' multicasting group list; meanwhile interbetween each routers different **routing protocols for multicasting** are used to generate **multicasting forwarding tree** to route the multicast packages. 

Multicast communication can have single or multiple senders and receivers and thus, IGMP can be used in :video_camera: streaming videos, :video_game:  gaming or :desktop_computer:   web conferencing tools. 


### IGMP (IPv4)
↗ [IGMP (IPv4)](IGMP%20(IPv4)/IGMP%20(IPv4).md)


### MLD (IPv6)
↗ [MLD (IPv6)](MLD%20(IPv6)/MLD%20(IPv6).md)


### Routing Protocols for Multicasting
↗ [Routing Protocols for Multicasting](../Routing%20Protocols%20for%20Multicasting.md)



## Ref
