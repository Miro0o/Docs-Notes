# Troubleshooting

[TOC]



## ๐ [to get the type name of a variable in java: ](https://www.cnblogs.com/smuxiaolei/p/7692392.html)

> ref: https://sunilkanzar.wordpress.com/2017/11/11/wrapper-vs-primitive/

1. for variable of primitive class (็ฎๅ็ฑปๅๅ้), to access its type directly is not allowed; 
2. for variable of  [[0x03 OOP (java core)#Wrapper Class ๅ่ฃ็ฑปๅ https www liaoxuefeng com wiki 1252599548343744 1260473794166400|wrapper class ]](ๅ่ฃ็ฑปๅๅ้), use `.getClass().getName()` 



## ๐ lookup installed JDK

> ref:
>
> - https://blog.csdn.net/caoxiaohong1005/article/details/73611424
> - https://www.liaoxuefeng.com/wiki/1252599548343744/1280507291631649

... turned out i forgot to export JDK's path to `$PATH` . 

```shell
## ~/.zshrc : 

  47   โ
  48   โ ## export java path to env path
  49   โ ##export JAVA_HOME='/usr/libexec/java_home -v 17' ????
  50   โ export JAVA_HOME='/Library/Java/JavaVirtualMachines/jdk-17.0.2.jdk/Contents/Home'
  51   โ export PATH=$JAVA_HOME/bin:$PATH
  52   โ
โโโโโโโโดโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ
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



## ๐ [ไฝฟ็จideaไฟฎๆนjarๅๆบ็ ๅนถ้ๆฐๆๅ](https://blog.csdn.net/weixin_43178406/article/details/119037447) #unsolved

tbd.. 

