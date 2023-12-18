# NAT (Network Address Translation)

[TOC]



## Res
👍 [「译」 NAT 穿透是如何工作的：技术原理及企业级实践（Tailscale, 2020）](https://arthurchiao.art/blog/how-nat-traversal-works-zh/)
- [How NAT traversal works](https://tailscale.com/blog/how-nat-traversal-works/)
- This article is archived into current folder in `.webarchive` extension, which is unseeable on obsidian.

>想了解更多新的 NAT 术语，可参考
> - RFC [4787](https://tools.ietf.org/html/rfc4787) (NAT Behavioral Requirements for UDP)
> - RFC [5382](https://tools.ietf.org/html/rfc5382) (for TCP)
> - RFC [5508](https://tools.ietf.org/html/rfc5508) (for ICMP)
>
>如果自己实现 NAT，那应该（should）遵循这些 RFC 的规范，这样才能使你的 NAT 行为符合业界惯例，与其他厂商的设备或软件良好兼容。



## Intro
NAT 是将一个地址域（如专用 Intranet）映射到另一个地址域（如 Internet）的标准方法，NAT 可以将内部网络中的所有节点的地址转换成一个 IP 地址，反之亦然。

![](../../../../../../../Assets/Pics/Screenshot%202023-12-16%20at%2011.02.51AM.png)


### NAT Working Principles
NAT 的实现方式有三种：静态网络地址转换、动态网络地址转换和网络地址端口映射。

![](../../../../../../../Assets/Pics/Screenshot%202023-12-16%20at%2011.01.37AM.png)
所谓静态地址转换，是指将公网 IP 地址一一对应地转换为内部私有 IP 地址

![](../../../../../../../Assets/Pics/Screenshot%202023-12-16%20at%2011.01.51AM.png)
动态地址转换将内部本地地址与内部合法地址一对一的进行转换，与静态地址转换不同的是它是从内部合法地址池动态分配临时的 IP 地址来对内部本地地址进行转换。

![](../../../../../../../Assets/Pics/Screenshot%202023-12-16%20at%2011.02.03AM.png)
网络地址端口映射就是将公网 IP 映射到私有 IP ，而外网多个 IP 被映射到同一内部共有 IP 地址的不同端口。

## Ref
[👍 Telegram: we get the IP address of the interlocutor]: https://n0a.pw/telegram-get-remote-ip/

