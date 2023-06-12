# IPv4 Address & Addressing

[TOC]



## Res


## Overview
### IP Address & Interface
IP address is the world-wide unique address assigned to **NIC (network interface card)** or simple network interface as its network communicating identity. 

![](../../../../../../../Assets/Pics/Screenshot%202023-05-12%20at%2010.35.06%20AM.png)


### IP Address Structure & Subnet

Subnet is device interfaces that can physically reach each other without passing through an intervening router.

![](../../../../../../../Assets/Pics/Screenshot%202023-05-12%20at%2010.38.17%20AM.png)



## IPv4 Address Coding
![Screenshot 2022-11-20 at 12.26.00 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2012.26.00%20PM.png)


### 1️⃣ Classful IPv4 Address Coding

🎬 【深入浅出计算机网络 微课视频】 https://www.bilibili.com/video/BV1NT411g7n6/?p=50&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

#### Classful IPv4 Address Coding Overview
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%209.32.07%20AM.png)


![Screenshot 2022-11-20 at 12.12.43 PM](../../../../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2012.12.43%20PM.png)
![Screenshot 2022-11-20 at 12.13.19 PM](../../../../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2012.13.19%20PM.png)


#### Type A Address
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%209.35.22%20AM.png)


#### Type B Address
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%209.37.47%20AM.png)


#### Type C Address
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%209.39.37%20AM.png)


#### 🤔 Exercise Problems
Problem \#1
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%209.42.18%20AM.png)

Problem \#2
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%209.44.06%20AM.png)

Problem \#3
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%209.46.45%20AM.png)


#### Type D Address (IP Multicasting Group Addresses)
↗ [IP Multicasting (Group Communication )（多播，组播）](../../🎮%20Control%20Plane%20(Routing%20&%20Managements)/Network%20Routing%20(IP%20Address%20Modes)%20(Route%20Selection)/IP%20Multicasting%20(Group%20Communication%20)（多播，组播）/IP%20Multicasting%20(Group%20Communication%20)（多播，组播）.md)


#### Type E Address


### 2️⃣ Subnetting

🎬 【深入浅出计算机网络 微课视频】 https://www.bilibili.com/video/BV1NT411g7n6/?p=51&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.23.25%20AM.png)


#### Subnet Mask
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%209.53.34%20AM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%209.54.49%20AM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%209.55.25%20AM.png)


#### 🤔 Exercise Problems
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.19.29%20AM.png)


#### Default Subnet Mask
![Screenshot 2022-11-20 at 12.24.02 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2012.24.02%20PM.png)


### 3️⃣ Classless Inter-Domain Routing (CIDR)

🔗 【深入浅出计算机网络 - 4.2.2 IPv4地址及其编址方法——无分类编址方法】 https://www.bilibili.com/video/BV1gD4y1B7iW/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
【深入浅出计算机网络 微课视频】 https://www.bilibili.com/video/BV1NT411g7n6/?p=52&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.39.03%20AM.png)
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.39.27%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.39.56%20AM.png)


#### Route Aggregation (Supernet)
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.40.54%20AM.png)


#### 🤔 Exercise Problems
Problem \#1
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.40.17%20AM.png)

Problem \#2
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.37.12%20AM.png)

Problem \#3
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.38.20%20AM.png)

Problem \#4
![Screenshot 2022-11-20 at 12.28.33 PM](../../../../../../../Assets/Pics/Screenshot%202022-11-20%20at%2012.28.33%20PM.png)



## IPv4 Application Planning
🔗 【深入浅出计算机网络 - 4.2.3 IPv4地址的应用规划】 https://www.bilibili.com/video/BV1J24y1Z72E/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

🔗【定长子网划分和变长子网划分的二叉树解法】 https://www.bilibili.com/video/BV11G4y1x75G/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.53.20%20AM.png)


### FLSM (Fixed Length Subnet Masking) via 2️⃣ Subnetting
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.57.05%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.58.15%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.58.45%20AM.png)



![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.48.48%20AM.png)


### VLSM (Variable Length Subnet Masking) via 3️⃣ CIDR
![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.49.43%20AM.png)

![](../../../../../../../Assets/Pics/Screenshot%202023-05-10%20at%2010.51.58%20AM.png)




## Ref

