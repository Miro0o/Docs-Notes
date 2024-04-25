# OpenStack

[TOC]



## Res
🏠 https://www.openstack.org
📂 https://docs.openstack.org/
📂 https://wiki.openstack.org/wiki/Main_Page
👨‍💻 https://www.openstack.org/blog/

🚧 https://github.com/openstack/devstack
System for quickly installing an OpenStack cloud from upstream git for testing and development. Mirror of code maintained at opendev.org.


### Related Topics
↗ [IaaS (Infrastructure as a Service)](../../🌵%20Cloud%20Native%20Overview/🗿%20Cloud%20Models/Cloud%20Service%20(Delivery)%20Models/IaaS%20(Infrastructure%20as%20a%20Service)/IaaS%20(Infrastructure%20as%20a%20Service).md)


### Other Materials
http://openstack.unixhot.com/openstack/openstack-introduce.html
OpenStack 快速入门

https://www.xjimmy.com/openstack-5min
每天5分钟玩转 OPENSTACK系列教程



## Intro
![|200](../../../../../../../Assets/Pics/Pasted%20image%2020230308140123.png)



## OpenStack Organization &  Architecture
### OpenStack Architecture Overview
![](../../../../../Assets/Pics/Pasted%20image%2020240424230252.png)
<small>https://zhuanlan.zhihu.com/p/35598437</small>

![](../../../../../Assets/Pics/Pasted%20image%2020240425133210.png)
<small>https://blogs.cisco.com/cloud/openstack-can-be-complicated-but-it-does-not-have-to-be</small>

![](../../../../../Assets/Pics/Pasted%20image%2020240424230243.png)
<small>https://zhuanlan.zhihu.com/p/35598437</small>


### 🎯 OpenStack Components

![](../../../../../Assets/Pics/Pasted%20image%2020240424230321.png)
<small>OpenStack关键组件及作用</small>

#### Dashboard /Web Frontend Services | Horizon
#### ⭐ Compute Services | Nova
#### ⭐ Networking Services | Neutron
#### ⭐ Storage Services
##### Object Storage | Swift
##### Block Storage | Cinder
#### Shared Services
##### Identity Service | Keystone
##### Image Service | Glance
##### Telemetry | Ceilometer
#### Higher-level Services
##### Orchestration | Heat
##### Database Service | Trove



## Ref
[👍 openstack入门第一章基础与部署环境 | CSDN]: https://blog.csdn.net/weixin_56665913/article/details/119833046

[👍 openstack深入学习 | Cnblog]: https://www.cnblogs.com/cuiyongchao007/p/12902169.html

[👍 OpenStack入门科普，看这一篇就够啦！ - 小枣君的文章 - 知乎]: https://zhuanlan.zhihu.com/p/35598437
推荐几个大咖，大家可以百度找他们的博客来看：陈沙克、何明桂、孔令贤，Cloudman。

[👍 OpenStack构架知识梳理]: http://www.cnblogs.com/kevingrace/p/5733508.html

[openstack学习-网络管理(转)]: https://heitaoq66.github.io/2020/03/19/openstack学习-网络管理/