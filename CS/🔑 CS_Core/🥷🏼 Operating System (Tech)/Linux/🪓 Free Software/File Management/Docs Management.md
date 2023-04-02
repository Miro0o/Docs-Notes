# Docs Management

[TOC]



## Res


## Intro
How to get docs & cheat sheets about a given command? There are a lot!

For built-in support, there are `man`, `info`, `apropos`, etc.
For online cheat sheets, ↗ [Cheat.sh](../../../🐚%20Shell/Shell%20Helper/Cheat.sh.md), ↗ [explainshell](../../../🐚%20Shell/Shell%20Helper/explainshell.md), ↗ [oh-my-zsh](../../../🐚%20Shell/Shell%20Helper/oh-my-zsh.md), and many more!
For emulator support, there are many emulators that integrate AI support for commands how-to, like ↗ [warp](../../../🐚%20Shell/Emulator%20|%20Terminal/warp.md)!




## `man`



## `INFO`
`info` is a program (info reader) akin `man` . it is for online docs reading.

Each entry is noted as `node`, and the whole documentation is organized as such nodes. 


### `INFO` basics
-  `d`  --- to go to directory node (Info main menu)
	```shell
	
	This is the Info main menu (aka directory node).
	A few useful Info commands:
	
	  'q' quits;
	  'H' lists all Info commands;
	  'h' starts the Info tutorial;
	  'mTexinfo RET' visits the Texinfo manual, etc.
	
	* Menu:
	```

- `b` --- to go to the top of the node
- `t` --- go to the top node _(default entrance node)_ of the documentation
- `n` / `p` --- next/previous node on _parent level_
- `[` / `]` --- next/previous node on _same level_
- `[SPC]` / `[DEL]` --- next/previous page 
- `l` --- retrace to last node
- `u` --- move up to parent node 
- `m`--- menu 
- `f` --- find the cross-reference on the page
- `[TAB]` --- toggle between the cross-reference on the page
	+ --- text auto-completion


### `INFO` advanced

#TODO 


## `apropos`
#TODO 



## Ref

