# [Node.JS](https://nodejs.org/en/)

Node.js® is a JavaScript runtime built on [Chrome's V8 JavaScript engine](https://v8.dev/).

📑 Look up [NodeJS API manual](https://nodejs.org/docs/latest-v17.x/api/documentation.html)

[ECMAScript Language Specification](https://tc39.es/ecma262/)

<u>contents tbd...</u>



[TOC]



## Res

[cnodajs.org](https://cnodejs.org) -- nodejs中文社区

[nodejs.org](https://nodejs.org/en/)



## 🕶 Guides

### 🔨 Installation

> go to `Node.JS` download page:  *[nodejs.org/download](https://nodejs.org/en/download/)*
>
> and also remember to check out this guide:  🤯 *[Installing Node.js via package manager](https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions)* 



#### For `Debian` distributions:

For some unknown reasons every time i tried to download `nodejs` on `Debian` i encountered this problem: i can only get `nodejs` for version 10 and there's no `npm` attatched. And when i tried to download `npm` manually the version won't match. It was really driving me crazy. 

After goolging around i found solution: 

As instructions following the above page says, reference **[NodeSource](https://github.com/nodesource/distributions/blob/master/README.md)** for full version supported download of `nodejs`.

e.g. : **Node.js LTS (v16.x)**:

```shell
# Using Ubuntu
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Using Debian, as root
curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
apt-get install -y nodejs
```



## nvm



## [npm](https://www.npmjs.com)



### npx



## 🔗 Refs

1. [node.js与nvm、npm的关系](https://juejin.cn/post/6844904013398278157)
2. [JavaScript 包管理器工作原理简介](