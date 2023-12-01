# Definite Integral

[TOC]



## Res


## Contents
### （黎曼积分）定积分的引入和定义
1. 定积分的引入
	1. 【数学分析 陈纪修老师 1080p高清版(全集)】 https://www.bilibili.com/video/BV15v411g7VP/?p=75&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
	2. 开普勒三大定律；求椭圆中向径划过的面积：（极限+夹逼）
		1. x等分，y取最小矩形高和最大矩形高,$\Delta{x_i}=\frac{1}{n}\to0$
			1. ![](../../../../Assets/Pics/Screenshot%202023-11-23%20at%2010.55.43AM.png)
			2. ![](../../../../Assets/Pics/Screenshot%202023-11-23%20at%2010.58.57AM.png)
		2. x不等分，y取随便一个中间值 -> $\lambda=max{x_i}\to{0}$
			1. 【数学分析 陈纪修老师 1080p高清版(全集)】 https://www.bilibili.com/video/BV15v411g7VP/?p=76&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
			2. ![](../../../../Assets/Pics/Screenshot%202023-11-27%20at%2011.16.06AM.png)
	3. 求运动物体的运动路程
		1. etc..
2. 定积分的定义：
	1. 黎曼可积（可积）：
		1. ![](../../../../Assets/Pics/Screenshot%202023-11-27%20at%2011.22.18AM.png)
		2. ![](../../../../Assets/Pics/Screenshot%202023-11-27%20at%2011.23.48AM.png)
		3. ![](../../../../Assets/Pics/Screenshot%202023-11-27%20at%2011.33.10AM.png)

### （黎曼）可积性的判断 (skip)
【数学分析 陈纪修老师 1080p高清版(全集)】 https://www.bilibili.com/video/BV15v411g7VP/?p=77&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d 
1. 达布和：
	1. 定义
		1. ![](../../../../Assets/Pics/Screenshot%202023-11-27%20at%2011.44.04AM.png)
2. 达布和引理：
	1. tbd..


### 定积分的基本性质
【数学分析 陈纪修老师 1080p高清版(全集)】 https://www.bilibili.com/video/BV15v411g7VP/?p=78&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

1. （加法/标量乘法）线性性（证明：由于定积分运算等价于对应的R上数求和的运算，利用R上数的线性性可知定积分运算的线性性）
	1. 推论：F在\[a,b\]上可积，G在\[a,b\]上和F只有有限个点取值不同，则G可积且和F积分相同。
	2. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%209.41.52AM.png)
	3. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%209.47.07AM.png)
3. 乘积可积性
	1. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%209.50.09AM.png)
	2. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%209.49.45AM.png)
4. 保序性
	1. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%209.51.46AM.png)
5. 绝对可积性
	1. 注意：F可积->|F|可积，但是反推不成立
		1. 例：$f=\begin{cases}1,&x有理数\\-1,&x无理数\end{cases}$
	2. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%209.56.23AM.png)
6. 区间可加性
	1. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%2010.02.50AM.png)
	2. tbd...
7. 积分第一中值定理
	1. https://www.bilibili.com/video/BV15v411g7VP/?p=81&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d&t=227
	2. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%2010.15.52AM.png)
		1. 考虑g(x)=1:
			1. $\int^{b}_{a}f(x)g(x)dx=\begin{cases}\theta(b-a)&f可积\\f(\theta)(b-a)&f连续\end{cases}$
	3. （例）
		1. tbd..
	4. 


### 定积分的计算
#### 微积分基本定理（牛顿-莱布尼茨公式）
【数学分析 陈纪修老师 1080p高清版(全集)】 https://www.bilibili.com/video/BV15v411g7VP/?p=82&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
##### 变限积分
1. 阿斯顿
2. 变限积分应用：
	1. 证明不等式：（将不等式化为变限积分，然后考虑导数性质）

#### 只有有限个间断点的有界函数的定积分

#### 定积分的积分法
##### 定积分的换元法
##### 定积分的分部积分法
#### 常用的定积分恒等式
1. $\int^{\frac{\pi}{2}}_{0}f(\sin{x})dx=\int^{\frac{\pi}{2}}_{0}f(\cos{x})dx, \ \int^{\pi}_{0}{x\cdot{f(\sin{x})}}dx=\frac{\pi}{2}\int^{\pi}_{0}f(\sin{x})dx$ (注意这里的积分限)
2. $\int^{\frac{\pi}{2}}_{0}\sin^n{x}dx=\int^{\frac{\pi}{2}}_{0}\cos^n{x}dx=\begin{cases}\frac{n-1}{n}\cdot\frac{n-3}{n-2}\cdot...\frac{3}{4}\cdot\frac{1}{2}\cdot\frac{\pi}{2} & n为偶数 \\ \frac{n-1}{n}\cdot\frac{n-3}{n-2}\cdot...\frac{4}{5}\cdot\frac{2}{3} & n为奇数 \end{cases}$
	1. $\int^{\frac{\pi}{2}}_{0}\sin^4{x}dx=\frac{3}{4}\cdot\frac{1}{2}\cdot\frac{\pi}{2}=\frac{3\pi}{16}$
	2. $\int^{\pi}_{0}\sin^4{x}dx=2\int^{\frac{\pi}{2}}_{0}\sin^4{x}dx=\frac{3\pi}{8}$ (结合几何意义，没有普遍性)
3. 奇函数和偶函数在关于0对称的区间上求定积分：偶倍奇零
4. 非奇/偶函数在关于0对程的区间上求定积分：
5. 周期函数在一个周期长度内求定积分：$\int^{a+T}_{a}f(x)dx=\int^{T}_{0}f(x)dx=\int^{\frac{T}{2}}_{-\frac{T}{2}}f(x)dx, \ \int^{a+nT}_{a}f(x)dx=n\int^{a+T}_{a}f(x)dx$

#### 定积分数值计算
1. 【数学分析 陈纪修老师 1080p高清版(全集)】 https://www.bilibili.com/video/BV15v411g7VP/?p=93&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
2. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%203.47.56PM.png)
3. 梯形公式（插值多项式，1点）
	1. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%203.48.49PM.png)
4. Simpson公式（插值多项式，2点）
	1. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%203.50.56PM.png)
5. 复化梯形公式
	1. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%203.54.29PM.png)
6. 复化Simpson公式
	1. ![](../../../../Assets/Pics/Screenshot%202023-11-29%20at%203.55.50PM.png)
#### 反常积分
↗ [Improper Integral](Improper%20Integral.md)


### 定积分应用
#### 定积分在几何计算中的应用
【数学分析 陈纪修老师 1080p高清版(全集)】 https://www.bilibili.com/video/BV15v411g7VP/?p=86&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
##### 平面图形的面积
##### 平行截面面积为已知的立体的体积
##### 平面曲线的弧长
#### 微积分实际应用
【数学分析 陈纪修老师 1080p高清版(全集)】 https://www.bilibili.com/video/BV15v411g7VP/?p=91&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d



## Ref
