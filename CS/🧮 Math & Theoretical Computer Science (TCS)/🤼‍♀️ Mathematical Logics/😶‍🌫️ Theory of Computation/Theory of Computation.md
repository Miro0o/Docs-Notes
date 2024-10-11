# Theory of Computation

[TOC]



## Res
### Related Topics
↗ [Set Theory](../Set%20Theory/Set%20Theory.md)
↗ [Graph Theory](../../Graph%20Theory/Graph%20Theory.md)


### Learning Resources
🎬【【北京大学】理论计算机科学基础（全70讲）】 https://www.bilibili.com/video/BV1m4411p7nS/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d
https://mannuan.github.io/计算理论课件/
主讲老师：刘田

🎬【【MIT18.404】计算理论基础(完结)—理论研究或算法应用的基础课】 https://www.bilibili.com/video/BV1qL411s7mr/?share_source=copy_web&vd_source=7740584ebdab35221363fc24d1582d9d - Michael Sipser

📂 https://hackmd.io/2AqODdrtTOuj6fb5uMDZYw?view
The goal is to build a collection of videos for an undergraduate Theory of Computation course. We hope that this collection of videos would be a useful community resource for flipped classes. The intent is that these videos can be used in a flipped class format. The flipped format has been quite successful for other topics and seems well suited to remote teaching that many of us are doing. The instructor can choose to use these videos in whatever fashion he/she thinks best. These videos will ideally be supplemented by classroom discussion, practice exercises and assignments as part of the course.

📖 Introduction to the Theory of Computation, 3rd edition, by Michael Sipser
- [Sipers-computation-3rd-solutions](https://github.com/gaurangsaini/sipser-computation-3rd-solutions)

📖 [Computational Complexity: A Modern Approach](http://www.cs.princeton.edu/theory/complexity/) by Arora and Barak.
📖 Introduction to automata theory, languages, and computation / by John E. Hopcroft,. Rajeev Motwani, Jeffrey D. Ullman. -- _3rd ed_.

📖 [Computational Complexity](http://rads.stackoverflow.com/amzn/click/0201530821) by Papadimitriou
📖 [Computability and Logic](https://www.cambridge.org/core/books/computability-and-logic/440B4178B7CBF1C241694233716AB271) by George S. Boolos and John P. Burgess.
📖 [Oded Goldreich's textbook](http://rads.stackoverflow.com/amzn/click/052188473X)

👨‍💻 https://www.mropengate.com/2015/06/formal-language.html
計算理論是計算機科學的靈魂 - 國立陽明交通大學
一、正則語言 Regular Languages  
- [Ch1 決定性有限自動機 Deterministic Finite automata, DFA](http://mropengate.blogspot.tw/2015/03/formal-language-ch11-finite-automata.html)
- [Ch2 非決定性有限自動機 Nondeterminism Finite automata, NFA](http://mropengate.blogspot.tw/2015/04/formal-language-ch2-nondeterminism.html)
- [Ch3 正則表達式 Regular Expression, RE](http://mropengate.blogspot.tw/2015/04/formal-language-ch3-regular-expression.html)
- [Ch3.5 常用的正則表示式 Regular Expression in Application](http://mropengate.blogspot.tw/2015/02/regular-expression.html)
- [Ch4 泵引理 Pumping Lemma](http://mropengate.blogspot.tw/2015/04/formal-language-ch4-pumping-lemma.html)
- [Ch5 邁希爾－尼羅德定理 Myhill-Nerode Theorem](http://mropengate.blogspot.tw/2015/04/formal-language-ch5-myhill-nerode.html)
二、上下文無關語言 Context-Free Languages  
- [Ch6 上下文無關語言 Context-free language, CFLs](http://mropengate.blogspot.tw/2015/04/formal-language-ch6-context-free.html)
- [Ch7 下推自動機 Pushdown automaton, PDAs](http://mropengate.blogspot.tw/2015/04/formal-language-ch7-pushdown-automaton.html)
- [Ch8 上下文無關語言泵引理 Pumping lemma for context free languages](http://mropengate.blogspot.tw/2015/04/formal-language-ch7-pumping-lemma-for.html)
三、邱奇－圖靈論題 Church–Turing Thesis  
- [Ch9 圖靈機 Turing Machines](http://mropengate.blogspot.tw/2015/05/formal-language-ch9-turing-machines.html)
- [Ch10 變種圖靈機 Variants of Turing Machines](http://mropengate.blogspot.tw/2015/05/formal-language-ch10-variants-of-turing.html)
四、決定性問題 Decidability  
- [Ch11 決定性問題 Decidability](http://mropengate.blogspot.tw/2015/05/formal-language-ch11-decidability.html)
- [Ch12 不可決定問題與圖靈可識別語言 Undecidable Problem and Turing-recognizable language](http://mropengate.blogspot.tw/2015/05/formal-language-undecidable-problem.html)
- [Ch12.5 決定與不可決定問題相關習題](http://mropengate.blogspot.tw/2015/05/formal-language-ch125.html)
五、歸約 Reducibility  
- [Ch13 可歸約性 Reducibility](http://mropengate.blogspot.tw/2015/05/formal-language-ch13-reducibility.html)
- [Ch14 多一歸約 Mapping Reducibility](http://mropengate.blogspot.tw/2015/05/formal-language-ch14-mapping.html)
- [Ch14.5 歸約相關習題 Exercises for Reducibility](http://mropengate.blogspot.tw/2015/05/formal-language-ch145-exercises-mapping.html)
六、時間複雜度 Time Complexity  
- [Ch15 複雜度P和NP Time Complexity, P and NP](http://mropengate.blogspot.tw/2015/06/formal-language-ch15-pnp-time.html)
- [Ch16 NP完全 NP-Complete, NPC](http://mropengate.blogspot.tw/2015/06/formal-language-ch16-np-np-complete-npc.html)
- [Ch16.5 Cook-Levin理論與卡普的二十一個NP-完全問題](http://mropengate.blogspot.tw/2015/06/algorithm-cook-levinnp.html)



## Intro
> 🔗 https://en.wikipedia.org/wiki/Theory_of_computation

In [theoretical computer science](https://en.wikipedia.org/wiki/Theoretical_computer_science "Theoretical computer science") and [mathematics](https://en.wikipedia.org/wiki/Mathematics "Mathematics"), the **theory of computation** is the branch that deals with what problems can be solved on a model of computation, using an algorithm, how efficiently they can be solved or to what degree (e.g., [approximate solutions](https://en.wikipedia.org/wiki/Approximation_algorithms "Approximation algorithms")versus precise ones). The field is divided into three major branches:
1. [automata theory](https://en.wikipedia.org/wiki/Automata_theory "Automata theory") and [formal languages](https://en.wikipedia.org/wiki/Formal_language "Formal language")
	1. 有哪些计算装置？能力如何
	2. 有穷（无穷）自动机 /下推自动机 /图灵机
	3. 正则语言 /上下文无关语言 /可计算语言 /半可计算语言
2. [computability theory](https://en.wikipedia.org/wiki/Computability_theory "Computability theory")
	1. 什么是计算？哪些问题可以计算/不可以计算？
	2. 丘奇-图灵论题 /通用机 /停机问题 /规约 /递归定理
3. [computational complexity theory](https://en.wikipedia.org/wiki/Computational_complexity_theory "Computational complexity theory"), which are linked by the question: _"What are the fundamental capabilities and limitations of computers?"._
	1. 什么是有效计算？哪些问题可以/不可以有效计算？
	2. 时间复杂性 /空间复杂性 /多项式时间归约 /完全问题


> 🔗 https://www.mropengate.com/2015/06/formal-language.html

透過計算模型，我們可以對計算定下明確的數學定義。而一旦有了明確的定義，便可以研究什麼是可計算的、什麼是不可計算的，而對於可計算的問題，必須花費多少時間和空間才可能計算。  
  
Church–Turing thesis 指出，所有演算法可解的問題，都可透過 Turing machines 求解，也因此，藉由研究 Turing machines 我們得以探討電腦的極限，以及對各種問題的難度訂出明確的界線。  
  
這是一門非常理論與數學的課，需要非常清晰的邏輯思考。老師曾說，資訊界日新月異，許多課程可能幾年後就不見了，或者教的東西大幅改變。但你幾乎可以確定，正規語言這門課還是會一直存在。從哲學的角度來說，計算理論在電腦科學裡佔了十分核心的地位。  
  
正規語言課程所學的東西其實也有很多延伸的應用，以至於很多讀者很可能早已接觸過某些部份，但直到這門課，才真正以嚴謹的方式學習背後的來歷。像是如果有接觸像 Python 等語言或者用過 Vim 等編輯器的搜尋功能的讀者，很有可能有接觸過正規表示式。而 CFG 和程式語言的設計以及編譯器等課程有密切相關，你或許會曾在程式語言的文件上看過他。如果在演算法等課程聽過 NP、P 等名詞，在這堂課裡，你可以學到這些名詞到底有什麼含意。而對什麼是演算法，時間複雜度、問題的可計算性等等，都會在這堂課得到更深的理解。



## Ref
[计算机专业学计算理论基础的意义？ - 知乎]: https://www.zhihu.com/question/27306122
[计算理论重点——Theory of Computation]: https://blog.csdn.net/abcjennifer/article/details/8494019
[什么是可计算理论]: https://www.cnblogs.com/hjlweilong/p/13908517.html
[理论计算机科学浅涉：可计算性理论（一）]: http://niwatori.io/2018/01/13/computability-theory/

[Waht is the best text of computation theory /theory of computation | Stack Exchange]: https://cstheory.stackexchange.com/a/3527
