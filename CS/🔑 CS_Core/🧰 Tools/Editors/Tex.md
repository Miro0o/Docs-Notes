> Tex belongs to [[CS entries quick-look#TUG|TUG(The Tex Users Group)]]
> 
> CTAN 👉  https://ctan.org is an active community contributing to the maintainense and development of Tex. 
> 
> [📌 📌 **A very brief & useful introduction to Tex**](https://liam.page/2014/09/08/latex-introduction/)

# [The LaTex Project](https://www.latex-project.org)


#### 遇到问题怎么办

0.  绝对的新手，先读完一本入门读物，了解基本的知识；
1.  无论如何，先读文档！绝大部分问题都是文档可以解决的；
2.  利用 Google 搜索你的问题；
3.  在各个论坛或者 LaTeX 交流群里聪明地提出你的问题。

参考：[https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)

-   CTeX 论坛提问版：[https://github.com/CTeX-org/forum/issues](https://github.com/CTeX-org/forum/issues)
-   提供一个 Telegram 交流群：[https://t.me/chinesetex](https://t.me/chinesetex)
-   提供一个 QQ 交流群：141877998

#### [MacTex](https://tex.stackexchange.com/questions/560814/which-versions-of-tex-do-i-need) 
-   **TeXShop** This is a full featured TeX editor/IDE. If you've never used LaTeX before it can make your life substantially easier, since as an IDE it has most of the functions that you would want to use built in and accessible. It's not just for beginners either; I use it as my regular editor for TeX even though I use other editors for editing code. This is actively maintained, and has a large user base. 
    
-   **BibDesk** This is a fantastic bibliography management tool. It not only allows you to maintain a `.bib` file, but also allows you to link your PDFs of the articles or notes to the `.bib` entry. It has many great features (e.g. paste a DOI and it retrieves the `.bib` data). It also links with TeXShop so that you can type a citation key and use autocomplete to complete the citation key from your open `.bib` file. This is also actively maintained and has a large user base.
    
-   **TeXLive Utility** This is a GUI interface to `tlmgr` which is used to keep your packages up to date. It can also set other global parameters such as default page size, and allows you to switch between different installed versions of TeXLive. Many of us keep multiple years on our machines, and TeXLive Utility makes switching between them when needed simple. One thing to note is that it assumes the most recent TeXLive distribution for updating, so it's probably a good idea to install the most recent MacTeX distribution rather than the one you currently have installed.
    
-   **LaTeXit** This is an equation editor, designed for turning snippets of LaTeX code into various formats (PDF, PNG, SVG, TIFF, JPG, MathML) that can be inserted into other kinds of documents, such as PowerPoint or Keynote. If you prefer to use these programs for presentations this can be a very useful tool.

## Syntax:
#### [typesetting](https://blog.csdn.net/qingdujun/article/details/80805613)
about the layout of the article. 

#### [math syntax basics](https://zhuanlan.zhihu.com/p/124275975)
about the math equation in tex.

#### [set relations](https://cloud.tencent.com/developer/article/1495188)
-   集合的大括号： \{ ... }\
-   集合中的“|”： \mid
-   属于： \in
-   不属于： \not\in
-   A包含于B： A\subset B
-   A真包含于B： A\subsetneqq B
-   A包含B： A\supset B
-   A真包含B： A\supsetneqq B
-   A不包含于B： A\not\subset B
-   A交B： A\cap B
-   A并B： A\cup B
-   A的闭包： \overline{A}
-   A减去B: A\setminus B
-   实数集合： \mathbb{R}
-   空集： \emptyset
