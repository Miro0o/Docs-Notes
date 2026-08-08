---
ai-generated: true
last-reviewed: 2026-07-30
---

# Domain-Specific, Low-Resource, Scientific, and Data Software

Back: [Academic Status](Academic-Status.md)

Scope: LLM-assisted software work where the language, artifact, execution environment, or correctness oracle is specific to science, data, databases, hardware, embedded systems, mobile applications, or another specialized domain. This page also tracks programming languages that receive too little training and evaluation coverage to inherit results from Python or Java.

## Status

General coding scores transfer poorly to specialized software. SQL dialects, Verilog and RTL, embedded toolchains, edge-device constraints, scientific specifications, and low-resource languages each impose different syntax, build systems, libraries, and behavioral oracles. The strongest work therefore uses domain compilers, formal equivalence, physical or deployment measurements, held-out data, or expert-checked research implementations.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Domain contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Cassano2024LowResourcePL | [Knowledge Transfer from High-Resource to Low-Resource Programming Languages for Code LLMs](https://doi.org/10.1145/3689735) | 2024 | OOPSLA/PACMPL / DOI | Builds validated training data for Julia, Lua, OCaml, R, and Racket by translating and testing high-resource examples. | Published |
| Trirat2025AutoMLAgent | [AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML](https://proceedings.mlr.press/v267/trirat25a.html) | 2025 | ICML/PMLR / proceedings | Automates data retrieval, preprocessing, model design, verification, and deployment across an ML pipeline. | Published |
| Lin2025DLBench | [DLBENCH: A Comprehensive Benchmark for SQL Translation with Large Language Models](https://conf.researchr.org/track/ase-2025/ase-2025-papers) | 2025 | ASE Research Papers / official program | Evaluates translation across SQL dialects, exposing database-specific interoperability failures. | Official program / Evaluation |
| Hua2025ResearchCodeBench | [ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Research Code](https://proceedings.neurips.cc/paper_files/paper/2025/hash/cd0d0a873cc3e601c76f46dccc3d4c5f-Abstract-Datasets_and_Benchmarks_Track.html) | 2025 | NeurIPS Datasets & Benchmarks / proceedings | Tests implementation of recent ML research ideas that postdate likely pretraining exposure. | Published / Evaluation |
| Yubeaton2025VeriThoughts | [VeriThoughts: Enabling Automated Verilog Code Generation using Reasoning and Formal Verification](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c946accd3ccc88c09dfae7e1cd40ffe-Abstract-Datasets_and_Benchmarks_Track.html) | 2025 | NeurIPS Datasets & Benchmarks / proceedings | Provides reasoning data and a formally checked benchmark for Verilog generation. | Published / Evaluation |
| Wang2025SymRTLO | [SymRTLO: Enhancing RTL Code Optimization with LLMs and Neuron-Inspired Symbolic Reasoning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/479922a6341a8035f75bcc11598ae1a9-Abstract-Conference.html) | 2025 | NeurIPS / proceedings | Combines LLM rewriting, RTL rules, symbolic FSM optimization, formal equivalence, and synthesis measurements. | Published |
| Rmus2025GeCCo | [Generating Computational Cognitive Models using Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7f14c9df045c5b58893a87079d16d2b3-Abstract-Conference.html) | 2025 | NeurIPS / proceedings | Iteratively generates executable cognitive models and refines them against held-out behavioral data. | Published |
| BoruchGruszecki2026Agnostics | [Agnostics: Learning to Synthesize Code in Any Programming Language with a Universal Reinforcement Learning Environment](https://iclr.cc/virtual/2026/poster/10007548) | 2026 | ICLR Poster / official record | Uses language-agnostic execution rewards to improve code synthesis for Lua, Julia, R, OCaml, and Fortran. | Published |
| Ran2026IndependentDeveloper | [From Assistant to Independent Developer—Are GPTs Ready for Software Development?](https://iclr.cc/virtual/2026/poster/10008933) | 2026 | ICLR Poster / official record | Evaluates whole Android-application construction from specifications with lifecycle-aware executable tests. | Published / Evaluation |
| Xu2026EmbedAgent | [EmbedAgent: Benchmarking Large Language Models in Embedded System Development](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Establishes an embedded-development benchmark rather than extrapolating from general code tasks. | Official program / Evaluation |
| Wen2026AdaptiveIoT | [End-to-End Model Generation with Large Language Models for Adaptive IoT Application Deployment](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/243/End-to-End-Model-Generation-with-Large-Language-Models-for-Adaptive-IoT-Application-D) | 2026 | ICSE Research Track / official program | Generates and adapts DNN software artifacts under measured edge-device accuracy and latency constraints. | Official program |

## Existing Foundations on Other Shelves

- [Paper2Code](Code-Generation-Completion-And-Translation.md) remains the canonical scientific-paper-to-code record.
- QiMeng-Xpiler and compiler-guided tensor work remain under [Performance Optimization and Compilation](Performance-Optimization-And-Compilation.md).
- The FSE low-resource and domain-specific code-generation survey remains under [Surveys and Systematization](Surveys-And-Systematization.md).

## Domain-Oracles Matrix

| Domain | Minimum credible oracle |
| --- | --- |
| Database and SQL | execution on named DBMS versions, result equivalence, and dialect/error classification |
| Hardware description | compilation/synthesis, simulation, formal equivalence, and power-performance-area measurements |
| Embedded and IoT | real or faithfully emulated toolchain, hardware constraints, latency/resource measurements, and device behavior |
| Scientific or ML code | held-out data, reference equations/algorithms, reproducible environment, and expert or experiment-backed validation |
| Low-resource language | compiler/runtime execution, language-specific tests, and contamination-aware cross-language comparison |
| Mobile application | lifecycle-aware build and UI/behavioral tests across app states |

## Research Gaps

- representative repositories and toolchains for languages outside the dominant benchmark set;
- scientific validation that checks equations, units, data assumptions, and numerical stability;
- database tasks beyond text-to-SQL, including migration, query plans, transactions, and schema evolution;
- end-to-end hardware and embedded evaluation under realistic build and device constraints;
- licensing and provenance for translated cross-language training data;
- domain-expert review cost and long-term ownership of generated specialist software.

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Shojaee2025LlmSrScientific | [LLM-SR: Scientific Equation Discovery via Programming with Large Language Models](<https://openreview.net/forum?id=m2nmp8P5in>) | 2025 | ICLR / accepted-program | Domain Specific Low Resource Scientific And Data Software | Introduces or evaluates lLM-SR: Scientific Equation Discovery via Programming with Large Language Models; abstract-level contribution review remains pending. | formal-venue |

### Frontier Preprints

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Nardone2026LlmBasedSource | [LLM-based Source Code Compression via Thresholded Symbol Ranking](<https://arxiv.org/abs/2607.24192>) | 2026 | arXiv / frontier-preprint | Domain Specific Low Resource Scientific And Data Software | Study the problem of lossless compression of source code, motivated by the storage demands of large-scale software archives, such as Software Heritage (https://www.softwareheritage.org/). | frontier-preprint |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
