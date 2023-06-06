# Diffie-Hellman Key Exchange

[TOC]



## Res


## Intro
Deffie-Hellman(简称 DH) 密钥交换是最早的 密钥交换算法之一，它使得通信的双方能在非安 全的信道中安全的交换密钥，用于加密后续的通 信消息。由前Sun Microsystems 公司首席安全官， 惠特菲尔德·迪菲(Whitfield Diffie)和斯坦福大 学电气工程系名誉教授马丁·赫尔曼(Martin Edward Hellman)在1976年首次发表。

2016年3月两人获2015ACM图灵奖



## Basic DH Key Exchange
![](../../../../../../../Assets/Pics/Screenshot%202023-06-06%20at%208.39.52%20AM.png)


### Security Issues
![](../../../../../../../Assets/Pics/Screenshot%202023-06-06%20at%208.43.35%20AM.png)

算法本身的安全性依赖于有限域上计算离散对数的困难性。但协议在实际应用时，一定要引入某种鉴别机制，否则就容易 受到**中间人攻击 (man-in-the-middle attack)**

密钥协商协议应能同时鉴别参加者的身份，这种协议称为**鉴别密钥协商**。



## Ref

