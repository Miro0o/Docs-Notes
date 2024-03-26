# AutoAudit-网络安全大模型

[TOC]



## Res
🏠 https://github.com/ddzipp/AutoAudit
- [AutoAudit-7B](https://github.com/ddzipp/AutoAudit/blob/main)，此版本为demo版，基于[Alpaca-Lora](https://github.com/tloen/alpaca-lora)训练而来，在网络安全的英文领域回答效果尚佳，但暂时不具备上下文关联的功能，需要用更大参数的模型来解决。
- AutoAudit-33B，该版本仍然在内部测试和训练过程中，我们会稍晚些时候放出。


### Related Topics
↗ [AssemblyLine 4](../../../../../../CyberSecurity/🛌%20Comprehensive%20Defense%20Systems%20&%20Security%20Products/Software%20Analysis%20Tools/AssemblyLine%204/AssemblyLine%204.md)



## Intro
ChatGPT开启了大语言模型发展的新方向，各大互联网巨头纷纷进入赛道。各大高校也加大对LLM的研发应用。在通用大语言模型领域OpenAI的统治地位暂时无可撼动；因此针对特定领域（Specific-Domain）的大语言模型是发展的必然趋势。目前医疗、教育、金融，法律领域已逐渐有了各自的模型，但网络安全领域迟迟没有模型发布。

无独有偶的是，我们发现微软也有类似定位产品——Microsoft Security Copilot，或许将自然语言处理的大语言模型引入到网络安全乃至安全审计领域，是一条可行的路线；

为促进大语言模型在网络安全领域的应用，本项目开源了网络安全大模型AutoAudit，AutoAudit作为专门针对网络安全领域的大语言模型，其目标是为安全审计和网络防御提供强大的自然语言处理能力。它具备分析恶意代码、检测网络攻击、预测安全漏洞等功能，为安全专业人员提供有力的支持。

通过引入AutoAudit这样的网络安全语言模型，我们可以期待在网络安全领域取得更大的突破。它将成为安全专业人员的得力助手，提供准确、快速的分析和预测，帮助应对不断演进的网络威胁。

为了便于交互，应对实际的安全审核应用场景，我们将AutoAudit模型与ClamAV进行耦合，搭建了一个安全扫描的平台（前端参考了Bootstrap所提供的模板）。如果您想直接下载AutoAudit模型，请访问[HuggingFace](https://huggingface.co/lilBuffaloEric/autoaudit_20230703_attempt1)直接获取权重。



## Ref

