
+ CLI --> command line interface 
+ GUI --> graphical user interface
+ Crud --> create, read, update, delete 
+ REPL --> read-evaluate-print loop
	+ lisp 
+ PyPl --> python package index 
+ [SDKs](https://whatis.techtarget.com/definition/software-developers-kit-SDK)
	+  software development toolkit, contains every thing needed to developed a software for specific platform.
	+  APIs

# $PATH
Mac系统的环境变量，加载顺序为：  
``` shell
/etc/profile 
/etc/paths 
/etc/paths.d/
~/.bash_profile 
~/.bash_login 
~/.profile


~/.bashrc
```

/etc/profile和/etc/paths是系统级别的，系统启动就会加载，后面几个是当前用户级的环境变量。后面3个按照从前往后的顺序读取，如果/.bash_profile文件存在，则后面的几个文件就会被忽略不读了，如果/.bash_profile文件不存在，才会以此类推读取后面的文件。~/.bashrc没有上述规则，它是bash shell打开的时候载入的。
