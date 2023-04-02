# FAQ

[TOC]



## 👉 Miscs
- [多个文件关联](https://blog.csdn.net/weixin_41594045/article/details/90645699)
- [头文件重复引用](http://c.biancheng.net/view/7636.html)

[include_directories / target_include_directories](https://stackoverflow.com/questions/31969547/what-is-the-difference-between-include-directories-and-target-include-directorie) : the diff between these two command is the scope designated. for `include_directories`, it doesn't specify any peculiar target, so it applies to all targets in the current directory; whereas `target_link_directory` specify the target of the directory to link to, so this designated directory only applies for the designated target. However idk what the[ second answer](https://stackoverflow.com/a/40244458/16542494) means, which looks important though.  

[include vs add_subdirectory](https://stackoverflow.com/questions/49984011/cmake-include-vs-add-subdirectory-relative-header-file-path)



## Ref

