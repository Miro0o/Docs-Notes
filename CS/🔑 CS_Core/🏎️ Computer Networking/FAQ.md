# FAQ

[TOC]



## 👉 Network, Computer Networks, internet, the Internet, Web, and WWW?

**Network**: vertexes + edges
**Computer Networks**: end hosts + link media
**internet**: a general term referring to a computer network that is interconnected (seen as a single network that is interconnected)

**Internet**: computer networks providing services (Web services, in most cases)
**WWW = Web**: a service of computer networks providing content to every connected end host

> **Tim Berners-Lee** proposed the architecture of what became known as the **World Wide Web**. He created the first web [server](https://developer.mozilla.org/en-US/docs/Glossary/Server), web [browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser), and webpage on his computer at the CERN physics research lab in 1990. In 1991, he announced his creation on the alt.hypertext newsgroup, marking the moment the Web was first made public.
> 
> The system we know today as "the Web" consists of several components:
> - The **[HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP)** protocol governs data transfer between a server and a client.
> - To access a Web component, a client supplies a unique universal identifier, called a **[URL](https://developer.mozilla.org/en-US/docs/Glossary/URL)**(uniform resource locator) or [URI](https://developer.mozilla.org/en-US/docs/Glossary/URI) (uniform resource identifier) (formally called Universal Document Identifier (UDI)).
> - **[HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML)** (hypertext markup language) is the most common format for publishing web documents.


[World Wide Web]: https://developer.mozilla.org/en-US/docs/Glossary/World_Wide_Web




## 👉 pipelining, parallelism, concurrency
> ↗ [HTTP Connection Management](📌%20Computer%20Networking%20Basics/0x01%20Application%20Layer/Web%20(WWW)/HTTP/HTTP%20Basics/HTTP%20Connection%20Management.md)

### HTTP Pipelining
**HTTP pipelining** is a feature of **HTTP/1.1** that allows ==multiple HTTP requests to be sent over a single TCP connection== without waiting for the corresponding responses


![](../../../Assets/Pics/Pasted%20image%2020230402134909.png)

![](../../../Assets/Pics/Pasted%20image%2020230402134420.png)


[Connection management in HTTP/1.x | MDN Docs]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Connection_management_in_HTTP_1.x

[HTTP pipelining | Wikipedia]: https://en.wikipedia.org/wiki/HTTP_pipelining

[pipelining | TechTarget]: https://www.techtarget.com/whatis/definition/pipelining

> Pipelining is the process of storing and prioritizing computer instructions that the processor executes. The pipeline is a "logical pipeline" that lets the processor perform a single instruction in multiple steps. The processing happens in a continuous, orderly, somewhat overlapped manner.

### HTTP Parallel Connection
```xml
 BrowserVersion | ConnectionsPerHostname | MaxConnections
----------------------------------------------------------
 Chrome34/32    | 6                      | 10
 IE9            | 6                      | 35
 IE10           | 8                      | 17
 IE11           | 13                     | 17
 Firefox27/26   | 6                      | 17
 Safari7.0.1    | 6                      | 17
 Android4       | 6                      | 17
 ChromeMobile18 | 6                      | 16
 IE Mobile9     | 6                      | 60
```

The first value is **_ConnectionsPerHostname_** and the second value is **_MaxConnections_**.

Source: [http://www.browserscope.org/?category=network&v=top](http://www.browserscope.org/?category=network&v=top)

Note: **_ConnectionsPerHostname_** is the maximum number of concurrent http requests that browsers will make to the same domain. To increase the number of concurrent connections, one can host resources (e.g. images) in different domains. However, you cannot exceed **_MaxConnections_**, the maximum number of connections a browser will open in total - across all domains. 

**2020 Update**;
Number of parallel connections per browser:
```xml
| Browser              | Connections per Domain         | Max Connections                |
| -------------------- | ------------------------------ | ------------------------------ |
| Chrome 81            | 6 [^note1]                     | 256[^note2]                    |
| Edge 18              | *same as Internet Explorer 11* | *same as Internet Explorer 11* |
| Firefox 68           | 9 [^note1] or 6 [^note3]       | 1000+[^note2]                  |
| Internet Explorer 11 | 12 [^note4]                    | 1000+[^note2]                  |
| Safari 13            | 6 [^note1]                     | 1000+[^note2]                  |
```

- [^note1]: tested with 72 requests, 1 domain(127.0.0.1)
- [^note2]: tested with 1002 requests, 6 requests per domain * 167 domains (127.0.0.*)
- [^note3]: when called in async context, e.g. in the callback of `setTimeout`, + `requestAnimationFrame`, `then`...
- [^note4]: of which the last 6 are follow-ups (2,4,6 available at 0.5s,1s,1.5s respectively)


[parallel HTTP connections in a browser?]: https://stackoverflow.com/questions/985431/max-parallel-http-connections-in-a-browser

[What are Max parallel HTTP connections in a browser]: https://www.tutorialspoint.com/what-are-max-parallel-http-connections-in-a-browser


### Network Concurrency
skip.

