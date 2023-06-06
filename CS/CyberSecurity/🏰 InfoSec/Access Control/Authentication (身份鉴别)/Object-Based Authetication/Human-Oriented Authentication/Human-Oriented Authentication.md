# Human-Oriented Authentication

[TOC]



## Res


## Intro
### 保证消息实时性
1、时间戳:A接受一个新消息仅当该消息包含一个时 间戳，该时间戳在A看来，是足够接近A所知道的当前 时间;这种方法要求不同参与者之间的时钟需要同步。

> 局限性： 由于变化的和不可预见的网络延迟的本性，不能期望分布式时钟保持精确的同步。因此，任何基于时间戳的过程必须采用时间窗的方式来处理:一方面时间窗应足够大以包容网络延迟， 另一方面时间窗应足够小以最大限度地减小遭受攻击 的机会。安全的时间服务器用以实现时钟同步可能是 最好的方法。


2、质询/响应方式(Challenge/Response):A期望从B 获得一个新消息，首先发给B一个随机质询值 (Challenge)，并要求后续从B收到的消息(Response) 包含正确的这个质询值(或其函数)。

>局限性： 不适应非连接性的应用，因为它要求在传输开始之前先有握手的额外销，这就抵消了无连接通信的主要特点。





## Password Based (基于口令)
Traditional password authentication is static, which is feasible to attack. That's where dynamic password authentication is adopted. 

↗ [Password Based Authentication (基于口令)](Password%20Based%20Authentication%20(基于口令)/Password%20Based%20Authentication%20(基于口令).md)



## Biometrics (生物特征提取)
↗ [Biometrics Authentication](Biometrics%20Authentication/Biometrics%20Authentication.md)



## Key Based (基于密钥)
↗ [Key Based Authentication](Key%20Based%20Authentication%20(基于密码学原理)/Key%20Based%20Authentication.md)



## Zero-Knowledge Proof (ZKP)
↗ [Zero-Knowledge Proof (ZKP)](Zero-Knowledge%20Proof%20(ZKP)/Zero-Knowledge%20Proof%20(ZKP).md)



## Anonymous Authentication



## Group Key Agreement


## 2FA /Multi-factor Authentication





## Ref

