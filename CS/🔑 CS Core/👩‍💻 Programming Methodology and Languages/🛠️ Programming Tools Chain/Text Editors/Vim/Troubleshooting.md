# Troubleshooting

[TOC]



## Res


## 👉 Vi/Vim – Backspace Not Working
🔗 https://www.shellhacks.com/vi-vim-backspace-not-working/

If you try to delete characters in the insert mode with the `backspace` key in `vi`/`vim`text editor, this sometimes may not work.

Even though this is not a bug but a _feature_ of `vi`/`vim`, you may still want to fix a backspace that is “not working”.

In this small note i will show how to fix “not working” `backspace` key in the insert mode in `vi`/`vim`.

Fix:
`:set backspace=indent,eol,start`



## 👉 Popup-menu Color & Signcolum Color (?)
My color is like this: 

![|450](../../../../../../Assets/Pics/Screenshot%202023-05-09%20at%209.24.33%20AM.png)

which is really ugly!

#TODO 


🔗 https://vi.stackexchange.com/a/12665

You can use the following highlight groups:
- `Pmenu` – normal item
- `PmenuSel` – selected item
- `PmenuSbar` – scrollbar
- `PmenuThumb` – thumb of the scrollbar

For example to set a grey background:
```
:highlight Pmenu ctermbg=gray guibg=gray
```
For Gvim you only need the `guibg` part (`ctermbg` is used when Vim is run in a terminal), but I find it useful to always define both.


UPDATE:
I didn't know this either; I used `:help i_ctrl-x` to find the help page for that key, then followed the `ins-completion` link mentioned in the entry, and searched for highlight with `/highlight` ;-)

Another way to find this information would have been to use `:help highlight-groups`, which lists all default highlight groups.

---

🔗 https://github.com/dracula/vim/issues/14

I just did the same thing, but follow the original dracula theme from PhpStorm, here comes with my customization:

```shell
hi Pmenu ctermfg=NONE ctermbg=236 cterm=NONE guifg=NONE guibg=#64666d gui=NONE
hi PmenuSel ctermfg=NONE ctermbg=24 cterm=NONE guifg=NONE guibg=#204a87 gui=NONE
```



## 👉 macOS pre-installed Vim, Vim, macvim (Vim support for python3)
🔗 [Make Homebrew installed Vim override system installed one | StackExchange](https://apple.stackexchange.com/a/362840)
🔗 [How to upgrade system default vim? | StackExchange](https://apple.stackexchange.com/a/252436)



## 👉 YCM Server Shut Down
🔗 [Troubleshooting steps for ycmd server SHUT DOWN](https://github.com/ycm-core/YouCompleteMe/wiki/Troubleshooting-steps-for-ycmd-server-SHUT-DOWN)

**Try rebuild...**

It could be that the YCM core library needs to be rebuilt. This can happen if:

-   Your python version has changed
-   You recently upgraded your OS
-   etc.

This frequently happens on macOS after a `brew upgrade` for example.

So, first, try re-running `install.py` using your normal arguments (see README).



## Ref

