## Windows Manager

### 👉 Tmux

👍 [Tmux Tutorial](https://leimao.github.io/blog/Tmux-Tutorial/)

[How to use tmux](https://www.howtogeek.com/671422/how-to-use-tmux-on-linux-and-why-its-better-than-screen/)

[tmux-plugins](https://github.com/tmux-plugins/list) 

[tmuxcheatsheet](https://tmuxcheatsheet.com)



[Everything you need to know about tmux – Status Bar]:https://arcolinux.com/everything-you-need-to-know-about-tmux-status-bar/
[Change Between Light and Dark Themes in tmux]:https://www.seanh.cc/2021/01/02/change-between-light-and-dark-themes-in-tmux/



#### 👍 [Byobu](https://www.byobu.org)
![|400](../../../../Assets/Pics/MGBpdtIbnix14nd4M07nCMkJCSbmjXcPx2_BNY1-QDC50KbNsd2Z2PFx6uQUftxVY97dQF3hw7DwdjKsc87URHu0wXaSVHtwSG238srX2QcyaosZwf7yAVv7nA=w1280.png)

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

