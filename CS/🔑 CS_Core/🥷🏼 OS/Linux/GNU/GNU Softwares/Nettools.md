# Net-Tools

[TOC]



## Intro

**net-tools, the collection of base networking utilities for Linux.**

:house: Project Home: https://sourceforge.net/projects/net-tools/

:telephone: Commands: [arp(8)](https://net-tools.sourceforge.io/man/arp.8.html), [hostname(1)](https://net-tools.sourceforge.io/man/hostname.1.html), [ifconfig(8)](https://net-tools.sourceforge.io/man/ifconfig.8.html), ipmaddr, iptunnel, [mii-tool(8)](https://net-tools.sourceforge.io/man/mii-tool.8.html), [nameif(8)](https://net-tools.sourceforge.io/man/nameif.8.html), [netstat(8)](https://net-tools.sourceforge.io/man/netstat.8.html), [plipconfig(8)](https://net-tools.sourceforge.io/man/plipconfig.8.html), [rarp(8)](https://net-tools.sourceforge.io/man/rarp.8.html), [route(8)](https://net-tools.sourceforge.io/man/route.8.html) und [slattach(8)](https://net-tools.sourceforge.io/man/slattach.8.html).

Additional mal pages: [ethers(5)](https://net-tools.sourceforge.io/man/ethers.5.html) -- /etc/ethers file for arp(8)

NB: some projects (like Debian and RedHat) use a net-tools based but different **hostname** command.



## iptables

`iptables` is designed for GNU/Linux hosts. For Unix-likes (like macOS) the countpart is `pfctl`.

Both of them server as a cli client of userspace communicating with core net filter module of kernelspace. The later functions as the actual net-pck maneger, or so-called firewall. 

In gnu/linux the core netfilter system is IP (), while Unix-likes PF (Packages Filter). 

>  👉 This series of article 🎉 [iptables 详解-- 朱双印的个人博客](https://www.zsythink.net/archives/tag/iptables/) is a great helper in understanding ipatebls
>
>  
>
>  ![img](../../../../../../Assets/Pics/021217_0051_6.png)
>
>  <small>Iptables architecture</small>





TBD..



**Simple examples**:

```shell
# Rules op
sudo iptables -I INPUT -p tcp --dport 22 -j DROP
sudo iptables -I INPUT -m mac --mac-source xx:xx:xx:xx:xx:xx -j ACCEPT #设置指定mac地址客户端可以访问虚拟机
sudo iptables -I INPUT -s xxx.xxx.xxx.xxx -p tcp --dport 22 -j ACCEPT #设置指定ip地址客户端可以访问虚拟机

# Save changes
sudo apt install iptables-persistent
sudo iptables-save > /etc/iptables/rules.v4


```



### Refs:

[iptables: sport, dport 解释]:https://www.cnblogs.com/yjt1993/p/9504352.html

[linux中iptables配置文件及命令详解详解]: https://blog.csdn.net/Dexter_Wang/article/details/67634385