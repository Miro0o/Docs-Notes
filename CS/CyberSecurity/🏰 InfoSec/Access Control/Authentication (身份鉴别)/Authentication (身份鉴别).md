# Authentication (身份鉴别)

[TOC]



## Res



## Intro

> 🔗 https://en.wikipedia.org/wiki/Authentication
>
> Conceptions easy to get confused:
> authentication, authorization, access control, identification;
> authentication, verification, certification,

Authentication is relevant to multiple fields. In 🎨[art](https://en.wikipedia.org/wiki/Art), 🩻[antiques](https://en.wikipedia.org/wiki/Antique), and 🐒[anthropology](https://en.wikipedia.org/wiki/Anthropology), a common problem is verifying that a given artifact was produced by a certain person or in a certain place or period of history. In 🖥️[computer science](https://en.wikipedia.org/wiki/Computer_science), verifying a user's identity is often required to allow access to confidential data or systems.

The context here specifically applies to **authentication in Computer Science**, which is also mostly implemented as **access control**.

> 🔗 [Access Control | wikipedia](https://en.wikipedia.org/wiki/Access_control)

In the field of access control, there are three major aspects:

- Physical Security
- Computer Security
- Telecommunication Security


![](../../../../../Assets/Pics/Screenshot%202023-06-05%20at%209.30.57%20PM.png)

> 鉴别就是可信地确认实体是它所声明的。


### Authentication Roles /Entity
身份鉴别的相关实体
(1)申请者(Claimant)，出示身份信息的实体，又称作示证者(Prover)，提出某种认证请求; 

(2)验证者(Verifier)，检验申请者提供的认证信息的正确性和合法性，决定是否满足其认证要求;

(3)攻击者，可以窃听和伪装申请者，骗取验证者 的信任。

(4)鉴别系统在必要时会有第三方，即可信赖者( 可信第三方)参与仲裁。


### Authentication Taxonomy
身份鉴别可以是单向的也可以是双向的。所谓单向鉴别是指通信双方中只有一方鉴别另 一方，而双向鉴别是指通信双方相互鉴别。在单向身份鉴别中，一个实体充当声称者;另一 个实体充当验证者。对于双向身份鉴别，每个实体同时充当声称者和验证者。双向鉴别可在 两个方向上使用相同或不同的鉴别机制。

依据鉴别信息是否共享进行分类，鉴别可分为对称鉴别和非对称鉴别。
- 对称鉴别方法的 例子有:口令和使用对称密码技术加密的质询。
- 非对称鉴别方法的例子有:使用非对称密码 技术和在不暴露任何信息情况下对信息所有者的信息进行验证的技术。

依据鉴别过程是否采 用密码技术，鉴别分为使用密码技术的鉴别和使用非密码技术的鉴别。
- 对称的、非对称的或混合的密码技术，可用于提供鉴别信息的完整性保护和鉴别信息的机密性保护。
- 非密码技术的身份鉴别技术包括使用口令或质询-响应表。使用密码技术的身份鉴别技术实例包括使用 加密来保护传输期间的口令。


### Requirements for Authentication Systems
(1)验证者正确鉴别合法申请者的概率极大化。

(2)不具可传递性(Transferability)，验证者B不可能重用申 请者A提供给他的信息来伪装申请者A，而成功地骗取其他人的验 证，从而得到信任。

(3)攻击者伪装申请者欺骗验证者成功的概率要小到可以忽略的 程度，能抗击已知密文攻击，即能对抗攻击者截获到申请者和验证者的多次通信密文，然后伪装申请者欺骗验证者。

(4)计算有效性，为实现身份鉴别所需的计算量要小。

(5)通信有效性，为实现身份鉴别所需通信次数和数据量要小。

(6)相互鉴别(按需)。

(7)可信第三方的实时参与(按需)。



## Authentication Factors
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



## Authentication Mathematical Principles
The authentication mechanism mainly adopts methods from modern cryptography.

↗️  [Modern Cryptography](../../🤐 Cryptography/Modern Cryptography/Modern Cryptography.md).



## 🧊 Object-based Authentication
### 🤦🏻‍♀️ Human-Oriented Authentication
↗ [Human-Oriented Authentication (鉴别对象为人)](Object-Based%20Authetication/Human-Oriented%20Authentication%20(鉴别对象为人)/Human-Oriented%20Authentication%20(鉴别对象为人).md)


### 📻 Machine-oriented Authentication
↗ [Machine-Oriented Authentication (鉴别对象为机器)](Object-Based%20Authetication/Machine-Oriented%20Authentication%20(鉴别对象为机器)/Machine-Oriented%20Authentication%20(鉴别对象为机器).md)


### ✏️ Thing-oriented Authentication

> 这里的“物”与前面的“机”从物理实体上看没有本质区别，但对“物“的认证更需要强调轻量级属性。在物联网环境中，“物”意味着终端感知节点或RFID标签，这些“物”的资源有限，因此，不能使用传统的针对“机”的认证方法。
>
> 考虑到资源有限的“物”通常所传递的数据量也很有限，因此，对物的认证其实是对数据来源的认证，即一个数据无论经过多少转发，其原始来源应该可以得到鉴别。

↗ [Thing-Oriented Authentication (鉴别对象为物)](Object-Based%20Authetication/Thing-Oriented%20Authentication%20(鉴别对象为物)/Thing-Oriented%20Authentication%20(鉴别对象为物).md)



## Authentication Applications
### Web Authentication Protocols
↗ [Web Authentication Protocols](../../../Application%20Security/💉%20Web%20Security/Access%20Control%20in%20Web/Web%20Authentication/Web%20Authentication%20Protocols/Web%20Authentication%20Protocols.md)



## Authentication in Secure Communication
![](../../../../../Assets/Pics/Screenshot%202023-06-05%20at%2010.09.26%20PM.png)

![](../../../../../Assets/Pics/Screenshot%202023-06-05%20at%2010.09.38%20PM.png)



## Attacks on Authentication Systems

![](../../../../../Assets/Pics/Screenshot%202023-06-05%20at%209.34.52%20PM.png)



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
