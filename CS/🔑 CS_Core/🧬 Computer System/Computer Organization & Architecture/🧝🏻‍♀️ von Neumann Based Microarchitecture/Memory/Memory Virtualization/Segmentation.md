# Segmentation

[TOC]



## Res


## Intro
Instead of dividing the virtual address space into equal, fixed-size pages, and the physical address space into equal-size page frames, ==the virtual address space is divided into **logical, variable-length units**, or **segments**.==

Physical memory isn’t really divided or partitioned into anything. When a segment needs to be copied into physical memory, the operating system looks for a chunk of free memory large enough to store the entire segment.

Each segment has a **base address**, indicating where it is located in memory, and a **bounds limit**, indicating its size. Each program, consisting of multiple segments, now has an associated **segment table** instead of a page table. This segment table is simply a collection of the base/bounds pairs for each segment.



## External Fraction
As with paging, segmentation suffers from fragmentation.
- Paging creates internal fragmentation because a frame can be allocated to a process that doesn’t need the entire frame. 
- Segmentation, on the other hand, suffers from external fragmentation. As segments are allocated and deallocated, the free chunks that reside in memory become broken up. Eventually, there are many small chunks, but none large enough to store an entire segment.

The difference between external and internal fragmentation is that, 
- with external fragmentation, enough total memory space may exist to allocate to a process, but this space is not contiguous—it exists as a large number of small, unusable holes.
- With internal fragmentation, the memory simply isn’t available because the system has overal-located memory to a process that doesn’t need it.


### GC (Garbage Collection) for External Fragmentation
To combat external fragmentation, systems use some sort of garbage collection. This process simply shuffles occupied chunks of memory to coalesce the smaller, fragmented chunks into larger, usable chunks. If you have ever defragmented a disk drive, you have witnessed a similar process, collecting the many small free spaces on the disk and creating fewer, larger ones.



## Ref

