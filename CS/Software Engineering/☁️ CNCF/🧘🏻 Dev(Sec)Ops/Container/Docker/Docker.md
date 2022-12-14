# ð³ [Docker](https://hub.docker.com/search?q=)



[TOC]

## ð Resources

ð [Docker Docs](https://docs.docker.com)

ðº [Docker å­¦ä¹ è·¯çº¿ ](https://www.cnblogs.com/poloyy/p/15257059.html)

[Docker ä¸­ææå](https://www.widuu.com/docker/index.html)

[Docker ä»å¥é¨å°å®è·µ](https://yeasy.gitbook.io/docker_practice/)

[Docker æç¨ -- èé¸](https://www.runoob.com/docker/docker-tutorial.html)



## ð§ð¿âð¦¯ Guides

### ð¬ Community

[Dockerone.io](https://www.dockone.io)



### ð§± Setup

There are two popullar docker implementation on Mac:

1. Docker Desktop
2. Lima VM + nerdctl + containered

Due to efficiency concern, i abandoned Docker Decktop and embraced Lima. 

Following context are about Lima implementation. 



#### 1ï¸â£ Docker Desktop

deprecated. : )



##### ð Links:

[Docker on Mac - how to speed it up?]:https://accesto.com/blog/docker-on-mac-how-to-speed-it-up/
[cgroup]:https://www.kernel.org/doc/Documentation/cgroup-v1/
[ä½¿ç¨ docker å¯¹å®¹å¨èµæºè¿è¡éå¶]:https://www.dockone.io/article/2569
[åDockeråå«çæ¶åå°äº]:https://juejin.cn/post/6911121470693310478



#### 2ï¸â£ [Lima](https://github.com/lima-vm/lima)

 ð See further detail in [Lima.md](Lima.md) 



#### ð³  Docker

> mainly follow [docker official tutorial](https://docs.docker.com/get-started/)

##### What is a container?

Now that youâve run a container, what *is* a container? Simply put, a container is a sandboxed process on your machine that is isolated from all other processes on the host machine. That isolation leverages [kernel namespaces and cgroups](https://medium.com/@saschagrunert/demystifying-containers-part-i-kernel-space-2c53d6979504), features that have been in Linux for a long time. Docker has worked to make these capabilities approachable and easy to use. To summarize, a container:

- is a runnable instance of an image. You can create, start, stop, move, or delete a container using the DockerAPI or CLI.
- can be run on local machines, virtual machines or deployed to the cloud.
- is portable (can be run on any OS).
- is isolated from other containers and runs its own software, binaries, and configurations.

> creat containers from scretch :https://youtu.be/8fi7uSYlOdc



### ð [Dockerhub](https://hub.docker.com)

**Intro**

[Docker Hub](https://hub.docker.com/) is a service provided by Docker for finding and sharing container images with your team. It is the worldâs largest repository of container images with an array of content sources including container community developers, open source projects and independent software vendors (ISV) building and distributing their code in containers.

Users get access to free public repositories for storing and sharing images or can choose a [subscription plan](https://www.docker.com/pricing) for private repositories.

**How-to**



More registries, see Registry, Harbor, etc..



### ð® What's next...

#### Container orchestration

Running containers in production is tough. You donât want to log into a machine and simply run a `docker run` or `docker-compose up`. Why not? Well, what happens if the containers die? How do you scale across several machines? **Container orchestration** solves this problem. Tools like **Kubernetes, Swarm, Nomad, and ECS** all help solve this problem, all in slightly different ways.

The general idea is that you have âmanagersâ who receive **expected state**. This state might be âI want to run two instances of my web app and expose port 80.â The managers then look at all of the machines in the cluster and delegate work to âworkerâ nodes. The managers watch for changes (such as a container quitting) and then work to make **actual state** reflect the expected state.



#### Cloud Native Computing Foundation projects

The CNCF is a vendor-neutral home for various open-source projects, including **Kubernetes, Prometheus, Envoy, Linkerd, NATS**, and more! You can view the [graduated and incubated projects here](https://www.cncf.io/projects/) and the entire [CNCF Landscape here](https://landscape.cncf.io/). There are a LOT of projects to help solve problems around monitoring, logging, security, image registries, messaging, and more!

So, if youâre new to the container landscape and cloud-native application development, welcome! Please connect with the community, ask questions, and keep learning! Weâre excited to have you!



## ð¤¨ FAQs

##### ð docker mirror sites

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





## ð Reading List:

1. ð [Dockeréç½®æä»¶-Dockerfileè¯¦è§£](https://www.cnblogs.com/pengrj/p/13600185.html) 
2. [Dockerå®¹å¨çåå»ºãå¯å¨ãååæ­¢](https://www.cnblogs.com/linjiqin/p/8608975.html) 
3. [Dockerå®è£Mysql](https://wangchujiang.com/mysql-tutorial/chapter2/2.3.html)
4. ð [dockerå®è£tomcatå¹¶é¨ç½²Springbooté¡¹ç®waråçæ¹æ³](http://m.studyofnet.com/news/6041.html)
5. ð [ä½¿ç¨Dockerå®è£éç½®Tomcat](https://www.voidking.com/dev-docker-tomcat/)
6. [ç»Dockerä¸­çMysqlå¯¼å¥sqlæä»¶æ°æ®](https://blog.csdn.net/fxtxz2/article/details/103362243)
7. [Dockerå®è£mysqlåmysqlæ°æ®åºçå¯¼å¥ä¸å¯¼åº](https://blog.csdn.net/weixin_36586564/article/details/102589486)
8. [å¨dockerä¸­å®è£mysqlå¹¶ä½¿ç¨](https://blog.51cto.com/u_15127647/4312701)
9. ð [Docker compose éç½®æä»¶è¯¦è§£](https://www.jianshu.com/p/2217cfed29d7)
10. [dockeræ´æ¢æå½åéåæº](https://blog.51cto.com/u_13281972/2997681)
11. ð [æ¬å°é¡¹ç®é¨ç½²å°æå¡å¨ââdocker-nginx](httpns://cloud.tencent.com/developer/article/1644896)
12. [ä½¿ç¨Dockeré¨ç½²ç®åçé¡¹ç®](https://segmentfault.com/a/1190000039239790)
13. [MacOS å®è£ Docker](https://www.widuu.com/docker/installation/mac.html)
14. ð [Dockerï¼34ï¼- å¦ä½ä¿®æ¹ docker å®¹å¨çç®å½æ å° ](https://www.cnblogs.com/poloyy/p/13993832.html)
15. [Dockeræ æ³æ­£å¸¸å¯å¨çåå åè§£å³åæ³](https://blog.csdn.net/u010716706/article/details/69524863)
16. [Mounting multiple volumes on a docker container?](https://stackoverflow.com/questions/18861834/mounting-multiple-volumes-on-a-docker-container) 
    1. ð¤· however i still have the problem on my baiduClound LS (Debian 10). I can't mount more than 1 volumes / directories on one dokcer container.  It didn't seem like i was running out of the memory. 
17. ð [dockeråºç¡ç¥è¯ä¹æè½½æ¬å°ç®å½çæ¹æ³](https://blog.51cto.com/6226001001/1953035)
18. ð [å³äºDockerç®å½æè½½çæ»ç»](https://www.cnblogs.com/ivictor/p/4834864.html)
19. (unfinished...) [DOCKER FOR MAC - SAFELY RESET FROM FACTORY DEFAULTS](https://corgibytes.com/blog/2019/05/13/docker-for-mac-safely-reset-from-factory-defaults/)
20. 
