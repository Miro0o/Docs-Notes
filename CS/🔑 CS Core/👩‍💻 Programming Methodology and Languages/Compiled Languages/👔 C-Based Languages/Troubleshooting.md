# Troubleshooting

[TOC]



## 👉 Sleep in C| warning implicit declaration of function `sleep'?
#c #syntax 

> TL;DR 
> As it is stated on the Linux _man_ page [here](https://linux.die.net/man/3/sleep) we need to include **unistd.h** and should do fine for all **OS**.

==The function `sleep` is not part of C programming language==. So, C compiler needs a declaration/prototype of it so that it can get to know about about number of arguments and their data types and return data type of the function. When it doesn't find it, it creates an `Implicit Declaration` of that function.

In Linux, `sleep` has a prototype in `<unistd.h>` and in windows, there is another function `Sleep` which has a prototype in `<windows.h>` or  `<synchapi.h>`. You can always get away with including header, if you explicitly supply the prototype of the function before using it. It is useful when you need only few functions from a header file.

The prototype of `Sleep` function in C on windows is:
```c
VOID WINAPI Sleep(_In_ DWORD dwMilliseconds);
```

Remember, it is always a good practice to supply the prototype of the function being used either by including the appropriate header file or by explicitly writing it. Even, if you don't supply it, compiler will just throw a warning most of the time and it will make an assumption which in most cases will be something that you don't want. It is better to include the header file as API might change in future versions of the Library.


[Sleep | warning implicit declaration of function `sleep'?]: https://stackoverflow.com/questions/39156743/sleep-warning-implicit-declaration-of-function-sleep



## 👉 Undefined reference to pthread_create in Linux
#cpp #c #pthread_create #linux 

Additionally: depending on the platform, you may need 
- a different compiler for threads,
- a different libc for threads (i.e. `-lc_r`),
- `-thread` or `-threads` or other, instead of or in addition to `-lpthread`

---
For Linux the correct command is:
```c
gcc -pthread -o term term.c
```

In general, libraries should follow sources and objects on command line, and `-lpthread` is not an "option", it's a library specification. On a system with only `libpthread.a` installed,
```c
gcc -lpthread ...
```

will fail to link.

Read [this](https://eli.thegreenplace.net/2013/07/09/library-order-in-static-linking) or [this](https://web.archive.org/web/20180627210132/webpages.charter.net/ppluzhnikov/linker.html) detailed explanation.

---
In my case: 
```Makefile
CC = gcc
LD = gcc
CFLAGS = -g -O2 -DHAVE_CONFIG_H -I.

all: shell
shell: shell.o nachos_syscall.o

# $(LD) $(CFLAGS) -s -o shell shell.o nachos_syscall.o -lc -lc_r
# change the -lc_r to -lpthread
$(LD) $(CFLAGS) -s -o shell shell.o nachos_syscall.o -lc -lpthread

clean:
$ (RM) -f shell.o nachos_syscall.o shell

distclean: clean
$(RM) -f Makefile config.h config.log config.status
```

[Undefined reference to pthread_create in Linux]: https://stackoverflow.com/questions/1662909/undefined-reference-to-pthread-create-in-linux

[Undefined Reference to pthread_create]: https://linuxhint.com/undefined-reference-pthread-create/


There are several reasons why the “Undefined reference to pthread_create” error occurs:
1. Missing Thread Header File, 
```c
#include <pthread.h>
```
2. Incorrect Compiler Flag
```Shell
## This gets the error
gcc -o threads posix_threads.c

## This is correct
gcc -pthread -o threads posix_threads.c

# Adding the -pthread option to the compiler commands allows the compiler to execute the code with the pthread.h library.
```
3. Cmake Flag Missing
You can do so by adding the following line to your make file.
```Makefile
add_compile_options(-pthread)
```

Or
```Makefile
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")
```



## 👉 warning: excess elements in array initializer
#c #cpp 



## 👉 static declaration follows non-static declaration
#static_declaration #c #cpp #syntax 



[extern报错:static declaration follows non-static declaration | CSDN]: http://t.csdnimg.cn/7UNnC



## 👉 dereferencing pointer to incomplete type

[dereferencing pointer to incomplete type | Stackoverflow]: https://stackoverflow.com/q/2700646
