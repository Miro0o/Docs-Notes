# LLM & Supply Chain Security

[TOC]



## Res
### Related Topics
↗ [LLM & Security](../../../CyberSecurity/🫧%20AI%20x%20Security/LLM%20&%20Security/LLM%20&%20Security.md)
↗ [Software Supply Chains Security](../../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20InfoSec/🍦%20Software%20Security/Software%20Supply%20Chains%20Security/Software%20Supply%20Chains%20Security.md)



## Intro



## Ref
### Reading Logs
https://resources.infosecinstitute.com/topics/malware-analysis/top-7-malware-sample-databases-and-datasets-for-research-and-training/
Top 7 malware sample databases and datasets for research and training




### Articles
**An Empirical Study on Using Large Language Models to Analyze Software Supply Chain Security Failures**
https://dl.acm.org/doi/abs/10.1145/3605770.3625214

As we increasingly depend on software systems, the consequences of breaches in the software supply chain become more severe. High-profile cyber attacks like SolarWinds and ShadowHammer have resulted in significant financial and data losses, underlining the need for stronger cybersecurity. One way to prevent future breaches is by studying past failures. However, traditional methods of analyzing past failures require manually reading and summarizing reports about them. Automated support could reduce costs and allow analysis of more failures. Natural Language Processing (NLP) techniques such as Large Language Models (LLMs) could be leveraged to assist the analysis of failures. In this study, we assessed the ability of Large Language Models (LLMs) to analyze historical software supply chain breaches. We used LLMs to replicate the manual analysis of 69 software supply chain security failures performed by members of the Cloud Native Computing Foundation (CNCF). We developed prompts for LLMs to categorize these by four dimensions: type of compromise, intent, nature, and impact. GPT 3.5's categorizations had an average accuracy of 68% and Bard's had an accuracy of 58% over these dimensions. We report that LLMs effectively characterize software supply chain failures when the source articles are detailed enough for consensus among manual analysts, but cannot yet replace human analysts. Future work can improve LLM performance in this context, and study a broader range of articles and failures.

**SkipAnalyzer: A Tool for Static Code Analysis with Large Language Models**
https://arxiv.org/abs/2310.18532

We introduce SkipAnalyzer, a large language model (LLM)-powered tool for static code analysis. SkipAnalyzer has three components: 1) an LLM-based static bug detector that scans source code and reports specific types of bugs, 2) an LLM-based false-positive filter that can identify false-positive bugs in the results of static bug detectors (e.g., the result of step 1) to improve detection accuracy, and 3) an LLM-based patch generator that can generate patches for the detected bugs above. As a proof-of-concept, SkipAnalyzer is built on ChatGPT, which has exhibited outstanding performance in various software engineering tasks. To evaluate SkipAnalyzer, we focus on two types of typical and critical bugs that are targeted by static bug detection, i.e., Null Dereference and Resource Leak as subjects. We employ Infer to aid the gathering of these two bug types from 10 open-source projects. Consequently, our experiment dataset contains 222 instances of Null Dereference bugs and 46 instances of Resource Leak bugs. Our study demonstrates that SkipAnalyzer achieves remarkable performance in the mentioned static analysis tasks, including bug detection, false-positive warning removal, and bug repair. In static bug detection, SkipAnalyzer achieves accuracy values of up to 68.37% for detecting Null Dereference bugs and 76.95% for detecting Resource Leak bugs, improving the precision of the current leading bug detector, Infer, by 12.86% and 43.13%, respectively. For removing false-positive warnings, SkipAnalyzer can reach a precision of up to 93.88% for Null Dereference bugs and 63.33% for Resource Leak bugs. Additionally, SkipAnalyzer surpasses state-of-the-art false-positive warning removal tools. Furthermore, in bug repair, SkipAnalyzer can generate syntactically correct patches to fix its detected bugs with a success rate of up to 97.30%.

**Achieving High-Level Software Component Summarization via Hierarchical Chain-of-Thought Prompting and Static Code Analysis**
https://ieeexplore.ieee.org/abstract/document/10292037

Comprehension of software systems is key to their successful maintenance and evolution. This comprehension comes at different levels of abstraction: At the low level, one must focus on comprehending functions; while at the high level, one must abstract and comprehend the system's requirements. Diverse Automated Source Code Summarization (ASCS) techniques have been proposed to comprehend systems at the lower level. However, techniques for abstracting higher-level explanations fall short. Research on related fields, such as software architecture recovery, has tried to address system comprehension at the higher level by attempting to detect abstractions of design decisions from source code. Nevertheless, this is an on-going effort and many steps in the process are still unsolved. In this paper, we lever-age the emergent abilities of Large Language Models (LLMs) together with the achievements in the ASCS and static code analysis fields to design an approach that produces component-level summaries of software systems. Particularly, we address the unreliability of LLMs in performing reasoning by applying a chain-of-thought prompting strategy, which allows us to emulate inductive reasoning. We follow a bottom-up approach, where we start by comprehending lower-level software abstractions (e.g., functions), and then we compose these findings-in a cascading style-to comprehend higher-level ones (e.g., classes, components). We demonstrate the feasibility of our approach by applying it to the open-source Java project JHotDraw version 5.1. We believe our approach offers a stepping stone in developing robust automated software summarization approaches that can be applied generally across domains and types of software system.

**Machine learning based malicious payload identification in software-defined networking**
https://www.sciencedirect.com/science/article/pii/S1084804521001934
Deep [packet inspection](https://www.sciencedirect.com/topics/computer-science/inspection-packet "Learn more about packet inspection from ScienceDirect's AI-generated Topic Pages") (DPI) has been extensively investigated in software-defined networking (SDN) as complicated attacks may intractably inject [malicious payloads](https://www.sciencedirect.com/topics/computer-science/malicious-payload "Learn more about malicious payloads from ScienceDirect's AI-generated Topic Pages") in the packets. Existing proprietary pattern-based or port-based third-party DPI tools can suffer from limitations in efficiently processing a large volume of data traffic. In this paper, a novel OpenFlow-enabled deep packet inspection (OFDPI) approach is proposed based on the SDN paradigm to provide adaptive and efficient packet inspection. First, OFDPI prescribes an early detection at the flow-level [granularity](https://www.sciencedirect.com/topics/engineering/granularity "Learn more about granularity from ScienceDirect's AI-generated Topic Pages") by checking the IP addresses of each new flow via [OpenFlow](https://www.sciencedirect.com/topics/computer-science/openflow "Learn more about OpenFlow from ScienceDirect's AI-generated Topic Pages") protocols. Then, OFDPI allows for deep packet inspection at the packet-level granularity: (i) for unencrypted packets, OFDPI extracts the features of accessible payloads, including tri-gram frequency based on Term Frequency and Inverted Document Frequency (TF–IDF) and linguistic features. These features are concatenated into a sparse [matrix representation](https://www.sciencedirect.com/topics/engineering/matrix-representation "Learn more about matrix representation from ScienceDirect's AI-generated Topic Pages") and are then applied to train a [binary classifier](https://www.sciencedirect.com/topics/computer-science/binary-classifier "Learn more about binary classifier from ScienceDirect's AI-generated Topic Pages") with [logistic regression](https://www.sciencedirect.com/topics/computer-science/logistic-regression "Learn more about logistic regression from ScienceDirect's AI-generated Topic Pages") rather than matching with specific pattern combinations. In order to balance the detection accuracy and [performance bottleneck](https://www.sciencedirect.com/topics/computer-science/performance-bottleneck "Learn more about performance bottleneck from ScienceDirect's AI-generated Topic Pages") of the SDN controller, OFDPI introduces an adaptive packet sampling window based on the linear prediction; and (ii) for encrypted packets, OFDPI extracts notable features of packets and then trains a binary classifier with a [decision tree](https://www.sciencedirect.com/topics/computer-science/decision-trees "Learn more about decision tree from ScienceDirect's AI-generated Topic Pages"), instead of decrypting the encrypted traffic to weaken user privacy. A prototype of OFDPI is implemented on the Ryu SDN controller and the Mininet platform. The performance and the overhead of the proposed solution are assessed using the real-world datasets through experiments. The numerical results indicate that OFDPI can provide a significant improvement in detection accuracy with acceptable overheads.


### Datasets
https://github.com/1N3/PowerExfil/tree/master 🤔 ✅
ps1

https://github.com/vxunderground/MalwareSourceCode
Collection of malware source code for a variety of platforms in an array of different programming languages. (software)

https://github.com/HynekPetrak/javascript-malware-collection/tree/master 🤔
Collection of almost 40.000 javascript malware samples (obfuscated)

https://github.com/iosifache/DikeDataset/tree/main 🤔
Dataset with labeled benign and malicious files 🗃️ (.exe)

🏭 https://github.com/topics/malware-dataset
Here are 9 public repositories matching this topic...

https://github.com/Virus-Samples/Malware-Sample-Sources
(Malware Sample Sources - A Collection of Malware Sample Repositories)

This is a project created to make it easier for malware analysts to find virus samples for analysis, research, reverse engineering, or review. Malware can be tricky to find, much less having a solid understanding of all the possible places to find it, This is a living repository where we have attempted to document as many resources as possible in order to make your job easier. Please be sure to exercise EXTREME CAUTION when handling these files because as you well know, they have been designed and developed with malicious intent by their original authors. We believe in transparency and helping the good guys have the right access and tools they need to rip these malicious files apart.

https://github.com/urwithajit9/ClaMP
A Malware classifier dataset built with header fields’ values of Portable Executable files

https://github.com/4dsec/tritium?tab=readme-ov-file
The dataset is a .h5 file containing both the feature vector and metadata as a single Dataframe which can be loaded using pandas (key='xy'). 

https://github.com/Djaferbenchadi/Malware_analysis_binary 🤔
This project focuses on malware analysis, specifically targeting malware spoofing and binary classification challenges. We implement the Kernel Constrained Subspace Method (KCSM) augmented with Random Fourier Features (RFF_CSM) for efficient and effective malware detection.
Full paper from here: [https://ieeexplore.ieee.org/abstract/document/10215631](https://ieeexplore.ieee.org/abstract/document/10215631).
- Enhanced malware detection using KCSM, capable of distinguishing between malware and benign files.
- Improved computational efficiency with the integration of RFF, reducing the complexity of kernel calculations.
- Suitable for large-scale and real-time malware detection systems.

https://github.com/samratashok/nishang/tree/master?tab=readme-ov-file 🤔 ✅
Nishang - Offensive PowerShell for red team, penetration testing and offensive security.

https://github.com/phra/PEzor/tree/master
Open-Source Shellcode & PE Packer

https://github.com/CWright2022/powershell_malware/blob/main/wifi%20passwords.ps1 🤔 ✅
ps1

https://github.com/das-lab/mpsd?tab=readme-ov-file ✅
All samples are divided into three categories:
- **malicious_pure**: The samples are malicious.
- **powershell_benign_dataset**: The samples in it are benign.
- **mixed_malicious**: All samples are malicious, and each sample is composed of a malicious sample and a random benign sample.


---
[Top 7 malware sample databases and datasets for research and training | Infosec](https://resources.infosecinstitute.com/topics/malware-analysis/top-7-malware-sample-databases-and-datasets-for-research-and-training/)

[GitHub - ossf/malicious-packages: A repository of reports of malicious packages identified in Open Source package repositories, consumable via the Open Source Vulnerability (OSV) format.](https://github.com/ossf/malicious-packages)

[GitHub - shramos/Awesome-Cybersecurity-Datasets: A curated list of amazingly awesome Cybersecurity datasets](https://github.com/shramos/Awesome-Cybersecurity-Datasets)

https://github.com/404notf0und/AI-for-Security-Learning?tab=readme-ov-file
安全场景、基于AI的安全算法和安全数据分析学习笔记（偏工程类学习笔记），持续阅读，保持对业界技术的跟进和迭代

