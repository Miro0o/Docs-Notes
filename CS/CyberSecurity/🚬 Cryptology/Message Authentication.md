# Message Authetication

[TOC]



## Res



## Intro
Recall the objective of cryptology:

> Data Confidentiality, Data Integrity, Authentication and Non-repudiation are core principles of modern-day Cryptology.
> 
> 1. **Confidentiality** refers to certain rules and guidelines usually executed under confidentiality agreements which ensure that the information is restricted to certain people or places. ==(Encryption)==
> 2. **Data integrity** refers to maintaining and making sure that the data stays accurate and consistent over its entire life cycle. ==(Encryption, Communicatin Channel)==
> 3. **Authentication** is the process of making sure that the piece of data being claimed by the user belongs to it. ==(Message Authentication)==
> 4. **Non-repudiation** refers to ability to make sure that a person or a party associated with a contract or a communication cannot deny the authenticity of their signature over their document or the sending of a message. ==(Message Authentication)==


在消息传递的过程中，需要考虑两个方面问题:一方面，为了可以抵抗窃听等被动攻击，需要对传 输的消息进行加密保护;另一方面，就是使用消息鉴别来防止攻击者对系统进行主动攻击，如伪造、篡 改消息等。消息鉴别是一个过程，用以验证接收消息的真实性(的确是由它所声称的实体发来的)和完 整性(未被篡改、插入、删除)，同时还用于验证消息的顺序性和时间性(未被重排、重放、延迟等)。 除此之外，在考虑信息安全时还需考虑业务的不可否认性，也称抗抵赖性，即防止通信双方中的某一方 对所传输消息的否认或抵赖。实现消息的不可否认性可采用数字签名，数字签名也是一种鉴别技术，它 可用于对抗主动攻击。消息鉴别对于开放的网络中的各种信息系统的安全性具有重要作用。



## Symmetric Key Based Message Authetication
↗ [Symmetric Cipher](🤐%20Cryptography/Modern%20Cryptography/Symmetric%20Cipher/Symmetric%20Cipher.md)




## Asymmetric Key Based Message Authentication
↗ [Asymmetric Cipher](🤐%20Cryptography/Modern%20Cryptography/Asymmetric%20Cipher/Asymmetric%20Cipher.md)




## Message Digest Based Message Authentication
↗ [Message Digest & Hash Function](🤐%20Cryptography/Modern%20Cryptography/Message%20Digest%20&%20Hash%20Function/Message%20Digest%20&%20Hash%20Function.md)
↗ [Digital Signiture](🤐%20Cryptography/Modern%20Cryptography/Message%20Digest%20&%20Hash%20Function/Digital%20Signiture.md)





## Ref

