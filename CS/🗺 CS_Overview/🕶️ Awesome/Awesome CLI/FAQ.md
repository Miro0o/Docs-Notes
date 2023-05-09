## FAQ


## 👉 [How to disable/enable mouse copy while keeping mouse scroll in tmux?](https://stackoverflow.com/questions/62544783/how-to-disable-mouse-copy-while-keeping-mouse-scroll-in-tmux)

1. set mouse mode to enable mouse scroll. 
2. Above setting disenables copy text. To copy text from buffer press `option` key.

A possible helpful tmux config :

```shell
set -g mouse on
unbind-key MouseDown2Pane
unbind-key MouseDragEnd1Pane
bind-key -n MouseDown2Pane run "tmux set-buffer \"$(xclip -o -sel primary)\"; tmux paste-buffer"
bind-key -T copy-mode MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "xclip -sel primary -i"
set -g set-clipboard external
```


[Mouse mode with tmux in iTerm2]: https://jasonmurray.org/posts/2020/tmuxdebian/



## 👉 Set Keybindings in Byobu

You're so close! You're just missing the capitalization of "R" in M-Right and "L" in M-Left.

Just add the following to `~/.byobu/keybindings.tmux`:

```
unbind -n M-Right
unbind -n M-Left
```

And then press F5 to reload your profile.


[Disable keybindings in byobu using tmux backend | AskUbuntu]: https://askubuntu.com/a/330545


you will find these lines :
```
bind-key -n M-Left previous-window
bind-key -n M-Right next-window
```

`M` is for _Meta_, aka the _ALT key_. Example. Change the lines for :
```
bind-key -n C-Left previous-window
bind-key -n C-Right next-window
```

`C` for _Ctrl key_ (and `S` for _Shift key_).


[Modify key-bindings in Byobu]: https://stackoverflow.com/a/24250346/16542494
