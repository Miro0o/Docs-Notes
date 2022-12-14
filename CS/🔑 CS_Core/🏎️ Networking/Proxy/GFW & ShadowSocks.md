# The story is on ...

[TOC]



## 一切的开始

> [原文地址](https://shadowsockshelp.github.io/Shadowsocks/whats-shadowsocks.html)

#### 早期大陆互联网

很久以前，我们访问各种网站都是简单直接的，用户的请求通过互联网发送到服务提供方，服务提供方直接将信息反馈给用户。

![img](https://shadowsockshelp.github.io/Shadowsocks/img/shadowsocks01.png)

#### GFW 防火墙的出现

然后有一天[ GFW ](https://zh.wikipedia.org/wiki/金盾工程)就出现了，他像一个收过路费的强盗一样夹在了在用户和服务之间，每当用户需要获取信息，都经过了 GFW，GFW将它不喜欢的内容统统过滤掉，于是客户当触发 GFW 的过滤规则的时候，就会收到 Connection Reset 这样的响应内容，而无法接收到正常的内容。

![img](https://shadowsockshelp.github.io/Shadowsocks/img/shadowsocks02.png)

#### 关于 ssh tunnel

聪明的人们想到了利用境外服务器代理的方法来绕过 GFW 的过滤，其中包含了各种HTTP代理服务、Socks服务、VPN服务… 其中以 ssh tunnel 的方法比较有代表性。

1）首先用户和境外服务器基于 ssh 建立起一条加密的通道 2-3) 用户通过建立起的隧道进行代理，通过 ssh server 向真实的服务发起请求 4-5) 服务通过 ssh server，再通过创建好的隧道返回给用户。

![img](https://shadowsockshelp.github.io/Shadowsocks/img/shadowsocks03.png)

由于 ssh 本身就是基于 RSA 加密技术，所以 GFW 无法从数据传输的过程中的加密数据内容进行关键词分析，避免了被重置链接的问题，但由于创建隧道和数据传输的过程中，ssh 本身的特征是明显的，所以 GFW 一度通过分析连接的特征进行干扰，导致 ssh 存在被定向进行干扰的问题。

#### Shadowsocks的出现

于是[ clowwindy ](https://github.com/clowwindy/shadowsocks)同学分享并开源了他的解决方案。简单理解的话，shadowsocks 是将原来 ssh 创建的 Socks5 协议拆开成 server 端和 client 端，所以下面这个原理图基本上和利用 ssh tunnel 大致类似。

1、6) 客户端发出的请求基于 Socks5 协议跟 ss-local 端进行通讯，由于这个 ss-local 一般是本机或路由器或局域网的其他机器，不经过 GFW，所以解决了上面被 GFW 通过特征分析进行干扰的问题。

2、5) ss-local 和 ss-server 两端通过多种可选的加密方法进行通讯，经过 GFW 的时候是常规的TCP包，没有明显的特征码而且 GFW 也无法对通讯数据进行解密。

3、4) ss-server 将收到的加密数据进行解密，还原原来的请求，再发送到用户需要访问的服务，获取响应原路返回。

![img](https://shadowsockshelp.github.io/Shadowsocks/img/shadowsocks04.png)



## [The Great Firewall](https://en.wikipedia.org/wiki/Great_Firewall)

[深度包检测](https://zh.wikipedia.org/zh-cn/深度包检测)



## [Shadowsocks](https://github.com/shadowsocks)

🧭 [Shadowsocks 终极指南](https://shadowsockshelp.github.io)



### [SS 的历史背景](https://shadowsockshelp.github.io/Shadowsocks/Shadowsocks-wiki.html#ssr--)

#### 前言

翻越GFW有很多种方法，大浪淘沙，很多的方法都已经消失了，在我能够想起来的过去的，现在的，做一简单的记录：

##### 经典思路

1. 修改电脑内部的host文件，通过自主指定相关网站的IP地址的方式实现，这种方式现在依然存在；
2. GFW主要攻击手段之一是DNS污染，于是便有了强制指定DNS的方式以避免IP被污染的方法，这种方法经常会结合1使用；
3. 原本用来作为一种匿名，安全，保密的VPN服务也被发掘出翻墙的潜力，其原理比较简单，选择一个没有被GFW封杀的服务器，通过该服务器将相关网站的流量转发到自己的设备，而设备与VPN服务器之间的通信并不在GFW的屏蔽范围之内，于是便达成了翻墙的目的。VPN最初的目的是用于企业服务，方便员工远程登录企业内网进行操作，主要协议有PPTP、L2TP、IPsec、IKEv2、openVPN等等；
4. GoAgent，自由门，fqrouter等一系列网络服务；

##### 新思路

1. Shadowsocks类：主要包括各类Shadowsocks衍生版本，ShadowsocksR，Shadowsocks-libev等，特点是加密了通信过程中的数据；
2. 内网穿透：比较典型的是[ZeroTier](https://www.zerotier.com/)，简单解释就是假装自己在国外上网，这么说的主要原因是因为当两台设备同时加入到ZeroTier的服务器之后，两台设备会拥有同一IP段内的IP地址，此时两台电脑相当于处于局域网之中，可以用iPad连接电脑远程运行MATLAB，而VPN不可以；
3. V2Ray：V2Ray 是 Project V 下的一个工具。Project V 是一个包含一系列构建特定网络环境工具的项目，而 V2Ray 属于最核心的一个。官方中介绍Project V 提供了单一的内核和多种界面操作方式。内核（V2Ray）用于实际的网络交互、路由等针对网络数据的处理，而外围的用户界面程序提供了方便直接的操作流程。不过从时间上来说，先有 V2Ray才有Project V；
4. 大杀器：奇怪的名字，似乎是一个有趣的人开发的，个人没有关注过。



#### clowwindy 与 SS

[Solzhenitsyn: 'Spiritual Death Has... Touched Us All](https://www.washingtonpost.com/wp-dyn/content/article/2008/08/04/AR2008080401822_pf.html)



#### breakwa11 与 SSR



#### App Store VPN ban



#### Surge



#### Shadowrocket



#### Others

+ [Potatso Lite](https://shadowsockshelp.github.io/Potatso-Lite/) 

+ [Quantumult](https://itunes.apple.com/us/app/quantumult/id1252015438#?platform=iphone)

+ Postern
+ [SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega)
