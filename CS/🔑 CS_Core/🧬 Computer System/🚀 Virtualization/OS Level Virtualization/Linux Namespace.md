# Linux Namespace

[TOC]



## Res


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

