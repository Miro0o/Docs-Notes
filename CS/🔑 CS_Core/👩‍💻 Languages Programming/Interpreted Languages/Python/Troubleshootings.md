# Troubleshootings

[TOC]



## 👉 Uninstall python



[Uninstall Python on Mac]: https://nektony.com/how-to/uninstall-python-on-mac



## 👉 How to force stop a python process
> 🔗 [how to force stop a python process](https://stackoverflow.com/a/53211247/16542494)

**level 1:**
`CTRL + C `  to raise  `KeyboardInterrupt`

**level 2:**
1. approach #1
`CREL + Z` to suspend the process
`jobs` to check the current suspended process
`fg %n` to resume the suspended process, where `n` is the corresponding number of the process listed by `jobs`.
`kill %n` kills the listed `n` process

2.  approach #2
`ps aux | grep python` check the PID (Process ID) of the running process
`kill <PID>` to kill the process
> `kill` command send a `SIGTERM` signal to the system by default. 

**level 3:**
if `SIGTERM`dosen't work, then send `SIGKILL` signal.
use `kill -KILL <pid>` (or `kill -9 <pid>`) to achieve this. 



## 👉 [Fix Pip “Yanked Version” Warnings](https://adamj.eu/tech/2021/09/20/how-to-fix-pip-yanked-version-warnings/)
PyPI allows package maintainers to yank a given version. This is intended for removing versions with bad faults, such as security holes or broken installation.

The maintainer *could* delete the version, but this would break all installations pinned to that version, unleashing chaos. Yanking the version instead marks the version as unsafe, making it somewhat invisible while allowing pinned installs to succeed.

Conventionally, while yanking a pck the maintainer will also relesase a secure version. Generally if one doesn't specifically designate a version when piping pcks, pip will automaticallty choose the secure version.

When Yanked Version warnning occurred, to fix it we need to find an un-yanked version of the package that will work for us. This might mean upgrading, downgrading, or waiting for a new version. Upgrading is the most common course of action, since if a maintainer has yanked a version, they’ve likely released a fix shortly after.

1️⃣ check out the package’s page on [pypi.org](https://pypi.org/).

2️⃣  check available versions with the `pip index versions` command with the package name



## 👉 ModuleNotFoundError and ImportError


[How to Fix ModuleNotFoundError and ImportError]: https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c
[Relative imports - ModuleNotFoundError: No module named x]: https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x



**TL;DR**
- Use **absolute** imports
- **Append your project’s root directory to** `PYTHONPATH` — In any environment you wish to run your Python application such as Docker, vagrant or your virtual environment i.e. in bin/activate, run (or e.g. add to `bin/activate` in case you are using virtualenv) the below command:

```
export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"
```

- *avoid using `sys.path.append("/path/to/your/project/")`



## 👉 Operator overloading

[浅析Python运算符重载](https://blog.csdn.net/goodlixueyong/article/details/52589979)



## 👉 [Difference between 'cls' and 'self' in Python classes?](https://stackoverflow.com/questions/4613000/difference-between-cls-and-self-in-python-classes)

The distinction between `"self"` and `"cls"` is defined in [`PEP 8`](http://www.python.org/dev/peps/pep-0008/#function-and-method-arguments) . As Adrien said, this is not mandatory. It's a coding style. `PEP 8` says:

> *Function and method arguments*:
>
> Always use `self` for the first argument to instance methods.
>
> Always use `cls` for the first argument to class methods.



## 👉 Assert, isinstance

[python中assert、isinstance的用法]: https://blog.csdn.net/qiqicos/article/details/78993748
[Python assert isinstance() Vector]: https://stackoverflow.com/questions/47268107/python-assert-isinstance-vector



## 👉 Start a http server using python module http.serever

 [Python_使用python快速启用HTTP服务器](https://www.cnblogs.com/testlearn/p/16072669.html) 

```shell
python -m http.server [port] [-d server-dir]
```



## 👉 Generating `requirement.txt`

```shell
$ pip freeze > requirements.txt

$ pip install pipreqs
# 在当前目录生成 
$ pipreqs . --encoding=utf8--force

```

[github.com/bndr/pipreqs](https://github.com/bndr/pipreqs)
 
 [python生成requirements.txt的两种方法 | learnku]: https://learnku.com/articles/47470
[python 项目自动生成requirements.txt文件]: https://blog.csdn.net/Irving_zhang/article/details/79087569



