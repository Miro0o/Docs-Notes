---
ai-generated: true
---

# LLM For Reverse Engineering And Binary Analysis

Back: [Academic Status](Academic-Status.md)

Scope: binary analysis, decompilation, deobfuscation, symbol recovery, shell-command explanation, malware/binary language models, and human-LLM reverse-engineering workflows.

Sources/time: 2024-present, checked on 2026-06-06. Formal entries draw from top security (IEEE S&P, USENIX Security, ACM CCS, NDSS), SE (ICSE, ESEC/FSE and FSE/PACMSE, ASE, ISSTA), PL (POPL, PLDI, OOPSLA, ICFP, primarily through PACMPL and relevant DBLP venue pages), and AI (NeurIPS, ICML, ICLR, AAAI) venues, plus selected journal, DBLP, DOI, or official accepted-paper/program pages when noted. arXiv entries come from targeted frontier sweeps over `cs.CR`, `cs.SE`, `cs.PL`, `cs.AI`, `cs.LG`, and `cs.CL`.

## Formal Published / Accepted Papers

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Hu2024DeGPT | [DeGPT: Optimizing Decompiler Output with LLM](https://www.ndss-symposium.org/ndss-paper/degpt-optimizing-decompiler-output-with-llm/) | 2024 | NDSS | Decompiler output | Improves readability of decompiled output with LLM post-processing. | Core |
| Lyu2024LiftFuzz | [LiftFuzz: Validating Binary Lifters through Context-aware Fuzzing with GPT](https://dblp.org/rec/conf/ccs/ZhouYSZCZ24) | 2024 | ACM CCS / DBLP | Binary lifter validation | Uses GPT-assisted context-aware fuzzing for lifter validation. | Core |
| Xie2024ReSym | [ReSym: Harnessing LLMs to Recover Variable and Data Structure Symbols from Stripped Binaries](https://dblp.org/rec/conf/ccs/Xie00X0024) | 2024 | ACM CCS / DBLP | Symbol recovery | Recovers analyst-meaningful symbols from stripped binaries. | Core |
| Zhou2025LATTE | [LATTE: LLM-Powered Static Binary Taint Analysis](https://doi.org/10.1145/3711816) | 2025 | ACM TOSEM | Binary taint | Uses LLMs for static binary taint semantics. | Core |
| Deng2025Raconteur | [RACONTEUR: A Knowledgeable, Insightful, and Portable LLM-Powered Shell Command Explainer](https://raconteur-ndss.github.io/) | 2025 | NDSS | Analyst assistance | Explains shell commands in security-analysis workflows. | Adjacent |
| Wei2025JsDeObsBench | [JsDeObsBench: Measuring and Benchmarking LLMs for JavaScript Deobfuscation](https://arxiv.org/abs/2506.20170) | 2025 | ACM CCS / arXiv | Deobfuscation benchmark | Benchmarks JavaScript deobfuscation by LLMs. | Core |
| Liu2025PDFMalwareIR | [Analyzing PDFs like Binaries: Adversarially Robust PDF Malware Analysis via Intermediate Representation and Language Model](https://dblp.org/rec/conf/ccs/Liu0ZLFP25) | 2025 | ACM CCS / DBLP | Malware analysis | Applies IR plus language model to PDF malware analysis. | Core |
| Nova2025AssemblyLM | [Nova: Generative Language Models for Assembly Code with Hierarchical Attention and Contrastive Learning](https://dblp.org/rec/conf/iclr/JiangWLX00B25) | 2025 | ICLR / DBLP | Assembly language model | Generative model for assembly code. | Adjacent |
| Su2025DiSCo | [DiSCo: Towards Decompiling EVM Bytecode to Source Code using Large Language Models](https://dblp.org/rec/journals/pacmse/SuLWNXZ25) | 2025 | FSE/PACMSE / DBLP | Smart-contract decompilation | LLM-assisted EVM bytecode decompilation. | Core |
| Wong2025DecLLM | [DecLLM: LLM-Augmented Recompilable Decompilation for Enabling Programmatic Use of Decompiled Code](https://dblp.org/rec/journals/pacmse/WongWWLLWTNW25) | 2025 | FSE/PACMSE / DBLP | Recompilable decompilation | Makes decompiled code usable programmatically. | Core |
| Li2026FidelityGPT | [FidelityGPT: Correcting Decompilation Distortions with Retrieval Augmented Generation](https://www.ndss-symposium.org/ndss-paper/fidelitygpt-correcting-decompilation-distortions-with-retrieval-augmented-generation/) | 2026 | NDSS | Decompiler correction | Uses RAG to correct decompilation distortions. | Frontier |
| Doupe2026HumanLLMSRE | [Decompiling the Synergy: An Empirical Study of Human-LLM Teaming in Software Reverse Engineering](https://dblp.org/rec/conf/ndss/BasqueDSGDSLWA26) | 2026 | NDSS / DBLP | Human-LLM SRE | Controlled evidence for reverse-engineering collaboration. | Adjacent |
| Jiang2026IRDecompilation | [Does Representation Matter? Evaluating IRs for LLM-based Binary Decompilation](https://www.ndss-symposium.org/ndss-paper/auto-draft-654/) | 2026 | NDSS BAR | Decompilation benchmark | Evaluates IR choices for LLM-based decompilation. | Frontier |
| Nishizaka2026LLMResistantProtection | [Towards LLM-Resistant Software Protection: Agent Failure Patterns in CTF Reverse Engineering](https://www.ndss-symposium.org/ndss-paper/auto-draft-657/) | 2026 | NDSS BAR | Agent failure modes | Maps LLM-agent failure patterns in reverse-engineering CTFs. | Frontier |
| Kurlandski2026MalwareLM | [Beyond Raw Bytes: Towards Large Malware Language Models](https://dblp.org/rec/conf/ndss/KurlandskiBPW26) | 2026 | NDSS / DBLP | Malware language models | Develops malware-oriented language-model direction. | Frontier |
| Xue2026RECoRD | [RECoRD: A Multi-Agent LLM Framework for Reverse Engineering Codebase to Relational Diagram](https://dblp.org/rec/conf/aaai/XueLBLN26) | 2026 | AAAI / DBLP | Codebase reverse engineering | Multi-agent system for reverse-engineering codebases into relational diagrams. | Frontier |

## arXiv / Frontier Preprints

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| 2604.03750 | [CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering](https://arxiv.org/abs/2604.03750) | 2026 | arXiv | Crypto RE benchmark | Benchmarks LLMs on cryptographic binary reverse engineering. | Frontier |
| 2601.20679 | [ShieldedCode: Learning Robust Representations for Virtual Machine Protected Code](https://arxiv.org/abs/2601.20679) | 2026 | arXiv | Software protection | Studies representations for protected/obfuscated code. | Frontier |
| 2606.05493 | [REStack: A Large-Scale Dataset of Reverse Engineering Discussions from Stack Exchange](https://arxiv.org/abs/2606.05493) | 2026 | arXiv | RE dataset | Dataset for reverse-engineering discussions and analyst workflows. | Frontier |

## Notes

- Evaluation should not rely only on exact-match metrics; analyst usefulness, speed, confidence, and error rates matter.
- Reverse-engineering assistant papers should be read with human-factors papers from `Human-Factor.md`.
