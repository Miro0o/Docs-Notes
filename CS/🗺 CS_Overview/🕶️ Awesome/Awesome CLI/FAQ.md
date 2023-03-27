##  ⁉️ FAQ

### 👉 [How to disable/enable mouse copy while keeping mouse scroll in tmux?](https://stackoverflow.com/questions/62544783/how-to-disable-mouse-copy-while-keeping-mouse-scroll-in-tmux)

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



🔗 Links:

[Mouse mode with tmux in iTerm2]: https://jasonmurray.org/posts/2020/tmuxdebian/
