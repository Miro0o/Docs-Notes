# 复数的引入和数域的扩充

> https://www.cnblogs.com/jy333/p/14351472.html

###### 复数（complex number）
一个复数是一个有序数对 $(a, b) = a + bi$ , 其中 $a,b \in R$
$C = \{a + bi: a,b \in R\}$
定义复数的加法和乘法

![[Screen Shot 2022-03-02 at 5.13.45 PM.png]]
 
设 $µ = a + bi \in C, ß = c + di \in C$
对于任意 $µ$, 使得 $µß = 1$ 的 $ß$ 满足：
$c = \frac{a}{b^2 + a^2} , d = \frac{-b}{b^2+a^2}$


x 存在且唯一：
1. 0 存在且唯一
2. x 存在且唯一

![[Screen Shot 2022-02-26 at 5.03.34 PM.png]]


###### 数域 filed : 
F 是一个集合，包含 加法运算 和 乘法运算。
定义 F 的加法运算 和 乘法运算。

F 上的加法（addition）：
1. 加法交换律
2. 加法结合律
3. 加法单位元
4. 加法逆元

F 上的乘法（multiplication）：
1. 乘法交换律
2. 乘法结合律
3. 乘法分配律
4. 乘法单位元
5. 乘法逆元*

###### 组 （list），长度（length）
组是长度为n 的有序元素。其中 n 是有限维。

###### $F^n, R^n, C^n$
长度为n的组的元素集合是 $F^n$ 




# 向量空间 
vector space (V) : addition & scalar multiplication close


###### 向量空间 V 及性质
向量空间（vector space）就是带有如下性质的集合 V :

- V上的加法（addition）：$u,v \in V, u+v = v \in V$
- V上的标量乘法（scalar multiplication）：$k \in F, u \in V, ku = v \in V$

- V上的运算律：（运算对象均为 $u,v \in V$）
	1. 加法交换性 （commutativity）
	2. 加法结合性 （associativity）
	3. 加法单位元（additive identity）
		1. 加法单位元存在唯一：
			1. 加法
	4. 加法逆元（additive inverse）
		1. 加法逆元存在唯一：
	5. 乘法单位元（multiplicative identity）
	6. 分配性质（distributive properties）
		1. ==标量乘法分配== 其中标量属于 F 
			1. **real vector space :** V 是 R 上的向量空间
			2. **complex vector space :** V 是 C 上的向量空间
		2. 向量乘法分配


- V 上的一些性质：
	设 $v\in V$ :
	数 -1 乘以向量:  $(-1)\times v = -v$
	数 0 乘以向量: $0\times v = 0$
	标量乘以 0向量: $u\times 0 = 0$

> 向量转化为数量的表示形式，然后利用向量空间的运算




###### 子空间（subspace）
Def： 若 ⓵ U 是向量空间 ，⓶ U 是 V 的子集 ，⓷V上的运算性质在 U 上也成立，则 U 是 V 的子空间
	$\iff$
U 满足：
1. ==加法单位元（additive identity）==
2. 加法封闭性 （closed under addition）
3. 标量乘法封闭性（closed under scalar multiplication）
	$\iff$
U 非空

![[Screen Shot 2022-02-26 at 9.49.41 PM.png]]


$R^2$ 的子空间：$\{0\}$, $\{R^2, 过原点的所有直线\}$
$R^3$ 的子空间：$\{0\}$, $\{R^3, 过原点的所有平面\}$

> 最近在看线性代数，对于其中子空间(subspace)的概念很是不理解？ - 破魔之箭的回答 - 知乎 https://www.zhihu.com/question/48849797/answer/115314179

![[Screen Shot 2022-03-02 at 5.26.49 PM.png]]

子集的和（sum of subset）：
子空间的和： 各个子空间的一组线性无关的基向量所构成一个空间，是一个线性子空间。
子空间的和是包含这些子空间的最小子空间
[线性子空间的交、并、和、维数与直和等各种关系总结](https://blog.csdn.net/xiaohen123456/article/details/82856523)


###### 直和（direct sum）
有 $U_1, U_2,... U_n \subset V^n$ ，且对于他们的和 $U_1 + U_2 +... U_n = V^n_n$ , 有唯一的 $a = u_1 + u_2 + ... + u_n \in V^n_n$ , 其中 $u_1 \in U_1, u_2 \in U_2 ,... u_n \in U_n$ , 则称 $V^n_n$ 为 $U_1, U_2,... U_n \subset V^n$ 的直和

> 个人理解：各元素线性无关，其基向量相加之和


![[Screen Shot 2022-03-02 at 9.59.29 PM.png]]



![[Screen Shot 2022-02-27 at 11.37.05 AM.png]]


