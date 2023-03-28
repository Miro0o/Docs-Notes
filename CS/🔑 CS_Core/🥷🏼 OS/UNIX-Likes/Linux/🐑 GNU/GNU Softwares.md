# GNU Softwares

This page mainly focus on *GNU/Linux Core tools*. Check in  [**zsh.md**](../../../../Software/CLI/Shell&Emulator/zsh.md)  or [**iTterm2.md**](../../../../Software/CLI/Shell&Emulator/iTterm2.md) or [**🏫 Missing tutorial - MIT.md**](../../../../../🗺 CS_Overview/🏫 Missing tutorial - MIT.md) and their 🔗links at the bottom of the page for more possible info about other fancy CLI tools. 🎉



[TOC]

## Res

- [short descriptions for all GNU packages](https://www.gnu.org/manual/blurbs.html);
- [documentation for GNU packages](https://www.gnu.org/manual/manual.html) (arranged by category);
- [GNU package logos](https://www.gnu.org/graphics/package-logos.html);
- [recent GNU releases](https://www.gnu.org/software/recent-releases.html).



## 🐌 Intro

> 🔗 Check out more on [GNU Software Homepage](https://www.gnu.org/software/#navigation)

>  [GNU](https://www.gnu.org/gnu/about-gnu.html) is an operating system which is 100% free software. It was launched in 1983 by Richard Stallman (rms) and has been developed by many people working together for the sake of freedom of all software users to control their computing. Technically, GNU is generally like Unix. But unlike Unix, GNU gives its users freedom.

The GNU system contains all of the [official GNU software packages](https://www.gnu.org/philosophy/categories.html#GNUsoftware) (which are listed below), and also includes non-GNU free software, notably TeX and the X Window System. Also, the GNU system is not a single static set of programs; users and distributors may select different packages according to their needs and desires. The result is still a variant of the GNU system.

👀 If you're looking for **a whole system t**o install, see our [list of GNU/Linux distributions which are entirely free software](https://www.gnu.org/distros/free-distros.html).

👀 To look for **individual free software packages**, both GNU and non-GNU, please see the [Free Software Directory](http://directory.fsf.org/): a categorized, searchable database of free software.

-  The Directory is actively maintained by the [Free Software Foundation](http://www.fsf.org/) and includes links to program home pages where available, as well as entries for [all GNU packages](http://directory.fsf.org/wiki/GNU/). 
- Another list of [all GNU packages](https://www.gnu.org/software/#allgnupkgs) is below. [Free software documentation links](https://www.gnu.org/doc/doc.html) are listed separately.

♻️ Finally, we have [a short list of free software replacements](https://directory.fsf.org/wiki/Free_Software_Directory:Free_software_replacements) for proprietary software running on various proprietary systems.

🎓 We have also published a [list of recommended educational software](https://www.gnu.org/software/free-software-for-education.html).



## [The GNU Netcat Proj](https://netcat.sourceforge.net)

- Outbound and inbound connections, TCP or UDP, to or from any ports.
- Featured **tunneling mode** which allows also special tunneling such as UDP to TCP, with the possibility of specifying all network parameters (source port/interface, listening port/interface, and the remote host allowed to connect to the tunnel.
- Built-in port-scanning capabilities, with randomizer.
- Advanced usage options, such as buffered send-mode (one line every N seconds), and hexdump (to stderr or to a specified file) of trasmitted and received data.
- Optional RFC854 telnet codes parser and responder.



## Util-linux





## 🧑🏽‍💻 /usr/bin/

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

[tar压缩解压缩命令详解](https://www.cnblogs.com/jyaray/archive/2011/04/30/2033362.html) 





## 🧑🏽‍💻 /usr/local/bin

> User cumsotized tool sets.

### automake & autoconf

[automake, autoconf 使用详解](https://www.laruence.com/2009/11/18/1154.html)

TBD... 



## 🖇 Refs:

[七个 GNU 工具，命令行的强大功能与终端亲密接触的必备工具](https://www.51cto.com/article/706173.html)

