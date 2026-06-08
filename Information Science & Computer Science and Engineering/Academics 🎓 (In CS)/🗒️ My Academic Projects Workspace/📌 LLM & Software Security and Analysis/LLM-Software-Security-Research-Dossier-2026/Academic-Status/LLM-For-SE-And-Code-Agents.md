---
ai-generated: true
---

# LLM For SE And Code Agents

Back: [Academic Status](Academic-Status.md)

Scope: repository-level coding, code generation, code-agent interfaces, software-failure localization, code-agent evaluation, and code-agent risks that matter for security workflows.

Sources/time: 2024-present, checked on 2026-06-06. Formal entries draw from top security (IEEE S&P, USENIX Security, ACM CCS, NDSS), SE (ICSE, ESEC/FSE and FSE/PACMSE, ASE, ISSTA), PL (POPL, PLDI, OOPSLA, ICFP, primarily through PACMPL and relevant DBLP venue pages), and AI (NeurIPS, ICML, ICLR, AAAI) venues, plus selected journal, DBLP, DOI, or official accepted-paper/program pages when noted. arXiv entries come from targeted frontier sweeps over `cs.CR`, `cs.SE`, `cs.PL`, `cs.AI`, `cs.LG`, and `cs.CL`.

## Formal Published / Accepted Papers

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Jimenez2024SWEBench | [SWE-bench: Can Language Models Resolve Real-world GitHub Issues?](https://dblp.org/rec/conf/iclr/JimenezYWYPPN24) | 2024 | ICLR / DBLP | SE/code-agent benchmark | Establishes repository-level issue resolution as a hard baseline for coding agents. | Core |
| Yang2024SWEAgent | [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://dblp.org/rec/conf/nips/YangJWLYNP24) | 2024 | NeurIPS / DBLP | SE/code agents | Shows that agent-computer interface design strongly affects SWE-bench performance. | Core |
| Bairi2024CodePlan | [CodePlan: Repository-Level Coding using LLMs and Planning](https://dblp.org/rec/journals/pacmse/BairiSKCIPRAS24) | 2024 | FSE/PACMSE / DBLP | Repo-level planning | Uses planning to decompose repository coding tasks. | Core |
| Guo2024CodeRefinement | [Exploring the Potential of ChatGPT in Automated Code Refinement: An Empirical Study](https://dblp.org/rec/conf/icse/GuoCXLL0024) | 2024 | ICSE / DBLP | Code refinement | Empirically studies ChatGPT for refinement-style code changes. | Adjacent |
| Nam2024CodeUnderstanding | [Using an LLM to Help With Code Understanding](https://dblp.org/rec/conf/icse/NamMHVM24) | 2024 | ICSE / DBLP | Code understanding | Studies LLM support for developer code comprehension. | Adjacent |
| Izadi2024CodeCompletion | [Language Models for Code Completion: A Practical Evaluation](https://dblp.org/rec/conf/icse/IzadiKDOPD24) | 2024 | ICSE / DBLP | Code completion | Practical evaluation of code-completion models and failure modes. | Adjacent |
| Pan2024CodeTranslationBugs | [Lost in Translation: A Study of Bugs Introduced by Large Language Models while Translating Code](https://dblp.org/rec/conf/icse/PanIKSWMSPSJ24) | 2024 | ICSE / DBLP | Translation risk | Shows code translation can introduce bugs, relevant to secure migration. | Negative/Evaluation |
| Muennighoff2024OctoPack | [OctoPack: Instruction Tuning Code Large Language Models](https://dblp.org/rec/conf/iclr/MuennighoffLZZH24) | 2024 | ICLR / DBLP | Code model training | Important code-LLM instruction-tuning baseline. | Adjacent |
| Holt2024L2MAC | [L2MAC: Large Language Model Automatic Computer for Extensive Code Generation](https://dblp.org/rec/conf/iclr/HoltLS24) | 2024 | ICLR / DBLP | Code generation | Agentic code generation system for larger tasks. | Adjacent |
| Luo2024WizardCoder | [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://dblp.org/rec/conf/iclr/LuoX0SGHT0LJ24) | 2024 | ICLR / DBLP | Code model training | Influential instruction-tuning approach for code LLMs. | Adjacent |
| Jiang2024LeDex | [LeDex: Training LLMs to Better Self-Debug and Explain Code](https://dblp.org/rec/conf/nips/Jiang00ZHRK0D24) | 2024 | NeurIPS / DBLP | Debugging/explanation | Trains models for self-debugging and code explanation. | Core |
| Bhatia2024Transpilation | [Verified Code Transpilation with LLMs](https://dblp.org/rec/conf/nips/BhatiaQHSC24) | 2024 | NeurIPS / DBLP | Code translation/verification | Uses verification to constrain LLM-assisted transpilation. | Core |
| Mundler2024SWTBench | [SWT-Bench: Testing and Validating Real-World Bug-Fixes with Code Agents](https://dblp.org/rec/conf/nips/MundlerMHV24) | 2024 | NeurIPS / DBLP | Bug-fix evaluation | Adds a real-world bug-fix validation benchmark for code agents. | Core |
| Guo2024RedCode | [RedCode: Risky Code Execution and Generation Benchmark for Code Agents](https://dblp.org/rec/conf/nips/GuoLXZZ0SL24) | 2024 | NeurIPS / DBLP | Code-agent risk benchmark | Evaluates risky code execution/generation behavior in code agents. | Core |
| Wang2025PlanningCodeGen | [Planning in Natural Language Improves LLM Search for Code Generation](https://dblp.org/rec/conf/iclr/WangCWBSNHHYZ25) | 2025 | ICLR / DBLP | Code generation search | Shows natural-language planning improves search over generated code. | Core |
| Antoniades2025SWESearch | [SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement](https://dblp.org/rec/conf/iclr/AntoniadesOZXGW25) | 2025 | ICLR / DBLP | Code agents | Applies MCTS and refinement to software agents. | Core |
| Xu2025OpenRCA | [OpenRCA: Can Large Language Models Locate the Root Cause of Software Failures?](https://dblp.org/rec/conf/iclr/XuZZHZLPHZ025) | 2025 | ICLR / DBLP | Failure localization | Evaluates root-cause localization for software failures. | Core |
| Hu2025MultiAgentSE | [Self-Evolving Multi-Agent Collaboration Networks for Software Development](https://dblp.org/rec/conf/iclr/HuCDZLYHTC25) | 2025 | ICLR / DBLP | Multi-agent SE | Studies collaboration networks for software-development agents. | Frontier |
| Zhang2025SoftwareAgents | [Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://dblp.org/rec/conf/iclr/ZhangYLFLNLLL0025) | 2025 | ICLR / DBLP | Multi-agent SE | Uses agent expertise diversity for SE tasks. | Frontier |
| Wang2025DeprecatedAPI | [LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-Based Code Completion](https://dblp.org/rec/conf/icse/Wang0ZFZ0025) | 2025 | ICSE / DBLP | API evolution | Tests whether code completion keeps up with library/API evolution. | Negative/Evaluation |
| Chen2025RuntimeBehavior | [Reasoning Runtime Behavior of a Program with LLM: How Far are We?](https://dblp.org/rec/conf/icse/ChenP000025) | 2025 | ICSE / DBLP | Program behavior reasoning | Evaluates limits of LLM reasoning about runtime behavior. | Negative/Evaluation |
| Bouzenia2025RepairAgent | [RepairAgent: An Autonomous, LLM-Based Agent for Program Repair](https://dblp.org/rec/conf/icse/BouzeniaDP25) | 2025 | ICSE / DBLP | Repair agent | Agent-oriented program repair system. | Core |
| Deligiannis2025RustAssistant | [RustAssistant: Using LLMs to Fix Compilation Errors in Rust Code](https://dblp.org/rec/conf/icse/DeligiannisLMPR25) | 2025 | ICSE / DBLP | Rust repair | Uses LLMs to fix Rust compilation errors. | Adjacent |
| Xia2025SEAgents | [Demystifying LLM-Based Software Engineering Agents](https://dblp.org/rec/journals/pacmse/XiaDDZ25) | 2025 | FSE/PACMSE / DBLP | SE-agent evaluation | Characterizes behavior and limits of LLM SE agents. | Core |
| Yu2025CXXCrafter | [CXXCrafter: An LLM-Based Agent for Automated C/C++ Open Source Software Building](https://dblp.org/rec/journals/pacmse/YuZWNZY25) | 2025 | FSE/PACMSE / DBLP | Build agents | Automates C/C++ OSS building, relevant to vulnerability reproduction. | Core |
| Ma2025SWEGPT | [SWE-GPT: A Process-Centric Language Model for Automated Software Improvement](https://dblp.org/rec/journals/pacmse/MaCCZCLLLHL25) | 2025 | FSE/PACMSE / DBLP | Automated improvement | Process-centric model for software-improvement tasks. | Adjacent |
| Gao2025CodeOptimization | [Search-Based LLMs for Code Optimization](https://dblp.org/rec/conf/icse/Gao0GL25) | 2025 | ICSE / DBLP | Code optimization | Uses search for LLM-driven code optimization. | Adjacent |
| Qiu2025CodeEfficiency | [How efficient is LLM-generated code? A rigorous & high-standard benchmark](https://dblp.org/rec/conf/iclr/QiuZELT25) | 2025 | ICLR / DBLP | Code-efficiency benchmark | Evaluates efficiency, not just correctness, of generated code. | Negative/Evaluation |

## arXiv / Frontier Preprints

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| 2606.05920 | [Asuka-Bench: Benchmarking Code Agents on Underspecified User Intent and Multi-Round Refinement](https://arxiv.org/abs/2606.05920) | 2026 | arXiv | Code-agent benchmark | Benchmarks multi-round refinement from underspecified user intent. | Frontier |
| 2606.05570 | [TensorBench: Benchmarking Coding Agents on a Compiler-Based Tensor Framework](https://arxiv.org/abs/2606.05570) | 2026 | arXiv | Code-agent benchmark | Compiler-backed benchmark for reliable code-agent evaluation. | Frontier |
| 2606.05574 | [SmellBench: Towards Fine-Grained Evaluation of Code Agents on Refactoring Tasks](https://arxiv.org/abs/2606.05574) | 2026 | arXiv | Refactoring benchmark | Evaluates code agents on code-smell and refactoring tasks. | Frontier |
| 2606.05249 | [SWE-InfraBench: Evaluating Language Models on Cloud Infrastructure Code](https://arxiv.org/abs/2606.05249) | 2026 | arXiv | IaC benchmark | Focuses on infrastructure-as-code, where reliability/security interact. | Frontier |
| 2603.01896 | [Agentic Code Reasoning](https://arxiv.org/abs/2603.01896) | 2026 | arXiv | Codebase reasoning | Studies codebase reasoning without execution. | Frontier |
| 2601.11840 | [Imandra CodeLogician: Neuro-Symbolic Reasoning for Precise Analysis of Software Logic](https://arxiv.org/abs/2601.11840) | 2026 | arXiv | Code logic reasoning | Combines LLMs and symbolic reasoning for precise software logic analysis. | Frontier |

## Notes

- The security relevance here is indirect but important: repository navigation, build reproduction, failure localization, and reliable edits are prerequisites for vulnerability validation and patch delivery.
- Benchmark contamination and oracle quality remain central concerns; prefer dynamically validated tasks over static output matching.
