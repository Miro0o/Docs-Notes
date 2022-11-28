# Reverse Engineering & Binary Exploitation



Reverse Engineering in a CTF is typically the process of taking a compiled (machine code, bytecode) program and converting it back into a more human readable format.

Very often the goal of a reverse engineering challenge is to understand the functionality of a given program such that you can identify deeper issues.



[TOC]



## Resource

[Malicious Coda Analysis](../../../🏠 Assets/CMU/Malicious Code Analysis/Intro.md) 

[二进制安全学习笔记](https://binhack.readthedocs.io/zh/latest/index.html)



## 🤿 RE



## 💭 Pwn

1. pwntools
2. shellcode
3. GDB (OD, LLDB)
   1. Peda
   2. qira
   3. pwngdb



[Mac 环境下 PWN入门系列（一）]:https://www.anquanke.com/post/id/187922#h3-5



### 🎯 Dummy

[Vulhub -- 使用Vulhub一键搭建漏洞测试靶场](https://vulhub.org/#/docs/docker-accelerator/)

[DVWA](https://github.com/digininja/DVWA)

- [DVWA 题解博客](https://www.cnblogs.com/wayne-tao/tag/DVWA/)



### 🐞 Debugger

GDB & LLDB are two popullar debuggers. 

#### 🌈 UI extensive for DBG

**For gdb**

1. gdb-dashboard
2. gef
3. Pwndbg
   1. 📂[Docs](https://github.com/pwndbg/pwndbg/blob/dev/FEATURES.md)
4. radare2
5. gdbinit



**For lldb**

1. [voltron](https://github.com/snare/voltron)
2. [Lldbinit](https://github.com/gdbinit/lldbinit) 
   1. [lldbinit - Improving LLDB](https://reverse.put.as/2018/01/15/lldbinit-improving-lldb/)
3. [chisel](https://github.com/facebook/chisel) 



[gdb 的配置、插件plugin与多彩显示]:https://www.cnblogs.com/welhzh/p/13958736.html



#### Pwndbg (Mainstream)

📂 [pwndbg docs](https://browserpwndbg.readthedocs.io/en/docs/)



**[splitmind](https://github.com/jerdna-regeiz/splitmind)**

`splitmind` helps to setup a layout of splits to organize presented information.

Currently only `gdb` with `pwndbg` as information provider is supported and `tmux` for splitting. It relies on the ability to ouput section of information to different tty.



**Readings**

[「pwn」调试：gdb+pwndbg食用指南]:https://blog.csdn.net/Breeze_CAT/article/details/103789233



### Pwntools

📂 [pwntools](https://github.com/Gallopsled/pwntools)



## 🤓 Extensive Readings

[浅析虚拟机逃逸漏洞]:https://www.freebuf.com/column/197651.html
[虚拟机逃逸入门（一）]:https://forum.butian.net/share/1666

[MacOS安装IDA Pro 7.0 Crack]: https://ylcao.top/2022/01/09/macos安装ida-pro-7-0-crack全过程/

[Reverse engineering and malware analysis tools]: https://resources.infosecinstitute.com/topic/reverse-engineering-and-malware-analysis-tools/

- Hopper
- X64dbg
- Hiew
- ODA
- Binary Ninja
- Ghidra
- [radare2](https://github.com/radareorg/radare2) 

[PE 文件格式](https://zhuanlan.kanxue.com/article-10602.htm)

