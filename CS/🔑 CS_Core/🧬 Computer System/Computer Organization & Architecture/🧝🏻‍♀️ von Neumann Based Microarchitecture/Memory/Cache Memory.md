# Cache Memory

[TOC]



## Res


## Intro

## Cache Performence Metrix
### Cache Miss/Hit
One field of the main memory address points us to a location in cache in which the data resides if it is resident in cache (this is called a cache hit), or where it is to be placed if it is not resident (which is called a cache miss). (This is slightly different for associative-mapped cache, which we discuss shortly.)


### Effective Access Time & Hit Ratio




## Cache Mapping Schemes
What makes cache “special”? ==Cache is not accessed by address; it is accessed by content. For this reason, cache is sometimes called content-addressable memory or CAM.== Under most cache mapping schemes, the cache entries must be checked or searched to see if the value being requested is stored in cache. To simplify this process of locating the desired data, various cache mapping algorithms are used.

🤔 In general, though various algorithms has been used in cache mapping, the common sense is using exponentially-increasing index by dividing cache either into blocks or sets of blocks. 

🤔 类似倍增的思想，通过对缓存进行倍增的划分（blocks, sets of blocks）提高indexing的效率和范围。


### Fields
How, then, does the CPU locate data when it has been copied into cache? The CPU uses a specific mapping scheme that “converts” the main memory address into a cache location.

This address conversion is done by giving special significance to the bits in the main memory address. We first divide the bits into distinct groups we call fields. Depending on the mapping scheme, we may have two or three fields. How we use these fields depends on the particular mapping scheme being used.


### Direct Mapping (DM Cache)
![理解 CPU Cache](https://ts1.cn.mm.bing.net/th/id/R-C.336f9fff21b3b61889a7b0246240d69d?rik=02m%2b6ayJ8dx80Q&riu=http%3a%2f%2fwsfdl.oss-cn-qingdao.aliyuncs.com%2fcpu_cache_direct_mapping.png&ehk=X%2fciJqHsMLfkbwxORN159Y4xhlEBbXuPuO2e8E90IeY%3d&risl=&pid=ImgRaw&r=0)


offset field, block field, tag field


### Fully Associative Mapping (FAM Cache)



### Set-associative Mapping (SAM Cache)


## Replacement Policies



## Cache Write Policies



## Levels of Cache (Cache Hierarchy)
> Recall Memroy Hierarchy discussied in [Memory /Memory Hierarchy](Memory.md)

For years, manufacturers have been trying to balance the higher latency in larger caches with the increase in hit rates by selecting just the right size cache. However, many designers are applying the concepts of levels of memory to cache itself, and they are now using a multilevel cache hierarchy in most systems—caches are using caching for increased performance!

### L1 Cache


### L2 Cache 



### L3 Cache





## Instruction and Data Caches
### Integrated Cache


### Harvard Cache



## Ref

