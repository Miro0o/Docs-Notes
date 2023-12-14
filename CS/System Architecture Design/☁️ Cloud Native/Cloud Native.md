# Cloud Native 

[TOC]



## Res
### Related Topics
↗ [Cloud Security](../../CyberSecurity/System%20Security/🎅🏼%20Cloud%20Security/Cloud%20Security.md)
↗ [Edge & Frog Computing](../../Embedded%20&%20Internet%20of%20Things/Edge%20&%20Frog%20Computing/Edge%20&%20Frog%20Computing.md)

### Cloud Native Computing Foundation (CNCF)
🏠 https://www.cncf.io/projects/

The Cloud Native Computing Foundation (CNCF) hosts critical components of the global technology infrastructure.

We bring together the world’s top developers, end users, and vendors and run the largest open source developer conferences. CNCF is part of the nonprofit [Linux Foundation](https://linuxfoundation.org/).

> [到底什么是“云原生”？](http://dockone.io/article/10581)


🗺️ https://landscape.cncf.io (CNCF Landscape)
The goal of the cloud native landscape is to compile and organize all cloud native open source projects and proprietary products into categories, providing an overview of the current ecosystem. Organizations that have a cloud native project or product can [submit a PR](https://github.com/cncf/landscape/) to request it to be added to the landscape.

🧭 https://landscape.cncf.io/guide (CNCF landscope Guide)
In this guide, we’ll break this mammoth landscape down and provide a high-level overview of its layers, columns, and categories.


📡 https://radar.cncf.io/how-it-works (CNCF End User Technology Radar )
The CNCF End User Technology Radar is a guide for evaluating cloud native technologies, on behalf of the CNCF End User Community. [Read more...](https://radar.cncf.io/how-it-works)


### 📆 CNCF Events
🔗 [CNCF Upcoming Events](https://linuxfoundation.org/)

KubeCon
CloudNativeCon
Open Source Summit
Open Infrastructure Summit


### 🗄 Documentations
📂 [云原生资料库](https://lib.jimmysong.io) 
📂 [DevOps资料库](https://doc.devpod.cn)
[jimmysong.io 云原生开源项目大全](https://jimmysong.io)

[云原生社区（中国）](https://cloudnative.to)

😎 [Awesome Cloud Native](https://jimmysong.io/awesome-cloud-native/?_gl=1*112yc3f*_ga*OTE3MDEzMDM5LjE2NzgyNjYwMDg.*_ga_MP490FS739*MTY3ODI2NjAwOC4xLjEuMTY3ODI3MDY1MS42MC4wLjA.)

[GoogleCloud](https://cloud.google.com/docs)

[AWS](https://docs.aws.amazon.com/index.html?nc2=h_ql_doc_do)

[云原生实战](https://www.yuque.com/leifengyang/oncloud/vfvmcd)


### 🎬 Video
[云原生Java架构师的第一课K8s+Docker+KubeSphere+DevOps](https://www.bilibili.com/video/BV13Q4y1C7hS?p=37&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d)
- [配套文档](https://www.yuque.com/leifengyang/oncloud/ctiwgo)


### 📚 Books
[Cloud Computing: Concepts, Technology & Architecture (The Pearson Service Technology Series from Thomas Erl)](https://www.amazon.com/Cloud-Computing-Concepts-Technology-Architecture/dp/0133387526)



## Intro
![](../../../Assets/Pics/Screen%20Shot%202022-09-02%20at%201.24.17%20AM-2053065.png)
<small>Cloud Native Landscope <a>https://landscape.cncf.io</a></small>


> 云实际上是平台级的资源调度方案。类比于SDN对异构网络设施进行平台级的网络资源的统一调度，云对异构计算机基础设施的（计算/网络/存储）资源进行平台级的统一调度。
> 通过容器技术（Container）将计算资源进行打包，通过编排技术（Orchestration）对计算资源进行统一管理并分发。
> 
> 云更多是一种服务模式/商业模式的创新，而不是技术上的创新。云的支柱性技术都是计算机行业中发展许久的技术：容器技术来自虚拟化技术；编排技术来自web工程，涉及负载均衡，服务发现，平台监控/日志，CDN分发，容灾备份，流量工程，等等；通信模式/SDN等等设计来自计算机网络。
> （云原生关于此有 15 Factors Application 标准。）
> 
> 云的平台级的调度可以类比美团平台对实际餐饮市场中的个体餐饮商户的服务资源进行调度：个体餐饮商户提供基础的餐饮服务（物理资源），包装技术对食物进行打包以便于统一调度（容器技术），外卖员负责异构基础设施间的资源通讯（SDN/NFV/网络通讯），美团平台统一进行资源调度/服务提供。通过美团平台的资源整合服务，整个城市所有接入平台的物理底层资源变得对城市内任意时空节点都具有可用性，而这种服务可用性的边界就是网络通讯的边界（外卖员的交通范围）；这就是云想要做的事情。
> 
> 可以看出不论是SDN，云（，还是美团）都是平台级别的资源调度架构/方案；这种架构的主要目标就是实现对一切可用资源的最大化利用。因此这些平台的商业成功严重依赖平台覆盖率，用户基数/活跃度，等等宏观因素；对规模较小的服务提供商来说他们不容易取得商业市场上的成功，对全球范围内/区域范围内来说市场也只容得下几个垄断性质的头部云厂商，可能再加上几个主打差异化的小型云厂商。总得来说，这不会是一个各家公平竞争的fair game。
> 
> 云的技术特点：
> 虚拟化 + 分布式 + 自动化


Start form ↗ [Cloud Computing](🌵%20Cloud%20Native%20Overview/🗿%20Cloud%20Models/Cloud%20Service%20(Delivery)%20Models/SaaS/Cloud%20Computing/Cloud%20Computing.md)



## Cloud Native Architectures
↗ [Cloud Computing Security Architecture](🌵%20Cloud%20Native%20Overview/🗿%20Cloud%20Models/Cloud%20Computing%20Security%20Architecture.md)
↗ [Cloud Deployment Models](🌵%20Cloud%20Native%20Overview/🗿%20Cloud%20Models/Cloud%20Deployment%20Models.md)
↗ [Cloud Service (Delivery) Models](🌵%20Cloud%20Native%20Overview/🗿%20Cloud%20Models/Cloud%20Service%20(Delivery)%20Models/Cloud%20Service%20(Delivery)%20Models.md)



## Cloud Security
↗ [Cloud Security](../../CyberSecurity/System%20Security/🎅🏼%20Cloud%20Security/Cloud%20Security.md)



## Ref
Cloud Stack
[Cilium](https://docs.cilium.io/en/stable/)

[Quarkus](https://quarkus.io)

[openstack](https://www.openstack.org)

[nacos](https://github.com/alibaba/nacos)

[drone](https://github.com/harness/drone)

[filebeat](https://www.elastic.co/beats/filebeat)

[Puppet Forge](https://forge.puppet.com)

[Stackify Retrace](https://docs.stackify.com/v1/docs?_ga=2.2045431.795068548.1606150356-1374364069.1597069964)

[heroku](https://elements.heroku.com)

...

---
[What is SRE (Site Reliability Engineering)](https://www.redhat.com/en/topics/devops/what-is-sre)

[KVM](https://www.linux-kvm.org/page/Main_Page)

[Serverless](Serverless/Intro.md) 

[DevOps](DevOps/Orientation.md) 

Agile Dev

阿里如何实现100%容器化镜像化？八年技术演进之路回顾 - 阿里云云栖号的文章 - 知乎
https://zhuanlan.zhihu.com/p/45467643