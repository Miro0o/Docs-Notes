# Pwndbg

[TOC]



## Res
🏠 https://github.com/pwndbg/pwndbg)
📂 [pwndbg docs](https://browserpwndbg.readthedocs.io/en/docs/)



## Intro
> `pwndbg` (/poʊndbæg/) is a GDB plug-in that makes debugging with GDB suck less, with a focus on features needed by low-level software developers, hardware hackers, reverse-engineers and exploit developers.
> 
> Pwndbg is a Python module that is loaded directly into GDB and provides a suite of utilities and crutches to hack around all of the cruft that is GDB and smooth out the rough edges.
> 
> Many other projects from the past (e.g., [gdbinit](https://github.com/gdbinit/Gdbinit), [PEDA](https://github.com/longld/peda)) and present (e.g. [GEF](https://github.com/hugsy/gef)) exist to fill some these gaps. Each provides an excellent experience and great features -- but they're difficult to extend (some are unmaintained, and all are a single [100KB](https://github.com/gdbinit/Gdbinit/blob/master/gdbinit), [200KB](https://github.com/longld/peda/blob/master/peda.py), or [300KB](https://github.com/hugsy/gef/blob/master/gef.py) file (respectively)).
> 
> Pwndbg exists not only to replace all of its predecessors but also to have a clean implementation that runs quickly and is resilient against all the weird corner cases that come up.


### Setup 
```shell
# 1. installation via github
git clone https://github.com/pwndbg/pwndbg
cd pwndbg 
./setup.sh
```


### Extensions
##### [splitmind](https://github.com/jerdna-regeiz/splitmind)
`splitmind` helps to set up a layout of splits to organize presented information.

Currently, only `gdb` with `pwndbg` as information provider is supported and `tmux` for splitting. It relies on the ability to ouput section of information to different tty.


### Pwntools
📂 [pwntools](https://github.com/Gallopsled/pwntools)



## Ref
[「pwn」调试：gdb+pwndbg食用指南]:https://blog.csdn.net/Breeze_CAT/article/details/103789233


