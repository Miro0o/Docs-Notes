# Cybersecurity Basics & InfoSec

[TOC]



## Res
### Related Topics
↗ [Cyber Ranges & Labs](../☠️%20Kill%20Chain/🎯%20Cyber%20Ranges%20&%20Labs/Cyber%20Ranges%20&%20Labs.md)
↗ [SEED Project](../☠️%20Kill%20Chain/🎯%20Cyber%20Ranges%20&%20Labs/🧪%20Labs/SEED%20Project/SEED%20Project.md)



## Intro
> 🔗 https://en.wikipedia.org/wiki/Information_security

**Information security**, sometimes shortened to **InfoSec**, is the practice of protecting [information](https://en.wikipedia.org/wiki/Information) by mitigating information risks.

It is part of [information risk management](https://en.wikipedia.org/wiki/Risk_management_information_systems). 

It typically involves preventing or reducing the probability of unauthorized/inappropriate access to [data](https://en.wikipedia.org/wiki/Data), or the unlawful use, [disclosure](https://en.wikipedia.org/wiki/Data_breach), disruption, deletion, corruption, modification, inspection, recording, or devaluation of information. It also involves actions intended to reduce the adverse impacts of such incidents. Protected information may take any form, e.g. electronic or physical, tangible (e.g. [paperwork](https://en.wikipedia.org/wiki/Document)) or intangible (e.g. [knowledge](https://en.wikipedia.org/wiki/Knowledge)). 

Information security's primary focus is the balanced protection of the [confidentiality](https://en.wikipedia.org/wiki/Confidentiality), [integrity](https://en.wikipedia.org/wiki/Integrity), and [availability](https://en.wikipedia.org/wiki/Availability) of data (also known as the CIA triad) while maintaining a focus on efficient [policy](https://en.wikipedia.org/wiki/Policy) implementation, all without hampering organization [productivity](https://en.wikipedia.org/wiki/Productivity). This is largely achieved through a structured [risk management](https://en.wikipedia.org/wiki/Risk_management) process that involves: 

- identifying information and related [assets](https://en.wikipedia.org/wiki/Asset_(computer_security)), plus potential [threats](https://en.wikipedia.org/wiki/Threat_(computer)), [vulnerabilities](https://en.wikipedia.org/wiki/Vulnerability_(computing)), and impacts;
- evaluating the risks;
- deciding how to address or treat the risks i.e. to avoid, mitigate, share or accept them;
- where risk mitigation is required, selecting or designing appropriate security controls and implementing them;
- monitoring the activities, making adjustments as necessary to address any issues, changes and improvement opportunities.

To standardize this discipline, academics and professionals collaborate to offer guidance, policies, and industry standards on [password](https://en.wikipedia.org/wiki/Password), [antivirus software](https://en.wikipedia.org/wiki/Antivirus_software), [firewall](https://en.wikipedia.org/wiki/Firewall_(computing)), [encryption software](https://en.wikipedia.org/wiki/Encryption_software), [legal liability](https://en.wikipedia.org/wiki/Legal_liability), [security awareness](https://en.wikipedia.org/wiki/Security_awareness) and training, and so forth. This [standardization](https://en.wikipedia.org/wiki/Standardization) may be further driven by a wide variety of laws and regulations that affect how data is accessed, processed, stored, transferred and destroyed. However, the implementation of any standards and guidance within an entity may have limited effect if a culture of [continual improvement](https://en.wikipedia.org/wiki/Continual_improvement_process) isn't adopted.


### Difference Between InfoSec & CyberSec?
最开始只有信息安全。
安全圈里的大佬们，一直觉得信息安全很重要，要从“计算机科学与技术”一级学科中独立出来，自成一级学科。怎奈，大佬们上书了数年，都以失败告终。

终于有一天，中央提出了“没有网络安全，就没有国家安全”。安全圈里的大佬们觉得机会来了。于是不申请“信息安全”一级学科，改为申请“网络空间安全”一级学科。

过审了。

“网络空间安全”就成了一级学科。招生指标更多了。

作者：吉事尚左
链接：https://www.zhihu.com/question/318261855/answer/818206085
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


### Objectives of InfoSec /What is InfoSec
> ↗ [CyberSecurity /What is Cybersecurity?](../CyberSecurity.md#What%20is%20Cybersecurity?)
> 信息安全：重点在信息资源本身的保护。

网络空间安全（应该是信息安全，但是原文如此）的最终任务是保护信息资源被合法用户安全使用，并禁止非法用户、入侵者、攻击者和黑客非法偷盗、使用信息资源。

网络空间安全（应该是信息安全，但是原文如此）的保护机制包括电磁辐射、环境安全、计算机技术、网络技术等技术因素，还包括信息安全管理（含系统安全管理、安全服务管理和安全机制管理）、法律和心理因素等机制。

国际信息系统安全认证组织（InternationalInformation Systems Security Consortium，简称ISC2）将信息安全划分为5重屏障共10大领域并给出了它们涵盖的知识结构

![](../../../Assets/Pics/Screenshot%202023-10-08%20at%209.23.41AM.png)



## 🛡️ InfoSec Principles & Objectives
↗ [Secure Communication & Cryptosystems /🤺 Threats in Secure Communication & Mechanisms](../🚬%20Cryptology/Secure%20Communication%20&%20Cryptosystems.md#🤺%20Threats%20in%20Secure%20Communication%20&%20Mechanisms)

### CIA Triad
![|400](../../../Assets/Pics/1920px-CIAJMK1209-en.svg.png)


<small>the CIA triad</small>

> The triad seems to have first been mentioned in a [NIST](https://en.wikipedia.org/wiki/NIST "NIST") publication in 1977

#### 🎯 Confidentiality
In information security, confidentiality "is the property, that information is not made available or disclosed to unauthorized individuals, entities, or processes."

#### 🎯 Integrity
数据完整性是防止非法实体对交换数据的修改、插入、替换和删除，或者如果被修改、插入、替换和删除时可以被检测出来。数据完整性可以通过消息认证模式来保证。

![](../../../Assets/Pics/Pasted%20image%2020231101161046.png)

In IT security, [data integrity](https://en.wikipedia.org/wiki/Data_integrity) means maintaining and assuring the accuracy and completeness of data over its entire lifecycle. This means that data cannot be modified in an unauthorized or undetected manner. This is not the same thing as [referential integrity](https://en.wikipedia.org/wiki/Referential_integrity) in [databases](https://en.wikipedia.org/wiki/Databases), although it can be viewed as a special case of consistency as understood in the classic [ACID](https://en.wikipedia.org/wiki/ACID) model of [transaction processing](https://en.wikipedia.org/wiki/Transaction_processing)

More broadly, integrity is an information security principle that involves human/social, process, and commercial integrity, as well as data integrity. As such it touches on aspects such as credibility, consistency, truthfulness, completeness, accuracy, timeliness, and assurance.

#### 🎯 Availability
↗ [Authentication (身份鉴别)](Identity%20&%20Access%20Management%20(IAM)/Access%20Control/Authentication%20(身份鉴别)/Authentication%20(身份鉴别).md)
↗ [Message Authentication (报文鉴别，消息鉴别)](../🚬%20Cryptology/Message%20Authentication%20(报文鉴别，消息鉴别)/Message%20Authentication%20(报文鉴别，消息鉴别).md)

For any information system to serve its purpose, the information must be [available](https://en.wikipedia.org/wiki/Availability) when it is needed.

[High availability](https://en.wikipedia.org/wiki/High_availability) systems aim to remain available at all times, preventing service disruptions due to power outages, hardware failures, and system upgrades.


### Other Security Models & Attributes
Debate continues about whether or not this CIA triad is sufficient to address rapidly changing technology and business requirements, with recommendations to consider expanding on the intersections between availability and confidentiality, as well as the relationship between **security** and **privacy**. 

- In 1992 and revised in 2002, the [OECD](https://en.wikipedia.org/wiki/OECD "OECD")'s _Guidelines for the Security of Information Systems and Networks proposed the nine generally accepted principles: [awareness](https://en.wikipedia.org/wiki/Information_security_awareness "Information security awareness"), responsibility, response, ethics, democracy, risk assessment, security design and implementation, security management, and reassessment. Building upon those, in 2004 the [NIST](https://en.wikipedia.org/wiki/NIST "NIST")'s _Engineering Principles for Information Technology Security proposed 33 principles. From each of these derived guidelines and practices.

- In 1998, [Donn Parker](https://en.wikipedia.org/wiki/Donn_Parker "Donn Parker") proposed an alternative model for the classic CIA triad that he called the [six atomic elements of information](https://en.wikipedia.org/wiki/Parkerian_Hexad "Parkerian Hexad"). The elements are [confidentiality](https://en.wikipedia.org/wiki/Confidentiality "Confidentiality"), [possession](https://en.wikipedia.org/wiki/Ownership "Ownership"), [integrity](https://en.wikipedia.org/wiki/Integrity "Integrity"), [authenticity](https://en.wikipedia.org/wiki/Authentication "Authentication"), [availability](https://en.wikipedia.org/wiki/Availability "Availability"), and [utility](https://en.wikipedia.org/wiki/Utility "Utility"). The merits of the [Parkerian Hexad](https://en.wikipedia.org/wiki/Parkerian_Hexad "Parkerian Hexad") are a subject of debate amongst security professionals.

- In 2011, [The Open Group](https://en.wikipedia.org/wiki/The_Open_Group "The Open Group") published the information security management standard [O-ISM3](https://en.wikipedia.org/wiki/Open_Information_Security_Maturity_Model "Open Information Security Maturity Model"). This standard proposed an [operational definition](https://en.wikipedia.org/wiki/Operational_definition "Operational definition") of the key concepts of security, with elements called "security objectives", related to [access control](https://en.wikipedia.org/wiki/Access_control "Access control") (9), [availability](https://en.wikipedia.org/wiki/Availability "Availability") (3), [data quality](https://en.wikipedia.org/wiki/Data_quality "Data quality") (1), compliance, and technical (4). In 2009, [DoD](https://en.wikipedia.org/wiki/DoD "DoD") [Software Protection Initiative](https://spi.dod.mil/) [Archived](https://web.archive.org/web/20160925225224/https://www.spi.dod.mil/) 2016-09-25 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine") released the [Three Tenets of Cybersecurity](https://spi.dod.mil/threat.htm) [Archived](https://web.archive.org/web/20200510012626/https://spi.dod.mil/threat.htm) 2020-05-10 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine")which are System Susceptibility, Access to the Flaw, and Capability to Exploit the Flaw. Neither of these models are widely adopted.

#### 🎯 Non-repudiation
> 抗抵赖机制旨在生成、收集、维护有关已声明的事件或动作的证据，并使该证据可得并且确认该证据，以此来解决关于此事件或动作发生或未发生而引起的争议。

In law, [non-repudiation](https://en.wikipedia.org/wiki/Non-repudiation "Non-repudiation") implies one's intention to fulfill their obligations to a contract. It also implies that one party of a transaction cannot deny having received a transaction, nor can the other party deny having sent a transaction.

It is important to note that while technology such as cryptographic systems can assist in non-repudiation efforts, **the concept is at its core a legal concept transcending the realm of technology**. It is not, for instance, sufficient to show that the message matches a digital signature signed with the sender's private key, and thus only the sender could have sent the message, and nobody else could have altered it in transit ([data integrity](https://en.wikipedia.org/wiki/Data_integrity "Data integrity")). The alleged sender could in return demonstrate that the digital signature algorithm is vulnerable or flawed, or allege or prove that his signing key has been compromised. The fault for these violations may or may not lie with the sender, and such assertions may or may not relieve the sender of liability, but the assertion would invalidate the claim that the signature necessarily proves authenticity and integrity. As such, the sender may repudiate the message (**because authenticity and integrity are pre-requisites for non-repudiation**)

#### Accountability



## Information Governance
TBD..



## Ref
[Information Security | Wikipedia]: https://en.wikipedia.org/wiki/Information_security#Further_reading
