# FAQ

[TOC]



## 👉 Source release & Binary Release?
#FreeSoftware #src #linux 

see [this](https://stackoverflow.com/a/5280925/16542494) answer on stack overflow. A source release is the source code of the packeg, which means user have to compile and construct the software themselves. While Binary release is the to-go software. 



## 👉 diff between hard link & soft link (symlink, symbolic link)
#symlink #filesystem #linux #hard_link #soft_link

![Pictorial representation](../../../../../Assets/Pics/f7Ijz.jpg)
<small>This illustration is not acurate though</small>

### Unix File System
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


### A further note with respect to hardlink files
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


[ The difference between hard and soft links]:https://linuxgazette.net/105/pitcher.html
[Questions on Stackoverflow]:https://stackoverflow.com/questions/185899/what-is-the-difference-between-a-symbolic-link-and-a-hard-link
[askubuntu]:https://askubuntu.com/questions/108771/what-is-the-difference-between-a-hard-link-and-a-symbolic-link



## 👉 Networking Modes --- Bridged, Host-only, NAT
#bridged #host-only #nat #network #linux 


![Screenshot 2023-01-12 at 9.38.05 PM](../../../../Assets/Pics/Screenshot%202023-01-12%20at%209.38.05%20PM.png)

 1. bridged(桥接模式)
![img](../../../../../Assets/Pics/1620.png)


2. host-only(主机模式)
![img](../../../../../Assets/Pics/1620-20230112213519191.png)


3. NAT(网络地址转换模式)
![img](../../../../../Assets/Pics/1620-20230112213526905.png)

![img](../../../../../Assets/Pics/1620-20230112213609530.png)



[网络配置三种模式对比（桥接模式，主机模式，网络地址转换）]: https://cloud.tencent.com/developer/article/1184666



## 👉 What is SELinux?
#SELinux

Security-Enhanced Linux (SELinux) is a [security](https://www.redhat.com/en/topics/security) architecture for [Linux® systems](https://www.redhat.com/en/topics/linux/what-is-linux) that allows administrators to have more control over who can access the system. It was originally developed by the United States National Security Agency (NSA) as a series of patches to the [Linux kernel](https://www.redhat.com/en/topics/linux/what-is-the-linux-kernel) using Linux Security Modules (LSM). 

SELinux was released to the [open source](https://www.redhat.com/en/topics/open-source/what-is-open-source) community in 2000, and was integrated into the upstream Linux kernel in 2003.

[What is SELinux]: https://www.redhat.com/en/topics/linux/what-is-selinux



## 👉 Linux: where are environment variables (of a specific process) stored?
#linux #environment_variable #process 

The environment variables of a process exist at runtime, and are not stored in some file or so. They are stored in the process's own memory (that's where they are found to pass on to children). But there is a virtual file in 
```shell
/proc/_pid_/environ
```

This file shows all the environment variables that were passed when calling the process (unless the process overwrote that part of its memory — most programs don't). The kernel makes them visible through that virtual file. One can list them. For example to view the variables of process 3940, one can do
```shell
cat /proc/3940/environ | tr '\0' '\n'
```

Each variable is delimited by a binary zero from the next one.`tr` replaces the zero into a newline.

[Linux: where are environment variables stored?]: https://stackoverflow.com/questions/532155/linux-where-are-environment-variables-stored

The **Global** environment variables of your system are stored in `/etc/environment`.  
Any changes here will get reflected throughout the system and will affect all users of the system. Also, you need a Reboot, for any changes made here to take effect.

**User** level Environment variables are mostly stored in `.bashrc` and `.profile` files in your Home folder. Changes here only affect that particular user. Just close and open the terminal for configuration changes to take place.

_Edit_ : If you don't want to Reboot or restart your terminal, you can make use of the source command.  
Eg. `source /etc/environment` or `source .bashrc`

[Environment variables - where are they stored by linux, how do I change them and is it safe to do so?]: https://askubuntu.com/questions/164586/environment-variables-where-are-they-stored-by-linux-how-do-i-change-them-and
