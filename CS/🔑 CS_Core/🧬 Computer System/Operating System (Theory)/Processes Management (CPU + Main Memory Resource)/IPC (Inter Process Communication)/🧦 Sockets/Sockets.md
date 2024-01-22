# Sockets

[TOC]



## Res



## Intro



## Types of Sockets
### 1️⃣ Internal Sockets | IPC
↗ [Internal Sockets & IPC](🌉%20Internal%20Sockets%20&%20IPC/Internal%20Sockets%20&%20IPC.md)


### 2️⃣ Network Sockets (External Communication) | RPC
↗ [Network Sockets & RPC](../../../IO%20System/IO%20Generality%20(via%20Abstraction)/🛜%20Network%20Sockets%20&%20RPC/Network%20Sockets%20&%20RPC.md)

↗ [Network Programming & RPC](../../../../../🏎️%20Computer%20Networking%20and%20Communication/🎅🏼%20Network%20Programming%20&%20RPC/Network%20Programming%20&%20RPC.md)
- [Socket Programming](../../../../../🏎️%20Computer%20Networking%20and%20Communication/🎅🏼%20Network%20Programming%20&%20RPC/Socket%20Programming/Socket%20Programming.md)

↗ [Cloud Native /RPC](../../../../../../Software%20Engineering/☁️%20Cloud%20Native/Cloud%20Platform%20(System%20Level%20Engineering)/🥋%20Orchestration%20&%20Management/Remote%20Procedure%20Call%20(RPC)/Remote%20Procedure%20Call%20(RPC).md)
↗ [SE /RPC](../../../../../../Software%20Engineering/👾%20Web%20Dev%20&%20Ops/🥪%20Middleware/Remote%20Procedure%20Call%20(RPC)/Remote%20Procedure%20Call%20(RPC).md)


### [Berkeley Sockets](https://en.wikipedia.org/wiki/Berkeley_sockets), POSIX Sockets & BSD Sockets
**Berkeley sockets** is an application programming interface for [Internet sockets](https://en.wikipedia.org/wiki/Internet_socket) and [Unix domain sockets](https://en.wikipedia.org/wiki/Unix_domain_socket), used for [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) (IPC). It is commonly implemented as a [library](https://en.wikipedia.org/wiki/Library_(computing)) of linkable modules. It originated with the [4.2BSD Unix](https://en.wikipedia.org/wiki/History_of_the_Berkeley_Software_Distribution#4BSD) operating system, which was released in 1983.

A [socket](https://en.wikipedia.org/wiki/Network_socket) is an abstract representation ([handle](https://en.wikipedia.org/wiki/Handle_(computing))) for the local endpoint of a network communication path. The Berkeley sockets API represents it as a [file descriptor](https://en.wikipedia.org/wiki/File_descriptor) ([file handle](https://en.wikipedia.org/wiki/File_handle)) in the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) that provides a common interface for input and output to [streams](https://en.wikipedia.org/wiki/Standard_streams) of data.

Berkeley sockets evolved with little modification from a [*de facto* standard](https://en.wikipedia.org/wiki/De_facto_standard) into a component of the [POSIX](https://en.wikipedia.org/wiki/POSIX) specification. The term **POSIX sockets** is essentially synonymous with *Berkeley sockets*, but they are also known as **BSD sockets**, acknowledging the first implementation in the [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution).



## Ref
[UNIX Domain vs BSD vs TCP vs Internet sockets?]: https://stackoverflow.com/a/22898357/16542494
