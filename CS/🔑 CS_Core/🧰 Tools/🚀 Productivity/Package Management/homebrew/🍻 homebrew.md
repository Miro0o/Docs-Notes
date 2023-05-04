# Homebrew

[TOC]



## Res
📂 [Homebrew Documentation](https://docs.brew.sh/) 

[程序员 Homebrew 使用指北](https://sspai.com/post/56009)



## 🚪 Intro
### 🍔 Installation
1. [installing command line tools on mac](https://www.freecodecamp.org/news/install-xcode-command-line-tools/)
	
	+ 🤔 [[../../../../../CyberSecurity/Network Security/Anonymous & Private Networks/Proxy/Proxy|using proxy]] to download form official web
	
2.  go to [homebrew](https://docs.brew.sh/Installation), run command code.
	>  FaQs:
	>  + https://www.zhihu.com/question/382533848
	>
	>  **trouble-shooting logs:**
	>
	>  +  [git clone error: RPC failed; curl 56 OpenSSL SSL_read: SSL_ERROR_SYSCALL, errno 10054](https://stackoverflow.com/questions/46232906/git-clone-error-rpc-failed-curl-56-openssl-ssl-read-ssl-error-syscall-errno) #unsolved  (but it somehow work it automatically itself?)_


### 🚮 Uninstall Pcks
#### `brew autoremove`
Ref --> [Uninstall / remove a Homebrew package including all its dependencies](https://stackoverflow.com/questions/7323261/uninstall-remove-a-homebrew-package-including-all-its-dependencies)

#### `brew cleanup`
By default, `homebrew` keeps copy file of already installed formulae downloads files around "*In case something goes wrong and you have to reinstall*". 

The [cleanup](https://github.com/Homebrew/brew/blob/master/docs/FAQ.md#how-do-i-uninstall-old-versions-of-a-formula) (`brew cleanup`) command will remove outdated installed package versions. To affect a particular package/formula, you may supply a formula name like so: `brew cleanup $FORMULA`. To simulate cleanup, i.e. see what would be removed, you may use the `-n` option: `brew cleanup -n`.

Add following alias in shell config file to simplify process:
```shell
alias brewski='brew update && brew upgrade && brew cleanup; brew doctor'
```

I end with `brew doctor` to make sure all packages are correctly symlinked, e.g., `awscli` seems to have a problem with this on the regular so I constantly have to unlink/relink. Hope this helps
> ⚠
>
>  `brew cleanup` dose not clean files in `~/Library/Caches/Homebrew`. 
>
> See this reason at ↗️ [FAQ](FAQ.md) 

> 👉 [从零开始，编写一个 HomeBrew 缓存清理脚本](https://sspai.com/post/65842)


🔗
[How can I remove outdated installed versions of Homebrew packages?]: https://superuser.com/questions/975701/how-can-i-remove-outdated-installed-versions-of-homebrew-packages




### 👮🏽 Usage & Terms
#### 1️⃣ [Taps](https://docs.brew.sh/Taps)
Taps allow homebrew manage third-party repo on host.


#### 2️⃣ [formulae & casks](https://stackoverflow.com/questions/46403937/what-is-the-difference-between-brew-install-xxx-and-brew-cask-install-xxx) (diff between `brew install` & `brew cask install`)
> ref: 
> [cask, cellar, tap](https://stackoverflow.com/a/64787434/16542494)

**formulae**: the CLI software homebrew managed
**casks**: the GUI software homebrew managed
**cellar**: the folder homebrew put the downloaded file 
**tap**: a source of formulae.


#### Basics
```shell
brew list
brew outdated
brew update
brew upgrade
brew autoremove
brew cleanup --prune=all --dry-run

```

<small>https://mac.install.guide/homebrew/8.html</small>



## 🪩 mirror sites
+ USTC : 
  + https://mirrors.ustc.edu.cn/help/brew.git.html?highlight=homebrew



## 🔗 Res:
📄 [Homebrew Documentation](https://docs.brew.sh/)

[Anonymous Aggregate User Behaviour Analytics](https://docs.brew.sh/Analytics)

🦯 quick guide: https://sspai.com/post/56009



