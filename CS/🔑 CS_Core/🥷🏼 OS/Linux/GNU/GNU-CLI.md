# Gnutools

This page mainly focus on *GNU/Linux Core tools*. Check in  [**zsh.md**](../../../../Software/CLI/Shell&Emulator/zsh.md)  or [**iTterm2.md**](../../../../Software/CLI/Shell&Emulator/iTterm2.md) or [**🏫 Missing tutorial - MIT.md**](../../../../../🗺 CS_Overview/🏫 Missing tutorial - MIT.md) and their 🔗links at the bottom of the page for more possible info about other fancy CLI tools. 🎉



[TOC]

## GNU coreutils

TBD.

## net-tools

### iptables

`iptables` is designed for GNU/Linux hosts. For Unix-likes (like macOS) the countpart is `pfctl`.

Both of them server as a cli client of userspace communicating with core net filter module of kernelspace. The later functions as the actual net-pck maneger, or so-called firewall. 

In gnu/linux the core netfilter system is IP (), while Unix-likes PF (Packages Filter). 

>  👉 This series of article 🎉 [iptables 详解-- 朱双印的个人博客](https://www.zsythink.net/archives/tag/iptables/) is a great helper in understanding ipatebls
>
> 
>
> ![img](../../../../../../Assets/Pics/021217_0051_6.png)
>
> <small>Iptables architecture</small>





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



#### Refs:

[iptables: sport, dport 解释]:https://www.cnblogs.com/yjt1993/p/9504352.html

[linux中iptables配置文件及命令详解详解]: https://blog.csdn.net/Dexter_Wang/article/details/67634385



## Util-linux





## 🧑🏽‍💻 /usr/bin/

> Built-in Packages of some essencial tool set.

### `INFO`

`info` is a program (info reader) akin `man` . it is for online docs reading.

each entry is noted as `node`, and the whole documentation is organized as such nodes. 



#### `INFO` basics

-  `d`  --- to go to directory node (Info main menu)

	```shell
	
	This is the Info main menu (aka directory node).
	A few useful Info commands:
	
	  'q' quits;
	  'H' lists all Info commands;
	  'h' starts the Info tutorial;
	  'mTexinfo RET' visits the Texinfo manual, etc.
	
	* Menu:
	```
-  `b` --- to go to the top of the node
-  `t` --- go to the top node _(default entrance node)_ of the documentation
- `n` / `p` --- next/previous node on _parent level_
- `[` / `]` --- next/previous node on _same level_
- `[SPC]` / `[DEL]` --- next/previous page 
- `l` --- retrace to last node
- `u` --- move up to parent node 
- `m`--- menu 
- `f` --- find the cross-reference on the page
- `[TAB]` --- toggle between the cross-reference on the page
	+ --- text auto-completion



#### `INFO` advanced #unsolved

tbd...



### tar & compression

[Quick Benchmark: Gzip vs Bzip2 vs LZMA vs XZ vs LZ4 vs LZO](https://catchchallenger.first-world.info/wiki/Quick_Benchmark:_Gzip_vs_Bzip2_vs_LZMA_vs_XZ_vs_LZ4_vs_LZO)

[tar压缩解压缩命令详解](https://www.cnblogs.com/jyaray/archive/2011/04/30/2033362.html) 





## 🧑🏽‍💻 /sbin/

> System Level Packages providing Core Op.

### ping

> [📜 ping host:port 使用ping命令对特定端口访问](https://blog.csdn.net/allway2/article/details/106961916)



### [telent](https://www.cnblogs.com/peida/archive/2013/03/13/2956992.html)

telent $\subset$ TELENT $\subset$ TCP/IP
```shell
$ telnet <ip_address> <port_number>

$ telnet <domain_name> <port_number>
```

### [nc]()

```shell
$ nc -vz <host> <port_number>

$ nc -vz <domain> <port_number>
```

### [nmap]()

```shell
$ nmap -p 1-100 <ip_address>

$ nmap -p 1-100 <hostname>
```

### [powershell]()

```shell
$ Test-NetConnection <ip_address> -p <port_number>

$ Test-NetConnection 192.168.178.35 -p 389
```



### nsenter

>  [nsenter使用](https://www.cnblogs.com/edeny/p/15247306.html) 



TBD..



## 🧑🏽‍💻 /usr/local/bin

> User cumsotized tool sets.

### automake & autoconf

[automake, autoconf 使用详解](https://www.laruence.com/2009/11/18/1154.html)

TBD... 



## 🖇 Refs:

[七个 GNU 工具，命令行的强大功能与终端亲密接触的必备工具](https://www.51cto.com/article/706173.html)

