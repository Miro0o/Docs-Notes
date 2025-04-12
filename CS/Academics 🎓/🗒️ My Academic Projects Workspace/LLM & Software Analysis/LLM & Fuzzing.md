# LLM & Fuzzing

[TOC]



## Res
### Related Topics
↗ [Fuzzing (Fuzz Testing)](../../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/🪆%20Software%20Analysis%20&%20Binary%20Engineering/📌%20Software%20Analysis%20Basics%20Methodologies/Fuzzing%20(Fuzz%20Testing)/Fuzzing%20(Fuzz%20Testing).md)



## Fuzzing Technology Trending List
AutoSafeCoder: A Multi-Agent Framework for Securing LLM Code Generation through Static Analysis and Fuzz Testing
https://arxiv.org/abs/2409.10737
https://ui.adsabs.harvard.edu/abs/2023arXiv230712469Z/abstract

Zhang, Cen, Yaowen Zheng, Mingqiang Bai, Yeting Li, Wei Ma, Xiaofei Xie, Yuekang Li, Limin Sun, and Yang Liu. "How effective are they? Exploring large language model based fuzz driver generation." In _Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis_, pp. 1223-1235. 2024.

技术进展 | Prompt-Fuzz：基于LLM的库模糊测试驱动自动化生成
https://mp.weixin.qq.com/s/V3OC6BbZuMC0eev53C_LWA
Prompt Fuzzing for Fuzz Driver Generation
https://arxiv.org/abs/2312.17677

FuzzGpt：对深度学习库进行模糊测试的大语言模型｜技术进展
https://mp.weixin.qq.com/s/2keGLL08Au9oAxTrRa67qQ
Large Language Models are Edge-Case Fuzzers: Testing Deep Learning Libraries via FuzzGPT
https://arxiv.org/abs/2304.02014

技术进展 | Fuzz4All：基于大语言模型的通用模糊测试
https://mp.weixin.qq.com/s/9QQcDYQPn8OnpZwmI4WPdg
https://www.software-lab.org/publications/icse2024_Fuzz4All.pdf

CovRL-Fuzz：基于大模型变异的JavaScript解释器模糊测试技术 | 技术进展
https://mp.weixin.qq.com/s/6DaD7rw3t7TFYupTJoEtaw

技术进展 | MINER：一种用于REST API模糊测试的混合数据驱动方法
https://mp.weixin.qq.com/s/u26iSavxWGswrcuLaaACKA

技术进展 | SDFUZZ:目标状态驱动的定向模糊测试
https://mp.weixin.qq.com/s/zodAi0hD05HuIji6krz9TA

SEAMFUZZ：灰盒模糊测试的学习种子自适应突变策略
https://mp.weixin.qq.com/s/duEtfMfayefdBzlqm1rM_g

---
大模型与模糊测试进行结合的研究论文汇总｜技术进展
https://mp.weixin.qq.com/s/DL4pGH-7nPi3eSRD-rlD-w

2024信息安全领域四大顶会Fuzz论文汇总｜技术进展
https://mp.weixin.qq.com/s/Dn5ooUahCT7IqXIMevjVug

2024年软件工程顶会Fuzz论文汇总
https://mp.weixin.qq.com/s/-ZYX-G_jX1AN8lzbHvW21g



## Graduation Thesis
### Thesis Template
https://github.com/cuiao/SCU_ThesisDissertation_LaTeXTemplate
_发布日期：2016年5月30日_

作者本人是一名四川大学的学生，在学习科研活动中经常需要进行学术写作。在使用传统的字处理软件（如_Microsoft® Word_）时，由于其对数学等特殊需求的支持不够友好，因此往往会遇到各种各样的问题，无法高效地写作。作者偶然接触到了LaTeX排版系统，其强大的功能、优美的数学排版和便利的自动化工具等众多优点使人印象深刻，特别适合理工科学生学习和使用。经过了解，发现国际期刊论文主要使用LaTeX进行排版，且国内外许多高校均提供LaTeX的学位论文模版，而我校在这方面的发展还略显不足。在这样的动机驱使下，作者在利用自己较为初级的LaTeX知识，参考了北京大学同学的_pkuthss_模版和其他相关文献的基础上，开发了_scuthesis_这个适用于四川大学研究生（虽包含有本科选项，但封面未修改）使用的LaTeX学位论文模版。希望此模版能够给各位同学提供一个额外的选择，模版中若有瑕疵，还请各位同学批评指正，留言、新建一个_ISSUSE_或_FORK_一个新分支修改。

https://github.com/fatestigma/scuthesis
ScuThsis 是一个**非官方**的四川大学本科生毕业设计论文模板，模板的制作目的是为了让大家可以更容易的利用 LaTeX 排版引擎制作出排版精美的毕业论文，一来提高毕业论文的排版质量，二来可以将更多的精力放在论文内容的输出上。

在2016届毕业生中共有10多位参与ScuThesis内测，并有4位获得四川大学本科优秀毕业论文，其中1位被打回，要求提交`doc`格式文档。

https://github.com/fanmcgrady/SCU-Thesis-LaTeX-Template
左大神（四川大学计算机学院左劼大神）告诉我他的博士论文是用自己设计的LaTeX模板写的。

> 题目：《基因表达式编程核心技术研究》，有兴趣的同学可以拜读一下

膜拜了左大神的博士论文以后感触很多。 为了追逐大神的脚步，我的博士论文当然也绝对不能用Word了。 四川大学研究生院提供了Word版本的论文格式[模板](http://gs.scu.edu.cn/info/1044/2110.htm)， 并没有提供相关的学位论文LaTeX模板。 在Github上找到原作者[cuiao](https://github.com/cuiao/SCU_ThesisDissertation_LaTeXTemplate)的项目_scuthesis_。 本项目是在原作者的基础上进行了一些修改，能够满足四川大学学位论文的格式要求。 希望本项目能让大家更加专注于学位论文的写作！

https://github.com/SunnyHaze/scu-thesis-template?tab=readme-ov-file
- 本Word模板仓库链接: https://github.com/SunnyHaze/scu-thesis-template
- 前辈大佬提供的Latex模板：https://github.com/fatestigma/scuthesis
- 另一个前辈大佬提供的Latex模板：https://github.com/dahakawang/scu_thesis_template
- 另一个大佬提供的学位论文Latex模板: https://github.com/cuiao/SCU_ThesisDissertation_LaTeXTemplate


### Survey


### Translation


### Graduation Paper
![Fuzz4All.excalidraw | 800](../../../../Assets/Illustrations/Fuzzing/Fuzz4All/Fuzz4All.excalidraw.md)



## Ref
[四川大学本科毕业论文（设计）格式和参考文献著录要求]: https://cs.scu.edu.cn/info/1050/9337.htm
[毕业论文（设计）]: https://jwc.scu.edu.cn/jxgl/bylw_sj_.htm

[网络空间安全学院2025届本科毕业论文工作流程安排]: https://ccs.scu.edu.cn/info/1026/3825.htm

[关于开展2025届本科毕业论文（设计）学术不端行为检测工作的通知]: https://jwc.scu.edu.cn/info/1069/9801.htm
[木可YK|如何在四川大学图书馆进行论文检测（查重）？]: https://www.bilibili.com/opus/748442302568988709