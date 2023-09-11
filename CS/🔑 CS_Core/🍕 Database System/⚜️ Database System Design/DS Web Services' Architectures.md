# DS Web Services' Architectures

[TOC]



## Res
↗ [Web & DBMS](../🪐%20Web%20&%20DBMS/Web%20&%20DBMS.md)



## DS Architectures in Web
### Mainframe Architecture
![](../../../../Assets/Pics/Pasted%20image%2020230306154507.png)

| Advantages of Mainframe Architecture | Disadvantages of Mainframe Architecture |
| - | - |
| Large number of concurrent users | Does not take advantage of local computer processing power |
| Able to handle very large volume of transactions | Does not take advantage of local computer processing power |
| Suitable for slow network environments | Does not take advantage of local computer processing power |
| Central location of both application | Hardware is relatively expensive |
| Character-based interface | DBMS makes maintenance relatively simple |


### Desktop Architecture
![|500](../../../../Assets/Pics/Pasted%20image%2020230306155045.png)

| Advantages of Mainframe Architecture | Disadvantages of Mainframe Architecture |
| - | - |
| Inexpensive to acquire | Only available to a single user at a time |
| Easy to configure | Only available at a single computer|
| Requires few resources to operate | May impose limits on how data can be stored |


### File Server Architecture
![](../../../../Assets/Pics/Pasted%20image%2020230306155115.png)

| Advantages of Mainframe Architecture | Disadvantages of Mainframe Architecture |
| - | - |
| Inexpensive to acquire | Only viable for a limited number of users, perhaps 10 or fewer |
| Easy to configure | Query performance declines quickly as the amount of data increases |
| Low-cost option for multi-user concurrency | Multiple installation of both application software and DBMS can lead to version control issues for both |


### Client/Server Architecture (Traditional Two-Tier C/S)
![](../../../../Assets/Pics/Pasted%20image%2020230306155216.png)

![](../../../../Assets/Pics/Screenshot%202023-03-06%20at%208.09.02%20PM.png)

| Advantages of Mainframe Architecture | Disadvantages of Mainframe Architecture |
| - | - |
| Makes good use of processing power of multiple computers | Application software is distributed, possibly leading to version control issues |
| Handles large amounts of both data and transactions | DBMS software is relatively expensive compared to the file-server approach |
| Can support thousands of concurrent users |  |



### Web Architecture (Three-Tier C/S, MVC)
![](../../../../Assets/Pics/Pasted%20image%2020230306155344.png)

![](../../../../Assets/Pics/Screenshot%202023-03-06%20at%208.09.30%20PM.png)


> 🔗 More of Modle-View-Control architecture is at [MVC](../../../Software%20Engineering/👾%20Web%20Dev%20&%20Ops/👩🏻‍🎨%20Design%20Pattern/MVC.md)

| Advantages of Mainframe Architecture | Disadvantages of Mainframe Architecture |
| - | - |
| All advantages of the client/server architecture |  Adds another layer of complexity (web server) |
| Increased ease of application version control | Various software apps must keep synchronized with database software |
| Very good at handling intermittent use from large numbers of users (millions)| Upgrades in browsers may require changes to application |


#### Application Server
#TODO 

> 一个应用服务器必须处理以下若千复杂的问题:
> 
> - 并发
> - 网络连接管理
> - 提供对所有数据库服务器的访问
> - 数据库连接池
> - 支持遗留数据库
> - 支持集群
> - 负载平衡
> - 失效备援


### N-Tier C/S Architecture
![](../../../../Assets/Pics/Pasted%20image%2020230306201808.png)

#TODO 


#### Middleware
↗ [Software Engineering /Middleware](../../../Software%20Engineering/👾%20Web%20Dev%20&%20Ops/🖖🏾%20Middleware/Middleware.md)
↗ [TP Monitor](../../../Software%20Engineering/👾%20Web%20Dev%20&%20Ops/👁️%20Operations%20Management/Monitoring%20&%20Analyzing/TP%20Monitor.md)



## 🔥 Web & SOA
#TODO 


## 🕸️ Distributed DBMS
↗ [Architecture Design /Distributed Systems](../../../System%20Architecture%20Design/♟️%20Distributed%20Systems/Distributed%20Systems.md)



## 🍧 Data Warehouse
#TODO 

数据库 与 数据仓库的本质区别是什么？ - 陈诚的回答 - 知乎 https://www.zhihu.com/question/20623931/answer/139842331



## ☁ Cloud Computing
↗ [Cloud Computing](../../../System%20Architecture%20Design/☁️%20Cloud%20Native/🌵%20Cloud%20Overview/🗿%20Cloud%20Models/Cloud%20Service%20(Delivery)%20Models/SaaS/Cloud%20Computing/Cloud%20Computing.md)



## Database System Design
↗ [Database System Design](Database%20System%20Design.md)



## Ref
[Database Architectures]: https://app.myeducator.com/reader/web/617b/chapter01/gj149/
[What is N-Tier Architecture? How It Works, Examples, Tutorials, and More]: https://stackify.com/n-tier-architecture/
