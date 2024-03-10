# Network Management Basics

[TOC]



## Res
↗ [Reconnaissance & Exploration](../../../../../CyberSecurity/☠️%20Kill%20Chain/Pen-testing%20Tools/Reconnaissance%20&%20Exploration/Reconnaissance%20&%20Exploration.md)



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


### 👉 `ssh` -> `mosh` /`autossh` -> `et`
**[SSH](https://www.openssh.com/)** stands for Secure Shell. It's the de facto standard for secure communication between two hosts on internet (LAN as well). 

**[Mosh](https://github.com/jarun/nnn/tree/master/plugins#installation)** is improved ssh. It adds some convinient features for dev test settings, though it has security concern under production environment for its UDP usage and port number attribution strategy. However, some of it's fancy functions such as internet roam and autometically reconnect after exiting shell still makes it a handy tool in dev.

[**Eternal Terminal (ET)**](https://eternalterminal.dev) is a remote shell that automatically reconnects without interrupting the session. Learn how to install and use it 📂 [here](https://eternalterminal.dev/usermanual).

ET is inspired & based on [**mosh**](https://mosh.org/). ([ssh](https://www.openssh.com/) and [autossh](https://linux.die.net/man/1/autossh) as well)


### 👉 `curl` | `wget`

`curl` is a tool for transferring data from or to a server using URLs. It supports these protocols:
> DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S,RTMP, RTMPS, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET, TFTP, WS and WSS.

`curl` is powered by `libcurl` for all transfer-related features.

---
GNU `Wget` is a free utility for non-interactive download of files from the Web.  It supports HTTP, HTTPS, and FTP protocols, as well as retrieval through HTTP proxies.

`Wget` is non-interactive, meaning that it can work in the background, while the user is not logged on.  This allows you to start a retrieval and disconnect from the system, letting `Wget` finish the work.  By contrast, most of the Web browsers require constant user's presence, which can be a great hindrance when transferring a lot of data.

`Wget` can follow links in HTML, XHTML, and CSS pages, to create local versions of remote web sites, fully recreating the directory structure of the original site.  This is sometimes referred to as "**recursive downloading**."  While doing that, `Wget` respects the Robot Exclusion Standard (/robots.txt).  `Wget` can be instructed to convert the links in downloaded files to point at the local files, for offline viewing.

`Wget` has been designed for robustness over slow or unstable network connections; if a download fails due to a network problem, it will keep retrying until the whole file has been retrieved.  If the server supports regetting, it will instruct the server to continue the download from where it left off.


```shell
wget -r -np -nH -R index.html http://url/including/files/you/want/to/download/
# -r : 遍历所有子目录
# -np : 不到上一层子目录去
# -nH : 不要将文件保存到主机名文件夹
# -R index.html: 不下载 index.html 文件
```


[curl VS wget]: https://www.baeldung.com/linux/curl-wget

**_wget_ is a simpler solution and only supports a small number of protocols.** It is very good for downloading files and can download directory structures recursively.
We also saw how **_curl_ supports a much larger range of protocols, making it a more general-purpose tool.**

- Protocol
	- HTTP
	- `CURL` --> STDOUT (console/terminal as default),  general-purpose tool for transferring data to or from a server.
	- `wget` --> specific file ,  basically a network downloader.
- Recursive download
	- http: _wget_ is _breadth-first_
	- ftp: _wget_ is _depth-first_

[linux服务器之间传输文件的四种方式]: https://blog.csdn.net/qw_xingzhe/article/details/80167888
[Linux curl 命令下载文件]: https://www.cnblogs.com/hujiapeng/p/8470099.html

[Downloading file from FTP using cURL]: https://superuser.com/a/265066/1656771



## Network Profiling
### Network Connections & Configuration
#### Basic Network Configuration & Net-tools
↗ [Nettools](Nettools.md)
#### 👉 `dhclient`
Description: **The Internet Systems Consortium DHCP Client**, dhclient, provides a means for configuring one or more network interfaces using the Dynamic Host Configuration Protocol, BOOTP protocol, or if these protocols fail, by statically assigning an address.
#### 👉 `netstat` (deprecated) --> `ss` | `hashcat`
↗ [Nettools /👉 `netstat`](Nettools.md#👉%20`netstat`)

#### 👉 `ifconfig` (deprecated) --> `ip`
↗ [Nettools /👉 ifconfig](Nettools.md#👉%20ifconfig)

#### 👉 `bind9` | `dnsutils`


### Network Usage
#### 👉 `nethogs`
 [`nethogs`](https://github.com/raboof/nethogs)
#### 👉 `iftop`
[`iftop`](http://www.ex-parrot.com/pdw/iftop/)
#### 👉 `nload`

[Linux系统nload命令查看网速流量]: https://www.5yun.org/20932.html) 


### Package Analysis
↗ [Packet Analyzing & Sniffing & Spoofing](../../../../🏎️%20Computer%20Networking%20and%20Communication/🎅🏼%20Network%20Programming%20&%20RPC/Packet%20Analyzing%20&%20Sniffing%20&%20Spoofing/Packet%20Analyzing%20&%20Sniffing%20&%20Spoofing.md)
↗ [Network Diagnostic & Packet Analysis](Network%20Diagnostic%20&%20Packet%20Analysis.md)
#### 👉 `ngrep`
#### 👉 `tcpdump`
↗ [tcpdump](../../../../🏎️%20Computer%20Networking%20and%20Communication/🎅🏼%20Network%20Programming%20&%20RPC/Packet%20Analyzing%20&%20Sniffing%20&%20Spoofing/tcpdump.md)



## Ref