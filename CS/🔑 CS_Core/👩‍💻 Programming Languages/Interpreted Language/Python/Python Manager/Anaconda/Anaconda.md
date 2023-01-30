# [Anaconda](https://anaconda.org/daddymir0/dashboard)

[TOC]



``` text

                                                            |
                _` |  __ \    _` |   __|   _ \   __ \    _` |   _` |
               (   |  |   |  (   |  (     (   |  |   |  (   |  (   |
              \__,_| _|  _| \__,_| \___| \___/  _|  _| \__,_| \__,_|

          
```





## ⚱️Resources

📂 [Anaconda Documentation](https://docs.anaconda.com/anacondaorg/user-guide/)

📂 [Conda Docs -- conda, conda-build, miniconda](https://docs.conda.io/en/latest/)

### Guides

⭐️ [conda常用命令](https://blog.csdn.net/zhayushui/article/details/80433768)

[Anaconda介绍、安装及使用教程](https://www.jianshu.com/p/62f155eb6ac5) 

[Anaconda虚拟环境管理（命令行）](https://blog.csdn.net/mighty13/article/details/119791434)

[新机器上手指南（新手向）](https://taylover2016.github.io/新机器上手指南（新手向）/index.html)

### Anaconda Integration

[anaconda + sublime text3](http://damnwidget.github.io/anaconda/)

[Pycharm + macOS + Anaconda + ssh ](https://zhuanlan.zhihu.com/p/83791688)



## Intro

Anaconda can be seen as **a release version of Python **, it helps for easier management of all kinds of packages needed for a python project to run and is trans-plantform. so to run a python project user just simply downloads Anaconda and simply run it without considering other environment configurations and libraries  whatsoever. 

So to speak, Anaconda is a trans-plantform env-manager & IDE for python. See 📜 official documentation on [anaconda.com](https://docs.anaconda.com)

> *Package, dependency and environment management for any language---Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN*
>
> Conda is an open-source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs, and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. It was created for Python programs but it can package and distribute software for any language.

Anaconda contains **conda** and **Python** and **R** and other 180+ Sci-packages and their dependent packages. 



> ⚠️⚠️⚠️ **USING MIRRO SITE !** 
> to have a better experience of anaconda under GFW, **use mirro site from** [tuna](https://mirrors.tuna.tsinghua.edu.cn), [USTC](http://mirrors.ustc.edu.cn), [BFSU](https://mirrors.bfsu.edu.cn), [tencent](https://mirrors.cloud.tencent.com), [aliyun](https://developer.aliyun.com/mirror/),[HuaWei](https://mirrors.huaweicloud.com/home), [douban](http://pypi.doubanio.com/simple/),  [NPM](https://developer.aliyun.com/special/npm/notice) and so on. 





## Components

### Conda

#### 👉 [Using conda for the management of envs](https://medium.com/python4u/用conda建立及管理python虛擬環境-b61fd2a76566)

when using anaconda for the env management, it generates and stores all env-related pkgs on its own folder, in my case  `/User/Mir0/opt/anaconda/env`, and thus seperates itself from the pkgs outside. 

on the time writing this note, 20/1/22,  my mac has two sets of sdk: anaconda-related & cammondlinetools-related (commandlinetools is an extension pkg set for Xcode, which enriched SDK required on the development work on macOS). `anaconda` is exclusively for Python dev, while `commandlinetools` aims fo r all sorts of dev including Python dev. Both anaconda and commandlinetools have own seperate Py_dev pkgs. 

and also one thing to notice  is the conception between [[Anaconda#Conda vs pip|Conda & pip]]. 



#### 🆚 Conda vs pip

http://zllbook.tudouwa.fun/Python实战/Python基础/Python包管理及虚拟环境管理.html



### Jupyter

The [Jupyter ](https://jupyter.orgNotebook) Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more. 
+ it can also runs on mobilephone.
+ visit its doc page [here](https://jupyter.org/documentation)
+ Jupyter & JupyterLab

this is a quick tutorial for Jupyter notebook https://zhuanlan.zhihu.com/p/32805175



### RStudio

+ **[radian](https://github.com/randy3k/radian)** help to streamline the experience for python & R

+ to run R [[#RStudio]] and [[VScode#R|vscode]] are both supported 

  

## Ref
