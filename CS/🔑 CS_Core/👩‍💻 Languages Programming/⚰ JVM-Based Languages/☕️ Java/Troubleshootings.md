# Troubleshooting

[TOC]



## 👉 [to get the type name of a variable in java: ](https://www.cnblogs.com/smuxiaolei/p/7692392.html)

> ref: https://sunilkanzar.wordpress.com/2017/11/11/wrapper-vs-primitive/

1. for variable of primitive class (简单类型变量), to access its type directly is not allowed; 
2. for variable of  [[📌 Java Basics/0x03 OOP (java core)#Wrapper Class 包装类型 https www liaoxuefeng com wiki 1252599548343744 1260473794166400|wrapper class ]](包装类型变量), use `.getClass().getName()` 



## 👉 lookup installed JDK

> ref:
>
> - https://blog.csdn.net/caoxiaohong1005/article/details/73611424
> - https://www.liaoxuefeng.com/wiki/1252599548343744/1280507291631649

... turned out i forgot to export JDK's path to `$PATH` . 

```shell
## ~/.zshrc : 

  47   │
  48   │ ## export java path to env path
  49   │ ##export JAVA_HOME='/usr/libexec/java_home -v 17' ????
  50   │ export JAVA_HOME='/Library/Java/JavaVirtualMachines/jdk-17.0.2.jdk/Contents/Home'
  51   │ export PATH=$JAVA_HOME/bin:$PATH
  52   │
───────┴─────────────────────────────────────────────────────────────────────────────────────────────
(base) mir0@fkSCU ~ % java --version
java 17.0.2 2022-01-18 LTS
Java(TM) SE Runtime Environment (build 17.0.2+8-LTS-86)
Java HotSpot(TM) 64-Bit Server VM (build 17.0.2+8-LTS-86, mixed mode, sharing)
(base) mir0@fkSCU ~ % whereis java
/usr/bin/java
(base) mir0@fkSCU ~ % whereis jmod
(base) mir0@fkSCU ~ % which jmod
/Library/Java/JavaVirtualMachines/jdk-17.0.2.jdk/Contents/Home/bin/jmod
```



## 👉 [使用idea修改jar包源码并重新打包](https://blog.csdn.net/weixin_43178406/article/details/119037447) #unsolved

tbd.. 

