## Filter & Finder

### 👉 [fzf](https://github.com/junegunn/fzf#usage)
![|400](../../../../Assets/Pics/fzf.png)



fzf is a general-purpose command-line fuzzy finder.

It's an interactive Unix filter for command-line that can be used with any list; files, command history, processes, hostnames, bookmarks, git commits, etc.


#### Pros
- Portable, no dependencies
- Blazingly fast
- The most comprehensive feature set
- Flexible layout
- Batteries included
  - Vim/Neovim plugin, key bindings, and fuzzy auto-completion



🔗 [fzf basic usage](https://github.com/junegunn/fzf#usage)

🔗 [Advanced fzf examples](https://github.com/junegunn/fzf/blob/master/ADVANCED.md)

🔗 [fzf Related Projects](https://github.com/junegunn/fzf/wiki/Related-projects)



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
