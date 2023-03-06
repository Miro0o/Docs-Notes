# 🐳 [Docker](https://hub.docker.com/search?q=)



[TOC]

## 💍 Resources

📂 [Docker Docs](https://docs.docker.com)

🗺 [Docker 学习路线 ](https://www.cnblogs.com/poloyy/p/15257059.html)

[Docker 中文指南](https://www.widuu.com/docker/index.html)

[Docker 从入门到实践](https://yeasy.gitbook.io/docker_practice/)

[Docker 教程 -- 菜鸟](https://www.runoob.com/docker/docker-tutorial.html)



## 🧑🏿‍🦯 Guides

### 👬 Community

[Dockerone.io](https://www.dockone.io)



### 🧱 Setup

There are two popullar docker implementation on Mac:

1. Docker Desktop
2. Lima VM + nerdctl + containered

Due to efficiency concern, i abandoned Docker Decktop and embraced Lima. 

Following context are about Lima implementation. 



#### 1️⃣ Docker Desktop

deprecated. : )



##### 🖇 Links:

[Docker on Mac - how to speed it up?]:https://accesto.com/blog/docker-on-mac-how-to-speed-it-up/
[cgroup]:https://www.kernel.org/doc/Documentation/cgroup-v1/
[使用 docker 对容器资源进行限制]:https://www.dockone.io/article/2569
[向Docker告别的时候到了]:https://juejin.cn/post/6911121470693310478



#### 2️⃣ [Lima](https://github.com/lima-vm/lima)

 👀 See further detail in [Lima.md](../../Lima/Lima.md) 



#### 🐳  Docker

> mainly follow [docker official tutorial](https://docs.docker.com/get-started/)

##### What is a container?

Now that you’ve run a container, what *is* a container? Simply put, a container is a sandboxed process on your machine that is isolated from all other processes on the host machine. That isolation leverages [kernel namespaces and cgroups](https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504), features that have been in Linux for a long time. Docker has worked to make these capabilities approachable and easy to use. To summarize, a container:

- is a runnable instance of an image. You can create, start, stop, move, or delete a container using the DockerAPI or CLI.
- can be run on local machines, virtual machines or deployed to the cloud.
- is portable (can be run on any OS).
- is isolated from other containers and runs its own software, binaries, and configurations.

> creat containers from scretch :https://youtu.be/8fi7uSYlOdc



### 🐋 [Dockerhub](https://hub.docker.com)

**Intro**

[Docker Hub](https://hub.docker.com/) is a service provided by Docker for finding and sharing container images with your team. It is the world’s largest repository of container images with an array of content sources including container community developers, open source projects and independent software vendors (ISV) building and distributing their code in containers.

Users get access to free public repositories for storing and sharing images or can choose a [subscription plan](https://www.docker.com/pricing) for private repositories.

**How-to**



More registries, see Registry, Harbor, etc..



### 🔮 What's next...

#### Container orchestration

Running containers in production is tough. You don’t want to log into a machine and simply run a `docker run` or `docker-compose up`. Why not? Well, what happens if the containers die? How do you scale across several machines? **Container orchestration** solves this problem. Tools like **Kubernetes, Swarm, Nomad, and ECS** all help solve this problem, all in slightly different ways.

The general idea is that you have “managers” who receive **expected state**. This state might be “I want to run two instances of my web app and expose port 80.” The managers then look at all of the machines in the cluster and delegate work to “worker” nodes. The managers watch for changes (such as a container quitting) and then work to make **actual state** reflect the expected state.



#### Cloud Native Computing Foundation projects

The CNCF is a vendor-neutral home for various open-source projects, including **Kubernetes, Prometheus, Envoy, Linkerd, NATS**, and more! You can view the [graduated and incubated projects here](https://www.cncf.io/projects/) and the entire [CNCF Landscape here](https://landscape.cncf.io/). There are a LOT of projects to help solve problems around monitoring, logging, security, image registries, messaging, and more!

So, if you’re new to the container landscape and cloud-native application development, welcome! Please connect with the community, ask questions, and keep learning! We’re excited to have you!



## 🤨 FAQs

##### 👉 docker mirror sites

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





## 🔗 Reading List:

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
