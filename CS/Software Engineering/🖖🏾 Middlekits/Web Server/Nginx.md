# [Nginx](https://www.nginx.com)

[TOC]



## 🧭 Guides

[nginx.cn](https://www.nginx.cn)    |    [nginx.com](https://www.nginx.com)    |    [nginx.org](https://nginx.org)



### 🎁 Resources

📂 [Official docs](https://nginx.org/en/docs/)

📂 [nginx 中文官方文档](https://wizardforcel.gitbooks.io/nginx-doc/content/index.html)





### ⚙️ Installation

Since on my newly-bought Baidu Cloud LS with CentOS8 the `dnf` package manager cannot install the LST version of Nginx, i had to manually install it. below is the how.

The KEY is to get Ningx installed under appropriate directory as neat and elegant as other things installed on a package manger. 

The right directory for binary file is `/usr/local/src` and then unzipped file on `/usr/local/nginx` then the executable under `/usr/local/bin` 

Finally symlink to `/usr/local/bin`

```shell
ln -s /usr/local/nodejs/bin/npm /usr/local/bin/ 
ln -s /usr/local/nodejs/bin/node /usr/local/bin/
```

#### refs :

1. [符号链接](https://www.geek-share.com/detail/2783343863.html)



### 📦 Configs

use `nginx -t`  to check out  `nginx.config` file.



#### refs:

1. [Full Example Configuration](https://www.nginx.com/resources/wiki/start/topics/examples/full/)



### 🗺 Directory

#### DocumentRoot:

`/usr/local/var/www`

`/usr/local/Cellar/nginx/1.21.6_1/html`



#### Configuration:

>  By default, the configuration file is named `nginx.conf` and placed in the directory `/usr/local/nginx/conf`, `/etc/nginx`, or `/usr/local/etc/nginx`.

in my case : `/usr/local/etc/nginx`



## 🖇 Refs

1. [nginx入门系列之安装与卸载](https://www.cnblogs.com/nuccch/p/11874221.html) 
2. [nginx搭建静态资源服务器](https://zhuanlan.zhihu.com/p/55698543)
3. [Nginx（二）------nginx.conf 配置文件](https://www.cnblogs.com/ysocean/p/9384880.html) 
4. [What does upsteam means in Nginx](https://stackoverflow.com/a/5877989/16542494)

