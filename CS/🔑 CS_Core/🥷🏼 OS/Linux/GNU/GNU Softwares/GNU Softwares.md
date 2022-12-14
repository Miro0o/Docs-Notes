# GNU Softwares

This page mainly focus on *GNU/Linux Core tools*. Check in  [**zsh.md**](../../../../Software/CLI/Shell&Emulator/zsh.md)  or [**iTterm2.md**](../../../../Software/CLI/Shell&Emulator/iTterm2.md) or [**π« Missing tutorial - MIT.md**](../../../../../πΊ CS_Overview/π« Missing tutorial - MIT.md) and their πlinks at the bottom of the page for more possible info about other fancy CLI tools. π



[TOC]



## π Intro

> :link: Check out more on [GNU Software Homepage](https://www.gnu.org/software/#navigation)



[GNU](https://www.gnu.org/gnu/about-gnu.html) is an operating system which is 100% free software. It was launched in 1983 by Richard Stallman (rms) and has been developed by many people working together for the sake of freedom of all software users to control their computing. Technically, GNU is generally like Unix. But unlike Unix, GNU gives its users freedom.

The GNU system contains all of the [official GNU software packages](https://www.gnu.org/philosophy/categories.html#GNUsoftware) (which are listed below), and also includes non-GNU free software, notably TeX and the X Window System. Also, the GNU system is not a single static set of programs; users and distributors may select different packages according to their needs and desires. The result is still a variant of the GNU system.

If you're looking for a whole system to install, see our [list of GNU/Linux distributions which are entirely free software](https://www.gnu.org/distros/free-distros.html).

To look for individual free software packages, both GNU and non-GNU, please see the [Free Software Directory](http://directory.fsf.org/): a categorized, searchable database of free software. The Directory is actively maintained by the [Free Software Foundation](http://www.fsf.org/) and includes links to program home pages where available, as well as entries for [all GNU packages](http://directory.fsf.org/wiki/GNU/). Another list of [all GNU packages](https://www.gnu.org/software/#allgnupkgs) is below. [Free software documentation links](https://www.gnu.org/doc/doc.html) are listed separately.

Finally, we have [a short list of free software replacements](https://directory.fsf.org/wiki/Free_Software_Directory:Free_software_replacements) for proprietary software running on various proprietary systems.

We have also published a [list of recommended educational software](https://www.gnu.org/software/free-software-for-education.html).



## Res

- [short descriptions for all GNU packages](https://www.gnu.org/manual/blurbs.html);
- [documentation for GNU packages](https://www.gnu.org/manual/manual.html) (arranged by category);
- [GNU package logos](https://www.gnu.org/graphics/package-logos.html);
- [recent GNU releases](https://www.gnu.org/software/recent-releases.html).



## Util-linux





## π§π½βπ» /usr/bin/

> Built-in Packages of some essencial tool set.

### `INFO`

`info` is a program (info reader) akin `man` . it is for online docs reading.

each entry is noted as `node`, and the whole documentation is organized as such nodes. 



#### `INFO` basics

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
-  `b` --- to go to the top of the node
-  `t` --- go to the top node _(default entrance node)_ of the documentation
- `n` / `p` --- next/previous node on _parent level_
- `[` / `]` --- next/previous node on _same level_
- `[SPC]` / `[DEL]` --- next/previous page 
- `l` --- retrace to last node
- `u` --- move up to parent node 
- `m`--- menu 
- `f` --- find the cross-reference on the page
- `[TAB]` --- toggle between the cross-reference on the page
	+ --- text auto-completion



#### `INFO` advanced #unsolved

tbd...



### tar & compression

[Quick Benchmark: Gzip vs Bzip2 vs LZMA vs XZ vs LZ4 vs LZO](https://catchchallenger.first-world.info/wiki/Quick_Benchmark:_Gzip_vs_Bzip2_vs_LZMA_vs_XZ_vs_LZ4_vs_LZO)

[tarεηΌ©θ§£εηΌ©ε½δ»€θ―¦θ§£](https://www.cnblogs.com/jyaray/archive/2011/04/30/2033362.html) 





## π§π½βπ» /sbin/

> System Level Packages providing Core Op.

### ping

> [π ping host:port δ½Ώη¨pingε½δ»€ε―ΉηΉε?η«―ε£θ?Ώι?](https://blog.csdn.net/allway2/article/details/106961916)



### [telent](https://www.cnblogs.com/peida/archive/2013/03/13/2956992.html)

telent $\subset$ TELENT $\subset$ TCP/IP
```shell
$ telnet <ip_address> <port_number>

$ telnet <domain_name> <port_number>
```

### [nc]()

```shell
$ nc -vz <host> <port_number>

$ nc -vz <domain> <port_number>
```

### [nmap]()

```shell
$ nmap -p 1-100 <ip_address>

$ nmap -p 1-100 <hostname>
```

### [powershell]()

```shell
$ Test-NetConnection <ip_address> -p <port_number>

$ Test-NetConnection 192.168.178.35 -p 389
```



### nsenter

>  [nsenterδ½Ώη¨](https://www.cnblogs.com/edeny/p/15247306.html) 



TBD..



## π§π½βπ» /usr/local/bin

> User cumsotized tool sets.

### automake & autoconf

[automake, autoconf δ½Ώη¨θ―¦θ§£](https://www.laruence.com/2009/11/18/1154.html)

TBD... 



## π Refs:

[δΈδΈͺ GNU ε·₯ε·οΌε½δ»€θ‘ηεΌΊε€§εθ½δΈη»η«―δΊ²ε―ζ₯θ§¦ηεΏε€ε·₯ε·](https://www.51cto.com/article/706173.html)

