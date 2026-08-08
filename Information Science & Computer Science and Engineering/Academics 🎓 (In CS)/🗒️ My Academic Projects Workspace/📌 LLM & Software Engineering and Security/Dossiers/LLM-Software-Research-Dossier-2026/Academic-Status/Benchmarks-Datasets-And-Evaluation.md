---
ai-generated: true
last-reviewed: 2026-07-30
---

# Benchmarks, Datasets, and Evaluation

Back: [Academic Status](Academic-Status.md)

Scope: benchmark design, task freshness, contamination, executable or formal oracles, environment reproducibility, cost reporting, and cross-topic evaluation. Full paper descriptions remain on their canonical topic pages.

## Published and Accepted Benchmark Index

| Benchmark | Year | Venue / evidence | Primary shelf | Main task and oracle |
| --- | ---: | --- | --- | --- |
| [SWE-bench](https://dblp.org/rec/conf/iclr/JimenezYWYPPN24) | 2024 | ICLR | [Software agents](Software-Agents-And-Repository-Engineering.md) | Real GitHub issues; repository patch tested against task tests. |
| [SWE-agent](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html) | 2024 | NeurIPS | [Software agents](Software-Agents-And-Repository-Engineering.md) | Evaluates agent-computer interfaces on repository repair and HumanEvalFix. |
| [SWT-Bench](https://dblp.org/rec/conf/nips/MundlerMHV24) | 2024 | NeurIPS | [Testing and repair](Testing-Debugging-And-General-Repair.md) | Real-world bug fixes with stronger test/validation focus. |
| [Mercury](https://dblp.org/rec/conf/nips/DuLJLN24) | 2024 | NeurIPS | [Performance](Performance-Optimization-And-Compilation.md) | Correctness plus execution efficiency. |
| [StackEval](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4126a607bbe2836cb6ca0eb45b75618b-Abstract-Datasets_and_Benchmarks_Track.html) | 2024 | NeurIPS Datasets & Benchmarks | [Program comprehension](Program-Comprehension-Search-Retrieval-Documentation-And-APIs.md) | Multilingual implementation, debugging, review, and conceptual-understanding assistance, plus a recent-data companion. |
| [LiveCodeBench](https://dblp.org/rec/conf/iclr/JainHGLYZWSSS25) | 2025 | ICLR | [Code generation](Code-Generation-Completion-And-Translation.md) | Continuously refreshed coding problems to reduce contamination. |
| [How Efficient Is LLM-Generated Code?](https://dblp.org/rec/conf/iclr/QiuZELT25) | 2025 | ICLR | [Performance](Performance-Optimization-And-Compilation.md) | High-standard runtime/resource evaluation. |
| [SWE-rebench](https://proceedings.neurips.cc/paper_files/paper/2025/hash/21bec6ace947b1b58967b945c8ac0f10-Abstract-Datasets_and_Benchmarks_Track.html) | 2025 | NeurIPS Datasets & Benchmarks | [Software agents](Software-Agents-And-Repository-Engineering.md) | Automated fresh-task collection and decontaminated interactive evaluation. |
| [Multi-SWE-bench](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5afa9cb1e917b898ad418216dc726fbd-Abstract-Datasets_and_Benchmarks_Track.html) | 2025 | NeurIPS Datasets & Benchmarks | [Software agents](Software-Agents-And-Repository-Engineering.md) | Multi-language repository issue resolution. |
| [DLBENCH](https://conf.researchr.org/track/ase-2025/ase-2025-papers) | 2025 | ASE / official program | [Domain-specific software](Domain-Specific-Low-Resource-Scientific-And-Data-Software.md) | SQL translation across database dialects. |
| [ResearchCodeBench](https://proceedings.neurips.cc/paper_files/paper/2025/hash/cd0d0a873cc3e601c76f46dccc3d4c5f-Abstract-Datasets_and_Benchmarks_Track.html) | 2025 | NeurIPS Datasets & Benchmarks | [Domain-specific software](Domain-Specific-Low-Resource-Scientific-And-Data-Software.md) | Implementation of novel ML research ideas from recent papers. |
| [VeriThoughts](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c946accd3ccc88c09dfae7e1cd40ffe-Abstract-Datasets_and_Benchmarks_Track.html) | 2025 | NeurIPS Datasets & Benchmarks | [Domain-specific software](Domain-Specific-Low-Resource-Scientific-And-Data-Software.md) | Verilog reasoning and code generation checked with formal verification. |
| [CodeSense: a Real-World Benchmark and Dataset for Code Semantic Reasoning](https://openreview.net/forum?id=ehXVDJm0PS) | 2026 | ICLR Poster / official record | [Program reasoning](Program-Analysis-Specification-Verification-And-Reasoning.md) | Fine-grained code understanding/reasoning evaluation. |
| [AutoCodeBench: Large Language Models are Automatic Code Benchmark Generators](https://openreview.net/forum?id=fN0MED2Idq) | 2026 | ICLR Poster / official record | [Code generation](Code-Generation-Completion-And-Translation.md) | Automatically constructed, current code-generation benchmark tasks. |
| [FeatureBench: Benchmarking Agentic Coding for Complex Feature Development](https://openreview.net/forum?id=41xrZ3uGuI) | 2026 | ICLR Poster / official record | [Software agents](Software-Agents-And-Repository-Engineering.md) | Repository-level feature implementation. |
| [SWR-Bench: Assessing LLM Performance in Real-World Code Review Comment Generation](https://conf.researchr.org/details/fse-2026/fse-2026-research-papers/78/SWR-Bench-Assessing-LLM-Performance-in-Real-World-Code-Review-Comment-Generation) | 2026 | FSE Research Papers / official program | [Code review and traceability](Code-Review-Change-Governance-And-Traceability.md) | Real pull requests with project context, structured ground truth, and human-aligned review-comment evaluation. |
| [Programming with Pixels](https://iclr.cc/virtual/2026/poster/10011120) | 2026 | ICLR Poster / official record | [Human-facing software](Human-Facing-Software-UI-UX-Education-And-Developer-Experience.md) | Visual IDE interaction across multimodal software-engineering tasks, with tool-API ablations. |
| [EmbedAgent](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | [Domain-specific software](Domain-Specific-Low-Resource-Scientific-And-Data-Software.md) | Embedded-system development rather than generic code generation. |
| [Does Representation Matter? Evaluating IRs for LLM-based Binary Decompilation](https://www.ndss-symposium.org/ndss-paper/auto-draft-654/) | 2026 | NDSS BAR / workshop record | [Binary understanding and decompilation](Program-Understanding-Binary-Analysis-Decompilation-And-Reverse-Engineering.md) | Controlled comparison of intermediate representations for binary reconstruction. |

## Frontier Benchmark Watchlist

These are useful signals, but remain preprints as of 2026-07-30.

| Benchmark | Source | Task | Main caution |
| --- | --- | --- | --- |
| [Asuka-Bench](https://arxiv.org/abs/2606.05920) | arXiv | Underspecified intent and multi-round refinement | Verify task provenance and independent tests. |
| [TensorBench](https://arxiv.org/abs/2606.05570) | arXiv | Compiler-backed tensor-framework agent tasks | Check environment portability and benchmark leakage. |
| [SmellBench](https://arxiv.org/abs/2606.05574) | arXiv | Fine-grained code-smell refactoring | Ensure behavior preservation, not style-only scoring. |
| [SWE-InfraBench](https://arxiv.org/abs/2606.05249) | arXiv | Cloud infrastructure code | Validate cloud semantics without unsafe live deployment. |

## Benchmark Quality Matrix

| Dimension | Weak evidence | Stronger evidence |
| --- | --- | --- |
| Freshness | fixed, widely trained-on tasks | dated collection protocol and continuously refreshed tasks |
| Oracle | exact string or LLM judge | executable tests, compiler, formal checker, or measured system behavior |
| Independence | generator writes both code and tests | hidden or independently generated tests/oracles |
| Environment | undocumented local setup | pinned container, dependencies, network policy, and replay script |
| Scope | isolated snippet | repository, build, history, tools, and multi-file change |
| Cost | pass rate only | tokens, tool calls, retries, time, compute, and human review |
| Robustness | one prompt/model | multiple models, seeds, scaffolds, perturbations, and confidence intervals |
| Contamination | assumed absent | temporal split, provenance checks, memorization analysis, and fresh tasks |

## Reporting Template

For every benchmark result, record:

1. model and checkpoint date;
2. prompt, scaffold, retrieval, and tools;
3. task/repository revision and data-release date;
4. execution environment and network access;
5. attempt, token, time, and cost budgets;
6. oracle provenance and flaky-test policy;
7. contamination controls;
8. success, partial success, invalid patch, and environment-failure counts;
9. complete trajectories or reproducible summaries.

## Avoid

- treating a public leaderboard as a stable model ranking;
- mixing accepted, preprint, and unpublished benchmark claims without labels;
- using an LLM judge as the only oracle for code correctness;
- counting build/environment failures as model reasoning failures without separation;
- duplicating a full paper record here when a canonical topic page already owns it.

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Allamanis2024UnsupervisedEvaluationCode | [Unsupervised Evaluation of Code LLMs with Round-Trip Correctness](<https://proceedings.mlr.press/v235/allamanis24a.html>) | 2024 | ICML / proceedings | Benchmarks Datasets And Evaluation | Benchmarks or evaluates unsupervised Evaluation of Code LLMs with Round-Trip Correctness; abstract-level contribution review remains pending. | formal-venue |
| Chen2024RmcbenchBenchmarkingLarge | [RMCBench: Benchmarking Large Language Models' Resistance to Malicious Code.](<https://doi.org/10.1145/3691620.3695480>) | 2024 | ASE / proceedings | Benchmarks Datasets And Evaluation | Introduces or evaluates rMCBench: Benchmarking Large Language Models' Resistance to Malicious Code; abstract-level contribution review remains pending. | formal-venue |
| Gong2024EvaluationLlmsSyntax | [Evaluation of LLMs on Syntax-Aware Code Fill-in-the-Middle Tasks](<https://proceedings.mlr.press/v235/gong24f.html>) | 2024 | ICML / proceedings | Benchmarks Datasets And Evaluation | Benchmarks or evaluates evaluation of LLMs on Syntax-Aware Code Fill-in-the-Middle Tasks; abstract-level contribution review remains pending. | formal-venue |
| OBrien2024ArePromptEngineering | [Are Prompt Engineering and TODO Comments Friends or Foes? An Evaluation on GitHub Copilot.](<https://doi.org/10.1145/3597503.3639176>) | 2024 | ICSE / proceedings | Benchmarks Datasets And Evaluation | Benchmarks or evaluates are Prompt Engineering and TODO Comments Friends or Foes? An Evaluation on GitHub Copilot; abstract-level contribution review remains pending. | formal-venue |
| Chi2025CopilotArenaPlatform | [Copilot Arena: A Platform for Code LLM Evaluation in the Wild](<https://proceedings.mlr.press/v267/chi25a.html>) | 2025 | ICML / proceedings | Benchmarks Datasets And Evaluation | Benchmarks or evaluates copilot Arena: A Platform for Code LLM Evaluation in the Wild; abstract-level contribution review remains pending. | formal-venue |
| Jain2025LivecodebenchHolisticContamination | [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](<https://openreview.net/forum?id=chfJJYC3iL>) | 2025 | ICLR / accepted-program | Benchmarks Datasets And Evaluation | Benchmarks or evaluates liveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code; abstract-level contribution review remains pending. | formal-venue |
| Si2026ScratchnetMultiModal | [ScratchNet: A Multi-modal Benchmark for Evaluating and Advancing LLMs on Scratch Programming Tasks](<https://conf.researchr.org/track/issta-2026/issta-2026-research-papers#event-e6154318-368a-4be8-aa97-9ba47babfe93>) | 2026 | ISSTA / accepted-program | Benchmarks Datasets And Evaluation | Benchmarks or evaluates scratchNet: A Multi-modal Benchmark for Evaluating and Advancing LLMs on Scratch Programming Tasks; abstract-level contribution review remains pending. | formal-venue |
| normalization2026InteractbenchBenchmarkingLlms | [InteractBench: Benchmarking LLMs on Competitive Programming under Unrevealed Information](<https://icml.cc/virtual/2026/poster/63326>) | 2026 | ICML / accepted-program | Benchmarks Datasets And Evaluation | Introduces or evaluates interactBench: Benchmarking LLMs on Competitive Programming under Unrevealed Information; abstract-level contribution review remains pending. | formal-venue |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
