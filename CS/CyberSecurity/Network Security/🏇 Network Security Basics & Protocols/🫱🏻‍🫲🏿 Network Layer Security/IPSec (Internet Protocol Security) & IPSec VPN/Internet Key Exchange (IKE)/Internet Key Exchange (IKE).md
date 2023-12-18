# Internet Key Exchange (IKE)

[TOC]



## Res
### Related Topics
↗ [Key Management](../../../../../🚬%20Cryptology/Key%20Management/Key%20Management.md)
↗ [Key Exchange & Agreement](../../../../../🚬%20Cryptology/Key%20Management/📌%20Key%20Management%20Life%20Circle/👥%20Key%20Exchange%20&%20Agreement/Key%20Exchange%20&%20Agreement.md)



## Intro



## Key Exchange Principles
IPsec采用IKE完成SA 的协商，IKE通过两个阶段的协商来完成SA的建立。它遵从了ISAKMP中给出的两步式协商，采用两阶段式协商完成SA的协商。
- 第一阶段，由IKE交换的发起方发起的一个主模式（Main Mode）交换，交换的结果是建立一个名为ISAKMP SA的安全关联。这个安全关联的作用是保护为安全协议协商SA的后续通信。
- 第二阶段，在ISAKMP SA的保护之下，可由通信的任何一方发起一个快捷模式（Quick Mode）的消息交换序列，完成用于保护通信数据的IPsec SA的协商。（这种模式必须在第一阶段运行后运行，它用于定义Diffie—Hellman专用组）请参RFC2409.



## Ref

