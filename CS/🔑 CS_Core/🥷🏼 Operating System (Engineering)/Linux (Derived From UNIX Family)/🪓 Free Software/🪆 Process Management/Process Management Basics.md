# Process Management

[TOC]



## Res


## System Service
↗ [System Services Management](System%20Services%20Management/System%20Services%20Management.md)



## Process Activity Management
### 👉 `ps`

[Linux进程之如何查看进程详情？（ps命令）](https://juejin.cn/post/6844903721369862152#heading-1)


### 👉 `watch`


### 👉 `pstree`


### 👉 `fg` | `bg` | `jobs` | `&` | `sleep`
1. start a programm from cli
2. [ctrl + z] to put it to the backgroud job lists
3. `jobs` to look up backgroud jobs

1. start a prgram as a backgroud job via `&`

[Linux Commands: jobs, bg, and fg | Redhat]: https://www.redhat.com/sysadmin/jobs-bg-fg



### 👉 `pgrep`
[`pgrep`](https://www.man7.org/linux/man-pages/man1/pgrep.1.html)


### 👉 `pkill`
[`pkill`](http://man7.org/linux/man-pages/man1/pgrep.1.html)


`history | awk '{$1="";print substr($0,2)}' | sort | uniq -c | sort -n | tail -n 10`


### 👉 `lsof`
[`lsof`](https://www.man7.org/linux/man-pages/man8/lsof.8.html) lists file information about files opened by processes. It can be quite useful for checking which process has opened a specific file.



## Resource Management of Process
### 👉 `nsenter`
>  🔗
>
>  [nsenter使用](https://www.cnblogs.com/edeny/p/15247306.html) 

> [nsenter](https://man7.org/linux/man-pages/man1/nsenter.1.html)命令是一个可以在指定进程的命令空间下运行指定程序的命令，它位于util-linux包中。其基本原理就是 [Linux Namespace](http://chengqian90.com/Linux%E5%86%85%E6%A0%B8/Linux-Namespace%E7%AE%80%E4%BB%8B.html) 
>
> **`nsenter`** 是用来进入容器内部的一个命令，它的优势之处在于可以自己选择加载容器的那些 `namespaces。`
>
> 说直白一点就是 排查docker容器可以具备inux宿主命令的的方法。
>
> 一典型的用途容器网络命令空间。容器为了轻量级，不包含基础的命令，如说 ip address，ping，telnet，ss，tcpdump 等，给调试容器网络带来很大困扰：只能通过 docker inspect ContainerID 获取容器IP，无法测试和其他网络的连通性。这时使用nsenter命令仅进入该容器的网络命名空间，使用宿主机的命令调试容器网络。nsenter也可以进入 mnt, uts, ipc, pid, user 命令空间，指定根目录和工作目录。
>
> namespace是Linux中一些进程的属性的作用域，使用命名空间，可以隔离不同的进程。



## Ref

