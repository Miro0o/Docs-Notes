# FAQ

[TOC]



## 👉 Web Frontend Buzzwords
#Web #frontend 

SaaS
https://en.wikipedia.org/wiki/Software_as_a_service

https://www.cisin.com/service/saas-development-services.htm


CGI
> Ref: 万法归宗——CGI - 果冻虾仁的文章 - 知乎 https://zhuanlan.zhihu.com/p/25013398

一个请求对应一个CGI， 一个CGI 对应一个进程。
FCGI 利用一个常驻内存的进程池提高了反应效率。
Java发明的Servlet技术也是一种常驻内存的网关通信技术，只不过它采用的是多线程而非进程。


URL/URI



## 👉 YAML / JSON /XML
#Web #frontend #yaml #json #xml #config 

YAML(YAL), JSON and XML are all widely used data serialization language.

- YAML stands for “*YAML Aint Markup Language*“.
- JSON stands for “*JavaScript Object Notation*“.
- XML is “*eXtensible Markup Language”* whereas YML is not a markup language.
- YAML uses indentation to define structured data. So each block in the YAML is differentiated by the number of white spaces.
- XML uses a tag to define the structure just like HTML.
- All three mentioned serialization language has same extension as their name. (.yaml for YAML, .json for JSON, .xml for XML). So it is easy to remember.
- In fact, file extensions are arbitrary for all the three data serialization standard. It is useful for the application and users to know what files format, type of the content and their data structure.

#### How to choose ?

TBD.. 


[YAML vs JSON vs XML | What is the Difference Between Them?]: https://www.csestack.org/yaml-vs-json-vs-xml-difference/



## 👉 `onclick` events
#python #Web #frontend #crawler #web_scraping

普通的爬虫或者网络库(比如说scrapy/urllib/requests)没有办法实现这样的功能，因为他们做到的事情跟你用迅雷等下载工具把网页文本下载回来了没什么区别。要实现访问后续网页，一般有两种解决方案。

1.自动控制浏览器访问，这里的浏览器可以是普通浏览器，也可以是占用资源较少的无窗口浏览器，主要因为浏览器有着解析js脚本的功能，可以做到跳转。实现方案一般是使用selenium+firefox或者selenium+phantomjs，网上可以找到很多教程，使用较为简单，但占用资源较多。

2.自己拦截请求或逆向网站前端代码，找到向服务器获取试卷代码的请求链接和格式，自己进行模拟，来获取试卷。

[How can I simulate onclick event in python? [closed]]: https://stackoverflow.com/questions/38298459/how-can-i-simulate-onclick-event-in-python
