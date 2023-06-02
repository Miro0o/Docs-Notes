# Network Sockets

[TOC]



## Res
↗ [Sockets](../../../Processes%20Management/IPC%20(Inter%20Process%20Communication)/Sockets/Sockets.md)

↗ [Socket Programming](../../../../../🏎️%20Computer%20Networking/📌%20Computer%20Networking%20Basics/Socket%20Programming/Socket%20Programming.md)



## Intro
> 🔗 <https://en.wikipedia.org/wiki/Network_socket>

### What is Socket
A **network socket** is a software structure within a [network node](https://en.wikipedia.org/wiki/Node_(networking)) of a [computer network](https://en.wikipedia.org/wiki/Computer_network) that serves as an endpoint for sending and receiving data across the network. The structure and properties of a socket are defined by an [application programming interface](https://en.wikipedia.org/wiki/Application_programming_interface) (API) for the networking architecture. Sockets are created only during the lifetime of a [process](https://en.wikipedia.org/wiki/Process_(computing)) of an application running in the node.


### Socket in Internet
Because of the standardization of the [TCP/IP](https://en.wikipedia.org/wiki/TCP/IP) protocols in the development of the [Internet](https://en.wikipedia.org/wiki/Internet), the term *network socket* is most commonly used in the context of the *Internet protocol suite*, and is therefore often also referred to as **Internet socket**. In this context, a socket is externally identified to other hosts by its **socket address**, which is the triad of [transport protocol](https://en.wikipedia.org/wiki/Transport_protocol), [IP address](https://en.wikipedia.org/wiki/IP_address), and [port number](https://en.wikipedia.org/wiki/Port_number).


### Socket in IPC
The term *socket* is also used for the software endpoint of node-internal [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) (IPC), which often uses the same API as a network socket.



## Socket Types
### 🌐 Internet Sockets
#### Datagram sockets
[Connectionless](https://en.wikipedia.org/wiki/Connectionless) sockets, which use [User Datagram Protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol) (UDP). Each packet sent or received on a datagram socket is individually addressed and routed. Order and reliability are not guaranteed with datagram sockets, so multiple packets sent from one machine or process to another may arrive in any order or might not arrive at all. Special configuration may be required to send [broadcasts](https://en.wikipedia.org/wiki/Broadcasting_(networking)) on a datagram socket. In order to receive broadcast packets, a datagram socket should not be bound to a specific address, though in some implementations, broadcast packets may also be received when a datagram socket is bound to a specific address.


#### Stream sockets
[Connection-oriented](https://en.wikipedia.org/wiki/Connection-oriented) sockets, which use [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) (TCP), [Stream Control Transmission Protocol](https://en.wikipedia.org/wiki/Stream_Control_Transmission_Protocol) (SCTP) or [Datagram Congestion Control Protocol](https://en.wikipedia.org/wiki/Datagram_Congestion_Control_Protocol) (DCCP). A stream socket provides a [sequenced](https://en.wikipedia.org/wiki/Sequenced) and unique flow of error-free data without record boundaries, with well-defined mechanisms for creating and destroying connections and reporting errors. A stream socket transmits data [reliably](https://en.wikipedia.org/wiki/Reliability_(computer_networking)), in order, and with [out-of-band](https://en.wikipedia.org/wiki/Out-of-band_data) capabilities. On the Internet, stream sockets are typically implemented using TCP so that applications can run across any networks using TCP/IP protocol.


#### Raw sockets
Allow direct sending and receiving of IP packets without any protocol-specific transport layer formatting. With other types of sockets, the [payload](https://en.wikipedia.org/wiki/Payload_(computing)) is automatically [encapsulated](https://en.wikipedia.org/wiki/Encapsulation_(networking)) according to the chosen transport layer protocol (e.g. TCP, UDP), and the socket user is unaware of the existence of protocol [headers](https://en.wikipedia.org/wiki/Header_(computing)) that are broadcast with the payload. When reading from a raw socket, the headers are usually included. When transmitting packets from a raw socket, the automatic addition of a header is optional.

Most socket [application programming interfaces](https://en.wikipedia.org/wiki/Application_programming_interface) (APIs), for example, those based on [Berkeley sockets](https://en.wikipedia.org/wiki/Berkeley_sockets), support raw sockets. [Windows XP](https://en.wikipedia.org/wiki/Windows_XP) was released in 2001 with raw socket support implemented in the [Winsock](https://en.wikipedia.org/wiki/Winsock) interface, but three years later, Microsoft limited Winsock's raw socket support because of security concerns.

Raw sockets are used in security-related applications like [Nmap](https://en.wikipedia.org/wiki/Nmap). One use case for raw sockets is the implementation of new transport-layer protocols in [user space](https://en.wikipedia.org/wiki/User_space). Raw sockets are typically available in network equipment, and used for [routing protocols](https://en.wikipedia.org/wiki/Routing_protocol) such as the Internet Group Management Protocol (IGMP) and [Open Shortest Path First](https://en.wikipedia.org/wiki/Open_Shortest_Path_First)(OSPF), and in the [Internet Control Message Protocol](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol) (ICMP) used, among other things, by the [ping utility](https://en.wikipedia.org/wiki/Ping_utility).


### 🏘️ Sockets in IPC
Other socket types are implemented over other transport protocols, such as [Systems Network Architecture](https://en.wikipedia.org/wiki/Systems_Network_Architecture) and [Unix domain sockets](https://en.wikipedia.org/wiki/Unix_domain_socket) for internal inter-process communication.


#### [Unix Domain Socket](https://en.wikipedia.org/wiki/Unix_domain_socket)
A **Unix domain socket** aka **UDS** or **IPC socket** ([inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) socket) is a data [communications endpoint](https://en.wikipedia.org/wiki/Communication_endpoint) for exchanging data between processes executing on the same host operating system. It is also referred to by its address family `AF_UNIX`. Valid socket types in the UNIX domain are:[[1\]](https://en.wikipedia.org/wiki/Unix_domain_socket#cite_note-man-unix-sockets-1)

- `SOCK_STREAM` (compare to [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)) – for a stream-oriented socket
- `SOCK_DGRAM` (compare to [UDP](https://en.wikipedia.org/wiki/User_Datagram_Protocol)) – for a datagram-oriented socket that preserves message boundaries (as on most UNIX implementations, UNIX domain datagram sockets are always reliable and don't reorder datagrams)
- `SOCK_SEQPACKET` (compare to [SCTP](https://en.wikipedia.org/wiki/SCTP)) – for a sequenced-packet socket that is connection-oriented, preserves message boundaries, and delivers messages in the order that they were sent

The Unix domain socket facility is a standard component of [POSIX](https://en.wikipedia.org/wiki/POSIX) [operating systems](https://en.wikipedia.org/wiki/Operating_system).

The [API](https://en.wikipedia.org/wiki/API) for Unix domain sockets is similar to that of an [Internet socket](https://en.wikipedia.org/wiki/Internet_socket), but rather than using an underlying network protocol, all communication occurs entirely within the operating system [kernel](https://en.wikipedia.org/wiki/Kernel_(operating_system)). **Unix domain sockets does'nt use the triad of  "transportation protocol + IP address + Portnumber" in IPC like Internet Socket in Internet.** Unix domain sockets may use the file system as their address [name space](https://en.wikipedia.org/wiki/Name_space). (Some operating systems, like [Linux](https://en.wikipedia.org/wiki/Linux), offer additional namespaces.) Processes reference Unix domain sockets as file system [inodes](https://en.wikipedia.org/wiki/Inode), so two processes can communicate by opening the same socket.

In addition to sending data, processes may send [file descriptors](https://en.wikipedia.org/wiki/File_descriptor) across a Unix domain socket connection using the `sendmsg()` and `recvmsg()` system calls. This allows the sending processes to grant the receiving process access to a file descriptor for which the receiving process otherwise does not have access.[[2\]](https://en.wikipedia.org/wiki/Unix_domain_socket#cite_note-neohapsis-2)[[3\]](https://en.wikipedia.org/wiki/Unix_domain_socket#cite_note-linux-cmsg-man-page-3) This can be used to implement a rudimentary form of [capability-based security](https://en.wikipedia.org/wiki/Capability-based_security).[[4\]](https://en.wikipedia.org/wiki/Unix_domain_socket#cite_note-wheeler-secure-linux-howto-4)


### [Berkeley Sockets](https://en.wikipedia.org/wiki/Berkeley_sockets), POSIX Sockets & BSD Sockets
**Berkeley sockets** is an application programming interface for [Internet sockets](https://en.wikipedia.org/wiki/Internet_socket) and [Unix domain sockets](https://en.wikipedia.org/wiki/Unix_domain_socket), used for [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) (IPC). It is commonly implemented as a [library](https://en.wikipedia.org/wiki/Library_(computing)) of linkable modules. It originated with the [4.2BSD Unix](https://en.wikipedia.org/wiki/History_of_the_Berkeley_Software_Distribution#4BSD) operating system, which was released in 1983.

A [socket](https://en.wikipedia.org/wiki/Network_socket) is an abstract representation ([handle](https://en.wikipedia.org/wiki/Handle_(computing))) for the local endpoint of a network communication path. The Berkeley sockets API represents it as a [file descriptor](https://en.wikipedia.org/wiki/File_descriptor) ([file handle](https://en.wikipedia.org/wiki/File_handle)) in the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) that provides a common interface for input and output to [streams](https://en.wikipedia.org/wiki/Standard_streams) of data.

Berkeley sockets evolved with little modification from a [*de facto* standard](https://en.wikipedia.org/wiki/De_facto_standard) into a component of the [POSIX](https://en.wikipedia.org/wiki/POSIX) specification. The term **POSIX sockets** is essentially synonymous with *Berkeley sockets*, but they are also known as **BSD sockets**, acknowledging the first implementation in the [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution).

#### 🔗 Other IPC Machanism ..
> ⛳ Go to  [IPC](../../../../../🥷🏼%20Operating%20System%20(Tech)/Linux%20(UNIX%20Family)/🔩%20Linux%20Kernel/Process%20Management%20&%20Scheduling/IPC/IPC.md) for more info on this section.
**[Pipeline](https://en.wikipedia.org/wiki/Pipeline_(Unix))**

![img](../../../../../../../../Assets/Pics/280px-Pipeline.svg.png)



**[Netlink](https://en.wikipedia.org/wiki/Netlink)**
The **Netlink** [socket](https://en.wikipedia.org/wiki/Network_socket) family is a [Linux kernel interface](https://en.wikipedia.org/wiki/Linux_kernel_interface) used for [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) (IPC) between both the kernel and [userspace](https://en.wikipedia.org/wiki/Userspace) processes, and between different userspace processes, in a way similar to the [Unix domain sockets](https://en.wikipedia.org/wiki/Unix_domain_socket). Similarly to the [Unix domain sockets](https://en.wikipedia.org/wiki/Unix_domain_sockets), and unlike [INET sockets](https://en.wikipedia.org/wiki/Network_socket), Netlink communication cannot traverse host boundaries. However, while the Unix domain sockets use the [file system](https://en.wikipedia.org/wiki/File_system) namespace, Netlink sockets are usually addressed by [process identifiers](https://en.wikipedia.org/wiki/Process_identifier) (PIDs).[[3\]](https://en.wikipedia.org/wiki/Netlink#cite_note-3)



## Refs

[Unix domain socket 简介]: https://www.cnblogs.com/sparkdev/p/8359028.html

