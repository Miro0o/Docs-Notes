# Spectre & Meltdown

[TOC]



## Res


## Intro


## Ref
[👍 科普幽灵(Spectre) 与熔断(Meltdown)以及自测方法]: https://blog.sciencenet.cn/blog-684007-1093420.html

刚在网上看了一些文章试图解释最近发现的计算机处理器硬件安全漏洞，有些文章笼统把幽灵(Spectre) 与熔断(Meltdown) 混为一谈。其实这两者非常不同。
- 熔断是 INTEL 特有的缺陷，是 INTEL处理器设计中允许猜测性非法访问的严重错误，熔断漏洞很容易被利用。
- 幽灵(Spectre) 缺陷则是利用所谓间接分叉预测 （indirect branch prediction --- IBP）。幽灵缺陷存在许多不确定因素，要利用相对困难许多。

[熔断漏洞原理与解决方案]: https://www.cnblogs.com/kvm-qemu/articles/8284508.html

[👍 浅谈熔断和幽灵]: https://www.wenhui.space/docs/08-ic-design/cpu/meltdown-and-spectre/#%E9%87%8D%E8%A6%81%E6%A6%82%E5%BF%B5
![](../../../../../Assets/Pics/Pasted%20image%2020240105135937.png)
