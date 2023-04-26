# Conda

[TOC]



## Res

📂 [Conda Doc](https://docs.conda.io/en/latest/)

📂 [Conda Userguide](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)

[Conda configuration](https://conda.io/projects/conda/en/latest/configuration.html#)

[Conda Glossary](https://conda.io/projects/conda/en/latest/glossary.html)

[Conda developer guide](https://conda.io/projects/conda/en/latest/dev-guide/index.html)



## Intro
>  TL;DR 
>
> Conda is a powerful package manager and environment manager that you use with command line commands at the Anaconda Prompt for Windows, or in a terminal window for macOS or Linux.

*Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, Fortran, and more.*

Conda is an open source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer. It was created for Python programs, but it can package and distribute software for any language.

Conda as a package manager helps you find and install packages. If you need a package that requires a different version of Python, you do not need to switch to a different environment manager, because conda is also an environment manager. With just a few commands, you can set up a totally separate environment to run that different version of Python, while continuing to run your usual version of Python in your normal environment.

In its default configuration, conda can install and manage the thousand packages at [repo.anaconda.com](https://repo.anaconda.com/) that are built, reviewed and maintained by **Anaconda®**.

Conda can be combined with continuous integration systems such as Travis CI and AppVeyor to provide frequent, automated testing of your code.


### Python distributions
Conda per sa is a single software issued by Anaconda® ( [formally Continuum Analytics](https://www.anaconda.com/blog/continuum-analytics-officially-becomes-anaconda) ) ; but very often it comes along with a **python distribution** which is like a distribution in linux os: it packages conda along with many other python packages into a single distribution for further use. 

There are multiple versions of distributions, differentiated by two things: the number of packages that get installed by default, and the version of defualt python it uses.

The most common two distributions are [Anaconda](Anaconda.md) and [miniconda](miniconda.md).

- [**Miniconda**](https://conda.io/miniconda.html) is a minimal installer for conda, which includes conda, Python, the packages they depend on, and a limited number of other useful packages (incl. pip, zlib, etc).  Its small base size and selectivity makes it a preferred choice for when space is a concern.

- [**Anaconda**](https://www.anaconda.com/) is the most popular **full Python distribution**. It comes with a package manager system, [conda](https://conda.io/docs/), and includes many commonly used Python modules. For this reason it occupies 3.2 GB as installed and includes hundreds of the most popular packages for large-scale data processing, predictive analytics, and scientific computing. Anacodna is more like to me for professional data scientist.

> 🔗 [Anaconda vs. miniconda](https://stackoverflow.com/questions/45421163/anaconda-vs-miniconda) 



## 🚇 conda channels
> ⚠ It is recommended to stick to a single source. 

### [Anaconda repo](https://repo.anaconda.com)
This is anaconda official repo. However it sometimes lacks of packages.

### [conda-forge](https://conda-forge.org)
[conda-forge](https://github.com/conda-forge) is a GitHub organization containing repositories of conda recipes. Thanks to some awesome continuous integration providers (AppVeyor, Azure Pipelines, CircleCI and TravisCI), each repository, also known as a feedstock, automatically builds its own recipe in a clean and repeatable way on Windows, Linux and OSX.

#### Why conda-forge?
> 🔗 [A brief introduction to conda-forge](https://conda-forge.org/docs/user/introduction.html)

The conda team, from [Anaconda, Inc.](https://anaconda.org/), packages a multitude of packages and provides them to all users free of charge in their `default` channel.

But what if a package you are looking for is not in the default channel? In the past users only had the option to create an [Anaconda Cloud](https://anaconda.org/) account and create their own channel.

**conda-forge is a community effort** that tackles these issues:
- All packages are shared in a single channel named `conda-forge`.
- Care is taken that all packages are up-to-date.
- Common standards ensure that all packages have compatible versions.
- By default, we build packages for macOS, Linux AMD64 and Windows AMD64.
- Many packages are updated by multiple maintainers with an easy option to become a maintainer.
- An active core developer team is trying to also maintain abandoned packages.


#### [Mini-forge](https://github.com/conda-forge/miniforge)
This repository holds a minimal installer for [Conda](https://conda.io/) specific to [conda-forge](https://conda-forge.org/). Miniforge allows you to install the conda package manager with the following features pre-configured:

- conda-forge set as the default (and only) channel.
  - Packages in the base environment are obtained from the [conda-forge channel](https://anaconda.org/conda-forge).
- Optional support for PyPy in place of standard Python interpreter (aka "CPython").
- Optional support for [Mamba](https://github.com/mamba-org/mamba) in place of Conda.
- An emphasis on supporting various CPU architectures (x86_64, ppc64le, and aarch64 including Apple M1).

It can be compared to the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installer.


### Mirror sources







## Ref

[conda 使用教程]: https://www.jianshu.com/p/576abf08dd76

[Anaconda Python]: https://csguide.cs.princeton.edu/conda
