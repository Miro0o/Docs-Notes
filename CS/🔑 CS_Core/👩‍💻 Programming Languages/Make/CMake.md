

# [CMake](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)



> 📀 cmake tutorial video verison : 
> https://www.bilibili.com/video/BV1Su411m7ey?share_source=copy_web
>
> 📜 [CLion -- CMake quick tutorial](https://www.jetbrains.com/help/clion/2021.3/quick-cmake-tutorial.html#ctest)
> 🎯 [CMake quick-tutorial](https://juejin.cn/post/6844904015587704839)
> 📖 [[CS entries quick-look#CMake|about CMake]]
>
> 🔗 Refs  :
>
> + https://blog.csdn.net/dbzhang800/article/details/6314073
> + https://juejin.cn/post/6854573214069161997  
> + https://codevion.github.io/#!index.md 
> + https://blog.csdn.net/pix_csdn/article/details/90384155?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-5.highlightwordscore&spm=1001.2101.3001.4242.4



## 为什么学习 CMake

CMake 是类似于 GNU make 的跨平台自动软件构建工具，使用 CMakeLists.txt 定义构建规则，相比于 make 它提供了更多的功能，在各种软件构建上广泛使用。**强烈建议学习使用 GNU Make 和熟悉 `Makefile` 后再学习 CMake**。



## 如何学习 CMake

`CMakeLists.txt` 比 `Makefile` 更为抽象，理解和使用难度也更大。现阶段很多 IDE (如 Visual Studio, CLion) 提供了自动生成 `CMakeLists.txt` 的功能，但掌握 `CMakeLists.txt` 的基本用法仍然很有必要。除了 [CMake 官方 Tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html) 外，上海交通大学 IPADS 组新人培训也提供了[大约一小时的视频教程](https://www.bilibili.com/video/BV14h41187FZ)。



## Logs

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



## FaQ

- [多个文件关联](https://blog.csdn.net/weixin_41594045/article/details/90645699)
- [头文件重复引用](http://c.biancheng.net/view/7636.html)

[include_directories / target_include_directories](https://stackoverflow.com/questions/31969547/what-is-the-difference-between-include-directories-and-target-include-directorie) : the diff between these two command is the scope designated. for `include_directories`, it doesn't specify any peculiar target, so it applies to all targets in the current directory; whereas `target_link_directory` specify the target of the directory to link to, so this designated directory only applies for the designated target. However idk what the[ second answer](https://stackoverflow.com/a/40244458/16542494) means, which looks important though.  

[include vs add_subdirectory](https://stackoverflow.com/questions/49984011/cmake-include-vs-add-subdirectory-relative-header-file-path)

