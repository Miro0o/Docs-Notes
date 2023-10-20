# Visualization

[TOC]



## Git Visualization
### 👉 [tig](https://github.com/jonas/tig)
Tig is an ncurses-based **text-mode interface for git**. It functions mainly as a Git repository browser, but can also assist in staging changes for commit at chunk level and act as a pager for output from various Git commands.


#### Resources
- Homepage: https://jonas.github.io/tig/
- Manual: https://jonas.github.io/tig/doc/manual.html
- Tarballs: https://github.com/jonas/tig/releases
- Git URL: git://github.com/jonas/tig.git
- Gitter: https://gitter.im/jonas/tig
- Q&A: https://stackoverflow.com/questions/tagged/tig



## Status Visualization
### 👉 Powerline
📂 [Powerline Docs](https://powerline.readthedocs.io/en/latest/usage.html)



## cat Visualization
### 👉 BAT
🏠 https://github.com/sharkdp/bat/

BAT is a substitude of `cat`. It supports loads of text highlighting, git Integratedtion, auto-paging ... and so on many fansy functiones. 

BAT can also be integrated with other tools. 

BAT is configured by configure file. The location of configure file is as `bat --config-file` shows. 
```shell
# Set the theme to auto-ajust as macOS system style changed
--theme="\$(defaults read -globalDomain AppleInterfaceStyle &> /dev/null && echo Sublime Snazzy || echo Solarized (light))"

# Show line numbers, Git modifications and file header (but no grid)
--style="numbers,changes,header"

# Use italic text on the terminal (not supported on all terminals)
# --italic-text=always

# Use C++ syntax for Arduino .ino files
--map-syntax "*.ino:C++"
```

For further detail, check through its official docs. 


### 👉 CCAT
`ccat` is the colorizing `cat`. It works similar to `cat` but displays content with syntax highlighting.


🏠 https://github.com/owenthereal/ccat




## ls Visualization
### 👉 lsd
lsd provides various services for CoreServices frameworks. It is not meant to be invoked directly and it must not be terminated.

#TODO 


### 👉 exa
#TODO 



## Database Client CLI Visualization
### 👉 mycli
🏠 https://github.com/dbcli/mycli
↗ [MySQL](../../../🔑%20CS_Core/🍕%20Database%20System/👔%20DBMS/RDBMS%20(Relational)/🌙%20MySQL/MySQL.md)

A command line client for MySQL that can do auto-completion and syntax highlighting.

HomePage: [http://mycli.net](http://mycli.net/) Documentation: [http://mycli.net/docs](http://mycli.net/docs)


`mycli` is written using [prompt_toolkit](https://github.com/jonathanslenders/python-prompt-toolkit/).

- Auto-completion as you type for SQL keywords as well as tables, views and columns in the database.
- Syntax highlighting using Pygments.
- Smart-completion (enabled by default) will suggest context-sensitive completion.
	- `SELECT * FROM <tab>` will only show table names.
	- `SELECT * FROM users WHERE <tab>` will only show column names.
- Support for multiline queries.
- Favorite queries with optional positional parameters. Save a query using `\fs alias query` and execute it with `\f alias` whenever you need.
- Timing of sql statements and table rendering.
- Config file is automatically created at `~/.myclirc` at first launch.
- Log every query and its results to a file (disabled by default).
- Pretty prints tabular data (with colors!)
- Support for SSL connections
- Some features are only exposed as [key bindings](https://github.com/dbcli/mycli/blob/main/doc/key_bindings.rst)


### 👉 pgcli
🏠 https://www.pgcli.com/
↗ [PostgreSQL](../../../🔑%20CS_Core/🍕%20Database%20System/👔%20DBMS/☕️%20Object-Relational%20Database/PostgreSQL/PostgreSQL.md)

Pgcli is a command line interface for Postgres with auto-completion and syntax highlighting.

Source: [https://github.com/dbcli/pgcli](https://github.com/dbcli/pgcli)



## Ref
