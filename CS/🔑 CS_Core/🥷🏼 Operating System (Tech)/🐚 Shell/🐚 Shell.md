# Shell

[TOC]



## Res
### Lots of notes about CLI !
[🏫 Missing Semester](../../../../🗺%20CS_Overview/🏫%20Missing%20Semester.md)
[🎭 The Art of Command Line](../../../../🗺%20CS_Overview/🎭%20The%20Art%20of%20Command%20Line.md)
[🤯 Awesome](../../../../🗺%20CS_Overview/🕶️%20Awesome/🤯%20Awesome.md)
[Free Software](../Linux%20(UNIX%20Family)/🪓%20Free%20Software/Free%20Software.md)
[MacOS CLI](../Apple/MacOS%20(UNIX%20Family)/MacOS%20CLI.md)
[MacOS cmd Cheatsheet](../../../../🗺%20CS_Overview/MacOS%20cmd%20Cheatsheet.md)
[👍 Vim](../../👩‍💻%20Languages%20Programming/🐛%20Programming%20Tools%20Chain/Text%20Editors/Vim/👍%20Vim.md)


### Also Lots notes about Shell Script!
[Shel Script Basics](📝%20Shell%20Scripts/Shel%20Script%20Basics.md)



## Intro


## Shell Configuration
> 🔗 https://unix.stackexchange.com/a/3085

`~/.profile` is the right place for environment variable definitions and for non-graphical programs that you want to run when you log in (e.g. `ssh-agent`, `screen -m`). It is executed by your login shell if that is a Bourne-style shell (sh, ksh, bash). Zsh runs `~/.zprofile` instead, and Csh and tcsh run `~/.login`.

If you log in under an X display manager (xdm, gdm, kdm, ...), whether `~/.profile` is run depends on how your display manager and perhaps desktop environment were configured by your distribution. If you log in under a “custom session”, that usually executes `~/.xsession`.

`~/.bashrc` is the right place for bash-specific settings, such as aliases, functions, shell options and prompts. As the name indicates, it is specific to bash; csh has `~/.cshrc`, ksh has `~/.kshrc`, and zsh has \<drumroll\> `~/.zshrc`. 

> ❗ For shell specific configurations go to their specific docs.



🔗 See also: 
- [Difference between `.bashrc` and `.bash_profile`](https://superuser.com/questions/183870/difference-between-bashrc-and-bash-profile)
- [Which setup files should be used for setting up environment variables with bash?](https://superuser.com/questions/183845/which-setup-files-should-be-used-for-setting-up-environment-variables-with-bash)
- [Zsh not hitting `~/.profile`](https://superuser.com/questions/187639/zsh-not-hitting-profile)




## Ref

