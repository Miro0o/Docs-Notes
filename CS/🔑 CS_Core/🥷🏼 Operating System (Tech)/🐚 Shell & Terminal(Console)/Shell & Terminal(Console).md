# Shell

[TOC]



## Res
### Lots of notes about CLI & Shell Commands!
↗ [🏫 Missing Semester](../../../🗺%20CS_Overview/💋%20Intro%20to%20CS/🏫%20Missing%20Semester.md)
↗ [🎭 The Art of Command Line](../../../🗺%20CS_Overview/💋%20Intro%20to%20CS/🎭%20The%20Art%20of%20Command%20Line.md)
↗ [🤯 Awesome List](../../../🗺%20CS_Overview/🕶️%20Awesome%20List/🤯%20Awesome%20List.md)
↗ [Free Software](../Linux%20(Derived%20From%20UNIX%20Family)/🪓%20Free%20Software/Free%20Software.md)
↗ [macOS CLI Software](../Apple/macOS%20(Derived%20From%20UNIX%20Family)/🪓%20macOS%20CLI%20Software/macOS%20CLI%20Software.md)
↗ [MacOS cmd Cheatsheet](../../../../🗺%20CS_Overview/MacOS%20cmd%20Cheatsheet.md)
↗ [👍 Vim](../../👩‍💻%20Programming%20Methodology%20and%20Languages/🛠️%20Programming%20Tools%20Chain/Text%20Editors/Vim/👍%20Vim.md)

🔍 https://ss64.com
Command Line Reference

### Also Lots notes about Shell Script!
↗ [Shell Implementations & Script Programming](🦞%20Shell%20Implementations%20&%20Script%20Programming/Shell%20Implementations%20&%20Script%20Programming.md)
↗ [Shell Helper](Shell%20Helper/Shell%20Helper.md)
- ↗ [Commands CheatCheet & Online Search](Shell%20Helper/Commands%20CheatSheet%20&%20Online%20Search/Commands%20CheatCheet%20&%20Online%20Search.md)
- and more!

📄 https://learnbyexample.github.io/tips/#command-line-tools
useful tips about command line tools !



## Intro
![pty_tty_console.excalidraw|800](../../../../Assets/Ilustrations/Computer%20System/pty_tty_console.excalidraw.md)

### Terminal, Console, Shell?
↗ [FAQ /👉 Terminal(TTY, PTY, etc.) & Consoles](FAQ.md#👉%20Terminal(TTY,%20PTY,%20etc.)%20&%20Consoles)




## 🍼 Shell Configuration
### Configuration File Loading
> 🔗 https://unix.stackexchange.com/a/3085

`~/.profile` is the right place for environment variable definitions and for non-graphical programs that you want to run when you log in (e.g. `ssh-agent`, `screen -m`). It is executed by your login shell if that is a Bourne-style shell (sh, ksh, bash). Zsh runs `~/.zprofile` instead, and Csh and tcsh run `~/.login`.

If you log in under an X display manager (xdm, gdm, kdm, ...), whether `~/.profile` is run depends on how your display manager and perhaps desktop environment were configured by your distribution. If you log in under a “custom session”, that usually executes `~/.xsession`.

`~/.bashrc` is the right place for bash-specific settings, such as aliases, functions, shell options and prompts. As the name indicates, it is specific to bash; csh has `~/.cshrc`, ksh has `~/.kshrc`, and zsh has \<drumroll\> `~/.zshrc`. 

> ❗ For shell specific configurations go to their specific docs.



🔗 See also: 
- [Difference between `.bashrc` and `.bash_profile`](https://superuser.com/questions/183870/difference-between-bashrc-and-bash-profile)
- [Which setup files should be used for setting up environment variables with bash?](https://superuser.com/questions/183845/which-setup-files-should-be-used-for-setting-up-environment-variables-with-bash)
- [Zsh not hitting `~/.profile`](https://superuser.com/questions/187639/zsh-not-hitting-profile)


### Default Shell
> 🔗 [Default Shell | Fish Doc](https://fishshell.com/docs/current/index.html#default-shell "Permalink to this heading")
> Applys to other shells.

There are multiple ways to switch to fish (or any other shell) as your default.

1️⃣ The simplest method is to set your terminal emulator (eg GNOME Terminal, Apple’s Terminal.app, or Konsole) to start fish directly. See its configuration and set the program to start to `/usr/local/bin/fish` (if that’s where fish is installed - substitute another location as appropriate).

2️⃣ Alternatively, you can set fish as your login shell so that it will be started by all terminal logins, including SSH.

> ⚠ Warning
> 
> Setting fish as your login shell may cause issues, such as an incorrect [`PATH`](https://fishshell.com/docs/current/language.html#envvar-PATH). Some operating systems, including a number of Linux distributions, require the login shell to be Bourne-compatible and to read configuration from `/etc/profile`. fish may not be suitable as a login shell on these systems.

To change your login shell to fish:

1.  Add the shell to `/etc/shells` with:
	```shell
	echo /usr/local/bin/fish | sudo tee -a /etc/shells
	```
1.  Change your default shell with:
	```shell
	chsh -s /usr/local/bin/fish
	```

Again, substitute the path to fish for `/usr/local/bin/fish` - see `command -s fish` inside fish. To change it back to another shell, just substitute `/usr/local/bin/fish` with `/bin/bash`, `/bin/tcsh` or `/bin/zsh` as appropriate in the steps above.



## Ref

