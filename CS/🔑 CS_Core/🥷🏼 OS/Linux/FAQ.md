# FAQ

[TOC]





## ð OS Management

### ð hardware info

[Linuxä¸æ¥ççµèç¡¬ä»¶ç¯å¢çå½ä»¤](https://blog.csdn.net/wjlwangluo/article/details/77511692) 



### ð Boot Linux on USB

[Rufus](https://rufus.ie/en/)

[å¨å®ä½PCæºä¸å®è£Linuxç³»ç»](https://blog.csdn.net/Blazar/article/details/79168116)



### ð Env veriables

> ð [How to Set and List Environment Variables in Linux](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/)

#### What is `env variables`

In Linux and Unix based systems **environment variables are a set of dynamic named values**, stored within the system that are used by applications launched in shells or subshells. In simple words, an environment variable is a variable with a name and an associated value.

Environment variables allow you to customize how the system works and the behavior of the applications on the system. For example, the environment variable can store information about the default [text editor](https://linuxize.com/post/how-to-use-nano-text-editor/) or browser, the path to executable files, or the system locale and keyboard layout settings.

#### How to list `env variables`

There are several commands available that allow you to list and set environment variables in Linux:

For `environment variables`:

- `env` â The command allows you to run another program in a custom environment without modifying the current one. When used without an argument it will print a list of the current environment variables.
- `printenv` â The command prints all or the specified environment variables.

For `environment variables` & `shell variables`: 

- `set` â The command sets or unsets shell variables. When used without an argument it will print a list of all variables including environment and shell variables, and shell functions.
- `unset` â The command deletes shell and environment variables.
- `export` â The command sets environment variables.



### ð Hostname

[å¦ä½å¨ Ubuntu 20.04 ä¸ä¿®æ¹ä¸»æºå](https://cloud.tencent.com/developer/article/1649332)

```shell
hostname
hostnamectl set-hostname
```



### ð Shutdown a machine

> [Linuxå³æºåéå¯å½ä»¤](http://c.biancheng.net/view/793.html)

```shell
reboot

shutdown 

halt

poweroff

init 
```





## ð File Management

### ð Linux directory hirachy

#### [/etc](https://blog.csdn.net/blueair_ren/article/details/79937599)

etcä¸æ¯ä»ä¹ç¼©åï¼æ¯and so onçææ æ¥æºäº æ³è¯­ç et cetera ç¿»è¯æä¸­æå°±æ¯ ç­ç­ çææ. è³äºä¸ºä»ä¹å¨/etcä¸é¢å­æ¾éç½®æä»¶ï¼ æç§åå§çUNIXçè¯´æ³([linuxæä»¶ç»æ](https://www.baidu.com/s?wd=linux%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84&from=1012015a&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1Y4mW79ryP-Pj-BP17WnWwb0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6KdThsqpZwYTjCEQLGCpyw9Uz4Bmy-bIi4WUvYETgN-TLwGUv3EPjcvPjm4PHRv)åèUNIXçæå­¦å®ç°MINIX) è¿ä¸é¢æ¾çé½æ¯ä¸å é¶é¶ç¢ç¢çä¸è¥¿, å°±å«etc, è¿å¶å®æ¯ä¸ªåå²éç.



#### /opt & /usr

1. /opt
   Aka optional, where optional files are stored. Trying out the latest Firefox beta? Install it to /opt where you can delete it without affecting other settings. **Programs here usually live inside a single folder whick contains all of their data, libraries, etc.**

 > ä¸¾ä¸ªä¾å­ï¼åæè£çæµè¯çfirefoxï¼å°±å¯ä»¥è£å°/opt/firefox_betaç®å½ä¸ï¼/opt/firefox_betaç®å½ä¸é¢å°±åå«äºè¿ è¡firefoxæéè¦çæææä»¶ãåºãæ°æ®ç­ç­ãè¦å é¤firefoxçæ¶åï¼ä½ åªéå é¤/opt/firefox_betaç®å½å³å¯ï¼éå¸¸ç®åã

2. /usr/local
   This is where mostÂ manually installed(ie. outside of your package manager) software goes.It has the same structure as /usr.Â It is a good idea to leave /usr to your package manager and put any custom scripts and things into /usr/local, since nothing important normally lives in /usr/local.



### ð [æ¯è¾æä»¶/ç®å½çä¸å](https://www.cnblogs.com/f-ck-need-u/p/9071033.html) #unsolved



### ð diff between hard linlk & soft link (symlink, symbolic link)

![Pictorial representation](../../../../Assets/Pics/f7Ijz.jpg)

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



### ð Source release & Binary release?

see [this](https://stackoverflow.com/a/5280925/16542494) answer on stack overflow. A source release is the source code of the packeg, which means user have to compile and construct the software themselves. While Binary release is the to-go software. 



### ð Binary code analysis

â­ï¸ [Radare2: The Libre Unix-Like Reverse Engineering Framework](https://github.com/radareorg/radare2)

ð¤ [å¨ Linux ä¸åæäºè¿å¶æä»¶ç 10 ç§æ¹æ³](https://linux.cn/article-12187-1.html)

1. `file`
2. `idd`
3. `Itrace`
4. `hexdump`
5. `strings`
6. `readelf`
7. `objdump`
8. `strace`
9. `nm`
10. `gdb`

ð¤ [Linuxä¸æ¥çäºè¿å¶æä»¶](https://blog.csdn.net/qq_19922839/article/details/115483499)

1. `hexdump`

2. `xdd`
3. `od`



## ð¾ User Management

### ð ç¨æ·/ç¨æ·ç»/ æé

```shell
# lookup users&groups
cat /etc/passwd
cat /etc/group

cat /etc/passwd|grep -v nologin|grep -v halt|grep -v shutdown|awk -F":" '{ print $1"|"$3"|"$4 }'|more

# delete user
userdel user_name

# force quit user
# w/ uptime/ finger/ ps/ top(htop gtop)
pkill -kill -t TTY

# change user group
usermod 

```

[Linuxä¸æ¥çç¨æ·åè¡¨åå é¤ç¨æ·](https://blog.csdn.net/qq_36850813/article/details/83899789)
[Linuxä¿®æ¹ç¨æ·æå¨ç»æ¹æ³](https://blog.csdn.net/czl8897098/article/details/51636407)
[æéè¯¦è§£](https://blog.csdn.net/u013197629/article/details/73608613)

æ·»å ç¨æ·å¹¶èµäºæé

- https://blog.csdn.net/stormbjm/article/details/9086163
- [chmod](https://www.computerhope.com/unix/uchmod.htm)



## ð² Network Management



### ð ssh

```shell
ssh-keygen -t -b

ssh-copy-id username@hostname
scp 
```

[scp (secure copy) command](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/) #unsolved 
[ssh ç»é](https://blog.csdn.net/li528405176/article/details/82810342)
[ssh é«çº§åºç¨](https://blog.csdn.net/pipisorry/article/details/52269785)



### ð Trafic

[Linuxç³»ç»nloadå½ä»¤æ¥çç½éæµé](https://www.5yun.org/20932.html) 



Ifconfig

> ð https://www.cnblogs.com/machangwei-8/p/10352887.html

1. What is [NIC](https://zh.wikipedia.org/zh-cn/ç½å¡) (Network Interface Controller)?

   The NIC may use one or more of the following techniques to indicate the availability of packets to transfer:

   - [Polling](https://en.wikipedia.org/wiki/Polling_(computer_science)) is where the [CPU](https://en.wikipedia.org/wiki/CPU) examines the status of the [peripheral](https://en.wikipedia.org/wiki/Peripheral) under program control.
   - [Interrupt](https://en.wikipedia.org/wiki/Interrupt_request)-driven I/O is where the peripheral alerts the CPU that it is ready to transfer data.

2. NICs may use one or more of the following techniques to transfer packet data:

- [Programmed input/output](https://en.wikipedia.org/wiki/Programmed_input/output), where the CPU moves the data to or from the NIC to memory.
- [Direct memory access](https://en.wikipedia.org/wiki/Direct_memory_access) (DMA), where a device other than the CPU assumes control of the [system bus](https://en.wikipedia.org/wiki/System_bus) to move data to or from the NIC to memory. This removes load from the CPU but requires more logic on the card. In addition, a packet buffer on the NIC may not be required and [latency](https://en.wikipedia.org/wiki/Latency_(engineering)) can be reduced.



### ð File transmission

[linuxæå¡å¨ä¹é´ä¼ è¾æä»¶çåç§æ¹å¼](https://blog.csdn.net/qw_xingzhe/article/details/80167888)

[Linux curl å½ä»¤ä¸è½½æä»¶](https://www.cnblogs.com/hujiapeng/p/8470099.html) 



### ð Port

â­ï¸ [Opening a port on Linux](https://www.digitalocean.com/community/tutorials/opening-a-port-on-linux)

TBD..



## âï¸ Process Management

[Linuxæ¥çç³»ç»æå¡](https://www.cnblogs.com/yychuyu/p/13428335.html)

