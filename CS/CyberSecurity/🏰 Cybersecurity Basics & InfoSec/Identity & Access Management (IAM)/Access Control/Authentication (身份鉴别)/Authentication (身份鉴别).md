# Authentication (身份鉴别)

[TOC]



## Res
↗ [Message Authentication (报文鉴别，消息鉴别)](../../../../🚬%20Cryptology/Message%20Authentication%20(报文鉴别，消息鉴别)/Message%20Authentication%20(报文鉴别，消息鉴别).md)



## Intro
### Overview
#### Authentication in General
> 🔗 https://en.wikipedia.org/wiki/Authentication
>
> Conceptions easy to get confused:
> authentication, authorization, access control, identification;
> authentication, verification, certification,

Authentication is relevant to multiple fields. In 🎨[art](https://en.wikipedia.org/wiki/Art), 🩻[antiques](https://en.wikipedia.org/wiki/Antique), and 🐒[anthropology](https://en.wikipedia.org/wiki/Anthropology), a common problem is verifying that a given artifact was produced by a certain person or in a certain place or period of history. In 🖥️[computer science](https://en.wikipedia.org/wiki/Computer_science), verifying a user's identity is often required to allow access to confidential data or systems.

#### ⭐ Authentication in CS /Information Systems
The property that ensures that the identity of a subject or resource is the one claimed. Authenticity applies to entities such as users, processes, systems and information.
- 鉴别就是确认实体是它所声明的
- 鉴别是最重要的安全服务之一。鉴别服务提供了关于某个实体身份的保证。（所有其它的安全服务都依赖于该服务）
- 鉴别可以对抗假冒攻击的危险

The context here specifically applies to **authentication in Computer Science**, which is also mostly implemented as **access control**.

> 🔗 [Access Control | wikipedia](https://en.wikipedia.org/wiki/Access_control)

In the field of access control, there are three major aspects:
- Physical Security
- Computer Security
- Telecommunication Security

![](../../../../../../Assets/Pics/Screenshot%202023-06-05%20at%209.30.57%20PM.png)

![](../../../../../../Assets/Pics/Screenshot%202023-11-01%20at%204.07.54PM.png)

与其它机制的关系
- 访问控制：作为访问控制服务的一种必要支持，访问控制服务的执行依赖于确知的身份（访问控制服务直接对达到机密性、完整性、可用性及合法使用目标提供支持）；
- 数据完整性：作为提供数据起源鉴别的一种可能方法（当它与数据完整性机制结合起来使用时）；
- 审计机制：作为对责任原则的一种直接支持，例如，在审计追踪过程中做记录时，提供与某一活动相联系的确知身份。

### Authentication Roles /Entity
身份鉴别的相关实体
(1)申请者/声称者(Claimant)，出示身份信息的实体，又称作示证者(Prover)，提出某种认证请求; 
(2)验证者V(Verifier)，检验申请者提供的认证信息的正确性和合法性，决定是否满足其认证要求;
(3)攻击者，可以窃听和伪装申请者，骗取验证者 的信任。
(4)鉴别系统在必要时会有第三方，即可信赖者( 可信第三方，TP「Trusted Thired Party」)参与仲裁。
![](../../../../../../Assets/Pics/Screenshot%202023-11-06%20at%208.40.24AM.png)

### Authentication Taxonomy
广义上来说，鉴别广泛应用在不限于网络空间安全领域的各个领域，比如艺术品真赝的鉴别，字迹的鉴别，等等。从这个广义的角度来说，按照鉴别对象分类标准分类，鉴别可以分为如下结构：
1. 基于客观存在物的鉴别
	1. 面对人的鉴别（身份鉴别，网安讨论的范围）
		1. 基于密码学原理
			1. 基于对称密码算法（不同于对称鉴别）
			2. 基于公钥密码算法
			3. 基于密码校验函数算法
		2. 基于非密码学原理
			1.  基于你所知道的（**What you know** ）
				1. 知识、口令、密码
			2. 基于你所拥有的（**What you have** ）
				1. 身份证、信用卡、钥匙、智能卡、令牌等
			3. 基于你的个人特征（**What you are**）
				1. 指纹，笔迹，声音，手型，脸型，视网膜，虹膜
		3. ZKP
	2. 面对机器的鉴别
	3. 面对物品的鉴别
2. 基于主观存在物的鉴别
	1. tbd..

---
身份鉴别可以是**单向**的也可以是**双向**的。
- 所谓**单向鉴别**是指通信双方中只有一方鉴别另一方，而双向鉴别是指通信双方相互鉴别。在单向身份鉴别中，一个实体充当声称者;另一个实体充当验证者。
- 对于**双向身份鉴别**，每个实体同时充当声称者和验证者。双向鉴别可在两个方向上使用相同或不同的鉴别机制。
- **第三方鉴别**：由可信第三方来确认身份

依据鉴别信息是否共享进行分类，鉴别可分为**对称鉴别**和**非对称鉴别**。
- **对称鉴别**方法的例子有:口令和使用对称密码技术加密的质询。
- **非对称鉴别**方法的例子有:使用非对称密码技术和在不暴露任何信息情况下对信息所有者的信息进行验证的技术。

依据鉴别过程是否采用密码技术，鉴别分为使用密码技术的鉴别和使用非密码技术的鉴别。
- **使用密码技术的鉴别**: 对称的、非对称的或混合的密码技术，可用于提供鉴别信息的完整性保护和鉴别信息的机密性保护。使用密码技术的身份鉴别技术实例包括使用加密来保护传输期间的口令。
- **使用非密码技术的鉴别**: 非密码技术的身份鉴别技术包括使用口令或质询-响应表。
	- 基于你所知道的（**What you know** ）
		- 知识、口令、密码
	- 基于你所拥有的（**What you have** ）
		- 身份证、信用卡、钥匙、智能卡、令牌等
	- 基于你的（生物）特征（**What you are**）
		- 指纹，笔迹，声音，手型，脸型，视网膜，虹膜
	- 双因素、多因素认证
- **零知识证明协议**

本地鉴别和远程鉴别
- **本地鉴别**：实体在本地环境的初始化鉴别
- **远程鉴别**：连接远程设备的实体鉴别

### Requirements for Authentication Systems
(1) 验证者正确鉴别合法申请者的概率极大化。
(2) 不具可传递性(Transferability)，验证者B不可能重用申请者A提供给他的信息来伪装申请者A，而成功地骗取其他人的验证，从而得到信任。
(3) 攻击者伪装申请者欺骗验证者成功的概率要小到可以忽略的程度，能抗击已知密文攻击，即能对抗攻击者截获到申请者和验证者的多次通信密文，然后伪装申请者欺骗验证者。
(4) 计算有效性，为实现身份鉴别所需的计算量要小。
(5) 通信有效性，为实现身份鉴别所需通信次数和数据量要小。
(6) 秘密参数能安全存储
(7) 相互鉴别(按需)。
(8) 可信第三方的实时参与(按需)。

网络环境下对身份鉴别的要求
- 唯一的身份标识（ID）
- 抗被动的威胁（窃听），口令不在网上明码传输
- 抵抗主动的威胁，比如阻断、伪造、重放,网络上传输的鉴别信息不可重用

### Authentication Protocols
身份鉴别协议：通信参与者为完成相互的身份鉴别或识别而采用的规程、约定、约束和交换信息的总和。



## 🎯 Authentication Factors
> ⚠ This entry applies to authentication in general terms, including **product authentication** and **art authentication** and also, **digital authentication**. 

How someone may be authenticated fall into three categories, based on what is known as the **factors of authentication**: 
- something the 1️⃣ user **knows**, 
- something the 2️⃣ user **has**,
- something the 3️⃣ user **is**. 

Each **authentication factor** covers a range of elements used to authenticate or verify a person's identity before being granted access, approving a transaction request, signing a document or other work product, granting authority to others, and establishing a chain of authority.

Security research has determined that for a **positive authentication**, elements from at least two, and preferably all three, factors should be verified. The three factors (classes) and some of the elements of each factor are:
- the **knowledge factors**: Something the user **knows** (e.g., a [password](https://en.wikipedia.org/wiki/Password), [partial password](https://en.wikipedia.org/wiki/Partial_password), [passphrase](https://en.wikipedia.org/wiki/Pass_phrase), [personal identification number](https://en.wikipedia.org/wiki/Personal_identification_number) (PIN), [challenge–response](https://en.wikipedia.org/wiki/Challenge–response) (the user must answer a question or pattern), [security question](https://en.wikipedia.org/wiki/Security_question)).
- the **ownership factors**: Something the user **has** (e.g., wristband, [ID card](https://en.wikipedia.org/wiki/ID_card), [security token](https://en.wikipedia.org/wiki/Security_token), [implanted device](https://en.wikipedia.org/wiki/Microchip_implant_(human)), [cell phone](https://en.wikipedia.org/wiki/Cell_phone) with a built-in [hardware token](https://en.wikipedia.org/wiki/Hardware_token), [software token](https://en.wikipedia.org/wiki/Software_token), or [cell phone](https://en.wikipedia.org/wiki/Cell_phone) holding a [software token](https://en.wikipedia.org/wiki/Software_token)).
- the **inherence factors**: Something the user **is or does** (e.g., [fingerprint](https://en.wikipedia.org/wiki/Fingerprint), [retinal](https://en.wikipedia.org/wiki/Retina) pattern, [DNA](https://en.wikipedia.org/wiki/DNA) sequence (there are assorted definitions of what is sufficient), [signature](https://en.wikipedia.org/wiki/Signature), face, voice, unique bio-electric signals, or other [biometric](https://en.wikipedia.org/wiki/Biometric) identifiers).

### Single-factor Authentication
As the weakest level of authentication, only a single component from one of the three categories of factors is used to authenticate an individual's identity. The use of only one factor does not offer much protection from misuse or malicious intrusion. This type of authentication is not recommended for financial or personally relevant transactions that warrant a higher level of security

### Multi-factor Authentication
> 🔗 [Multi-factor authentication](https://en.wikipedia.org/wiki/Multi-factor_authentication) 

Multi-factor authentication involves two or more authentication factors (*something you know*, *something you have*, or *something you are*). Two-factor authentication is a special case of multi-factor authentication involving exactly two factors



## 🎯 Authentication Taxonomy
### 1️⃣ 按保护等级分类
#### 0级鉴别（无保护）

#### 1级鉴别（抗泄露保护）

#### 2级鉴别（抗泄露和对不同验证者重放的保护）

#### 3级鉴别（抗泄露和对同一验证者重放的保护）

#### 4级鉴别（抗泄露和对相同/不同验证者重放的保护）

### 2️⃣ 按机制的配置分类
#### 涉及可信第三方的模型
##### 阶段模型
##### 使用初始化信息知识的模型
#### 介入鉴别的可信第三方之间的关系
##### 联机可信第三方
##### 脱机可信第三方

### 3️⃣ 按鉴别对象分类
#### 🧊 Object-based Authentication
##### 🤦🏻‍♀️ Human-Oriented Authentication
↗ [Human-Oriented Authentication (鉴别对象为人)](Object-Based%20Authetication/Human-Oriented%20Authentication%20(鉴别对象为人)/Human-Oriented%20Authentication%20(鉴别对象为人).md)

##### 📻 Machine-oriented Authentication
↗ [Machine-Oriented Authentication (鉴别对象为机器)](Object-Based%20Authetication/Machine-Oriented%20Authentication%20(鉴别对象为机器)/Machine-Oriented%20Authentication%20(鉴别对象为机器).md)

##### ✏️ Thing-oriented Authentication

> 这里的“物”与前面的“机”从物理实体上看没有本质区别，但对“物“的认证更需要强调轻量级属性。在物联网环境中，“物”意味着终端感知节点或RFID标签，这些“物”的资源有限，因此，不能使用传统的针对“机”的认证方法。
>
> 考虑到资源有限的“物”通常所传递的数据量也很有限，因此，对物的认证其实是对数据来源的认证，即一个数据无论经过多少转发，其原始来源应该可以得到鉴别。

↗ [Thing-Oriented Authentication (鉴别对象为物)](Object-Based%20Authetication/Thing-Oriented%20Authentication%20(鉴别对象为物)/Thing-Oriented%20Authentication%20(鉴别对象为物).md)

#### Message Authentication
↗ [Message Authentication (报文鉴别，消息鉴别)](../../../../🚬%20Cryptology/Message%20Authentication%20(报文鉴别，消息鉴别)/Message%20Authentication%20(报文鉴别，消息鉴别).md)


### 4️⃣ 按鉴别技术分类
#### Non-Cryptography Authentication
#### Cryptography-based Authentication
#### Zero-Knowledge-Proof (ZKP)
↗ [Zero-Knowledge Proof (ZKP)](Object-Based%20Authetication/Human-Oriented%20Authentication%20(鉴别对象为人)/Zero-Knowledge%20Proof%20(ZKP)/Zero-Knowledge%20Proof%20(ZKP).md)



## Authentication Applications
### Web Authentication Protocols
↗ [Web Authentication Technologies & Frameworks](../../../../Application%20Security/💉%20Web%20Security/📌%20Web%20Security%20Basics/Web%20Access%20Control/Web%20Authentication%20Technologies%20&%20Frameworks/Web%20Authentication%20Technologies%20&%20Frameworks.md)



## 🌅 Authentication in Secure Communication
↗ [Secure Communication & Cryptosystems /🌅 Secure Communication with CIA Properties](../../../../🚬%20Cryptology/Secure%20Communication%20&%20Cryptosystems.md#🌅%20Secure%20Communication%20with%20CIA%20Properties)



## Threats To Authentication Systems
鉴别交换协议的核心问题有两个：
- 保密性
	- 为了防止伪装和防止暴露会话密钥，基本鉴别与会话密码信息必须以保密形式通信。这就要求预先存在保密或公开密钥供实现加密使用。
- 时效性
	- 涉及防止消息重放攻击。

![](../../../../../../Assets/Pics/Screenshot%202023-06-05%20at%209.34.52%20PM.png)

### Relay Attacks
常见的消息重放攻击形式有：
- **简单重放**：攻击者简单复制一条消息，以后在重新发送它；
- **可被日志记录的复制品**：攻击者可以在一个合法有效的时间窗内重放一个带时间戳的消息；
- **不能被检测到的复制品**：这种情况可能出现，原因是原始信息已经被拦截，无法到达目的地，而只有重放的信息到达目的地。
- **反向重放，不做修改**：向消息发送者重放。当采用传统对称加密方式时，这种攻击是可能的。因为消息发送者不能简单地识别发送的消息和收到的消息在内容上的区别。
	- 针对同一验证者的重放：非重复值
	- 针对不同验证者的重放：验证者的标识符

#### Relay Attacks Countermeasures
##### Sequence Number
计数的策略：对付重放攻击的一种方法是在认证交换中使用一个序数来给每一个消息报文编号。仅当收到的消息序数顺序合法时才接受之。但这种方法的困难是要求双方必须保持上次消息的序号。

##### Time Stamp
**A**接受一个新消息仅当该消息包含一个时间戳，该时间戳在**A**看来，是足够接近**A**所知道的当前时间；这种方法要求不同参与者之间的时钟需要同步
##### Radom Value from Verifier
不可预测、不重复



## Ref
[网络安全之身份认证（转载） - 纹身的大熊猫的文章 - 知乎]: https://zhuanlan.zhihu.com/p/84993949

[信息系统访问控制的层次模型]: 中国科学院 计算机网络信息中心，北京 100190;2. 中国科学院研究生院，北京 100049) "吴开超，沈志宏，周园春，阎保平"

[secure authentication]: https://www.securecoding.com/blog/secure-authentication/
[自己动手做一个简单的 Telegram 入群验证 Bot |]: https://tstrs.me/1490.html
[用于识别、认证和验证的生物识别认证系统]: https://www.boonedam.com/zh-cn/accessories-and-additions/biometric-authentication-systems
[微信官方文档 -- 生物认证]: https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/bio-auth.html

- 小程序通过 [SOTER](https://github.com/Tencent/soter) 提供生物认证方式。
- 目前暂时只支持指纹识别认证。设备支持的生物认证方式可使用 [wx.checkIsSupportSoterAuthentication](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/soter/wx.checkIsSupportSoterAuthentication.html) 查询

[22. Anonymous Authentication（匿名认证）]: https://www.cnblogs.com/jrkl/p/13513429.html

[SAML Explained in Plain English]: https://www.onelogin.com/learn/saml
