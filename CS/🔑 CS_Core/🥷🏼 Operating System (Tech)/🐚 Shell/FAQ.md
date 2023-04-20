# FAQ

[TOC]



## 👉 obtain absolute path of file
使用终端需要获取文件绝对路径进行操作，如`scp`
使用`pwd`只能获取当前文件夹路径不够方便

**方案**
使用`realpath`
```bash
$ realpath example.txt
/home/username/example.txt
```

如果没有安装`realpath`也可以自己临时写平替
```bash
function realpath { echo $(cd $(dirname $1); pwd)/$(basename $1); }
```

**扩展**
使用`readlink`读取符号链接
```bash
$ readlink -e libopendds_wrapper.so
/home/username/target/lib/libopendds_wrapper.so.0.4.0
```

**ref**
[shell获取文件绝对路径]: https://www.cnblogs.com/azureology/p/14928468.html
[How to obtain the absolute path of a file via Shell (BASH/ZSH/SH)? - Stack Overflow]: https://stackoverflow.com/questions/3915040/how-to-obtain-the-absolute-path-of-a-file-via-shell-bash-zsh-sh



## 👉 Shell Environment Variables 🆚 Regular Shell Variables
```shell
#### Shell Environment Variables
$ env 

#### Regular Shell Variables
$ set
```

The difference between environment variables and regular shell variables (6.8) is that **a shell variable is local to a particular instance of the shell (such as a shell script), while environment variables are "inherited" by any program you start, including another shell**

