---
ai-generated: true
---

# LLM For Reverse Engineering And Binary Analysis

Back: [Academic Status](Academic-Status.md)

Scope: binary analysis, decompilation, deobfuscation, symbol recovery, shell-command explanation, malware/binary language models, and human-LLM reverse-engineering workflows.

| Key | Paper | Year | Venue/source | Area fit | Contribution | Label | Link |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| Hu2024DeGPT | DeGPT: Optimizing Decompiler Output with LLM | 2024 | NDSS | Decompiler output | Improves readability of decompiled output with LLM post-processing. | Core | https://www.ndss-symposium.org/ndss-paper/degpt-optimizing-decompiler-output-with-llm/ |
| Lyu2024LiftFuzz | LiftFuzz: Validating Binary Lifters through Context-aware Fuzzing with GPT | 2024 | ACM CCS / DBLP | Binary lifter validation | Uses GPT-assisted context-aware fuzzing for lifter validation. | Core | https://dblp.org/rec/conf/ccs/ZhouYSZCZ24 |
| Xie2024ReSym | ReSym: Harnessing LLMs to Recover Variable and Data Structure Symbols from Stripped Binaries | 2024 | ACM CCS / DBLP | Symbol recovery | Recovers analyst-meaningful symbols from stripped binaries. | Core | https://dblp.org/rec/conf/ccs/Xie00X0024 |
| Zhou2025LATTE | LATTE: LLM-Powered Static Binary Taint Analysis | 2025 | ACM TOSEM | Binary taint | Uses LLMs for static binary taint semantics. | Core | https://doi.org/10.1145/3711816 |
| Deng2025Raconteur | RACONTEUR: A Knowledgeable, Insightful, and Portable LLM-Powered Shell Command Explainer | 2025 | NDSS | Analyst assistance | Explains shell commands in security-analysis workflows. | Adjacent | https://raconteur-ndss.github.io/ |
| Wei2025JsDeObsBench | JsDeObsBench: Measuring and Benchmarking LLMs for JavaScript Deobfuscation | 2025 | ACM CCS / arXiv | Deobfuscation benchmark | Benchmarks JavaScript deobfuscation by LLMs. | Core | https://arxiv.org/abs/2506.20170 |
| Liu2025PDFMalwareIR | Analyzing PDFs like Binaries: Adversarially Robust PDF Malware Analysis via Intermediate Representation and Language Model | 2025 | ACM CCS / DBLP | Malware analysis | Applies IR plus language model to PDF malware analysis. | Core | https://dblp.org/rec/conf/ccs/Liu0ZLFP25 |
| Nova2025AssemblyLM | Nova: Generative Language Models for Assembly Code with Hierarchical Attention and Contrastive Learning | 2025 | ICLR / DBLP | Assembly language model | Generative model for assembly code. | Adjacent | https://dblp.org/rec/conf/iclr/JiangWLX00B25 |
| Su2025DiSCo | DiSCo: Towards Decompiling EVM Bytecode to Source Code using Large Language Models | 2025 | FSE/PACMSE / DBLP | Smart-contract decompilation | LLM-assisted EVM bytecode decompilation. | Core | https://dblp.org/rec/journals/pacmse/SuLWNXZ25 |
| Wong2025DecLLM | DecLLM: LLM-Augmented Recompilable Decompilation for Enabling Programmatic Use of Decompiled Code | 2025 | FSE/PACMSE / DBLP | Recompilable decompilation | Makes decompiled code usable programmatically. | Core | https://dblp.org/rec/journals/pacmse/WongWWLLWTNW25 |
| Li2026FidelityGPT | FidelityGPT: Correcting Decompilation Distortions with Retrieval Augmented Generation | 2026 | NDSS | Decompiler correction | Uses RAG to correct decompilation distortions. | Frontier | https://www.ndss-symposium.org/ndss-paper/fidelitygpt-correcting-decompilation-distortions-with-retrieval-augmented-generation/ |
| Doupe2026HumanLLMSRE | Decompiling the Synergy: An Empirical Study of Human-LLM Teaming in Software Reverse Engineering | 2026 | NDSS / DBLP | Human-LLM SRE | Controlled evidence for reverse-engineering collaboration. | Adjacent | https://dblp.org/rec/conf/ndss/BasqueDSGDSLWA26 |
| Jiang2026IRDecompilation | Does Representation Matter? Evaluating IRs for LLM-based Binary Decompilation | 2026 | NDSS BAR | Decompilation benchmark | Evaluates IR choices for LLM-based decompilation. | Frontier | https://www.ndss-symposium.org/ndss-paper/auto-draft-654/ |
| Nishizaka2026LLMResistantProtection | Towards LLM-Resistant Software Protection: Agent Failure Patterns in CTF Reverse Engineering | 2026 | NDSS BAR | Agent failure modes | Maps LLM-agent failure patterns in reverse-engineering CTFs. | Frontier | https://www.ndss-symposium.org/ndss-paper/auto-draft-657/ |
| Kurlandski2026MalwareLM | Beyond Raw Bytes: Towards Large Malware Language Models | 2026 | NDSS / DBLP | Malware language models | Develops malware-oriented language-model direction. | Frontier | https://dblp.org/rec/conf/ndss/KurlandskiBPW26 |
| 2604.03750 | CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering | 2026 | arXiv | Crypto RE benchmark | Benchmarks LLMs on cryptographic binary reverse engineering. | Frontier | https://arxiv.org/abs/2604.03750 |
| 2601.20679 | ShieldedCode: Learning Robust Representations for Virtual Machine Protected Code | 2026 | arXiv | Software protection | Studies representations for protected/obfuscated code. | Frontier | https://arxiv.org/abs/2601.20679 |
| 2606.05493 | REStack: A Large-Scale Dataset of Reverse Engineering Discussions from Stack Exchange | 2026 | arXiv | RE dataset | Dataset for reverse-engineering discussions and analyst workflows. | Frontier | https://arxiv.org/abs/2606.05493 |
| Xue2026RECoRD | RECoRD: A Multi-Agent LLM Framework for Reverse Engineering Codebase to Relational Diagram | 2026 | AAAI / DBLP | Codebase reverse engineering | Multi-agent system for reverse-engineering codebases into relational diagrams. | Frontier | https://dblp.org/rec/conf/aaai/XueLBLN26 |

## Notes

- Evaluation should not rely only on exact-match metrics; analyst usefulness, speed, confidence, and error rates matter.
- Reverse-engineering assistant papers should be read with human-factors papers from `Human-Factor.md`.
