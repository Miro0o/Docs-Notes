# HTTP

[TOC]

## Intro



### HTTP/3

:see_no_evil: What is [HTTP3](https://en.wikipedia.org/wiki/HTTP/3) ?



**HTTP/3** is the third major version of the [Hypertext Transfer Protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) used to exchange information on the [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web), alongside [HTTP/1.1](https://en.wikipedia.org/wiki/HTTP/1.1) and [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2). HTTP/3 always runs over [QUIC](https://en.wikipedia.org/wiki/QUIC) (not the [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) of TCP/IP, which QUIC is a replacement for), which *is* completed (and is the heart of HTTP/3), published as [RFC](https://en.wikipedia.org/wiki/RFC_(identifier)) [9000](https://datatracker.ietf.org/doc/html/rfc9000).[[1\]](https://en.wikipedia.org/wiki/HTTP/3#cite_note-1)[[2\]](https://en.wikipedia.org/wiki/HTTP/3#cite_note-2)



[![img](../../../../../Assets/Pics/336px-HTTP-1.1_vs._HTTP-2_vs._HTTP-3_Protocol_Stack.svg.png)](https://en.wikipedia.org/wiki/File:HTTP-1.1_vs._HTTP-2_vs._HTTP-3_Protocol_Stack.svg)

Protocol Stack of HTTP/3 compared to HTTP/1.1 and HTTP/2



HTTP/3 uses the same semantics as the earlier revisions, including the same [request methods](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods), [status codes](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Response_status_codes), and [message fields](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields), but encodes them differently and maintains session state differently.

As of May 2022, the HTTP/3 protocol is an [Internet Draft](https://en.wikipedia.org/wiki/Internet_Draft) awaiting final author review before publication (one of three already approved).[[3\]](https://en.wikipedia.org/wiki/HTTP/3#cite_note-3) HTTP/3 is already supported by 73% of running web browsers,[[4\]](https://en.wikipedia.org/wiki/HTTP/3#cite_note-canIuse-4) and according to W3Techs 25% of the top 10 million websites.[[5\]](https://en.wikipedia.org/wiki/HTTP/3#cite_note-W3Techs-5) It has been supported by [Chromium](https://en.wikipedia.org/wiki/Chromium_(web_browser)) (including [Google Chrome](https://en.wikipedia.org/wiki/Google_Chrome), [Microsoft Edge](https://en.wikipedia.org/wiki/Microsoft_Edge), [Samsung Internet](https://en.wikipedia.org/wiki/Samsung_Internet), and [Opera](https://en.wikipedia.org/wiki/Opera_(web_browser)) which are based on it, and Chrome for Android)[[6\]](https://en.wikipedia.org/wiki/HTTP/3#cite_note-6) since April 2020 and by [Mozilla Firefox](https://en.wikipedia.org/wiki/Mozilla_Firefox) since May 2021.[[4\]](https://en.wikipedia.org/wiki/HTTP/3#cite_note-canIuse-4)[[7\]](https://en.wikipedia.org/wiki/HTTP/3#cite_note-:2-7) [Safari](https://en.wikipedia.org/wiki/Safari_(web_browser)) 14 (on [macOS Big Sur](https://en.wikipedia.org/wiki/MacOS_Big_Sur) and [iOS 14](https://en.wikipedia.org/wiki/IOS_14)) has also implemented the protocol but it is [disabled by default](https://en.wikipedia.org/wiki/Feature_toggle).[[8\]](https://en.wikipedia.org/wiki/HTTP/3#cite_note-safari14-8)

