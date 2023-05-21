# Symmetric Cipher

[TOC]



## Res
↗ [Symmetric Cipher Cryptanalysis](../../../🤮%20Cryptanalysis/Modern%20Cipher%20Cryptanalysis/Symmetric%20Cipher%20Cryptanalysis/Symmetric%20Cipher%20Cryptanalysis.md)



## Intro



## Drawbacks of Symmetric Cipher
对称密码体制不能完全适应应用的需要，主要表现在以下三方面:

1. **密钥管理的困难性问题**
对称密码体制中，任何两个用户间要进行保密通信就需要一个密钥，不同用户间进行保 密通信时必须使用不同的密钥;密钥为发送方和接收方所共享，用于消息的加密和解密。在 一个有 n 个用户的保密通信网络中，用户彼此间进行保密通信就需要 n(n-1)/2 个密钥。当 网络中用户数量增加时，密钥的数量将急剧增大。如当 n=100 时，需要 4950 个密钥;而 n =500 时，需要 124750个密钥。

2. **系统的开放性问题**
电子商务等网络应用提出了互不认识的网络用户间进行秘密通信问题，而对称密码体制的密钥分发方法要求密钥共享各方互相信任，因此它不能解决陌生人间的密钥传递问题，也就不能支持陌生人间的保密通信。

3. **数字签名问题**
对称密码体制难以从机制上提供数字签名功能，也就不能实现通信中的抗抵赖需求。

正是对称密码体制存在上述的局限性，促使人们产生了建立新的密码体制的愿望。公钥 密码体制又称为非对称密码体制，或双密钥密码体制，其思想在 1976 年由 W.Diffie 和 M . E. Hellman 在其开创性的论文“密码学新方向”’中首先提出来的。

↗ [Asymmetric Cipher](../Asymmetric%20Cipher/Asymmetric%20Cipher.md)



## Ref

