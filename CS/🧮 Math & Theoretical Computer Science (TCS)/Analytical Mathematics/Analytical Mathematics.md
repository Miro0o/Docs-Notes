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
	- 可列：不重复，不遗漏地排列（反映了集合的离散性）
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
	- 对应关系：（见下“常见函数列表”）
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
	- 其他重要不等式
		- ![Triangle_Inequity.excalidraw|300](../../../Assets/Ilustrations/Math/Triangle_Inequity.excalidraw.md)
		- 
- ==三角函数恒等式==
	- Asda发
- ==常见的特殊函数==
	- 基本初等函数
	- 基本初等函数的推广
		- 初等函数
		- 高等函数
	- 分段函数
		- Dirichlet 函数
		- Riemann 函数
	- 符号函数
		- Sigmoid 函数


### 2️⃣ Sequence of Number (数列)
↗ [Algebraic Structure](../🧊%20Algebra/Algebraic%20Structure/Algebraic%20Structure.md)
↗ [Sequence of Number](Sequence%20of%20Number%20&%20Functions%20Basics/Sequence%20of%20Number.md)


### 3️⃣ Limits of Functions & Continuity of Functions (函数极限和连续函数)
↗ [Set Theory /Function](../🤼‍♀️%20Mathematical%20Logics/Set%20Theory/Function/Function.md)
↗ [Limits & Continuity of Functions](Sequence%20of%20Number%20&%20Functions%20Basics/Limits%20&%20Continuity%20of%20Functions.md)


### 4️⃣ Derivative｜Differential Calculus (导数，微分)
↗ [Differential Calculus & Derivative](Differential%20Calculus%20&%20Derivative/Differential%20Calculus%20&%20Derivative.md)


### 5️⃣ Mean Value Theorem (Lagrange Theorem)
↗ [Mean Value Theorem & Applications](Differential%20Calculus%20&%20Derivative/Mean%20Value%20Theorem%20&%20Applications.md)


### 6️⃣ Indefinite Integral (不定积分)
↗ [Indefinite Integral](Definite%20&%20Indefinite%20Integral/Indefinite%20Integral/Indefinite%20Integral.md)


### 7️⃣ Definite Integral (定积分)
↗ [Definite Integral](Definite%20&%20Indefinite%20Integral/Definite%20Integral/Definite%20Integral.md)


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