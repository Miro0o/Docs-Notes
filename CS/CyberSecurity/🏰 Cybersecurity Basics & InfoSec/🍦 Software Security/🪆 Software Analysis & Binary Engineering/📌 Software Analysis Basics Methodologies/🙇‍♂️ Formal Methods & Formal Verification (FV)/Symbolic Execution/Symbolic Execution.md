# Symbolic Execution

[TOC]



## Res
🏠 
🚧 


### Related Topics



## Intro



## Ref
[简单理解符号执行技术]: https://www.k0rz3n.com/2019/02/28/简单理解符号执行技术/

Wiki中的定义是：在计算机科学中，符号执行技术指的是通过程序分析的方法，确定哪些输入向量会对应导致程序的执行结果为某个向量的方法(绕)。通俗的说，**如果把一个程序比作DOTA英雄，英雄的最终属性值为程序的输出（包括攻击力、防御力、血槽、蓝槽），英雄的武器出装为程序的输入（出A杖还是BKB）。那么符号执行技术的任务就是，给定了一个英雄的最终属性值，分析出该英雄可以通过哪些出装方式达到这种最终属性值效果。**

可以发现，**符号执行技术是一种白盒的静态分析技术**。即，分析程序可能的输入需要能够获取到目标源代码的支持。**同时，它是静态的，因为并没有实际的执行程序本身，而是分析程序的执行路径**。如果把上述英雄的最终属性值替换成程序形成的bug状态，比如，存在数组越界复制的状态，那么，我们就能够利用此技术挖掘漏洞的输入向量了。

[🤔 Understanding SMT solvers: An Introduction to Z3]: https://de-engineer.github.io/SMT-Solvers/
This post was an overview of SMT solvers with the practical example of a CTF challenge and we also touched a bit on their limitations. I’m not an expert on the topic, I tried to cover all the introductory knowledge that I could put in without increasing the complexity of the blog. There is indeed far more to learn about and you can do so by checking all the links in the resources section.
- [Symbolic Execution Lecture from MIT](https://www.youtube.com/watch?v=yRVZPvHYHzw)
- [Symbolic Execution with Triton Engine](https://pwn.umasscybersec.org/lectures/index.html)
- [HexRays CTF solution with Z3](https://www.youtube.com/watch?v=kZd1Hi0ZBYc)
- [OST2 Course on Symbolic Analysis (teaches angr)](https://p.ost2.fyi/courses/course-v1:OpenSecurityTraining2+RE3201_symexec+2021_V1/course/)
- [Papers by Z3 team](https://z3prover.github.io/papers/)
- [The Path Explosion Problem in Symbolic Execution - Paper](https://studenttheses.uu.nl/bitstream/handle/20.500.12932/35856/thesis.pdf?sequence=1&isAllowed=y)
