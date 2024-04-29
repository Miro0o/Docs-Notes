# Tex & LaTex

[TOC]



## Res
> Tex belongs to **TUG(The Tex Users Group)**
> 
> CTAN 👉  https://ctan.org is an active community contributing to the maintainers and development of Tex. 
> 
> [📌 📌 **A very brief & useful introduction to Tex**](https://liam.page/2014/09/08/latex-introduction/)

🏠 The LaTex Project: https://www.latex-project.org
https://www.overleaf.com/learn

👍 📂 https://www.overleaf.com/learn
Welcome to the Overleaf knowledge base. A complete list of topics is provided on the left hand-side, but here is a selection of useful articles:

📂 https://steeven9.github.io/USI-LaTeX/index.html
A USI's guide on how to use LaTeX

📂 https://latexref.xyz (LaTeX2e: An unofficial reference manual)
This is an unofficial reference manual for LaTeX. See below for the [Table of Contents](https://latexref.xyz/#SEC_Overview). If you want a tutorial then please instead visit [`learnlatex.org`](https://www.learnlatex.org/) or [this list](https://ctan.org/topic/tut-latex).


### Other Links
↗ [Tex & LaTex Related Tools](../../../../Software%20Engineering/CASE%20(Computer-Aided%20Software%20Engineering)%20Tools/Integrated%20CASE%20Tools/Docs%20Tools/Tex%20&%20LaTex%20Related%20Tools/Tex%20&%20LaTex%20Related%20Tools.md)

https://www.overleaf.com/project
online LaTex editor

🔥 https://github.com/kevinleeex/scu_thesis_2020
四川大学研究生学位论文模板LaTex(复刻官方word模板)Here you go!



## Intro
### 遇到问题怎么办
0. 绝对的新手，先读完一本入门读物，了解基本的知识；
1. 无论如何，先读文档！绝大部分问题都是文档可以解决的；
2. 利用 Google 搜索你的问题；
3. 在各个论坛或者 LaTeX 交流群里聪明地提出你的问题。

参考：[https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)

- CTeX 论坛提问版：[https://github.com/CTeX-org/forum/issues](https://github.com/CTeX-org/forum/issues)
- 提供一个 Telegram 交流群：[https://t.me/chinesetex](https://t.me/chinesetex)
- 提供一个 QQ 交流群：141877998


### 什么是LaTex
如果你需要写论文，那么请直接跳到下一节，因为你不学也得学。

LaTeX 是一种基于 TeX 的排版系统，由图灵奖得主 Lamport 开发，而 Tex 则是由 Knuth 最初开发，这两位都是计算机界的巨擘。当然开发者强并不是我们学习 LaTeX 的理由，LaTeX 和常见的所见即所得的 Word 文档最大的区别就是用户只需要关注写作的内容，而排版则完全交给软件自动完成。这让没有任何排版经验的普通人得以写出排版非常专业的论文或文章。

Berkeley计算机系教授 Christos Papadimitriou 曾说过一句半开玩笑的话：

> Every time I read a LaTeX document, I think, wow, this must be correct!


### 如何学习 LaTeX
推荐的学习路线如下：
- LaTeX 的环境配置是个比较头疼的问题。如果你本地配置 LaTeX 环境出现了问题，可以考虑使用 [Overleaf](https://www.overleaf.com/) 这个在线 LaTeX 编辑网站。站内不仅有各种各样的 LaTeX 模版供你选择，还免去了环境配置的难题。
- 阅读下面三篇 Tutorial: [Part-1](https://www.overleaf.com/latex/learn/free-online-introduction-to-latex-part-1), [Part-2](https://www.overleaf.com/latex/learn/free-online-introduction-to-latex-part-2), [Part-3](https://www.overleaf.com/latex/learn/free-online-introduction-to-latex-part-3)。
- 学习 LaTeX 最好的方式当然是写论文，不过从一门数学课入手用 LaTeX 写作业也是一个不错的选择。



## MacTex
🏠 https://tex.stackexchange.com/questions/560814/which-versions-of-tex-do-i-need

- **TeXShop** This is a full featured TeX editor/IDE. If you've never used LaTeX before it can make your life substantially easier, since as an IDE it has most of the functions that you would want to use built in and accessible. It's not just for beginners either; I use it as my regular editor for TeX even though I use other editors for editing code. This is actively maintained, and has a large user base. 

- **BibDesk** This is a fantastic bibliography management tool. It not only allows you to maintain a `.bib` file, but also allows you to link your PDFs of the articles or notes to the `.bib` entry. It has many great features (e.g. paste a DOI and it retrieves the `.bib` data). It also links with TeXShop so that you can type a citation key and use autocomplete to complete the citation key from your open `.bib` file. This is also actively maintained and has a large user base.
 
- **TeXLive Utility** This is a GUI interface to `tlmgr` which is used to keep your packages up to date. It can also set other global parameters such as default page size, and allows you to switch between different installed versions of TeXLive. Many of us keep multiple years on our machines, and TeXLive Utility makes switching between them when needed simple. One thing to note is that it assumes the most recent TeXLive distribution for updating, so it's probably a good idea to install the most recent MacTeX distribution rather than the one you currently have installed.

- **LaTeXit** This is an equation editor, designed for turning snippets of LaTeX code into various formats (PDF, PNG, SVG, TIFF, JPG, MathML) that can be inserted into other kinds of documents, such as PowerPoint or Keynote. If you prefer to use these programs for presentations this can be a very useful tool.



## Tex Syntax
### typesetting
🔗 https://blog.csdn.net/qingdujun/article/details/80805613
about the layout of the article. 


### math syntax basics
🔗 https://zhuanlan.zhihu.com/p/124275975
about the math equation in tex.


### set relations
🔗 https://cloud.tencent.com/developer/article/1495188

- 集合的大括号： \{ ... }\
- 集合中的“|”： \mid
- 属于： \in
- 不属于： \not\in
- A包含于B： A\subset B
- A真包含于B： A\subsetneqq B
- A包含B： A\supset B
- A真包含B： A\supsetneqq B
- A不包含于B： A\not\subset B
- A交B： A\cap B
- A并B： A\cup B
- A的闭包： \overline{A}
- A减去B: A\setminus B
- 实数集合： \mathbb{R}
- 空集： emptyset



## Ref
[LaTex支持中文的三种方式 | CSDN]: http://t.csdnimg.cn/UvhOd
[LaTeX Error: File `ctex.sty' not found | StackExchange]: https://tex.stackexchange.com/q/687540/312951
[How do I add a .sty file to my MacTeX/TeXShop installation? | StackExchange]: https://tex.stackexchange.com/q/10252/312951

[LaTex输入中文英文混排 | CSDN]: http://t.csdnimg.cn/xnwFP
[LaTeX支持中文英文混排编译的三种方式-Slager - 中奥智能SINOAUS的文章 - 知乎]: https://zhuanlan.zhihu.com/p/381759570
