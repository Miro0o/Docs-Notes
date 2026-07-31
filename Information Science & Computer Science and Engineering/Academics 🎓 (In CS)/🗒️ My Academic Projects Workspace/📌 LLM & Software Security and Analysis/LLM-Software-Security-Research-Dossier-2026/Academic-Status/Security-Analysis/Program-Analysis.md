---
ai-generated: true
last-reviewed: 2026-07-30
---

# Security Analysis: Program Analysis

Back: [Academic Status](../Academic-Status.md)

Scope: static, taint, graph, symbolic/concolic, fuzzing/dynamic, and binary-analysis methods whose primary evaluated outcome is a vulnerability, exploitability judgment, security-relevant failure, malware finding, or verified defense. Fuzzing is a child topic here because it is an execution-backed program-analysis technique, not a peer taxonomy branch. Generic correctness testing, decompilation, and reverse engineering belong in the sibling software-research dossier.

Checked: 2026-07-30. Each paper has one canonical row in this dossier. Cross-cutting benchmark and OS/device views link here or to another primary home instead of copying rows.

Labels: `Core` = central, established contribution; `Frontier` = recent/preprint work needing follow-up; `Negative/Evaluation` = limits or comparative evidence; `Accepted/program record` = verified on an official 2026 program, but final bibliographic details may still change.

## Static, Taint, Graph, And Specification Analysis

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Li2024IRIS | [IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities](https://arxiv.org/abs/2405.17238) | 2025 | ICLR / arXiv | Static vulnerability analysis | Infers taint specifications and context while static analysis verifies flows. | Core |
| Lekssays2025LLMxCPG | [LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided LLMs](https://dblp.org/rec/conf/uss/LekssaysMT0K25) | 2025 | USENIX Security / DBLP | CPG-guided analysis | Selects analysis-relevant repository context with code-property graphs. | Core |
| Lin2026SpecAuditor | [SpecAuditor: Generating Audit Specifications for LLM-Driven Bug Detection](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | Audit specification | Makes generated audit specifications an explicit, checkable analysis artifact. | Accepted/program record |
| Qiu2026DNSLLM | [Knocking on the Front Door: An LLM-Guided Systematic Analysis of DNS Query Processing Vulnerabilities](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | Protocol analysis | Applies LLM-guided analysis to DNS query-processing attack surfaces. | Accepted/program record |
| Zhang2024GPTScan | [GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis](https://dblp.org/rec/conf/icse/0001WXLWXX024) | 2024 | ICSE / DBLP | Smart-contract analysis | Combines GPT semantic recognition with program analysis for logic flaws. | Core |
| Liu2025APIRules | [Generating API Parameter Security Rules with LLM for API Misuse Detection](https://dblp.org/rec/conf/ndss/LiuY0L25) | 2025 | NDSS / DBLP | API misuse | Generates parameter-security rules for a conventional checker. | Core |
| Yang2025MidasTouch | [The Midas Touch: Triggering the Capability of LLMs for RM-API Misuse Detection](https://dblp.org/rec/conf/ndss/YangL0L25) | 2025 | NDSS / DBLP | API misuse | Studies how to elicit and ground API-misuse reasoning. | Core |
| Yang2025KNighter | [KNighter: Transforming Static Analysis with LLM-Synthesized Checkers](https://doi.org/10.1145/3731569.3764827) | 2025 | SOSP | Kernel static analysis | Synthesizes checkers for Linux-kernel bug and vulnerability discovery. | Core |
| Ji2025Artemis | [Artemis: Toward Accurate Detection of Server-Side Request Forgeries through LLM-Assisted Inter-procedural Path-Sensitive Taint Analysis](https://dblp.org/rec/journals/pacmpl/JiDZTH25) | 2025 | PACMPL / DBLP | Taint analysis | Uses LLM assistance inside path-sensitive SSRF analysis. | Core |
| Ji2025STaint | [STaint: Detecting Second-Order Vulnerabilities in PHP Applications with LLM-Assisted Bi-Directional Static Taint Analysis](https://dblp.org/rec/conf/kbse/JiCH25) | 2025 | ASE / DBLP | Taint analysis | Adds LLM-derived semantics to bidirectional PHP taint analysis. | Core |
| Fleischer2026GONDAR | [Contextualizing Sink Knowledge for Java Vulnerability Discovery](https://arxiv.org/abs/2604.01645) | 2026 | IEEE S&P / arXiv | Sink-centric discovery | Joins sink semantics, reachability, and fuzzing feedback for Java vulnerabilities. | Core |
| Li2026Neo | [Detecting Privilege Escalation in Polyglot Microservices via Agentic Program Analysis](https://doi.org/10.1109/SP63933.2026.00121) | 2026 | IEEE S&P | Microservice analysis | Uses agentic cross-language analysis to detect privilege escalation in polyglot services. | Core |
| 2603.24837 | [Bridging Code Property Graphs and Language Models for Program Analysis](https://arxiv.org/abs/2603.24837) | 2026 | arXiv | CPG + LLM | Connects CPG structure with repository-scale vulnerability reasoning. | Frontier |
| 2603.27224 | [Finding Memory Leaks in C/C++ Programs via Neuro-Symbolic Augmented Static Analysis](https://arxiv.org/abs/2603.27224) | 2026 | arXiv | Resource analysis | Uses neuro-symbolic augmentation to find security-relevant memory leaks. | Frontier |
| 2601.12890 | [Efficient Code Analysis via Graph-Guided Large Language Models](https://arxiv.org/abs/2601.12890) | 2026 | arXiv | Graph-guided analysis | Targets malicious behavior fragmented across files. | Frontier |
| 2601.10865 | [Multi-Agent Taint Specification Extraction for Vulnerability Detection](https://arxiv.org/abs/2601.10865) | 2026 | arXiv | Taint specification | Extracts JavaScript taint specifications with multiple agents. | Frontier |
| 2603.28345 | [Where Code Meets Natural Language: Taxonomy-Driven Information Flow Analysis for LLM-Integrated Applications](https://arxiv.org/abs/2603.28345) | 2026 | arXiv | LLM-app information flow | Models prompt and model boundaries as information-flow edges. | Frontier |

## Symbolic, Concolic, And Formal Security Reasoning

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Luo2026ConcoLLMic | [Agentic Concolic Execution](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | Concolic execution | Uses agentic assistance in concolic path exploration. | Accepted/program record |
| Tu2026Cottontail | [Large Language Model-Driven Concolic Execution for Highly Structured Test Input Generation](https://arxiv.org/abs/2504.17542) | 2026 | IEEE S&P / arXiv | Concolic execution | Generates highly structured inputs under concolic guidance. | Core |
| Song2026ProtocolGuard | [ProtocolGuard: Detecting Protocol Non-compliance Bugs via LLM-guided Static Analysis and Dynamic Verification](https://dblp.org/rec/conf/ndss/SongPWZHZLZG26) | 2026 | NDSS / DBLP | Hybrid verification | Extracts protocol rules, narrows code statically, and verifies dynamically. | Core |
| PropertyGPT2025 | [PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation](https://dblp.org/rec/conf/ndss/0012XW00S025) | 2025 | NDSS / DBLP | Formal verification | Generates retrieval-grounded properties for smart-contract verification. | Core |
| Mao2025SecurityProtocolModeling | [LLM-Aided Automatic Modeling for Security Protocol Verification](https://dblp.org/rec/conf/icse/MaoWSQX25) | 2025 | ICSE / DBLP | Protocol verification | Translates protocol descriptions into models for verification. | Core |
| Yang2025Hyperion | [Hyperion: Unveiling DApp Inconsistencies Using LLM and Dataflow-Guided Symbolic Execution](https://dblp.org/rec/conf/icse/YangtLCZXHWZ25) | 2025 | ICSE / DBLP | Symbolic execution | Combines LLM semantics, dataflow, and symbolic execution for DApps. | Core |
| 2603.19239 | [Defusing Logic Bombs in Symbolic Execution with LLM-Generated Ghost Code](https://arxiv.org/abs/2603.19239) | 2026 | arXiv | Symbolic execution | Generates ghost code to bypass solver-hostile fragments. | Frontier |

## Fuzzing And Dynamic Analysis

The primary pattern is “LLM proposes; execution decides.” Device-, firmware-, kernel-, and OS-specific papers have their canonical rows in [Systems And OS Security](../Systems-And-OS-Security/Systems-And-OS-Security.md); benchmark-first papers are indexed in [Security Benchmarks And Evaluation](../Cross-Cutting/Security-Benchmarks-And-Evaluation.md).

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Meng2024ProtocolFuzzing | [Large Language Model Guided Protocol Fuzzing](https://dblp.org/rec/conf/ndss/MengMBR24) | 2024 | NDSS / DBLP | Protocol fuzzing | Infers protocol structure to guide generation and state exploration. | Core |
| Wang2024ProphetFuzz | [ProphetFuzz: Fully Automated Prediction and Fuzzing of High-Risk Option Combinations with Only Documentation via Large Language Model](https://dblp.org/rec/conf/ccs/WangZ00M24) | 2024 | ACM CCS / DBLP | Documentation-guided fuzzing | Mines documentation for risky option combinations. | Core |
| Lyu2024PromptFuzzing | [Prompt Fuzzing for Fuzz Driver Generation](https://dblp.org/rec/conf/ccs/LyuXCC24) | 2024 | ACM CCS / DBLP | Harness generation | Systematically searches prompt strategies for driver generation. | Core |
| Lyu2024LiftFuzz | [LiftFuzz: Validating Binary Lifters through Context-aware Fuzzing with GPT](https://dblp.org/rec/conf/ccs/ZhouYSZCZ24) | 2024 | ACM CCS / DBLP | Binary-lifter validation | Uses GPT context to fuzz and validate binary lifters. | Core |
| Zhang2025PromeFuzz | [PromeFuzz: A Knowledge-Driven Approach to Fuzzing Harness Generation with Large Language Models](https://dblp.org/rec/conf/ccs/LiuDJWWHWS25) | 2025 | ACM CCS / DBLP | Harness generation | Grounds harness generation in target knowledge. | Core |
| Yang2025HyLLFuzz | [Hybrid Language Processor Fuzzing via LLM-Based Constraint Solving](https://dblp.org/rec/conf/uss/YangYCL25) | 2025 | USENIX Security / DBLP | Constraint-guided fuzzing | Uses LLMs to solve constraints for language-processor fuzzing. | Core |
| Chen2025ELFuzz | [ELFuzz: Efficient Input Generation via LLM-driven Synthesis Over Fuzzer Space](https://dblp.org/rec/conf/uss/ChenDC25) | 2025 | USENIX Security / DBLP | Input generation | Synthesizes generators over a space of fuzzing strategies. | Core |
| Zhang2025NonTextualFuzzing | [Low-Cost and Comprehensive Non-textual Input Fuzzing with LLM-Synthesized Input Generators](https://dblp.org/rec/conf/uss/ZhangLW0025) | 2025 | USENIX Security / DBLP | Non-textual fuzzing | Produces target-specific generators for binary/non-textual inputs. | Core |
| Shiraishi2026PILOT | [PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | CLI fuzzing | Uses path feedback to generate option and input combinations. | Accepted/program record |
| Li2026DeepSURF | [deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses](https://arxiv.org/abs/2506.15648) | 2026 | IEEE S&P / arXiv | Rust memory safety | Generates Rust-aware harnesses around unsafe code. | Core |
| Lin2026R1Fuzz | [R1-Fuzz: Specializing Language Models for Textual Fuzzing via Reinforcement Learning](https://arxiv.org/abs/2509.20384) | 2026 | IEEE S&P / arXiv | Textual fuzzing | Specializes a model for security fuzzing with reinforcement learning. | Accepted/program record |
| Ye2026ProtocolFormats | [Generating Precise Format Specification for Network Protocols Through Adversarial LLM Interactions](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) | 2026 | USENIX Security | Protocol specification | Co-refines packet formats and parsers; inferred formats enable fuzzing and vulnerability discovery. | Accepted/program record |
| Wang2026Bulbasaur | [Bulbasaur: Branch-Guided Online Mutator Generation for Greybox Fuzzing](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) | 2026 | USENIX Security | Greybox fuzzing | Generates branch-specific online mutators from static and dynamic context. | Accepted/program record |
| Ma2025OpDiffer | [OpDiffer: LLM-Assisted Opcode-Level Differential Testing of Ethereum Virtual Machine](https://doi.org/10.1145/3728946) | 2025 | FSE/PACMSE / DOI | EVM security testing | Generates semantically valid opcode tests, localizes EVM implementation bugs, and reports confirmed vulnerabilities and CNVD identifiers. | Core |
| 2602.19490 | [FuzzySQL: Uncovering Hidden Vulnerabilities in DBMS Special Features with LLM-Driven Fuzzing](https://arxiv.org/abs/2602.19490) | 2026 | arXiv | DBMS fuzzing | Targets obscure database features with LLM-generated inputs. | Frontier |
| 2602.00667 | [zkCraft: Prompt-Guided LLM as a Zero-Shot Mutation Pattern Oracle for TCCT-Powered ZK Fuzzing](https://arxiv.org/abs/2602.00667) | 2026 | arXiv | ZK fuzzing | Supplies mutation patterns while a conventional fuzzer retains the oracle. | Frontier |

## Security-Targeted Binary Analysis, Reverse Engineering, And Malware

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Zhou2025LATTE | [LATTE: LLM-Powered Static Binary Taint Analysis](https://doi.org/10.1145/3711816) | 2025 | ACM TOSEM | Binary taint | Uses LLM assistance to recover semantics for binary taint analysis. | Core |
| Deng2025Raconteur | [RACONTEUR: A Knowledgeable, Insightful, and Portable LLM-Powered Shell Command Explainer](https://raconteur-ndss.github.io/) | 2025 | NDSS | Analyst assistance | Explains shell commands inside security-analysis workflows. | Core |
| Liu2025PDFMalwareIR | [Analyzing PDFs like Binaries: Adversarially Robust PDF Malware Analysis via Intermediate Representation and Language Model](https://dblp.org/rec/conf/ccs/Liu0ZLFP25) | 2025 | ACM CCS / DBLP | Malware analysis | Combines an intermediate representation and language model for robust PDF analysis. | Core |
| Wong2025DecLLM | [DecLLM: LLM-Augmented Recompilable Decompilation for Enabling Programmatic Use of Decompiled Code](https://dblp.org/rec/journals/pacmse/WongWWLLWTNW25) | 2025 | FSE/PACMSE / DBLP | Vulnerability-analysis enablement | Produces recompilable decompiled code for downstream programmatic analysis, including CodeQL-based vulnerability analysis. | Core |
| Doupe2026HumanLLMSRE | [Decompiling the Synergy: An Empirical Study of Human-LLM Teaming in Software Reverse Engineering](https://dblp.org/rec/conf/ndss/BasqueDSGDSLWA26) | 2026 | NDSS / DBLP | Security-analyst collaboration | Measures how LLM assistance changes security reverse-engineering performance and error. | Core |
| Kurlandski2026MalwareLM | [Beyond Raw Bytes: Towards Large Malware Language Models](https://dblp.org/rec/conf/ndss/KurlandskiBPW26) | 2026 | NDSS / DBLP | Malware modeling | Develops malware-oriented language-model representations. | Frontier |
| 2601.20679 | [ShieldedCode: Learning Robust Representations for Virtual Machine Protected Code](https://arxiv.org/abs/2601.20679) | 2026 | arXiv | Protected code | Studies robust representations for virtual-machine-protected binaries. | Frontier |

## Boundary And Cross-Links

- General verification, compiler testing, Android bug replay, ordinary test repair, generic decompilation, and general codebase understanding belong in the sibling [software-research dossier](../../../LLM-Software-Research-Dossier-2026/LLM-Software-Research-Dossier-2026.md) unless the paper evaluates a security property. Generic binary reconstruction has its canonical shelf under [Program Understanding, Binary Analysis, Decompilation, And Reverse Engineering](../../../LLM-Software-Research-Dossier-2026/Academic-Status/Program-Understanding-Binary-Analysis-Decompilation-And-Reverse-Engineering.md).
- Device- and OS-specific fuzzing: [Systems And OS Security](../Systems-And-OS-Security/Systems-And-OS-Security.md).
- Vulnerability detector reliability and proof-of-vulnerability workflows: [Detection, Triage, And Reasoning](../Vulnerability-Lifecycle/Detection-Triage-And-Reasoning.md).
- Benchmark and dataset views: [Security Benchmarks And Evaluation](../Cross-Cutting/Security-Benchmarks-And-Evaluation.md).
