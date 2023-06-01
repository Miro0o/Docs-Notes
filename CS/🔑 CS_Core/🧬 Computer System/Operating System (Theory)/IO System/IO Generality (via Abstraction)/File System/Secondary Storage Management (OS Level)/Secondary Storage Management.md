# Secondary Storage Management

[TOC]



## Res
↗ [Memory Management](../../../../Memory%20Management/Memory%20Management.md)



## Intro
> Goal: Manage the disk space to support a stream of file operations, i.e., insertion and deletion (管理磁盘空间，支持一系列文件操作)

Two basic tasks:
- File allocation: Given a set of blocks associated with a file and the set of available disk blocks, determine where to place the blocks (文件分配：决定文件的数据块在二级存储中存放的盘块位置)
- Free space management: Keep track of available disk blocks (空闲空间管理：维护可用盘块集合)



## Ref

