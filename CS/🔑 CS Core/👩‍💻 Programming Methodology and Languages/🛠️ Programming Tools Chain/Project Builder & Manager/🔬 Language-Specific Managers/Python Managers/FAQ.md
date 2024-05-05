# FAQ

[TOC]



## 👉 Accessing anaconda channels from mamba
#mamba

Otherwise, one can switch to using Anaconda packages by adding the `anaconda` channel, as in [this answer](https://stackoverflow.com/a/68991641/570918). Just be aware that [channel mixing can be messy](https://conda-forge.org/docs/user/tipsandtricks.html#using-multiple-channels). Personally, I would just stick to Conda Forge.



[Accessing Anaconda Channels from Mamba]: https://stackoverflow.com/questions/73627956/accessing-anaconda-channels-from-mamba



## 👉 Diff between  anaconda、conda、pip、and virtualenv
#conda #pip #virtualenv #anaconda

+ **anaconda** is a release version of python. it contains any thing you need to run a python proj. and even more.
+ **conda** per se is a package manager. it can help download packages & manage/switch the environment user currently running.  
+ **pip** is simply a downloader inherently built in python.
+ **virtualenv** is simply a env-manager. it help switch through different envs user already has.

> conda ≈ pip（python包管理） + virtualenv（虚拟环境） + 非python依赖包管理
>
> 级别不一样conda和yum比较类似，可以安装很多库，不限于Python。conda是创建一个局部的环境，并安装相应包；pip是安装包到原有的环境中。
>
> pip install会检查一些依赖包并给你安装，而conda的这种检查更多，甚至会把你已有的卸了替换成他认为合适的...反正conda我只是拿来管理，安装一直是pip install...conda install真心不太喜欢乱检测乱适配....
>
> pip和conda默认源也不一样。conda有很多第三方库，pip是python官方发布库。


[What is the difference between pip and conda?]: https://stackoverflow.com/questions/20994716/what-is-the-difference-between-pip-and-conda
[Anaconda介绍、安装及使用教程]: https://www.jianshu.com/p/62f155eb6ac5
[conda install和pip install区别]: https://www.cnblogs.com/Li-JT/p/14024034.html



## 👉 To mannually update anaconda...
#anaconda 

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



## 👉 Installing non-conda packages
#anaconda #conda 

If a package is not available from conda or Anaconda.org, you may be able to find and install the package via conda-forge or with another package manager like **pip**.

**Pip** packages do not have all the features of conda packages and we recommend first trying to install any package with conda. If the package is unavailable through conda, try finding and installing it with [conda-forge](https://conda-forge.org/search.html).

If you still cannot install the package, you can try installing it with **pip**. The differences between pip and conda packages cause certain unavoidable limits in compatibility but conda works hard to be as compatible with pip as possible.

**To install a non-conda package**

1. Activate the environment where you want to put the program:
   - On Windows, in your Anaconda Prompt, run `activate myenv`.
   - On macOS and Linux, in your terminal window, run `conda activate myenv`.
2. To use **pip** to install a program such as See, in your terminal window or an Anaconda Prompt, run:
   ```
   pip install see
   ```

3. To verify the package was installed, in your terminal window or an Anaconda Prompt, run:
   ```
   conda list
   ```

   If the package is not shown, install **pip** as described in [Using pip in an environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#pip-in-env) and try these commands again.



[Managing packages]: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html?highlight=pip#id5



## 👉 Uninstall anaconda distribution
#anaconda 

When uninstalling Anaconda, you have two options: a full uninstall or a simple remove. A simple remove is fine for most users. full uninstall removes every file related to anaconda, while simple uninstall removes ONLY the anaconda software. 

**simple uninstall**
```shell
# The following are a few examples of how you may need to delete your Anaconda folder
rm -rf anaconda3
rm -rf ~/anaconda3
rm -rf ~/opt/anaconda3
```

🔗 See specific steps on https://docs.anaconda.com/anaconda/install/uninstall/

also other ways :
[conda: remove all installed packages from base/root environment](https://stackoverflow.com/questions/52830307/conda-remove-all-installed-packages-from-base-root-environment) 

```shell
# Not generally recommended!
conda install --revision 0
```



## 👉 anaconda export environment
#anaconda 

```shell
conda env export | grep -v "^prefix: " > environment.yml
## or
conda env export > environment.yml
```

Either way, the other user then runs:
```shell
conda env create -f environment.yml
```


[Anaconda export Environment file]: https://stackoverflow.com/questions/41274007/anaconda-export-environment-file
[Creating an environment from an environment.yml file]: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#id2



## 👉 Difference between `--find-links`, `--index-url`,  `extra-index-url` ?
#pip 


> I pasted the answer from stack overflow below but i still don't get where the difference is. 
>
> now i just use `extra-url-index` to refer to additional pip repo.
>
> ```shell
> [global]
> timeout = 60
> index-url = https://pypi.org/simple
> 
> [freeze]
> timeout = 10
> 
> [install]
> extra-index-url =
>     http://mirrors.aliyun.com/pypi/simple/
>     https://pypi.mirrors.ustc.edu.cn/simple/
>     http://pypi.douban.com/simple/
>     https://pypi.tuna.tsinghua.edu.cn/simple/
>     http://pypi.mirrors.ustc.edu.cn/simple/
> 
> trusted-host =
>     mirrors.aliyun.com/pypi/simple/
>     pypi.mirrors.ustc.edu.cn/simple/
>     pypi.douban.com/simple/
>     pypi.tuna.tsinghua.edu.cn/simple/
>     pypi.mirrors.ustc.edu.cn/simple/
> 
> ```


`index-url` can be considered a page with nothing but packages on it. You're telling pip to find what you want to install on that page; and that page is in a predictable format as per PEP 503. The index will only list packages it has available.

`find-links` is an array of locations to look for certain packages. You can pass it file paths, individual URLs to TAR or WHEEL files, HTML files, git repositories and more.

You can combine the two, for example, if you wanted to use some packages from your local system and others from a repository online.

You can see all the different ways pip will parse "links to packages" in the [`pip/test_index.pyp`](https://github.com/pypa/pip/blob/a9d56c7734fd465d01437d61f632749a293e7805/tests/unit/test_index.py)unit tests.

Check these examples below on official documentation of `pip install`, example [9. Install from alternative package repositories](https://pip.pypa.io/en/stable/reference/pip_install/#examples) > `Install from a local flat directory containing archives (and don’t scan indexes):`

```shell
pip install --no-index --find-links=file:///local/dir/ SomePackage
pip install --no-index --find-links=/local/dir/ SomePackage
pip install --no-index --find-links=relative/dir/ SomePackage
```


[What's the difference between --find-links and --index-url pip flags?]: https://stackoverflow.com/questions/46651454/whats-the-difference-between-find-links-and-index-url-pip-flags
[pip install -find-links search order]: https://stackoverflow.com/questions/62929339/pip-install-find-links-search-order
[Can pip.conf specify two index-url at the same time?]: https://stackoverflow.com/questions/30889494/can-pip-conf-specify-two-index-url-at-the-same-time
[index-url extra-index-url install priority order #8606]: https://github.com/pypa/pip/issues/8606



## 👉 Meaning of `[install]`, `[global]`, and alikes in configuration file?
#pip 

Idk 🤷 

TODO



## 👉 How to create a 32 bits exclusive conda env
#conda #32-bit


#TODO 


[How to create a 32 bits exclusive conda env]: https://stackoverflow.com/questions/72973933/how-to-create-a-32-bits-exclusive-conda-env

