# Q&A

## [Oracle JDK vs OpenJDK](https://stackoverflow.com/questions/22358071/differences-between-oracle-jdk-and-openjdk)

Both OpenJDK and Oracle JDK are created and maintained currently by Oracle only.

OpenJDK and Oracle JDK are implementations of the same Java specification passed the TCK (Java Technology Certification Kit).

Most of the vendors of JDK are written on top of OpenJDK by doing a few tweaks to [mostly to replace licensed proprietary parts / replace with more high-performance items that only work on specific OS] components without breaking the TCK compatibility.

Many vendors implemented the Java specification and got TCK passed. For example, IBM J9, Azul Zulu, Azul Zing, and Oracle JDK.

Almost every existing JDK is derived from OpenJDK.

As suggested by many, licensing is a change between JDKs. 

Starting with JDK 11 accessing the long time support Oracle JDK/Java SE will now require a commercial license. You should now pay attention to which JDK you're installing as Oracle JDK without subscription could stop working. [source](https://www.infoworld.com/article/3284164/java/oracle-now-requires-a-subscription-to-use-java-se.html)

Ref: *[List of Java virtual machines](https://en.wikipedia.org/wiki/List_of_Java_virtual_machines#Proprietary_implementations)*



## [public void main (String... args)](https://stackoverflow.com/q/1672083/16542494)

The `string[]` parameter is used to save command line arguments with first being the class name. Moreover, if you call your main method without `string[]` it will simply be an overload and JVM will not be calling that method.And if you skip this signature main method JVM will throw an exception.



## [import ](https://blog.csdn.net/qq_25665807/article/details/74747868)

1. import & import static 
`import` : targets _java-class or _interface_
`static import` : static member

> static import和import其中一个不一致的地方就是static import导入的是**静态成员**，而import导入的是**类或接口类型**。

2. single-type-import & type-import-on-demand (单类型导入&按需导入)

==type-import-on-demand (按需导入) has impact on compiling efficiency whereas not runtime efficiency.==

format : 
```java
import path.to.java-class

import path.to.parent.folder.*
```



## [System.getProperty()](https://www.tutorialspoint.com/system-getproperty-in-java)

```java
public static String getProperty(String key)
```
where `key` can be passed as : 
- file.separator

- java.specification.version

- java.vm.version

- java.class.path

- java.vendor

- java.class.version

- os.arch

- java.compiler

- line.separator

- java.version

- java.vendor.url

- os.name

  

###### `==` and `.equal()`

> Ref: https://www.geeksforgeeks.org/difference-between-and-equals-method-in-java/

`==` is for reference comparison
`.eaual()` is for content comparison



## [判断对象是否为null](https://www.cnblogs.com/DFX339/p/9945771.html) #unsolved

1. 对象存在实例，但是对象属性都为空 ``
2. 对象不存在实例 `Object == null`



## Parallel, Serial, Concurrency

- 并行(parallel)：指在同一时刻，有多条指令在多个处理器上同时执行。所以无论从微观还是从宏观来看，二者都是一起执行的。

- 串行(serial)：与并行(parallel)相对应，是指的我们从事某项工作时一个步骤一个步骤的去实施。

- 并发(concurrency)：指在同一时刻只能有一条指令执行，但多个进程指令被快速的轮换执行，使得在宏观上具有多个进程同时执行的效果，但在微观上并不是同时执行的，只是把时间分成若干段，使多个进程快速交替的执行。

  

## Further Readings ...

### Articles:

- [通俗易懂，什么是.NET?什么是.NET Framework？什么是.NET Core?](https://www.cnblogs.com/1996V/p/9037603.html)
- [CLR vs JVM：.NET和Java之间的争斗如何扩展到VM级别](https://blog.csdn.net/danpu0978/article/details/106767365)
- [模块依赖（Java9）](https://www.cnblogs.com/IcanFixIt/p/6994501.html)



