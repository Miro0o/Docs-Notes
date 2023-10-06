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
- 映射：集合间的一种对应关系（有序对）F,（x,y）
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
- 函数的定义：
	- 函数命名：X元X函数 （未知量个数，定义域集合）
		- （例）一元实函数
	- 定义域：自变量
		- 自然定义域：自变量的最大取值范围
			- （例）$log_ax: D=(0, +\infty)$
	- 值域：因变量
	- 对应关系：
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
				- ![](../../../../../Assets/Pics/Screenshot%202023-10-05%20at%2011.20.50%20PM.png)
- （下面的内容逻辑上应该在数列之后）
- ==函数的初等性质==
	- 有界性
		- 上界，上确界
		- 下...
	- 单调性
		- 单调增加，严格单调增加
		- 减少...
	- 奇偶性
		- 奇: $F(-x) = -F(x)$
		- 偶: $F(-x) = F(x)$
	- 周期性
		-  $x \in D, x + T \in D, F(x) = F(x+T)$
		- 最小周期T
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
- 有理数集Q：加法、减法、乘法、除法封闭
- (第一次数学危机)
	- 可公度：a，b两线段的长度，则存在另一长度为c的线段，使得$a=mc, b=nc, \frac{a}{b} = \frac{m}{n}$
	- （例）证明 $\sqrt2$ 不是有理数
		- 反证法
	- 
- 实数集R：加法、减法、乘法、除法、根号 封闭
- 复数集

实数系的连续性
- Z: 离散性
- Q: 稠密性，但有空隙
	- 无限分割
- R: 连续性（实数连续统）

最大数与最小数：
- 有限非空集
	- 必有最大最小数：
		- （证）反证法
- 无限集
	- 不一定有最大最小数
		- （证）

上界/下界
- 定义：
- 上界集合/下界集合
	- 定义：
	- 上界集合最大数/最小数
		- （证）
		- 上确界：
	- 下界集合最大数/最小数
		- （证）
		- 下确界：
- <a style="red">确界存在定理（实数系连续性定理）</a>
	- 定义：
	- 证明：

数列
- 数列的定义：特殊的离散函数
- 数列的表示：
	- 枚举
	- 表达式
	- 通项式
- ==数列的极限==
	- （例）圆周率
		- 刘徽：圆内接正多边形的周长逼近
	- 数列极限的定义：（柯西）$lim_{n\to\infty}{x_n}=a: \forall\theta\gt0,\exists{N}, \forall n\gt{N}, \vert x_n - a \vert \lt \theta$
		- (数列极限与数列前项无关)
		- 收敛：
		- 发散：
		- ![](../../../Assets/Pics/Screenshot%202023-10-06%20at%2012.29.54%20AM.png)
		- 使用定义证明数列极限： $n \to \infty$ (放缩)
			- https://www.bilibili.com/video/BV1sX4y1Y7jH/?p=10&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
			- 基本初等函数
				- 常数函数
					- $lim_{n\to\infty}a$
				- 幂、指、对函数
					- ${n^2}$
					- ${\left(-1\right)^n}$
					- ${q^n, 0<\vert q \vert<1}$
					- $lim_{n \to \infty}{\sqrt[n]{a}} = 1, a>1$
				- 三角、反三角函数
					- 
			- 初等函数
				- 加减+基本初等函数（及其复合/求逆）：
					- 略
				- 乘除+基本初等函数（及其复合/求逆）：
					- ${\frac{n}{n+3}} \to 1$
					- ${\frac{1}{n}}$
					- $lim_{n\to\infty}{\sqrt[n]n = 1}$
					- $lim_{n\to\infty}{\frac{n^2+1}{2n^2-7n}}=\frac{1}{2}$
				- 基本初等函数的复合/求逆
	- 数列极限的性质：
		- 唯一性
			- $lim_{n\to\infty}{x_n}=a, lim_{n\to\infty}{x_n}=b \to a=b$
		- 有界性
			- <a style="red">收敛数列必定有界</a>
				- （证）
		- 保序性（实际上是前两个性质的推论）
			- ![](../../../Assets/Pics/Screenshot%202023-10-06%20at%2010.42.51%20AM.png)
			- 推论1: $if \ lim_{n\to\infty}{y_n = b \gt 0}, \ then \ \exists N, \forall n \gt N, y_n \gt \frac{b}{2} \gt 0$
			- 推论2: $if \ lim_{n\to\infty}{y_n = b \lt 0}, \ then \ \exists N, \forall n \gt N, y_n \lt \frac{b}{2} \lt 0$
			- 推论3: $if \ lim_{n\to\infty}{y_n = b \neq 0}, \ then \ \exists N, \forall n \gt N, \vert y_n \vert \gt \vert \frac{b}{2} \vert \gt 0$
	- 数列极限的重要计算方法：
		- <a style="red">加逼定理</a>
			- （证）
			- （例）$lim_{n\to\infty}({\sqrt{n+1}-\sqrt{n})}$
			- （例）$lim_{n\to\infty}{(a_1^n + a_2^n + ... + a_q^n)^{\frac{1}{n}}} = \max{a_i}$
			- （例）$lim_{n\to\infty}{\sqrt[n]n = 1}$
				- $1 \lt \sqrt[n]{n} = \sqrt[n]{\sqrt{n}\sqrt{n}\cdot\underbrace{1\cdot1\cdot ... \cdot1}}_{n-2} \leq \frac{2\sqrt{n} + n -2}{n}$
			- （例）$lim_{n\to\infty}{\sqrt[n]{n^2} = 1}$
				- $1 \lt \sqrt[n]{n^2} = \sqrt[n]{\sqrt{n}\sqrt{n}\sqrt{n}\sqrt{n}\cdot\underbrace{1\cdot1\cdot ... \cdot1}}_{n-4} \leq \frac{4\sqrt{n} + n - 4}{n}$
			- 
	- <a style="red">数列极限的四则运算（确定，有限）</a>
		- **前提：$x_n, \ y_n$ 极限均存在**，设 $lim_{n\to\infty}{x_n}=a, \ lim_{n\to\infty}{y_n}=b$，对其做**有限次**四则运算：
			- $lim_{n\to\infty}({\alpha{x_n}+\beta{y_n}}) = \alpha a + \beta b$
				- （证）
			- $lim_{n\to\infty}({\alpha{x_n} \times \beta{y_n}}) = \alpha a \times \beta b$
				- （证）
			- $lim_{n\to\infty}{\frac{\alpha{x_n}}{\beta{y_n}}} = \frac{\alpha a}{\beta b}$
				- （证）
		- **初等函数**在数列极限上的**有限次**四则运算：
			- $lim_{n\to\infty}{\frac{5^{n+1}-(-2)^n}{3\cdot5^n + 2\cdot3^n}} \to 1$
			- $lim_{n \to \infty}{\sqrt[n]{a}} = 1, a>0$
				- $\begin{cases}a \gt 1 & 已证 \\ a = 1 & 显然 \\ a \lt 1 & lim_{n\to\infty}{\frac{1}{\sqrt[n]{\frac{1}{a}}}} \end{cases}$
			- $lim_{n\to\infty}{n\cdot(\sqrt{n^2+1} - \sqrt{n^2-1})}$
			- ==重要不等式的数列极限==
				- $\frac{a_1 + a_2 + a_3 + ... a_n}{n} \geq \sqrt{a_1a_2a_3...a_n} \geq \frac{n}{\frac{1}{a_1}+\frac{1}{a_2}+...+\frac{1}{a_n}}$
				- $\frac{a_1 + a_2 + a_3 + ... a_n}{n}$
				- $\sqrt{a_1a_2a_3...a_n}$
				- $\frac{n}{\frac{1}{a_1}+\frac{1}{a_2}+...+\frac{1}{a_n}}$
			- ==其他一些重要极限==
				- 
		- **初等函数**在数列极限上的**无限次**四则运算：
			- $lim_{n\to\infty}({\frac{1}{\sqrt{n^2+1}}+\frac{1}{\sqrt{n^2+2}}+\frac{1}{\sqrt{n^2+3}}+...+\frac{1}{\sqrt{n^2+n}}})$
				- 加逼
	- 特殊的极限：
		- 特殊极限定义：
			- $\infty$ 无穷大量 （正无穷大，负无穷大）
				- 定义：
				- （例）
			- $0$ 无穷小量
				- 定义：
				- （例）
		- 特殊极限性质：
			- $if \ x_n \neq 0, \ n \to \infty, \ then \ (\{x_n\} \to \infty ) \Leftrightarrow ( \{\frac{1}{x_n}\} \to 0 )$
				- （证）
		- 特殊极限运算：
			- https://www.bilibili.com/video/BV1sX4y1Y7jH/?p=14&share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
	- 数列极限的收敛准则（数列极限的判断）
		- 



### 3️⃣ Function (函数)
↗ [Function](../🤼‍♀️%20Mathematical%20Logics/Set%20Theory/Function/Function.md)


### 4️⃣ Differential Calculus | Derivative (微分，导数)
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