# ICMP (Internet Control Message Protocol)

[TOC]



## Res


## Intro
### Why is ICMP categorized as a l3 protocol?
🔗 [Why is ICMP categorized as a L3 protocol? | serverFautl](https://serverfault.com/questions/511965/why-is-icmp-categorized-as-a-layer-3-protocol)

ICMP is actually at the "top" of the layer 3. It uses the IP protocol to deliver data to a remote host. In other words, ICMP messages must be encapsulated in IP packets. 

Consider it as similar to ARP which could be considered to be "at the top" of layer 2, while using the Ethernet protocol to actually send packets.

ICMP is implemented as a part of the IP layer so ICMP processing can be viewed as occurring parallel to, or as a part of, IP processing. Therefore, in the topic on TCP/IP-based layered network, ICMP is shown as a layer 3 protocol.

**@Robbie Mckennie**

Which layer ICMP belongs to is a subject of fierce debate. The ICMP header is at layer 4, just like TCP and UDP so people argue that it belongs in layer 4. Others however argue that ICMP is a layer 3 protocol, since it assists IP and has no concept of ports.

For me, classification of a protocol as belonging to a certain layer in the OSI model depends on how protocol works. An example:

> BGP is used to route at layer 3, but BGP itself is carried by TCP ( and of course IP )



## Ref

