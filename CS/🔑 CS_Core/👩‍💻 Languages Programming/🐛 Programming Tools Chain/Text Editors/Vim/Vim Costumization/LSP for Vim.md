# LSP for Vim

[TOC]



## Res




## LSP Clients for VIM
### 1️⃣ vim-lsp
🏠 https://github.com/prabirshrestha/vim-lsp

async language server protocol plugin for vim and neovim


#### vim-lsp-settings
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




## Ref

