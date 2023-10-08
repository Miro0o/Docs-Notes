# Analytical Mathematics

[TOC]



## Res
🎬 数学分析 陈纪修老师 1080p高清版(全集) https://www.bilibili.com/video/BV15v411g7VP?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

🎬【数学分析陈纪修无障碍重制版】 https://www.bilibili.com/video/BV1sX4y1Y7jH/?p=3&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d

🎬 3blue1brown

📖 几米多维奇习题册 
📖 普林斯顿微积分读本
📖 工科数学分析基础 (马知恩，王绵森)

微积分之倚天宝剑（美）C.亚当斯等
微积分之屠龙宝刀（美）C.亚当斯等

微积分学教程(菲赫金哥尔茨第8版)
数学分析原理(Principles of Mathematical Analysis), Rudin

数学分析中的典型问题 裴

积分的方法与技巧（完整）

自然科学问题的数学分析 (B·A·卓里奇)



## Contents
### 1️⃣ Set Theory | Mapping | Function (集合，映射，函数)
↗ [Set Theory](../🤼‍♀️%20Mathematical%20Logics/Set%20Theory/Set%20Theory.md)
↗ [Set Theory Basics](../🤼‍♀️%20Mathematical%20Logics/Set%20Theory/📌%20Set%20Theory%20Basics/Set%20Theory%20Basics.md)


---
集合
- 集合定义：无序，无重
- 集合的表示
	- 枚举
	- 描述
- 集合的关系
	- 集合和元素的关系
		- 属于，
	- 集合和集合的关系
		- 包含，
		- 子集，超集，补集，幂集
- 集合和集合的运算法则
	- 初级交，初级并，相对补，对称差 （两个集合间）
	- 广义交，广义并 （N个集合间）
- 集合运算律（集合恒等式）
	- 14
- 特殊集合
	- 空集
		- 任何集合的子集
	- 全集
- 有限集/无限集合
- 可列集
	- 可列：不重复，不遗漏
		- （例）整数集Z是可列集
			- 易证
	- 可列个可列集并也是可列集合
		- 对角线法则
		- （例）有理数集合Q是可列集
			- $(+\infty, -\infty)$由可列个可列集合$(n,n+1]$的并构成，只要证 $(0,1]$ 有理数全体是可列集.
1. 

有序对 /笛卡尔积（卡氏积）/笛卡尔积集合
- $R^2 = R \times R$, 笛卡尔直角坐标系
- $R^3 = R \times R \times R$，笛卡尔空间直角坐标系

映射
- 映射的定义：集合间的一种对应关系（有序对）F,（x,y）
	- y:像, x:逆像
	- X: 定义域
	- Y: 值域
	- F: 映射规则，像的唯一性
- 映射的基本要素：
	- D(x):定义域
		- 单值，多值，
	- Z(y):值域
		- 单射，满射
	- f:对应规则
		- 逆映射，复合映射

函数
- 函数的定义：（特殊的映射关系）
	- 函数命名：X元X函数 （未知量个数，定义域集合）
		- （例）一元实函数
	- 定义域：自变量
		- 单值函数，多值函数
			- 单叶分支
		- 自然定义域：自变量的最大取值范围
			- （例）$log_ax: D=(0, +\infty)$
	- 值域：因变量
		- 单射，满射
	- 对应关系：
		- 逆函数，复合函数
		- ==基本初等函数==
			- 常函数
			- 幂函数
			- 指数函数
			- 对数函数
			- 三角函数
			- 反三角函数
		- 基本初等函数的推广
			- 初等函数
				- 由基本初等函数进行**有限次四则运算**和**复合运算**产生的函数
			- 高等函数
				- ...无限次运算...
		- 分段函数
			- （例）整数部分函数，非负小数部分函数
		- 符号函数
			- （例）Dirichlet函数
			- （例）Sigmoid 函数
- 函数的表示
	- 解析法
		- 显式表示（显函数）
			- $F(x) = y$
				- 基本初等函数及推广
				- 分段函数
				- 符号函数
		- 隐式表示（隐函数）
			- $F(x, y) = 0$
				- （例）Kepler方程：$y = x + \partial\sin{y}$
		- 参数表示
			- 引进参数t
				- $x = x(t), y = y(t)$
				- （例）：级坐标方程表示
				- （例）：旋轮线（摆线）
					- ![](../../../../../Assets/Pics/Screenshot-2023-10-05-at-11.20.50-PM.png)
	- 图像法
	- 表格法
- （下面的内容逻辑上应该在数列之后）
- ==函数的初等性质
	- 有界性
		- 上界，上确界
		- 下...
	- 单调性
		- 单调增加，严格单调增加
		- 减少...
	- 奇偶性
		- 奇: $F(-x) = -F(x)$
			- （例）双曲正弦函数：$y=f(x)=sh(x)=\frac{e^x+e^{-x}}{2}$
			- （例）双曲正切函数：$y=f(x)=th(x)=\frac{sh(x)}{ch(x)}$
		- 偶: $F(-x) = F(x)$
			- （例）双曲余弦函数：$y=f(x)=ch(x)=\frac{e^x-e^{-x}}{2}$
			- （例）双曲余切函数：$y=f(x)=cth(x)=\frac{ch(x)}{sh(x)}$
	- 周期性
		-  $x \in D, x + T \in D, F(x) = F(x+T)$
		- 最小周期T (基本周期，周期)
			- 是否周期函数都有最小周期T？
				- 否， (例) Dirichlet 周期
- ==重要不等式==
	- 三角不等式（证）
		- $|a| - |b| \leq |a+b| \leq |a| + |b|$
	- 平均值不等式 （证）
		- 算术平均：$\frac{a_1 + a_2 + a_3 + ... a_n}{n}$
		- 几何平均： $\sqrt{a_1a_2a_3...a_n}$
		- 调和平均：$\frac{n}{\frac{1}{a_1}+\frac{1}{a_2}+...+\frac{1}{a_n}}$
		- $\frac{a_1 + a_2 + a_3 + ... a_n}{n} \geq \sqrt{a_1a_2a_3...a_n} \geq \frac{n}{\frac{1}{a_1}+\frac{1}{a_2}+...+\frac{1}{a_n}}$
- ==三角函数恒等式==
	- 


### 2️⃣ Sequence of Number (数列)
↗ [Sequence of Number](Sequence%20of%20Number/Sequence%20of%20Number.md)
↗ [Algebraic Structure](../🧊%20Algebra/Algebraic%20Structure/Algebraic%20Structure.md)


---
数系的扩充 （回忆代数结构）
- 自然数集N：加法、乘法封闭
- 整数集Z：加法、减法、乘法封闭
	- 离散性
- 有理数集Q：加法、减法、乘法、除法封闭 (有限小数+无限循环小数)
	- 稠密性（无限分割），但有空隙
- (第一次数学危机)
	- 可公度：a，b是任意两线段的长度，则存在另一长度为c的线段，使得$a=mc, b=nc, \frac{a}{b} = \frac{m}{n}$
	- 正方形对角线不可公度！
	- （例）证明 $\sqrt2$ 不是有理数
		- 反证法：$\sqrt2 = \frac{p}{q}, \ p,q\in{Z}$
	- 几何上：数轴上存在有理数无法到达的点
- 实数集R：加法、减法、乘法、除法、根号 封闭 （有理数 + 无理数「无限不循环小数」）
	- 使得数轴完全填满
	- 连续性（实数连续统）
- 复数集

实数系的连续性
- 实数集合内的最大数与最小数
	- 有限非空集
		- 最大数
			- $S \subset R, \ S \neq \emptyset; \ if \ \exists C \in S, \ \forall{x}\in{S}, x \leq C, \ \to \text{C is the maxium in S}, \ C = \max{S}$
		- 最小数
			- 
		- 有限非空集合必有最大最小数
			- （证）反证法
	- 无限集
		- 不一定有最大最小数
			- （证）
- 实数集合的上界/下界
	- 上界：$S \subset R, \ S \neq \emptyset; \ if \ \exists M \in R, \ \forall{x}\in{S}, x \leq M$, 称M是S一个上界，或称S有上界
	- 下界：$S \subset R, \ S \neq \emptyset; \ if \ \exists m \in R, \ \forall{x}\in{S}, x \geq m$, 称m是S一个下界，或称S有下界
- 实数集合的上界集合/下界集合，上确界/下确界
	- 上界集合最大数/最小数，上确界
		- 设U 是集合S的上界集合，则U没有最大数；但是U一定有最小数，记为 $\beta=\sup{S}$，称为S的**上确界**。「确界存在定理（实数系连续性定理）」
		- $\beta \ \begin{cases}\beta \ 是上界&\forall{x}\in{S}, \ x \leq\beta \\ \beta=\sup{S}&\forall\varepsilon\gt0, \ \exists{x}\in{S}, \ x \gt \beta-\varepsilon \end{cases}$
	- 下界集合最大数/最小数，下确界
		- 设U 是集合S的下界集合，则U没有最小数；但是U一定有最大数，记为 $\alpha=\inf{S}$，称为S的**下确界**。「确界存在定理（实数系连续性定理）」
		- $\alpha \ \begin{cases}\alpha \ 是下界&\forall{x}\in{S}, \ x \geq\alpha \\ \alpha=\inf{S}&\forall\varepsilon\gt0, \ \exists{x}\in{S}, \ x \lt \alpha+\varepsilon \end{cases}$
- <a style="red">确界存在定理（实数系连续性定理）</a>
	- https://www.bilibili.com/video/BV1sX4y1Y7jH/?p=8&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
	- 定义：非空有上界的（实）数集必有上确界；非空有下界的（实）数集必有下确界。
	- 证明：
		- 设 $S \subset R, S \neq\emptyset, \ \text{S有上界}, \ S=\{a_0+0.a_1a_2...a_n... \vert \ a_0=[x], \ 0.a_1a_2...a_n...=(x), \ s\in{S}\}$
	- （例）$T=\{x \vert x\in{Q}, \ x\gt{0}, \ x^2\lt{2}\}, \ \text{则T在Q内没有上确界} \left(\sqrt{2}不是上确界，因为\sqrt{2}\notin{Q} \right)$
	- 

数列
- 数列的定义：特殊的离散函数（$Z^+ \to \text{some sets...}$）
- 数列的表示
	- 枚举
	- 表达式
	- 通项式
- ==数列的极限==
	- （例）圆周率$\pi$
		- 刘徽：使用圆内接正多边形的周长逼近圆的周长（$2\pi$）
		- "割值弥细，所失弥少；割之又割，以至于不可割，则与圆周合体而无所失矣。"
		- （见下“重要数列极限”）
	- 数列极限的定义
		- 邻域的定义
			- 
		- （柯西）
			- $lim_{n\to\infty}{x_n}=a, \ a\in{R}: \forall\varepsilon\gt0,\exists{N_0}\in{N}, \forall n\gt{N_0}, \vert x_n - a \vert \lt \varepsilon$
			- 若a存在，称$x_n$收敛于a；否则称其发散
		- （瓦尔）
			- ..
			- 若a存在，称$x_n$收敛于a；否则称其发散
		- (注意：数列收敛与否与数列前有限项无关)
		- ![](../../../Assets/Pics/Screenshot%202023-10-06%20at%2012.29.54%20AM.png)
		- 使用定义证明数列极限： $n \to \infty$ (放缩)
			- https://www.bilibili.com/video/BV1sX4y1Y7jH/?p=10&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
			- 基本初等函数
				- 常数函数
					- $lim_{n\to\infty}a$
				- 幂、指、对函数
					- ${n^2}$
					- ${\left(-1\right)^n}$
					- ${q^n, \ 0<\vert q \vert<1}$
						- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%204.51.50%20PM.png)
					- $lim_{n \to \infty}{\sqrt[n]{a}} = 1, a>1$
						- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%204.52.12%20PM.png)
				- 三角、反三角函数
					- 
			- 初等函数
				- 加减+基本初等函数（及其复合/求逆）
					- 略
				- 乘除+基本初等函数（及其复合/求逆）
					- ${\frac{n}{n+3}} \to 1$
					- ${\frac{1}{n}}$
					- $lim_{n\to\infty}{\sqrt[n]n = 1}$
						- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%204.52.29%20PM.png)
					- $lim_{n\to\infty}{\sqrt[n]{n^{k}} = 1}, \ k\in{N}$
					- $lim_{n\to\infty}{\frac{n^2+1}{2n^2-7n}}=\frac{1}{2}$
						- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%204.55.14%20PM.png)
					- $lim_{n\to\infty}{a_n} = a, \ lim_{n\to\infty}{\frac{a_1+a_2+...+a_n}{n}} = a$
						- 见下“重要不等式的数列极限”
				- 基本初等函数的复合/求逆
	- <a style="red">数列极限的性质</a>
		- 唯一性
			- $lim_{n\to\infty}{x_n}=a, lim_{n\to\infty}{x_n}=b \to a=b$
			- （证）
		- 有界性
			- $\exists{M}\in{R}, \ \forall{n}\in{N^+}\to x_n \leq M$: 称M为$\{x_n\}$上界，或称其有上界
			- $\exists{m}\in{R}, \ \forall{n}\in{N^+}\to x_n \geq m$: 称M为$\{x_n\}$下界，或称其有下界
			- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%205.11.32%20PM.png)
			- <a style="red">收敛数列必定有界</a> （有界不一定收敛；单调有界必收敛；见下“收敛准则”）
				- （证）
		- 保序性（实际上是前两个性质的推论）
			- 
			- ![](../../../Assets/Pics/Screenshot%202023-10-06%20at%2010.42.51%20AM.png)
			- 推论1: $if \ lim_{n\to\infty}{y_n = b \gt 0}, \ then \ \exists N, \forall n \gt N, y_n \gt \frac{b}{2} \gt 0$
			- 推论2: $if \ lim_{n\to\infty}{y_n = b \lt 0}, \ then \ \exists N, \forall n \gt N, y_n \lt \frac{b}{2} \lt 0$
			- 推论3: $if \ lim_{n\to\infty}{y_n = b \neq 0}, \ then \ \exists N, \forall n \gt N, \vert y_n \vert \gt \vert \frac{b}{2} \vert \gt 0$
	- ==收敛数列极限的重要计算方法==
		- <a style="red">夹逼定理</a>
			- （证）
			- （例）$lim_{n\to\infty}({\sqrt{n+1}-\sqrt{n})}$
			- （例）$lim_{n\to\infty}{(a_1^n + a_2^n + ... + a_p^n)^{\frac{1}{n}}} = \max{a_i}$
			- （例）$lim_{n\to\infty}{\sqrt[n]n = 1}$
				- $1 \lt \sqrt[n]{n} = \sqrt[n]{\sqrt{n}\sqrt{n}\cdot\underbrace{1\cdot1\cdot ... \cdot1}}_{n-2} \leq \frac{2\sqrt{n} + n -2}{n}$
			- （例）$lim_{n\to\infty}{\sqrt[n]{n^2} = 1}$
				- $1 \lt \sqrt[n]{n^2} = \sqrt[n]{\sqrt{n}\sqrt{n}\sqrt{n}\sqrt{n}\cdot\underbrace{1\cdot1\cdot ... \cdot1}}_{n-4} \leq \frac{4\sqrt{n} + n - 4}{n}$
		- <a style="red">单调有界数列必收敛</a>
			- （见下“收敛准则”）
	- <a style="red">收敛数列的四则运算（确定，有限）</a>
		- **前提：$x_n, \ y_n$ 极限均存在**，设 $lim_{n\to\infty}{x_n}=a, \ lim_{n\to\infty}{y_n}=b$，对其做**有限次**四则运算
			- $lim_{n\to\infty}({\alpha{x_n}+\beta{y_n}}) = \alpha a + \beta b$
				- （证）
			- $lim_{n\to\infty}({\alpha{x_n} \times \beta{y_n}}) = \alpha a \times \beta b$
				- （证）
			- $lim_{n\to\infty}{\frac{\alpha{x_n}}{\beta{y_n}}} = \frac{\alpha a}{\beta b}$
				- （证）
		- **初等函数**在数列极限上的**有限次**四则运算
			- $lim_{n\to\infty}{\frac{5^{n+1}-(-2)^n}{3\cdot5^n + 2\cdot3^n}} \to 1$
			- $lim_{n \to \infty}{\sqrt[n]{a}} = 1, a>0$
				- $\begin{cases}a \gt 1 & 已证 \\ a = 1 & 显然 \\ a \lt 1 & lim_{n\to\infty}{\frac{1}{\sqrt[n]{\frac{1}{a}}}} \end{cases}$
			- $lim_{n\to\infty}{n\cdot(\sqrt{n^2+1} - \sqrt{n^2-1})}$
			- ==重要不等式的数列极限== （$设 \ lim_{n\to\infty}{a_n} = a$）
				- 回顾重要不等式： $\frac{a_1 + a_2 + a_3 + ... a_n}{n} \geq \sqrt{a_1a_2a_3...a_n} \geq \frac{n}{\frac{1}{a_1}+\frac{1}{a_2}+...+\frac{1}{a_n}}$
				- $\frac{a_1 + a_2 + a_3 + ... a_n}{n}$
					- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%205.06.56%20PM.png)
					- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%205.07.04%20PM.png)
				- $\sqrt{a_1a_2a_3...a_n}$
				- $\frac{n}{\frac{1}{a_1}+\frac{1}{a_2}+...+\frac{1}{a_n}}$
			- ==其他一些重要极限==
				- （见下“收敛准则”）
		- **初等函数**在数列极限上的**无限次**四则运算：
			- $lim_{n\to\infty}({\frac{1}{\sqrt{n^2+1}}+\frac{1}{\sqrt{n^2+2}}+\frac{1}{\sqrt{n^2+3}}+...+\frac{1}{\sqrt{n^2+n}}})$
				- 夹逼
	- ==特殊的数列极限：无穷量==
		- 无穷量定义
			- $\infty$ 无穷大量 （正无穷大，负无穷大）
				- 定义：$\forall{G}\gt{0}, \ \exists{N_0}\in{N}, \ \forall{n}\gt{N_0}\to \vert{x_n}\vert\gt{G}$
					- 正无穷大量：$\forall{G}\gt{0}, \ \exists{N_0}\in{N}, \ \forall{n}\gt{N_0}\to {x_n}\gt{G}$
					- 负无穷大量：$\forall{G}\gt{0}, \ \exists{N_0}\in{N}, \ \forall{n}\gt{N_0}\to {x_n}\lt{-G}$
				- （例）$\vert{q}\vert\gt{1}, \ lim_{n\to\infty}{q^n}\to\infty$
				- （例）$lim_{n\to\infty}{\frac{n^2-1}{n+5}}\to\infty$
			- $0$ 无穷小量
				- 定义：
				- （例）
		- <a style="red">无穷量的性质</a>
			- $if \ x_n \neq 0, \ lim_{n\to\infty}{x_n} \to \infty \Leftrightarrow ( lim_{n\to\infty}{\frac{1}{x_n}} \to 0 )$
				- （证）
		- 无穷量运算
			- https://www.bilibili.com/video/BV1sX4y1Y7jH/?p=14&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
			- $lim_{n\to\infty}{\frac{a_0n^k+a_1n^{k-1}+a_3n^{k-2}+...+a_{k-1}n+a_k}{b_0n^l+b_1n^{l-1}+b_3n^{l-2}+...+b_{l-1}n+b_l}}, \ a_0,b_0 \neq 0, \ k,l\in{N^+}$
				- $lim_{n\to\infty}{[n^{k-l}\frac{a_0+\frac{a_1}{n}+\frac{a_2}{n^2}+...+\frac{a_k}{n^k}}{b_0+\frac{b_1}{n}+\frac{b_2}{n^2}+...+\frac{b_l}{n^l}}]}, \ \frac{a_0}{b_0}\neq0$
				- $=\begin{cases}\infty&k\gt{l}\\\frac{a_0}{b_0}&k=l\\0&k\lt{l}\end{cases}$
			- 无穷量运算类型
				- 确定型：
					- 
				- 待定型：
					- 
			- 无穷量运算法则
				- <a style="red">Stolz Theorm</a>
					- $\{y_n\}严格单增, \ lim_{n\to\infty}{+\infty}; \ if \ lim_{n\to\infty}{\frac{x_n-x_{n-1}}{y_n-y_{n-1}}}=a, \ (a\in{R}, \ +\infty, \ -\infty) \ then \ lim_{n\to\infty}{\frac{x_n}{y_n}}=a$
					- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%206.10.30%20PM.png)
					- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%206.10.48%20PM.png)
					- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%206.14.34%20PM.png)
					- （例）$lim_{n\to\infty}{\frac{1^k+2^k+3^k+...+n^k}{n^{k+1}}}$
					- （例）$lim_{n\to\infty}{a_n}=a, \ lim_{n\to\infty}{\frac{a_1+2a_2+3a_3+...+na_n}{n^2}}$
	- ==数列收敛准则==
		- 收敛数列有界，有界数列不一定收敛
		- <a style="red">单调有界数列必收敛</a>
			- （证）
			- （例）$x_1>0, \ x_{n+1}=1+\frac{x_n}{1+x_n}, \ n=1,2,3...$
				- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%206.41.19%20PM.png)
				- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%206.42.16%20PM.png)
			- （例）$0\lt{x_1}\lt{1}, \ x_{n+1}=x_n(1-x_n), \ lim_{n\to\infty}{x_n}=?$
				- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%207.49.31%20PM.png)
				- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%207.49.40%20PM.png)
			- （例）$x_1=\sqrt2, \ x_{n+1}=\sqrt{3+2x_n}, \ n=1,2,3... \ lim_{n\to\infty}{x_n}=?$
				- ![](../../../Assets/Pics/Screenshot%202023-10-07%20at%207.55.49%20PM.png)
			- （例）$x_1=\sqrt2, \ x_2=\sqrt{2+\sqrt2}, \ x_3=\sqrt{2+\sqrt{2+\sqrt2}}, ... \ lim_{x\to\infty}{\sqrt{2+x_{n-1}}} = ?$
		- 
	- ==重要收敛数列和其极限==
		- https://www.bilibili.com/video/BV15v411g7VP/?p=17&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
		- ⭐ Fabbinaci 数列
			- tbd..
		- ⭐ $\pi$  
			- 
		- ⭐ $e$ 
			- $lim_{n\to\infty}(1+\frac{1}{n}) \ \to e$
		- ⭐ 调和级数数列
			- $a_n=1+\frac{1}{2^p}+\frac{1}{3^p}+\frac{1}{4^p}+...+\frac{1}{n^p}, \ p \gt 0$
			- $\begin{cases}p\gt1&{a_n}收敛\\p=1&a_n调和级数\\0\lt{p}\lt{1}&{a_n\to\infty}\end{cases}$
	- 子数列的收敛性\*
		- 子数列定义：
		- 区间套定义：
		- 子数列性质：
			- <a style="red">子数列收敛的继承性</a>
				- 
			- <a style="red">区间套定理</a>
				- 
			- <a style="red">致密性定理（Bolzano-weierstrass Theorem）</a>
		- 
- 



### 3️⃣ Function (函数)
↗ [Function](../🤼‍♀️%20Mathematical%20Logics/Set%20Theory/Function/Function.md)

> 回顾第一部分关于函数的内容和数列的内容...

1. 函数定义
	1. 略
2. 函数初等性质
	1. 略
3. 函数初等运算
	1. 复合函数
		1. 定义：
		2. （例）
		2. （例）
		2. （例）
	2. 反函数
		1. 定义：
		2. 初等函数的反函数：
		3. <a style="red">反函数存在定理</a>
			1. 定义：
			2. 证明：
			3. （例）反双曲函数
				1. asdf
4. 基本初等函数和初等函数
	1. 略
5. ==函数极限/收敛函数==
	1. 函数极限定义 （收敛，发散）
		1. 单侧极限
		2. 双侧极限
		3. 渐近线
	2. <a style="red">收敛函数的性质</a>
		1. 唯一性
		2. 局部有界性
		3. 保序性
			1. 推论1
			2. 推论2
	3. 收敛函数的运算法则
		1. <a style="red">收敛函数的四则运算法则</a>
		2. <a style="red">收敛函数的复合运算法则</a>
	4. 函数极限与数列极限的关系
		1. <a style="red">海涅定理</a>
			1. （证）
			2. （例）$lim_{x\to\infty}\sin{\frac{1}{x}}$
	5. 收敛函数的判别准则/函数极限计算的重要方法
		1. <a style="red">夹逼定理</a>
			1. 定义：
			2. （证）
			3. （例）$lim_{x\to0}{\frac{\sin{x}}{x}}=1$
			4. （例）$lim_{x\to0}{\frac{1-\cos{x}}{x^2}}$
			5. （例）$lim_{x\to\infty}{(1+\frac{1}{x})^x}=e$
	6. ==重要收敛函数及其极限==
		1. $lim_{x\to0}{\frac{\sin{x}}{x}}=1$
			1. （证）
			2. ![Triangle_Inequity.excalidraw|150](../../../Assets/Ilustrations/Math/Triangle_Inequity.excalidraw.md)
			3. （例）
			4. ⚠ $lim_{x\to\infty}{\frac{\sin{x}}{x}}=0$
				1. $x\to\infty, \ -\frac{1}{x}\lt{\frac{\sin{x}}{x}}\lt\frac{1}{x}$
		2. $lim_{x\to\infty}{(1+\frac{1}{x})^x}=e, \ lim_{x\to0}{(1+x)^{\frac{1}{x}}}=e$
			1. （证）(数列 + 夹逼) 这里需要夹逼而不能直接说明由于 $x\to\infty, \ n\to\infty$，从而直接把数列的结论拿来用；这是因为我们此时的知识无法证明这两个无穷量在数列和实函数上的极限过程是相同的。
				1. $for \ \forall{x}\in{R}, \ \exists{n}, \ n \lt x \lt n+1; \ let \ x \to\infty , \ {(1+\frac{1}{n})^n} \lt {(1+\frac{1}{x})^x} \lt {(1+\frac{1}{n+1})^{n+1}}$
			2. （例）
	7. 无穷小量（虽然在数列部分也讨论过无穷量，但是区别在于此时讨论域属于实函数上而非数列）
		1. 无穷小量
		2. 无穷大量
			1. 无穷小量和无穷大量的关系
		3. 函数极限的无穷小量的表示
		4. 无穷小量的性质
		5. 无穷小量的比较
6. 函数的连续性


### 4️⃣ Derivative｜Differential Calculus (导数，微分)
↗ [Differential Calculus & Derivative](Differential%20Calculus%20&%20Derivative/Differential%20Calculus%20&%20Derivative.md)


### 5️⃣ 


### 6️⃣ Indefinite Integral (不定积分)
↗ [Indefinite Integral](Integral/Indefinite%20Integral/Indefinite%20Integral.md)


### 7️⃣ Definite Integral (定积分)
↗ [Definite Integral](Integral/Definite%20Integral/Definite%20Integral.md)


### 8️⃣ (反常积分)


### 9️⃣ (级数)


### 🔟 (函数项级数，幂级数)


### 1️⃣1️⃣ (级数)


### 1️⃣2️⃣ (偏导数，全微分)


### 1️⃣3️⃣ (重积分)


### 1️⃣4️⃣


### 1️⃣5️⃣ (欧拉积分)


### 1️⃣6️⃣ (傅立叶级数)



## Ref