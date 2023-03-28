# Vim Customization
[TOC]



## .vimrc
[basic vimrc]: https://www.huweihuang.com/linux-notes/vim/basic-vimrc.html



## Themes & Colors
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



## Plugins
### Netrw -- vim built-in file explorer
#### links
to grasp a glance of Netrw 
👉 [Using Netrw, vim's builtin file explorer](https://vonheikemen.github.io/devlog/tools/using-netrw-vim-builtin-file-explorer/)
👉 [Using netrw instead of NERDTree for Vim](https://blog.stevenocchipinti.com/2016/12/28/using-netrw-instead-of-nerdtree-for-vim/ "Using netrw instead of NERDTree for Vim")

other useful resources (pausibaly): 
🤷‍♀️ [Vim Netrw 快捷键最全说明](https://gist.github.com/wilon/20ee2cf4aafffc2986c54c639ed6d80e)
🤷‍♀️ [how to use Netrw Directory Listing in VIM split window without exiting it when a file has been read](https://vi.stackexchange.com/questions/9287/how-to-use-netrw-directory-listing-in-vim-split-window-without-exiting-it-when-a)

#### basics
`mf` mark file ;
`mt` mark target;
`mx` | `mc` | `mm` : operation on marked file / marked target

> When you try to do something on marked files, the action only applies to the files that are listed in the current buffer.



### [Nerdtree](https://github.com/preservim/nerdtree)
#### Intro
The NERDTree is a file system explorer for the Vim editor. Using this plugin, users can visually browse complex directory hierarchies, quickly open files for reading or editing, and perform basic file system operations.

#### Getting Started
After installing NERDTree, the best way to learn it is to turn on the Quick Help. Open NERDTree with the `:NERDTree` command, and press `?` to turn on the Quick Help, which will show you all the mappings and commands available in the NERDTree. Of course, your most complete source of information is the documentation: `:help NERDTree`.


🔗 
[NERDTree - how to delete file](https://stackoverflow.com/questions/10615294/nerdtree-how-to-delete-file)


### [Solarized 8: True Colors](https://github.com/lifepillar/vim-solarized8)
This is yet another Solarized theme for Vim. It places itself half way between the original [Solarized](https://github.com/altercation/vim-colors-solarized) and the [Flattened](https://github.com/romainl/flattened) variant. It removes only *some* of the bullshit. The color palette is exactly the same as in Solarized, although some highlight groups are defined slightly differently (for instance, I have tried to avoid red on blue).

The main reason for the existence of this project is that the original Solarized theme does not define `guifg` and `guibg` in terminal Vim, making it unsuitable for versions of Vim supporting true-color (i.e., 24-bit color) terminals. Instead, this color scheme works **out of the box everywhere**. For the best experience, you need:

- Vim ≥7.4.1799, or NeoVim, with `termguicolors` set, **and**
- a terminal supporting millions of colors (but see below for workarounds)


### [vim-airline](https://github.com/vim-airline/vim-airline)
Vim-ariline is a customizable terminal status bar. Go to its github homepage for more.


### [Vim-Powerline](https://github.com/Lokaltog/vim-powerline)
> Vim-powerline has been transfered to  **[Powerline](../../../../🗺 CS_Overview/Awesome/🎩 FancyCLI.md# 👉 Powerline)** 

Akin to vim-airline, vim-powerline provides rich features&display of status. 


### [powerline-go](https://github.com/justjanne/powerline-go#version-control)
A [Powerline](https://github.com/Lokaltog/vim-powerline) like prompt for Bash, ZSH and Fish. Based on [Powerline-Shell](https://github.com/banga/powerline-shell) by @banga. Ported to golang by @justjanne.

- Shows some important details about the git/hg branch (see below)
- Changes color if the last command exited with a failure code
- If you're too deep into a directory tree, shortens the displayed path with an ellipsis
- Shows the current Python [virtualenv](http://www.virtualenv.org/) environment
- Shows the current Ruby version using [rbenv](https://github.com/rbenv/rbenv) or [rvm](https://rvm.io/)
- Shows if you are in a [nix](https://nixos.org/) shell
- It's easy to customize and extend. See below for details.


### [Vim-Plug](https://github.com/junegunn/vim-plug)
Vim-plug is a vim plugin manager. 


## Ref
