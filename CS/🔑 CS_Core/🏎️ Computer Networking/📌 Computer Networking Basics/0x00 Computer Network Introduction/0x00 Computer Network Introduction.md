# Computer Network Introduction

[TOC]


## Res

## Overview
🔗【深入浅出计算机网络 - 1.4 计算机网络的定义和分类】 https://www.bilibili.com/video/BV1BP411j7XH/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

![](../../../../../Assets/Pics/Screenshot%202022-12-03%20at%209.25.01%20AM.png)

### Computer Network Definition


### Comput Network Taxonomy 
#### ☎️ Switching Methods
↗ [History of Computer Networks and Internet /Evolution of Communication Technologies](History%20of%20Computer%20Networks%20and%20the%20Internet.md)


#### 🧞‍♀️ Users
Public Network
Private Network


#### ⛓️ Link Media
##### Wired Network
The following classes of wired technologies are used in computer networking.
- _[Coaxial cable](https://en.wikipedia.org/wiki/Coaxial_cable "Coaxial cable")_ is widely used for cable television systems, office buildings, and other work sites for local area networks. Transmission speed ranges from 200 million bits per second to more than 500 million bits per second.
	- [ITU-T](https://en.wikipedia.org/wiki/ITU-T "ITU-T") [G.hn](https://en.wikipedia.org/wiki/G.hn "G.hn") technology uses existing [home wiring](https://en.wikipedia.org/wiki/Home_wiring "Home wiring")([coaxial cable](https://en.wikipedia.org/wiki/Ethernet_over_coax "Ethernet over coax"), phone lines and [power lines](https://en.wikipedia.org/wiki/Power_line_communication "Power line communication")) to create a high-speed local area network.

- _[Twisted pair](https://en.wikipedia.org/wiki/Twisted_pair "Twisted pair")_ cabling is used for wired [Ethernet](https://en.wikipedia.org/wiki/Ethernet "Ethernet") and other standards. It typically consists of 4 pairs of copper cabling that can be utilized for both voice and data transmission. The use of two wires twisted together helps to reduce [crosstalk](https://en.wikipedia.org/wiki/Crosstalk_(electronics) "Crosstalk (electronics)") and [electromagnetic induction](https://en.wikipedia.org/wiki/Electromagnetic_induction "Electromagnetic induction"). The transmission speed ranges from 2 Mbit/s to 10 Gbit/s. Twisted pair cabling comes in two forms: unshielded twisted pair (UTP) and shielded twisted-pair (STP). Each form comes in several [category ratings](https://en.wikipedia.org/wiki/Category_cable "Category cable"), designed for use in various scenarios.

- An _[optical fiber](https://en.wikipedia.org/wiki/Optical_fiber "Optical fiber")_ is a glass fiber. It carries pulses of light that represent data via lasers and [optical amplifiers](https://en.wikipedia.org/wiki/Optical_amplifier "Optical amplifier"). Some advantages of optical fibers over metal wires are very low transmission loss and immunity to electrical interference. Using dense [wave division multiplexing](https://en.wikipedia.org/wiki/Wavelength-division_multiplexing "Wavelength-division multiplexing"), optical fibers can simultaneously carry multiple streams of data on different wavelengths of light, which greatly increases the rate that data can be sent to up to trillions of bits per second. Optic fibers can be used for long runs of cable carrying very high data rates, and are used for [undersea communications cables](https://en.wikipedia.org/wiki/Undersea_communications_cables "Undersea communications cables") to interconnect continents. 
	- There are two basic types of fiber optics, [single-mode optical fiber](https://en.wikipedia.org/wiki/Single-mode_optical_fiber "Single-mode optical fiber")(SMF) and [multi-mode optical fiber](https://en.wikipedia.org/wiki/Multi-mode_optical_fiber "Multi-mode optical fiber") (MMF). Single-mode fiber has the advantage of being able to sustain a coherent signal for dozens or even a hundred kilometers. Multimode fiber is cheaper to terminate but is limited to a few hundred or even only a few dozen of meters, depending on the data rate and cable grade.


##### Wireless Network
- _Radio and [spread spectrum](https://en.wikipedia.org/wiki/Spread_spectrum "Spread spectrum") technologies_ – Wireless LANs use a high-frequency radio technology similar to digital cellular. Wireless LANs use spread spectrum technology to enable communication between multiple devices in a limited area. [IEEE 802.11](https://en.wikipedia.org/wiki/IEEE_802.11 "IEEE 802.11") defines a common flavor of open-standards wireless radio-wave technology known as [Wi-Fi](https://en.wikipedia.org/wiki/Wi-Fi "Wi-Fi").
	- _[Cellular networks](https://en.wikipedia.org/wiki/Cellular_network "Cellular network")_ use several radio communications technologies. The systems divide the region covered into multiple geographic areas. Each area is served by a low-power [transceiver](https://en.wikipedia.org/wiki/Transceiver "Transceiver").
	- _[Communications satellites](https://en.wikipedia.org/wiki/Communications_satellite "Communications satellite")_ – Satellites also communicate via microwave. The satellites are stationed in space, typically in geosynchronous orbit 35,400 km (22,000 mi) above the equator. These Earth-orbiting systems are capable of receiving and relaying voice, data, and TV signals.
	- _Terrestrial [microwave](https://en.wikipedia.org/wiki/Microwave "Microwave")_ – Terrestrial microwave communication uses Earth-based transmitters and receivers resembling satellite dishes. Terrestrial microwaves are in the low gigahertz range, which limits all communications to line-of-sight. Relay stations are spaced approximately 40 miles (64 km) apart.

- _[Free-space optical communication](https://en.wikipedia.org/wiki/Free-space_optical_communication "Free-space optical communication")_ uses visible or invisible light for communications. In most cases, [line-of-sight propagation](https://en.wikipedia.org/wiki/Line-of-sight_propagation "Line-of-sight propagation") is used, which limits the physical positioning of communicating devices.

- Extending the Internet to interplanetary dimensions via radio waves and optical means, the [Interplanetary Internet](https://en.wikipedia.org/wiki/Interplanetary_Internet "Interplanetary Internet").

- [IP over Avian Carriers](https://en.wikipedia.org/wiki/IP_over_Avian_Carriers "IP over Avian Carriers") was a humorous April fool's [Request for Comments](https://en.wikipedia.org/wiki/Request_for_Comments "Request for Comments"), issued as [RFC](https://en.wikipedia.org/wiki/RFC_(identifier) "RFC (identifier)") [1149](https://datatracker.ietf.org/doc/html/rfc1149). It was implemented in real life in 2001.

The last two cases have a large [round-trip delay time](https://en.wikipedia.org/wiki/Round-trip_delay_time "Round-trip delay time"), which gives slow [two-way communication](https://en.wikipedia.org/wiki/Two-way_communication "Two-way communication") but doesn't prevent sending large amounts of information (they can have high throughput).


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
> Recall Overlay/Underlay Architecture in ↗ [SDN Architecture](../../🙌🏻%20SDN/Overview/SDN%20Architecture.md)

An [overlay network](https://en.wikipedia.org/wiki/Overlay_network "Overlay network") is a virtual network that is built on top of another network. Nodes in the overlay network are connected by virtual or logical links. Each link corresponds to a path, perhaps through many physical links, in the underlying network. The topology of the overlay network may (and often does) differ from that of the underlying one.

**Examples**
1. The most striking example of an overlay network is the Internet itself. The Internet itself was initially built as an overlay on the [telephone network](https://en.wikipedia.org/wiki/Telephone_network).

2. Many [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer "Peer-to-peer") networks are also overlay networks. They are organized as nodes of a virtual system of links that run on top of the [Internet](https://en.wikipedia.org/wiki/Internet "Internet").

3. Another example of an overlay network is a [distributed hash table](https://en.wikipedia.org/wiki/Distributed_hash_table "Distributed hash table"), which maps keys to nodes in the network. In this case, the underlying network is an IP network, and the overlay network is a table (actually a [map](https://en.wikipedia.org/wiki/Associative_array "Associative array")) indexed by keys.


### Computer Network Nodes
#TODO 


### Communication Protocols



## 🎸 Development of Computer Networks and the Internet
🤔 Network, Computer Networks, internet, the Internet, Web, and WWW?

**Network**: vertexes + edges
**Computer Networks**: end hosts + link media
**internet**: a general term referring to a computer network that is interconnected (seen as a single network that is interconnected)

**Internet**: computer networks providing services (Web services, in most cases)
**WWW = Web**: a service of computer networks providing content to every connected end host

> **Tim Berners-Lee** proposed the architecture of what became known as the **World Wide Web**. He created the first web [server](https://developer.mozilla.org/en-US/docs/Glossary/Server), web [browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser), and webpage on his computer at the CERN physics research lab in 1990. In 1991, he announced his creation on the alt.hypertext newsgroup, marking the moment the Web was first made public.
> 
> The system we know today as "the Web" consists of several components:
> - The **[HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP)** protocol governs data transfer between a server and a client.
> - To access a Web component, a client supplies a unique universal identifier, called a **[URL](https://developer.mozilla.org/en-US/docs/Glossary/URL)**(uniform resource locator) or [URI](https://developer.mozilla.org/en-US/docs/Glossary/URI) (uniform resource identifier) (formally called Universal Document Identifier (UDI)).
> - **[HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML)** (hypertext markup language) is the most common format for publishing web documents.


[World Wide Web]: https://developer.mozilla.org/en-US/docs/Glossary/World_Wide_Web


↗ [History of Computer Networks and the Internet](History%20of%20Computer%20Networks%20and%20the%20Internet.md)



## 🍔 Computer Network Layering Architecture
↗ [Computer Network Layering Architecture](Computer%20Network%20Layering%20Architecture.md)



## ⏲️ Computer Network Performance
↗ [Computer Network Performance Metrics](Computer%20Network%20Performance%20Metrics.md)



## ✍🏾 HW
![](../../../../../Assets/Pics/Screen%20Shot%202022-09-24%20at%204.55.51%20PM-4009768.png)

## Ref

