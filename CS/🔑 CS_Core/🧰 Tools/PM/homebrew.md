# Homebrew đģ



[TOC]



## đĢ Guides

### đĒ Intro

[į¨åēå Homebrew äŊŋį¨æå](https://sspai.com/post/56009)



#### đ Installation

1. [installing command line tools on mac](https://www.freecodecamp.org/news/install-xcode-command-line-tools/)
	
	+ đ¤ [[Proxy|using proxy]] to download form official web
	
2.  go to [homebrew](https://docs.brew.sh/Installation), run command code.
	>  FaQs:
	>  + https://www.zhihu.com/question/382533848
	>
	>  **trouble-shooting logs:**
	>
	>  +  [git clone error: RPC failed; curl 56 OpenSSL SSL_read: SSL_ERROR_SYSCALL, errno 10054](https://stackoverflow.com/questions/46232906/git-clone-error-rpc-failed-curl-56-openssl-ssl-read-ssl-error-syscall-errno) #unsolved  (but it somehow work it automatically itself?)_



#### đŽ Uninstall Pcks

Ref --> [Uninstall / remove a Homebrew package including all its dependencies](https://stackoverflow.com/questions/7323261/uninstall-remove-a-homebrew-package-including-all-its-dependencies)

```shell
brew autoremove
```



#### đŽđŊ Usage & Terms

##### 1ī¸âŖ [Taps](https://docs.brew.sh/Taps)

Taps allow homebrew manage third-party repo on host.



##### 2ī¸âŖ [formulae & casks](https://stackoverflow.com/questions/46403937/what-is-the-difference-between-brew-install-xxx-and-brew-cask-install-xxx) (diff between `brew install` & `brew cask install`)

> ref: 
> [cask, cellar, tap](https://stackoverflow.com/a/64787434/16542494)

**formulae**: the CLI software homebrew managed
**casks**: the GUI software homebrew managed
**cellar**: the folder homebrew put the downloaded file 
**tap**: a source of formulae.



### đĒŠ mirror sites

+ USTC : 
  + https://mirrors.ustc.edu.cn/help/brew.git.html?highlight=homebrew



### đ Res:

đ [Homebrew Documentation](https://docs.brew.sh/)

[Anonymous Aggregate User Behaviour Analytics](https://docs.brew.sh/Analytics)

đĻ¯ quick guide: https://sspai.com/post/56009



## Linuxbrew

The Homebrew package manager may be used on Linux and [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/about) 2. Homebrew was formerly referred to as Linuxbrew when running on Linux or WSL. It can be installed in your home directory, in which case it does not use *sudo*. Homebrew does not use any libraries provided by your host system, except *glibc* and *gcc* if they are new enough. Homebrew can install its own current versions of *glibc* and *gcc* for older distributions of Linux.

[Features](https://docs.brew.sh/Homebrew-on-Linux#features), [installation instructions](https://docs.brew.sh/Homebrew-on-Linux#install) and [requirements](https://docs.brew.sh/Homebrew-on-Linux#requirements) are described below. Terminology (e.g. the difference between a Cellar, Tap, Cask and so forth) is [explained in the documentation](https://docs.brew.sh/Formula-Cookbook#homebrew-terminology).



## âī¸ Trouble shooting

### đafter running `brew doctor`...

```shell
Warning:Unbrewed '.pc' files were found in /usr/local/lib/pkgconfig.
If you didn't put them there on purpose they could cause problems when
building Homebrew formulae, and may need to be deleted.

Unexpected '.pc' files:
  /usr/local/lib/pkgconfig/tcl.pc
  /usr/local/lib/pkgconfig/tk.pc

Warning: Unbrewed static libraries were found in /usr/local/lib.
If you didn't put them there on purpose they could cause problems when
building Homebrew formulae, and may need to be deleted.

Unexpected static libraries:
  /usr/local/lib/libtclstub8.6.a
  /usr/local/lib/libtkstub8.6.a

Warning: Broken symlinks were found. Remove them with `brew cleanup`:
  /usr/local/bin/subl
  
```

[Solusion #1](https://apple.stackexchange.com/questions/125853/homebrew-doctor-warnings-requesting-library-deletions)

+ it says that the `.pc` file belongs to R studio(?). and the workaround is as given.



### đ update github tokens

git-hub token homepage :https://github.com/settings/tokens
to update token: https://gist.github.com/willgarcia/7347306870779bfa664e



### đ [brew ä¸čŊŊä¸­æ­](https://blog.csdn.net/lhp171302512/article/details/122810869)

for instance, when i was downloading `php@8.0` from brew: 
```shell
curl: (35) error:02FFF036:system library:func(4095):Connection reset by peer

Error: php@8.0: Failed to download resource "sqlite_bottle_manifest"
Download failed: https://ghcr.io/v2/homebrew/core/sqlite/manifests/3.38.2
```

one solution here is to download the required file manually and replace it form the brew cache folder to cheat brew to continue downloading.



### đ lingos:

![Pasted image 20211103212800](../../Assets/pics/Pasted image 20211103212800.png)

 > Ref: 



### đ  [Reset Homebrew Formula](https://stackoverflow.com/questions/9369519/reset-homebrew-formula)

The update-reset version of this command resets all formulae to be identical to the contents of their remote repositories, deleting any local changes. It is only used as a last-resort effort to fix a problem (itâs like unplugging Homebrew and plugging it back in). 

Related articles: 

1. [homebrew åŽčŖ formula įä¸ååå˛įæŦââäģĨåŽčŖ node ä¸ēäž](https://www.cnblogs.com/BlackStorm/p/homebrew-install-old-versions-take-node-for-example.html) 

2.  [Another git process seems to be running in this repository](https://stackoverflow.com/questions/38004148/another-git-process-seems-to-be-running-in-this-repository) 

   ```shell
   Another git process seems to be running in this repository, e.g.
   an editor opened by 'git commit'. Please make sure all processes
   are terminated then try again. If it still fails, a git process
   may have crashed in this repository earlier:
   remove the file manually to continue.
   ```



### đ What is "unbound" in the `brew services list`? #129

> https://github.com/Homebrew/discussions/discussions/129



### đ Error: Permission denied @ apply2files - /usr/local/lib/docker/cli-plugin

This solusion âĄī¸ [How to fix the Homebrew error `Permission denied @ apply2files`](https://flaviocopes.com/homebrew-fix-permission-denied-apply2files/) fixed my problem. Though still don't know what's going wrong.... 





