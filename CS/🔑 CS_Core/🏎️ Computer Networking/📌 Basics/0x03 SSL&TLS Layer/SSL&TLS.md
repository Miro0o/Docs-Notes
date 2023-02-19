# SSL/TLS Layer

[TOC]



> :bulb: For the heads-up: 
>
> **SSL (Secure Sockets Layer) specifications (1994, 1995, 1996) is an already deprecated protocol.**  It was first introduced by [Netscape Communications](https://en.wikipedia.org/wiki/Netscape_Communications) for adding the HTTPS protocol to their [Navigator](https://en.wikipedia.org/wiki/Netscape_Navigator) web browser, then deprecated as the release of **Transport Layer Security** (**TLS**) 1.0 in 1999, which was built on SSL. TLS is a proposed [Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force) (IETF) standard and the current version is TLS 1.3, defined in [RFC 8446](https://tools.ietf.org/html/rfc8446), August 2018. 
>
> However SSL and TLS are still used together to refer as SSL/TLS Layer.

## Intro

### SSL

Read these to find more: 

- [Frequently Asked Questions About SSL/TLS](https://www.ssl.com/faqs/faq-what-is-ssl/#faq)
- [Keys, Certificates, and Handshakes](https://www.ssl.com/faqs/faq-what-is-ssl/#keys)
- [SSL/TLS and Secure Web Browsing](https://www.ssl.com/faqs/faq-what-is-ssl/#secure-web-browsing)
- [Obtaining an SSL/TLS Certificate](https://www.ssl.com/faqs/faq-what-is-ssl/#obtain)

Or, for a quick TL;DR introduction to SSL, just jump ahead to watch a short **[video](https://www.ssl.com/faqs/faq-what-is-ssl/#video)**.



### TLS

> :bulb: [Transport Layer Security -- WiKipedia](https://en.wikipedia.org/wiki/Transport_Layer_Security)



**Transport Layer Security** (**TLS**) is a [cryptographic protocol](https://en.wikipedia.org/wiki/Cryptographic_protocol) designed to provide communications security over a computer network. The [protocol](https://en.wikipedia.org/wiki/Communication_protocol) is widely used in applications such as [email](https://en.wikipedia.org/wiki/Email), [instant messaging](https://en.wikipedia.org/wiki/Instant_messaging), and [voice over IP](https://en.wikipedia.org/wiki/Voice_over_IP), but its use in securing [HTTPS](https://en.wikipedia.org/wiki/HTTPS) remains the most publicly visible.

The TLS protocol aims primarily to provide security, including [privacy](https://en.wikipedia.org/wiki/Privacy) (confidentiality), integrity, and authenticity through the use of [cryptography](https://en.wikipedia.org/wiki/Cryptography), such as the use of [certificates](https://en.wikipedia.org/wiki/Public_key_certificate), between two or more communicating computer applications. It runs in the [presentation layer](https://en.wikipedia.org/wiki/Presentation_layer) and is itself composed of two layers: the TLS record and the TLS [handshake protocols](https://en.wikipedia.org/wiki/Handshake_(computing)).

The closely related **Datagram Transport Layer Security** (**DTLS**) is a [communications protocol](https://en.wikipedia.org/wiki/Communications_protocol) providing [security](https://en.wikipedia.org/wiki/Communications_security) to [datagram](https://en.wikipedia.org/wiki/Datagram)-based applications. In technical writing you often you will see references to **(D)TLS** when it applies to both versions.[[1\]](https://en.wikipedia.org/wiki/Transport_Layer_Security#cite_note-1)

TLS is a proposed [Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force) (IETF) standard, first defined in 1999, and the current version is TLS 1.3, defined in August 2018. TLS builds on the now-deprecated **SSL (Secure Sockets Layer**) specifications (1994, 1995, 1996) developed by [Netscape Communications](https://en.wikipedia.org/wiki/Netscape_Communications) for adding the HTTPS protocol to their [Navigator](https://en.wikipedia.org/wiki/Netscape_Navigator) web browser.



[Transport Layer Security protocol -- Microsoft Dev Docs]: https://learn.microsoft.com/en-us/windows-server/security/tls/transport-layer-security-protocol



## Readings

[数字签名、数字证书与HTTPS是什么关系？]: https://www.freebuf.com/company-information/238820.html
[一文彻底搞懂加密、数字签名和数字证书！]: https://segmentfault.com/a/1190000024523772


