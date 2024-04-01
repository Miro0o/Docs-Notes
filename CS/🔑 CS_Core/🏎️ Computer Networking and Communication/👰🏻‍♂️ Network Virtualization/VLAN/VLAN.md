# VLAN

[TOC]



## Res
【深入浅出计算机网络 微课视频】 https://www.bilibili.com/video/BV1NT411g7n6/?p=39&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

【深入浅出计算机网络 微课视频】 https://www.bilibili.com/video/BV1NT411g7n6/?p=40&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

### Related Topics



## Intro
As the name suggests, a switch that supports VLANs allows multiple virtual local area networks to be defined over a single physical local area network infrastructure. **Hosts within a VLAN communicate with each other as if they (and no other hosts) were connected to the switch**.

In a port-based VLAN, the switch’s ports (interfaces) are divided into groups by the network manager. Each group constitutes a VLAN, with the ports in each VLAN forming a **broadcast domain** (i.e., broadcast traffic from one port can only reach other ports in the group)

![](../../../../../Assets/Pics/Screenshot%202023-06-12%20at%204.24.55%20PM.png)


### vLANs Types & Working Layers
In this discussion, we’ve only briefly touched on VLANs and have focused on **port-based VLANs**. We should also mention that VLANs can be defined in several other ways: 
- In **MAC-based VLANs**, the network manager specifies the set of MAC addresses that belong to each VLAN; whenever a device attaches to a port, the port is connected into the appropriate VLAN based on the MAC address of the device. 
- VLANs can also be defined based on **network-layer protocols** (e.g., IPv4, IPv6, or AppleTalk) and other criteria. 
- It is also possible for VLANs to be **extended across IP routers**, allowing islands of LANs to be connected together to form a single VLAN that could span the globe. 

See the 802.1Q standard [IEEE 802.1q 2005] for more details.



## Ref

