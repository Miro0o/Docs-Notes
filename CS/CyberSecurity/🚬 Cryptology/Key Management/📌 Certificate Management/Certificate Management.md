# Public Key Certificate Management

[TOC]



## Res
### Related Topics
↗ [X.509 Public Key Certificate Standard](../📌%20Key%20Management%20Life%20Circle/🚛%20Key%20Distribution/Asymmetric%20Key%20Distribution%20(AKD)/AKD%20via%20Public%20Key%20Certificates/X.509%20Public%20Key%20Certificate%20Standard/X.509%20Public%20Key%20Certificate%20Standard.md)

↗ [PKI Scheme (Centralized)](../📌%20Key%20Management%20Life%20Circle/🚛%20Key%20Distribution/Asymmetric%20Key%20Distribution%20(AKD)/AKD%20via%20Public%20Key%20Certificates/🏦%20PKI%20Scheme%20(Centralized)/PKI%20Scheme%20(Centralized).md)
↗ [OpenSSL Project](../../../../../Network%20Security/🏇%20Network%20Security%20Basics%20&%20Protocols/🚉%20Transportation%20Layer%20Security%20Protocols/SSL%20&%20TLS%20Protocol/OpenSSL%20Project/OpenSSL%20Project.md)



## Intro



## Process in Digital Certificate Management

---
数字证书的管理包含证书的签署、发放、更新、挂起以及作废等。  

**1 数字证书的签发** 
证书机构接收、验证用户(包括下级证书机构和最终用户)数字证书的申请，将申请的内容进行备案，并根据申请的内容确定是否受理该数字证书申请。如果证书机构接受该数字证 书的申请，则需进一步确定所颁发证书的类型。新证书用证书机构的私钥签名以后，发送到 目录服务器供用户下载和查询;为了保证消息的完整性，返回给用户的所有应答信息都要使 用证书机构的签名。

由于数字证书不需要特别的安全保护，因而可以使用不安全的协议在不可信的系统和网 络上进行分发。


**2 数字证书的更新** 
证书机构可以定期更新所有用户的证书，或者根据用户请求来更新特定用户的证书。 


**3 数字证书的查询** 
证书的查询可以分为证书申请的查询和用户证书的查询。前者要求证书机构根据用户的查询请求返回申请的处理过程和结果;后者则由目录服务器根据用户的请求返回适当的证 书。


**4 数字证书的作废**
数字证书都有一定的使用期限，其使用期限是由包含在证书中的开始日期和到期日期确 定的，而有效期的长短(几个月至几年)则由证书机构的安全策略决定。

在某些特殊情况下(如对应的私钥已经失密、名字更改、主体与证书机构的关系已经改 变等)要求􏰁前作废该证书，证书机构通过周期性地发布并维护证书撤销列表(CRL， Certificate Revocation List)来完成上述功能。证书撤销列表是一个带时间戳的己作废数字证 书列表，该列表由证书机构进行签名处理，供证书的使用者访问。该 CRL 可以发布在一个 知名的互联网站上或是在该证书机构自己的目录上进行分发。每份被撤销的证书在 CRL 上 以其证书序列号进行标识。一个系统在使用一个经过认证的公钥前，不仅需要检查证书的签 名和有效期，还要查询最新的 CRL 以确认该证书的序列号不在其中。因此，只有同时满足 以下三个条件的证书才是有效的证书，即 CA 的签名有效，证书在有效期内，并且未被列入 到CRL中。

---



## Digital Certification Verification

---
**序列号验证**
检查证书中签名实体序列号是否与签发者证书的序列号一致。

**有效期验证**
检查日期是否有效、合法:
1. 用户证书的有效期和私钥有效期是否在CA证书的有效期内。 否则交易是不安全的。
2. 用户证书的有效期中的起始时间应在CA证书的私钥有效期内。否则证书是不安全的。

**证书作废列表查询**
“黑名单查询”，向证书 库查询证书吊销列表。

**证书使用策略的认证**
证书用途:
主机、用户、加密、签名 验证......

**证书真实性的认证**
验证证书的CA数字签名有 效性(基于证书CA的验证 公钥)

**证书链的认证**
所谓证书链的认证是想通过证 书链追溯到可信赖的CA的根

**证书持有人的确认**
基于“三趟消息”机制

----


## Ref

