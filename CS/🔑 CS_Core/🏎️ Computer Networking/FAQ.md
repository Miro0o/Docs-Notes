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
> ↗ [HTTP Connection Management](📌%20Computer%20Networking%20Basics/0x01%20Application%20Layer/🔥%20Web%20(WWW)/HTTP/HTTP%20Basics/HTTP%20Connection%20Management.md)

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



## 中国四大骨干网和三大网运营商是什么关系？

中国四大骨干网（中国科技网、[中国公用计算机互联网](https://www.zhihu.com/search?q=%E4%B8%AD%E5%9B%BD%E5%85%AC%E7%94%A8%E8%AE%A1%E7%AE%97%E6%9C%BA%E4%BA%92%E8%81%94%E7%BD%91&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A93743561%7D)、[中国教育和科研计算机网](https://www.zhihu.com/search?q=%E4%B8%AD%E5%9B%BD%E6%95%99%E8%82%B2%E5%92%8C%E7%A7%91%E7%A0%94%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A93743561%7D)、中国金桥信息网）和三大网运营商（电信，移动，联通）是什么关系？是电信移动联通投资组建了四大骨干网，还是四大骨干网租给三大运营商使用？还是怎么的？

电信运营“中国公用计算机互联网”(CHINANET)，它原属邮电部，邮电部撤销后改由中国电信经营。

另两个运营商都有自建网络。移动有专门的“中国移动互联网”(CMNET)，联通也有自己的“中国联通计算机互联网”(UNINET)，[网通](https://www.zhihu.com/search?q=%E7%BD%91%E9%80%9A&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A93743561%7D)也有自己的“中国网通公用互联网”(CNCNET)，不过因为现在网通是联通的子公司所以也可以说是由联通经营。

其他的几个网络和三大运营商没关系，比如“中国教育和科研计算机网”(CERNET)是由教育部管理的，“中国金桥信息网”(CHINAGBN)是由信息产业部管理的，“中国科技网”(CSTNET)是由中国科学院管理的。


那中国教育和科研计算机网、金桥信息网、科技网三个是不是不对个人用户开放使用，他们怎么赢利，还是只靠政府财政维持?

金桥网同公网一样是经营性的，对个人用户开放。科技网连接全国科研机构。[教育网](https://www.zhihu.com/search?q=%E6%95%99%E8%82%B2%E7%BD%91&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A93743561%7D)连接全国高校，如果你是大学生的话，你在学校就是用的教育网。盈利方式同公网一样，通过对接入者收费。如果盈利不足财政肯定会支持的嘛，因为科技网和教育网本身就是非营利性的网络。

中国宽带互联网（CHINANET）与公用电话交换网（PSTN）、[公用数字数据网](https://www.zhihu.com/search?q=%E5%85%AC%E7%94%A8%E6%95%B0%E5%AD%97%E6%95%B0%E6%8D%AE%E7%BD%91&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A93743561%7D)（CHINADDN）、[公用分组交换网](https://www.zhihu.com/search?q=%E5%85%AC%E7%94%A8%E5%88%86%E7%BB%84%E4%BA%A4%E6%8D%A2%E7%BD%91&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A93743561%7D)（CHINAPAC）、公用帧中继（CHINAFR）等所有电信基础网络实现了互联，可以为客户提供多种不同的接入方式。同时，中国宽带互联网（CHINANET）通过与国内各大互联网络运营商以及科研、教育网络实现了互联互通，并且与国际主要互联网服务运营商实现了对等合作，用户接入中国宽带互联网（CHINANET），可以使用CHINANET和INTERNET所有业务。

作者：技术小事  
链接：https://www.zhihu.com/question/40826300/answer/93743561  
来源：知乎  
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。  

