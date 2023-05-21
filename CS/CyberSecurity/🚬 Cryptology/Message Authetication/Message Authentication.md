# Message Authetication

[TOC]



## Res
↗ [Access Contorl /Authentication (身份认证)](../../🏰%20InfoSec/Access%20Control/Authentication%20(身份认证)/Authentication%20(身份认证).md)



## Intro
Recall the objective of cryptology:

> Data Confidentiality, Data Integrity, Authentication and Non-repudiation are core principles of modern-day Cryptology.
> 
> 1. **Confidentiality** refers to certain rules and guidelines usually executed under confidentiality agreements which ensure that the information is restricted to certain people or places. ==(Encryption)==
> 2. **Data integrity** refers to maintaining and making sure that the data stays accurate and consistent over its entire life cycle. ==(Encryption, Communicatin Channel)==
> 3. **Authentication** is the process of making sure that the piece of data being claimed by the user belongs to it. ==(Message Authentication)==
> 4. **Non-repudiation** refers to ability to make sure that a person or a party associated with a contract or a communication cannot deny the authenticity of their signature over their document or the sending of a message. ==(Message Authentication)==


在消息传递的过程中，需要考虑两个方面问题:
- 一方面，为了可以抵抗窃听等**被动攻击**，需要对传输的消息进行**加密保护**;
- 另一方面，就是使用消息鉴别来防止攻击者对系统进行**主动攻击**，如伪造、篡改消息等。消息鉴别是一个过程，用以验证接收消息的**真实性**(的确是由它所声称的实体发来的)和**完整性**(未被篡改、插入、删除)，同时还用于验证消息的**顺序性和时间性**(未被重排、重放、延迟等)。 

除此之外，在考虑信息安全时还需考虑业务的**不可否认性**，也称**抗抵赖性**，即防止通信双方中的某一方对所传输消息的否认或抵赖。实现消息的不可否认性可采用数字签名，数字签名也是一种鉴别技术，它 可用于对抗主动攻击。消息鉴别对于开放的网络中的各种信息系统的安全性具有重要作用。



## 1️⃣ Symmetric Key Based Message Authetication
↗ [Symmetric Cipher](🤐%20Cryptography/Modern%20Cryptography/Symmetric%20Cipher/Symmetric%20Cipher.md)




## 2️⃣ Asymmetric Key Based Message Authentication
↗ [Asymmetric Cipher](🤐%20Cryptography/Modern%20Cryptography/Asymmetric%20Cipher/Asymmetric%20Cipher.md)



## 3️⃣ Message Digest Based Message Authentication
↗ [Message Digest & Hash Function](🤐%20Cryptography/Modern%20Cryptography/Message%20Digest%20&%20Hash%20Function/Message%20Digest%20&%20Hash%20Function.md)
↗ [Digital Signiture](Digital%20Signiture/Digital%20Signiture.md)


### MAC (Message Authentication Code)


### MD-based Message Authentication
![](../../../../Assets/Pics/Screenshot%202023-05-10%20at%202.46.31%20PM.png)

![](../../../../Assets/Pics/Screenshot%202023-05-10%20at%202.46.41%20PM.png)

![](../../../../Assets/Pics/Screenshot%202023-05-10%20at%202.46.54%20PM.png)


### HMAC
早期构造消息鉴别码(MAC)的方法常常是使用分组密码的CBC模式，即基于分组密码的构造方法。 而构造消息鉴别码(MAC)的另一类方法是基于散列函数的构造方法。这类方法的好处是散列算法(如 MD5、SHA-1等)的软件实现快于分组密码的软件实现，函数的库代码来源广泛、限制较少。基于散列函数的消息鉴别码构造的基本思想就是将某个散列函数嵌入到消息鉴别码的构造过程中。

HMAC作为这种构造方法的代表，已经作为[RFC2104]公布，并在IPSec和其他网络协议(如SSL)中得到应用。

#### HMAC Design Principles


#### HMAC Algorithm
![](../../../../Assets/Pics/Screenshot%202023-05-10%20at%202.47.15%20PM.png)


![](../../../../Assets/Pics/Screenshot%202023-05-10%20at%202.47.30%20PM.png)


#### HMAC Security Analysis
由HMAC的结构可以发现，其安全性依赖于所嵌入散列函数的安全性。对HMAC的攻击等价于对内 嵌散列函数的下列攻击之一:
(1)攻击者能够计算压缩函数的一个输出，即使IV是机密的或者随机的。 
(2)攻击者能够找到散列函数的碰撞，即使IV是机密的或者随机的。

第一种攻击可以认为压缩函数与散列函数等价，n 位的初始链接变量IV可以看作HMAC的密钥。因此攻击可以通过对密钥的穷举来进行攻击。对密钥穷举的计算复杂度为O(2n)。

第二种攻击要求寻找两个具有相同散列值的消息，即实施生日攻击，对于具有 n 位长散列值的散列 函数而言，其计算复杂度为 O(2n/2)。例如，对于散列值长度为 128 位的散列函数，第二种攻击的复杂度 为 O(264)，按照现有技术这是可能的。但是这不影响将该散列函数用于 HMAC。因为攻击者对散列函 数实施生日攻击时，由于已经知道算法和缺省 IV 值，因此在选择消息集合后可以离线地寻找碰撞。但 是在攻击 HMAC 时，由于攻击者不知道密钥 K，从而不能离线产生消息和散列码对。所以攻击者必须 监听并得到 HMAC 在同一密钥下产生的一系列消息，并对得到的消息序列进行攻击。对于长度为 128 位的散列值来说，要求得到同一密钥下产生的 264 个分组(273 位)。在 1Gbit/s 的链路上这大约需要 25 万年。因此就速度和安全性而言，采用该散列函数或者计算复杂度更高的散列函数嵌入到 HMAC 中是可以接受的。



## Ref

