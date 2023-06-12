# RPC

[TOC]



## Res
RPC is an implementation of ↗ [IPC (Inter Process Communication)](../../../../🧬%20Computer%20System/Operating%20System%20(Theory)/Processes%20Management%20(CPU%20+%20Main%20Memory%20Resource)/IPC%20(Inter%20Process%20Communication)/IPC%20(Inter%20Process%20Communication).md).

↗ [SE / Middleware /RPC](../../../../../Software%20Engineering/🖖🏾%20Middleware/RPC/RPC.md)
↗ [Cloud Native /RPC](../../../../../🌁%20Cloud%20Native/🥋%20Orchestration%20&%20Management/RPC/RPC.md)




## Intro
> 🔗 https://en.wikipedia.org/wiki/Remote_procedure_call

In [distributed computing](https://en.wikipedia.org/wiki/Distributed_computing "Distributed computing"), a **remote procedure call** (**RPC**) is when a computer program causes a procedure (subroutine) to execute in a different [address space](https://en.wikipedia.org/wiki/Address_space "Address space") (commonly on another computer on a shared network), which is written as if it were a normal (local) procedure call, without the programmer explicitly writing the details for the remote interaction. That is, the programmer writes essentially the same code whether the subroutine is local to the executing program, or remote. 
- This is a form of client–server interaction (caller is client, executor is server), typically implemented via a **request–response message-passing system**. 
- In the object-oriented programming paradigm, RPCs are represented by **remote method invocation (RMI)**. 
- The RPC model implies a level of **location transparency**, namely that calling procedures are largely the same whether they are local or remote, but usually, they are not identical, so local calls can be distinguished from remote calls. Remote calls are usually orders of magnitude slower and less reliable than local calls, so distinguishing them is important.

RPCs are a form of inter-process communication (IPC), in that different processes have different address spaces: if on the same host machine, they have distinct virtual address spaces, even though the physical address space is the same; while if they are on different hosts, the physical address space is different. Many different (often incompatible) technologies have been used to implement the concept.


### Sequence of events 
1. The client calls the client [stub](https://en.wikipedia.org/wiki/Stub_(distributed_computing) "Stub (distributed computing)"). The call is a local procedure call, with parameters pushed on to the stack in the normal way.
2. The [client stub](https://en.wikipedia.org/wiki/Class_stub "Class stub") packs the parameters into a message and makes a system call to send the message. Packing the parameters is called [marshalling](https://en.wikipedia.org/wiki/Marshalling_(computer_science) "Marshalling (computer science)").
3. The client's local [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system") sends the message from the client machine to the server machine.
4. The local [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system") on the server machine passes the incoming packets to the [server stub](https://en.wikipedia.org/wiki/Class_skeleton "Class skeleton").
5. The server stub unpacks the parameters from the message. Unpacking the parameters is called [unmarshalling](https://en.wikipedia.org/wiki/Unmarshalling "Unmarshalling").
6. Finally, the server stub calls the server procedure. The reply traces the same steps in the reverse direction.


### Standard contact mechanisms
To let different clients access servers, a number of standardized RPC systems have been created. Most of these use an [interface description language](https://en.wikipedia.org/wiki/Interface_description_language "Interface description language") (IDL) to let various platforms call the RPC. The IDL files can then be used to generate code to interface between the client and servers.

> For more at ↗ [IDL](IDL/IDL.md)



## Ref

