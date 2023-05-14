# Replacement Policy

[TOC]



## Res


## Intro
In most operating system texts, the treatment of memory management includes a sec- tion entitled “replacement policy,” which deals with the selection of a page in main memory to be replaced when a new page must be brought in. This topic is sometimes difficult to explain because several interrelated concepts are involved:
- How many page frames are to be allocated to each active process
- Whether the set of pages to be considered for replacement should be limited to those of the process that caused the page fault or encompass all the page frames in main memory
- Among the set of pages considered, which particular page should be selected for replacement

We shall refer to the first two concepts as resident set management, which will be dealt with in the next subsection, and reserve the term replacement policy for the third concept, which is discussed in this subsection.


### Frame Locking



## Replacement Algorithms
![](../../../../../../Assets/Pics/Screenshot%202023-05-11%20at%202.45.26%20PM.png)

![](../../../../../../Assets/Pics/Screenshot%202023-05-11%20at%203.20.03%20PM.png)



### OPT


### LRU


### FIFO


### CLOCK
![](../../../../../../Assets/Pics/Screenshot%202023-05-11%20at%203.20.15%20PM.png)


#### Enhanced CLOCK
The clock algorithm can be made more powerful by increasing the number of bits that it employs. On the other hand, if we reduce the number of bits employed to zero, the clock algorithm degenerates to FIFO.




## Ref

