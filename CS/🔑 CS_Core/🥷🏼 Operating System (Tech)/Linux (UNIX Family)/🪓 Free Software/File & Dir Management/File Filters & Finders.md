# File Filters & Finders

[TOC]



## Res



## File Filters /Finders
### 👉 fd
fd is a simple, fast and user-friendly alternative to find(1).

By default fd uses regular expressions for the pattern. However, this can be

changed to use simple glob patterns with the '--glob' option.


**`fd`**
`fd` is an alternative to `find`. Aims to be faster and easier to use than `find`.

```shell
 cheat:fd
# Simple search:
fd <search query>

# Specifying the root directory for the search:
fd <search query> <directory>

# Searching for a particular file extension:
fd -e <file extension> <search query>

# Searching for a particular file name:
fd -g <file name>.<file extension>

# Search for hidden and ignored files:
fd -H <search query>

# Excluding specific files or directories:
fd -E <file or directories which should be excluded> <search query>
```


### 👉 `find

```shell
# Find all directories named src
find . -name src -type d
# Find all python files that have a folder named test in their path
find . -path '*/test/*.py' -type f
# Find all files modified in the last day
find . -mtime -1
# Find all zip files with size in range 500k to 10M
find . -size +500k -size -10M -name '*.tar.gz'
# Delete all files with .tmp extension
find . -name '*.tmp' -exec rm {} \;
# Find all PNG files and convert them to JPG
find . -name '*.png' -exec convert {} {}.jpg \;
```


### 👉 `locate`
- ` sudo /usr/libexec/locate.updatedb`

🔗 [locate vs find: usage, pros and cons of each other](https://unix.stackexchange.com/questions/60205/locate-vs-find-usage-pros-and-cons-of-each-other) 



## Codes Filters /Finders
### 👉 `grep`
[`grep`](https://www.man7.org/linux/man-pages/man1/grep.1.html)


### 👉 `ack`
- [ack](https://github.com/beyondgrep/ack3)


### 👉 `ag`
- [ag](https://github.com/ggreer/the_silver_searcher) (The Silver Search)


### 👉 `rg`
- [rg](https://github.com/BurntSushi/ripgrep) (Ripgrep)



## Finding shell cmds
`history` 

`Ctrl+R`: perform backwards search 

- [fzf](https://github.com/junegunn/fzf/wiki/Configuring-shell-key-bindings#ctrl-r) can be enabled for `Ctrl + R` after activated in `oh-my-zsh` (?)

> You can modify your shell’s history behavior, like preventing commands with a leading space from being included. This comes in handy when you are typing commands with passwords or other bits of sensitive information. To do this, add `HISTCONTROL=ignorespace` to your `.bashrc` or `setopt HIST_IGNORE_SPACE` to your `.zshrc`. If you make the mistake of not adding the leading space, you can always manually remove the entry by editing your `.bash_history` or `.zhistory`.


**history-based autosuggestions**



## File Comparision
### Text Interface

#### 👉 `diff`

#### 👉 `rsync`


### Graphics Interface

#### 👉 `vimdiff`

#### 👉 `meld`


[Linux下快速比较两个目录的不同]: https://www.cnblogs.com/f-ck-need-u/p/9071033.html



## Ref

