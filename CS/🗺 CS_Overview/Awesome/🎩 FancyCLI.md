# FancyCLI 🥳

Check out AMAZING TOOLS maintained by the amazing ppl of the big open source community !

> :warning: This list only cover CLIs available on Mac. 
>
> :arrow_right:  For more possibly info about *CLI*
>
> -  [GNU-CLI](../../🔑 CS_Core/Computer System/OS/Linux/GNU/GNU-CLI.md) 
> - [zsh.md](../../🔑 CS_Core/Software/CLI/Shell&Emulator/zsh.md) 
> - [🏫 Missing tutorial - MIT.md](../🏫 Missing tutorial - MIT.md) 
> -  [macOS](../../🔑 CS_Core/Computer System/OS/UNIX/Appl/macOS/macOS.md) 



## Watching🥰 List

- [Top popular Zsh plugins on GitHub (2021)](https://safjan.com/top-popular-zsh-plugins-on-github-2021/)

- [GVP - Gitee Most Valuable Project](https://gitee.com/gvp)

- [unixorn](https://github.com/unixorn)/**[awesome-zsh-plugins](https://github.com/unixorn/awesome-zsh-plugins)**

- [Gitee - Trending](https://gitee.com/explore)

- [Github - Trending](https://github.com/explore)





[TOC]

## zsh-plugins

### 👉 [tig](https://github.com/jonas/tig)

Tig is an ncurses-based **text-mode interface for git**. It functions mainly as a Git repository browser, but can also assist in staging changes for commit at chunk level and act as a pager for output from various Git commands.

#### Resources

- Homepage: https://jonas.github.io/tig/
- Manual: https://jonas.github.io/tig/doc/manual.html
- Tarballs: https://github.com/jonas/tig/releases
- Git URL: git://github.com/jonas/tig.git
- Gitter: https://gitter.im/jonas/tig
- Q&A: https://stackoverflow.com/questions/tagged/tig



### 👉 [navi](https://github.com/denisidoro/navi)

navi allows you to **browse through cheatsheets** (that you may write yourself or download from maintainers) **and execute commands**. Suggested values for arguments are dynamically displayed in a list.

#### Pros

- it will spare you from knowing CLIs by heart
- it will spare you from copy-pasting output from intermediate commands
- it will make you type less
- it will teach you new one-liners

It uses [fzf](https://github.com/junegunn/fzf), [skim](https://github.com/lotabout/skim), or [Alfred](https://www.alfredapp.com/) under the hood and it can be either used as a command or as a shell widget (*à la* Ctrl-R).



### 👉 Tmux



[Everything you need to know about tmux – Status Bar]:https://arcolinux.com/everything-you-need-to-know-about-tmux-status-bar/
[Change Between Light and Dark Themes in tmux]:https://www.seanh.cc/2021/01/02/change-between-light-and-dark-themes-in-tmux/



#### 👍 [tmuxinator](https://github.com/tmuxinator/tmuxinator)

tmuxinator is a **tmux sessions manager**. 

```shell
tmuxinator new <project>
tmuxinator edit <project>
tmuxinator start <project>
tmuxinator stop <project>
tmuxinator list
```



#### 👍 [tmux-config](https://github.com/samoshkin/tmux-config#installation)

Along with tmuxinator, tmux-config is a re-configured tmux with some fansy features.

To install tmux-config:

```shell
git clone https://github.com/samoshkin/tmux-config.git
./tmux-config/install.sh
```

The `install.sh` script does following:

- copies files to `~/.tmux` directory
- symlink tmux config file at `~/.tmux.conf`, existing `~/.tmux.conf` will be backed up
- [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) will be installed at default location `~/.tmux/plugins/tpm`, unless already presemt
- required tmux plugins will be installed

**bug fix**

The original config aims at tmux v2. With new tmux v3 some are off.

Edit `~/.tmux.conf` and add '\\' before everywhere reported error.



### 👉 [nnn](https://github.com/jarun/nnn)

`nnn` (*n³*) is a full-featured **terminal file manager**. It's tiny, nearly 0-config and [incredibly fast](https://github.com/jarun/nnn/wiki/Performance).

It is designed to be unobtrusive with smart workflows to match the trains of thought.

`nnn` can analyze disk usage, batch rename, launch apps and pick files. The plugin repository has tons of plugins to extend the capabilities further e.g. [live previews](https://github.com/jarun/nnn/wiki/Live-previews), (un)mount disks, find & list, file/dir diff, upload files. A [patch framework](https://github.com/jarun/nnn/tree/master/patches) hosts sizable user-submitted patches which are subjective in nature.

Independent (neo)vim plugins - [nnn.vim](https://github.com/mcchrish/nnn.vim), [vim-floaterm nnn wrapper](https://github.com/voldikss/vim-floaterm#nnn) and [nnn.nvim](https://github.com/luukvbaal/nnn.nvim) (neovim exclusive).

Runs on the Pi, [Termux](https://www.youtube.com/embed/AbaauM7gUJw) (Android), Linux, macOS, BSD, Haiku, Cygwin, WSL, across DEs or a strictly CLI env.

[*(there's more)*](https://github.com/jarun/nnn/wiki/Basic-use-cases#the_nnn-magic)



👏 Hit `?` inside nnn for help. 

**Get More...**

1. [nnn plugins](https://github.com/jarun/nnn/tree/master/plugins#installation)
   1. Live Preview <https://github.com/jarun/nnn/wiki/Live-previews>



### 👉 [peco](https://github.com/peco/peco)

`peco` (pronounced *peh-koh*) is based on a python tool, [percol](https://github.com/mooz/percol). `percol` was darn useful, but I wanted a tool that was a single binary, and forget about python. `peco` is written in Go, and therefore you can just grab [the binary releases](https://github.com/peco/peco/releases) and drop it in your `$PATH`.

`peco` can be **a great tool to filter stuff** like logs, process stats, find files, because unlike grep, you can type as you think and look through the current results.

For basic usage, continue down below. For more cool elaborate usage samples, 📂 [please see the wiki](https://github.com/peco/peco/wiki/Sample-Usage), and if you have any other tricks you want to share, please add to it!

#### Config

`peco` by default consults a few locations for the config files.

1. Location specified in --rcfile. If this doesn't exist, peco complains and exits
2. $XDG_CONFIG_HOME/peco/config.json
3. $HOME/.config/peco/config.json
4. for each directory listed in \$XDG_CONFIG_DIRS, \$DIR/peco/config.json
5. If all else fails, $HOME/.peco/config.json



Mine is in ~/config/peco/config.json:

```json
{
        "Prompt": "🎮  Type in your query >>> ",
        "InitialFilter": "Fuzzy",
        "Use256Color": true,
        "Style": {
                "Basic": ["on_default", "default"],
                "SavedSelection": ["bold", "on_yellow", "white"],
                "Selected": ["underline", "on_cyan", "black"],
                "Query": ["yellow", "bold"],
                "Matched": ["black", "on_cyan"]
        }
}
```





### 👉 [tldr](https://tldr.sh)

The tldr pages are a community effort to simplify the beloved [man pages](https://en.wikipedia.org/wiki/Man_page) with practical examples.

For more go to :arrow_right: [wiki](https://github.com/tldr-pages/tldr/wiki/tldr-pages-clients)

![tldr screenshot](../../../Assets/Pics/screenshot.png)

<small>tldr demo</small>



### 👉 Powerline

📂 [Powerline Docs](https://powerline.readthedocs.io/en/latest/usage.html)



### 👉 [BAT](https://github.com/sharkdp/bat#configuration-file)

BAT is a substitude of `cat`. It supports loads of text highlighting, git Integratedtion, auto-paging ... and so on many fansy functiones. 

BAT can also be integrated with other tools. 

BAT is configured by configure file. The location of configure file is as `bat --config-file` shows. 

```shell
# an example of configure file look. 
# Set the theme to "TwoDark"
--theme="TwoDark"

# Show line numbers, Git modifications and file header (but no grid)
--style="numbers,changes,header"

# Use italic text on the terminal (not supported on all terminals)
--italic-text=always

# Use C++ syntax for Arduino .ino files
--map-syntax "*.ino:C++"
```

For further detail, check through its official docs. 



### 👉 [Lynx](https://lynx.browser.org)

[Lynx colours? How can I do that?](https://www.linuxquestions.org/questions/linux-general-1/lynx-colours-how-can-i-do-that-582681/)





## FAQ

### 👉 [How to disable/enable mouse copy while keeping mouse scroll in tmux?](https://stackoverflow.com/questions/62544783/how-to-disable-mouse-copy-while-keeping-mouse-scroll-in-tmux)

1. set mouse mode to enable mouse scroll. 
2. Above setting disenables copy text. To copy text from buffer press `option` key.

A possible helpful tmux config :

```shell
set -g mouse on
unbind-key MouseDown2Pane
unbind-key MouseDragEnd1Pane
bind-key -n MouseDown2Pane run "tmux set-buffer \"$(xclip -o -sel primary)\"; tmux paste-buffer"
bind-key -T copy-mode MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "xclip -sel primary -i"
set -g set-clipboard external
```

Links:

[Mouse mode with tmux in iTerm2]:https://jasonmurray.org/posts/2020/tmuxdebian/