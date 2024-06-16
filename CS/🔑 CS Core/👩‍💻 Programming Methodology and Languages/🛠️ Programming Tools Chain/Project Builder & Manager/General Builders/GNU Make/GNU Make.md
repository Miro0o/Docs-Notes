# GNU Make

[TOC]



## Res
### Related Topics


### Other Resources
[Make](https://seisman.github.io/how-to-write-makefile/overview.html)



## Intro
### 为什么学 GNU Make
大家第一次写 hello world 程序的时候一定都记得，在编辑完 `helloworld.c` 之后，需要用 `gcc`编译生成可执行文件，然后再执行（如果你不理解前面这段话，请先自行谷歌 *gcc 编译* 并理解相关内容）。但如果你的项目由成百上千个 C 源文件组成，并且星罗棋布在各个子目录下，你该如何将它们编译链接到一起呢？假如你的项目编译一次需要半个小时（大型项目相当常见），而你只修改了一个分号，是不是还需要再等半个小时呢？

这时候 GNU Make 就闪亮登场了，它能让你在一个脚本里（即所谓的 `Makefile`）定义整个编译流程以及各个目标文件与源文件之间的依赖关系，并且只重新编译你的修改会影响到的部分，从而降低编译的时间。


### 如何学习 GNU Make
这里有一篇写得深入浅出的文档 [跟我一起写makefile](https://seisman.github.io/how-to-write-makefile/overview.html) 供大家参考。

GNU Make 掌握起来相对容易，但用好它需要不断的练习。将它融入到自己的日常开发中，勤于学习和模仿其他优秀开源项目里的 `Makefile` 的写法，总结出适合自己的 template，久而久之，你对 GNU Make 的使用会愈加纯熟。

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



## Ref
[makefile -- 后缀规则]: https://blog.csdn.net/Anhui_Chen/article/details/107874270
> 后缀规则是一种 make 定义隐式规则的旧式方式。**模式规则更加通用、清晰，后缀规则已经被废弃。** 为了兼容旧的 makefiles，GNU make 依然支持后缀规则。后缀规则有两种形式：**双后缀**和**单后缀**。
