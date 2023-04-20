# Troubleshooting

[TOC]



## 👉 Sleep in C| warning implicit declaration of function `sleep'?
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