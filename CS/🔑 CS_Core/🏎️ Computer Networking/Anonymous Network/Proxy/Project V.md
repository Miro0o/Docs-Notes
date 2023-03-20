# [Project V](https://www.v2ray.com/en/index.html)

[TOC]



## Intro
🇨🇳  [官方手册](https://www.v2fly.org)

🇺🇸  [Official mannul](https://www.v2fly.org/en_US/#who-will-lead-the-development-of-project-v)

🌏 [Project GitHub URL](https://github.com/v2fly/v2ray-core)


Project V is a set of tools to help you build your own privacy network over internet. The core of Project V, named `V2Ray`, is responsible for network protocols and communications. It can work alone, as well as combined with other tools.



## v2ray
[V2Ray (V2Fly) 简介](https://v2fly.blogspot.com/2019/06/v2ray-v2fly.html)

🧭 [V2ray 新白话文指南](https://guide.v2fly.org/#声明)

🔗 [V2ray 原始指南](https://github.com/ToutyRater/v2ray-guide)


### v2ray 是什么
**v2ray 是Project V 的核心，** 他是一个代理工具/协议集成环境。v2ray 社区在不断发展壮大的过程中最终形成了Project V 项目。

Project V 包含了与 V2Ray 有关的全部，除了 V2Ray 自己，所有相关的软件、工具、新协议都是 Project V 的一部分。这里的“相关软件”主要指：

1. V2Ray 的一些辅助工具，比如用于生成证书和校验配置文件的工具。
2. 基于 V2Ray 开发的移植到其它平台（Windows、macOS、iOS 等等）的实现，特别是那些带图形界面的。


### v2ray 支持的协议
截止到2019年7月，V2Ray支持以下协议：

- 传统的代理协议：HTTP 和 SOCKS。
- MTProto：Telegram 的开发团队制作的一款协议，作为 Telegram 的专用代理协议。
- Shadowsocks：这个无需多言。
- VMess：V2Ray 独创的一款翻墙协议，比 Shadowsocks 更安全。推荐商家：🫰 [墙裂](https://www.qianglie.com/cart.php)，采用领先的翻墙协议，更高可用性，更高安全性。

同样是截止到2018年12月，V2Ray 可选的传输层配置有：

+ 用于优化网络质量的 kcp、QUIC 和 TCP Fast Open；
+ 用于伪装的 WebSocket；
+ HTTP/2 传输；
+ TLS 加密。


### v2ray 的部署
==deprecated content==

知乎：
[git 设置终端代理](https://www.zhihu.com/question/35928898)

+ trouble shooting logs
  +  [E325: ATTENTION swap file already present error in Vim](https://askubuntu.com/questions/1036030/e325-attention-swap-file-already-present-error-in-vi)   ------ _solved_
  +  [zsh: function definition file not found](https://sibunglon.com/2020/05/24/solve-zsh-function-definition-file-not-found/)  ------ _unsolved_

---


### V2ray GUI
#### [Clash](https://github.com/Dreamacro/clash/wiki)

> + Ref _(un-recommended, i put these here only for logging_)
>	+ https://github.com/Dreamacro/clash/issues/592
>	+ https://blog.csdn.net/qq_36517296/article/details/118599195


 *关于ClashX的一些使用*

+  https://jerrysun.org/skill/2020/02/19/proxy/

+ 7890 --> http/https
+ 7891 --> socks5

+ [重新安装homebrew](https://tonydeng.github.io/2015/07/11/brew-reinstall/)
  + mentioned `.git` and **Git**


##### 💘 Troubleshoutings
###### ✅ Log  `~/.zshrc` .
Date: Nov.3.21
```shell
 # proxy list
alias setproxy="export https_proxy=http://127.0.0.1:7890;export http_proxy=http://127.0.0.1:7890;export all_proxy=socks5://127.0.0.1:7891;echo \"Set proxy successfully\" "
alias unsetproxy="unset http_proxy;unset https_proxy;unset all_proxy;echo \"Unset proxy successfully\" "
```
postscripts:
+ `http_proxy`,`https_proxy`,`ftp_proxy`,and `socks5_proxy` here is environment variable pre-defined by  [POSIX](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap08.html) ?
	+ 👀 see questions on [What's the 'right' format for the HTTP_PROXY environment variable? Caps or no caps?](https://unix.stackexchange.com/questions/212894/whats-the-right-format-for-the-http-proxy-environment-variable-caps-or-no-ca)
+ `export` command here reset these environmnet variable. 



###### ✅ [mac配置clash代理忽略列表](https://wonderlq.github.io/archives/87d77c17.html)
1. 在 ~/.config/clash/ 新建 proxyIgnoreList.plist文件

2. 编辑文件，内容如下:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <array>
       <string>192.168.0.0/16</string>
       <string>10.0.0.0/8</string>
       <string>172.16.0.0/12</string>
       <string>127.0.0.1</string>
       <string>localhost</string>
       <string>*.local</string>
       <string>*.crashlytics.com</string>
       <string>my-custom-site.com</string>
   </array>
   </plist>
   ```

3. 在array最后追加自定义需要忽略的网址。

4. 保存，重启。

5. 打开mac网络配置可以看到新配置。

   ![image](../../../../Assets/Pics/di6Zv2mw7bgtoNU.png)



#### [SSR](https://github.com/Alvin9999/new-pac/wiki/自建ss服务器教程)
ShadowsocksRocket. V2ray for iOS. 



## 🔗 Extensive Readings ...
1. 🫰[duyao 机场测速](https://www.duyaoss.com)
2. 🫰[机场常见名词](https://young1lin.me/2020/10/30/GFW/#机场)
3. [Speech that Enables Speech: China Takes Aim at Its Coders](https://www.eff.org/deeplinks/2015/08/speech-enables-speech-china-takes-aim-its-coders)
4. [Solzhenitsyn: 'Spiritual Death Has... Touched Us All'](https://www.washingtonpost.com/wp-dyn/content/article/2008/08/04/AR2008080401822_pf.html)
5. [Mac让Mail(自带邮箱客户端)的gmail走代理及终端走代理](https://www.xiebruce.top/1061.html)

