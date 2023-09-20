# FAQ

[TOC]



## 👉 Terminal(TTY, PTY, etc.) & Consoles
#terminal #TTY #PTY #console

![pty_tty_console.excalidraw|800](../../../../Assets/Ilustrations/pty_tty_console.excalidraw.md)


---
From the [Linux Kernel documentation on Kernel.org](https://www.kernel.org/doc/html/latest/admin-guide/devices.html):

``` shell
/dev/tty        # Current TTY device
/dev/console    # System console
/dev/tty0       # Current virtual console
```
In the good old days `/dev/console` was System Administrator console. And TTYs were users' serial devices attached to a server.

Now `/dev/console` and `/dev/tty0` represent current display and usually are the same. You can override it for example by adding `console=ttyS0` to `grub.conf`. After that your `/dev/tty0` is a monitor and `/dev/console` is `/dev/ttyS0`.

An exercise to show the difference between `/dev/tty` and `/dev/tty0`:

Switch to the 2nd console by pressing Ctrl+Alt+F2. Login as `root`. Type `sleep 5; echo tty0 > /dev/tty0`. Press Enter and switch to the 3rd console by pressing Alt+F3. Now switch back to the 2nd console by pressing Alt+F2. Type `sleep 5; echo tty > /dev/tty`, press Enter and switch to the 3rd console.

You can see that `tty` is the console where process starts, and `tty0` is a always current console.


[Linux: Difference between /dev/console, /dev/tty and /dev/tty0]: https://unix.stackexchange.com/questions/60641/linux-difference-between-dev-console-dev-tty-and-dev-tty0

---
### Terminals & Consoles

![](../../../../Assets/Pics/Pasted%20image%2020230920160147.png)

![](../../../../Assets/Pics/Pasted%20image%2020230920160326.png)

- console 是系统控制台，一般系统输出会走这个设备，直接与主机相连，一般只有一个
- terminal是用户远程控制台，通过通信电缆/电信网络/直连主机，可以有多个

![](../../../../Assets/Pics/Pasted%20image%2020230920160250.png)
<small>远古时期的tty架构示意图</small>

![](../../../../Assets/Pics/Pasted%20image%2020230920160256.png)
<small>现代tty架构示意图</small>

#### /dev/console
这个设备表示的是系统控制台，主要用于接收系统message的，系统消息一般不会被发送到tty上，而是发送给console设备上。现代linux系统中console是相当于一个链接，没有真正的对应的一个实体；console是被配置链接到系统中的某一个tty的（？）；当然我们也可以配置console为其他tty，这样系统消息就会被发送到对应tty终端上，通过cmdline指定console=tty0，此时/dev/console相当于是/dev/tty0的一个别名。同样我们也可以指定它为一个串口设备，通过设定console=/dev/ttyS1进行指定，此时/dev/console相当于是/dev/ttyS1的一个别名。

#### /dev/tty0
tty0表示的是**当前虚拟控制台**的一个别名，而实际的虚拟控制台是tty1…ttyn。  
其中tty1和tty2为X窗口系统，其余为虚拟字符终端。

#### /dev/tty
这个设备表示的是**控制终端**，如果当前的shell登录环境有关联控制终端，那么执行它就可以看到回显。  
echo test > /dev/tty  
它其实是一个当前控制终端的一个别名，实际控制终端可以是伪终端（/dev/pts/x），也可以是虚拟控制台（/dev/ttyx）。/dev/tty有些类似于到实际所使用终端设备的一个链接


[👍 Difference between /dev/console, /dev/tty, and /dev/tty0]: https://www.baeldung.com/linux/monitor-keyboard-drivers#devconsole
[如何区分tty和tty0和console设备]: https://blog.csdn.net/rikeyone/article/details/112340907

[终端、Shell、tty 和控制台（console）有什么区别？ - 蓬岸 Dr.Quest的回答 - 知乎]: https://www.zhihu.com/question/21711307/answer/118788917

[终端、Shell、tty 和控制台（console）有什么区别？ - 大川的回答 - 知乎]: https://www.zhihu.com/question/21711307/answer/2231006377


### Types of Terminals
There are fore types of Terminal:
- **Hardware terminal**, i.e., teletypewriters, hard-copy, video display unit (VDU), and others
- **Software terminal**, i.e., **virtual TeleTYpe (TTY)**, which is the main interface of a Linux operating system
- **Software pseudo-terminal**, i.e., **PseudoTeletYpe (PTY)**, which allows emulating a TTY
- **Software terminal emulator**, based on the previous ideas, but usually enhancing them via the actual or CLI-emulated GUI

Basically, both TTY & PTY are bi-directional channels, but a TTY is a main OS terminal, while PTYs can be allocated on request.

In conclusion, a PTY is very similar to a TTY but allows for more flexibility, enabling the development of convenient userland applications and protocols.


#### TTY
TTY is an acronym for _teletype_ or _teletypewriter_. In essence, **TTYs are devices that enable typing (_type_, _typewriter_) from a distance (_tele_)**.

In a modern operating system (OS), the concept applies directly. **Linux uses a [device file](https://www.baeldung.com/linux/dev-directory) to represent a virtual TTY, which enables interaction with the OS** by handling input (usually a keyboard) and output (usually a screen).

While Linux systems can have multiple TTYs, their number is usually limited by the configuration. Actually, we can change this by modifying _/etc/init/tty*.conf_, _/etc/securetty_, _/etc/systemd/logind.conf_, or similar configuration files depending on the Linux distribution.
``` shell
# list all tty
find /dev -regex '.*/tty[0-9]+'

# list all serial devices 
find /sys/class/tty/ | sort -V

# In this case, we see several other related devices:
/dev/tty
/dev/console
/dev/ttyS#
/dev/ptmx
```

Pure TTYs do allow communication, but they don’t provide much flexibility because **at least one end of the TTY is (a keyboard, mouse, or another input device via) the kernel**. On the other hand, ==a PTY can be linked to any application on both ends.==


##### `getty@.service`
Importantly, in recent Linux distributions, [_systemd_](https://www.baeldung.com/linux/differences-systemctl-service#1-sysvinit-and-systemd) spawns the _getty@.service_, which generates, provides, and monitors `/dev/tty*` devices. This way, we can use a command like the following to reset a problematic terminal:
```shell
$ systemctl restart getty@tty1.service
```

Furthermore, **device files such as _/dev/ttyS#_, _/dev/ttyUSB#_, and similar can be handled by `serial-getty@.service` and are meant to be channels for communication with COM, USB, and other devices**.


#### PTY
PTY is an acronym for _pseudo-TTY_. **The name _PTY_ stems from the fact that it behaves like a TTY but for any two endpoints**. This minor difference enables multiple PTYs to co-exist within the context of the same TTY.

In fact, both sides of a PTY have a name:
- **slave**, `/dev/pts`, represented by a file in `/dev/pts/#`
- **master**, `ptm`, which only exists as a file descriptor of the process, which requests a PTY

This is where `/dev/ptmx`, the **pseudo-terminal multiplexor device**, comes in. Effectively, there are several steps to establish and use a PTY:
1. A process opens `/dev/ptmx`
2. The OS returns a master `ptm` file descriptor
3. The OS creates a corresponding `/dev/pts/#` slave pseudo-device
4. From this point, slave input goes to the master, while master input goes to the slave

To know the correspondence between a master and slave, we can call the [_ptsname_](https://pubs.opengroup.org/onlinepubs/009695399/functions/ptsname.html) function.

Basically, **a PTY enables bi-directional communication similar to pipes**. Unlike pipes, it provides a terminal interface to any process that requires it.

##### PTY Applications
↗ [Awesome Windows Manager](../../../🗺%20CS_Overview/🕶️%20Awesome%20List/📌%20Awesome%20General%20CLI%20Software%20List/Awesome%20Windows%20Manager.md)


#### Terminal Emulator
In essence, **a terminal emulator requests as many PTYs as it needs from the OS**, often presenting them as tabs or windows in the GUI. Let’s follow how that works and how it links to the concepts of TTY and PTY.

First, Linux boots into a TTY. We can confirm this and the current terminal backend in general via the [_tty_](https://man7.org/linux/man-pages/man1/tty.1.html)command:
```shell
$ tty
/dev/tty1
```

In this case, we’re on _/dev/tty1_, commonly the first TTY, used for login and the GUI. In fact, we can usually start the [X Window System](https://www.x.org/releases/current/doc/man/man7/X.7.xhtml) with [_startx_](https://www.x.org/releases/X11R7.6/doc/man/man1/startx.1.xhtml). Now, we have a GUI running on _/dev/tty1_.

From there, we can open any terminal emulator application and check its terminal:
```shell
$ tty
/dev/pts/0
```

The output shows we’re in the first pseudo-TTY slave.

In fact, we can even skip the GUI step, as there are terminal emulators in the CLI.



[👍 What do PTY and TTY Mean?]: https://www.baeldung.com/linux/pty-vs-tty

[Perplexity about TTY and PTY | Stack Exchange]: https://unix.stackexchange.com/questions/673184/perplexity-about-tty-and-pty

[👍 Terminal under the hood - TTY & PTY]: https://yakout.io/blog/terminal-under-the-hood/
[👍 What do pty and tty mean? | Stackoverflow]: https://stackoverflow.com/questions/4426280/what-do-pty-and-tty-mean

[Linux: Difference Between /dev/tty, /dev/tty0, and /dev/console]: https://www.tecmint.com/linux-tty-tty0-and-console/


## 👉 Obtain Absolute Path of File
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
