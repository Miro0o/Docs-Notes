# Insecure Deserialization

[TOC]



## Res
### Related Topics
↗ [Data Serialization & Deserialization](../../../../../🔑%20CS%20Core/🏎️%20Computer%20Networking%20and%20Communication/📌%20Computer%20Networking%20Basics%20(Protocol%20Part)/0x02%20Presentation%20Layer%20(Syntax%20Layer)/Data%20Serialization%20&%20Deserialization/Data%20Serialization%20&%20Deserialization.md)



## Intro



## Ref
[👍 全网最全详细的反序列化攻击知识梳理 | 大军安全]: https://mp.weixin.qq.com/s/F31ou2nfTfZrqPC9ab_IAA
1. 理解序列化和反序列化
2. PHP反序列化
	1. 什么是序列化与反序列化
	2. 序列化的概念
	3. 反序列化的概念
	4. 反序列化漏洞的产生
	5. 小试牛刀
	6. PHP魔术方法
		1. PHP讲以双下划线__保留为魔术方法，所有的魔术方法 必须 声明为 public。
		2. `__construct()`，类的构造函数
		3. `__destruct()`，类的析构函数
		4. `__call()`，在对象中调用一个不可访问方法时调用
		5. `__callStatic()`，用静态方式中调用一个不可访问方法时调用
		6. `__get()`，获得一个类的成员变量时调用
		7. `__set()`，设置一个类的成员变量时调用
		8. `__isset()`，当对不可访问属性调用`isset()`或`empty()`时调用  
		9. `__unset()`，当对不可访问属性调用`unset()`时被调用。  
		10. `__sleep()`，执行`serialize()`时，先会调用这个函数  
		11. `__wakeup()`，执行`unserialize()`时，先会调用这个函数  
		12. `__toString()`，类被当成字符串时的回应方法  
		13. `__invoke()`，调用函数的方式调用一个对象时的回应方法  
		14. `__set_state()`，调用`var_export()`导出类时，此静态方法会被调用。  
		15. `__clone()`，当对象复制完成时调用  
		16. `__autoload()`，尝试加载未定义的类  
		17. `__debugInfo()`，打印所需调试信息
3. 练习
	1. Hackthebox-Tenet
	2. 反序列化对象注入-CVE-2016-7124
