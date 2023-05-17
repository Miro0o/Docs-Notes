# Control Plane (Routing & Managements)

[TOC]



## Res


## Intro
### Routing Tables, Forwarding Tables & Flow Tables
![](../../../../../../Assets/Pics/Screenshot%202023-05-06%20at%2010.30.01%20AM.png)

Recall Figures 4.2 and 4.3. There, we saw that the **forwarding table** (in the case of **destination-based forwarding**) and the **flow table** (in the case of **generalized forwarding**) were the principal elements that linked the network layer’s data and control planes. We learned that these tables specify the local data-plane forwarding behavior of a router. We saw that in the case of generalized forwarding, the actions taken could include not only **forwarding** a packet to a router’s output port, but also **dropping** a packet, **replicating** a packet, and/or **rewriting** layer 2, 3 or 4 packet-header fields.

In this chapter, we’ll study how those forwarding and flow tables are **computed**, **maintained** and **installed**. In our introduction to the network layer in Section 4.1, we learned that there are two possible approaches for doing so.

### Per-router Control
![](../../../../../../Assets/Pics/Screenshot%202023-05-17%20at%209.59.44%20AM.png)


### Logically Centralized Control
![](../../../../../../Assets/Pics/Screenshot%202023-05-17%20at%209.59.25%20AM.png)

The controller interacts with a **control agent (CA)** in each of the routers via a well-defined protocol to configure and manage that router’s flow table. Typically, the CA has minimum functionality; its job is to communicate with the controller, and to do as the controller commands. Unlike the routing algorithms in Figure 5.1, the CAs do not directly interact with each other nor do they actively take part in computing the forwarding table. This is a key distinction between per-router control and logically centralized control.

By “logically centralized” control [Levin 2012] we mean that the routing control service is accessed as if it were a single central service point, even though the service is likely to be implemented via multiple servers for fault-tolerance, and performance scalability reasons. As we will see in Section 5.5, SDN adopts this notion of a logically centralized controller—an approach that is finding increased use in production deployments. Google uses SDN to control the rout- ers in its internal B4 global wide-area net





## Ref

