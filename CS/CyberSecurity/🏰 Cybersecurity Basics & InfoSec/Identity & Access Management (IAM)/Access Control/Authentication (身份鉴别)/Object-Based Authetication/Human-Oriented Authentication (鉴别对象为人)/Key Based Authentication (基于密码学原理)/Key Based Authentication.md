# Key Based Authentication

[TOC]



## Res



## Intro



## 1️⃣ Asymmetric Key Based Authentication
### Certification Based Authentication (基于证书)
Generally, for certificate-based authentication, the system will generate a digital certificate to validate the user. It can be generated from the user’s unique Id like voter ID, passport, or other. It contains the user’s public key and digital signature, with this system will identify the right user, A system takes a digital sign from a user and uses cryptography to make sure it’s a valid user. 



## 2️⃣ Symmetric Key Based Authentication
基于对称密码算法的鉴别依靠一定协议下的数据加密处理。通信双方共享一个密钥（通常存储在硬件中），该密钥在质询—应答协议中处理或加密信息交换。

### Token Based Authentication (基于令牌)
Token-based authentication is a process in which users identify with unique tokens after the user provides credentials to the system. A token is valid only for a designated time period, after that user needs to re-generate it to use again. 

> ⚠ **Diff between certification & token**
>
> Tokens are essentially symmetric keys. That means that the same key has to be both on the client and the server to be able to authenticate users.
>
> Certificates use an asymmetric set of keys. Certificates are based on public-key cryptography. The client keeps possession of the private, which is never shared by anyone else.
>
> In Web Security, instead of just signing a ‘challenge’, the client signs the entirety of the message that’s sent by the server.



## 3️⃣ Message Digest Based Authentication
- 在该机制中，待鉴别的实体通过表明它拥有某个秘密鉴别密钥来证实其身份。可由该实体以其秘密密钥和特定数据作输入，使用密码校验函数获得密码校验值来达到。
- 声称者和验证者共享秘密鉴别密钥，应仅为该两个实体所知，以及他们的信任方。



## Ref

