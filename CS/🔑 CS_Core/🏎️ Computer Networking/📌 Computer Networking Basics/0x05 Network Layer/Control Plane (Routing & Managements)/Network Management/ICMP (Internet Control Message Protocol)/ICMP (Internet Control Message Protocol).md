# ICMP (Internet Control Message Protocol)

[TOC]



## Res


## Intro
The Internet Control Message Protocol (ICMP), specified in [RFC 792], is used by hosts and routers to communicate network-layer information to each other. 

The most typical use of ICMP is for **error reporting**.
> For example, when running an HTTP session, you may have encountered an error message such as “Destination network unreachable.” This message had its origins in ICMP. 

At some point, an IP router was unable to find a path to the host specified in your HTTP request. That router created and sent an ICMP message to your host indicating the error.

==ICMP is often considered part of IP, but architecturally it lies just above IP, as ICMP messages are carried inside IP datagrams.== That is, ICMP messages are carried as IP payload, just as TCP or UDP segments are carried as IP payload. Similarly, when a host receives an IP datagram with ICMP specified as the upper-layer protocol (an upper-layer protocol number of 1), it demultiplexes the datagram’s contents to ICMP, just as it would demultiplex a datagram’s content to TCP or UDP.

> **🤦🏼 Why is ICMP categorized as a l3 protocol?**
> 🔗 [Why is ICMP categorized as a L3 protocol? | serverFautl](https://serverfault.com/questions/511965/why-is-icmp-categorized-as-a-layer-3-protocol)
> 
> ICMP is actually **at the "top" of the layer 3.** It uses the IP protocol to deliver data to a remote host. In other words, ICMP messages must be encapsulated in IP packets. 
> 
> Consider it as similar to ARP which could be considered to be **"at the top" of layer 2**, while using the Ethernet protocol to actually send packets.
> 
> ICMP is implemented as a part of the IP layer so ICMP processing can be viewed as occurring parallel to, or as a part of, IP processing. Therefore, in the topic on TCP/IP-based layered network, ICMP is shown as a layer 3 protocol.
> 
> **@Robbie Mckennie**
> Which layer ICMP belongs to is a subject of fierce debate. The ICMP header is at layer 4, just like TCP and UDP so people argue that it belongs in layer 4. Others however argue that ICMP is a layer 3 protocol, since it assists IP and has no concept of ports.
> 
> For me, classification of a protocol as belonging to a certain layer in the OSI model depends on how protocol works.
> 
> An example:
> BGP is used to route at layer 3, but BGP itself is carried by TCP ( and of course IP )




## Ref

