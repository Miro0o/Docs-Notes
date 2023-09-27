# FAQ



## 👉 How to disable/enable mouse copy while keeping mouse scroll in tmux?
#tmux


1. set mouse mode to enable mouse scroll. 
2. Above setting disenables copy text. To copy text from buffer press `option` key.

A possiblly helpful tmux config :
```shell
set -g mouse on
unbind-key MouseDown2Pane
unbind-key MouseDragEnd1Pane
bind-key -n MouseDown2Pane run "tmux set-buffer \"$(xclip -o -sel primary)\"; tmux paste-buffer"
bind-key -T copy-mode MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel "xclip -sel primary -i"
set -g set-clipboard external
```

 [How to disable/enable mouse copy while keeping mouse scroll in tmux?]: https://stackoverflow.com/questions/62544783/how-to-disable-mouse-copy-while-keeping-mouse-scroll-in-tmux
[Mouse mode with tmux in iTerm2]: https://jasonmurray.org/posts/2020/tmuxdebian/



## 👉 Tmux Splitting Windows /Resizing Panes
#tmux  


[💡 Split tmux window with same initial command in new tmux pane]: https://unix.stackexchange.com/questions/63838/split-tmux-window-with-same-initial-command-in-new-tmux-pane

[`#{pane_start_command}`](http://man.openbsd.org/OpenBSD-current/man1/tmux.1) is a way to access the command used to start the current pane. This is available since v1.7 (10/2012).

`bind-key S run-shell "tmux split-window \"#{pane_start_command}\""`  
is a solution for your question using `#{pane_start_command}`. (`tmux` version >= 1.9 (02/2014)).

With versions 1.7 >= X < 1.9 you can use something like this in your `~/tmux.conf` file:
```
bind-key S run-shell "tmux split-window \"$(tmux display-message -p '#{pane_start_command}')\""
```

- The substituted `display-message` command extracts `#{pane_start_command}`.
- That command is given as an argument to `tmux split-window`.

`pane_start_command` will be the empty string if the pane was started without a command string and there was no `default-command`, but that is okay because `split-window` will start a plain login shell if it is given an empty command string.



[💡 Tmux splitting a parent window with existing panes | SuperUser]: https://superuser.com/questions/643473/tmux-splitting-a-parent-window-with-existing-panes

Try this: `:splitw -v -f`

According to this description:

> The -f option creates a new pane spanning the full window height (with -h) or full window width (with -v), instead of splitting the active pane.

I guess it is still not as versitle as the "parent pane" design, but will solve many less complicated layouts easily.



[💡 Tmux: Switch the split style of two adjacent panes]: https://stackoverflow.com/questions/15439294/tmux-switch-the-split-style-of-two-adjacent-panes
```
#flipping the orientation of the current pane with the pane <arrow-way>-of

bind -n S-Up move-pane -h -t '.{up-of}'
bind -n S-Right move-pane -t '.{right-of}'
bind -n S-Left move-pane -t '.{left-of}'
bind -n S-down move-pane -h -t '.{down-of}'
```

here are my example to change the otiantation with the pane in the way of the arrow only Press Shift and Arrow-key or rebind the command how you want



[💡 How do I resize tmux pane by holding down prefix and arrow key for a while?]: https://superuser.com/questions/1560523/how-do-i-resize-tmux-pane-by-holding-down-prefix-and-arrow-key-for-a-while

By default these bindings (among others) are active:

```
bind-key -r -T prefix       M-Up              resize-pane -U 5
bind-key -r -T prefix       M-Down            resize-pane -D 5
bind-key -r -T prefix       M-Left            resize-pane -L 5
bind-key -r -T prefix       M-Right           resize-pane -R 5
bind-key -r -T prefix       C-Up              resize-pane -U
bind-key -r -T prefix       C-Down            resize-pane -D
bind-key -r -T prefix       C-Left            resize-pane -L
bind-key -r -T prefix       C-Right           resize-pane -R
```

...etc



## 👉 Set Keybindings in Byobu
#tmux  #Byobu 

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



## 👉 `bat` cannot interpret `$()` expression in config file & cannot interpret theme name like `Sublime Snazzy` with space
#bat

I want to config `bat` to adjust theme according to macOS system light/dark themes following official docs via this commands:
```shell
alias cat="bat --theme=\$(defaults read -globalDomain AppleInterfaceStyle &> /dev/null && echo default || echo GitHub)"
```

My practice is i put following into `bat` config file located at `~/.config/bat/config`:
```shell
# Set the theme to "TwoDark"
--theme="\$(defaults read -globalDomain AppleInterfaceStyle &> /dev/null && echo 'Sublime Snazzy' || echo 'Solarized (light)')"

# Show line numbers, Git modifications and file header (but no grid)
--style="numbers,changes,header"

# Use italic text on the terminal (not supported on all terminals)
# --italic-text=always

# Use C++ syntax for Arduino .ino files
--map-syntax "*.ino:C++"
```

The problem is it seems that this `bat` config file cannot process the `$()` expression within it (which i found inexplicable). 
I also tried these expressions:
```shell
# Set the theme to "TwoDark"
--theme=$(defaults read -globalDomain AppleInterfaceStyle &> /dev/null && echo 'Sublime Snazzy' || echo 'Solarized (light)')

# Set the theme to "TwoDark"
--theme=$(defaults read -globalDomain AppleInterfaceStyle &> /dev/null && echo 'Sublime Snazzy' || echo 'Solarized (light)')
```
Then i got error report says:
```shell
error: unexpected argument '-g' found

  note: to pass '-g' as a value, use '-- -g'

Usage: bat [OPTIONS] [FILE]...
       bat <COMMAND>

For more information, try '--help'.
```

I have no clue what went wrong. So i change it to the `~/.zshrc` as official doc suggests:
```shell
alias bat="bat --theme=\$(defaults read -globalDomain AppleInterfaceStyle &> /dev/null && echo 'Sublime Snazzy' || echo 'Solarized (light)')"
```

This time the error says:
```shell
[bat warning]: Unknown theme 'Sublime', using default.
```
It can not recognize the theme 'Sublime Snazzy' even if I wrap it with `''`. (this naming with two seperate words is also stupid..)

So finally i change it to this:
```shell
alias bat="bat --theme=\$(defaults read -globalDomain AppleInterfaceStyle &> /dev/null && echo default || echo GitHub)"
```
Then no reports....


TBD..



## 👉 Tmux cannot set mouse on with command '`:set -g mouse on`'
#tmux 

TBD...



[How do I enable tmux mouse support?]: https://unix.stackexchange.com/questions/516800/how-do-i-enable-tmux-mouse-support