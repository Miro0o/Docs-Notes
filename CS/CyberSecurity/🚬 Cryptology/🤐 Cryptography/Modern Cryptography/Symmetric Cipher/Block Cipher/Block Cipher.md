# Block Cipher

[TOC]



## Res
↗ [Block Cipher Cryptanalysis](../../../../🤮%20Cryptanalysis/Modern%20Cipher%20Cryptanalysis/Symmetric%20Cipher%20Cryptanalysis/Block%20Cipher%20Cryptanalysis/Block%20Cipher%20Cryptanalysis.md)



## Intro
分组密码是每次只能处理特定长度的一块数据的算法，每块都是一个分组，分组的比特数就称为分组长度，但是当加密的内容超过分组密码的分组长度时，就要对分组密码算法进行迭代，迭代的方法称为分组密码的模式。



## 👩🏼‍🏫 Block Cipher Design Principles 
### Security Perspective
![](../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%202.40.51%20PM.png)

#### Diffusion
尽量将每一位明文和密钥的的影响尽可能迅速地分布到较多的输出密文位中，以便隐藏明文的统计特性。 扩散的目的是希望密文的任一位Ci都尽可能与明文和密钥相关联，或者说明文和密钥任一位上值的改变都会影响到Ci的值。

![](../../../../../../../Assets/Pics/Screenshot%202023-04-24%20at%203.39.30%20PM.png)

#### Confusion
使密文与明文、加密密钥之间的统计关系尽量复杂化，使破译者难以从密文的统计特性导出与密钥相关的信息。为此，可以使用与密钥和明文输入有关的很复杂的非线性算法。(实现时主要利用复杂的替换算法) 使用复杂的非线性代替变换可以达到比较好的混淆效果，而简单的线性代替变换得到的混淆效果则不理想。

> 扩散和混淆机制是现代分组密码的设计基础。
> 
> 乘积和迭代机制有助于实现扩散和混淆: 如通常选择某些较简单的受密钥控制的密码变换(替代-置换)，通过乘积和迭代可以取得比较好的扩散和混淆的效果


### Implementation Perspective 
![](../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%202.41.21%20PM.png)


### 🎲 Block Cipher Measure Metrics
对分组密码的评估主要有 3 个方面:(1)安全性;(2)性能;(3)算法和实现特性。

1. 安全性是评估中的最重要因素，包括下述要点:算法抗密码分析的强度，可靠的数学基础，算法输出的随机性，与其他候选算法比较的相对安全性。

2. 算法性能主要包括:在各种平台上的计算效率和对存储空间的需求。计算效率主要指算法在用软硬 件实现时的执行速度。

3. 算法和实现特性主要包括:灵活性、硬件和软件适应性、算法的简单性等。算法的灵活性指可以满 足更多应用的需求，如:
	1. 密钥和分组长度可以进行调整;
	2. 在许多不同类型的环境中能够安全和有 效地实现;
	3. 可以为序列密码、HASH 函数等的实现􏰂供帮助;
	4. 算法必须能够用软件和硬件两种方 法实现。另外，算法设计相对简单也是一个评估因素。



## ⭐ Block Cipher Crypto-systems
### Product Cipher + Iterative Cipher
当今绝大多数的分组密码都是乘积密码。所谓乘积密码，就是以某种方式连续执行两个或多个密码，以使得所得到的最后结果或乘积比其任意一个组成密码都更强。乘积密码通常伴随一系列置换与代换操作，常见的乘积密码是迭代密码，即对同一种密码进行迭代使用。

![](../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%202.41.40%20PM.png)


![](../../../../../../../Assets/Pics/Screenshot%202023-04-12%20at%202.41.50%20PM.png)



### ⭐️ Block Cipher Design Models
↗ [Block Cipher Design Models](📌%20Block%20Cipher%20Design/Block%20Cipher%20Design%20Models.md)



### 🎯 Block Cipher Implementations
↗ [DES (Data Encryption Standard)](DES%20(Data%20Encryption%20Standard)/DES%20(Data%20Encryption%20Standard).md)
↗ [AES (Advanced Encryption Standard)](AES%20(Advanced%20Encryption%20Standard)/AES%20(Advanced%20Encryption%20Standard).md)
↗ [IDEA (International Data Encryption Algorithm)](IDEA(International%20Data%20Encryption%20Algorithm)/IDEA%20(International%20Data%20Encryption%20Algorithm).md)
↗ [RC5](RC/RC5.md)



## Ref
[密码学 分组密码模式]: https://www.secpulse.com/archives/173833.html


