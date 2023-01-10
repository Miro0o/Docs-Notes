# FAQ

[TOC]



> :warning: This file was writen in early time. Contents may be sketchy & missing.



##  diffs btween[new/delete -- malloc/free](https://stackoverflow.com/questions/240212/what-is-the-difference-between-new-delete-and-malloc-free)

> *p = new int / int p ??
> see [[顺序表和链表#^f56a27| malloc]]

```c++
void* malloc (size_t size);
```

```c++
int main(){
 	int *a; int M = 10;
	a = (int *) malloc(M);			
	cout<<"sizeof(a) == "<< sizeof(a)<<endl;	//a是指针，a本身大小永远是一个指针的大小8byte 
	for(int i=0;i<M;i++) a[i] = i;
	for(int i=0;i<M;i++) cout<<" "<<a[i];
	
	return 0;
}

```



## 异或运算

不进位加法。相同为0，不同为1。



## 😡 Char initialize （字符数组初始化）:

```c++
char parr[] = "zifuchuanshuzu";
    //⬆️ 与charr_test[]等价,字符串末尾有\n
char charr_test[] = { 'z','i','f','u','c','h','u','a','n','s','h','u','z','u' ,'\0'};	
char charr[] = { 'z','i','f','u','c','h','u','a','n','s','h','u','z','u' };
 // ⬆️ 字符串末没有 \n
```



## binary/ hex/ oct output（格式控制输出）:

+ bitset

```c++
  	cout<<hex<<n<<endl;        // 输出 16 进制
    cout<<oct<<n<<endl;		   // 输出 8 进制
	
	bitset<8> n(15);			// 二进制使用补码输出
	cout<<n.to_string()<<endl;
	bitset<8> b(-13);
	cout<<b.to_string()<<endl; 
```


## **auto** 关键字

> + [c.biancheng 中文教程](http://c.biancheng.net/view/6984.html)
> + [microsoft docs](https://docs.microsoft.com/en-us/cpp/cpp/auto-cpp?view=msvc-160) 
+ `auto` is a kind of spaceholder. the compiler replace this command with the right specifier it concluded form the text. and ⚠️ **NOTICE** that in c/c++ any variable MUST have a specific type. 



## **sizeof()**

+ 不是函数，预编译阶段已经算出大小



## [strtol](https://blog.csdn.net/S031302306/article/details/52060914)

+ cstdlib
	```c++
	long strtol(const char *__str, char **__endptr, int __base);
	```
+ `__str` 是目标串，`__endpter`是结束地址。base是指定的合法数字的范围。
+ base = 0 时合法数字0 ～ 9
+ base = n (n≠0) 时 合法数字 0～n



##  [range-based for loop](https://en.cppreference.com/w/cpp/language/range-for)

+ see on [stackflow](https://stackoverflow.com/questions/12702561/iterate-through-a-c-vector-using-a-for-loop) 

	```c++
	attr(optional) for (init-statement(optional);range-declaration: range-expression ){
	
		loop-statement
	
	}
	
	// e.g.
	
	int a[M_size];
	for(int &i:a){
		cout<<i<<endl;
	}
	```



## [Union](https://blog.csdn.net/lincyang/article/details/6176642)





## [enum](https://www.runoob.com/cprogramming/c-enum.html)





## [typedef](http://c.biancheng.net/view/298.html)

+ typedef _originaltype _wantedtype
	+ e.g.
		>  typedef int INT_ARRAY_100[100];
		>  INT_ARRAY_100 arr;
+ 考虑如下语句：
> typedef char* PCHAR;
> int strcmp(const PCHAR,const PCHAR);

+  其中 ```const PCHAR = const (char*) ≠ const char* = (const char)* ```
	+ 前者声明链PCHAR指针本身的const属性，后者声明了指针指向元素的const属性
+ typedef 属于*[存储类关键字](https://blog.csdn.net/shenwanjiang111/article/details/78340722)*
	+  其他：auto、extern、static、 register、thread_local
	+  >  typedef static int INT_STATIC;
	+  故上述代码不成立，VC++2010 中的报错信息为“无法指定多个存储类”。
	



##  [endl&\n](https://www.jianshu.com/p/2c0c72f4fde7)

**关于 endl与'\n' 区别**:

-   1、在 C++ 中，终端输出换行时，用 cout<<......<<endl 与 "\n" 都可以，这是初级的认识。但二者有小小的区别，用 endl 时会刷新缓冲区，使得栈中的东西刷新一次，但用 "\n" 不会刷新，它只会换行，盏内数据没有变化。但一般情况，二者的这点区别是很小的，在大的程序中可能会用到。建议用 endl 来换行。
    
-   2、endl 除了写 '\n' 进外，还调用 flush 函数，刷新缓冲区，把缓冲区里的数据写入文件或屏幕.考虑效率就用 '\n'。
    
-   3、cout *lt;< endl; 除了往输出流中插入一个 '\n' 还有刷新输出流的作用。
    

```c
cout << endl; 
等价于: 
cout << '\n' << flush;

```

**在没有必要刷新输出流的时候应尽量使用 cout << '\n', 过多的 endl 是影响程序执行效率低下。**



## rand&srand
+ http://c.biancheng.net/view/2043.html
+ rand() 是伪随机函数。她是符合一种正态分布，根据固定的种子值有固定的随机树。
+ srand可以用来重新生成这个种子数。



## [编译/链接/运行](https://blog.csdn.net/ASJBFJSB/article/details/81252308)
> see more:
	> [bilibili](https://www.bilibili.com/video/BV1pf4y1J7YF?from=search&seid=8872179399538554368&spm_id_from=333.337.0.0) (pretty much detailed & instructive)
	> [csdn](https://blog.csdn.net/jsjsjs1789/article/details/103305529)
	> [csdn](https://blog.csdn.net/qq_37753409/article/details/82026613)
+ VFS (virtual file system)
+ programme = command + data
+ virtual address space
	+ ALU	
	+ .data .bss .text
+ **1. Compile**
	>.c/.cpp/.h --> .o/.obj (二进制可重定位文件)
	+ pre-compile `gcc -E *.c -o *.i` 
		+ windows --> .obj
		+ linux --> .o
	+ compile `gcc -S *.i -o *.s`
	+ assembly `gcc -c *.s -o *.o`
+ **2. Link**
	> .o/.obj/.lib --> .exe/.dll
+   **3.Build**




## [指针 Pointer](https://www.cnblogs.com/tongye/p/9650573.html)
+  内存地址/内存空间编码
	+ ALU, 步长
+ 语法
	+ ``` *p[N] <--> (*P)[N] ```
+ 指针与数组/结构体/函数/指针（双指针）




## [*C++ios](https://zhuanlan.zhihu.com/p/352961501)
> 目前仅作了解



## STL
+ [strcpy/strncpy](https://blog.csdn.net/lanzhihui_10086/article/details/39827729)



## [conio.h](https://stackoverflow.com/questions/59812014/why-use-conio-h)

conio stands for console i/o, is built on MSVC and has DOS specs. it is referable for win coding. 

The conio.h header is specific to Turbo C, which predates the earliest C standard by several years. It contains routines that are specific to the DOS command line. One function here that's frequently used is `getch`, which allows reading one character at a time without having to press the Enter key. It also contains `gotoxy` which allows placing the cursor at a specific location in the terminal

Generally speaking, methods of communicating with the terminal like this are very OS specific, so each has their own (typically non-portable) way of doing it.

This contrasts with the functions in stdio.h which contain functions like `printf`, `scanf`, and `getchar` which work regardless of what type of console is in use.



## [time.h](https://blog.csdn.net/qq_36667170/article/details/79507547)

clock()
CLOCKS_PER_SEC



## [文件读写模式控制符](https://www.cnblogs.com/acode/p/5986958.html)

 + r / r+
 + w/ w+
 + a / a+
 + 

 