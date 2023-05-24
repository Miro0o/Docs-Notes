# Vim

[TOC]



## Res
### Vim Variants & Integration
↗ [Neovim](../Neovim/Neovim.md)
↗ [ST Package Contorl /NeoVintageous](../SublimeText/SublimeText%20Configuration/ST%20Package%20Contorl.md)


### Learn Vim
- [Missing Semester --- Vim](https://missing.csail.mit.edu/2020/editors/)
- [写给 VS Code 用户的 Vim 入坑指南](https://www.ahonn.me/blog/the-vim-guide-for-vs-code-users)
- [Learn Vim For the Last Time: A Tutorial and Primer](https://danielmiessler.com/study/vim/)
	- [get start with VimGolf](http://codenhance.com/2015/10/07/getting-started-with-vim-golf.html)
	- [VimGolf](http://vimgolf.com/) is a competitive game that improves your text editing skills. It’s a great way to kill five minutes inbetween tasks and offers the promise of some seriously obscure bragging rights.
	- If you’re completely unfamiliar with Vim, go try [this online tutorial(openvim)](http://www.openvim.com/tutorial.html), or at least play [Vim Snake](http://www.vimsnake.com/) or [Vim Adventures](http://vim-adventures.com/) to get used to the basic movements. What follows will be a quick walkthrough of installing the necessary programs, creating an account, and submitting your first entry.
- [Vim-galore](https://github.com/mhinz/vim-galore)
  - language supported: en, zn, ja, pt, ru, vi
- [Vimawesome](https://vimawesome.com)  --- awesome vim plug-in from across the universe
- Learn Vim progressively
  - [简明Vim练级攻略](https://coolshell.cn/articles/5426.html)
- Deep dive into vim
  - [Learn Vim Script the Hard Way](https://learnvimscriptthehardway.stevelosh.com/) 

Interactive Vim tutorial: [Open Vim](https://openvim.com/)
Vim quick reference from Vim help pages: [quickref.txt](https://vimhelp.org/quickref.txt.html)
List of all Vim ex (:) commands: [ex-cmd-index](https://vimhelp.org/index.txt.html#ex-cmd-index)


### 🐍 Vim Cheat Sheet
👍 https://devhints.io/vim

https://vim.rtorr.com
https://vimsheet.com


### Vim Docs
📂 [Vim Help](https://vimhelp.org)





## Overview
### 🤷 What is [Vim](https://www.vim.org) ?
Vim stands for Vi IMproved.  Most of Vim was made by Bram Moolenaar, but only through the help of many others.

> [Vim, emacs, nano, neovim, ed, etc..](https://medium.com/linode-cube/emacs-nano-or-vim-choose-your-terminal-based-text-editor-wisely-8f3826c92a68)


### 🧐 Why Vim?
Check out [this article](http://www.viemu.com/a-why-vi-vim.html).


### 💨 Try Vim
> To learn Vim basics, enter `vimtutor` in your terminal to access an interactive walkthrough.
> 
> 💪 When you’re ready for some advanced practice, try [VimGolf](http://www.vimgolf.com/) for exercises that encourage finding better, more efficient solutions to solve challenges.

Vim is a highly configurable text editor built to make creating and changing any kind of text very efficient. It is included as "vi" with most UNIX systems and with Apple OS X.

> **关于键位映射**
> 用 Vim 编辑代码的时候会频繁用到 ESC 和 CTRL 键, 但是这两个键都离 home row 很远, 可以把 CapsLock 键映射到 Esc 或者 Ctrl 键，让手更舒服一些。
>
> Windows 系统可以使用 [Powertoys](https://learn.microsoft.com/en-us/windows/powertoys/) 或者 [AutoHotkey](https://www.autohotkey.com/) 重映射键位。 
> MacOS 系统提供了重映射键位的[设置](https://vim.fandom.com/wiki/Map_caps_lock_to_escape_in_macOS)，另外也可以使用 [Karabiner-Elements](https://karabiner-elements.pqrs.org/) 重映射。
>
> 但更佳的做法是同时将 CapsLock 映射为 Ctrl 和 Esc，点按为 Esc，按住为 Ctrl。
> Windows 系统下，这个[AutoHotKey gist](https://gist.github.com/sedm0784/4443120) 实现了这个功能。 
> MacOS 可以导入[这个 karabiner rule](https://ke-complex-modifications.pqrs.org/#caps_lock_tapped_escape_held_left_control) 重映射。



## Vim Basics
Get an overview of vim basics from below:
``` shell
Get specific help:  It is possible to go directly to whatever you want help on, by giving an argument to the :help command. 

Prepend something to specify the context:  help-context


    WHAT                  PREPEND    EXAMPLE
Normal mode command                  :help x
Visual mode command         v_       :help v_u
Insert mode command         i_       :help i_<Esc>
Command-line command        :        :help :quit
Command-line editing        c_       :help c_<Del>
Vim command argument        -        :help -r
Option                      '        :help 'textwidth'
Regular expression          /        :help /[

See help-summary for more contexts and an explanation.
See notation for an explanation of the help syntax.
```

Get a quick look of vim basics from below:
``` shell
// in vim, type :help [section_name] for info list

BASIC:
quickref        Overview of the most common commands you will use
tutor           30-minute interactive course for beginners
copying         About copyrights
iccf            Helping poor children in Uganda
sponsor         Sponsor Vim development, become a registered Vim user
www             Vim on the World Wide Web
bugs            Where to send bug reports

USER MANUAL: These files explain how to accomplish an editing task.

usr_toc.txt     Table Of Contents
```


### 📚 Vim Docs
#### 1️⃣ User Manual
USER MANUAL: These files explain how to accomplish an editing task.

1. Getting started
```
usr_01.txt  About the manuals
usr_02.txt  The first steps in Vim
usr_03.txt  Moving around
usr_04.txt  Making small changes
usr_05.txt  Set your settings
usr_06.txt  Using syntax highlighting
usr_07.txt  Editing more than one file
usr_08.txt  Splitting windows
usr_09.txt  Using the GUI
usr_10.txt  Making big changes
usr_11.txt  Recovering from a crash
usr_12.txt  Clever tricks
```

2. Editing Effectively
```
usr_20.txt  Typing command-line commands quickly
usr_21.txt  Go away and come back
usr_22.txt  Finding the file to edit
usr_23.txt  Editing other files
usr_24.txt  Inserting quickly
usr_25.txt  Editing formatted text
usr_26.txt  Repeating
usr_27.txt  Search commands and patterns
usr_28.txt  Folding
usr_29.txt  Moving through programs
usr_30.txt  Editing programs
usr_31.txt  Exploiting the GUI
usr_32.txt  The undo tree
```

3. Tuning Vim
```
usr_40.txt  Make new commands
usr_41.txt  Write a Vim script
usr_42.txt  Add new menus
usr_43.txt  Using filetypes
usr_44.txt  Your own syntax highlighted
usr_45.txt  Select your language
```

4. Writing Vim scripts
```
usr_50.txt  Advanced Vim script writing
usr_51.txt  Create a plugin
usr_52.txt  Write plugins using Vim9 script
```

5. Making Vim Run
```
usr_90.txt  Installing Vim
```


#### 2️⃣ Reference Manual
REFERENCE MANUAL: These files explain every detail of Vim.

1. Basics editing
```
starting.txt    starting Vim, Vim command arguments, initialisation
editing.txt     editing and writing files
motion.txt      commands for moving around
scroll.txt      scrolling the text in the window
insert.txt      Insert and Replace mode
change.txt      deleting and replacing text
undo.txt        Undo and Redo
repeat.txt      repeating commands, Vim scripts and debugging
visual.txt      using the Visual mode (selecting a text area)
various.txt     various remaining commands
recover.txt     recovering from a crash
```

2. Advanced editing
```
cmdline.txt     Command-line editing
options.txt     description of all options
pattern.txt     regexp patterns and search commands
map.txt         key mapping and abbreviations
tagsrch.txt     tags and special searches
windows.txt     commands for using multiple windows and buffers
tabpage.txt     commands for using multiple tab pages
spell.txt       spell checking
diff.txt        working with two to eight versions of the same file
autocmd.txt     automatically executing commands on an event
eval.txt        expression evaluation, conditional commands
builtin.txt     builtin functions
userfunc.txt    defining user functions
channel.txt     Jobs, Channels, inter-process communication
fold.txt        hide (fold) ranges of lines
```

3. General subjects
```
intro.txt       general introduction to Vim; notation used in help files
help.txt        overview and quick reference (this file)
helphelp.txt    about using the help files
index.txt       alphabetical index of all commands
help-tags       all the tags you can jump to (index of tags)
howto.txt       how to do the most common editing tasks
tips.txt        various tips on using Vim
message.txt     (error) messages and explanations
quotes.txt      remarks from users of Vim
todo.txt        known problems and desired extensions
develop.txt     development of Vim
debug.txt       debugging Vim itself
uganda.txt      Vim distribution conditions and what to do with your money
```

4. Special issues
```
testing.txt     testing Vim and Vim scripts
print.txt       printing
remote.txt      using Vim as a server or client
term.txt        using different terminals and mice
terminal.txt    Terminal window support
popup.txt       popup window support
vim9.txt        using Vim9 script
```

5. Programming language support
6. Language support
7. GUI
8. Versions
9. Interfaces
```
if_cscop.txt    using Cscope with Vim
if_lua.txt      Lua interface
if_mzsch.txt    MzScheme interface
if_perl.txt     Perl interface
if_pyth.txt     Python interface
if_tcl.txt      Tcl interface
if_ole.txt      OLE automation interface for Win32
if_ruby.txt     Ruby interface
debugger.txt    Interface with a debugger
netbeans.txt    NetBeans External Editor interface
sign.txt        debugging signs
```

10. Remarks about specific systems
11. Standard plugins
```
pi_getscript.txt Downloading latest version of Vim scripts
pi_gzip.txt      Reading and writing compressed files
pi_logipat.txt   Logical operators on patterns
pi_netrw.txt     Reading and writing files over a network
pi_paren.txt     Highlight matching parens
pi_spec.txt      Filetype plugin to work with rpm spec files
pi_tar.txt       Tar file explorer
pi_vimball.txt   Create a self-installing Vim script
pi_zip.txt       Zip archive explorer
```



## 🤤 Vim Costumization
↗ [Vim Costumization](Vim%20Costumization.md)



## 🦹🏼‍♂️ Vim Advance
↗ [Vim Advance](Vim%20Advance.md)



## 🔗 Refs
- [quit Vim](https://blog.csdn.net/luo200618/article/details/52510781)
- [Vim hotkey](https://www.cnblogs.com/zlcxbb/p/6442083.html)
- [优雅地查找与替换](https://harttle.land/2016/08/08/vim-search-in-file.html#header-0)
- [复制、删除、粘贴](https://blog.csdn.net/ljx_5489464/article/details/50896080)
	- [一文搞懂复制粘贴](https://www.cnblogs.com/huahuayu/p/12235242.html)
- [how do i quit from vim ](https://stackoverflow.com/questions/11828270/how-do-i-exit-the-vim-editor)
- [Vim Cheetsheet](https://devhints.io/vim)
- [vim技巧：在不同文件buffer间切换，在多窗口跳转和改变窗口大小](https://segmentfault.com/a/1190000021070194)
- [vim 多窗口使用技巧](https://blog.51cto.com/hackedu/3404063)
- [VIM学习笔记 多标签页（Tabs） - YYQ的文章 - 知乎]( https://zhuanlan.zhihu.com/p/25946307)
- [如何用 vim 文本编辑器比较两文件](https://www.cnblogs.com/klchang/p/13441038.html) 

[👍 A Practical Guide to Learning Vim (NV on ST)]: https://zzzachzzz.github.io/blog/a-practical-guide-to-learning-vim
