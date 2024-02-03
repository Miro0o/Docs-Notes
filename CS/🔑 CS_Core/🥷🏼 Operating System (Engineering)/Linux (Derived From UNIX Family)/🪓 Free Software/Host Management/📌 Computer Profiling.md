# Computer Profiling

[TOC]



## Res
↗ [Process Management Basics](../🪆%20Process%20Management/Process%20Management%20Basics.md)



## 🎯 System Configurations & Runtimes
### 👉 `lscpu`


### 👉 `lshw` | `hwinfo`


### 👉 `lnxi`
Inxi is a 10K line mega bash script that fetches hardware details from multiple different sources and commands on the system, and generates a beautiful looking report that non technical users can read easily.


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


### 👉 `getconf`




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
 `Dstat` is a versatile replacement for `vmstat`, `iostat` and `ifstat`. `Dstat` overcomes some of the limitations of these programs and adds some
 extra features.
#### 👉 `perf`
https://perf.wiki.kernel.org/index.php/Main_Page
perf: Linux profiling with performance counters


### Resource Virtualization
- [Flame Graph](http://www.brendangregg.com/flamegraphs.html)  
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

#### 👉 `vmstat`

#### 👉 `dmidecode`
The dmidecode command is different from all other commands. It extracts hardware information by reading data from the [SMBOIS data structures](https://en.wikipedia.org/wiki/System_Management_BIOS) (also called DMI tables).
#### 👉 `hdparm`

#### 👀 Looking up files under `/proc/`
You might be asking yourself, “Where do these commands get this information from?”. In some cases, they get it from the ==`/proc/meminfo`== file. Guess what? You can read that file directly with the command `less /proc/meminfo`.

One thing you should know about `/proc/meminfo`: This is not a real file. Instead `/pro/meminfo` is a virtual file that contains real-time, dynamic information about the system. In particular, you’ll want to check the values for:
- MemTotal
- MemFree
- MemAvailable
- Buffers
- Cached
- SwapCached
- SwapTotal
- SwapFree

If you want to get fancy with `/proc/meminfo` you can use it in conjunction with the egrep command like so: `egrep –color ‘Mem|Cache|Swap’ /proc/meminfo`. This will produce an easy to read listing of all entries that contain Mem, Cache, and Swap … with a splash of color.



## Ref
[16 Commands to Check Hardware Information on Linux]: https://www.binarytides.com/linux-commands-hardware-info/

[Linux下查看电脑硬件环境的命令]: https://blog.csdn.net/wjlwangluo/article/details/77511692

[Classic SysAdmin: Linux 101: 5 Commands for Checking Memory Usage in Linux]: https://www.linuxfoundation.org/blog/blog/classic-sysadmin-linux-101-5-commands-for-checking-memory-usage-in-linux

[dmidecode command in Linux with Examples]: https://www.geeksforgeeks.org/dmidecode-command-in-linux-with-examples/