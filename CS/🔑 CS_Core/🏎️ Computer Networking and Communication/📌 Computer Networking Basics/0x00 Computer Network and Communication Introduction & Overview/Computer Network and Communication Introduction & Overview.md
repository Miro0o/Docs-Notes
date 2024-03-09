# Computer Network and Communication Introduction & Overview

[TOC]


## Res



## Overview
🔗【深入浅出计算机网络 - 1.4 计算机网络的定义和分类】 https://www.bilibili.com/video/BV1BP411j7XH/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

![](../../../../../Assets/Pics/Screenshot%202022-12-03%20at%209.25.01%20AM.png)


### Computer Network Definition


### Comput Network Taxonomy 
#### ☎️ Switching Methods
↗ [History of Computer Networks and Internet /Evolution of Communication Technologies](History%20of%20Computer%20Networks.md)
#### 🧞‍♀️ Users
Public Network
Private Network
#### ⛓️ Link Media
↗ [0x07 Physical Layer](../0x07%20Physical%20Layer/0x07%20Physical%20Layer.md)
#### 🌄 Spatial Scope (Geographic Scale)
> 🔗 [Computer network](https://en.wikipedia.org/wiki/Computer_network)

![Data Networks classification by spatial scope.svg](../../../../../Assets/Pics/150px-Data_Networks_classification_by_spatial_scope.svg-20221203085442189.png)

- [Nanoscale](https://en.wikipedia.org/wiki/Nanonetwork)
- [Near-field (NFC)](https://en.wikipedia.org/wiki/Near-field_communication)
- [Body](https://en.wikipedia.org/wiki/Body_area_network)
- [Personal (PAN)](https://en.wikipedia.org/wiki/Personal_area_network)
- [Near-me](https://en.wikipedia.org/wiki/Near-me_area_network)
- [Local (LAN)](https://en.wikipedia.org/wiki/Local_area_network)
  - [Storage (SAN)](https://en.wikipedia.org/wiki/Storage_area_network)
  - [Wireless (WLAN)](https://en.wikipedia.org/wiki/Wireless_LAN)
  - [Virtual (VLAN)](https://en.wikipedia.org/wiki/VLAN)
- [Home (HAN)](https://en.wikipedia.org/wiki/Home_network)
- [Building](https://en.wikipedia.org/wiki/Building_area_network)
- [Campus (CAN)](https://en.wikipedia.org/wiki/Campus_network)
- [Backbone](https://en.wikipedia.org/wiki/Backbone_network)
- [Metropolitan (MAN)](https://en.wikipedia.org/wiki/Metropolitan_area_network "Metropolitan area network")
  - [Municipal wireless (MWN)](https://en.wikipedia.org/wiki/Municipal_wireless_network)
- [Wide (WAN)](https://en.wikipedia.org/wiki/Wide_area_network)
- Enterprise private network
- Virtual private network
- Global area network
- [Cloud](https://en.wikipedia.org/wiki/Internet_area_network)
- [Internet](https://en.wikipedia.org/wiki/Internet "Internet")
- [Interplanetary Internet](https://en.wikipedia.org/wiki/Interplanetary_Internet)
#### 🕸️ Topology
Common layouts are:
- [Bus network](https://en.wikipedia.org/wiki/Bus_network "Bus network"): all nodes are connected to a common medium along this medium.
	- This was the layout used in the original [Ethernet](https://en.wikipedia.org/wiki/Ethernet "Ethernet"), called [10BASE5](https://en.wikipedia.org/wiki/10BASE5 "10BASE5") and [10BASE2](https://en.wikipedia.org/wiki/10BASE2 "10BASE2"). 
	- This is still a common topology on the [data link layer](https://en.wikipedia.org/wiki/Data_link_layer "Data link layer"), 
	- although modern [physical layer](https://en.wikipedia.org/wiki/Physical_layer "Physical layer") variants use [point-to-point](https://en.wikipedia.org/wiki/Point-to-point_(telecommunications) "Point-to-point (telecommunications)") links instead, forming a star or a tree.
- [Star network](https://en.wikipedia.org/wiki/Star_network "Star network"): all nodes are connected to a special central node.
	- This is the typical layout found in a small [switched Ethernet](https://en.wikipedia.org/wiki/Switched_Ethernet "Switched Ethernet") LAN, where each client connects to a central network switch
	- and logically in a [wireless LAN](https://en.wikipedia.org/wiki/Wireless_LAN "Wireless LAN"), where each wireless client associates with the central [wireless access point](https://en.wikipedia.org/wiki/Wireless_access_point "Wireless access point").
- [Ring network](https://en.wikipedia.org/wiki/Ring_network "Ring network"): each node is connected to its left and right neighbor node, such that all nodes are connected and that each node can reach each other node by traversing nodes left or rightwards.
	- [Token ring](https://en.wikipedia.org/wiki/Token_ring "Token ring") networks, and 
	- the [Fiber Distributed Data Interface](https://en.wikipedia.org/wiki/Fiber_Distributed_Data_Interface "Fiber Distributed Data Interface") (FDDI), made use of such a topology.
- [Mesh network](https://en.wikipedia.org/wiki/Mesh_network "Mesh network"): each node is connected to an arbitrary number of neighbors in such a way that there is at least one traversal from any node to any other.
- [Fully connected network](https://en.wikipedia.org/wiki/Fully_connected_network "Fully connected network"): each node is connected to every other node in the network.
- [Tree network](https://en.wikipedia.org/wiki/Tree_network "Tree network"): nodes are arranged hierarchically. This is the natural topology for a larger Ethernet network with multiple switches and without redundant meshing.
##### Overlay Network
> Recall Overlay/Underlay Architecture in ↗ [SDN Architecture](../../🙌🏻%20SDN%20(Software%20Defined%20Network)/SDN%20Overview/SDN%20Architecture.md)

An [overlay network](https://en.wikipedia.org/wiki/Overlay_network "Overlay network") is a virtual network that is built on top of another network. Nodes in the overlay network are connected by virtual or logical links. Each link corresponds to a path, perhaps through many physical links, in the underlying network. The topology of the overlay network may (and often does) differ from that of the underlying one.

**Examples**
1. The most striking example of an overlay network is the Internet itself. The Internet itself was initially built as an overlay on the [telephone network](https://en.wikipedia.org/wiki/Telephone_network).
2. Many [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer "Peer-to-peer") networks are also overlay networks. They are organized as nodes of a virtual system of links that run on top of the [Internet](https://en.wikipedia.org/wiki/Internet "Internet").
3. Another example of an overlay network is a [distributed hash table](https://en.wikipedia.org/wiki/Distributed_hash_table "Distributed hash table"), which maps keys to nodes in the network. In this case, the underlying network is an IP network, and the overlay network is a table (actually a [map](https://en.wikipedia.org/wiki/Associative_array "Associative array")) indexed by keys.


### Computer Network Nodes


### Communication Protocols



## 🎸 Development of Computer Networks and the Internet

↗ [History of Computer Networks](History%20of%20Computer%20Networks.md)

> 🤔 Network, Computer Networks, internet, the Internet, Web, and WWW?
> Answer at ↗ [FAQ](../FAQ.md) or above notes ⏫



## 🍔 Computer Network Layering Architecture
↗ [Computer Network Layering Architecture](Computer%20Network%20Layering%20Architecture.md)



## ⏲️ Computer Network Performance
↗ [Computer Network Performance Metrics](Computer%20Network%20Performance%20Metrics.md)



## ✍🏾 HW
![](../../../../../Assets/Pics/Screen%20Shot%202022-09-24%20at%204.55.51%20PM-4009768.png)



## Ref