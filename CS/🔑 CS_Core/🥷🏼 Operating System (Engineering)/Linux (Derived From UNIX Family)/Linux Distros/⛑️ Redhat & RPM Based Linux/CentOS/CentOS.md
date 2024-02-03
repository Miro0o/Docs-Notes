# CentOS 8

> based on Baidu Clound LightServer.



## 🫵🏽 Guides

### 🌐 Overview

> CentOS 8 宣布21年底停止支持，升级至CentOS Stream：
>
> [CentOS 支持到期 生产环境还有哪些选择](https://www.cnblogs.com/wswind/p/centos-alternatives.html) 
>
> [What is CentOS Stream?](https://www.redhat.com/en/topics/linux/what-is-centos-stream)



## 🗑 Troubleshooting

##### 👉 CentOS 8 换源

###### 1️⃣ Overview

[CentOS 8 / CentOS Stream 换源，设置dnf / yum镜像](https://www.cnblogs.com/wswind/p/11751829.html) 

centos 8 默认是会读取centos.org的mirrorlist的，所以一般来说是不需要配置镜像的。
如果你的网络访问mirrorlist有问题，才需要另外配置
相关镜像配置，请参考各镜像站的相关帮助

1. https://developer.aliyun.com/mirror/centos
2. https://mirrors.tuna.tsinghua.edu.cn/help/centos/
3. http://mirrors.ustc.edu.cn/help/centos.html
4. https://mirrors.huaweicloud.com/



###### 2️⃣ Aproaches:

1. change mirrorsite
   1. aliyun
   2. ustc
   3. tuna
   4. ...
2. sed
3. EPEL ([What is EPEL?](https://docs.fedoraproject.org/en-US/epel/))
4. dnf fastest mirror



###### 3️⃣ Example

take `tuna.tsinghua.edu.cn` for example:

> https://mirrors.tuna.tsinghua.edu.cn/help/centos/

1. Backup  `/etc/yum.repos.d/`
2. Edit `CentOS-*.repo` files in  `/etc/yum.repos.d/` : 
   1. 在 `mirrorlist=` 开头行前面加 `#` 注释掉；并将 `baseurl=` 开头行取消注释（如果被注释的话）。 对于 CentOS 7 ，请把该行内的域名（例如`mirror.centos.org`）替换为 `mirrors.tuna.tsinghua.edu.cn`。 对于 CentOS 8 ，请把 `mirror.centos.org/$contentdir` 替换为 `mirrors.tuna.tsinghua.edu.cn/centos`
3.  `sudo yum makecache`

