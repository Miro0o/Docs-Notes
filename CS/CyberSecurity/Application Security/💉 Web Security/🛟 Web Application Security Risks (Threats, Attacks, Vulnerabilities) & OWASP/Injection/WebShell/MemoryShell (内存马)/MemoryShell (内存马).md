# MemoryShell (内存马)

[TOC]



## Res
### Related Topics


### Other Resources
🚧 https://github.com/W01fh4cker/LearnJavaMemshellFromZero
- [一、前言](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#%E4%B8%80%E5%89%8D%E8%A8%80)
- [二、前置知识](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#%E4%BA%8C%E5%89%8D%E7%BD%AE%E7%9F%A5%E8%AF%86)
    - [2.1 Servlet容器与Engine、Host、Context和Wrapper](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#21-servlet%E5%AE%B9%E5%99%A8%E4%B8%8Eenginehostcontext%E5%92%8Cwrapper)
    - [2.2 编写一个简单的servlet](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#22-%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA%E7%AE%80%E5%8D%95%E7%9A%84servlet)
    - [2.3 从代码层面看servlet初始化与装载流程](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#23-%E4%BB%8E%E4%BB%A3%E7%A0%81%E5%B1%82%E9%9D%A2%E7%9C%8Bservlet%E5%88%9D%E5%A7%8B%E5%8C%96%E4%B8%8E%E8%A3%85%E8%BD%BD%E6%B5%81%E7%A8%8B)
        - [2.3.1 servlet初始化流程分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#231-servlet%E5%88%9D%E5%A7%8B%E5%8C%96%E6%B5%81%E7%A8%8B%E5%88%86%E6%9E%90)
        - [2.3.2 servlet装载流程分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#232-servlet%E8%A3%85%E8%BD%BD%E6%B5%81%E7%A8%8B%E5%88%86%E6%9E%90)
    - [2.4 Filter容器与FilterDefs、FilterConfigs、FilterMaps、FilterChain](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#24-filter%E5%AE%B9%E5%99%A8%E4%B8%8Efilterdefsfilterconfigsfiltermapsfilterchain)
    - [2.5 编写一个简单的Filter](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#25-%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA%E7%AE%80%E5%8D%95%E7%9A%84filter)
    - [2.6 从代码层面分析Filter运行的整体流程](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#26-%E4%BB%8E%E4%BB%A3%E7%A0%81%E5%B1%82%E9%9D%A2%E5%88%86%E6%9E%90filter%E8%BF%90%E8%A1%8C%E7%9A%84%E6%95%B4%E4%BD%93%E6%B5%81%E7%A8%8B)
    - [2.7 Listener简单介绍](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#27-listener%E7%AE%80%E5%8D%95%E4%BB%8B%E7%BB%8D)
    - [2.8 编写一个简单的Listener（ServletRequestListener）](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#28-%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA%E7%AE%80%E5%8D%95%E7%9A%84listenerservletrequestlistener)
    - [2.9 从代码层面分析Listener运行的整体流程](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#29-%E4%BB%8E%E4%BB%A3%E7%A0%81%E5%B1%82%E9%9D%A2%E5%88%86%E6%9E%90listener%E8%BF%90%E8%A1%8C%E7%9A%84%E6%95%B4%E4%BD%93%E6%B5%81%E7%A8%8B)
    - [2.10 简单的spring项目搭建](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#210-%E7%AE%80%E5%8D%95%E7%9A%84spring%E9%A1%B9%E7%9B%AE%E6%90%AD%E5%BB%BA)
        - [2.10.1 编写一个简单的Spring Controller](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2101-%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA%E7%AE%80%E5%8D%95%E7%9A%84spring-controller)
        - [2.10.2 编写一个简单的Spring Interceptor](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2102-%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA%E7%AE%80%E5%8D%95%E7%9A%84spring-interceptor)
        - [2.10.3 编写一个简单的Spring WebFlux的Demo（基于Netty）](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2103-%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA%E7%AE%80%E5%8D%95%E7%9A%84spring-webflux%E7%9A%84demo%E5%9F%BA%E4%BA%8Enetty)
    - [2.11 Spring MVC介绍](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#211-spring-mvc%E4%BB%8B%E7%BB%8D)
        - [2.11.1 Spring MVC九大组件](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2111-spring-mvc%E4%B9%9D%E5%A4%A7%E7%BB%84%E4%BB%B6)
        - [2.11.2 简单的源码分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2112-%E7%AE%80%E5%8D%95%E7%9A%84%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90)
            - [2.11.2.1 九大组件的初始化](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#21121-%E4%B9%9D%E5%A4%A7%E7%BB%84%E4%BB%B6%E7%9A%84%E5%88%9D%E5%A7%8B%E5%8C%96)
            - [2.11.2.2 url和Controller的关系的建立](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#21122-url%E5%92%8Ccontroller%E7%9A%84%E5%85%B3%E7%B3%BB%E7%9A%84%E5%BB%BA%E7%AB%8B)
            - [2.11.2.3 Spring Interceptor引入与执行流程分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#21123-spring-interceptor%E5%BC%95%E5%85%A5%E4%B8%8E%E6%89%A7%E8%A1%8C%E6%B5%81%E7%A8%8B%E5%88%86%E6%9E%90)
    - [2.12 Spring WebFlux介绍与代码调试分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#212-spring-webflux%E4%BB%8B%E7%BB%8D%E4%B8%8E%E4%BB%A3%E7%A0%81%E8%B0%83%E8%AF%95%E5%88%86%E6%9E%90)
        - [2.12.1 什么是Mono？](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2121-%E4%BB%80%E4%B9%88%E6%98%AFmono)
        - [2.12.2 什么是Flux？](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2122-%E4%BB%80%E4%B9%88%E6%98%AFflux)
        - [2.12.3 Spring WebFlux启动过程分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2123-spring-webflux%E5%90%AF%E5%8A%A8%E8%BF%87%E7%A8%8B%E5%88%86%E6%9E%90)
        - [2.12.4 Spring WebFlux请求处理过程分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2124-spring-webflux%E8%AF%B7%E6%B1%82%E5%A4%84%E7%90%86%E8%BF%87%E7%A8%8B%E5%88%86%E6%9E%90)
        - [2.12.5 Spring WebFlux过滤器WebFilter运行过程分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2125-spring-webflux%E8%BF%87%E6%BB%A4%E5%99%A8webfilter%E8%BF%90%E8%A1%8C%E8%BF%87%E7%A8%8B%E5%88%86%E6%9E%90)
    - [2.13 Tomcat Valve介绍与运行过程分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#213-tomcat-valve%E4%BB%8B%E7%BB%8D%E4%B8%8E%E8%BF%90%E8%A1%8C%E8%BF%87%E7%A8%8B%E5%88%86%E6%9E%90)
        - [2.13.1 Valve与Pipeline](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2131-valve%E4%B8%8Epipeline)
        - [2.13.2 编写一个简单Tomcat Valve的demo](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2132-%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA%E7%AE%80%E5%8D%95tomcat-valve%E7%9A%84demo)
        - [2.13.3 Tomcat Valve打入内存马思路分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2133-tomcat-valve%E6%89%93%E5%85%A5%E5%86%85%E5%AD%98%E9%A9%AC%E6%80%9D%E8%B7%AF%E5%88%86%E6%9E%90)
    - [2.14 Tomcat Upgrade介绍与打入内存马思路分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#214-tomcat-upgrade%E4%BB%8B%E7%BB%8D%E4%B8%8E%E6%89%93%E5%85%A5%E5%86%85%E5%AD%98%E9%A9%AC%E6%80%9D%E8%B7%AF%E5%88%86%E6%9E%90)
        - [2.14.1 编写一个简单的Tomcat Upgrade的demo](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2141-%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA%E7%AE%80%E5%8D%95%E7%9A%84tomcat-upgrade%E7%9A%84demo)
            - [2.14.1.1 利用SpringBoot搭建](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#21411-%E5%88%A9%E7%94%A8springboot%E6%90%AD%E5%BB%BA)
            - [2.14.1.2 利用Tomcat搭建](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#21412-%E5%88%A9%E7%94%A8tomcat%E6%90%AD%E5%BB%BA)
        - [2.14.2 Tomcat Upgrade内存马介绍与相关代码调试分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2142-tomcat-upgrade%E5%86%85%E5%AD%98%E9%A9%AC%E4%BB%8B%E7%BB%8D%E4%B8%8E%E7%9B%B8%E5%85%B3%E4%BB%A3%E7%A0%81%E8%B0%83%E8%AF%95%E5%88%86%E6%9E%90)
    - [2.15 Tomcat Executor内存马介绍与打入内存马思路分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#215-tomcat-executor%E5%86%85%E5%AD%98%E9%A9%AC%E4%BB%8B%E7%BB%8D%E4%B8%8E%E6%89%93%E5%85%A5%E5%86%85%E5%AD%98%E9%A9%AC%E6%80%9D%E8%B7%AF%E5%88%86%E6%9E%90)
        - [2.15.1](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2151)
        - [2.15.2 Tomcat Executor内存马介绍与代码调试分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#2152-tomcat-executor%E5%86%85%E5%AD%98%E9%A9%AC%E4%BB%8B%E7%BB%8D%E4%B8%8E%E4%BB%A3%E7%A0%81%E8%B0%83%E8%AF%95%E5%88%86%E6%9E%90)
            - [2.15.2.1 Endpoint五大组件](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#21521-endpoint%E4%BA%94%E5%A4%A7%E7%BB%84%E4%BB%B6)
            - [2.15.2.2 Endpoint分类](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#21522-endpoint%E5%88%86%E7%B1%BB)
            - [2.15.2.3 Executor相关代码分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#21523-executor%E7%9B%B8%E5%85%B3%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90)
- [三、传统Web型内存马](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#%E4%B8%89%E4%BC%A0%E7%BB%9Fweb%E5%9E%8B%E5%86%85%E5%AD%98%E9%A9%AC)
    - [3.1 Servlet内存马](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#31-servlet%E5%86%85%E5%AD%98%E9%A9%AC)
        - [3.1.1 简单的servlet内存马demo编写](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#311-%E7%AE%80%E5%8D%95%E7%9A%84servlet%E5%86%85%E5%AD%98%E9%A9%ACdemo%E7%BC%96%E5%86%99)
        - [3.1.2 servlet内存马demo代码分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#312-servlet%E5%86%85%E5%AD%98%E9%A9%ACdemo%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90)
        - [3.1.3 关于StandardContext、ApplicationContext、ServletContext的理解](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#313-%E5%85%B3%E4%BA%8Estandardcontextapplicationcontextservletcontext%E7%9A%84%E7%90%86%E8%A7%A3)
    - [3.2 Filter内存马](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#32-filter%E5%86%85%E5%AD%98%E9%A9%AC)
        - [3.2.1 简单的filter内存马demo编写](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#321-%E7%AE%80%E5%8D%95%E7%9A%84filter%E5%86%85%E5%AD%98%E9%A9%ACdemo%E7%BC%96%E5%86%99)
        - [3.2.2 servlet内存马demo代码分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#322-servlet%E5%86%85%E5%AD%98%E9%A9%ACdemo%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90)
        - [3.2.3 tomcat6下filter内存马的编写](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#323-tomcat6%E4%B8%8Bfilter%E5%86%85%E5%AD%98%E9%A9%AC%E7%9A%84%E7%BC%96%E5%86%99)
    - [3.3 Listener内存马](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#33-listener%E5%86%85%E5%AD%98%E9%A9%AC)
        - [3.3.1 简单的Listener内存马demo编写](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#331-%E7%AE%80%E5%8D%95%E7%9A%84listener%E5%86%85%E5%AD%98%E9%A9%ACdemo%E7%BC%96%E5%86%99)
        - [3.3.2 Listener内存马demo代码分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#332-listener%E5%86%85%E5%AD%98%E9%A9%ACdemo%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90)
- [四、Spring MVC框架型内存马](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#%E5%9B%9Bspring-mvc%E6%A1%86%E6%9E%B6%E5%9E%8B%E5%86%85%E5%AD%98%E9%A9%AC)
    - [4.1 Spring Controller型内存马](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#41-spring-controller%E5%9E%8B%E5%86%85%E5%AD%98%E9%A9%AC)
        - [4.1.1 简单的Spring Controller型内存马demo编写](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#411-%E7%AE%80%E5%8D%95%E7%9A%84spring-controller%E5%9E%8B%E5%86%85%E5%AD%98%E9%A9%ACdemo%E7%BC%96%E5%86%99)
        - [4.1.2 Spring Controller型内存马demo代码分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#412-spring-controller%E5%9E%8B%E5%86%85%E5%AD%98%E9%A9%ACdemo%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90)
    - [4.2 Spring Interceptor型内存马](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#42-spring-interceptor%E5%9E%8B%E5%86%85%E5%AD%98%E9%A9%AC)
    - [4.3 Spring WebFlux内存马](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#43-spring-webflux%E5%86%85%E5%AD%98%E9%A9%AC)
        - [4.3.1 简单的Spring WebFlux内存马demo编写](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#431-%E7%AE%80%E5%8D%95%E7%9A%84spring-webflux%E5%86%85%E5%AD%98%E9%A9%ACdemo%E7%BC%96%E5%86%99)
        - [4.3.2 Spring WebFlux内存马demo代码分析](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#432-spring-webflux%E5%86%85%E5%AD%98%E9%A9%ACdemo%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90)
- [五、中间件型内存马](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#%E4%BA%94%E4%B8%AD%E9%97%B4%E4%BB%B6%E5%9E%8B%E5%86%85%E5%AD%98%E9%A9%AC)
    - [5.1 Tomcat Valve型内存马](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#51-tomcat-valve%E5%9E%8B%E5%86%85%E5%AD%98%E9%A9%AC)
    - [5.2 Tomcat Upgrade内存马](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#52-tomcat-upgrade%E5%86%85%E5%AD%98%E9%A9%AC)
    - [5.3 Tomcat Executor内存马](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#53-tomcat-executor%E5%86%85%E5%AD%98%E9%A9%AC)
- [六、致谢](https://github.com/W01fh4cker/LearnJavaMemshellFromZero#%E5%85%AD%E8%87%B4%E8%B0%A2)

🚧 https://github.com/gobysec/Memory-Shell
Traditional webshell backdoors, no matter how much effort is put into hiding or how they are disguised, are unable to persist in the target system under existing defense measures. Some simple examples of defense measures include: For terminal security: file monitoring, anti-tampering, and EDR; For backdoors: webshell detection and traffic monitoring; For the network layer: firewalls to prevent reverse connections, and reverse proxy systems to hide real IPs; and so on.

**From asset detection, vulnerability scanning, injection of memory shells to management of webshells, they can all be directly completed by Goby.**

Here are some articles to introduce:  
[The king of shell Javaweb Memory Shell-Cognitive Section](https://github.com/gobysec/Memory-Shell/blob/main/Memory%20shell%20%5BCognitive%20Section%5D.md)
[Use Goby to break into the memory horse through the deserialization vulnerability-exploitation Edition](https://github.com/gobysec/Memory-Shell/blob/main/Goby%20memory%20shell%5Bexploitation%5D.md)
[Goby Exploits Memory Shellcode Technology Details-Technical Edition](https://github.com/gobysec/Memory-Shell/blob/main/Memory%20shellcode%5BTechnical%5D.md)
[Goby Official URL](https://gobies.org/)
1. GitHub issue: [https://github.com/gobysec/Goby/issues](https://github.com/gobysec/Goby/issues)
2. Telegram Group: [http://t.me/gobies](http://t.me/gobies) (Group benefits: enjoy the version update 1 month in advance)
3. Telegram Channel: [https://t.me/joinchat/ENkApMqOonRhZjFl](https://t.me/joinchat/ENkApMqOonRhZjFl) (Channel benefits: enjoy the version update 1 month in advance)
4. WeChat Group: First add my personal WeChat: **gobyteam**, I will add everyone to the official WeChat group of Goby. (Group benefits: enjoy the version update 1 month in advance)



## Intro
> 🔗 https://www.freebuf.com/articles/web/274466.html

webshell的变迁过程大致如下所述：web服务器管理页面——> 大马——>小马拉大马——>一句话木马——>加密一句话木马——>加密内存马

![](../../../../../../../../Assets/Pics/Pasted%20image%2020240331133657.png)

内存马是无文件攻击的一种常用手段，随着攻防演练热度越来越高：攻防双方的博弈，流量分析、EDR等专业安全设备被蓝方广泛使用，传统的文件上传的webshll或以文件形式驻留的后门越来越容易被检测到，内存马使用越来越多。

Webshell内存马，是在内存中写入恶意后门和木马并执行，达到远程控制Web服务器的一类内存马，其瞄准了企业的对外窗口：网站、应用。但传统的Webshell都是基于文件类型的，黑客可以利用上传工具或网站漏洞植入木马，区别在于Webshell内存马是无文件马，利用中间件的进程执行某些恶意代码，不会有文件落地，给检测带来巨大难度。



## Ref
[👍 一文看懂内存马 | freebuf]: https://www.freebuf.com/articles/web/274466.html
- [java web请求三大器——listener、filter、servlet](https://blog.csdn.net/chenwiehuang/article/details/80811193)  
- [Tomcat架构原理](https://segmentfault.com/a/1190000023475177)  
- [利用“进程注入”实现无文件复活 WebShell](https://www.freebuf.com/articles/web/172753.html)  
- [深入理解反射](https://mp.weixin.qq.com/s/TqSLUWYWfhHjpfI_srETJg)  
- [查杀Java web filter型内存马](http://gv7.me/articles/2020/kill-java-web-filter-memshell/)

[分享几个直接可用的内存马，记录一下学习过程中看过的文章 | github]: https://github.com/bitterzzZZ/MemoryShellLearn

[🤔 Shell中的幽灵王者—JAVAWEB 内存马 【认知篇】]: https://nosec.org/home/detail/5049.html
