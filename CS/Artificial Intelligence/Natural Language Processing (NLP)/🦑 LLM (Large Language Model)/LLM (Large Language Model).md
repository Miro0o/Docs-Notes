# LLM (Large Language Model)

[TOC]



## Res
### Related Topics
↗ [Deep Learning (Neural Networks)](../../🗝️%20AI%20Basics%20&%20Machine%20Learning/📌%20Deep%20Learning%20(Neural%20Network)/Deep%20Learning%20(Neural%20Networks).md)
↗ [Transformers (Encoder-Decoder)](../../🗝️%20AI%20Basics%20&%20Machine%20Learning/📌%20Deep%20Learning%20(Neural%20Network)/🗿%20Neural%20Network%20Models/Transformers%20(Encoder-Decoder)/Transformers%20(Encoder-Decoder).md)

↗ [LangChain](../../../Software%20Engineering/🤖%20AI%20x%20SE/LLM%20Dev/LLM%20Application%20Dev%20Frameworks/LangChain/LangChain.md)

↗ [LLM & Federated Learning](../../../../Academics/🗒️%20Papers%20Reading%20Notes/LLM%20&%20Federated%20Learning/LLM%20&%20Federated%20Learning.md) 🎓
↗ [LLM & Security](../../../../CyberSecurity/🤖%20AI%20x%20Security/LLM%20&%20Security/LLM%20&%20Security.md)
↗ [AI x SE](../../../../Software%20Engineering/🤖%20AI%20x%20SE/AI%20x%20SE.md)
- ↗ [LLM Dev](../../../../Software%20Engineering/🤖%20AI%20x%20SE/LLM%20Dev/LLM%20Dev.md)


### Learning Resource
📖 大规模语言模型：从理论到实践
https://intro-llm.github.io
大语言模型（Large Language Models，LLM）是一种由包含数百亿以上权重的深度神经网络构建的语言模型，使用自监督学习方法通过大量无标记文本进行训练。自2018年以来，包含Google、OpenAI、Meta、百度、华为等公司和研究机构都纷纷发布了包括BERT， GPT等在内多种模型，并在几乎所有自然语言处理任务中都表现出色。2021年开始大模型呈现爆发式的增长，特别是2022年11月ChatGPT发布后，更是引起了全世界的广泛关注。用户可以使用自然语言与系统交互，从而实现包括问答、分类、摘要、翻译、聊天等从理解到生成的各种任务。大型语言模型展现出了强大的对世界知识掌握和对语言的理解。本书将介绍大语言模型的基础理论包括语言模型、分布式模型训练以及强化学习，并以Deepspeed-Chat框架为例介绍实现大语言模型和类ChatGPT系统的实践。

🔥 👍 📄 https://github.com/RUCAIBox/LLMSurvey （大语言模型综述 | 中国人民大学高瓴人工智能学院）
A collection of papers and resources related to Large Language Models.
The organization of papers refers to our survey [**"A Survey of Large Language Models"**](https://arxiv.org/abs/2303.18223).
To facilitate the reading of our (English-verison) survey, we also translate a [**Chinese version**](https://github.com/RUCAIBox/LLMSurvey/blob/main/assets/LLM_Survey_Chinese.pdf) for this survey. We will continue to update the Chinese version.

🔥 📄 https://arc.net/folder/D0472A20-9C20-4D3F-B145-D2865C0A9FEE
Papers must know to understand the world of deep learning & AIGC

---
🔥 🪜 https://github.com/Hannibal046/Awesome-LLM/tree/main
Large Language Models(LLM) have taken the ~~NLP community~~ ~~AI community~~ **the Whole World** by storm. Here is a curated list of papers about large language models, especially relating to ChatGPT. It also contains frameworks for LLM training, tools to deploy LLM, courses and tutorials about LLM and all publicly available LLM checkpoints and APIs.

![|500](../../../../Assets/Pics/Pasted%20image%2020240512212009.png)

- [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM/tree/main#awesome-llm-) 
    - [Milestone Papers](https://github.com/Hannibal046/Awesome-LLM/tree/main#milestone-papers)
    - [Other Papers](https://github.com/Hannibal046/Awesome-LLM/tree/main#other-papers)
    - [Open LLM](https://github.com/Hannibal046/Awesome-LLM/tree/main#open-llm)
    - [LLM Training Frameworks](https://github.com/Hannibal046/Awesome-LLM/tree/main#llm-training-frameworks)
    - [LLM Evaluation Frameworks](https://github.com/Hannibal046/Awesome-LLM/tree/main#llm-evaluation-frameworks)
    - [Tools for deploying LLM](https://github.com/Hannibal046/Awesome-LLM/tree/main#deploying-tools)
    - [Tutorials about LLM](https://github.com/Hannibal046/Awesome-LLM/tree/main#tutorials)
    - [Courses about LLM](https://github.com/Hannibal046/Awesome-LLM/tree/main#courses)
    - [Opinions about LLM](https://github.com/Hannibal046/Awesome-LLM/tree/main#opinions)
    - [Other Useful Resources](https://github.com/Hannibal046/Awesome-LLM/tree/main#other-useful-resources)
    - [Contributing](https://github.com/Hannibal046/Awesome-LLM/tree/main#contributing)

Trending LLM Projects
- [LWM](https://github.com/LargeWorldModel/LWM) - Large World Model (LWM) is a general-purpose large-context multimodal autoregressive model.
- [Sora](https://openai.com/sora) - Sora is an AI model that can create realistic and imaginative scenes from text instructions.
- [Gemma](https://blog.google/technology/developers/gemma-open-models/) - Gemma is built for responsible AI development from the same research and technology used to create Gemini models.
- [minbpe](https://github.com/karpathy/minbpe) - Minimal, clean code for the Byte Pair Encoding (BPE) algorithm commonly used in LLM tokenization.

---



## Intro


## Ref
[什么是LLM大语言模型？Large Language Model，从量变到质变 - 艾凡AFan的文章 - 知乎]: https://zhuanlan.zhihu.com/p/622518771

[👍 大语言模型调研汇总 - guolipa的文章 - 知乎]: https://zhuanlan.zhihu.com/p/614766286

[👍 大语言模型综述 | 中国人民大学高瓴人工智能学院]: http://ai.ruc.edu.cn/research/science/20230605100.html

[基于自然语言处理的漏洞检测方法综述]: https://m.fx361.com/news/2022/1215/16831048.html

[第二篇 基于自然语言处理的漏洞检测方法综述]: https://blog.csdn.net/qq_55202378/article/details/127583425
[76页综述+300余篇参考文献，天大团队全面介绍大语言模型对齐技术]: https://cloud.tencent.com/developer/article/2336345

[从Prompt注入到命令执行：探究LLM大型语言模型中 OpenAI的风险点]: https://www.secpulse.com/archives/199158.html

Prompt Injection 是一种攻击技术，黑客或恶意攻击者操纵 AI 模型的输入值，以诱导模型返回非预期的结果。这里提到的属于是SSTI服务端模板注入。

这允许攻击者利用模型的安全性来泄露用户数据或扭曲模型的训练结果。在某些模型中，很多情况下输入提示的数据会直接暴露或对输出有很大影响。

[深入剖析大模型安全问题：Langchain框架的隐藏风险 | 腾讯技术工程]: https://www.secrss.com/articles/59635

[👍 AAAI2024 | 分享10篇优秀论文，涉及图神经网络、大模型优化、表格分析等热门话题]: https://mp.weixin.qq.com/s/F7X8N_wUyZQNhDtIfHm17Q
