# Partial Order & Total Order (Linear Order) & Well-Order

[TOC]



## Res
### Related Topics



## Intro
### Total Order & Totally Ordered Sets (Tosets)


### Partial Order & Partially Ordered Sets (Posets)
> 🔗 https://courses.compute.dtu.dk/02242/topics/bounded-static-analysis.html#sec:2.2

A _partially ordered set_ or poset is a tuple $(L, \sqsubseteq)$, meaning a set of elements $L$ with an (partially) ordering relationship $\sqsubseteq$ on it, that uphold: $$\begin{aligned} & \forall a. \ a\sqsubseteq a & reflexive \\
& ∀a. \ a\sqsubseteq b\land b\sqsubseteq a\implies a=b & antisymetric \\
& ∀a. \ a\sqsubseteq b\land b\sqsubseteq c\implies a\sqsubseteq c & transitive
\end{aligned}$$
Common partially ordered sets are the integers $(ℤ,≤)$ (also in the other direction $(ℤ,≥)$), the booleans $(\{𝚝𝚝,𝚏𝚏\},\implies)$, and the set of Sign′s $(2^{Sign},\subseteq)$.
- We can draw the diagram of a poset. Below is the so called **Hasse Diagram** of poset $(2^{\text{\{A, B, C\}}}, \subseteq)$:
- ![|400](../../../../../../../Assets/Pics/Screenshot%202025-10-09%20at%2022.52.59.png)
- <small><a>https://blog.wohin.me/posts/nju-program-analysis-05/</a></small>


> 🔗 https://blog.wohin.me/posts/nju-program-analysis-05/
> **Upper/ lower bounds of a poset; lub & join; glb & meet**

给定一个偏序集$(P,\preceq)$和它的子集$S（S\subseteq P）$，我们说$u\in P$是$S$的一个**上界**，当且仅当$\forall x\in S, x\preceq u$；类似地，$l\in P$是$S$的一个**下界**，当且仅当$\forall x\in S, l\preceq x$。

若$S$是由下图中绿色部分组成的集合，那么$\{a,b,c\}$就是$S$的上界，$\{ \}$是$S$的下界：
![|300](../../../../../../../Assets/Pics/Screenshot%202025-10-11%20at%2012.51.15.png)

在此基础上，我们定义**最小上界（叫做lub或join）**，记为$\lfloor\rfloor S$，对于$S$的每一个上界$u$，有$\lfloor\rfloor S \preceq u \lfloor\rfloor S \preceq u$；类似地，定义最大下界（叫做glb或meet），记为$\lceil\rceil S$，对于$S$的每一个下界$l$，有$l\preceq l\lceil\rceil S\preceq\lceil\rceil S$。

还是以集合为例，若$S$是由下图中绿色部分组成的集合，则$\{a,b,c\}$和$\{a,b\}$都是它的上界，后者还是最小上界；$\{ \}$则是$S$的唯一下界，因此也是最大下界：

![|300](../../../../../../../Assets/Pics/Screenshot%202025-10-11%20at%2012.51.41.png)

若$S$只包含两个元素$a$和$b$，我们也可以将$\lfloor\rfloor S$写为$a\lfloor\rfloor b$，将$\lceil\rceil S$写为$a\lceil\rceil b$。

关于上下界的两个特性：
1. 不是所有的poset都有lub或glb。
2. 如果一个poset有lub或glb，它一定是唯一的。这一点可以借助偏序关系的antisymmetry特点证明。
#### Lattice (Poset Structure)
> ↗ [Lattice (Set Theory)](Lattice%20(Set%20Theory)/Lattice%20(Set%20Theory).md)

> 🔗 https://courses.compute.dtu.dk/02242/topics/bounded-static-analysis.html#sec:2.3

A lattice is partially ordered sets $(L,\sqsubseteq)$, with two extra operators $\lfloor \rfloor$ and $\lceil \rceil$. 
- $\lfloor \rfloor$ is the **least upper bound (lub), or join**.  $a\lfloor \rfloor b$, meaning that $$\forall c. \ a\sqsubseteq c\land b\sqsubseteq c \implies a\lfloor \rfloor b \sqsubseteq c.$$
- $\lceil \rceil$ is the **greatest lower bound (glb), or meet**. $a\lceil \rceil b$ meaning that $$\forall c. \ c\sqsubseteq a\land c\sqsubseteq b \implies c \sqsubseteq a\lceil \rceil b.$$
Furthermore, this implies that there exist a least bound $\bot=\lceil\rceil L$ and a greatest bound $\top=\lfloor\rfloor L$, from which we have the following identities: $$\begin{aligned}
& \top\lceil\rceil a = a = a\lfloor\rfloor \bot \\
& \top\lfloor\rfloor a = \top \\
& a \lceil\rceil\bot = \bot
\end{aligned}$$
#### Complete Partial Order (CPO)


### Well Order
#### Well-Ordering/ Zermelo Theorem



## Ref
[全序关系和偏序关系的区别是什么？ - 三川啦啦啦的回答 - 知乎]: https://www.zhihu.com/question/36758436/answer/500886873

偏序与完全序（离散数学知识）
**（1）偏序与完全序的概念：**
- [偏序关系](https://zhida.zhihu.com/search?content_id=131032430&content_type=Answer&match_order=1&q=%E5%81%8F%E5%BA%8F%E5%85%B3%E7%B3%BB&zhida_source=entity)、[全序关系](https://zhida.zhihu.com/search?content_id=131032430&content_type=Answer&match_order=1&q=%E5%85%A8%E5%BA%8F%E5%85%B3%E7%B3%BB&zhida_source=entity)都是[公理集合论](https://zhida.zhihu.com/search?content_id=131032430&content_type=Answer&match_order=1&q=%E5%85%AC%E7%90%86%E9%9B%86%E5%90%88%E8%AE%BA&zhida_source=entity)中的一种[二元关系](https://zhida.zhihu.com/search?content_id=131032430&content_type=Answer&match_order=1&q=%E4%BA%8C%E5%85%83%E5%85%B3%E7%B3%BB&zhida_source=entity)。
- 偏序集合：配备了偏序关系的集合。
	- 偏序：只对部分要元素成立关系（部分可比）
	- 集合内只有部分元素之间在这个关系下是可以比较的。
	- 比如：比如复数集中并不是所有的数都可以比较大小，那么“大小”就是复数集的一个偏序关系。
- 全序集合：配备了全序关系的集合。
	- 全序：对集合中任意两个元素都有关系
	- 集合内任何一对元素在在这个关系下都是相互可比较的。
	- 比如：有限长度的序列按字典序是全序的。最常见的是单词在字典中是全序的。
**（2）偏序与完全序的定义:**
- 偏序的定义：
	- 设R是集合A上的一个二元关系，若R满足：
		- Ⅰ [自反性](https://zhida.zhihu.com/search?content_id=131032430&content_type=Answer&match_order=1&q=%E8%87%AA%E5%8F%8D%E6%80%A7&zhida_source=entity)：对任意x∈A，有xRx；
		- Ⅱ [反对称性](https://zhida.zhihu.com/search?content_id=131032430&content_type=Answer&match_order=1&q=%E5%8F%8D%E5%AF%B9%E7%A7%B0%E6%80%A7&zhida_source=entity)（即反对称关系）：对任意x,y∈A，若xRy，且yRx，则x=y；
		- Ⅲ [传递性](https://zhida.zhihu.com/search?content_id=131032430&content_type=Answer&match_order=1&q=%E4%BC%A0%E9%80%92%E6%80%A7&zhida_source=entity)：对任意x, y,z∈A，若xRy，且yRz，则xRz。
	- 则称R为A上的偏序关系。
- 全序的定义：
	- 设集合X上有一全序关系，如果我们把这种关系用 ≤ 表述，则下列陈述对于 X 中的所有 a, b 和 c 成立：
		- 如果 a ≤ b 且 b ≤ a 则 a = b (反对称性)
		- 如果 a ≤ b 且 b ≤ c 则 a ≤ c (传递性)
		- a ≤ b 或 b ≤ a (完全性)
	- **注意**：
		- 完全性本身也包括了自反性。 所以，全序关系必是偏序关系。

---
以上答主好像都没有举例子，那我就当一回搬运工吧。
- 集合的包含关系是一种偏序。
- 在整数集中定义偏序：若a能整除b，我们就记为a≺b
显然它满足序公理。但整数集中，不是任何两个数都存在整除关系，这个关系是**局部**的（partial），太“偏颇”，于是被称为**偏序**。

[👍 南大软分课程笔记｜05 数据流分析理论]: https://blog.wohin.me/posts/nju-program-analysis-05/

[语言背后的代数学（七）：数学结构]: https://thzt.github.io/2018/02/09/semantics-7/