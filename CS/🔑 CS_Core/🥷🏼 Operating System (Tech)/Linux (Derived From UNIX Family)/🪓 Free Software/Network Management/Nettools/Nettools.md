# Net-Tools

[TOC]



## Res
🏠 Project Home: https://sourceforge.net/projects/net-tools/

☎ Commands: [arp(8)](https://net-tools.sourceforge.io/man/arp.8.html), [hostname(1)](https://net-tools.sourceforge.io/man/hostname.1.html), [ifconfig(8)](https://net-tools.sourceforge.io/man/ifconfig.8.html), ipmaddr, iptunnel, [mii-tool(8)](https://net-tools.sourceforge.io/man/mii-tool.8.html), [nameif(8)](https://net-tools.sourceforge.io/man/nameif.8.html), [netstat(8)](https://net-tools.sourceforge.io/man/netstat.8.html), [plipconfig(8)](https://net-tools.sourceforge.io/man/plipconfig.8.html), [rarp(8)](https://net-tools.sourceforge.io/man/rarp.8.html), [route(8)](https://net-tools.sourceforge.io/man/route.8.html) und [slattach(8)](https://net-tools.sourceforge.io/man/slattach.8.html).

Additional mal pages: [ethers(5)](https://net-tools.sourceforge.io/man/ethers.5.html) -- /etc/ethers file for arp(8)

NB: some projects (like Debian and RedHat) use a net-tools based but different **hostname** command.



## Intro
**net-tools, the collection of base networking utilities for Linux.**



## 👉 `ifconfig`
`ifconfig` (interface configuration) command is used to configure the kernel-resident network interfaces. It is used at the boot time to set up the interfaces as necessary. After that, it is usually used when needed during debugging or when you need system tuning. Also, this command is used to assign the IP address and netmask to an interface or to enable or disable a given interface.

```shell
# ifconfig
# Network Interface Configurator.
# More information: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

# View network settings of an Ethernet adapter:
ifconfig eth0

# Display details of all interfaces, including disabled interfaces:
ifconfig -a

# Assign IP address to eth0 interface:
ifconfig eth0 ip_address

# To take down / up the wireless adapter:
ifconfig wlan0 {up|down}

# To set a static IP and netmask:
ifconfig eth0 192.168.1.100 netmask 255.255.255.0

# You may also need to add a gateway IP:
route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1
```

ifconfig returns DHCP configured information of the host. 
- `ine`t: The IP information obtained by the DHCP server should provide us with at least one active subnet which can be utilized to identify the list of live systems and services through different scanning techniques.
- `netmask`: This information can be utilized to calculate the subnet ranges. From the previous screenshot, we have `255.255.240.0`, which means CIDR is /20 and potentially we can expect `4094` hosts on the same subnet.
- **Default gateway**: The IP information of the gateway will provide the opportunity to ping other similar gateway IP's. For example, if your default gateway IP is `192.168.1.1` by using ping scans attackers may be able to enumerate other similar IPs such as `192.168.2.1`, `192.168.3.1`, and so on.
-  **Other IP address**: DNS information can be obtained by accessing the `/etc/resolv.conf` file. The IP addresses in this file are commonly addressed in all of the subnets and domain information will also be automatically available in the same file.



## 👉 `iptables`
> 🫵🏽 `iptables` is designed for GNU/Linux hosts. For Unix-likes (like macOS) the countpart is `pfctl` at ↗ [Network Management](../../../../Apple/macOS%20(Derived%20From%20UNIX%20Family)/🪓%20macOS%20CLI%20Software/Network%20Management/Network%20Management.md)
> 
> Both of them server as a cli client of userspace communicating with core **net filter module** of kernelspace. The later functions as the actual net-pck maneger, or so-called firewall. 
> 
> In gnu/linux the core netfilter system is `IP`, while Unix-likes `PF` (Packages Filter). 

>  👉 This series of article 🎉 [iptables 详解-- 朱双印的个人博客](https://www.zsythink.net/archives/tag/iptables/) is a great helper in understanding ipatebls
>  ![img](../../../../../../../Assets/Pics/021217_0051_6.png)
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



## 👉 `netstat`




## Ref
[iptables: sport, dport 解释]: https://www.cnblogs.com/yjt1993/p/9504352.html

[linux中iptables配置文件及命令详解详解]: https://blog.csdn.net/Dexter_Wang/article/details/67634385
