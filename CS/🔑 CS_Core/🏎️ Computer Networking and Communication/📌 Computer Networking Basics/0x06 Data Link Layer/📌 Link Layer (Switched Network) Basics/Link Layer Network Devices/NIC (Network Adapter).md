# NIC (Network Adapter)

[TOC]



## Res
【深入浅出计算机网络 微课视频】 https://www.bilibili.com/video/BV1NT411g7n6/?p=27&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

↗ [MAC (Media Access Control) Protocol](../📌%20MAC%20(Media%20Access%20Control)%20Protocol/MAC%20(Media%20Access%20Control)%20Protocol.md)



## Intro
> 🖇 https://www.cnblogs.com/machangwei-8/p/10352887.html

1. What is [NIC](https://zh.wikipedia.org/zh-cn/网卡) (Network Interface Controller)?
   The NIC may use one or more of the following techniques to indicate the availability of packets to transfer:

   - [Polling](https://en.wikipedia.org/wiki/Polling_(computer_science)) is where the [CPU](https://en.wikipedia.org/wiki/CPU) examines the status of the [peripheral](https://en.wikipedia.org/wiki/Peripheral) under program control.
   - [Interrupt](https://en.wikipedia.org/wiki/Interrupt_request)-driven I/O is where the peripheral alerts the CPU that it is ready to transfer data.

2. NICs may use one or more of the following techniques to transfer packet data:
- [Programmed input/output](https://en.wikipedia.org/wiki/Programmed_input/output), where the CPU moves the data to or from the NIC to memory.
- [Direct memory access](https://en.wikipedia.org/wiki/Direct_memory_access) (DMA), where a device other than the CPU assumes control of the [system bus](https://en.wikipedia.org/wiki/System_bus) to move data to or from the NIC to memory. This removes load from the CPU but requires more logic on the card. In addition, a packet buffer on the NIC may not be required and [latency](https://en.wikipedia.org/wiki/Latency_(engineering)) can be reduced.



## Ref

