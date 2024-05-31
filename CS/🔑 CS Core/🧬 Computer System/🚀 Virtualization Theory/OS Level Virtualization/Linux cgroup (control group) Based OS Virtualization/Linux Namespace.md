# Linux Namespace

[TOC]



## Res
### Related Topics
↗ [🍸 Linux Kernel](../../../../🥷🏼%20Operating%20System%20(Engineering%20Part)/Linux%20(Derived%20From%20UNIX%20Family)/🔩%20Linux%20Kernel/🍸%20Linux%20Kernel.md)
↗ [Process Management & Scheduling](../../../../🥷🏼%20Operating%20System%20(Engineering%20Part)/Linux%20(Derived%20From%20UNIX%20Family)/🔩%20Linux%20Kernel/⭕️%20Process%20Management%20&%20Scheduling/Process%20Management%20&%20Scheduling.md)



## Intro
**Namespaces**: provides process isolation, complete isolation of containers, separate file system.

There are 6 types of namespaces:  
1. **mount ns** - for file system.  
2. **UTS(Unique time sharing) ns** - which checks for different hostnames of running containers   
3. **IPC ns** - interprocess communication  
4. **Network ns** - takes care of different ip allocation to different containers  
5. **PID ns** - process id isolation  
6. **user ns** - different username(uid)



## Ref

