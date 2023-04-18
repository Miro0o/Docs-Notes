# Memory Virtualization

[TOC]



## Res
↗ [Cache Memory (高速缓存)](../Cache%20Memory%20(高速缓存).md)



## Intro
The purpose of virtual memory is to use the hard disk as an extension of RAM, thus increasing the available address space a process can use.

Using virtual memory, your computer addresses more main memory than it actually has, and it uses the hard drive to hold the excess. This area on the hard drive is called a **page file,** because it holds chunks of main memory on the hard drive.

The most common way to implement virtual memory is by using **paging**, a method in which main memory is divided into fixed-size blocks and programs are divided into the same-size blocks.


### Terminology
**Virtual address**: The logical or program address that the process uses. Whenever the CPU generates an address, it is always in terms of virtual address space.

**Physical address**: The real address in physical memory.

**Mapping**: The mechanism by which virtual addresses are translated into physical ones (very similar to cache mapping).

**Page frames**: The equal-sized chunks or blocks into which main memory (physical memory) is divided.

**Pages**: The chunks or blocks into which virtual memory (the logical address space) is divided, each equal in size to a page frame. Virtual pages are stored on disk until needed.

**Paging**: The process of copying a virtual page from disk to a page frame in main memory.

**Fragmentation**: Memory that becomes unusable.

**Page fault**: An event that occurs when a requested page is not in main memory and must be copied into memory from disk.




## Memory Virtualization Methods
### Paging
↗ [Paging](Paging.md)


### Segmentation
↗ [Segmentation](Segmentation.md)


### Paging 🆚 Segmentation: Pros and Cons
Paging is based on a purely physical value: The program and main memory are divided up into chunks of the same physical size. 
Segmentation, on the other hand, allows for logical portions of the program to be divided into variable-sized partitions.

With segmentation, the user is aware of the segment sizes and boundaries; with paging, the user is unaware of the partitioning. 

Paging is easier to manage: Allocation, freeing, swapping, and relocating are easy when everything’s the same size. However, pages are typically smaller than segments, which means more overhead (in terms of resources to both track and transfer pages). 

Paging eliminates external fragmentation, whereas segmentation eliminates internal fragmentation. 

Segmentation has the ability to support sharing and protection, both of which are very difficult to do with paging.


### 💑 Paging Combined with Segmentation
In a combined approach, the virtual address space is divided into segments of variable length, and the segments are divided into fixed-size pages. Main memory is divided into frames of the same size.

Each segment has a page table, which means that every program has multiple page tables. The physical address is divided into three fields. The first field is the segment field, which points the system to the appropriate page table. The second field is the page number, which is used as an offset into this page table. The third field is the offset within the page.

Combined segmentation and paging is advantageous because it allows for segmentation from the user’s point of view and paging from the system’s point of view.




## Fragmentation




## Ref