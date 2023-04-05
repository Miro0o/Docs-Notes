# Digital Singature

[TOC]

## Intro

> 🔗 Digest from [Wikipedia](https://en.wikipedia.org/wiki/Digital_signature).

A **digital signature** is a mathematical scheme for verifying the authenticity of digital messages or documents. A valid digital signature, where the prerequisites are satisfied, gives a recipient very high confidence that the message was created by a known sender ([authenticity](https://en.wikipedia.org/wiki/Authentication)), and that the message was not altered in transit ([integrity](https://en.wikipedia.org/wiki/Data_integrity)).

Digital signatures are a standard element of most [cryptographic protocol](https://en.wikipedia.org/wiki/Cryptographic_protocol) suites, and are commonly used for software distribution, financial transactions, [contract management software](https://en.wikipedia.org/wiki/Contract_management_software), and in other cases where it is important to detect forgery or [tampering](https://en.wikipedia.org/wiki/Tampering_(crime)).

Digital signatures are often used to implement [electronic signatures](https://en.wikipedia.org/wiki/Electronic_signature), which includes any electronic data that carries the intent of a signature, but not all electronic signatures use digital signatures. Electronic signatures have legal significance in some countries, including [Canada](https://en.wikipedia.org/wiki/Canada), [South Africa](https://en.wikipedia.org/wiki/South_Africa), the [United States](https://en.wikipedia.org/wiki/United_States), [Algeria](https://en.wikipedia.org/wiki/Algeria), [Turkey](https://en.wikipedia.org/wiki/Turkey), [India](https://en.wikipedia.org/wiki/India), [Brazil](https://en.wikipedia.org/wiki/Brazil), [Indonesia](https://en.wikipedia.org/wiki/Indonesia), [Mexico](https://en.wikipedia.org/wiki/Mexico), [Saudi Arabia](https://en.wikipedia.org/wiki/Saudi_Arabia), [Uruguay](https://en.wikipedia.org/wiki/Uruguay), [Switzerland](https://en.wikipedia.org/wiki/Switzerland), [Chile](https://en.wikipedia.org/wiki/Chile) and the countries of the [European Union](https://en.wikipedia.org/wiki/European_Union).

Digital signatures employ [asymmetric cryptography](https://en.wikipedia.org/wiki/Asymmetric_key_algorithm). In many instances, they provide a layer of validation and security to messages sent through a non-secure channel: Properly implemented, a digital signature gives the receiver reason to believe the message was sent by the claimed sender. Digital signatures are equivalent to traditional handwritten signatures in many respects, but properly implemented digital signatures are more difficult to forge than the handwritten type. Digital signature schemes, in the sense used here, are cryptographically based, and must be implemented properly to be effective. They can also provide [non-repudiation](https://en.wikipedia.org/wiki/Non-repudiation), meaning that the signer cannot successfully claim they did not sign a message, while also claiming their [private key](https://en.wikipedia.org/wiki/Private_key) remains secret. Further, some non-repudiation schemes offer a timestamp for the digital signature, so that even if the private key is exposed, the signature is valid. Digitally signed messages may be anything representable as a [bitstring](https://en.wikipedia.org/wiki/Bitstring): examples include electronic mail, contracts, or a message sent via some other cryptographic protocol.



## Readings
[数字签名是什么？-- 阮一峰的日志]: https://www.ruanyifeng.com/blog/2011/08/what_is_a_digital_signature.html
[数字签名与HTTPS详解]: https://www.cnblogs.com/rinack/p/10743355.html
