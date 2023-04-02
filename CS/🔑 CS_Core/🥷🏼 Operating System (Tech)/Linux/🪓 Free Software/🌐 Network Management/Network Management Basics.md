# Network Management Basics

[TOC]





## ping

> [📜 ping host:port 使用ping命令对特定端口访问](https://blog.csdn.net/allway2/article/details/106961916)



## [telent](https://www.cnblogs.com/peida/archive/2013/03/13/2956992.html)

telent $\subset$ TELENT $\subset$ TCP/IP

```shell
$ telnet <ip_address> <port_number>

$ telnet <domain_name> <port_number>
```



## [nc]()

```shell
$ nc -vz <host> <port_number>

$ nc -vz <domain> <port_number>
```



## [nmap]()

```shell
$ nmap -p 1-100 <ip_address>

$ nmap -p 1-100 <hostname>
```



## [powershell]()

```shell
$ Test-NetConnection <ip_address> -p <port_number>

$ Test-NetConnection 192.168.178.35 -p 389
```





## dhclient

Description: **The Internet Systems Consortium DHCP Client**, dhclient, provides a means for configuring one or more network interfaces using the Dynamic Host Configuration Protocol, BOOTP protocol, or if these protocols fail, by statically assigning an address.



