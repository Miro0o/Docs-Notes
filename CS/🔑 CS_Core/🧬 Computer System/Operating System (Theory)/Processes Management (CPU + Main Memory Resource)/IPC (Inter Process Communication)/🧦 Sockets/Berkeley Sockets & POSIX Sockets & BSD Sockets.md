# Berkeley Sockets & POSIX Sockets & BSD Sockets

[TOC]



## Res
### Related Topics
↗ [Network Programming & RPC](../../../../../🏎️%20Computer%20Networking%20and%20Communication/🎅🏼%20Network%20Programming%20&%20RPC/Network%20Programming%20&%20RPC.md)

↗ [Internet Domain Socket](../../../IO%20System/IO%20Generality%20(via%20Abstraction)/🛜%20Network%20Sockets%20&%20RPC/Internet%20Domain%20Socket.md)
- ↗ [Internet Domain Socket Programming](../../../../../🏎️%20Computer%20Networking%20and%20Communication/🎅🏼%20Network%20Programming%20&%20RPC/Internet%20Domain%20Socket%20Programming/Internet%20Domain%20Socket%20Programming.md)
↗ [UNIX Domain Sockets (POSIX)](🌉%20Internal%20Sockets%20&%20LPC/UNIX%20Domain%20Sockets%20(POSIX).md)



## Intro
**Berkeley sockets** is an application programming interface for [Internet sockets](https://en.wikipedia.org/wiki/Internet_socket) and [Unix domain sockets](https://en.wikipedia.org/wiki/Unix_domain_socket), used for [inter-process communication](https://en.wikipedia.org/wiki/Inter-process_communication) (IPC). It is commonly implemented as a [library](https://en.wikipedia.org/wiki/Library_(computing)) of linkable modules. It originated with the [4.2BSD Unix](https://en.wikipedia.org/wiki/History_of_the_Berkeley_Software_Distribution#4BSD) operating system, which was released in 1983.

A [socket](https://en.wikipedia.org/wiki/Network_socket) is an abstract representation ([handle](https://en.wikipedia.org/wiki/Handle_(computing))) for the local endpoint of a network communication path. The Berkeley sockets API represents it as a [file descriptor](https://en.wikipedia.org/wiki/File_descriptor) ([file handle](https://en.wikipedia.org/wiki/File_handle)) in the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) that provides a common interface for input and output to [streams](https://en.wikipedia.org/wiki/Standard_streams) of data.

Berkeley sockets evolved with little modification from a [*de facto* standard](https://en.wikipedia.org/wiki/De_facto_standard) into a component of the [POSIX](https://en.wikipedia.org/wiki/POSIX) specification. The term **POSIX sockets** is essentially synonymous with **Berkeley sockets**, but they are also known as **BSD sockets**, acknowledging the first implementation in the [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution).



## Ref

