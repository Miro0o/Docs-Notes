# Awesome CLI 🥳

[TOC]



Check out AMAZING TOOLS maintained by the amazing ppl of the big open source family !



> :warning: This list might mainly cover CLIs available on Mac. 
>
> :arrow_right:  For more possibly info about *CLI*
>
> -  [🏫 Missing Semester](../🏫 Missing Semester.md) (THIS IS STRONGLY RECOMMANDED !!!!)
> -  [🎭 The Art of Command Line](../🎭 The Art of Command Line.md)
> -  [Linux Softwares](../../🔑 CS_Core/🥷🏼 OS/Linux/🪓 Linux Softwares/Linux Softwares.md) 
> -  [ZSH](../../🔑 CS_Core/🥷🏼 OS/🐚 Shell/ZSH.md) and many other shells and emulators and more!
> -  [MacOS cmd Cheatsheet](../MacOS cmd Cheatsheet.md) 
> -  [OS X CLI.md](../../🔑 CS_Core/🥷🏼 OS/Apple.Inc/OS X/OS X CLI.md) 
> -  [homebrew](../../🔑 CS_Core/🧰 Tools/🚀 Productivity/Package Manager/homebrew/homebrew.md) and many other packages managers !
>
> Many other field-specific CLI tools may be excluded from this list. Ther are carefully noted under each topic.



##  Watching🥰 List

- [Top popular Zsh plugins on GitHub (2021)](https://safjan.com/top-popular-zsh-plugins-on-github-2021/)

- [GVP - Gitee Most Valuable Project](https://gitee.com/gvp)

- [unixorn](https://github.com/unixorn)/**[awesome-zsh-plugins](https://github.com/unixorn/awesome-zsh-plugins)**

- [Gitee - Trending](https://gitee.com/explore)

- [Github - Trending](https://github.com/explore)

- [awesome-cli-apps](https://github.com/agarrharr/awesome-cli-apps)

- [awesome-shell](https://github.com/alebcay/awesome-shell)

- [terminals-are-sexy](https://github.com/k4m4/terminals-are-sexy) 

- [awesome-mac](https://github.com/jaywcjlove/awesome-mac)





## Network

### 👉 [httpie](https://httpie.io)

HTTPie (pronounced **aitch-tee-tee-pie**) is a command-line HTTP client. Its goal is to make CLI interaction with web services as human-friendly as possible. HTTPie is designed for testing, debugging, and generally interacting with APIs & HTTP servers. The **`http`** & **`https`** commands allow for creating and sending arbitrary HTTP requests. They use simple and natural syntax and provide formatted and colorized output.

#### [Main features](https://httpie.io/docs/cli/main-features)

- Expressive and intuitive syntax
- Formatted and colorized terminal output
- Built-in JSON support
- Forms and file uploads
- HTTPS, proxies, and authentication
- Arbitrary request data
- Custom headers
- Persistent sessions
- Wget-like downloads
- Linux, macOS, Windows, and FreeBSD support
- Plugins
- Documentation
- Test coverage

#### [Usage](https://httpie.io/docs/cli/usage)

Hello World:

```shell
$ https httpie.io/hello
```

Synopsis:

```shell
$ http [flags] [METHOD] URL [ITEM [ITEM]]
```

See also `http --help` (and for systems where man pages are available, you can use `man http`).



:link: Visit more on [Website](https://httpie.io/docs/cli/usage).



### 👉 [Serial 2](https://www.decisivetactics.com/products/serial/)

Connect to routers, servers, firewalls, industrial control and IoT devices with ease.

TODO



### 👉 [termius](https://www.termius.com)

Connect with one click from any mobile and desktop device. No re-entering IP addresses, ports, and passwords.

TODO





## Filter & Finder

### 👉 [fzf](https://github.com/junegunn/fzf#usage)

<img src="../../../Assets/Pics/fzf.png" alt="fzf - a command-line fuzzy finder" style="zoom:20%;" />



fzf is a general-purpose command-line fuzzy finder.

It's an interactive Unix filter for command-line that can be used with any list; files, command history, processes, hostnames, bookmarks, git commits, etc.

#### Pros

- Portable, no dependencies
- Blazingly fast
- The most comprehensive feature set
- Flexible layout
- Batteries included
  - Vim/Neovim plugin, key bindings, and fuzzy auto-completion



:link: [fzf basic usage](https://github.com/junegunn/fzf#usage)

:link: [Advanced fzf examples](https://github.com/junegunn/fzf/blob/master/ADVANCED.md)

:link: [fzf Related Projects](https://github.com/junegunn/fzf/wiki/Related-projects)



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



### 👉 [navi](https://github.com/denisidoro/navi)

navi allows you to **browse through cheatsheets** (that you may write yourself or download from maintainers) **and execute commands**. Suggested values for arguments are dynamically displayed in a list.

#### Pros

- it will spare you from knowing CLIs by heart
- it will spare you from copy-pasting output from intermediate commands
- it will make you type less
- it will teach you new one-liners

It uses [fzf](https://github.com/junegunn/fzf), [skim](https://github.com/lotabout/skim), or [Alfred](https://www.alfredapp.com/) under the hood and it can be either used as a command or as a shell widget (*à la* Ctrl-R).



## Visualization

### 👉 [tig](https://github.com/jonas/tig)

Tig is an ncurses-based **text-mode interface for git**. It functions mainly as a Git repository browser, but can also assist in staging changes for commit at chunk level and act as a pager for output from various Git commands.

#### Resources

- Homepage: https://jonas.github.io/tig/
- Manual: https://jonas.github.io/tig/doc/manual.html
- Tarballs: https://github.com/jonas/tig/releases
- Git URL: git://github.com/jonas/tig.git
- Gitter: https://gitter.im/jonas/tig
- Q&A: https://stackoverflow.com/questions/tagged/tig



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



### 👉 CCAT



### 👉 [mycli](https://github.com/dbcli/mycli)

TODO



### 👉 [pgcli](https://www.pgcli.com/)

TODO



## Windows Manager

### 👉 Tmux

👍 [Tmux Tutorial](https://leimao.github.io/blog/Tmux-Tutorial/)

[How to use tmux](https://www.howtogeek.com/671422/how-to-use-tmux-on-linux-and-why-its-better-than-screen/)

[tmux-plugins](https://github.com/tmux-plugins/list) 

[tmuxcheatsheet](https://tmuxcheatsheet.com)



[Everything you need to know about tmux – Status Bar]:https://arcolinux.com/everything-you-need-to-know-about-tmux-status-bar/
[Change Between Light and Dark Themes in tmux]:https://www.seanh.cc/2021/01/02/change-between-light-and-dark-themes-in-tmux/



#### 👍 [Byobu](https://www.byobu.org)

<img src="../../../../Assets/Pics/MGBpdtIbnix14nd4M07nCMkJCSbmjXcPx2_BNY1-QDC50KbNsd2Z2PFx6uQUftxVY97dQF3hw7DwdjKsc87URHu0wXaSVHtwSG238srX2QcyaosZwf7yAVv7nA=w1280.png" alt="img" style="zoom:30%;" />

Byobu is a [GPLv3](http://www.google.com/url?q=http%3A%2F%2Fwww.gnu.org%2Flicenses%2Fgpl-3.0.txt&sa=D&sntz=1&usg=AOvVaw2SdxEQNfQHLvXbZdusdaQx) open source text-based window manager and terminal multiplexer. It was originally designed to provide elegant enhancements to the otherwise functional, plain, practical [GNU Screen](http://www.google.com/url?q=http%3A%2F%2Fwww.gnu.org%2Fsoftware%2Fscreen%2F&sa=D&sntz=1&usg=AOvVaw0m279_Wo9nqZfTvhyA6pAE), for the [Ubuntu](http://www.google.com/url?q=http%3A%2F%2Fwww.ubuntu.com%2F&sa=D&sntz=1&usg=AOvVaw3el9anN507B3WIzdxf9INt) server distribution. Byobu now includes an enhanced profiles, convenient keybindings, configuration utilities, and toggle-able system status notifications for both the GNU Screen window manager and the more modern [Tmux](https://www.google.com/url?q=https%3A%2F%2Fgithub.com%2Ftmux%2Ftmux&sa=D&sntz=1&usg=AOvVaw3njEytKxDbcSOXUKtIbAzh) terminal multiplexer, and works on most Linux, BSD, and Mac distributions.



> [byobu VS tmuxinator](https://www.saashub.com/compare-byobu-vs-tmuxinator)



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



## File Manager

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



## Data Handling

### 👉 [Miller](https://miller.readthedocs.io/en/latest/)

**Miller is a command-line tool for querying, shaping, and reformatting data files in various formats including CSV, TSV, JSON, and JSON Lines.**

**The big picture:** Even well into the 21st century, our world is full of text-formatted data like CSV. Google *CSV memes*, for example. We need tooling to *thrive in this world*, nimbly manipulating data which is in CSVs. And we need tooling to *move beyond CSV*, to be able to pull data out and into other storage and processing systems. Miller is designed for both these goals.

TODO



### 👉 VisiData

VisiData is an interactive multitool for tabular data. It combines the clarity of a spreadsheet, the efficiency of the terminal, and the power of Python, into a lightweight utility which can handle millions of rows with ease.

TODO





## 💣 Experimental

### 👉 [Lynx](https://lynx.browser.org)

[Lynx colours? How can I do that?](https://www.linuxquestions.org/questions/linux-general-1/lynx-colours-how-can-i-do-that-582681/)



### 👉 [asdf](https://asdf-vm.com)

`asdf` is a tool version manager. All tool version definitions are contained within one file (`.tool-versions`) which you can check in to your project's Git repository to share with your team, ensuring everyone is using the **exact** same versions of tools.

The old way of working required multiple CLI version managers, each with their distinct API, configurations files and implementation (e.g. `$PATH` manipulation, shims, environment variables, etc...). `asdf` provides a single interface and configuration file to simplify development workflows, and can be extended to all tools and runtimes via a simple plugin interface.

> :exclamation: STRONGLY suggest follow official site's instruction.  
>
> :film_projector: [Use asdf to manage versions of Python, NodeJS, GoLang and more!](https://youtu.be/RTaqWRj-6Lg)
>
> [Introduction](https://asdf-vm.com/guide/introduction.html) 
>
> [Getting Started](https://asdf-vm.com/guide/getting-started.html)  
>
> :file_folder:  [More Detailed Docs](https://asdf-vm.com/manage/core.html)



#### Setup

1. install dependency

2. download asdf

3. install asdf

   > Add `asdf.sh` to your `~/.zshrc` with:
   >
   > ```
   > echo -e "\n. $(brew --prefix asdf)/libexec/asdf.sh" >> ${ZDOTDIR:-~}/.zshrc
   > ```
   >
   > **OR** use a ZSH Framework plugin like [asdf for oh-my-zshopen in new window](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/asdf) which will source this script and setup completions.
   >
   > Completions are configured by either a ZSH Framework `asdf` or will need to be [configured as per Homebrew's instructionsopen in new window](https://docs.brew.sh/Shell-Completion#configuring-completions-in-zsh). If you are using a ZSH Framework the associated plugin for asdf may need to be updated to use the new ZSH completions properly via `fpath`. The Oh-My-ZSH asdf plugin is yet to be updated, see [ohmyzsh/ohmyzsh#8837open in new window](https://github.com/ohmyzsh/ohmyzsh/pull/8837).

4. install plugin

5. set a version



#### Bug

I found out that `asdf` only changes the runtime version, and it doesn't do anything more like env variable mangement or dependency management like `conda` does in python. I still dont have any solid solution to this problem. 😢

For instance, i have `NODE_PATH` exported to the coresponding path when previously working on a `node` outside `asdf`. However when i enabled `asdf` to manage some new `node`s under it, the `NODE_PATH` stayed the same old path instead of chaing to the new path to the new `node`. It's bugging, right? 🤷



## 🕹️ Life /entertainment

### 👉 [cmus](https://cmus.github.io)

mus is a small, *fast* and powerful console music player for Unix-like operating systems.

TODO



### 👉 mpg123

> :link: https://www.makeuseof.com/best-command-line-music-players-linux/

mpg123 is an open-source music player for Linux. Its command-line interface makes it more efficient and gives you a seamless music player experience. Its terminal control keys allow you to use the media player with your keyboard.



## 🤣 Things might be interesting ...

TODO

[**rebound**](https://github.com/shobrook/rebound/)

Rebound is a command-line tool that **instantly fetches Stack Overflow results when an exception is thrown**. Just use the `rebound` command to execute your file.



[**Spaceship Prompt**](https://github.com/spaceship-prompt/spaceship-prompt)

Spaceship is a **minimalistic, powerful and extremely customizable [Zsh](http://zsh.org/) prompt**. Prompt is what you see when you type a command. It can show a lot of useful tips, saving your time and making user experience smooth and pleasant. It combines everything you may need for convenient work, without unnecessary complications, like a real spaceship.



[**Taskbook**](https://github.com/klaudiosinani/taskbook)

By utilizing a simple and minimal usage syntax, that requires a flat learning curve, taskbook enables you to **effectively manage your tasks and notes across multiple boards from within your terminal**. All data are written atomically to the storage in order to prevent corruptions, and are never shared with anyone or anything. Deleted items are automatically archived and can be inspected or restored at any moment.



[**TheFuck**](https://github.com/nvbn/thefuck)

the fuck is an cli auto-corrector.



##  ⁉️ FAQ

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



:link: Links:

[Mouse mode with tmux in iTerm2]:https://jasonmurray.org/posts/2020/tmuxdebian/