# Free Space Management

[TOC]



## Res


## Intro
> Free space management: Keep track of available disk blocks (空闲空间管理：维护可用盘块集合)


### Disk Allocation Table (DAT)
> Disk allocation table (DAT) is the data structure that keeps track of block usage (通过磁盘分配表记录盘块的使用情况)



## Free Space Management Methods
### Bit Table


### Chained Free Portion
> - Organize the free portions in a chain (对空闲分区采用链式管理)
> - The start block of a portion stores length & next portion (每个空闲分区的开头盘块存储当前分区的长度和下一个空闲分区的开头)
> - No DAT is needed: store the head free portion    (不需要磁盘分配表：记录首个空闲分区的位置即可)


- Find available [...]
	- block: Take one block from the head (从链首指向的分区分配一块并更新链表状态)
	- portion: Find the first suitable free portion in the chain (从第一个可以满足条件的分区进行分配并更新链表状态)

- Issues
	- Fragmentation (碎片)
	- Long allocation/recycle time (分配及回收时间长)


### Indexing




## Ref

