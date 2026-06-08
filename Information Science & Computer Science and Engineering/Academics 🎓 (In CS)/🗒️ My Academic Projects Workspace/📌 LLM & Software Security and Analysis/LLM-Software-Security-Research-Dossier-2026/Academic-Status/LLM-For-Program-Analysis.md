---
ai-generated: true
---

# LLM For Program Analysis

Back: [Academic Status](Academic-Status.md)

Scope: LLMs as semantic/specification assistants for static analysis, taint analysis, symbolic/concolic execution, theorem proving, API misuse detection, and formal or semi-formal verification.

Sources/time: 2024-present, checked on 2026-06-06. Formal entries draw from top security (IEEE S&P, USENIX Security, ACM CCS, NDSS), SE (ICSE, ESEC/FSE and FSE/PACMSE, ASE, ISSTA), PL (POPL, PLDI, OOPSLA, ICFP, primarily through PACMPL and relevant DBLP venue pages), and AI (NeurIPS, ICML, ICLR, AAAI) venues, plus selected journal, DBLP, DOI, or official accepted-paper/program pages when noted. arXiv entries come from targeted frontier sweeps over `cs.CR`, `cs.SE`, `cs.PL`, `cs.AI`, `cs.LG`, and `cs.CL`.

## Formal Published / Accepted Papers

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Li2024IRIS | [IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities](https://arxiv.org/abs/2405.17238) | 2025 | ICLR / arXiv | Static analysis | Infers taint specs and context while static analysis verifies flows. | Core |
| Lekssays2025LLMxCPG | [LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided LLMs](https://dblp.org/rec/conf/uss/LekssaysMT0K25) | 2025 | USENIX Security / DBLP | CPG-guided analysis | Uses CPGs to select analysis-relevant context for LLM reasoning. | Core |
| Zhou2025LATTE | [LATTE: LLM-Powered Static Binary Taint Analysis](https://doi.org/10.1145/3711816) | 2025 | ACM TOSEM | Binary taint | Applies LLM assistance to recover taint rules in binary analysis. | Core |
| Lin2026SpecAuditor | [SpecAuditor: Generating Audit Specifications for LLM-Driven Bug Detection](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | Audit specs | Treats audit-spec generation as a first-class LLM-assisted analysis task. | Frontier |
| Luo2026ConcoLLMic | [Agentic Concolic Execution](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | Concolic execution | Adds LLM-agent assistance to concolic path exploration. | Core |
| Tu2026Cottontail | [Large Language Model-Driven Concolic Execution for Highly Structured Test Input Generation](https://arxiv.org/abs/2604.12426) | 2026 | IEEE S&P / arXiv | Concolic execution | Uses LLMs to generate structured inputs under concolic guidance. | Core |
| Song2026ProtocolGuard | [ProtocolGuard: Detecting Protocol Non-compliance Bugs via LLM-guided Static Analysis and Dynamic Verification](https://dblp.org/rec/conf/ndss/SongPWZHZLZG26) | 2026 | NDSS / DBLP | Protocol analysis | Extracts protocol rules, narrows code statically, verifies dynamically. | Core |
| Qiu2026DNSLLM | [Knocking on the Front Door: An LLM-Guided Systematic Analysis of DNS Query Processing Vulnerabilities](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | Domain-specific analysis | LLM-guided protocol analysis for DNS query processing. | Core |
| Zhang2024GPTScan | [GPTScan: Detecting Logic Vulnerabilities in Smart Contracts by Combining GPT with Program Analysis](https://dblp.org/rec/conf/icse/0001WXLWXX024) | 2024 | ICSE / DBLP | Smart contracts | Combines GPT with program analysis for smart-contract logic vulnerabilities. | Core |
| Liu2025APIRules | [Generating API Parameter Security Rules with LLM for API Misuse Detection](https://dblp.org/rec/conf/ndss/LiuY0L25) | 2025 | NDSS / DBLP | API misuse | Generates parameter security rules for misuse detection. | Core |
| Yang2025MidasTouch | [The Midas Touch: Triggering the Capability of LLMs for RM-API Misuse Detection](https://dblp.org/rec/conf/ndss/YangL0L25) | 2025 | NDSS / DBLP | API misuse | Studies how to elicit API-misuse detection capability. | Core |
| PropertyGPT2025 | [PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation](https://dblp.org/rec/conf/ndss/0012XW00S025) | 2025 | NDSS / DBLP | Formal verification | Generates formal properties for smart-contract verification. | Core |
| Thompson2025Rango | [Rango: Adaptive Retrieval-Augmented Proving for Automated Software Verification](https://dblp.org/rec/conf/icse/ThompsonSCFSB0L25) | 2025 | ICSE / DBLP | Software verification | Retrieval-augmented proving for verification tasks. | Core |
| Mao2025SecurityProtocolModeling | [LLM-Aided Automatic Modeling for Security Protocol Verification](https://dblp.org/rec/conf/icse/MaoWSQX25) | 2025 | ICSE / DBLP | Protocol verification | Uses LLMs to model security protocols for verification. | Core |
| Patel2025RuntimeErrorStaticDetection | [Planning a Large Language Model for Static Detection of Runtime Errors in Code Snippets](https://dblp.org/rec/conf/icse/PatelYDN25) | 2025 | ICSE / DBLP | Static detection | Uses planning with LLMs for runtime-error static detection. | Adjacent |
| Yang2025Hyperion | [Hyperion: Unveiling DApp Inconsistencies Using LLM and Dataflow-Guided Symbolic Execution](https://dblp.org/rec/conf/icse/YangtLCZXHWZ25) | 2025 | ICSE / DBLP | Dataflow/symbolic | Combines LLMs and symbolic execution for DApp inconsistency detection. | Core |
| Li2024StaticBugDetection | [Enhancing Static Analysis for Practical Bug Detection: An LLM-Integrated Approach](https://dblp.org/rec/journals/pacmpl/LiHZQ24) | 2024 | PACMPL / DBLP | Static analysis | Integrates LLM support into practical static bug detection. | Core |
| Mugnier2025Laurel | [Laurel: Unblocking Automated Verification with Large Language Models](https://dblp.org/rec/journals/pacmpl/MugnierGPJY25) | 2025 | PACMPL / DBLP | Automated verification | Uses LLMs to help automated verification progress through blockers. | Core |
| Ji2025Artemis | [Artemis: Toward Accurate Detection of Server-Side Request Forgeries through LLM-Assisted Inter-procedural Path-Sensitive Taint Analysis](https://dblp.org/rec/journals/pacmpl/JiDZTH25) | 2025 | PACMPL / DBLP | Taint analysis | LLM-assisted path-sensitive taint analysis for SSRF. | Core |
| Li2025LLMSymbolicExecution | [Large Language Model Powered Symbolic Execution](https://dblp.org/rec/journals/pacmpl/LiMD25) | 2025 | PACMPL / DBLP | Symbolic execution | Adds LLM reasoning to symbolic execution. | Core |
| Fein2025LitterBoxPlus | [LitterBox+: An Extensible Framework for LLM-enhanced Scratch Static Code Analysis](https://dblp.org/rec/conf/kbse/FeinOF25) | 2025 | ASE / DBLP | Static analysis | Uses LLMs to enhance static analysis in an educational language setting. | Adjacent |
| Ji2025STaint | [STaint: Detecting Second-Order Vulnerabilities in PHP Applications with LLM-Assisted Bi-Directional Static Taint Analysis](https://dblp.org/rec/conf/kbse/JiCH25) | 2025 | ASE / DBLP | Taint analysis | LLM-assisted bidirectional taint for second-order PHP vulnerabilities. | Core |

## arXiv / Frontier Preprints

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| 2603.24837 | [Bridging Code Property Graphs and Language Models for Program Analysis](https://arxiv.org/abs/2603.24837) | 2026 | arXiv | CPG + LLM | Connects CPGs with LLMs for repository-scale vulnerability analysis. | Frontier |
| 2603.27224 | [Finding Memory Leaks in C/C++ Programs via Neuro-Symbolic Augmented Static Analysis](https://arxiv.org/abs/2603.27224) | 2026 | arXiv | Static analysis | Uses neuro-symbolic augmentation to improve memory-leak analysis. | Frontier |
| 2601.12890 | [Efficient Code Analysis via Graph-Guided Large Language Models](https://arxiv.org/abs/2601.12890) | 2026 | arXiv | Graph-guided analysis | Targets malicious behavior fragmented across files. | Frontier |
| 2601.10865 | [Multi-Agent Taint Specification Extraction for Vulnerability Detection](https://arxiv.org/abs/2601.10865) | 2026 | arXiv | Taint specs | Extracts taint specifications for JavaScript vulnerability detection. | Frontier |
| 2603.28345 | [Where Code Meets Natural Language: Taxonomy-Driven Information Flow Analysis for LLM-Integrated Applications](https://arxiv.org/abs/2603.28345) | 2026 | arXiv | LLM-app information flow | Models prompt/LLM boundaries as program-analysis targets. | Frontier |
| 2603.19239 | [Defusing Logic Bombs in Symbolic Execution with LLM-Generated Ghost Code](https://arxiv.org/abs/2603.19239) | 2026 | arXiv | Symbolic execution | Uses LLM-generated ghost code to bypass solver-hostile fragments. | Frontier |
| 2604.00039 | [Transformers for Program Termination](https://arxiv.org/abs/2604.00039) | 2026 | arXiv | Program analysis | Studies transformer recognition of termination patterns. | Frontier |

## Notes

- The strongest pattern is still "LLM proposes, analyzer verifies."
- The most publishable open question is how to record which LLM-generated specifications or summaries were actually checked by a verifier.
