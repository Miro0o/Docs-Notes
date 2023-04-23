# TCP

[TOC]



## Res
↗ [🍻 Principles of Reliable Data Transfer](../../RDT/🍻%20Principles%20of%20Reliable%20Data%20Transfer.md)



## Overview
![Screenshot 2022-11-13 at 10.46.24 AM](../../../../../../Assets/Pics/Screenshot%202022-11-13%20at%2010.46.24%20AM.png)


### TCP Connections
#### Send/Receive Buffers
Once a TCP connection is established, the two application processes can send data to each other. 

Let’s consider the sending of data from the client process to the server process. The client process passes a stream of data through the socket (the door of the process). Once the data passes through the door, the data is in the hands of TCP running in the client. TCP directs this data to the connection’s **send buffer**, which is one of the buffers that is set aside during the initial three-way handshake. From time to time, TCP will grab chunks of data from the send buffer and pass the data to the network layer. 

Interestingly, the TCP specification [RFC 793] is very laid back about specifying when TCP should actually send buffered data, stating that TCP should “send that data in seg- ments at its own convenience.”

![](../../../../../../Assets/Pics/Screenshot%202023-04-19%20at%2012.57.17%20PM.png)

Each side of the connection has its own send buffer and its own receive buffer. (You can see the online flow-control interactive animation at 🔗 http://www.awl.com/kurose-ross, which provides an anima- tion of the send and receive buffers.)


#### Maximum Segment Size, MSS
The maximum amount of data that can be grabbed and placed in a segment is limited by the **maximum segment size (MSS)**. 
- The MSS is typically set by first determining the length of the largest link-layer frame that can be sent by the local sending host (the so-called **maximum transmission unit, MTU**), and then setting the MSS to ensure that a TCP segment (when encapsulated in an IP datagram) plus the TCP/IP header length (typically 40 bytes) will fit into a single link-layer frame.
	- Both Ethernet and PPP link-layer protocols have an MTU of 1,500 bytes. Thus, a typical value of MSS is 1460 bytes.
	- Approaches have also been proposed for discovering the **path MTU**: the largest link-layer frame that can be sent on all links from source to destination [RFC 1191] -- and setting the MSS based on the path MTU value.
- Note that the MSS is the maximum amount of application-layer data in the segment, not the maximum size of the TCP segment including headers. (This terminology is confusing, but we have to live with it, as it is well entrenched.)



## TCP Segment Header Structure
🔗【深入浅出计算机网络 - 5.3.1 TCP报文段的首部格式】 https://www.bilibili.com/video/BV1Ce4y1674L/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d


![Explaining TCP/IP | Kelvin.Liang](../../../../../../Assets/Pics/TCP_header.jpeg)
<small>TCP Segment Header</small>

![](../../../../../../Assets/Pics/Screenshot%202023-04-19%20at%2012.44.14%20PM.png)

![](../../../../../../Assets/Pics/Screenshot%202023-04-19%20at%2012.45.29%20PM.png)
<small>Source: <a>https://skminhaj.wordpress.com/2016/02/15/tcp-segment-vs-udp-datagram-header-format/</a></small>



## 🫱🏻‍🫲🏿 TCP Connection Management
↗ [TCP Connection Management](TCP%20Connection%20Management.md)



## 🚰 TCP Flow Control
↗ [TCP Flow Control](TCP%20Flow%20Control.md)



## 🚦 TCP Congestion Control
↗ [TCP Congestion Control](TCP%20Congestion%20Control.md)



## TCP Meaturements
![](../../../../../../Assets/Pics/Screenshot%202023-04-22%20at%203.39.35%20PM.png)

![](../../../../../../Assets/Pics/Screenshot%202023-04-22%20at%203.39.52%20PM.png)



## 🛸 Evolusion of Transport Layer Functionality

🙈 See [QUIC](../../QUIC.md) 



## Ref
