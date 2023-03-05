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



## 👉 Installing non-conda packages

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

When uninstalling Anaconda, you have two options: a full uninstall or a simple remove. A simple remove is fine for most users. full uninstall removes every file related to anaconda, while simple uninstall removes ONLY the anaconda software. 

**simple uninstall**

```shell
# The following are a few examples of how you may need to delete your Anaconda folder
rm -rf anaconda3
rm -rf ~/anaconda3
rm -rf ~/opt/anaconda3
```

:link: See specific steps on https://docs.anaconda.com/anaconda/install/uninstall/

also other ways :

[conda: remove all installed packages from base/root environment](https://stackoverflow.com/questions/52830307/conda-remove-all-installed-packages-from-base-root-environment) 

```shell
# Not generally recommended!
conda install --revision 0
```



## 👉 anaconda export environment



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
