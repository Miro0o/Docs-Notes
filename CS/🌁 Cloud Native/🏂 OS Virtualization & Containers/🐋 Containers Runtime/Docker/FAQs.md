# FAQs

[TOC]



## 👉 docker mirror sites
```shell
cd /etc/docker
vim daemon.json
```
```json
{
  "registry-mirrors": [
    "https://hub-mirror.c.163.com",
    "https://ustc-edu-cn.mirror.aliyuncs.com",
    "https://ghcr.io",
    "https://mirror.baidubce.com"
  ]
}
```



## 👉 Docker Network
### Change Docker Network
When you start a container, such as: 
```shell
docker run -d --name alpine1 alpine
```

It is by default connected to the `bridge` network, check it with:
```shell
docker container inspect alpine1
```

If you try to connect it to `host` network with:
```shell
docker network connect host alpine1
```

you obtain an error:
> Error response from daemon: container cannot be disconnected from host network or connected to host network

you have to delete the container and run it again on the host network:
```shell
docker stop alpine1
docker rm alpine1
docker run -d --network host --name alpine1 alpine
```

This limitation is not present on bridge networks. You can start a container:
```shell
docker run -d --name alpine2 alpine
```

disconnect it from the bridge network and reconnect it to another bridge network.
```shell
docker network disconnect bridge alpine2
docker network create --driver bridge alpine-net
docker network connect alpine-net alpine2
```

Note also that according to the [documentation](https://docs.docker.com/network/host/):

> The host networking driver only works on Linux hosts, and is not supported on Docker Desktop for Mac, Docker Desktop for Windows, or Docker EE for Windows Server.



[How to change the network of a running docker container?]: https://stackoverflow.com/questions/54720587/how-to-change-the-network-of-a-running-docker-container

[👍 Docker容器网络更改 | 51cto]: https://blog.51cto.com/u_15127640/3909055
[👍 Docker容器间网络通信的方案 - 运维笔记 | 51cto]: https://blog.51cto.com/u_6215974/4937668
[👍 docker容器内部端口映射到外部宿主机端口 | 51cto]: https://blog.51cto.com/lovebetterworld/2839896#2ipip19216810214_30

[Docker 之容器间通信配置 | 腾讯云]: https://cloud.tencent.com/developer/article/1674259
[Docker容器访问宿主机 | 简书]: https://www.jianshu.com/p/4a358a120983



## Ref
1. 👍 [Docker配置文件-Dockerfile详解](https://www.cnblogs.com/pengrj/p/13600185.html) 
2. [Docker容器的创建、启动、和停止](https://www.cnblogs.com/linjiqin/p/8608975.html) 
3. [Docker安装Mysql](https://wangchujiang.com/mysql-tutorial/chapter2/2.3.html)
4. 👍 [docker安装tomcat并部署Springboot项目war包的方法](http://m.studyofnet.com/news/6041.html)
5. 👍 [使用Docker安装配置Tomcat](https://www.voidking.com/dev-docker-tomcat/)
6. [给Docker中的Mysql导入sql文件数据](https://blog.csdn.net/fxtxz2/article/details/103362243)
7. [Docker安装mysql及mysql数据库的导入与导出](https://blog.csdn.net/weixin_36586564/article/details/102589486)
8. [在docker中安装mysql并使用](https://blog.51cto.com/u_15127647/4312701)
9. 👍 [Docker compose 配置文件详解](https://www.jianshu.com/p/2217cfed29d7)
10. [docker更换成国内镜像源](https://blog.51cto.com/u_13281972/2997681)
11. 👍 [本地项目部署到服务器——docker-nginx](httpns://cloud.tencent.com/developer/article/1644896)
12. [使用Docker部署简单的项目](https://segmentfault.com/a/1190000039239790)
13. [MacOS 安装 Docker](https://www.widuu.com/docker/installation/mac.html)
14. 👍 [Docker（34）- 如何修改 docker 容器的目录映射 ](https://www.cnblogs.com/poloyy/p/13993832.html)
15. [Docker无法正常启动的原因及解决办法](https://blog.csdn.net/u010716706/article/details/69524863)
16. [Mounting multiple volumes on a docker container?](https://stackoverflow.com/questions/18861834/mounting-multiple-volumes-on-a-docker-container) 
    1. 🤷 however i still have the problem on my baiduClound LS (Debian 10). I can't mount more than 1 volumes / directories on one dokcer container.  It didn't seem like i was running out of the memory. 
17. 👍 [docker基础知识之挂载本地目录的方法](https://blog.51cto.com/6226001001/1953035)
18. 👍 [关于Docker目录挂载的总结](https://www.cnblogs.com/ivictor/p/4834864.html)
19. (unfinished...) [DOCKER FOR MAC - SAFELY RESET FROM FACTORY DEFAULTS](https://corgibytes.com/blog/2019/05/13/docker-for-mac-safely-reset-from-factory-defaults/)
20. 
