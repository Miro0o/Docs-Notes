# Process Management

[TOC]



## Res


## `exec()`



## `wait` / `waitpid`


## `fork()`


## Ref
[👍 Linux编程之exec类函数（参数详解+示例）]: https://blog.csdn.net/qq_44786250/article/details/105329417
[👍 Linux - 进程控制(进程等待)]: https://blog.csdn.net/ikun66666/article/details/129664969
[👍 C++之execlp函数用法]: https://blog.csdn.net/chengqiuming/article/details/88926460
[waitpid()函数]: https://www.cnblogs.com/wanghao-boke/p/11311806.html


[C++多线程项目 - 创建子进程]: https://blog.csdn.net/YJEthan/article/details/127194435
[C++ 快速获取文件夹(目录)下的所有文件名]: https://blog.csdn.net/Love_Point/article/details/109209154
[Linux系统 C/C++获取当前文件夹路径和文件名]: https://blog.csdn.net/qq_40250056/article/details/114832692
[C++执行shell命令]: https://blog.csdn.net/u012234115/article/details/89215980
```cpp
FILE *pp = popen("cd /xxxx && ls -l", "r"); // build pipe if (!pp) return 1;
pclose(pp);
```

```cpp
system("ps -ef| grep myprocess");
```

