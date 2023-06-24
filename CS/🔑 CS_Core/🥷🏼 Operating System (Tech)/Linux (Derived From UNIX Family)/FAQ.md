# FAQ

[TOC]



## 🏞 Software Management
### 👉 Source release & Binary Release?
see [this](https://stackoverflow.com/a/5280925/16542494) answer on stack overflow. A source release is the source code of the packeg, which means user have to compile and construct the software themselves. While Binary release is the to-go software. 



## 🗄 File Management
### 👉 diff between hard linlk & soft link (symlink, symbolic link)

![Pictorial representation](../../../../../Assets/Pics/f7Ijz.jpg)
<small>This illustration is not acurate though</small>

#### Unix File System
Unix files consist of two parts: the data part and the filename part.
```shell
# the data part:

                               .---------------> ! data ! ! data ! etc
                              /                  +------+ +------+
        ! permbits, etc ! data addresses !
        +------------inode---------------+
        
        
# the filename part: 

                        .--------------> ! permbits, etc ! addresses !
                        /                 +---------inode-------------+
        ! filename ! inode # !
        +--------------------+
```

The hark link is two filename referring to the same inode number:
```shell
        ! filename ! inode # !
        +--------------------+
                        \
                         >--------------> ! permbits, etc ! addresses !
                        /                 +---------inode-------------+
        ! othername ! inode # !
        +---------------------+
```

While the soft link (or symbolic link, symlink ) is the redirection of filename link: 
```shell
       ! filename ! inode # !
        +--------------------+
                        \
                         .-------> ! permbits, etc ! addresses !
                                   +---------inode-------------+
                                                      /
                                                     /
                                                    /
    .----------------------------------------------'
   ( 
    '-->  !"/path/to/some/other/file"! 
          +---------data-------------+
                  /                      }
    .~ ~ ~ ~ ~ ~ ~                       }-- (redirected at open() time)
   (                                     }
    '~~> ! filename ! inode # !
         +--------------------+
                         \
                          '------------> ! permbits, etc ! addresses !
                                         +---------inode-------------+
                                                            /
                                                           /
     .----------------------------------------------------'
    (
     '->  ! data !  ! data ! etc.
          +------+  +------+ 

```

Now, the filename part of the file is stored in a special file of its own along with the filename parts of other files; this special file is called a directory. The directory, as a file, is just an array of filename parts of other files.

When a directory is built, it is initially populated with the filename parts of two special files: the '.' and '..' files. The filename part for the '.' file is populated with the inode# of the directory file in which the entry has been made; '.' is a hardlink to the file that implements the current directory.

The filename part for the '..' file is populated with the inode# of the directory file that contains the filename part of the current directory file. '..' is a hardlink to the file that implements the immediate parent of the current directory.

The 'ln' command knows how to build hardlinks and softlinks; the 'mkdir' command knows how to build directories (the OS takes care of the above hardlinks).

There are restrictions on what can be hardlinked (both links must reside on the same filesystem, the source file must exist, etc.) that are not applicable to softlinks (source and target can be on seperate file systems, source does not have to exist, etc.). OTOH, softlinks have other restrictions not shared by hardlinks (additional I/O necessary to complete file access, additional storage taken up by softlink file's data, etc.)

In other words, there's tradeoffs with each.


#### A further note with respect to hardlink files
When deleting files, the data part isn't disposed of until all the filename parts have been deleted. There's a count in the inode that indicates how many filenames point to this file, and that count is decremented by 1 each time one of those filenames is deleted. When the count makes it to zero, the inode and its associated data are deleted.

By the way, the count also reflects how many times the file has been opened without being closed (in other words, how many references to the file are still active). This has some ramifications which aren't obvious at first: you can delete a file so that no "filename" part points to the inode, without releasing the space for the data part of the file, because the file is still open.

Have you ever found yourself in this position: you notice that `/var/log/messages` (or some other syslog-owned file) has grown too big, and you
```shell
rm /var/log/messages
touch /var/log/messages
```

to reclaim the space, but the used space doesn't reappear? This is because, although you've deleted the filename part, there's a process that's got the data part open still (syslogd), and the OS won't release the space for the data until the process closes it. In order to complete your space reclamation, you have to
```shell
kill -SIGHUP `cat /var/run/syslogd.pid`
```

to get syslogd to close and reopen the file.

You can use this to your advantage in programs: have you ever wondered how you could hide a temporary file? Well, you could do the following:
```C++
{
	FILE *fp;
	fp = fopen("some.hidden.file","w");
	unlink("some.hidden.file"); /* deletes the filename part */

	/* some.hidden.file no longer has a filename and is truely hidden */
    fprintf(fp,"This data won't be found\n"); /* access the data part */
    /*etc*/
    fclose(fp); /* finally release the data part */
}
```


#### Refs
[ The difference between hard and soft links]:https://linuxgazette.net/105/pitcher.html
[Questions on Stackoverflow]:https://stackoverflow.com/questions/185899/what-is-the-difference-between-a-symbolic-link-and-a-hard-link
[askubuntu]:https://askubuntu.com/questions/108771/what-is-the-difference-between-a-hard-link-and-a-symbolic-link




## 👾 User Management



## 📲 Network Management
### 👉 What is NIC?

> 🖇 https://www.cnblogs.com/machangwei-8/p/10352887.html

1. What is [NIC](https://zh.wikipedia.org/zh-cn/网卡) (Network Interface Controller)?
   The NIC may use one or more of the following techniques to indicate the availability of packets to transfer:

   - [Polling](https://en.wikipedia.org/wiki/Polling_(computer_science)) is where the [CPU](https://en.wikipedia.org/wiki/CPU) examines the status of the [peripheral](https://en.wikipedia.org/wiki/Peripheral) under program control.
   - [Interrupt](https://en.wikipedia.org/wiki/Interrupt_request)-driven I/O is where the peripheral alerts the CPU that it is ready to transfer data.

2. NICs may use one or more of the following techniques to transfer packet data:
- [Programmed input/output](https://en.wikipedia.org/wiki/Programmed_input/output), where the CPU moves the data to or from the NIC to memory.
- [Direct memory access](https://en.wikipedia.org/wiki/Direct_memory_access) (DMA), where a device other than the CPU assumes control of the [system bus](https://en.wikipedia.org/wiki/System_bus) to move data to or from the NIC to memory. This removes load from the CPU but requires more logic on the card. In addition, a packet buffer on the NIC may not be required and [latency](https://en.wikipedia.org/wiki/Latency_(engineering)) can be reduced.


### 👉 Port
⭐️ [Opening a port on Linux](https://www.digitalocean.com/community/tutorials/opening-a-port-on-linux)

TBD..



### 👉 Networking Modes --- Bridged, Host-only, NAT

> 🔗  [网络配置三种模式对比（桥接模式，主机模式，网络地址转换）](https://cloud.tencent.com/developer/article/1184666)

![Screenshot 2023-01-12 at 9.38.05 PM](../../../../Assets/Pics/Screenshot%202023-01-12%20at%209.38.05%20PM.png)

#### 1. bridged(桥接模式)
![img](../../../../../Assets/Pics/1620.png)

#### 2. host-only(主机模式)
![img](../../../../../Assets/Pics/1620-20230112213519191.png)

#### 3. NAT(网络地址转换模式)
![img](../../../../../Assets/Pics/1620-20230112213526905.png)

![img](../../../../../Assets/Pics/1620-20230112213609530.png)



## ⌛️ Process Management
[Linux查看系统服务](https://www.cnblogs.com/yychuyu/p/13428335.html)

