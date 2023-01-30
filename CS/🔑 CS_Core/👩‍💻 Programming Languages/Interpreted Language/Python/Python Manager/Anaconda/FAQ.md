# FAQ

[TOC]



## 👉 Diff between  anaconda、conda、pip、and virtualenv

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





## 👉 To mannually update anaconda...

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



