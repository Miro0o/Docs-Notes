# FAQ

[TOC]



## 👉 obtain absolute path of file
#shell-script #bash #zsh

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



## 👉 Shell Environment Variables | Regular Shell Variables | `env`, `set`, `export`
#bash #shell-script

```shell
#### Shell Environment Variables (valid for current shell session and subshells inherented from this shell)
$ env
$ export

# This is valid, the GREP_OPTIONS is passed to grep
$ export GREP_OPTIONS='-v'
$ grep one test.txt

# env and export are basics the same, difference is env is an shell-free
# program which means you can use it in basics every shell whereas export is specifical to bash and bash-compatibles.

# 1. we can set global variables that other programs or scripts access
# 2. we can use export to make variables available to subprocesses
# Another use case of _export_ is to configure system-wide settings


#### Regular Shell Variables (valid for current shell session)
$ set 


#### Regular Shell Variables (valid for executing shell ling)
# this is valid, the GREP_OPTIONS is passed to grep
$ GREP_OPTIONS='-v' grep one test.txt

# this is invalid, the GREP_OPTIONS only worked when it was called in its line
$ GREP_OPTIONS='-v'
$ grep one test.txt

# this is also invalid; the semicolon makes one command line executed in two times (two separate bash commands)
$ GREP_OPTIONS='-v' ; grep one test.txt
```

The difference between environment variables and regular shell variables (6.8) is that **a shell variable is local to a particular instance of the shell (such as a shell script), while environment variables are "inherited" by any program you start, including another shell**

---
**set**
The [_set_](https://www.baeldung.com/linux/set-command) command in Bash lets us **change the environment variables and options of the current shell session**. We can use it to adjust the features and behavior of the shell, as well as to show the values of [variables](https://www.baeldung.com/cs/user-vs-system-variables) and [functions](https://www.baeldung.com/linux/bash-functions).

The _set_ command has many [options](https://www.baeldung.com/linux/set-command#set-command-options) that we can use to modify various aspects of the shell, such as error handling, debugging, [expansion](https://www.baeldung.com/linux/parameter-expansion-vs-command-substitution), and [job control](https://www.baeldung.com/linux/jobs-job-control-bash). Let’s see some of the most common options:
- _-e_: exit right away if a command exits with a non-zero status
- _-u_: treat unset variables as an error
- _-x_: print commands and their arguments as they are run, mostly useful for debugging and tracing
- _-o_: set or unset one of the shell options

**export**
The [_export_](https://www.baeldung.com/linux/bash-variables-export) command is a built-in Bash command that we can **use to create [environment variables](https://www.baeldung.com/linux/sudo-manage-environment-variables#shell-environment)**. Environment variables are global variables that are accessible by all processes running in the current shell session and its child processes.

**env** & **export**
This was all done in bash.
- `export` is a bash builtin; `VAR=whatever` is bash syntax.
- `env`, on another hand, is a program in itself. When `env` is called, following things happen:
	- The command `env` gets executed as a new process
	- `env` modifies the environment, and
	- calls the command that was provided as an argument. The `env` process is replaced by the `command` process.

**In summary**
- we primarily use the `set` command to configure error handling, debugging, and script behavior within the local scope of a script or shell session. 
- On the other hand, we use the `export` command to create global environment variables that other processes or scripts running in the same session can access.


---
**Additional note on `#!/usr/bin/env`**

This is also why the idiom `#!/usr/bin/env interpreter` is used rather than `#!/usr/bin/interpreter`. `env` does not require a full path to a program, because it uses the `execvp()` function which searches through the `PATH` variable just like a shell does, and then _replaces_ itself by the command run. Thus, it can be used to find out where an interpreter (like perl or python) "sits" on the path.

It also means that by modifying the current path you can influence which python variant will be called. This makes the following possible:
```bash
echo -e '#!/usr/bin/bash\n\necho I am an evil interpreter!' > python
chmod a+x ./python
export PATH=.
python
```

instead of running Python, will result in
```bash
I am an evil interpreter!
```

---
**Common Pitfalls of Using `set` and `export`**

1. forget to quote variables
2. overwriting built-in variables
3. overusing `set` options
4. using uppercase variable names for local variables
5. forgetting to unset variables

More visit 👇


[What’s the Difference Between Bash’s _set_ and _export_?]: https://www.baeldung.com/linux/bash-set-and-export#:~:text=In%20summary%2C%20we%20primarily%20use,the%20same%20session%20can%20access

[What's the difference between set, export and env and when should I use each | Ask ubuntu]: https://askubuntu.com/a/205698



## 👉 Shell Configuration Files Loading Order
#config #shell-script 

Mac系统的环境变量，加载顺序为：  
``` shell
/etc/profile 
/etc/paths 
/etc/paths.d/
~/.bash_profile 
~/.bash_login 
~/.profile

~/.bashrc
```

/etc/profile和/etc/paths是系统级别的，系统启动就会加载，后面几个是当前用户级的环境变量。后面3个按照从前往后的顺序读取，如果/.bash_profile文件存在，则后面的几个文件就会被忽略不读了，如果/.bash_profile文件不存在，才会以此类推读取后面的文件。~/.bashrc没有上述规则，它是bash shell打开的时候载入的。
