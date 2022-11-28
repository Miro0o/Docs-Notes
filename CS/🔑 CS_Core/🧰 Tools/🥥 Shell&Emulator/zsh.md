# ZSH

## 🌐 Overview

📖 Docs:
+ [zsh Documentation](https://zsh.sourceforge.io/Doc/)
+ [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html#index-export)

👨‍🏫  Tutorial:
+ [linux 中国](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ping)



##### Refs：

[网络测速](https://juejin.cn/post/6844904152108105742)
[zsh 变量和语句](https://kennethfan.github.io/2017/09/20/zsh-变量和语句/) #unsolved 
[更改shell 为 zsh](https://blog.csdn.net/weixin_40002692/article/details/116994108)

- ` usermod -s /bin/zsh username`
- `chsh -s /bin/zsh`



## [oh-my-zsh](https://ohmyz.sh/#install)

```shell
Looking for an existing zsh config...
Found ~/.zshrc. Backing up to /Users/mir0/.zshrc.pre-oh-my-zsh
Using the Oh My Zsh template file and adding it to ~/.zshrc.

         __                                     __
  ____  / /_     ____ ___  __  __   ____  _____/ /_
 / __ \/ __ \   / __ `__ \/ / / /  /_  / / ___/ __ \
/ /_/ / / / /  / / / / / / /_/ /    / /_(__  ) / / /
\____/_/ /_/  /_/ /_/ /_/\__, /    /___/____/_/ /_/
                        /____/                       ....is now installed!


Before you scream Oh My Zsh! look over the `.zshrc` file to select plugins, themes, and options.

• Follow us on Twitter: @ohmyzsh
• Join our Discord community: Discord server
• Get stickers, t-shirts, coffee mugs and more: Planet Argon Shop
```



### Customization

#### 🤲🏼 Self-made Script

##### opening prompt

I write this opening prompt for fun. The script is to output an artful text on the screen everytime it is activated. The script is stored in `oh-my-zsh` and is invoked in `~/.zshrc`.



How i configure this: [Colorful Banners With figlet and lolcat](https://blog.victormendonca.com/2019/03/10/colorful-banners-with-figlet-and-lolcat/)
```shell
figlet -w 170 -f ~/.local/share/figlet-fonts/Cosmike.flf 'H e l l o , W o r l d !' | lolcat -a -d 1
```
To manually write a script (plugin) under `~/.oh-my-zsh/plugin` using [Figlet](http://www.figlet.org) & [Lolcat](https://github.com/busyloop/lolcat). [Figlet Fonts](https://github.com/xero/figlet-fonts) is also needed as output fonts. Here Cosmike is chosen. 

I also made some tweaks about the parameter. I set `-w 170` as the specific output width, and `lolcat -a -d 1` to add some animation to the output text. 



#### 🎄 Theme

##### [Powerlevel10](https://github.com/romkatv/powerlevel10k/blob/master/README.md#configuration)

> [Powerlevel9](https://github.com/Powerlevel9k/powerlevel9k)
> P10k is totally compatible with P9k configuration parameter. 

How i configure Powerlevel10: [配置Powerlevel10 以及一些ohmyzsh插件](https://blog.csdn.net/hch814/article/details/108434036)
1. have iterm2 installed
2. configure Fonts need to use on iterm2 (here the author of the tutorial used [Nerd Fonts](https://www.nerdfonts.com/font-downloads), but i prefer [Powerline](https://github.com/powerline/fonts))



#### 🔌 Plugins

> [built-in plugins](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)
>
> 👍 [Top popular Zsh plugins on GitHub (2021)](https://safjan.com/top-popular-zsh-plugins-on-github-2021/)



## 🔗OutLinks

1. [oh my zsh 简单插件开发之终端启动欢迎界面](https://blog.isuoge.com/a/oh-my-zsh-jian-dan-cha-jian-kai-fa-zhi-zhong-duan-.html)
2. [Best character image generator (ASCII Art text)](https://www.reddit.com/r/rpg/comments/nzmv4c/best_character_image_generator/)
3. [on-my-zsh 完全学习手册](https://blog.csdn.net/JENREY/article/details/118600067)
4. 👍 [Top popular Zsh plugins on GitHub (2021)](https://safjan.com/top-popular-zsh-plugins-on-github-2021/)

