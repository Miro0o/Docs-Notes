# Computer Profiling

[TOC]



## Res
↗ [Process Management Basics](../🪆%20Process%20Management/Process%20Management%20Basics.md)



## 🎯 System Configurations & Runtimes
### 👉 `lscpu`


### 👉 `lshw` | `hwinfo`


### 👉 `lnxi`
Inxi is a 10K line mega bash script that fetches hardware details from multiple different sources and commands on the system, and generates a beautiful looking report that non technical users can read easily.


### 👉 `dmidecode`
The dmidecode command is different from all other commands. It extracts hardware information by reading data from the [SMBOIS data structures](https://en.wikipedia.org/wiki/System_Management_BIOS) (also called DMI tables).


### 👉 `uname`


### 👉 `hostname` | `hostnamectl`
Display the system's hostname using:
```shell
$ hostname
```

You can also use the `hostname` command to modify the system's name temporarily. Here's an example:
```shll
$ hostname demo.example.com
```

To persistently change the hostname, use the `hostnamectl` command, or directly modify the default configuration file `/etc/hostname`.
```shell
 hostnamectl set-hostname server1.example.com
```

[如何在 Ubuntu 20.04 上修改主机名]: https://cloud.tencent.com/developer/article/1649332


### 👉 getconf




## 🎯 Interfaces Info
### 👉 `lspci` | `lsscsi` | `lsusb`



## 🎯 Logging
### 👉 `dmesg`
[dmesg](https://www.man7.org/linux/man-pages/man1/dmesg.1.html)


### 👉 `log` | `syslog` | `logger` | `journalctl`
[log show](https://www.manpagez.com/man/1/log/) 

[logger](https://www.man7.org/linux/man-pages/man1/logger.1.html) 

[journalctl](https://www.man7.org/linux/man-pages/man1/journalctl.1.html) 


### 👉 `lnav`
[lnav](http://lnav.org/)



## 🎯 Signals
### System Calls
#### 👉 `strace` | `dtrace` | `dtruss`
[strace](https://www.man7.org/linux/man-pages/man1/strace.1.html)
[dtrace](http://dtrace.org/blogs/about/)
[dtruss](https://www.manpagez.com/man/1/dtruss/)



## 🎯 Resource Monitoring
### General Monitoring
#### 👉 `top` | `htop` | `gtop`


#### 👉 `glances`


#### 👉 `dstat`

### Resource Virtualiztion
-  [Flame Graph](http://www.brendangregg.com/flamegraphs.html)  
- python -m [pycallgraph](https://pycallgraph.readthedocs.io/) 



### Timing


### CPU Profiler
- There are two main types of CPU profilers: *tracing* and *sampling* profilers. 

- python - cProfile

-  [line_profiler](https://github.com/pyutils/line_profiler)


### I/O Operations
#### 👉 `iotop`


### Process/ Jobs Activity
↗ [Process Management Basics](../🪆%20Process%20Management/Process%20Management%20Basics.md)


### Network Profiling
↗ [Network Management Basics](../Network%20Management/Network%20Management%20Basics.md)


### Disk /Memory Usage
[Valgrind](https://valgrind.org/) 
- [memory-profiler](https://pypi.org/project/memory-profiler/)


#### 👉 `du` | `ncdu`
The du command is a standard Linux/Unix command that **allows a user to gain disk usage information quickly**. It is best applied to specific directories and allows many variations for customizing the output to meet your needs. As with most commands, the user can take advantage of many options or flags.



#### 👉 `lsblk` | `df` | `pydf`


#### 👉 `fdisk` | `hdisk` | `mount` | `free`


#### 👉 `hdparm`


#### 👀 Looking up files under `/proc/`





## Ref
[16 Commands to Check Hardware Information on Linux]: https://www.binarytides.com/linux-commands-hardware-info/

[Linux下查看电脑硬件环境的命令]: https://blog.csdn.net/wjlwangluo/article/details/77511692

