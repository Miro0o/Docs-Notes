# IP

[TOC]



## Res


## IP Overview
### IP Datagram Format
🔗 【深入浅出计算机网络 - 4.2.7 IPv4数据报的首部格式】 https://www.bilibili.com/video/BV19Y4y1K7i7/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

🔗 【深入浅出计算机网络 - 4.9.2~4.9.3 IPv6数据报的基本首部和扩展首部】 https://www.bilibili.com/video/BV1wW4y1S7q9/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

🔗【深入浅出计算机网络 - 4.9.1 IPv6引进的主要变化】 https://www.bilibili.com/video/BV1VY4y1J7GV/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d\

> 🏃 For IPv6, go to [IPv6](IPv6/IPv6.md).
>
> 🏃 For more about IPv4, go to [IPv4](IPv4/IPv4.md).


![](../../../../../../../Assets/Pics/technologies_white_paper0900aecd8054d37d-03.jpg)
<small>IPv4 vs IPv6</small>


![IPv6 features](../../../../../../../Assets/Pics/image44.png)
<small>IPv4 vs IPv6</small>


### 🎰 Limited IP Address & Addressing

> - For Mac Addressing, 🙈 check out [MAC & ARP](MAC & ARP.md) 

> ⚠ As for Mac addressing, it can be categorized both as Network Layer or Link Layer. Here it falls on Network Layer.


The number of IPv4 address is very limited. To tackle this problem tons of efforts have been made:
↗ [IPv4 Addressing](IPv4/IPv4%20Addressing.md)
↗ [NAT](../MiddleBoxes/NAT/NAT.md)
↗ [IPv6](IPv6/IPv6.md)

Among all of this solusion, IPv6 is deemed to be the ultimate method dealing with "limited number of address" --- because it's unlimited!


### IP Address Assignment
#### 👐🏼 IP Address: How to get one (usr)?
##### Hard-coded


##### DHCP


#### 👐🏼 IP Address: How to get one (ISP)?
##### ICANN

##### NAT

##### IPv6



## 🚚 IP Datagram Delivering
🔗 【深入浅出计算机网络 - 4.2.6 IP数据报的发送和转发流程】 https://www.bilibili.com/video/BV1Ne4y187tz/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

![Screenshot 2022-11-26 at 3.55.37 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-26%20at%203.55.37%20PM.png)


![Screenshot 2022-11-26 at 3.55.01 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-26%20at%203.55.01%20PM.png)


### Indirect Delivery
![](../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.30.32%20AM.png)


#### Default Gateway
![](../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.32.14%20AM.png)

![](../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.33.33%20AM.png)

![](../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.37.35%20AM.png)


#### Multicast Segregation
![](../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.36.59%20AM.png)

![](../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.36.33%20AM.png)


### 🤔 Exercise Problems
Problem \#1
![](../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.39.11%20AM.png)


Problem \#2
![](../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2011.39.40%20AM.png)



## 🚏IP Datagram Routing
### Routing Protocols
🔗 【深入浅出计算机网络 - 4.4.1~4.4.2 因特网的路由选择协议概述】 https://www.bilibili.com/video/BV1ie4y187ss/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

> 🏃 For detailed info, go to  [IP Routing](../../IP Routing/IP Routing.md) 


### 👷🏻 Static Routing Configuration
🔗【深入浅出计算机网络 - 4.3 静态路由配置】 https://www.bilibili.com/video/BV1vB4y1n7pW/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

- 默认路由
- 特定主机路由


![Screenshot 2022-11-26 at 4.09.26 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-26%20at%204.09.26%20PM.png)

![Screenshot 2022-11-26 at 4.09.43 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-26%20at%204.09.43%20PM.png)



### 🕊️ Dynamic Routing Configuration

![Screenshot 2022-11-20 at 2.02.09 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-20%20at%202.02.09%20PM.png)



## Ref
