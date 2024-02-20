# Windows Console & ConPTY Based

[TOC]



## Res
### Related Topics
↗ [mintty](../📌%20Pseudo%20tty%20(pty)%20Based/mintty.md)



## Intro
> 🔗 https://silaoa.github.io/2019/2019-12-29-Cygwin系列（十）：折腾终端1.html
> 🔗 https://silaoa.github.io/2020/2020-01-13-Cygwin系列（十一）：折腾终端2.html



## Ref
[👍 Cygwin系列（十）：折腾终端1]: https://silaoa.github.io/2019/2019-12-29-Cygwin系列（十）：折腾终端1.html

- cmder是一款默认配置十分漂亮的开源终端，项目地址：[https://cmder.net](https://cmder.net/)。cmder是基于ConEmu而开发的，它分为mini版和full版，mini版基本就是一套ConEmu了，full版就是把git bash for Windows也打包在一起。
- console2、consoleZ都是基于Windows Console的开源终端，支持多标签页，是`conhost`的包装。console2项目地址 [https://sourceforge.net/projects/console](https://sourceforge.net/projects/console)，由于长久未更新，才有了分支consoleZ，后者项目地址[https://github.com/cbucher/console](https://github.com/cbucher/console)，支持连接到cmd/Power Shell、Cygwin、msys(2)，**界面与Mintty极其相似**。
- git bash for Windows是git官方给Windows平台做的git打包，可以看作是msys(2)的子集，使用的终端是Mintty，另外把整套git和少数UNIX常用命令行程序打包在一起。
- Xshell、MobaXterm均为商业产品，界面华丽，不是单纯的终端了，它们把telnet、ssh、ftp这些常用客户端程序也打包进来了，MobaXterm甚至把x server都打包进来。

[👍 Cygwin系列（十一）：折腾终端2]: https://silaoa.github.io/2020/2020-01-13-Cygwin系列（十一）：折腾终端2.html
