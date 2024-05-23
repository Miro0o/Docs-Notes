# Cryptology

[TOC]



## Res
> 🎉 More resources can be found at ↗ [Cryptography](🤐%20Cryptography/Cryptography.md) & ↗ [Cryptanalysis](🤮%20Cryptanalysis/Cryptanalysis.md)

### Tutorials / Books
📖 应用密码学：协议、算法与C源程序（原书第2版）
📖 图解密码技术:第3版/ (日)结城浩著

👍 [Learnku - 密码学入门](https://learnku.com/docs/cryptography)

### Learn in Action
🇬🇧 [Cracking Codes with Python](https://inventwithpython.com/cracking/)
🇨🇳 [Python 密码破解指南](https://github.com/apachecn/invent-with-python-zh/tree/master/docs/cracking)

### School Projects
https://github.com/0v3rW4tch/Cryptography-course-design/tree/master
> CUMT密码学课程设计源代码
> 
> 代码可能不是特别完善，还有可能存在其他的没有考虑周全的地方，请多多谅解
> A5.py ---------------> A5加解密
> RC4加解密.py-----------------> RC4加解密
> DES_destruct----------->DES加解密的S盒，P盒等结构
> DES加解密文件.py ---------->DES核心算法
> DigitalSignature.py----------->数字签名
> messageCheck.py --------------->消息认证
> mymd5 .py     -------------------> Hash算法
> myRSA.py ------------------------> RSA加解密

https://github.com/wsxk/hust_crypto_design
> 华中科技大学 19级密码学课程设计
> 
> PKCS7
> RSA 参数计算
> SPN增强
> SPN实现
> CRT
> 差分分析
> 彩虹表
> 模重复平方
> 线性分析

👍 https://github.com/KangweiiLiu/UCAS_courses
> 中国科学院大学网安-计算机相关课程资源，高级人工智能，深度学习，应用密码学，机器学习，信息隐藏，信息论与编码，多媒体编码等
> 

https://github.com/szluyu99/Encryption-And-Decryption-By-Yu
> 自制的密码学综合工具，综合了对称加密算法DES，AES，IDEA，公开加密算法RSA，ECC，散列算法MD5，SHA1，CRC32，以及RSA，DSA，ECDSA数字签名验证。

https://github.com/ThuWangzw/RSA
> 2020清华大学软件学院应用密码学大作业 --- RSA

### ⚖️ Laws & Legislations
https://www.oscca.gov.cn/sca/xxgk/2023-06/04/content_1057225.shtml
中华人民共和国密码法 （2020.1.1）

https://www.oscca.gov.cn/sca/xxgk/2023-10/07/content_1061109.shtml
《商用密码应用安全性评估管理办法》已经2023年9月11日国家密码管理局局务会议审议通过，现予公布，自2023年11月1日起施行。



## Intro
Information security uses [cryptography](https://en.wikipedia.org/wiki/Cryptography) to transform usable information into a form that renders it unusable by anyone other than an authorized user; this process is called [encryption](https://en.wikipedia.org/wiki/Encryption).

> 密码学是一门关于通信安全的学科，主要研究如何保护信息的机密性、完整性和可用性。在密码学中，通常使用加密算法和解密算法来实现对信息的保护。
> 
> 信息安全是保护计算机系统和网络中的信息免受未经授权的访问、使用、泄露、破坏和干扰的一种技术、政策和管理措施的总称。信息安全包括密码学、网络安全、物理安全、应用程序安全、数据安全等多个方面。
> 在现代社会中，信息安全已经成为一个非常重要的领域。无论是政府、军队、企业还是个人，都需要保护自己的信息安全。例如，企业需要保护客户的个人数据，政府需要保护机密信息，个人需要保护自己的隐私和财产安全。
> 
> 密码学是实现信息安全的重要手段之一。通过使用密码学技术，可以保护信息的机密性和完整性，从而防止信息被未经授权的访问、泄露和篡改。常见的密码学技术包括对称加密、非对称加密和哈希函数等。


### ⭐ Objective of Cryptology
> Refer back to principles of ↗ [Cybersecurity Basics & InfoSec /🛡️ InfoSec Principles & Objectives](../🏰%20Cybersecurity%20Basics%20&%20InfoSec/Cybersecurity%20Basics%20&%20InfoSec.md#🛡️%20InfoSec%20Principles%20&%20Objectives) for more info.

Data Confidentiality, Data Integrity, Authentication and Non-repudiation are core principles of modern-day Cryptology.

1. **Confidentiality (机密性)** refers to certain rules and guidelines usually executed under confidentiality agreements which ensure that the information is restricted to certain people or places. ==(Encryption)==
2. **Data integrity (完整性)** refers to maintaining and making sure that the data stays accurate and consistent over its entire life cycle. ==(Encryption, Communication Channel)==
3. **Authentication (真实性)** is the process of making sure that the piece of data being claimed by the user belongs to it. ==(Message Authentication)==
4. **Non-repudiation (不可抵赖性)** refers to ability to make sure that a person or a party associated with a contract or a communication cannot deny the authenticity of their signature over their document or the sending of a message. ==(Message Authentication)==

> Other infosec attributes includes:
>  1. Availability
>  2. Reliability
>  3. Controllability
>  4. Accountability


### Categories of Cryptology 
#### Cryptography
> 密码编码学的主要任务是寻求有效密码算法和协议，以保证信息的机密性或认证性的方法。它主要研究密码算法 的构造与设计，也就是密码体制的构造。它是密码理论的基础，也是保密系统设计的基础。

↗ [Cryptography](🤐%20Cryptography/Cryptography.md)

#### Cryptanalysis
> 密码分析学的主要任务是研究加密信息的破译或认证信息的伪造。
> 它主要是对密码信息的解析方法进行研究。例如， 试图通过分析密文获取对方的真正明文。密码分析是检验密码体制安全性最为直接的手段，只有通过实 际密码分析考验的密码体制，才是真正可用的。这一点香农在几十年前就已表明:只有密码分析者才能 评判密码体制的安全性。因此，密码编码学和密码分析学是密码学的两个方面，两者既相互对立，又互 相促进和发展。

↗ [Cryptanalysis](🤮%20Cryptanalysis/Cryptanalysis.md)


### ⭐️ History of Information & Communication Systems | Secure Communication (保密通讯)

↗ [History of Information Systems & Security Systems](../History%20of%20Information%20Systems%20&%20Security%20Systems.md)
↗ [Secure Communication & Cryptosystems](Secure%20Communication%20&%20Cryptosystems.md)



## Cryptographic Software
![](../../../Assets/Pics/Screenshot%202024-04-26%20at%203.28.56%20PM.png)
<small>https://en.wikipedia.org/wiki/Encryption_software</small>



## Ref
[密码学与计算机网络安全、信息安全与密码学、解决区块链隐私问题的密码学]: https://blog.csdn.net/dujuancao11/article/details/109138506

[密码学与信息安全]: https://juejin.cn/s/密码学与信息安全
[现代密码学概述]: https://blog.csdn.net/qq_51524329/article/details/121542115
[密码学系列之二：密码学基本概念]: https://blog.csdn.net/apr15/article/details/125055333
[1.6 密码系统的安全性（二）]: https://learnku.com/docs/cryptography/16-security-of-cryptographic-system-2/8922

[🤔 关于密评，这10个问题你一定要知道！]: http://www.lingpan.cn/newsinfo/1183029.html

[👍 密码学最好的课程是什么？ - 知乎]: https://www.zhihu.com/question/390212555
直接上干货，个人觉得不用看别的了
1. https://www.coursera.org/learn/cryptography
2. https://www.coursera.org/learn/crypto
3. https://www.youtube.com/playlist?list=PL6ogFv-ieghe8MOIcpD6UDtdK-UMHG8oH
