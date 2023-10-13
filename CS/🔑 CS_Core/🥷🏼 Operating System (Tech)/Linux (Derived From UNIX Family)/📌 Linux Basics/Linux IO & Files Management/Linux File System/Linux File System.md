# Linux File System

[TOC]


## Res
📂 [Filesystem Hierarchy Standard | LSB Workgroup, The Linux Foundation](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)

↗ [UNIX File System](../../../../UNIX%20Family/📌%20UNIX%20Basics/UNIX%20IO%20&%20Files%20Management/UNIX%20File%20System/UNIX%20File%20System.md)



## Intro
[Linux](https://en.wikipedia.org/wiki/Linux "Linux") supports numerous file systems, but common choices for the system disk on a block device include the ext* family ([ext2](https://en.wikipedia.org/wiki/Ext2 "Ext2"), [ext3](https://en.wikipedia.org/wiki/Ext3 "Ext3") and [ext4](https://en.wikipedia.org/wiki/Ext4 "Ext4")), [XFS](https://en.wikipedia.org/wiki/XFS "XFS"), [JFS](https://en.wikipedia.org/wiki/JFS_(file_system) "JFS (file system)"), and [btrfs](https://en.wikipedia.org/wiki/Btrfs "Btrfs"). For raw flash without a [flash translation layer](https://en.wikipedia.org/wiki/Flash_translation_layer "Flash translation layer") (FTL) or [Memory Technology Device](https://en.wikipedia.org/wiki/Memory_Technology_Device "Memory Technology Device") (MTD), there are [UBIFS](https://en.wikipedia.org/wiki/UBIFS "UBIFS"), [JFFS2](https://en.wikipedia.org/wiki/JFFS2 "JFFS2") and [YAFFS](https://en.wikipedia.org/wiki/YAFFS "YAFFS"), among others. [SquashFS](https://en.wikipedia.org/wiki/SquashFS "SquashFS") is a common compressed read-only file system.


### LSB Workgroup


### FHS (File Hierarchy System)
FHS is not considered to be some authority on directory structure and contents for absolutely every Linux distribution, but it is ==generally the most common standard of linux file layout.== All directories and files in FHS appear under ‘/’ (i.e. the root directory).

↗ [UNIX File System /FHS (Filesystem Hierarchy Standard)](../../../../UNIX%20Family/📌%20UNIX%20Basics/UNIX%20IO%20&%20Files%20Management/UNIX%20File%20System/UNIX%20File%20System.md#FHS%20(Filesystem%20Hierarchy%20Standard))

### Mounting
The term "to mount" a filesystem in Linux refers back to the early days of computing when a tape or removable disk pack would need to be physically mounted on an appropriate drive device. After being physically placed on the drive, the filesystem on the disk pack would be logically mounted by the operating system to make the contents available for access by the OS, application programs and users.

A **mount point** is simply a directory, like any other, that is created as part of the root filesystem. So, for example, the home filesystem is mounted on the directory /home. Filesystems can be mounted at mount points on other non-root filesystems but this is less common.

The Linux root filesystem is mounted on the root directory (/) very early in the boot sequence. Other filesystems are mounted later, by the Linux startup programs, either **`rc`** under SystemV or by **`systemd`** in newer Linux releases. Mounting of filesystems during the startup process is managed by the `/etc/fstab` configuration file. An easy way to remember that is that `fstab` stands for "file system table," and it is a list of filesystems that are to be mounted, their designated mount points, and any options that might be needed for specific filesystems.

Filesystems are mounted on an existing directory/mount point using the **mount** command. In general, any directory that is used as a mount point should be empty and not have any other files contained in it. Linux will not prevent users from mounting one filesystem over one that is already there or on a directory that contains files. If you mount a filesystem on an existing directory or filesystem, the original contents will be hidden and only the content of the newly mounted filesystem will be visible.



## Linux File Types
### Text File (Read, Write)
↗ [Linux File Types & Formats /🎯 Text File](Linux%20File%20Types%20&%20Formats.md#🎯%20Text%20File)


### Binary File (Executable)
> Instructions are packaged in a form called an executable object program and stored as a binary disk file. Object programs are also referred to as executable object files.

↗ [Linux File Types & Formats / 🎯 Binary File](Linux%20File%20Types%20&%20Formats.md#🎯%20Binary%20File)



## Linux Directory System
> Conventionally FHS has been standards for Unix & Unix-like systems. Linux directly borrowed this standards from it and thus basically share the same directory hierarchy with Unix, despite minor modifications(?).
> 
> ↗ [UNIX File System](../../../../UNIX%20Family/📌%20UNIX%20Basics/UNIX%20IO%20&%20Files%20Management/UNIX%20File%20System/UNIX%20File%20System.md)

### /etc
etc不是什么缩写，是and so on的意思 来源于 法语的 et cetera 翻译成中文就是 等等 的意思. 至于为什么在/etc下面存放配置文件， 按照原始的UNIX的说法([linux文件结构](https://www.baidu.com/s?wd=linux%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84&from=1012015a&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1Y4mW79ryP-Pj-BP17WnWwb0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6KdThsqpZwYTjCEQLGCpyw9Uz4Bmy-bIi4WUvYETgN-TLwGUv3EPjcvPjm4PHRv)参考UNIX的教学实现MINIX) 这下面放的都是一堆零零碎碎的东西, 就叫etc, 这其实是个历史遗留.

https://blog.csdn.net/blueair_ren/article/details/79937599

### /opt & /usr
1. /opt
   Aka optional, where optional files are stored. Trying out the latest Firefox beta? Install it to /opt where you can delete it without affecting other settings. **Programs here usually live inside a single folder whick contains all of their data, libraries, etc.**

 > 举个例子：刚才装的测试版firefox，就可以装到/opt/firefox_beta目录下，/opt/firefox_beta目录下面就包含了运 行firefox所需要的所有文件、库、数据等等。要删除firefox的时候，你只需删除/opt/firefox_beta目录即可，非常简单。

2. /usr/local
   This is where most manually installed(ie. outside of your package manager) software goes.It has the same structure as /usr. It is a good idea to leave /usr to your package manager and put any custom scripts and things into /usr/local, since nothing important normally lives in /usr/local.


## Ref
[Linux File Hierarchy Structure | GeeksforGeeks]: https://www.geeksforgeeks.org/linux-file-hierarchy-structure/

[Classic SysAdmin: The Linux Filesystem Explained]: https://www.linuxfoundation.org/blog/blog/classic-sysadmin-the-linux-filesystem-explained

[An introduction to Linux filesystems]: https://opensource.com/life/16/10/introduction-linux-filesystems

[👍 File system | Wikipedia]: https://en.wikipedia.org/wiki/File_system#

[👍 List of File Systems | Wikipedia]: https://en.wikipedia.org/wiki/List_of_file_systems

