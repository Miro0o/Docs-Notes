# QUIC ( Quick Udp Internet Connection )

[TOC]



## Res
🏠 https://quicwg.org

QUIC belongs to  [The Chromium Projects](https://www.chromium.org/)



## QUIC, a multiplexed transport over UDP
![QUIC-Badge-Dark-RGB-Horiz](../../../../../../Assets/Pics/QUIC-Badge-Dark-RGB-Horiz.png)

QUIC is a new multiplexed transport built on top of UDP. HTTP/3 is designed to take advantage of QUIC's features, including lack of Head-Of-Line blocking between streams.

The QUIC project started as **an alternative to TCP+TLS+HTTP/2**, with the goal of improving user experience, particularly page load times. The [**QUIC working group**](https://datatracker.ietf.org/wg/quic/about/) at the IETF defined a clear boundary between the transport([QUIC](https://datatracker.ietf.org/doc/html/rfc9000)) and application(HTTP/3) layers, as well as migrating from QUIC Crypto to [TLS 1.3](https://datatracker.ietf.org/doc/html/rfc8446).

Because TCP is implemented in operating system kernels and middleboxes, widely deploying significant changes to TCP is next to impossible. However, since QUIC is built on top of UDP and the transport functionality is encrypted, it suffers from no such limitations.

*Key features of QUIC and HTTP/3 over TCP+TLS and HTTP/2 include**
- Reduced connection establishment time - 0 round trips in the common case
- Improved congestion control feedback
- Multiplexing without head of line blocking
- Connection migration
- Transport extensibility
- Optional unreliable delivery

The [IETF](https://www.ietf.org/) QUIC Working Group produced QUIC version 1 — **a UDP-based, stream-multiplexing, encrypted transport protocol**. The protocol itself is published as [RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html), and there are other related RFCs of note, see below.

We are now [chartered](https://datatracker.ietf.org/wg/quic/about/) to be the focal point for any QUIC-related work in the IETF. Our work covers maintenance and evolution of published specifications, the deployability of QUIC, and new extensions to QUIC.

The QUIC Working Group originated HTTP/3, the mapping of HTTP to QUIC, and the QPACK header compression scheme. These are now maintained by the [HTTP Working Group](https://httpwg.org/).

<small>* See our [contribution guidelines](https://github.com/quicwg/base-drafts/blob/master/CONTRIBUTING.md) if you want to work with us.</small>



## Refs
[The Road to QUIC]: https://blog.cloudflare.com/the-road-to-quic/
[科普：QUIC协议原理分析 - 腾讯技术工程的文章 - 知乎]: https://zhuanlan.zhihu.com/p/32553477
[让互联网更快的协议，QUIC在腾讯的实践及性能优化 - 腾讯技术工程的文章 - 知乎]: https://zhuanlan.zhihu.com/p/32560981

