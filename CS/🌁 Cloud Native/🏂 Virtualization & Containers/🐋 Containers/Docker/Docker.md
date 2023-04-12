# 🐳 [Docker](https://hub.docker.com/search?q=)

[TOC]



![](../../../../../Assets/Pics/Pasted%20image%2020230308140205.png)

## 💍 Res
### Learning Docs
📂 [Docker Docs](https://docs.docker.com)
🗺 [Docker 学习路线 ](https://www.cnblogs.com/poloyy/p/15257059.html)
[Docker 中文指南](https://www.widuu.com/docker/index.html)
[Docker 从入门到实践](https://yeasy.gitbook.io/docker_practice/)

[Docker.com - Educational Resources](https://docs.docker.com/get-started/resources/)

[Docker 教程 -- 菜鸟](https://www.runoob.com/docker/docker-tutorial.html)

### 👬 Community
[Dockerone.io](https://www.dockone.io)



## 🧑🏿‍🦯 Basics

> 🔗 https://docs.docker.com/get-started/overview/
> 🔗 [Language-specific Guides](https://docs.docker.com/language/)

### Docker Architecture
![](../../../../../../Assets/Pics/Screenshot%202023-03-07%20at%201.29.34%20PM.png)

> **The underlying technology**
> 
> ↗ [Golang](../../../../🔑%20CS_Core/👩‍💻%20Languages%20Programming/Compiled%20Languages/Golang/Golang.md)
> ↗ 
> 
> Docker is written in the [Go programming language](https://golang.org/) and takes advantage of several features of the Linux kernel to deliver its functionality. Docker uses a technology called `namespaces` to provide the isolated workspace called the _container_. When you run a container, Docker creates a set of _namespaces_ for that container.
> 
> These namespaces provide a layer of isolation. Each aspect of a container runs in a separate namespace and its access is limited to that namespace.


#### Docker Client
> **docker client configurations**
> `~/.docker/config.json`


The Docker client (`docker`) is the primary way that many Docker users interact with Docker. When you use commands such as `docker run`, the client sends these commands to `dockerd`, which carries them out. The `docker` command uses the Docker API. **The Docker client can communicate with more than one daemon.**


#### Docker Host
> 🔗 [Configure the daemon with systemd](https://docs.docker.com/config/daemon/systemd/#httphttps-proxy)
> 
> **dockerd configurations**
> Docker Host Server running `dockerd` daemon on the background, which is managed by the host OS service management unit (in this case `systemd`). 
> 
> **regular mode**
> `/etc/systemd/system/docker.service.d`
> 
> **rootless mode**
> `~/.config/systemd/user/docker.service.d`
> 
  restart system service:
> ```shell
> systemctl --user daemon-reload
> systemctl --user restart docker
> ```

When you use Docker, you are creating and using images, containers, networks, volumes, plugins, and other objects. This section is a brief overview of some of those objects.


##### Images
An _image_ is a read-only template with instructions for creating a Docker container. Often, an image is _based on_ another image, with some additional customization. 

You might create your own images or you might only use those created by others and published in a registry. To build your own image, you create a `Dockerfile` with a simple syntax for defining the steps needed to create the image and run it.

> Use `docker build` to build an container by `dockerfile`
> Use `docker compose` to compose an container by `docker-compose.yaml`


##### Containers
A container is a sandboxed process on your machine that is isolated from all other processes on the host machine. 

> 💡 This isolation leverages [kernel namespaces and cgroups](https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504), features that have been in Linux for a long time. 

Docker has worked to make these capabilities approachable and easy to use. To summarize, a container:

- is a runnable instance of an image. You can create, start, stop, move, or delete a container using the DockerAPI or CLI.
- can be run on local machines, virtual machines or deployed to the cloud.
- is portable (can be run on any OS).
- is isolated from other containers and runs its own software, binaries, and configurations.

> creat containers from scretch :https://youtu.be/8fi7uSYlOdc


##### Networking
[nicolaka/netshoot](https://github.com/nicolaka/netshoot) is a container running within a docker network that provides network tools.


##### Persistng DB
```shell
## Using Container Volume 
docker volume create todo-db
docker run -dp 3000:3000 --mount type=volume,src=todo-db,target=/etc/todos getting-started

docker volume inspect todo-db


## Using bind mounts
docker run -it --mount type=bind,src="$(pwd)",target=/src ubuntu bash

docker run -dp 3000:3000 \
    -w /app --mount type=bind,src="$(pwd)",target=/app \
    node:18-alpine \
    sh -c "yarn install && yarn run dev"


docker logs -f <container-id>
```

##### Container Building


##### Service Composing


#### Docker Registries /Repositeries
##### 🐋 [Dockerhub](https://hub.docker.com)
[Docker Hub](https://hub.docker.com/) is a service provided by Docker for finding and sharing container images with your team. It is the world’s largest repository of container images with an array of content sources including container community developers, open source projects and independent software vendors (ISV) building and distributing their code in containers.

Users get access to free public repositories for storing and sharing images or can choose a [subscription plan](https://www.docker.com/pricing) for private repositories.


##### Docker Registry
The Registry is a stateless, highly scalable server side application that stores and lets you distribute Docker images. The Registry is open-source, under the permissive [Apache license](https://en.wikipedia.org/wiki/Apache_License). You can find the source code on [Distribution](https://github.com/distribution/distribution).

> ↗
> See insights of [Docker Registry](Docker%20Insights/Docker%20Registry.md) notes
> or visit it online at https://docs.docker.com/registry/

> **Distribution**
> This repository's main product is the Open Source Registry implementation for storing and distributing container images using the [OCI Distribution Specification](https://github.com/opencontainers/distribution-spec).


##### [Harbor](https://goharbor.io)
Harbor is an open source registry that secures artifacts with policies and role-based access control, ensures images are scanned and free from vulnerabilities, and signs images as trusted. 
Harbor, a CNCF Graduated project, delivers compliance, performance, and interoperability to help you consistently and securely manage artifacts across cloud native compute platforms like Kubernetes and Docker.

##### More Docker Registries
🔗 [CNCF Cloud Native Registries](https://landscape.cncf.io/card-mode?category=container-registry&grouping=category)


### 🧱 Getting Docker Host...
There are two popullar docker implementations on Mac:
1. Docker Desktop
2. Lima VM + nerdctl + containered

Due to efficiency concern, i abandoned Docker Decktop and embraced Lima. 
Following context are about Lima implementation. 


#### 1️⃣ Docker Desktop
deprecated. : )



[Docker on Mac - how to speed it up?]:https://accesto.com/blog/docker-on-mac-how-to-speed-it-up/
[cgroup]:https://www.kernel.org/doc/Documentation/cgroup-v1/
[使用 docker 对容器资源进行限制]:https://www.dockone.io/article/2569
[向Docker告别的时候到了]:https://juejin.cn/post/6911121470693310478


#### 2️⃣ [Lima](https://github.com/lima-vm/lima)
👀 See details at ↗ [Lima](../../Lima/Lima.md) 

🙈 Also at ↗ [Colima](../../Lima/Colima.md)


#### 3️⃣ OrbStack
THE BEST !

↗ [OrbStack](../../OrbStack/OrbStack.md)



## 🔮 Develop with Docker
### Docker Deployment
#TODO 


### Cloud Deployment



### Orchestration
#### Container orchestration
Running containers in production is tough. You don’t want to log into a machine and simply run a `docker run` or `docker-compose up`. Why not? Well, what happens if the containers die? How do you scale across several machines? **Container orchestration** solves this problem. Tools like **Kubernetes, Swarm, Nomad, and ECS** all help solve this problem, all in slightly different ways.

The general idea is that you have “managers” who receive **expected state**. This state might be “I want to run two instances of my web app and expose port 80.” The managers then look at all of the machines in the cluster and delegate work to “worker” nodes. The managers watch for changes (such as a container quitting) and then work to make **actual state** reflect the expected state.


#### Cloud Native Computing Foundation Projects
> ↗ Clound Native Projects notes are here --> [Cloud Native](../../../../../🌁%20Cloud%20Native/Cloud%20Native.md)

The CNCF is a vendor-neutral home for various open-source projects, including **Kubernetes, Prometheus, Envoy, Linkerd, NATS**, and more! You can view the [graduated and incubated projects here](https://www.cncf.io/projects/) and the entire [CNCF Landscape here](https://landscape.cncf.io/). There are a LOT of projects to help solve problems around monitoring, logging, security, image registries, messaging, and more!

So, if you’re new to the container landscape and cloud-native application development, welcome! Please connect with the community, ask questions, and keep learning! We’re excited to have you!



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
