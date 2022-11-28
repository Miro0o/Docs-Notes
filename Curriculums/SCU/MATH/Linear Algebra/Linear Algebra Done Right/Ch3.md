# 线性映射

### 映射（map）
###### 函数映射（Function）线性/非线性
1. 定义域
2. 对映方法
3. 一一对映（对于定义域上每一个元素，都有唯一的值域元素与之对映）

> 这里注意的是，range（T）= W 是称为满的（surjective）

### 线性映射
![[Screen Shot 2022-03-30 at 8.09.21 PM.png]]

![[Screen Shot 2022-03-14 at 10.38.11 AM.png]]

一些特殊的线性映射： 
1. 零映射
2. 恒等映射
3. 微分映射
4. 向后位移（backward shift）映射
5. ⭐️ ==从 $F^n$ 到$F^m$ 的映射==



![[Screen Shot 2022-03-14 at 11.19.06 AM.png]]
线性映射的线性运算定义的合理性：
1. 唯一性
2. 封闭性
3. 线性映射是良定义的（即线性映射间的运算结果仍是线性映射）

![[Screen Shot 2022-03-14 at 11.05.15 AM.png]]


> 两个映射T和S相等 等价于 对于任意v，Tv = Sv



![[Screen Shot 2022-03-14 at 11.24.07 AM.png]]
即对于 $t, l \in Ĺ(V,W)$ 满足八大性质。

由此引出线性映射的乘积： （感觉更像是线性映射的嵌套）

![[Screen Shot 2022-03-30 at 8.35.21 PM.png]]

由于线性映射的线性运算性质，有 3.11： 
![[Screen Shot 2022-03-30 at 8.41.02 PM.png]]


# 子空间和值域
![[Screen Shot 2022-03-30 at 8.43.56 PM.png]]
![[Screen Shot 2022-03-30 at 8.46.03 PM.png]]

零空间是子空间。

![[Screen Shot 2022-03-30 at 8.52.14 PM.png]]
![[Screen Shot 2022-03-30 at 8.51.05 PM.png]]

值域（Range）
值域是子空间


![[Screen Shot 2022-03-30 at 8.56.11 PM.png]]

![[Screen Shot 2022-03-13 at 4.55.45 PM.png]]

![[Screen Shot 2022-03-30 at 8.57.54 PM.png]]
![[Screen Shot 2022-03-30 at 9.04.52 PM.png]]

一些推论。。。

![[Screen Shot 2022-03-30 at 9.05.13 PM.png]]

# 线性映射的矩阵
![[Screen Shot 2022-03-30 at 10.01.57 PM.png]]

线性映射 $T \in L(V, W)$ 的意义是定义了空间V 到空间 W 的映射方式； 从微观上看，这种映射反应为空间的基的映射关系，即，确定了V 的每一个基到W 的每一个基的映射。于是线性映射 T 的矩阵 $M(T)$  则表示了这种基对基的映射方式。

> 为什么要竖着写 https://www.bilibili.com/video/BV1Vg411G7cz?p=26&t=508.6

![[Screen Shot 2022-03-30 at 9.16.53 PM.png]]
矩阵M 是线性的
矩阵M 是向量空间

![[Screen Shot 2022-03-30 at 10.18.32 PM.png]]

类比线性映射乘法，
![[Screen Shot 2022-03-30 at 10.20.13 PM.png]]

# 逆
![[Screen Shot 2022-04-06 at 4.01.32 PM.png]]

![[Screen Shot 2022-04-06 at 4.01.57 PM.png]]



# 同构
![[Screen Shot 2022-04-06 at 4.03.17 PM.png]]
![[Screen Shot 2022-04-06 at 4.03.36 PM.png]]



###### 矩阵同构
![[Screen Shot 2022-04-06 at 3.51.21 PM.png]]

矩阵和线性映射等价

![[Screen Shot 2022-04-06 at 3.53.07 PM.png]]



![[Screen Shot 2022-04-06 at 3.59.25 PM.png]]

![[Screen Shot 2022-04-06 at 3.59.14 PM.png]]
![[Screen Shot 2022-04-06 at 3.59.48 PM.png]]



# 算子（operator）和可逆算子
![[Screen Shot 2022-04-06 at 3.12.42 PM.png]]

![[Screen Shot 2022-04-06 at 3.13.05 PM.png]]


# 向量空间的乘积
![[Screen Shot 2022-04-06 at 5.00.36 PM.png]]
![[Screen Shot 2022-04-06 at 5.04.49 PM.png]]

![[Screen Shot 2022-04-06 at 5.05.44 PM.png]]

# 向量空间的商
![[Screen Shot 2022-04-11 at 4.08.47 PM.png]]

![[Screen Shot 2022-04-11 at 1.10.58 PM.png]]
![[Screen Shot 2022-04-11 at 4.10.36 PM.png]]
![[Screen Shot 2022-04-11 at 4.12.03 PM.png]]
![[Screen Shot 2022-04-11 at 4.15.40 PM.png]]
V/U满足八大性质 ： https://www.bilibili.com/video/BV1Vg411G7cz?p=37&t=2201.2

![[Screen Shot 2022-04-11 at 4.20.27 PM.png]]

![[Screen Shot 2022-04-11 at 4.27.17 PM.png]]
![[Screen Shot 2022-04-11 at 4.33.18 PM.png]]
1. 线性
	1. 加性
	2. 齐性
2. 单性
3. 满性


![[Screen Shot 2022-04-11 at 4.39.14 PM.png]]

