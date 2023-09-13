# Troubleshooting

[TOC]



## 👉 Undefined reference to pthread_create in Linux
#cpp #c #pthread_create


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

