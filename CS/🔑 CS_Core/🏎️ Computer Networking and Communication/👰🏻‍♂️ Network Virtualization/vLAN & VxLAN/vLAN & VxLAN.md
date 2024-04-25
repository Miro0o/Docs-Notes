# vLAN & VXLAN

[TOC]



## Res
### Related Topic
↗ [Link Layer (Tier-2) Switch](../../📌%20Computer%20Networking%20Basics/0x06%20Data%20Link%20Layer/📌%20Link%20Layer%20(Switched%20Network)%20Basics/Link%20Layer%20Network%20Devices/Link%20Layer%20(Tier-2)%20Switch.md)
↗ [Switched LAN](../../📌%20Computer%20Networking%20Basics/0x06%20Data%20Link%20Layer/Switched%20LAN/Switched%20LAN.md)

↗ [Tunneling & VPN](../../../../CyberSecurity/Network%20Security/Anonymous%20&%20Private%20Networks/👻%20Tunneling%20&%20VPN/Tunneling%20&%20VPN.md)
↗ [Tunneling Protocols & Technologies](../../../../CyberSecurity/Network%20Security/Anonymous%20&%20Private%20Networks/👻%20Tunneling%20&%20VPN/📌%20Tunneling%20Protocols%20&%20Technologies/Tunneling%20Protocols%20&%20Technologies.md)


### Learning Resrouces
🎬【深入浅出计算机网络 微课视频】 https://www.bilibili.com/video/BV1NT411g7n6/?p=39&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

🎬【深入浅出计算机网络 微课视频】 https://www.bilibili.com/video/BV1NT411g7n6/?p=40&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d



## Intro
### LAN (Local Area Network)
↗ [Switched LAN](../../📌%20Computer%20Networking%20Basics/0x06%20Data%20Link%20Layer/Switched%20LAN/Switched%20LAN.md)


### vLAN (Virtual Local Area Network)
As the name suggests, a switch that supports VLANs allows multiple virtual local area networks to be defined over a single physical local area network infrastructure. **Hosts within a VLAN communicate with each other as if they (and no other hosts) were connected to the switch**.
#### vLANs Types & Working Layers
1. In a **port-based VLAN**, the switch’s ports (interfaces) are divided into groups by the network manager. Each group constitutes a VLAN, with the ports in each VLAN forming a **broadcast domain** (i.e., broadcast traffic from one port can only reach other ports in the group)

![](../../../../../Assets/Pics/Screenshot%202023-06-12%20at%204.24.55%20PM.png)

2. In **MAC-based VLANs**, the network manager specifies the set of MAC addresses that belong to each VLAN; whenever a device attaches to a port, the port is connected into the appropriate VLAN based on the MAC address of the device. 
3. VLANs can also be defined based on **network-layer protocols** (e.g., IPv4, IPv6, or AppleTalk) and other criteria. 
4. It is also possible for VLANs to be **extended across IP routers**, allowing islands of LANs to be connected together to form a single VLAN that could span the globe. 

See the 802.1Q standard [IEEE 802.1q 2005] for more details.


### VXLAN (Virtual eXtensible Local Area Network)



## Ref
[👍 深入理解lan、vlan、vxlan《OpenStack 网络》]: https://developer.aliyun.com/article/945531#slide-1
