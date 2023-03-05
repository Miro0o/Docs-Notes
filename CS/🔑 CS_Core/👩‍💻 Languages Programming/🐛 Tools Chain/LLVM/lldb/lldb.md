# [LLDB](https://lldb.llvm.org)

[TOC]



## Res
### Tutorial
👉 [llvm - lldb - tutorial](https://lldb.llvm.org/use/tutorial.html)
[comamand quicklook](https://ld246.com/article/1556200452086#用-查看)


Ref:
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


