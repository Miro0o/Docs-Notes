# Languages Debuggers

[TOC]



## Res
↗ [Reverse Engineering](../../../CyberSecurity/🥇%20Best%20Practice/Reverse%20Engineering/Reverse%20Engineering.md)


## gdb

> Original ↗ [gdb](GCC/gdb/gdb.md) or enhanced gdb below 😃

### 🌈 UI extensive for gdb

1. gdb-dashboard
2. gef
3. Pwndbg
   1. 📂 [Docs](https://github.com/pwndbg/pwndbg/blob/dev/FEATURES.md)
4. radare2
5. gdbinit
6. Voltron


### [Pwndbg](https://github.com/pwndbg/pwndbg)

📂 [pwndbg docs](https://browserpwndbg.readthedocs.io/en/docs/)

> `pwndbg` (/poʊndbæg/) is a GDB plug-in that makes debugging with GDB suck less, with a focus on features needed by low-level software developers, hardware hackers, reverse-engineers and exploit developers.
> 
> Pwndbg is a Python module which is loaded directly into GDB, and provides a suite of utilities and crutches to hack around all of the cruft that is GDB and smooth out the rough edges.
> 
> Many other projects from the past (e.g., [gdbinit](https://github.com/gdbinit/Gdbinit), [PEDA](https://github.com/longld/peda)) and present (e.g. [GEF](https://github.com/hugsy/gef)) exist to fill some these gaps. Each provides an excellent experience and great features -- but they're difficult to extend (some are unmaintained, and all are a single [100KB](https://github.com/gdbinit/Gdbinit/blob/master/gdbinit), [200KB](https://github.com/longld/peda/blob/master/peda.py), or [300KB](https://github.com/hugsy/gef/blob/master/gef.py) file (respectively)).
> 
> Pwndbg exists not only to replace all of its predecessors, but also to have a clean implementation that runs quickly and is resilient against all the weird corner cases that come up.


#### Setup 
```shell
# 1. installation via github
git clone https://github.com/pwndbg/pwndbg
cd pwndbg 
./setup.sh
```

#### Extensions
##### [splitmind](https://github.com/jerdna-regeiz/splitmind)
`splitmind` helps to setup a layout of splits to organize presented information.

Currently only `gdb` with `pwndbg` as information provider is supported and `tmux` for splitting. It relies on the ability to ouput section of information to different tty.

#### Pwntools
📂 [pwntools](https://github.com/Gallopsled/pwntools)



## lldb

> Original ↗ [lldb](LLVM/lldb/lldb.md) or enhanced gdb below 😃

### 🌈 UI extensive for lldb
1. [voltron](https://github.com/snare/voltron)
2. [Lldbinit](https://github.com/gdbinit/lldbinit) 
   1. [lldbinit - Improving LLDB](https://reverse.put.as/2018/01/15/lldbinit-improving-lldb/)
3. [chisel](https://github.com/facebook/chisel) 


### [voltron](https://github.com/snare/voltron)

> Voltron is an extensible debugger UI toolkit written in Python. It aims to improve the user experience of various debuggers (LLDB, GDB, VDB and WinDbg) by enabling the attachment of utility views that can retrieve and display data from the debugger host. By running these views in other TTYs, you can build a customised debugger user interface to suit your needs.


#### Setup
```shell
# 1.1 Installation via github
git clone https://github.com/snare/voltron
cd voltron
./install.sh

# 1.2 Installation via pip
/path/to/python -m pip install voltron [ --user ]
# 1.2 source entrty.py in config file (~/.lldbinit or ~/.gdbinit)
## lldb
command script import /path/to/voltron/entry.py
## gdb
source /path/to/voltron/entry.py

```


## Other DBGs
### OllyDbg

### WinDbg

### More..
Visit ↗ [Reverse Engineering](../../../CyberSecurity/🥇%20Best%20Practice/Reverse%20Engineering/Reverse%20Engineering.md)



## Recomanded Readings
[「pwn」调试：gdb+pwndbg食用指南]:https://blog.csdn.net/Breeze_CAT/article/details/103789233
[gdb 的配置、插件plugin与多彩显示]:https://www.cnblogs.com/welhzh/p/13958736.html


## Ref
