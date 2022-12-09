# [Anaconda](https://anaconda.org/daddymir0/dashboard)

``` text

                                                            |
                _` |  __ \    _` |   __|   _ \   __ \    _` |   _` |
               (   |  |   |  (   |  (     (   |  |   |  (   |  (   |
              \__,_| _|  _| \__,_| \___| \___/  _|  _| \__,_| \__,_|

          
```

Anaconda can be seen as **a release version of [[Languages Overview#Python|Python]] **, it helps for easier management of all kinds of packages needed for a python project to run and is trans-plantform. so to run a python project user  just simply downloads Anaconda and simply run it without considering other environment configurations and libraries  whatsoever. 

So to speak, Anaconda is a trans-plantform env-manager & IDE for python. See 📜 official documentation on [anaconda.com](https://docs.anaconda.com)

> *Package, dependency and environment management for any language---Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN*
>
> Conda is an open-source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs, and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. It was created for Python programs but it can package and distribute software for any language.

Anaconda contains **conda** and **Python** and **R** and other 180+ Sci-packages and their dependent packages. 



> ⚠️⚠️⚠️ **USING MIRRO SITE !** 
> to have a better experience of anaconda under GFW, **use mirro site from** [tuna](https://mirrors.tuna.tsinghua.edu.cn), [USTC](http://mirrors.ustc.edu.cn), [BFSU](https://mirrors.bfsu.edu.cn), [tencent](https://mirrors.cloud.tencent.com), [aliyun](https://developer.aliyun.com/mirror/),[HuaWei](https://mirrors.huaweicloud.com/home), [douban](http://pypi.doubanio.com/simple/),  [NPM](https://developer.aliyun.com/special/npm/notice) and so on. 



## 🦮 Guides

###### ⁉️ how to download&use anaconda?

⭐️ [conda常用命令](https://blog.csdn.net/zhayushui/article/details/80433768)

[Anaconda介绍、安装及使用教程](https://www.jianshu.com/p/62f155eb6ac5) 

[Anaconda虚拟环境管理（命令行）](https://blog.csdn.net/mighty13/article/details/119791434)

[新机器上手指南（新手向）](https://taylover2016.github.io/新机器上手指南（新手向）/index.html)



## ⚱️Resources

📂 [Anaconda Documentation](https://docs.anaconda.com/anacondaorg/user-guide/)

📂 [Conda Docs -- conda, conda-build, miniconda](https://docs.conda.io/en/latest/)

## Components

### Conda

###### 👉 [Using conda for the management of envs](https://medium.com/python4u/用conda建立及管理python虛擬環境-b61fd2a76566)

when using anaconda for the env management, it generates and stores all env-related pkgs on its own folder, in my case  `/User/Mir0/opt/anaconda/env`, and thus seperates itself from the pkgs outside. 

on the time writing this note, 20/1/22,  my mac has two sets of sdk: anaconda-related & cammondlinetools-related (commandlinetools is an extension pkg set for Xcode, which enriched SDK required on the development work on macOS). `anaconda` is exclusively for Python dev, while `commandlinetools` aims fo r all sorts of dev including Python dev. Both anaconda and commandlinetools have own seperate Py_dev pkgs. 

and also one thing to notice  is the conception between [[Anaconda#Conda vs pip|Conda & pip]]. 



###### 🆚 Conda vs pip

http://zllbook.tudouwa.fun/Python实战/Python基础/Python包管理及虚拟环境管理.html



### Jupyter

The [Jupyter ](https://jupyter.orgNotebook) Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more. 
+ it can also runs on mobilephone.
+ visit its doc page [here](https://jupyter.org/documentation)
+ Jupyter & JupyterLab

this is a quick tutorial for Jupyter notebook https://zhuanlan.zhihu.com/p/32805175



### RStudio

> [[Languages Overview#R]]
+ **[radian](https://github.com/randy3k/radian)** help to streamline the experience for python & R

+ to run R [[#RStudio]] and [[VScode#R|vscode]] are both supported 

  

### [Python](http://damnwidget.github.io/anaconda/)

> e[[Languages Overview#Python]]

[Pycharm + macOS + Anaconda + ssh ](https://zhuanlan.zhihu.com/p/83791688)



## FAQ

#### 👉 Diff between  anaconda、conda、pip、and virtualenv

+ **anaconda** is a release version of python. it contains any thing you need to run a python proj. and even more.
+ **conda** per se is a package manager. it can help download packages & manage/switch the environment user currently running.  
+ **pip** is simply a downloader inherently built in python.
+ **virtualenv** is simply a env-manager. it help switch through different envs user already has.

More: 

[What is the difference between pip and conda?](https://stackoverflow.com/questions/20994716/what-is-the-difference-between-pip-and-conda)

[Anaconda介绍、安装及使用教程](https://www.jianshu.com/p/62f155eb6ac5)

[conda install和pip install区别](https://www.cnblogs.com/Li-JT/p/14024034.html)

> conda ≈ pip（python包管理） + virtualenv（虚拟环境） + 非python依赖包管理
>
> 级别不一样conda和yum比较类似，可以安装很多库，不限于Python。conda是创建一个局部的环境，并安装相应包；pip是安装包到原有的环境中。
>
> pip install会检查一些依赖包并给你安装，而conda的这种检查更多，甚至会把你已有的卸了替换成他认为合适的...反正conda我只是拿来管理，安装一直是pip install...conda install真心不太喜欢乱检测乱适配....
>
> pip和conda默认源也不一样。conda有很多第三方库，pip是python官方发布库。





#####  ⤴️ To mannually update anaconda...

https://zhuanlan.zhihu.com/p/121601968

```shell
conda update conda
conda update anaconda
conda update --all
```

1. 添加源：

```shell
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/

conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
```

2. 设置启动设置好的国内镜像源

```shell 
conda config --set show_channel_urls yes
```

3. 查看是否添加上了源

```shell
conda config --show
```



## 🗃 logs

###### Jan.24.2022

try to pip opencv to my env. after few failed tryouts, it turned out that [opencv is not supported on Python3.8 yet. ](https://stackoverflow.com/a/58918787/16542494) so i piped Python3.6.2 on pythonProject (env name) instead and pip opencv by `conda install -c conda-forge opencv` found on [this website](https://anaconda.org/conda-forge/opencv) and it worked out finally. 

now working on [this tutorial](https://new.pythonforengineers.com/blog/image-and-video-processing-in-python/)



## 📸 Troubleshootings

#### 👉 `conda update conda` error

Turn out to be the channel site's error. I deleted all other channels but default and conda-forge. Then it worked.



["conda update conda" error #10333]:https://github.com/conda/conda/issues/10333



#### 👉 `Solving environment: failed with initial frozen solve. Retrying with flexible solve`

I highly doubted that this has something to do with my inconsistency envrionment error report. 

I found these solusions but none of them worked for me:

- create a new conda env
- downgrade conda version
- conda config --set priority :false
- conda config  --set priority: flexible 



[Solving environment: failed with initial frozen solve. Retrying with flexible solve.#9367]: https://github.com/conda/conda/issues/9367
[Conda install and update do not work also solving environment get errors]: https://stackoverflow.com/questions/57518050/conda-install-and-update-do-not-work-also-solving-environment-get-errors



#### 👉 The environment is inconsistent, please check the package plan carefully

**Description**

After error occured when downloading anything package from repo, i realized it might be the repo itself went slip. So i deleted every other repo but `default` and `conda-forge` . Then `conda install` again. Since the previous packages are all from situ mirror site, the new "conda" mirror site packages are, as reported, inconsistent.

**Solusion**

Still no solusion to this. 

I desperately tried following shell:

```shell
# all under base env
conda update conda
conda install anaconda
# i run this for several times because i found each time i try it it promptes new updates. There was a time i doubt it can never end...
conda update --all
```

I have no idea how things going.

However after i desperately run above code for several times i can somehow `pip` the package sucessfully like a charm!

But i still cannot `conda install`. Instead i make with `pip`.

🥹🥹🥹🥹



[The environment is inconsistent, please check the package plan carefully #8490]: https://github.com/conda/conda/issues/8490
[How to resolve inconsistent package warnings in conda?]:https://stackoverflow.com/questions/56072846/how-to-resolve-inconsistent-package-warnings-in-conda



#### 👉  Why Conda cannot call correct Python version after activating the environment?

TLDR;

```shell
# deactivate Conda environment
# (until even base environment is deactivated)
conda deactivate
# activate your environment
conda activate your_env_name_goes_here
```

This happened after `conda update --all`. Shut the terminal down and restart. 



[Why Conda cannot call correct Python version after activating the environment?]: https://stackoverflow.com/questions/36733179/why-conda-cannot-call-correct-python-version-after-activating-the-environment
