---
ai-generated: true
last-reviewed: 2026-07-30
---

# Code Generation, Completion, and Translation

Back: [Academic Status](Academic-Status.md)

Scope: task-first code synthesis, completion, constrained decoding, code translation/transpilation, and correctness-preserving transformation. Code-model training recipes, adaptation data, and learned representations belong in [Code-Model Training, Adaptation, Data, and Representation](Code-Model-Training-Adaptation-Data-And-Representation.md); repository issue resolution belongs in [Software Agents and Repository Engineering](Software-Agents-And-Repository-Engineering.md); performance-first transformation belongs in [Performance Optimization and Compilation](Performance-Optimization-And-Compilation.md).

## Status

The central movement is from unconstrained token generation to structured search with compiler, type, execution, or equivalence feedback. Translation is a useful stress test because plausible output is insufficient: the target must build and preserve source behavior across language and library differences.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Izadi2024CodeCompletion | [Language Models for Code Completion: A Practical Evaluation](https://dblp.org/rec/conf/icse/IzadiKDOPD24) | 2024 | ICSE / proceedings | Practical evaluation of completion quality and failure modes. | Evaluation |
| Pan2024CodeTranslationBugs | [Lost in Translation: A Study of Bugs Introduced by Large Language Models while Translating Code](https://dblp.org/rec/conf/icse/PanIKSWMSPSJ24) | 2024 | ICSE / proceedings | Shows that syntactically successful translations can introduce semantic bugs. | Evaluation |
| Holt2024L2MAC | [L2MAC: Large Language Model Automatic Computer for Extensive Code Generation](https://dblp.org/rec/conf/iclr/HoltLS24) | 2024 | ICLR / proceedings | Generates larger programs through structured model-computer interaction. | Published |
| Bhatia2024Transpilation | [Verified Code Transpilation with LLMs](https://dblp.org/rec/conf/nips/BhatiaQHSC24) | 2024 | NeurIPS / proceedings | Couples LLM translation with verification rather than trusting generated code. | Published |
| Wang2025PlanningCodeGen | [Planning in Natural Language Improves LLM Search for Code Generation](https://openreview.net/forum?id=B2iSfPNj49) | 2025 | ICLR Spotlight / official record | Searches over diverse natural-language plans before emitting code. | Published |
| Macedo2025INTERTRANS | [INTERTRANS: Leveraging Transitive Intermediate Translations to Enhance LLM-Based Code Translation](https://doi.org/10.1109/ICSE55347.2025.00236) | 2025 | ICSE / DOI | Uses intermediate languages to improve translation success. | Published |
| Mundler2025TypeConstrained | [Type-Constrained Code Generation with Language Models](https://doi.org/10.1145/3729274) | 2025 | PLDI / DOI | Enforces type constraints during decoding and reduces uncompilable output. | Published |
| Zhang2025WholeProjectTranslation | [Scalable, Validated Code Translation of Entire Projects using Large Language Models](https://doi.org/10.1145/3729315) | 2025 | PLDI / DOI | Modularizes whole-project Go-to-Rust translation and validates I/O equivalence. | Published |
| Lavon2025ExecutionGuided | [Execution Guided Line-by-Line Code Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/d8b69a226ec6bea8f187ca990abb2dae-Abstract-Conference.html) | 2025 | NeurIPS / proceedings | Refreshes execution feedback at line boundaries during generation. | Published |
| Princis2026TreeCoder | [TreeCoder: Systematic Exploration and Optimisation of Decoding and Constraints for LLM Code Generation](https://doi.org/10.1145/3808347) | 2026 | PLDI / DOI | Treats decoding, constraints, and hyperparameters as searchable components. | Published |
| Seo2026Paper2Code | [Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning](https://openreview.net/forum?id=3DcaUTjdKc) | 2026 | ICLR Poster / official record | Tests long-form implementation from technical specifications in papers. | Published |
| Chou2026AutoCodeBench | [AutoCodeBench: Large Language Models are Automatic Code Benchmark Generators](https://openreview.net/forum?id=fN0MED2Idq) | 2026 | ICLR Poster / official record | Automates the construction of difficult multilingual code-generation tasks and validates them through sandbox execution. | Published / Evaluation |

## What to Measure

- exact model, prompt/scaffold, decoding budget, and tool access;
- syntax, type, build, and dependency success separately;
- held-out behavioral tests and contamination controls;
- translation equivalence, unsupported-feature handling, and repair-loop termination;
- review effort and maintainability, not only pass@k.

## Boundary Notes

- Secure-code generation is indexed only in the [security dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md).
- OctoPack and WizardCoder are canonical on [Code-Model Training, Adaptation, Data, and Representation](Code-Model-Training-Adaptation-Data-And-Representation.md) because their primary contributions are code-specific data and instruction-tuning methods.
- QiMeng-Xpiler is canonical under [Performance Optimization and Compilation](Performance-Optimization-And-Compilation.md) because its primary claim is a neural-symbolic transcompiler for heterogeneous tensor systems.
- LiveCodeBench and AutoCodeBench are cross-indexed from [Benchmarks, Datasets, and Evaluation](Benchmarks-Datasets-And-Evaluation.md).

## Research Gaps

- whole-project translation with library, concurrency, and undefined-behavior semantics;
- constrained decoding that scales beyond syntax and local types;
- evaluation of future maintenance cost and human comprehension;
- non-English and low-resource programming languages;
- stable comparisons when proprietary models and scaffolds change.
