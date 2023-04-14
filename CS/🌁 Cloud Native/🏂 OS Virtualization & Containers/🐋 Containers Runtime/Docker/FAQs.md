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



