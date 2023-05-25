# I/O Buffering

[TOC]



## Res


## Intro
### I/O Buffering Motivations


### I/O Buffering Modes
#### Block-oriented


#### Stream-oriented



## Types of I/O Buffering

![|500](../../../../../../../Assets/Pics/Screenshot%202023-05-25%20at%203.24.53%20PM.png)


### 1️⃣ Single Buffer



### 2️⃣ Double Buffer
An improvement over single buffering can be had by assigning two system buffers to the operation (see Figure 11.5c). A process now transfers data to (or from) one buffer while the operating system empties (or fills) the other. This technique is known as double buffering or buffer swapping.

For block-oriented transfer, we can roughly estimate the execution time as max [C, T]. It is therefore possible to keep the block-oriented device going at full speed if C ... T. On the other hand, if C 7 T, double buffering ensures that the pro- cess will not have to wait on I/O. In either case, an improvement over single buffering is achieved. Again, this improvement comes at the cost of increased complexity.

For stream-oriented input, we again are faced with the two alternative modes of operation. For line-at-a-time I/O, the user process need not be suspended for input or output, unless the process runs ahead of the double buffers. For byte-at-a-time operation, the double buffer offers no particular advantage over a single buffer of twice the length. In both cases, the producer/consumer model is followed.



### 3️⃣ Circular Buffer
A double-buffer scheme should smooth out the flow of data between an I/O device and a process. If the performance of a particular process is the focus of our concern, then we would like for the I/O operation to be able to keep up with the process. Double buffering may be inadequate if the process performs rapid bursts of I/O. In this case, the problem can often be alleviated by using more than two buffers.

When more than two buffers are used, the collection of buffers is itself referred to as a circular buffer (see Figure 11.5d), with each individual buffer being one unit in the circular buffer. This is simply the bounded-buffer producer/consumer model studied in Chapter 5.



## The Utility of Buffering
Buffering is a technique that **smoothes out peaks** in I/O demand. However, no amount of buffering will allow an I/O device to keep pace with a process indefinitely when the average demand of the process is greater than the I/O device can service. Even with multiple buffers, all of the buffers will eventually fill up, and the process will have to wait after processing each chunk of data. However, in a multiprogramming environment, when there is a variety of I/O activity and a variety of process activity to service, buffering is one tool that can increase the efficiency of the OS and the performance of individual processes.



## Ref

