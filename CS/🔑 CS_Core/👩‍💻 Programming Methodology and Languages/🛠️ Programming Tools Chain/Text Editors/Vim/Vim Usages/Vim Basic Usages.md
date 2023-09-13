# Vim Basic Usages

[TOC]



## Res


## Intro
Get an overview of vim basics from below:
``` shell
Get specific help:  It is possible to go directly to whatever you want help on, by giving an argument to the :help command. 

Prepend something to specify the context:  help-context


    WHAT                  PREPEND    EXAMPLE
Normal mode command                  :help x
Visual mode command         v_       :help v_u
Insert mode command         i_       :help i_<Esc>
Command-line command        :        :help :quit
Command-line editing        c_       :help c_<Del>
Vim command argument        -        :help -r
Option                      '        :help 'textwidth'
Regular expression          /        :help /[

See help-summary for more contexts and an explanation.
See notation for an explanation of the help syntax.
```

Get a quick look of vim basics from below:
``` shell
// in vim, type :help [section_name] for info list

BASIC:
quickref        Overview of the most common commands you will use
tutor           30-minute interactive course for beginners
copying         About copyrights
iccf            Helping poor children in Uganda
sponsor         Sponsor Vim development, become a registered Vim user
www             Vim on the World Wide Web
bugs            Where to send bug reports

USER MANUAL: These files explain how to accomplish an editing task.

usr_toc.txt     Table Of Contents
```


### 📚 Vim Docs
#### 1️⃣ User Manual
USER MANUAL: These files explain how to accomplish an editing task.

1. Getting started
```
usr_01.txt  About the manuals
usr_02.txt  The first steps in Vim
usr_03.txt  Moving around
usr_04.txt  Making small changes
usr_05.txt  Set your settings
usr_06.txt  Using syntax highlighting
usr_07.txt  Editing more than one file
usr_08.txt  Splitting windows
usr_09.txt  Using the GUI
usr_10.txt  Making big changes
usr_11.txt  Recovering from a crash
usr_12.txt  Clever tricks
```

2. Editing Effectively
```
usr_20.txt  Typing command-line commands quickly
usr_21.txt  Go away and come back
usr_22.txt  Finding the file to edit
usr_23.txt  Editing other files
usr_24.txt  Inserting quickly
usr_25.txt  Editing formatted text
usr_26.txt  Repeating
usr_27.txt  Search commands and patterns
usr_28.txt  Folding
usr_29.txt  Moving through programs
usr_30.txt  Editing programs
usr_31.txt  Exploiting the GUI
usr_32.txt  The undo tree
```

3. Tuning Vim
```
usr_40.txt  Make new commands
usr_41.txt  Write a Vim script
usr_42.txt  Add new menus
usr_43.txt  Using filetypes
usr_44.txt  Your own syntax highlighted
usr_45.txt  Select your language
```

4. Writing Vim scripts
```
usr_50.txt  Advanced Vim script writing
usr_51.txt  Create a plugin
usr_52.txt  Write plugins using Vim9 script
```

5. Making Vim Run
```
usr_90.txt  Installing Vim
```


#### 2️⃣ Reference Manual
REFERENCE MANUAL: These files explain every detail of Vim.

1. Basics editing
```
starting.txt    starting Vim, Vim command arguments, initialisation
editing.txt     editing and writing files
motion.txt      commands for moving around
scroll.txt      scrolling the text in the window
insert.txt      Insert and Replace mode
change.txt      deleting and replacing text
undo.txt        Undo and Redo
repeat.txt      repeating commands, Vim scripts and debugging
visual.txt      using the Visual mode (selecting a text area)
various.txt     various remaining commands
recover.txt     recovering from a crash
```

2. Advanced editing
```
cmdline.txt     Command-line editing
options.txt     description of all options
pattern.txt     regexp patterns and search commands
map.txt         key mapping and abbreviations
tagsrch.txt     tags and special searches
windows.txt     commands for using multiple windows and buffers
tabpage.txt     commands for using multiple tab pages
spell.txt       spell checking
diff.txt        working with two to eight versions of the same file
autocmd.txt     automatically executing commands on an event
eval.txt        expression evaluation, conditional commands
builtin.txt     builtin functions
userfunc.txt    defining user functions
channel.txt     Jobs, Channels, inter-process communication
fold.txt        hide (fold) ranges of lines
```

3. General subjects
```
intro.txt       general introduction to Vim; notation used in help files
help.txt        overview and quick reference (this file)
helphelp.txt    about using the help files
index.txt       alphabetical index of all commands
help-tags       all the tags you can jump to (index of tags)
howto.txt       how to do the most common editing tasks
tips.txt        various tips on using Vim
message.txt     (error) messages and explanations
quotes.txt      remarks from users of Vim
todo.txt        known problems and desired extensions
develop.txt     development of Vim
debug.txt       debugging Vim itself
uganda.txt      Vim distribution conditions and what to do with your money
```

4. Special issues
```
testing.txt     testing Vim and Vim scripts
print.txt       printing
remote.txt      using Vim as a server or client
term.txt        using different terminals and mice
terminal.txt    Terminal window support
popup.txt       popup window support
vim9.txt        using Vim9 script
```

5. Programming language support
6. Language support
7. GUI
8. Versions
9. Interfaces
```
if_cscop.txt    using Cscope with Vim
if_lua.txt      Lua interface
if_mzsch.txt    MzScheme interface
if_perl.txt     Perl interface
if_pyth.txt     Python interface
if_tcl.txt      Tcl interface
if_ole.txt      OLE automation interface for Win32
if_ruby.txt     Ruby interface
debugger.txt    Interface with a debugger
netbeans.txt    NetBeans External Editor interface
sign.txt        debugging signs
```

10. Remarks about specific systems
11. Standard plugins
```
pi_getscript.txt Downloading latest version of Vim scripts
pi_gzip.txt      Reading and writing compressed files
pi_logipat.txt   Logical operators on patterns
pi_netrw.txt     Reading and writing files over a network
pi_paren.txt     Highlight matching parens
pi_spec.txt      Filetype plugin to work with rpm spec files
pi_tar.txt       Tar file explorer
pi_vimball.txt   Create a self-installing Vim script
pi_zip.txt       Zip archive explorer
```



## Navigation
### Navigation within File



### Navigation betweent Files


### Go TO Definition
#### 1️⃣ include & define

#### 2️⃣ Ctags


#### 3️⃣ Static code analysis
The smartest "Jump to Definition" mechanic would definitely rely on parsing and analyzing the code itself, which is what static analysis engines are for.

There are multiple plugins out there that work to integrate with these engines, e.g. [tern_for_vim](https://github.com/ternjs/tern_for_vim) for Javascript. Try and find one for your language of choice, or ask some of the helpful chaps in [r/vim](https://www.reddit.com/r/vim/) or \#vim on freenode!

##### Language Server Protocol!
which aims to provide a standard for text editors and static analysis engines to work together.

↗ [LSP for Vim](../Vim%20Customization/LSP%20for%20Vim.md)



## Ref
[Vim and Definitions | Github]: https://gist.github.com/igemnace/dfa545d0d71228e010876d48a420a50b

