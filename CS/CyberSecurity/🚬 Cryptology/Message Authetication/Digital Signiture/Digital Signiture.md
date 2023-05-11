# Digital Singature

[TOC]



## Res



## Intro

> 🔗 Digest from [Wikipedia](https://en.wikipedia.org/wiki/Digital_signature).

A **digital signature** is a mathematical scheme for verifying the authenticity of digital messages or documents. A valid digital signature, where the prerequisites are satisfied, gives a recipient very high confidence that the message was created by a known sender ([authenticity](https://en.wikipedia.org/wiki/Authentication)), and that the message was not altered in transit ([integrity](https://en.wikipedia.org/wiki/Data_integrity)).

Digital signatures are a standard element of most c**ryptographic protocol suites**, and are commonly used for software distribution, financial transactions, [contract management software](https://en.wikipedia.org/wiki/Contract_management_software), and in other cases where it is important to detect forgery or [tampering](https://en.wikipedia.org/wiki/Tampering_(crime)).

Digital signatures are often used to implement [electronic signatures](https://en.wikipedia.org/wiki/Electronic_signature), which includes any electronic data that carries the intent of a signature, but not all electronic signatures use digital signatures. Electronic signatures have legal significance in some countries, including Canada, South Africa, the United States, Algeria, Turkey, India, Brazil, Indonesia, Mexico, Saudi Arabia, Uruguay, Switzerland, Chile and the countries of the European Union.

Digital signatures employ [asymmetric cryptography](https://en.wikipedia.org/wiki/Asymmetric_key_algorithm). In many instances, they provide a layer of validation and security to messages sent through a non-secure channel: Properly implemented, a digital signature gives the receiver reason to believe the message was sent by the claimed sender. Digital signatures are equivalent to traditional handwritten signatures in many respects, but properly implemented digital signatures are more difficult to forge than the handwritten type. Digital signature schemes, in the sense used here, are cryptographically based, and must be implemented properly to be effective. They can also provide [non-repudiation](https://en.wikipedia.org/wiki/Non-repudiation), meaning that the signer cannot successfully claim they did not sign a message, while also claiming their [private key](https://en.wikipedia.org/wiki/Private_key) remains secret. Further, some non-repudiation schemes offer a timestamp for the digital signature, so that even if the private key is exposed, the signature is valid. Digitally signed messages may be anything representable as a [bitstring](https://en.wikipedia.org/wiki/Bitstring): examples include electronic mail, contracts, or a message sent via some other cryptographic protocol.


### Objective & Requirements of Digital Signiture

> 数字签名解决的是身份认证的问题。而身份认证问题的解决使得下面所述的大部分问题连带解决。

当通信双方发生下列情况时，必须解决其安全问题:
- 抵赖，发送方否认自己发送过某一文件;接收方否认自己曾接收到某一文件。
- 伪造，攻击者伪造一份文件，声称它来自发送方。  
- 冒充，网络上的某个用户冒充另一个用户接收或发送信息。  
- 篡改，攻击者对通信信息进行篡改。

一般来讲，手写签名和数字签名的主要差别在于:  
- 所签文件方面的不同。一个手写签名是所签文件的物理部分，而一个数字签名并不是所签文件的物理部分，因此所使用的数字签名算法必须设法把签名“捆绑”到所签文件上。  
- 验证方面的不同。一个手写签名是通过和一个真实的手写签名比较来验证的，这种方法很不安全，容易伪造某些人的手写签名，需要验证者有较丰富的鉴别经验。而数字签名是通过密码技术来实 现的，签名信息难以伪造，并通过一个公开的验证算法来验证，这样“任何人”都能验证一个数字签名。
- “拷贝”方面的不同。一个手写签名不易拷贝，因为一个文件的手写签名的拷贝通常容易与原文件 区别开来。而一个数字签名容易拷贝，因为一个文件的数字签名的拷贝与原文件一样，这个特点 要求阻止一个数字签名消息的重复使用和滥用。


一个完善的签名方案应满足以下三个条件:
- 签名者事后不能否认或抵赖自己的签名。  
- 其他任何人均不能伪造签名，也不能对接收或发送的信息进行篡改、伪造和冒充。  
- 若当事双方对签名真伪发生争执时，能够在公正的仲裁者面前通过验证签名来确定其真伪。

为了实现数字签名要求，当事双方应首先达成有关协议，数字签名协议中包括签名的产生、验证及 纠纷的解决方法等内容。一般来说，数字签名方案还应满足以下要求:
1. 签名是不可伪造的。除了合法的签名者外，任何其他人伪造其数字签名在计算上是不可行的，无论是通过用已有数字签名来构造新消息，还是对给定消息伪造一个数字签名。
2. 签名是不可抵赖的。签名者事后不能否认自己的签名。签名要求使用签名者的惟一秘密信息，以防止伪造和抵赖。
3. 签名是可信的。签名的识别和验证必须相对容易，任何人都可以验证签名的有效性。;
4. 签名是不可复制的。对一个消息的签名不能通过复制变为另一个消息的签名。签名与消息是一个不可分割的整体，如果对一个消息的签名是从别处复制而来，则任何人都可以发现签名与消息的不一致性，从而拒收此签名的消息。
5. 签名的消息是不可篡改的。经签名的消息是不能被篡改，否则任何人都可以发现签名与消息的不一致性，从而拒收此签名的消息。



## Digital Signiture Design Principles 
一个数字签名方案由两部分组成:带有陷门的数字签名算法(Signature Algorithm)和验证算法 (Verification Algorithm)。

归纳起来，一个数字签名方案的应用一般包括三个过程: 
1. 系统初始化过程:产生数字签名方案中用到的所有系统和用户参数，有公开的，也有秘密的
2. 签名产生过程:用户利用给定的签名算法和参数对消息产生签名，这种签名过程可以公开也可以不公开，但一定包含仅签名者才拥有的秘密信息(签名密钥)。
3. 签名验证过程:验证者利用公开的验证方法和参数对给定消息的签名进行验证，得出签名的有效性。



### Signature Algorithm


### Verification Algorithm





## Digital Signiture Execution
### Direct Execution


### Arbitration-based Execution
具有仲裁的数字签名是在通信双方的基础上引入了第三方仲裁者参与。通常的做法是所有从发送方 到接收方的签名消息首先送到仲裁者，仲裁者将消息及其数字签名进行一系列的测试，以检查其来源和 内容，并将消息加上时间戳，与已被仲裁者验证通过的数字签名一起发送给接收方。在这种方式下，仲 裁者扮演裁判的角色，起着重要作用并应取得所有的参与者的信任。

下面给出几个需要仲裁者的数字签名方案。其中 S 表示发送方，R 表示接收方，A 是仲裁者，m 是 传送的消息。

#### 对称加密，仲裁者可以看到消息内容

#### 对称加密，仲裁者不能看到消息内容

#### 公钥加密，仲裁者不能看到消息内容




## Readings
[数字签名是什么？-- 阮一峰的日志]: https://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature.html
[数字签名与HTTPS详解]: https://www.cnblogs.com/rinack/p/10743355.html
