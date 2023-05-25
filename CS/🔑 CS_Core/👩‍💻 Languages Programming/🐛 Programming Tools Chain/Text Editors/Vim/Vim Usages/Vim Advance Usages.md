# Vim Advance

[TOC]



## Register
```shell
:help registers


There are ten types of registers:               registers {register} E354
1. The unnamed register ""
2. 10 numbered registers "0 to "9
3. The small delete register "-
4. 26 named registers "a to "z or "A to "Z
5. Three read-only registers ":, "., "%
6. Alternate buffer register "#
7. The expression register "=
8. The selection and drop registers "*, "+ and "~
9. The black hole register "_
10. Last search pattern register "/
```

Vim registers are spaces in memory that Vim uses to store some text or operation details. Each of these spaces has an identifier so that it can be accessed later.

When we want to reference a Vim register, we use a double quote followed by the register’s name. For instance, `“a` means the Vim register <span style="color:red">a</span> and `“:` means the Vim register <span style="color:red">:</span>.

In fact, **registers are used everywhere in Vim**. Let’s see some examples of common usages of Vim registers:
- When we remove texts – for example, using the *x* command – the deleted text is stored in the unnamed register “”
- Once we execute an *Ex* command (*:Command*) in Vim, the register *“:* holds the command
- When we search text by */somePattern*, the search pattern is stored in the *“/* register

#TODO 


[Using Vim Registers]: https://www.baeldung.com/linux/vim-registers
[Vim registers: The basics and beyond]: https://www.brianstorti.com/vim-registers/



## Find & Substitude
### Examples 
Comment lines (add `#` before the line) from 5 to 20:
```vi
:5,20s/^/#/
```

Uncomment lines from 5 to the end, revert the previous changes:
```vi
:5,$s/^#//
```

Replace all instances of ‘apple’, ‘orange’, and ‘mango’ with ‘fruit’:
```vi
:%s/apple\|orange\|mango/fruit/g
```

Remove trailing whitespace at the end of each line:
```vi
:%s/\s\+$//e
```


### Syntaxs & Usecase
``` vim
:[range]s/{pattern}/{string}/[flags] [count]
```

The command searches each line in `[range]` for a `{pattern}`, and replaces it with a `{string}`. `[count]` is a positive integer that multiplies the command.

If no `[range]` and `[count]` are given, only the pattern found in the current line is replaced. The current line is the line where the cursor is placed.

e.g.

```vim
:s/foo/bar/

#### % for whole range & g for entire line
:s/foo/bar/g
:%s/foo/bar/g
:s/foo//g

#### i for case insensitive & I for case sensitive
:s/Foo/bar/gi
:s/Foo/bar/gI


#### Substituting whole word (default look for the pattern as a string not a whole word)
:s/\<Foo\>/bar/gi
```


#### 1️⃣ Delimiters
Instead of the slash character (`/`), you can use any other non-alphanumeric single-byte character except as a delimiter. This option is useful when you have the ‘/’ character in the search pattern or the replacement string.
```vim
:s|foo|bar|
```


#### 2️⃣ Confirm Substitution
To confirm each substitution, use the `c` flag:
```vi
:s/foo/bar/gc
```
Output:
``` vim
replace with bar (y/n/a/q/l/^E/^Y)?
```
Press `y` to replace the match or `l` to replace the match and quit. Press `n` to skip the match and `q` or `Esc` to quit substitution. The `a` option substitutes the match and all remaining occurrences of the match. To scroll the screen down, use `CTRL+Y`, and to scroll up, use `CTRL+E`.


#### 3️⃣ Regualr Expressions
You can also use [regular expressions](https://linuxize.com/post/regular-expressions-in-grep/) as a search pattern. The command bellow replaces all lines starting with ‘foo’ with ‘Vim is the best’:
```vim
:%s/^foo.*/Vim is the best/gc
```
The `^` (caret) symbol matches the beginning of a line and `.*` matches any number of any characters.


#### 4️⃣ Search Range
To substitute all occurrences of ‘foo’ to ‘bar’ in all lines starting from line 3 to line 10 you would use:
```vim
:3,10s/foo/bar/g
```
The range is inclusive, which means that the first and last lines are included in the range.

To substitute ‘foo’ in all lines starting from the current line to the last one:
```vi
:.,$s/foo/bar/
```

The line specifier can also be set using the ‘+’ or ‘-’ symbol,followed by a number that is added or subtracted from the preceding line number. If the number after the symbol is omitted, it defaults to 1.

For example to substitute each ‘foo’ with ‘bar’ starting from the current line and the four next lines, type:

```vi
:.,+4s/foo/bar/g
```


[Find and Replace in Vim / Vi]: https://linuxize.com/post/vim-find-replace/#search-range



## Muiltiple Windows & Files
### Tabs
> 🔗 https://www.linux.com/training-tutorials/vim-tips-using-tabs/


Tabs can be extremely useful, and it only takes a short while to become proficient with them. For more on working with tabs in Vim, run `:help tab-page-intro` within Vim.

#### Opening a tab
```shell
# Probably the easiest to open a new tab
:tabnew 
:tabnew filename


# Another way to do this is to open more than one file at startup using the `-p` option. If you want to open three files in separate tabs, you’d use this syntax:
vim -p file1 file2 file3

# The default maximum is 10 tabs, but you can change this by setting the `tabpagemax` option in your .vimrc, like so:
set tabpagemax=15

#  search for a file in your current path and open it in a new tab
#  For instance, if you want to open a file called inventory.txt that’s in your current path, you could run:
:tabf inven*
```

#### Moving between tabs
You can switch between tabs using `:tabn` and `:tabp`, or you can use `gt` while you’re in normal mode. Of course, if you’re using Vim’s GUI, GVim, you can also use the mouse to switch between tabs or use keyboard shortcuts. In GVim, you can also access a context menu for tabs by right-clicking on the tab bar. Here you can open new tabs with a new buffer or an existing file, or close the current tab.

If you have a lot of tabs open, you can use `:tabfirst`, or just `:tabfir`, to jump to the first tab, and `:tablast` to jump to the last tab that’s open.


#### Rearranging tabs
If you’re really meticulous and want to position tabs _just so_ in Vim, you can move the tabs to a specific spot in the tab order using `:tabm _n_`, where `_n_` is the position number that you want to use. If you don’t give the `:tabm` command an argument, then the current tab will be moved to the last spot.


#### Running commands in tabs
```shell
:tabdo %s/foo/bar/g

```

### Buffers


### Terminals





[How To Edit Multiple Files Using Vim Editor]: https://ostechnix.com/how-to-edit-multiple-files-using-vim-editor/
[vim打开多窗口、多文件之间的切换]: https://blog.csdn.net/qq_22716879/article/details/50810449




## Ref
