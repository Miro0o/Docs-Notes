# Kerberos

[TOC]



## Res
📂 [Kerberos: The Network Authentication Protocol | MIT](https://web.mit.edu/kerberos/)



## Intro
![](../../../../../../../../Assets/Pics/kerberos.sml.png)

**Kerberos** ([/ˈkɜːrbərɒs/](https://en.wikipedia.org/wiki/Help:IPA/English "Help:IPA/English")) is a computer-network authentication protocol that works on the basis of **tickets** to allow nodes communicating over a non-secure network to prove their identity to one another in a secure manner. Its designers aimed it primarily at a **client–server** model, and it provides **mutual authentication** — both the user and the server verify each other's identity. Kerberos protocol messages are protected against [eavesdropping](https://en.wikipedia.org/wiki/Computer_insecurity#Eavesdropping "Computer insecurity") and [replay attacks](https://en.wikipedia.org/wiki/Replay_attack "Replay attack").

Kerberos builds on **symmetric-key cryptography** and requires a trusted third party, and optionally may use **public-key cryptography** during certain phases of authentication. Kerberos uses UDP port 88 by default.

The protocol was named after the character _[Kerberos](https://en.wikipedia.org/wiki/Cerberus "Cerberus")_ (or _[Cerberus](https://en.wikipedia.org/wiki/Cerberus "Cerberus")_) from Greek mythology, the ferocious three-headed guard dog of [Hades](https://en.wikipedia.org/wiki/Hades "Hades").

### Kerberos Features
优点
- 单点登录，只要用户拿到了**TGT**并且该**TGT**没有过期，就可以使用该**TGT**通过**TGS**完成到任一个服务器的鉴别而不必重新输入密码
- 与授权机制相结合
- 支持双向的身份鉴别通过交换“跨域密钥”实现分布式网 络环境下的鉴别

缺点
- **AS**和**TGS**是集中式管理，容易形成瓶颈，系统的性能和安全也严重依赖于**AS**和**TGS**的性能和安全
- 时钟同步问题
- 身份鉴别采用的是对称加密机制，随用户数量增加，密钥管理较复杂



## Ref
[Kerberos (protocol) | Wikipedia]: https://en.wikipedia.org/wiki/Kerberos_(protocol)

[Kerberos | GeeksforGeeks]: https://www.geeksforgeeks.org/kerberos/