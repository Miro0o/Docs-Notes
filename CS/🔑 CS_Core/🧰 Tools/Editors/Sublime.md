# [Sublime Text (ST)](https://www.sublimetext.com/support)



## Guides：



👉 ST 非官方文档：[ZN](https://sublime-text.readthedocs.io/en/latest/basic_concepts.html) [EN](https://sublime-text-unofficial-documentation.readthedocs.io/en/latest/index.html)

🎯 [sublimetext official docs](https://www.sublimetext.com/docs/)
[Build project on sublime](https://www.cnblogs.com/lieberdq/p/13457697.html)
[中文全教程](https://www.w3cschool.cn/sublimetext/)
[快速配置](https://blog.guowenfh.com/2015/12/26/SublimeText/)



## [Package control](https://packagecontrol.io)

sublime text package manager that makes it exceedingly simple to find, install and keep packages up-to-date.

[chinese language package install](https://blog.csdn.net/qq_35246620/article/details/78341979) #unsolved 

### hexview



### Java

Refer to [this blog](https://blog.csdn.net/hsl416604093/article/details/86645792)
... and [here](https://blog.csdn.net/Letian_Yuan/article/details/101275984) a more detailed doc. (but on win, so i just quickly checked it through)

```java
{
"cmd": ["javac \"$file_name\" && java \"$file_base_name\""], // cmd takes array, while shell_cmd takes string
"working_dir": "${project_path:${folder}}", // working directory
"file_regex": "^(...*?):([0-9]*):?([0-9]*)", // error output in regex(regular expression)
"selector": "source.java", // ST interpretor selector
"shell": true, //  idk what this is?
"encoding": "utf-8" 
}
```



### [Anaconda](../Dev_/Anaconda.md)

##### [ST(sublime text)->anaconda->python->turtle: build system](https://www.gushiciku.cn/pl/pSDw)

###### 🙋‍♀️ issue description: 
i can't use sublime text to run turtle on python, because the default run-time env on ST of python is on `bash` , and the corresponding env is NOT activated. 
###### 👌 workaround: 
👇 [==Add costumed build system==](https://blog.csdn.net/ShiAokai/article/details/83507924)
1. install ST & anaconda
2. install ST anaconda using pkg control in ST
3. modify configs of ST anaconda.
	1. default, system level (**python interpreter path**)
	2. user, individual level
	3. project, project level
4. [**new build system**](https://www.sublimetext.com/docs/build_systems.html)
	1. shell_cmd vs cmd
		1. shell_cmd & cmd designate the command pass on to shell. default shell here is `bash`  (idk 🤷 why it's not zsh or system default shell so that it is also zsh #unsolved  ). 
		2. here i use `"cmd": "python -u $file" ` for this setting. 
	
> **"cmd" : array of strings**
> 
>- The executable to run, plus any arguments to pass to it. Shell constructs such as piping and redirection are not supported ---- see [shell_cmd](https://www.sublimetext.com/docs/build_systems.html#exec_option-shell_cmd) for related info.
>- May use [variables](https://www.sublimetext.com/docs/build_systems.html#variables).
>
>e.g.
> ``` shell
> "cmd": ["my_command", "-d", "$file"],
> ```
 >---
>**"shell_cmd" : string**
>- A shell command to execute. Unlike the [cmd](https://www.sublimetext.com/docs/build_systems.html#exec_option-cmd) option, this does allow piping and redirection. Will use `bash` on Mac and Linux machine, and `cmd.exe` on Windows.
>- May use [variables](https://www.sublimetext.com/docs/build_systems.html#variables).
> 
> e.g.
>```shell
>"shell_cmd": "my_command \"$file\" | other_command", 
>```

4.	
	2.  path: 
		1.  path is the working directory. if not explicited designated, working directory is found from `$PATH` (环境变量，一般指当前用户在系统上的用户环境变量).
		2.  here in order to be in anaconda base env, i manually assigned the path to the path of my base env directory `/User/Mir0/opt/anaconda/bin`
	3.  now everytime need to change run-time env of python, just change the `path` to the corresponding directory. 🎉
5.  remove the white box && troubleshooting
	1.  https://blog.csdn.net/qq_31347869/article/details/104724952

more on config-related docs, move [here](https://sublime-text-unofficial-documentation.readthedocs.io/en/latest/reference/build_systems/configuration.html)

```shell
// my anaconda config, named 'conda_base'.

// /Users/mir0/Library/Application Support/Sublime Text/Packages/User/conda_base.sublime-build

{
  	"cmd": ["python", "-u", "$file"],						// commands 	
  	"path":"/Users/mir0/opt/anaconda3/bin",					// path to interpretor env 
  	"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",	// fetch error info form console
  	"selector": "source.python" 							// automatic selector identifier
}
```



### [SublimeREPL](https://packagecontrol.io/packages/SublimeREPL)

📌 [SublimeREPL official doc](https://sublimerepl.readthedocs.io/en/latest/)

https://www.gushiciku.cn/pl/pSDw

[Mac中如何在Sublime Text3上通过REPL插件切换不同Anconda下的Python开发环境，实现交互式代码运行、调试？p](https://blog.csdn.net/weixin_42782150/article/details/122003031)i



### PHP

prerequisite: server (appache/ tomcat/ nginx ) + php env 
ref: https://blog.csdn.net/C_ZDCSDN/article/details/112068247



### [NeoVintageous](https://github.com/NeoVintageous)/**[NeoVintageous](https://github.com/NeoVintageous/NeoVintageous)**

> [Vintage vs NeoVintageous vs SublimeSix](https://forum.sublimetext.com/t/vintage-vs-neovintageous-vs-sublimesix/41190)
>
> [vintage mode](https://www.sublimetext.com/docs/vintage.html)

NeoVintageous is an advanced Vim emulation layer for Sublime Text.

- Strong defaults
- Highly configurable
- Plugins out-of-the-box
  - Abolish
  - Commentary
  - Highlighted Yank
  - Indent Object
  - Multiple cursors
  - Surround
  - Sneak (disabled by default)
  - Targets
  - Unimpaired
- Integrations: [GitGutter](https://github.com/jisaacks/GitGutter), [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3), [Origami](https://github.com/SublimeText/Origami)
- Drop-in replacement for Vintageous



### Markdown

###### Solusion #1: 

[Sublime Text3 的 Markdown 实时预览全面总结](https://blog.csdn.net/qq_20011607/article/details/81370236)

###### Solusion #2:

[Typora Markdown App (OSX)](https://packagecontrol.io/packages/Typora%20Markdown%20App%20%28OSX%29)

open Typora inside ST2



## Tips

- [查看二进制文件 ---  Hex view 包](https://blog.coderap.com/article/183)
- [sublime 简单配置](https://segmentfault.com/a/1190000004274054)
- [简单个性定制](https://segmentfault.com/a/1190000013426306) (配置编译器，主题，snippet)
	- [更改build system 编译器路径](https://blog.csdn.net/orDream/article/details/99618643)
- [sublime snippet](https://www.freecodecamp.org/news/a-guide-to-preserving-your-wrists-with-sublime-text-snippets-7541662a53f2/)



## Q&A

##### 👉 操作系统中的Python vs Sublime Text 2内嵌的[Python](https://sublime-text.readthedocs.io/en/latest/basic_concepts.html#python-vs-sublime-text-2python "Permalink to this headline")

在 **Windows** 以及 **Linux** 平台，Sublime Text的Python解释器是完全与系统的Python解释器分离的。
而在 **OS X** 平台上，Sublime Text使用的则是系统的Python解释器。这就导致对系统Python解释器版本所做的修改，可能会对Sublime Text造成影响。比如使用MacPorts提供的解释器替换系统默认的解释器，就可能造成一些问题。
这个内嵌的解释器只是为了与插件API作交互，并不应该用来进行通用Python应用的开发。



##### 👉 [White line appears when in full-screen](https://gitlab.com/gnachman/iterm2/-/issues/9199)

Please try this build:

https://iterm2.com/adhocbuilds/iTerm2-3_4_20201227_121705-adhoc.zip

Turn on **Prefs > Advanced > Work around Big Sur bug where a white line flashes at the top of the screen in full screen mode** and then restart the app.



##### 👉 Remap hotkey on `Neovintinge`

>  [How do I remap escape when in Sublime Text vintage mode?](https://stackoverflow.com/questions/9620812/how-do-i-remap-escape-when-in-sublime-text-vintage-mode) 

1. For [Vintageous](https://github.com/guillermooo/Vintageous) plugin, use [the following key binding](https://github.com/guillermooo/Vintageous/wiki/Using-jj-instead-of-Esc):

```js
{
    "keys": ["j", "k"],
    "command": "_enter_normal_mode",
    "args": {"mode": "mode_insert"},
    "context": [{"key": "vi_insert_mode_aware"}]
}
```

2. For  `Neovintageous` you can set these options in Sublime Text preferences to remap <Esc>:

```shell
"vintageous_i_escape_jj": true

"vintageous_i_escape_jk": true
```

However neither works for me 🤷🏽‍♂️

TBD....



## [Sublime merge](https://www.sublimemerge.com)

🎯 [getting start with Sublime merge!](https://www.sublimemerge.com/docs/getting_started)

Sublime merge supports Sublime text to access to git, like github and gitbucket.



