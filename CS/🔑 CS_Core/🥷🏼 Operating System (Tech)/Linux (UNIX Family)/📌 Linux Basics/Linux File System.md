# Linux File System

[TOC]


## Res
📂 [Filesystem Hierarchy Standard | LSB Workgroup, The Linux Foundation](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)

↗ [UNIX File System](../../UNIX%20Family/📌%20UNIX%20Basics/UNIX%20File%20System.md)



## Intro
### LSB Workgroup


### FHS (File Hierarchy System)
FHS is not considered to be some authority on directory structure and contents for absolutely every Linux distribution, but it is ==generally the most common standard of linux file layout.== All directories and files in FHS appear under ‘/’ – the root directory.



## Linux FHS
### [/etc](https://blog.csdn.net/blueair_ren/article/details/79937599)
etc不是什么缩写，是and so on的意思 来源于 法语的 et cetera 翻译成中文就是 等等 的意思. 至于为什么在/etc下面存放配置文件， 按照原始的UNIX的说法([linux文件结构](https://www.baidu.com/s?wd=linux%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84&from=1012015a&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1Y4mW79ryP-Pj-BP17WnWwb0ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6KdThsqpZwYTjCEQLGCpyw9Uz4Bmy-bIi4WUvYETgN-TLwGUv3EPjcvPjm4PHRv)参考UNIX的教学实现MINIX) 这下面放的都是一堆零零碎碎的东西, 就叫etc, 这其实是个历史遗留.


### /opt & /usr
1. /opt
   Aka optional, where optional files are stored. Trying out the latest Firefox beta? Install it to /opt where you can delete it without affecting other settings. **Programs here usually live inside a single folder whick contains all of their data, libraries, etc.**

 > 举个例子：刚才装的测试版firefox，就可以装到/opt/firefox_beta目录下，/opt/firefox_beta目录下面就包含了运 行firefox所需要的所有文件、库、数据等等。要删除firefox的时候，你只需删除/opt/firefox_beta目录即可，非常简单。

2. /usr/local
   This is where most manually installed(ie. outside of your package manager) software goes.It has the same structure as /usr. It is a good idea to leave /usr to your package manager and put any custom scripts and things into /usr/local, since nothing important normally lives in /usr/local.


## Ref
[Linux File Hierarchy Structure | GeeksforGeeks]: https://www.geeksforgeeks.org/linux-file-hierarchy-structure/
