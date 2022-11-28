# Make in a nutshell

###### what is make/cmake/qmake?
🎯 🎯 [how is make/cmake/qmake different??](https://www.cnblogs.com/cj2014/p/6111634.html) #unsolved 



###### Make

make is a command line tool on Unix-like OS, executing Makefile and based on that to organize the project as it is expected.
+ `makefile` is a script-like file. it contains all the commands needed for running a project, including  when and how to compile and organize every and each file.
+ Hence, for a large softeware project engineers don't have to compile each file manually one by one. and also `make` makes the maintainness of the proj. easier.  
+ Makefile is specifically ont Unix-like OS.



###### CMake
since make is Unix-like OS specific, there comes cmake. cmake is cross-plantform, it generates `makefile ` for different OS running it. 

```shell
<srcfile> -> cmakelist -> cmake -> makefile -> make -> <targetfile> 
```



###### qmake

akin to cmake. but qmake and cmake have different architecture and policy handling makefile-generating. 
qmake belongs to QT. 



###### other build system...
[make、gmake、cmake、nmake和Dmake 区别](https://blog.csdn.net/lionhenryzxxy/article/details/58585716)
+ Build System :
	+ GUN make
	+ Dmake
	+ NMake (win)
	+ MSBuild
	+  Ninja
	+  CMake
	+  [**qmake**](https://www.jetbrains.com/help/clion/qt-tutorial.html)
		+  [QT](http://c.biancheng.net/view/3868.html). 
	+ cmake
	+ ...
# [Make](https://seisman.github.io/how-to-write-makefile/overview.html)

> 👌 👌 👌  [A very detailed makefile tutorial](https://seisman.github.io/how-to-write-makefile/overview.html) (learn make before learn CMake is recommanded)



```makefile
OBJ = hello.o

hello : $(OBJ)
	g++v $(OBJ) -o hello

$(OBJ) : head.hpp

.PHONY : clean
clean: 
	rm hello $(OBJ)

```


# [CMake](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)
> 📀 cmake tutorial video verison : 
> https://www.bilibili.com/video/BV1Su411m7ey?share_source=copy_web
> 
📜 [CLion -- CMake quick tutorial](https://www.jetbrains.com/help/clion/2021.3/quick-cmake-tutorial.html#ctest)
> 🎯 [CMake quick-tutorial](https://juejin.cn/post/6844904015587704839)
> 📖 [[CS entries quick-look#CMake|about CMake]]
> 
> 🔗 Refs  :
> + https://blog.csdn.net/dbzhang800/article/details/6314073
> + https://juejin.cn/post/6854573214069161997  
> + https://codevion.github.io/#!index.md 
> + https://blog.csdn.net/pix_csdn/article/details/90384155?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-5.highlightwordscore&spm=1001.2101.3001.4242.4
> 


---
+ Architecture
	+ 顶级目录
	+ 构建目录
		+ 构建系统文件 （配置文件）
		+ 构建输出文件


```cmake
cmake_mininum_required (VERSION 3.13)
project (cmaketest)
set (CMAKE_CXX_STANDARD 11)

add_executable (main main.cpp)
add_executable (submain submain.cpp)

add_library (testlib STATIC testlib.cpp)
add_library (testDlib DYNAMIC testDlib.cpp)


find_library(TEST test_lib lib)
target_link_libraries ()

include_directories (inctest/subinctest)

add_subdirectories ()

```



###### FaQ

- [多个文件关联](https://blog.csdn.net/weixin_41594045/article/details/90645699)
- [头文件重复引用](http://c.biancheng.net/view/7636.html)

[include_directories / target_include_directories](https://stackoverflow.com/questions/31969547/what-is-the-difference-between-include-directories-and-target-include-directorie) : the diff between these two command is the scope designated. for `include_directories`, it doesn't specify any peculiar target, so it applies to all targets in the current directory; whereas `target_link_directory` specify the target of the directory to link to, so this designated directory only applies for the designated target. However idk what the[ second answer](https://stackoverflow.com/a/40244458/16542494) means, which looks important though.  

[include vs add_subdirectory](https://stackoverflow.com/questions/49984011/cmake-include-vs-add-subdirectory-relative-header-file-path)

