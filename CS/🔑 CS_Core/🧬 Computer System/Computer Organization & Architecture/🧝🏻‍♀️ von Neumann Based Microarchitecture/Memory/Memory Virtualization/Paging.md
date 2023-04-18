# Paging

[TOC]



## Res


## Intro
> 💡 The success of paging, like that of cache, is dependent on the locality principle.

The basic idea behind paging is quite simple: Allocate physical memory to processes in fixed-size chunks (page frames) and keep track of where the various pages of the process reside by recording information in a **page table**.

==Every process has its own page table==, which typically resides in main memory; the page table stores the physical location of each virtual page of the process.


### Page Table Structure
The page table has N rows, where N is the number of virtual pages in the process. If there are pages of the process currently not in main memory, the page table indicates this by setting a valid bit to 0; if the page is in main memory, the valid bit is set to 1. Therefore, each entry of the page table has two fields: a valid bit and a frame number.


#### Additional Fields
1️⃣ For example, a **dirty bit** (or a **modify bit**) could be added to indicate whether the page has been changed. This makes returning the page to disk more efficient, because if it is not modified, it does not need to be rewritten to disk.

2️⃣ Another bit (the **usage bit**) can be added to indicate the page usage. This bit is set to 1 whenever the page is accessed. After a certain time period, the usage bit is set to 0. If the page is referenced again, the usage bit is set to 1. However, if the bit remains 0, this indicates that the page has not been used for a period of time, and the system might benefit by sending this page out to disk. 

By doing so, the system frees up this page’s location for another page that the process eventually needs (we discuss this in more detail when we introduce replacement algorithms).


### Virtual Address: Formats & Translations


### Paging EAT



## Internal Fractions



## TLB
We can speed up the page table lookup by storing the most recent page lookup values in a page table cache called a translation look-aside buffer (TLB). Each TLB entry consists of a virtual page number and its corresponding frame number.

Typically, the TLB is implemented as associative cache, and the virtual page/frame pairs can be mapped anywhere. Here are the steps necessary for an address lookup when using a TLB.



## Pros & Cons of Paging
### Paging Cons
1️⃣ Virtual memory implemented through paging adds an extra memory reference when accessing data. This time penalty is partially alleviated by using a TLB to cache page table entries. However, even with a high hit ratio in the TLB, this process still incurs translation overhead.

2️⃣ Another disadvantage of virtual memory and paging is the extra resource consumption (the memory overhead for storing page tables). In extreme cases (very large programs), the page tables may take up a significant portion of physical memory. One solution offered for this latter problem is to page the page tables, which can get very confusing indeed!

3️⃣ Virtual memory and paging also require special hardware and operating system support.


### Paging Pros
1️⃣ Programs are no longer restricted by the amount of physical memory that is available. Virtual memory permits us to run individual programs whose virtual address space is larger than physical memory. (In effect, this allows one process to share physical memory with itself.) This makes it much easier to write programs because the programmer no longer has to worry about the physical address space limitations.

2️⃣ Because each program requires less physical memory, virtual memory also permits us to run more programs at the same time. This allows us to share the machine among processes whose total address space sizes exceed the physical memory size, resulting in an increase in CPU utilization and system throughput.

3️⃣ The fixed size of frames and pages simplifies both allocation and placement from the perspective of the operating system. Paging also allows the operating system to specify protection (“this page belongs to User X and you can’t access it”) and sharing (“this page belongs to User X but you can read it”) on a per-page basis.


## ⭐️ Putting It All Together: The TLB, Page Table, Cache, and Main Memory





## Ref

