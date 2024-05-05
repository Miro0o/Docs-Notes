# Remote Procedure Call (RPC)

[TOC]



## Res
### Related Topics
↗ [Procedure & Function Call](../../../../../🛣️%20Program%20Execution%20&%20Compilation%20System/🧙🏿‍♀️%20Execution%20(Runtime)/Procedure%20&%20Function%20Call/Procedure%20&%20Function%20Call.md)
↗ [Local Procedure Call (LPC)](../../../OS%20Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource)/IPC%20(Inter%20Process%20Communication)/🧦%20Sockets/🌉%20Internal%20Sockets/Local%20Procedure%20Call%20(LPC).md)



## Intro
> 🔗 https://www.cnblogs.com/yunnotes/archive/2013/04/19/3032535.html

在传统的编程概念中，过程（procedure）是由程序员在本地编译完成，并只能局限在本地运行的一段代码，即其主程序和过程之间的运行关系是本地调用关系，这种结构在网络日益发展的今天已无法适应实际需求。众所周知，传统过程调用模式无法充分利用网络上其他主机的资源（如CPU、Memory等），也无法提高代码在实体间的共享程度，使得主机资源大量浪费。RPC很好地解决了传统过程所存在的一系列弊端。通过RPC可以充分利用非共享内存的多处理器环境（例如通过局域网连接得多台工作站）,这样可以简便地将应用分布在多台工作站上，应用程序就像运行在一个多处理器的计算机上一样，因此可以方便的实现过程代码共享，提高系统资源的利用率，也可以将以大量数值处理的操作放在处理能力较强的系统上运行，从而减轻前端机的负担。

RPC其实也是种C/S的编程模式，其工作过程大致包含以下几个步骤：
1. 服务器启动，它向所在主机上的端口映射器（port mapper）注册自身。客户然后启动，它调用clnt_create，该函数则与服务器主机上的端口映射器联系，以找到服务器的临时端口。clnt_create函数还建立一个与服务器的TCP连接。
2. 客户调用一个称为客户端存根（Client stub）的本地过程（存根由rpcgen工具生成）。对于客户来说，客户程序存根看起来像是它想要调用的真正的服务器过程。存根的目的在于把待传递给远程过程的参数打包，可能的话把它们转换成某种标准格式，然后构造一个或多个网络消息。把客户提供的参数打包成一个网络消息的过程称为集结（marshaling）。客户程序的各个例程和存根通常调用RPC运行时函数库中的函数。
3. 这些网络消息由客户程序存根发给远程系统。通常需要一次陷入本地内核的系统调用（例如write或是sendto）。
4. 这些消息传送到远程系统，通常使用TCP或UDP协议。
5. 一个服务器存根（server stub）过程一直在远程系统上等待客户的请求。它从这些网络消息中解散（unmarshaling）出参数。
6. 服务器程序存根执行一个本地过程调用以激活真正的服务器函数，传递给该函数的参数是它从来自客户的网络消息中解散出来的。
7. 当服务器过程完成时，它向服务器程序存根返回其返回值。
8. 服务器存根在必要时对返回值作转换，然后把它们集结到一个或多个网络消息中，以便发送回客户
9. 这些消息通过网络传送回客户。
10. 客户程序存根从本地内核中读出这些网络消息（如read或recvfrom）。
11. 对返回值进行可能的转换后，客户程序存根最终返回客户函数。



## Ref
[SUN RPC简介 | cnblog]: https://www.cnblogs.com/yunnotes/archive/2013/04/19/3032535.html
