# Vim Advance

[TOC]



## Register
Vim registers are spaces in memory that Vim uses to store some text or operation details. Each of these spaces has an identifier so that it can be accessed later.

When we want to reference a Vim register, we use a double quote followed by the register’s name. For instance, *“a* means *the Vim register a* and *“:* means *the Vim register :*.

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


### Basics
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



## Windows & Files



[vim打开多窗口、多文件之间的切换]: https://blog.csdn.net/qq_22716879/article/details/50810449