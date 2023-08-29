# LSP for Vim

[TOC]



## Res




## LSP Clients/Server for VIM
### 1️⃣ vim-lsp
🏠 https://github.com/prabirshrestha/vim-lsp
🏠 https://vimawesome.com/plugin/vim-lsp

async language server protocol plugin for vim and neovim


#### vim-lsp-settings (auto configuration via vim-lsp)
🏠 https://github.com/mattn/vim-lsp-settings

Language Servers are not easy to install. Visual Studio Code provides easy ways to install and update Language Servers and Language Server Client. This plugin provides the same feature for Vim.

##### Basics Usages
While editing a file with a supported filetype:
```
:LspInstallServer
```
To uninstall server:
```
:LspUninstallServer server-name
```
Because there is no way to update a server, please run `:LspInstallServer` again, the newer version will be installed.



### 2️⃣ LanguageClient-neovim 
🏠 https://github.com/autozimu/languageclient-neovim

Features:
- Non-blocking asynchronous calls.
- [Sensible completion](https://github.com/autozimu/LanguageClient-neovim/issues/35#issuecomment-288731936). Integrated well with [deoplete](https://github.com/Shougo/deoplete.nvim) or [ncm2](https://github.com/ncm2/ncm2), or [MUcomplete](https://github.com/lifepillar/vim-mucomplete). Or simply with vim built-in `omnifunc`.
- [Realtime diagnostics/compiler/lint message.](https://github.com/autozimu/LanguageClient-neovim/issues/35#issuecomment-288732042)
- [Rename.](https://github.com/autozimu/LanguageClient-neovim/issues/35#issuecomment-288731403)
- [Hover/Get identifier info.](https://github.com/autozimu/LanguageClient-neovim/issues/35#issuecomment-288731665)
- [Goto definition.](https://github.com/autozimu/LanguageClient-neovim/issues/35#issuecomment-288731744)
- Goto reference locations.
- [Workspace/Document symbols query](https://github.com/autozimu/LanguageClient-neovim/issues/35#issuecomment-288731839).
- [Formatting](https://github.com/autozimu/LanguageClient-neovim/issues/35#issuecomment-324497559).
- [Code Action/Quick Fix](https://github.com/autozimu/LanguageClient-neovim/issues/35#issuecomment-331016526).



## LSP Color Scheme
### LSP SignColumn
Set vim SignColumn bg to NONE, or disable singcolumn

```vim
" set signcolumn=no                                                                                                                                                        hi SignColumn guibg=NONE ctermbg=NONE
```


### LSP Error & Warning Highlight
There are three elements in LSP (or vim in general?) relates to error & waring signs. They are: (warning highlight for example)

![](../../../../../../../Assets/Pics/Screenshot%202023-05-26%20at%2011.10.30%20AM.png)

To modify them, use below configurations:
```
LspErrorHighlight
LspWarningHighlight

LspErrorText
LspWarningText

LspErrorVirtualText
LspWarningVirtualText
```

[SignColumn LSP diagnostics bg set to none | Reddit]: https://www.reddit.com/r/neovim/comments/vps7ao/signcolumn_lsp_diagnostics_bg_set_to_none/

[Grey bar on left in vim? | Stackoverflow]: https://stackoverflow.com/questions/4112128/grey-bar-on-left-in-vim

[How to contol vim colors]: https://alvinalexander.com/linux/vi-vim-editor-color-scheme-syntax/

[👀 vim color names]: https://codeyarns.com/tech/2011-07-29-vim-chart-of-color-names.html#gsc.tab=0

[Can we change color scheme #41]: https://github.com/jackguo380/vim-lsp-cxx-highlight/issues/41


## Ref

