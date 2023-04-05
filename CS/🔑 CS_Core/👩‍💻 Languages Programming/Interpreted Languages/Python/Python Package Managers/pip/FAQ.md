# FAQ

[TOC]



## 👉 Difference between `--find-links`, `--index-url`,  `extra-index-url` ?

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

Idk 🤷 

TODO