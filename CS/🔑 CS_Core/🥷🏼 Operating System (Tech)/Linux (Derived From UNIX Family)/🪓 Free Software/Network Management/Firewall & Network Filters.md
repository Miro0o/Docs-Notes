# Firewall & Network Filters

[TOC]



## Res



## Intro
### 👉 netfilter





## 👉 `iptables`
[Nettools / 👉 iptables](Nettools/Nettools.md#👉%20iptables)



### 👉 `ipset`



## 👉 `ufw`
### `Netfilter` 🆚 `Iptables` 🆚 `UFW`
↗ [FAQ / `Netfilter` 🆚 `Iptables` 🆚 `UFW` ?](../FAQ.md#`Netfilter`%20🆚%20`Iptables`%20🆚%20`UFW`%20?)



## 👉 `firewalld`
### `firewalld` 🆚 `iptables`
↗ [FAQ/ `firewalld` 🆚 `iptables`?](../FAQ.md#`firewalld`%20🆚%20`iptables`?)



## Ref
[How To Open a Port on Linux]: https://www.digitalocean.com/community/tutorials/opening-a-port-on-linux

[How to enable iptables (instead of firewalld) services on RHEL 7 and Fedora 18?]: https://serverfault.com/questions/470287/how-to-enable-iptables-instead-of-firewalld-services-on-rhel-7-and-fedora-18
```shell
yum install iptables-services
```

[How To Restart Iptables In Kali Linux]: https://www.systranbox.com/how-to-restart-iptables-in-kali-linux/

[Kali 防火墙配置]: https://www.cnblogs.com/aashui/p/8376257.html

[👍 firewalld和iptables区别]: https://www.cnblogs.com/mefj/p/13328360.html

[👍 How To Setup a Firewall with UFW on an Ubuntu and Debian Cloud Server]: https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server

[👍 Ufw and Iptables. Which is better and why? | StackExchange + serverFault]: https://serverfault.com/a/1014625/948999

[👍 firewalld vs iptables: when to use which | stackexchange]: https://serverfault.com/a/671975

As `firewalld` is based on XML configuration, some might think that it's easier to configure the firewall in a programmatic manner. This can be achieved by `iptables` just as well, but with a different way, which is not XML. If you are already familiar with the way `iptables` works, why would you migrate all your configuration to `firewalld`?

If you consider your largest `iptables` firewall rule set, how often do you think you would benefit from the dynamic aspect of `firewalld`? In most cases the performance of `iptables`is never the issue. In most cases where the performance of `iptables` is an issue can be fixed by using `ipset` based source/destination IP sets.

It is a different debate whether or not you should use NetworkManager.

[👍 firewalld和iptables区别]: https://www.cnblogs.com/mefj/p/13328360.html

在RHEL7里有几种防火墙共存：firewalld、iptables、ebtables，默认是使用firewalld来管理netfilter子系统，不过底层调用的命令仍然是iptables等。