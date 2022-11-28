# Vim

## 🤷 What is [Vim](https://www.vim.org) ?

> [Vim, emacs, nano, neovim, ed, etc..](https://medium.com/linode-cube/emacs-nano-or-vim-choose-your-terminal-based-text-editor-wisely-8f3826c92a68)

## 💨 Try Vim:

> To learn Vim basics, enter `_vimtutor_` in your terminal to access an interactive walkthrough.
> 
> 💪 When you’re ready for some advanced practice, try [VimGolf](http://www.vimgolf.com/) for exercises that encourage finding better, more efficient solutions to solve challenges.



Vim is a highly configurable text editor built to make creating and changing any kind of text very efficient. It is included as "vi" with most UNIX systems and with Apple OS X.



## 🧐Why Vim?

Check out [this article](http://www.viemu.com/a-why-vi-vim.html).



## 🥵How to Vim?

### 🧠 to learn systematically:

[Git-documentation](https://git-scm.com/doc)

[git-book](https://git-scm.com/book/en/v2) ⭐️⭐️⭐️



### 🚈 to quickly access ...

- [写给 VS Code 用户的 Vim 入坑指南](https://www.ahonn.me/blog/the-vim-guide-for-vs-code-users)
- [Learn Vim For the Last Time: A Tutorial and Primer](https://danielmiessler.com/study/vim/)
  - [get start with VimGolf](http://codenhance.com/2015/10/07/getting-started-with-vim-golf.html)
  - [VimGolf](http://vimgolf.com/) is a competitive game that improves your text editing skills. It’s a great way to kill five minutes inbetween tasks and offers the promise of some seriously obscure bragging rights.
  - If you’re completely unfamiliar with Vim, go try [this online tutorial](http://www.openvim.com/tutorial.html), or at least play [Vim Snake](http://www.vimsnake.com/) or [Vim Adventures](http://vim-adventures.com/) to get used to the basic movements. What follows will be a quick walkthrough of installing the necessary programs, creating an account, and submitting your first entry.
- [Vim-galore](https://github.com/mhinz/vim-galore)
  - language supported: en, zn, ja, pt, ru, vi
- [Vimawesome](https://vimawesome.com)  --- awesome vim plug-in from across the universe
- Learn Vim progressively
  - [简明Vim练级攻略](https://coolshell.cn/articles/5426.html)



## 🤤 Get into Vim

### 1️⃣ A go-to solusion for vim customization: [Configure iTerm2 and Vim like a Pro](https://medium.com/@jeantimex/how-to-configure-iterm2-and-vim-like-a-pro-on-macos-e303d25d5b5c)

- [Iterm2](../../Shell/iterm2.md) 
- [oh-my-zsh](../../Shell/zsh.md) 
- Powerlevel10k (The coolest theme for Zsh)
- Vim Airline (Vim status bar)
- NERDTree (A file system tree for Vim)
- FZF (fuzzy finder)



### 2️⃣ check out vim color scheme : [VIM 配色方案推荐 - 知乎用户Xw7tdG的文章 - 知乎]( https://zhuanlan.zhihu.com/p/58188561)

- [solarized_8](https://github.com/lifepillar/vim-solarized8) 
  - i like this the most probably because it's light and elegant i think (?) 🤷



### Plugins

#### Netrw -- vim built-in file explorer

#### go-to refs:

to grasp a glance of Netrw 
👉 [Using Netrw, vim's builtin file explorer](https://vonheikemen.github.io/devlog/tools/using-netrw-vim-builtin-file-explorer/)
👉 [Using netrw instead of NERDTree for Vim](https://blog.stevenocchipinti.com/2016/12/28/using-netrw-instead-of-nerdtree-for-vim/ "Using netrw instead of NERDTree for Vim")

other useful resources (pausibaly): 
🤷‍♀️ [Vim Netrw 快捷键最全说明](https://gist.github.com/wilon/20ee2cf4aafffc2986c54c639ed6d80e)
🤷‍♀️ [how to use Netrw Directory Listing in VIM split window without exiting it when a file has been read](https://vi.stackexchange.com/questions/9287/how-to-use-netrw-directory-listing-in-vim-split-window-without-exiting-it-when-a)



##### basic operations:  #unsolved

`mf` mark file ;
`mt` mark target;
`mx` | `mc` | `mm` : operation on marked file / marked target

> When you try to do something on marked files, the action only applies to the files that are listed in the current buffer.



#### [Nerdtree](https://github.com/preservim/nerdtree)

#### Brief

The NERDTree is a file system explorer for the Vim editor. Using this plugin, users can visually browse complex directory hierarchies, quickly open files for reading or editing, and perform basic file system operations.



#### Getting Started

After installing NERDTree, the best way to learn it is to turn on the Quick Help. Open NERDTree with the `:NERDTree` command, and press `?` to turn on the Quick Help, which will show you all the mappings and commands available in the NERDTree. Of course, your most complete source of information is the documentation: `:help NERDTree`.



#### Refs

[NERDTree - how to delete file](https://stackoverflow.com/questions/10615294/nerdtree-how-to-delete-file)



#### [Solarized 8: True Colors](https://github.com/lifepillar/vim-solarized8)

This is yet another Solarized theme for Vim. It places itself half way between the original [Solarized](https://github.com/altercation/vim-colors-solarized) and the [Flattened](https://github.com/romainl/flattened) variant. It removes only *some* of the bullshit. The color palette is exactly the same as in Solarized, although some highlight groups are defined slightly differently (for instance, I have tried to avoid red on blue).

The main reason for the existence of this project is that the original Solarized theme does not define `guifg` and `guibg` in terminal Vim, making it unsuitable for versions of Vim supporting true-color (i.e., 24-bit color) terminals. Instead, this color scheme works **out of the box everywhere**. For the best experience, you need:

- Vim ≥7.4.1799, or NeoVim, with `termguicolors` set, **and**
- a terminal supporting millions of colors (but see below for workarounds)



#### [vim-airline](https://github.com/vim-airline/vim-airline)

Vim-ariline is a customizable terminal status bar. Go to its github homepage for more.



#### [Vim-Powerline](https://github.com/Lokaltog/vim-powerline)

> Vim-powerline has been transfered to  **[Powerline](../../../../🗺 CS_Overview/Awesome/🎩 FancyCLI.md# 👉 Powerline)** 

Akin to vim-airline, vim-powerline provides rich features&display of status. 



#### [powerline-go](https://github.com/justjanne/powerline-go#version-control)

A [Powerline](https://github.com/Lokaltog/vim-powerline) like prompt for Bash, ZSH and Fish. Based on [Powerline-Shell](https://github.com/banga/powerline-shell) by @banga. Ported to golang by @justjanne.

- Shows some important details about the git/hg branch (see below)
- Changes color if the last command exited with a failure code
- If you're too deep into a directory tree, shortens the displayed path with an ellipsis
- Shows the current Python [virtualenv](http://www.virtualenv.org/) environment
- Shows the current Ruby version using [rbenv](https://github.com/rbenv/rbenv) or [rvm](https://rvm.io/)
- Shows if you are in a [nix](https://nixos.org/) shell
- It's easy to customize and extend. See below for details.



#### [Vim-Plug](https://github.com/junegunn/vim-plug)

Vim-plug is a vim plugin manager. 



## 🔗 Refs:

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

