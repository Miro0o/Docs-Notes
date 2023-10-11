# Network Management Basics

[TOC]



## Res
↗ [Reconnaissance & Exploration](../../../../../CyberSecurity/☠️%20Kill%20Chain/🤔%20Pen-testing%20Tools/Reconnaissance%20&%20Exploration/Reconnaissance%20&%20Exploration.md)



## RPC /File Transmission
### 👉 `telent` | `SSH` | `Powershell` 
[telent](https://www.cnblogs.com/peida/archive/2013/03/13/2956992.html)
telent $\subset$ TELENT $\subset$ TCP/IP
```shell
$ telnet <ip_address> <port_number>

$ telnet <domain_name> <port_number>
```

↗ [SSH (Secure SHell)](../../../../../CyberSecurity/Network%20Security/🏇%20Network%20Security%20Basics%20&%20Protocols/📱%20Application%20Layer%20Security%20Protocols/SSH%20(Secure%20SHell)/SSH%20(Secure%20SHell).md)


powershell
```shell
$ Test-NetConnection <ip_address> -p <port_number>

$ Test-NetConnection 192.168.178.35 -p 389
```


### 👉 `ssh` -> `mosh` | `et`
**[SSH](https://www.openssh.com/)** stands for Secure Shell. It's the de facto standard for secure communication between two hosts on internet (LAN as well). 

**[Mosh](https://github.com/jarun/nnn/tree/master/plugins#installation)** is improved ssh. It adds some convinient features for dev test settings, though it has security concern under production environment for its UDP usage and port number attribution strategy. However, some of it's fancy functions such as internet roam and autometically reconnect after exiting shell still makes it a handy tool in dev.

[**Eternal Terminal (ET)**](https://eternalterminal.dev) is a remote shell that automatically reconnects without interrupting the session. Learn how to install and use it 📂 [here](https://eternalterminal.dev/usermanual).

ET is inspired & based on [**mosh**](https://mosh.org/). ([ssh](https://www.openssh.com/) and [autossh](https://linux.die.net/man/1/autossh) as well)


### 👉 `curl` | `wget`


```shell
wget -r -np -nH -R index.html http://url/including/files/you/want/to/download/
# -r : 遍历所有子目录
# -np : 不到上一层子目录去
# -nH : 不要将文件保存到主机名文件夹
# -R index.html: 不下载 index.html 文件
```



[linux服务器之间传输文件的四种方式]: https://blog.csdn.net/qw_xingzhe/article/details/80167888
[Linux curl 命令下载文件]: https://www.cnblogs.com/hujiapeng/p/8470099.html



## Network Profiling
### Network Connections & Configuration
#### 👉 Basic Network Configuration & Net-tools
↗ [Nettools](Nettools/Nettools.md)


#### 👉 dhclient
Description: **The Internet Systems Consortium DHCP Client**, dhclient, provides a means for configuring one or more network interfaces using the Dynamic Host Configuration Protocol, BOOTP protocol, or if these protocols fail, by statically assigning an address.


#### 👉 `netstat` (deprecated) --> `ss` | `hashcat`


#### 👉 `ifconfig` (deprecated) --> `ip` | `ipconfig`
↗ [Nettools](Nettools/Nettools.md#👉%20ifconfig)


### 👉 `bind9` | `dnsutils`



### Network Usage
#### 👉 `nethogs`
 [`nethogs`](https://github.com/raboof/nethogs)


#### 👉 `iftop`
[`iftop`](http://www.ex-parrot.com/pdw/iftop/)


#### 👉 `nload`

[Linux系统nload命令查看网速流量]: https://www.5yun.org/20932.html) 




## Network Security Management



## Ref