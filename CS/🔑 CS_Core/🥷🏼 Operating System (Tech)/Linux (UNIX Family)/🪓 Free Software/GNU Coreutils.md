# GNU Coreutils

[TOC]



![coreutils brought to you by the GNU project](../../../../../../Assets/Pics/GNU.png)



🏠 https://www.gnu.org/software/coreutils/#help

The GNU Core Utilities are the basic file, shell and text manipulation utilities of the GNU operating system. **These are the core utilities which are expected to exist on every operating system.**



## Getting GNU Coreutils
The latest source with revision history can be browsed using [cgit](https://git.sv.gnu.org/cgit/coreutils.git), [gitweb](https://git.sv.gnu.org/gitweb/?p=coreutils.git) or [GitHub](https://github.com/coreutils/coreutils).
Assuming you have [git](https://git-scm.com/) installed, you can retrieve the latest version with this command:
```
git clone git://git.sv.gnu.org/coreutils
```

A [Coreutils code structure overview](http://www.maizure.org/projects/decoded-gnu-coreutils/) is available, which is useful for educational purposes, or for those interested in contributing changes.
To build from the latest sources please follow the instructions in [README-hacking](https://git.sv.gnu.org/cgit/coreutils.git/plain/README-hacking).
Please note that we do not suggest using test versions of Coreutils for production use.



## Helpful background for code reading
> 🔗 http://www.maizure.org/projects/decoded-gnu-coreutils/

The GNU coreutils has its foibles. Many of these utilities are approaching 30 years old and include revisions by many people over the years. Here are some things to keep in mind when reading the code:

- Tiny programs
  - These utilities are small, (mostly) single-source file programs designed to do one thing and do it well. They are not designed for long life or to scale beyond their role. Consequently, we see designs often considered 'bad practice' such as:
  - Many globals
  - Liberal use of macros
  - `goto` statements
  - Long functions with nested switchs/loops
  
- **Know POSIX** - Start with the [Utility Syntax Guidelines](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html#tag_12_02). In general, POSIX supports interoperability by defining appropriate inputs and outputs, but leaves the 'work' to the implementation. While the GNU coreutils [may not strictly conform](https://www.gnu.org/software/coreutils/manual/html_node/Standards-conformance.html) to POSIX, many ideas are entrenched: permission bits, uids/gids, environment variables, exit status, and about [3718 pages](http://www.open-std.org/jtc1/sc22/open/n4217.pdf) of more trivia. 
  
- **Outside help** - Portability is a complex problem and coreutils relies on extra help from a related project: [gnulib](https://www.gnu.org/s/gnulib/). Almost every utility includes functions from gnulib which are specially designed for common problems used in many places across various systems - No need to reinvent the wheel.
  
- **Launched from a shell** - The Core utilities expect support from a shell such as bash, zsh, ksh, and others. The shell forks/clones in to the utility, passes the arguments, sets up the environment, redirects I/O via pipes, and retains exit values.
  
- **Three families** - GNU coreutils were originally three distinct packages for shell, text, and file utilities. Utilities within the same type share many of the same design patterns.



## Getting Help
- Check Questions and Answers for common problems: [Coreutils FAQ](https://www.gnu.org/software/coreutils/faq/coreutils-faq.html)
- Read the manual locally using info coreutils or see the latest [online manual](https://www.gnu.org/software/coreutils/manual/) ([日本語](https://linuxjm.osdn.jp/info/GNU_coreutils/coreutils-ja.html)).
- The [Coreutils Gotchas](https://www.pixelbeat.org/docs/coreutils-gotchas.html) contains a list of some quirks and unexpected behaviour (which are often mistaken for bugs).
- Search the archives for previous questions and answers:
  - Search mailing lists: 
  - General usage and advice: [coreutils mailing list](https://lists.gnu.org/archive/html/coreutils/).
  - Bug reports: [bug-coreutils mailing List](https://lists.gnu.org/archive/html/bug-coreutils/).
- Send general questions or suggestions to the mailing list at <[coreutils@gnu.org](mailto:coreutils@gnu.org)>.
- Send translation requests to the language team at the [Translation Project](https://translationproject.org/domain/coreutils.html).
- Report bugs, including version and distribution variant, to the list at <[bug-coreutils@gnu.org](mailto:bug-coreutils@gnu.org)>.
  Before sending the bug, please consult the FAQ and mailing list archives (above).
  Often these perceived bugs are simply due to wrong program usage.
  To learn more about reporting bugs, see [Getting help with GNU software](https://www.gnu.org/software/gethelp.html).



## Ref
