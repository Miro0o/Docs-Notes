# Cryptology

[TOC]



## Res
📖 应用密码学
[密码学入门](https://learnku.com/docs/cryptography)



## Categories of Cryptology 

> 密码学主要包括密码编码学(Cryptography)和密码分析学(Cryptoanalysis)两个分支。
> 
> 密码编码学的主要任务是寻求有效密码算法和协议，以保证信息的机密性或认证性的方法。
> 它主要研究密码算法 的构造与设计，也就是密码体制的构造。它是密码理论的基础，也是保密系统设计的基础。
> 
> 密码分析学的主要任务是研究加密信息的破译或认证信息的伪造。
> 它主要是对密码信息的解析方法进行研究。例如， 试图通过分析密文获取对方的真正明文。密码分析是检验密码体制安全性最为直接的手段，只有通过实 际密码分析考验的密码体制，才是真正可用的。这一点香农在几十年前就已表明:只有密码分析者才能 评判密码体制的安全性。因此，密码编码学和密码分析学是密码学的两个方面，两者既相互对立，又互 相促进和发展。


### Cryptography
👉 [Cryptography](../🏰%20InfoSec/🤐%20Cryptography/Cryptography.md)


### Cryptoanalysis
#TODO 




## Cryptology Intro
### ⭐ Cryptology's main purpose
Data Confidentiality, Data Integrity, Authentication and Non-repudiation are core principles of modern-day Cryptology.

1. **Confidentiality** refers to certain rules and guidelines usually executed under confidentiality agreements which ensure that the information is restricted to certain people or places.
2. **Data integrity** refers to maintaining and making sure that the data stays accurate and consistent over its entire life cycle.
3. **Authentication** is the process of making sure that the piece of data being claimed by the user belongs to it.
4. **Non-repudiation** refers to ability to make sure that a person or a party associated with a contract or a communication cannot deny the authenticity of their signature over their document or the sending of a message.

> Other infosec attributes:
> 
>  1. Availability
>  2. Reliability
>  3. Controllability
>  4. Accountability


### Secure Communication

![](../../../Assets/Pics/Screenshot%202023-03-01%20at%208.48.15%20PM.png)
<small>An example: asymmetric secure communication model</small>

#### Cryptosystem
通常一个密码体制可以有如下几个部分:

1. 消息空间 M(又称明文空间): 所有可能明文 m 的集合;
2. 密文空间 C: 所有可能密文 c 的集合;
3. 密钥空间 K: 所有可能密钥k的集合，其中每一密钥k由加密密钥ke和解密密钥kd组成，即k=(ke，kd);
4. 加密算法 E: 一簇由加密密钥控制的、从 M 到 C 的加密变换;
5. 解密算法 D: 一簇由解密密钥控制的、从 C 到 M 的解密变换。

五元组 $$\{ M，C，K，E，D \}$$就称为一个密码系统。在密码系统中，对于每一个确定的密钥k，加密
算法将确定一个具体的加密变换，解密算法将确定一个具体的解密变换，而且解密变换就是加密变换的 逆变换。对于明文空间M中的每一个明文m，加密算法E在加密密钥ke的控制下将明文m加密成密文c; 而解密算法D则在密钥kd的控制下将密文c解密成同一明文m，即:

对 $$m∈M，(ke，kd)∈K，$$有 $$D_kd (Eke (m))=m。$$


#### Measurement of Cryptosystem's Security 
##### 密码系统的安全性
一个密码系统的安全性主要与两个方面的因素有关。

1. **密码算法本身**的安全强度

密码算法的安全强度取决于密码设计水平、破译技术等。可以说一个密码系统所使用密码算法的安全强度是 该系统安全性的技术保证。

2. 密码系统的管理或使用中的漏洞 （**密码算法外**的不安全因素）

另外一个方面就是密码算法之外的不安全因素。因为即使一个密码算法能够达到足够高的安全强度，但攻击者却有可能通过其他非技术手段(例如用社会工程手段收买相关密钥管理人员)攻破一个密码系统。这些不安全因素来自于密码系统的管理或使用中的漏洞。

> 因此，密码算法的保密强度并不等价于密码系统整体的安全性。一个密码系统必须同时完善技术与管理要求，才能保证整个密码系统的安全。本教材仅讨论影响一个密码系统安全性的技术因素，即密码 算法本身。

##### 密码系统安全性的评估
1. 无条件安全性

这种评价方法考虑的是假定攻击者拥有无限的计算资源，但仍然无法破译该密码系统。按照信息论的观点就是，攻击者观察密文前后明文的不确定性相等，也即攻击者通过观察密文不会得到任何有助于破译密码系统的信息。这种密码系统就是理论上不可破译的，或者称该密码体制具有完善保密性(Perfect Secrecy )或无条件安全性。

> 1918 年，AT&T 工程师 Gilbert Vernam 发明的**一次一密(OTP)密码方案**是最早被人们认识的无条件安全的密码体制。这种密码系统使用与消息一样长的随机密钥，且密钥使用永不重复，由于它产生不带有与明文有任何统计关系的随机输出，这种方案如果被正确使用，就是理论上不可破译的密码系统。但这一方案虽然安全性能卓越，但实际上不实用，因为其密钥生成十分困难，密钥不能重复使用，密钥管理成为一个非常艰难的问题，完全的一次一密密码体制往往只具有理论上的意义。

2. 可证明安全性
这种方法是将密码系统的安全性归结为某个经过深入研究的数学难题(如大整数素因子分解、计算 离散对数等)，数学难题被证明求解困难。这种评估方法存在的问题是它只说明了这个密码方法的安全 性与某个困难问题相关，没有完全证明问题本身的安全性，并给出它们的等价性证明。

3. 计算安全性
计算安全性又称为实际安全性，这种评价方法是指使用目前最好的方法攻破该密码系统所需要的计 算远远超出攻击者的计算资源水平，则可以定义这个密码系统是安全的。

🎤 综上，一个密码系统要达到实际安全性，就要满足以下准则:  
1. 破译该密码系统的实际计算量(包括计算时间或费用)十分巨大，以致于在实际上是无法实现的;
2. 破译该密码系统所需要的计算时间超过被加密信息有用的生命周期。例如，战争中发起战斗攻击的作战命令只需要在战斗打响前需要保密;重要新闻消息在公开报道前需要保密的时间往往也只有几个小时;
3. 破译该密码系统的费用超过被加密信息本身的价值;

如果一个密码系统能够满足以上准则之一，就可以认为是满足实际安全性的。对于实际应用中的密码系统而言，由于至少存在一种破译方法，即强力攻击法，因此都不能满足无条件安全性，只提供计算安全性。


#### Design Principles of Cryptosystem
Kerckhoffs principle

> 🔗 https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle#Explanation_of_the_principle


#### Types of Cryptosystem
##### Key Specific 根据密码算法所用的密钥数量
对称密码体制(Symmetric cipher，也称为单钥密码体制、秘密密钥密码体制、 对称密钥密码体制或常规密码体制)

非对称密码体制(Asymmetric cipher，也称为双钥密码体制、公开密钥密码体制、非对称密钥密码体制)

> 由于非对称密码体制的安全性一般是依赖于某个公认的数学难题，普遍认为其安全性没有对称密码 体制高。


##### Encryption Specific 根据对明文信息的处理方式
分组密码(Block cipher)

序列密码(Stream cipher，也称为流密码)

##### Reversable Specific 根据是否能进行可逆的加密变换
单向函数密码体制

双向变换密码体制

##### Other cutting-edge Cryptosystems ...
Identity-Based Encryption, IBE
Attribute-Based Encryption, ABE
Functional Encryption, FE
Full Homomorphic Encryption, FHE
Deniable Encryption


### Cryptology Application


### Cryptology Laws


## Ref
[密码学与计算机网络安全、信息安全与密码学、解决区块链隐私问题的密码学]: https://blog.csdn.net/dujuancao11/article/details/109138506
[密码学与信息安全]: https://juejin.cn/s/密码学与信息安全
[现代密码学概述]: https://blog.csdn.net/qq_51524329/article/details/121542115
[密码学系列之二：密码学基本概念]: https://blog.csdn.net/apr15/article/details/125055333

