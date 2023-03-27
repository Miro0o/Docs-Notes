# NFS

[TOC]



## Res


## Intro
### Platforms
SMB and [NetWare Core Protocol](https://en.wikipedia.org/wiki/NetWare_Core_Protocol "NetWare Core Protocol") (NCP) occur more often than NFS on systems running Microsoft Windows;

AFP occurs more often than NFS in Apple Macintosh systems;

QFileSvr.400 occurs more often in IBM i systems.

[Haiku](https://en.wikipedia.org/wiki/Haiku_(operating_system) "Haiku (operating system)") in 2012 added NFSv4 support as part of a Google Summer of Code project.


### Protocol Development
> 🔗 https://en.wikipedia.org/wiki/Network_File_System


#TODO 



## Ref
[NFS网络文件系统简介]: https://cloud-atlas.readthedocs.io/zh_CN/latest/infra_service/nfs/intro_nfs.html

为解决本地文件系统的限制 (磁盘空间有限、无法多客户端共享访问)，网络文件系统(Network File System, NFS)被发明出来:
- 多个客户端可以共享访问服务器上相同的文件
- 非常便于集中管理NFS服务器上的文件(提供一定的安全性)，例如集中备份、冗灾等'

网络文件系统(NFS)是一个守护进程，它允许其他计算机在另一台远程计算机上 `挂载` 磁盘文件系统目录，并像访问本地文件和文件夹一样访问这些文件。
NFS最早是Sun Microsystems公司于1984年发明

[1. NFS简介]: https://www.huweihuang.com/linux-notes/tools/nfs-usage.html

[一个 NFS 的简介]: https://planet.ustclug.org/post/217

[NFS介绍与配置]: https://www.plob.org/article/125.html

[认识 NFS 文件共享协议]: https://zhuanlan.zhihu.com/p/31626338


