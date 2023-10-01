# FAQ

[TOC]



## 👉 firewalld & iptables & ebtables & UFW & others
#firewalld #iptables #ebtables #ufw #firewall 

### `Netfilter` 🆚 `Iptables` 🆚 `UFW`
UFW and Iptables are related because UFW is essentially a simpler interface for managing Iptables. The main difference between them is, how much control you want over your firewall configuration:
- **Netfilter**: The lowest level, making pizza from scratch at home. Requires the most knowledge but gives you the most control.
- **Iptables**: A layer on top of Netfilter. It's like buying a pizza kit that you cook yourself. You have less control, but it's easier to manage.
- **UFW**: Further simplification, similar to ordering a pizza for delivery. You have even less control, but it's even easier to use.
- **Predefined setups**: The simplest option, it's like dining out at a restaurant. You have minimal control, but it's the easiest to use. The 'better' choice depends on your needs and comfort level with managing firewall rules.

---
**part I:** i found a pretty decent and easy to understand article for the UFW: [Understanding UFW](https://hackernoon.com/understanding-ufw-8d70d5d8f9d2) (on HackerNoon)

**part II:** this guide shows you the slight deeper using of iptables: [The Beginner’s Guide to iptables, the Linux Firewall](https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/) (on HowToGeek)

**part III:** here are informations about the packetfilter, this is the basis of many firewall solutions [A Deep Dive into Iptables and Netfilter Architecture](https://www.digitalocean.com/community/tutorials/a-deep-dive-into-iptables-and-netfilter-architecture) (on DigitalOcean)

the parts are based on hierarchy, top is dependant on the lower ones.

---
**Further Reading**
1. **UFW:** This **[HackerNoon article](https://hackernoon.com/understanding-ufw-8d70d5d8f9d2)** provides a good overview of UFW.
2. **Iptables:** This **[HowToGeek guide](https://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/)** goes a bit deeper into using Iptables.
3. **Netfilter:** This **[DigitalOcean article](https://www.digitalocean.com/community/tutorials/a-deep-dive-into-iptables-and-netfilter-architecture)** dives deep into the architecture of Iptables and Netfilter, which is the foundation for many firewall solutions.


[👍 Ufw and Iptables. Which is better and why? | StackExchange + serverFault]: https://serverfault.com/a/1014625/948999


### `firewalld` 🆚 `iptables`

在RHEL7里有几种防火墙共存：firewalld、iptables、ebtables，默认是使用firewalld来管理netfilter子系统，不过底层调用的命令仍然是iptables等。

firewalld跟iptables比起来至少有两大好处：
1、firewalld可以动态修改单条规则，而不需要像iptables那样，在修改了规则后必须得全部刷新才可以生效；

2、firewalld在使用上要比iptables人性化很多，即使不明白“五张表五条链”而且对TCP/IP协议也不理解也可以实现大部分功能。

firewalld跟iptables比起来，不好的地方是每个服务都需要去设置才能放行，因为默认是拒绝。而iptables里默认是每个服务是允许，需要拒绝的才去限制。

firewalld自身并不具备防火墙的功能，而是和iptables一样需要通过内核的netfilter来实现，也就是说firewalld和 iptables一样，他们的作用都是用于维护规则，而真正使用规则干活的是内核的netfilter，只不过firewalld和iptables的结构以及使用方法不一样罢了。


[👍 firewalld和iptables区别]: https://www.cnblogs.com/mefj/p/13328360.html


---
As `firewalld` is based on XML configuration, some might think that it's easier to configure the firewall in a programmatic manner. This can be achieved by `iptables` just as well, but with a different way, which is not XML. If you are already familiar with the way `iptables` works, why would you migrate all your configuration to `firewalld`?

If you consider your largest `iptables` firewall rule set, how often do you think you would benefit from the dynamic aspect of `firewalld`? In most cases the performance of `iptables`is never the issue. In most cases where the performance of `iptables` is an issue can be fixed by using `ipset` based source/destination IP sets.

It is a different debate whether or not you should use NetworkManager.


[👍 firewalld vs iptables: when to use which | stackexchange]: https://serverfault.com/a/671975