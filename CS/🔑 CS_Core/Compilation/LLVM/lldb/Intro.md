# [LLDB](https://lldb.llvm.org)

LLDB, a set of debugger developed by [[CS entries quick-look#LLVM|LLVM]]

## Tutorial

👉 [llvm - lldb - tutorial](https://lldb.llvm.org/use/tutorial.html)

[comamand quicklook](https://ld246.com/article/1556200452086#用-查看)



###### Ref:

- https://www.cnblogs.com/gaoxiaoniu/p/5864530.html
- https://cloud.tencent.com/developer/article/1013359
- https://casatwy.com/shi-yong-lldbdiao-shi-cheng-xu.html 

### logs:

```shell
clang++ -g demo.cpp

lldb a.out

```


<iframe width="560" height="315" src="https://www.youtube.com/embed/2GV0K9Y2MKA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### quick notes:

##### 1. basics

```shell
$ lldb <src> arg1 argv[]
(lldb) settings set -- target.run-args  "arg1"

(lldb) break set -f <src.c> -l #
(lldb) br s -f <src.c> -l #
(lldb) b <src.c> : #
(lldb) b <function_name>

(lldb) br list
(lldb) b l 

(lldb) br del #
(lldb) br del 

(lldb) p varname

(lldb) frame variable
(lldb) fr v
(lldb) fr s #
(lldb) f #

(lldb) watchpoint set variable <>
(lldb) watchpoint set variable -w read | write | read_write <>
(lldb) w s v <>

```

##### 2. diff file compilement

```shell
> clang -g <src.c> -o <dst>
	> dst.out
	> dst.dYSM
> clang <src.c> -o <dst>
	> dst (excutable)
```

+ screenshot for `lldb dst`

```shell
Process 31912 launched: '/Users/mir0/Desktop/labs/t1' (x86_64)
Process 31912 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
    frame #0: 0x00000001000030a0 t1`main
t1`main:
->  0x1000030a0 <+0>: pushq  %rbp
    0x1000030a1 <+1>: movq   %rsp, %rbp
    0x1000030a4 <+4>: subq   $0x10, %rsp
    0x1000030a8 <+8>: movq   0xf51(%rip), %rdi         ; (void *)0x00007ff847b955e0: std::__1::cout
Target 0: (t1) stopped.
```

+ for `lldb dst.out`

 > [a.out](https://www.cnblogs.com/zhangfeionline/p/5967671.html)

```shell
Process 32094 launched: '/Users/mir0/Desktop/labs/debuglab1' (x86_64)
Process 32094 stopped
* thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
    frame #0: 0x0000000100003df6 debuglab1`main(argc=2, argv=0x00007ff7bfeff7d8) at lab1_src.c:89:6
   86
   87  	int main (int argc, char *argv[])
   88  	{
-> 89  		int dummy = 1;
   90  		int start, stride;
   91  		int key1, key2, key3, key4;
   92  		char * msg1, * msg2;
Target 0: (debuglab1) stopped.
```


---

<iframe width="560" height="315" src="https://www.youtube.com/embed/rU78J2MlXOk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


# Troubleshooting

## [floating point exception](https://www.cnblogs.com/tdyizhen1314/p/4963814.html)

## [segment fault](https://www.cnblogs.com/hello--the-world/archive/2012/05/31/2528326.html#:~:text=A%20segmentation%20fault%20%28often%20shortened%20to%20segfault%29%20is,a%20way%20that%20is%20not%20allowed%20%28e.g.%2C%20)

> A segmentation fault (often shortened to segfault) is a particular error condition that can occur during the operation of computer software. In short, a segmentation fault occurs when a program attempts to access a memory location that it is not allowed to access, or attempts to access a memory location in a way that is not allowed (e.g., attempts to write to a read-only location, or to overwrite part of the operating system). Systems based on processors like the Motorola 68000 tend to refer to these events as Address or Bus errors. 
> Segmentation is one approach to memory management and protection in the operating system. It has been superseded by paging for most purposes, but much of the terminology of segmentation is still used, "segmentation fault" being an example. Some operating systems still have segmentation at some logical level although paging is used as the main memory management policy.  
> On Unix-like operating systems, a process that accesses invalid memory receives the SIGSEGV signal. On Microsoft Windows, a process that accesses invalid memory receives the STATUS_ACCESS_VIOLATION exception.

> 所谓的段错误 就是指访问的内存超出了系统所给这个程序的内存空间，通常这个值是由gdtr来保存的，他是一个48位的寄存器，其中的32位是保存由它指向的gdt表， 后13位保存相应于gdt的下标，最后3位包括了程序是否在内存中以及程序的在cpu中的运行级别,指向的gdt是由以64位为一个单位的表，在这张表中 就保存着程序运行的代码段以及数据段的起始地址以及与此相应的段限和页面交换还有程序运行级别还有内存粒度等等的信息。一旦一个程序发生了越界访 问，cpu就会产生相应的异常保护，于是segmentation fault就出现了

通过上面的解释，段错误应该就是访问了不可访问的内存，这个内存区1. 要么是不存在的，2. 要么是受到系统保护的。

Segment fault 之所以能够流行于世，是与Glibc库中基本所有的函数都默认型参指针为非空有着密切关系的。