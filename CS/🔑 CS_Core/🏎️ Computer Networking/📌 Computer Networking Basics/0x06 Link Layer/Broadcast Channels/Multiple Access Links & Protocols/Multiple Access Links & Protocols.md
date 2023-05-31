# Multiple Access Links & Protocols

[TOC]



## Res


## Intro
In order to ensure that the broadcast channel performs useful work when multiple nodes are active, it is necessary to somehow coordinate the transmissions of the active nodes. This coordination job is the responsibility of the multiple access protocol. Over the past 40 years, thousands of papers and hundreds of PhD dissertations have been written on multiple access protocols; a comprehensive survey of the first 20 years of this body of work is [Rom 1990]. Furthermore, active research in multiple access protocols continues due to the continued emergence of new types of links, particularly new wireless links.

Over the years, dozens of multiple access protocols have been implemented in a variety of link-layer technologies. Nevertheless, we can classify just about any multiple access protocol as belonging to one of three categories:
- channel partitioning protocols
- random access protocols
- taking-turns protocols. 

We’ll cover these categories of multiple access protocols in the following three subsections.


### Multiple Access Scenarios
> Perhaps a more apt human analogy for a broadcast channel is a cocktail party, where many people gather in a large room (the air providing the broadcast medium) to talk and listen. A second good analogy is something many readers will be familiar with—a classroom—where teacher(s) and student(s) similarly share the same, single, broadcast medium.
> 
> A central problem in both scenarios is that of determining who gets to talk (that is, transmit into the channel) and when.

![](../../../../../../../Assets/Pics/Screenshot%202023-05-31%20at%209.16.09%20AM.png)


### Multiple Access Protocol Characteristics
Let’s conclude this overview by noting that, ideally, a multiple access protocol for a broadcast channel of rate R bits per second should have the following desirable characteristics:
1. When only one node has data to send, that node has a throughput of R bps.
2. When M nodes have data to send, each of these nodes has a throughput of R/M bps. This need not necessarily imply that each of the M nodes always has an instantaneous rate of R/M, but rather that each node should have an average transmission rate of R/M over some suitably defined interval of time.
3. The protocol is decentralized; that is, there is no master node that represents a single point of failure for the network.
4. The protocol is simple, so that it is inexpensive to implement.


## Case Study: DOCSIS 
> DOCSIS: The Link-Layer Protocol for Cable Internet Access



## Ref

