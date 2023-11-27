# Definite Integral

[TOC]



## Res


## Contents
### 定积分的引入和定义
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
		1. 阿斯顿发
2. 定积分的定义：
	1. 黎曼可积（可积）：
		1. ![](../../../../Assets/Pics/Screenshot%202023-11-27%20at%2011.22.18AM.png)
		2. ![](../../../../Assets/Pics/Screenshot%202023-11-27%20at%2011.23.48AM.png)
		3. ![](../../../../Assets/Pics/Screenshot%202023-11-27%20at%2011.33.10AM.png)
### （黎曼）可积性的判断
【数学分析 陈纪修老师 1080p高清版(全集)】 https://www.bilibili.com/video/BV15v411g7VP/?p=77&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
1. 达布和：
	1. 定义
		1. ![](../../../../Assets/Pics/Screenshot%202023-11-27%20at%2011.44.04AM.png)
2. 达布和引理：
	1. 


### 定积分的计算
#### 变限积分
1. 阿斯顿
2. 变限积分应用：
	1. 证明不等式：（将不等式化为变限积分，然后考虑导数性质）
	2. 
##### 牛顿-莱布尼茨公式
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



## Ref
