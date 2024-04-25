# Proxy

[TOC]


## Res
### Related Topics
↗ [OpenVPN Project & OpenVPN Community Project](../👻%20Tunneling%20&%20VPN/VPN%20&%20NAT%20Implementations/📌%20OpenVPN%20Project%20&%20OpenVPN%20Community%20Project/OpenVPN%20Project%20&%20OpenVPN%20Community%20Project.md)
↗ [WireGuard](../👻%20Tunneling%20&%20VPN/VPN%20&%20NAT%20Implementations/VPN%20&%20NAT%20Free%20Software/WireGuard.md)



### Proxy & GFW Info
[墙知乎](https://wallzhihu.com)

🔗 https://www.duyaoss.com
duyaoss机场测速

🔗 https://9.234456.xyz/abc.html
机场推广列表

### Proxy Service Providers
1. [qianglie](https://www.qianglie.com/#/profile)
2. [AgentNEO](https://neoladder.com/dashboard)
3. [GLaDOS](https://glados.rocks/register)
	1. SPV54-EMK9S-HUH77-QXWB0
4. [米白云](https://docs.mebi.me/docs/intro)
	1. 没用过，不知道怎么样；文档写得挺好看的
5. [搬瓦工机场 Just My Socks](https://justmysockss.org/)
2. [wgetcloud](https://invite.wgetcloud.ltd/auth/register?code=oikW)
3. [搬瓦工自建](https://v2ray-x.com/banwagon-v2ray/)

美国住宅IP代理可以使用：[https://oxylabs.io/](https://oxylabs.io/)，按流量计费，$15/G，按需使用，建议使用switchOmega浏览器插件设置只对openai.com域名走代理，跑不了多少流量。

住宅IP的vps可以使用：[https://www.soladrive.com/support/aff.php?aff=146](https://www.soladrive.com/support/aff.php?aff=146)，进入网站后选择Residential IP VPS即可，$25每月，流量2T/月，适合于平时除了用chatGPT还顺便用来解锁netflix看看视频的。


### Guidelines
🚧 https://github.com/hoochanlon/fq-book
📖《网络代理与VPN应用详解》 详细阐述代理、隧道、VPN运作过程，并对GFW策略如：地址端口封锁、服务器缓存投毒、数字验证攻击、SSL连接阻断做相关的原理说明



## Intro



## GFW 🇨🇳 & Countermoves
### 🚧 What is GFW?
↗ [Internet Censorship & GFW (Great FireWall)](../Internet%20Censorship%20&%20GFW%20(Great%20FireWall).md)


### Methods of bypassing the firewall
> 🔗 https://shadowsockshelp.github.io/Shadowsocks/Shadowsocks-wiki.html#ssr-- (2021)

翻越GFW有很多种方法，大浪淘沙，很多的方法都已经消失了，在我能够想起来的过去的，现在的，做一简单的记录：

1. 经典思路
	1. 修改电脑内部的host文件，通过自主指定相关网站的IP地址的方式实现，这种方式现在依然存在；
	2. GFW主要攻击手段之一是DNS污染，于是便有了强制指定DNS的方式以避免IP被污染的方法，这种方法经常会结合1使用；
	3. 原本用来作为一种匿名，安全，保密的VPN服务也被发掘出翻墙的潜力，其原理比较简单，选择一个没有被GFW封杀的服务器，通过该服务器将相关网站的流量转发到自己的设备，而设备与VPN服务器之间的通信并不在GFW的屏蔽范围之内，于是便达成了翻墙的目的。VPN最初的目的是用于企业服务，方便员工远程登录企业内网进行操作，主要协议有PPTP、L2TP、IPsec、IKEv2、openVPN等等；
	4. GoAgent，自由门，fqrouter等一系列网络服务；

2. 新思路
	1. Shadowsocks类：主要包括各类Shadowsocks衍生版本，ShadowsocksR，Shadowsocks-libev等，特点是加密了通信过程中的数据；
	2. 内网穿透：比较典型的是[ZeroTier](https://www.zerotier.com/)，简单解释就是假装自己在国外上网，这么说的主要原因是因为当两台设备同时加入到ZeroTier的服务器之后，两台设备会拥有同一IP段内的IP地址，此时两台电脑相当于处于局域网之中，可以用iPad连接电脑远程运行MATLAB，而VPN不可以；
	3. V2Ray：V2Ray 是 Project V 下的一个工具。Project V 是一个包含一系列构建特定网络环境工具的项目，而 V2Ray 属于最核心的一个。官方中介绍Project V 提供了单一的内核和多种界面操作方式。内核（V2Ray）用于实际的网络交互、路由等针对网络数据的处理，而外围的用户界面程序提供了方便直接的操作流程。不**过从时间上来说，先有 V2Ray才有Project V**；
	4. 大杀器：奇怪的名字，似乎是一个有趣的人开发的，个人没有关注过。


> 🔗 https://en.wikipedia.org/wiki/Great_Firewall#Circumvention (2022)

Because the Great Firewall blocks destination IP addresses and domain names and inspects the data being sent or received, a basic censorship circumvention strategy is to **1️⃣ use proxy nodes** and **2️⃣ encrypt the data**. Bypassing the firewall is known as _fānqiáng_ (翻墙, "climb over the wall"), and most circumvention tools combine these two mechanisms:

1. via proxy nodes
	- [Proxy servers](https://en.wikipedia.org/wiki/Proxy_server "Proxy server") outside China can be used, although using just a simple open proxy (HTTP or SOCKS) without also using an encrypted tunnel (such as HTTPS) does little to circumvent the sophisticated censors.
	- [Freegate](https://en.wikipedia.org/wiki/Freegate "Freegate"), [Ultrasurf](https://en.wikipedia.org/wiki/Ultrasurf "Ultrasurf"), [Psiphon](https://en.wikipedia.org/wiki/Psiphon "Psiphon"), and [Lantern](https://en.wikipedia.org/wiki/Lantern_(software) "Lantern (software)") are free programs designed and experienced with circumventing the China firewall using multiple [open proxies](https://en.wikipedia.org/wiki/Open_proxies "Open proxies").
	- [VPNs](https://en.wikipedia.org/wiki/VPN "VPN") (virtual private networks) are one of the most popular tools used by Westerners for bypassing censorship technologies. They use the same basic approaches, proxies, and encrypted channels used by other circumvention tools, but depend on a private host, a virtual host, or an account outside of China, rather than open, free proxies.
	- [Tor](https://en.wikipedia.org/wiki/Tor_(anonymity_network) "Tor (anonymity network)") partially can be used in China. Since 2010, almost all bridges at TorProject.org are blocked through [proxy distribution](https://en.wikipedia.org/wiki/Great_Firewall#Proxy_distribution). Tor still functions in China using Snowflake, independently published Obfs4 bridges and meek.
	- [I2P](https://en.wikipedia.org/wiki/I2P "I2P") or [garlic routing](https://en.wikipedia.org/wiki/Garlic_routing "Garlic routing") is useful when properties similar to Tor's anonymity are needed. Due to I2P being much less popular than Tor, it has faced little to no blocking attempts.

2. Non-proxy circumvention strategies include:
	- Using [encrypted DNS](https://en.wikipedia.org/wiki/DNS_over_HTTPS "DNS over HTTPS") may bypass blocking of a few sites including TorProject and all of GitHub, which may be used to obtain further circumvention. In 2019 Firefox released an update to make it easy to enable DNS over HTTPS. Despite DNS over encryption, the majority of services remain blocked by IP.
	- Ignoring TCP reset packets sent by the GFW. Distinguishing them by the TTL value (time to live), and not routing any further packets to sites that have triggered blocking behavior.
	- There is a popular rumour that using [IPv6](https://en.wikipedia.org/wiki/IPv6 "IPv6") bypasses [DPI](https://en.wikipedia.org/wiki/Deep_packet_inspection "Deep packet inspection") filtering in China. The academic community is yet to confirm.


#### Known blocked methods (2022)
- The [OpenVPN](https://en.wikipedia.org/wiki/OpenVPN "OpenVPN") protocol is detected and blocked. Connections not using symmetric keys or using "tls-auth" are blocked at handshake, and connections using the new "tls-crypt" option are detected and throttled (under 56kbit/s) by the QoS filtering system.
- [GRE](https://en.wikipedia.org/wiki/Generic_Routing_Encapsulation "Generic Routing Encapsulation") tunnels and protocols that use GRE (e.g., [PPTP](https://en.wikipedia.org/wiki/PPTP "PPTP")) are blocked.
- [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security "Transport Layer Security"), the Great Firewall can identify the difference between HTTPS TLS and other implementations by inspecting the handshake parameters


### Development of Proxy Software & Protocols
#### 1️⃣ clowwindy & SS
[Solzhenitsyn: 'Spiritual Death Has... Touched Us All](https://www.washingtonpost.com/wp-dyn/content/article/2008/08/04/AR2008080401822_pf.html)


#### 2️⃣ breakwa11 & SSR


#### 3️⃣ App Store VPN ban


#### 4️⃣ Surge


#### 4️⃣ ShadowSocketRocket (SSR)


#### Others
+ [Potatso Lite](https://shadowsockshelp.github.io/Potatso-Lite/) 
+ [Quantumult](https://itunes.apple.com/us/app/quantumult/id1252015438#?platform=iphone)
+ Postern
+ [SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega)



## Ref
[机场推荐]:https://pawswrite.xyz/posts/33840.html#测速结果

1. 🫰[duyao 机场测速](https://www.duyaoss.com)
2. 🫰[机场常见名词](https://young1lin.me/2020/10/30/GFW/#机场)
3. [Speech that Enables Speech: China Takes Aim at Its Coders](https://www.eff.org/deeplinks/2015/08/speech-enables-speech-china-takes-aim-its-coders)
4. [Solzhenitsyn: 'Spiritual Death Has... Touched Us All'](https://www.washingtonpost.com/wp-dyn/content/article/2008/08/04/AR2008080401822_pf.html)
5. [Mac让Mail(自带邮箱客户端)的gmail走代理及终端走代理](https://www.xiebruce.top/1061.html)

[拆解“翻墙”：50个“翻墙”行政处罚案例之解析]: https://mp.weixin.qq.com/s/4AUBEY39EaIhbxjO94J7Og

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaSnMfKUYm4sOz6tmzmupuLMQFxalo6DkfFsqbg1ibgCq7z3tIepetsiaDnuUUunds8fgsb7VoeF20DnpA29sZ1icA/640?wx_fmt=png)

[SwitchyOmega | github]: https://github.com/FelisCatus/SwitchyOmega
