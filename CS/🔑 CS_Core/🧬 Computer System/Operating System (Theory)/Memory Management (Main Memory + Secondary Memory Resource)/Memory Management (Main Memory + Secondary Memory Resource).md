# Memory Management (Main Memory + Secondary Memory Resource)

[TOC]



## Res

## Intro
![](../../../../../Assets/Pics/Screenshot%202023-05-04%20at%201.25.23%20PM.png)
<small>Memory Management Techniques</small>

Fixed /Dynamic Partitioning: 整个程序作为整体，程序全部加载，地址连续
Simple Paging/ Segmentation: 整个程序划分为块，程序全部加载，地址不连续
Virtual Memory Paging/ Segmentation: 整个程序划分为块，程序部分加载，地址不连续




## Memory Management Requirements
#TODO 


## Principal Operation of Memory Management
### 


## Ref
[操作系统~内存管理之覆盖与交换、连续内存分配 | CSDN]: https://blog.csdn.net/Shangxingya/article/details/113802996

- [内存管理](https://blog.csdn.net/Shangxingya/article/details/113802996#_31)
    - [内存保护](https://blog.csdn.net/Shangxingya/article/details/113802996#_39)
        - [内存交换技术](https://blog.csdn.net/Shangxingya/article/details/113802996#_57)
        - [内存分配](https://blog.csdn.net/Shangxingya/article/details/113802996#_80)
        - [单一连续分配](https://blog.csdn.net/Shangxingya/article/details/113802996#_81)
            - [固定分区分配](https://blog.csdn.net/Shangxingya/article/details/113802996#_90)
            - [动态分区分配](https://blog.csdn.net/Shangxingya/article/details/113802996#_103)
            - [动态分配算法](https://blog.csdn.net/Shangxingya/article/details/113802996#_114)


[👍 Linux堆内存管理深入分析（上）]: https://introspelliam.github.io/2017/09/10/Linux堆内存管理深入分析（上）/
鉴于篇幅过长，我将文章分成了上下两部分，上部分主要介绍堆内存管理中的一些基本概念以及相互关系，同时也着重介绍了堆中chunk分配和释放策略中使用到的隐式链表技术。后半部分主要介绍glibc malloc为了提高堆内存分配和释放的效率，引入的显示链表技术，即binlist的概念和核心原理。其中使用到的源码在：
- https://github.com/sploitfun/lsploits/tree/master/glibc
- [malloc.c源码](https://introspelliam.github.io/others/files/malloc.c)

