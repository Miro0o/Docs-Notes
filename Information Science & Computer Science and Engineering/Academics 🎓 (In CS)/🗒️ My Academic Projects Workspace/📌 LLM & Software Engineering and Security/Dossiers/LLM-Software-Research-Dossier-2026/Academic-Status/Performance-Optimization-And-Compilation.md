---
ai-generated: true
last-reviewed: 2026-07-30
---

# Performance Optimization and Compilation

Back: [Academic Status](Academic-Status.md)

Scope: LLM-assisted code efficiency, compiler-guided transformation, tensor/program lowering, autotuning, profiling-led optimization, and benchmarks that measure resource behavior rather than only functional correctness.

## Status

The credible pattern is an optimization loop with three independent components: opportunity localization, candidate synthesis/search, and semantic/performance validation. Production evidence now exists, but evaluation must count rejected changes, review load, rollout failures, and the energy or compute cost of the optimization process.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Du2024Mercury | [Mercury: A Code Efficiency Benchmark for Code Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1df1df43b58845650b8dada00fca9772-Abstract-Datasets_and_Benchmarks_Track.html) | 2024 | NeurIPS Datasets & Benchmarks / proceedings | Measures generated-code efficiency rather than correctness alone. | Published / Evaluation |
| Gao2025CodeOptimization | [Search-Based LLMs for Code Optimization](https://doi.org/10.1109/ICSE55347.2025.00021) | 2025 | ICSE / DOI | Searches candidate programs for measured efficiency gains. | Published |
| Qiu2025CodeEfficiency | [How Efficient Is LLM-Generated Code? A Rigorous and High-Standard Benchmark](https://dblp.org/rec/conf/iclr/QiuZELT25) | 2025 | ICLR / proceedings | Evaluates runtime and resource efficiency with stricter standards. | Published / Evaluation |
| Wang2025ReductiveAnalysis | [Reductive Analysis with Compiler-Guided Large Language Models for Input-Centric Code Optimizations](https://doi.org/10.1145/3729282) | 2025 | PLDI / DOI | Uses compiler guidance and reductive analysis to infer important input features. | Published |
| Li2025GuidedTensorLifting | [Guided Tensor Lifting](https://doi.org/10.1145/3729330) | 2025 | PLDI / DOI | Uses guidance to lift low-level tensor computations into optimizable representations. | Published |
| Dong2025QiMengXpiler | [QiMeng-Xpiler: Transcompiling Tensor Programs for Deep Learning Systems with a Neural-Symbolic Approach](https://www.usenix.org/conference/osdi25/presentation/dong) | 2025 | OSDI / official proceedings | Combines LLM transformation passes, symbolic repair, and autotuning across heterogeneous tensor platforms. | Published |
| Coignion2025Greener | [When Faster Isn't Greener: The Hidden Costs of LLM-Based Code Optimization](https://conf.researchr.org/details/ase-2025/ase-2025-papers/65/When-Faster-Isn-t-Greener-The-Hidden-Costs-of-LLM-Based-Code-Optimization) | 2025 | ASE / official program | Evaluates whether speed improvements justify optimization energy costs. | Published / Evaluation |
| Ye2026AnchorOptimization | [A Problem-Oriented Perspective and Anchor Verification for Code Optimization](https://openreview.net/forum?id=HGaUV3jjvo) | 2026 | ICLR Poster / official record | Builds problem-oriented optimization pairs and uses anchor verification to control correctness loss. | Published |
| ICSE2026LLM4JMH | [LLM4JMH: LLM-Assisted Java Performance Microbenchmark Generation](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Generates performance microbenchmarks for Java; DOI metadata pending. | Accepted |
| Lin2026ECO | [ECO: An AI-Driven Code Efficiency Optimizer for Warehouse Scale Computers](https://www.usenix.org/conference/osdi26/presentation/lin-hannah) | 2026 | OSDI / official proceedings | Uses fleet profiling, candidate localization, staged validation, and deployment monitoring; reports 6,400+ landed production commits. | Published |
| ISSTA2026OptiMine | [OptiMine](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers) | 2026 | ISSTA Research Papers / accepted, conference upcoming | Accepted optimization-oriented record; normalize title/authors/DOI after proceedings. | Accepted |

## Systems-Venue Cross-Links

- [gigiprofiler](Systems-OS-Cloud-And-Infrastructure-Software.md) is canonical under systems diagnosis because its primary claim is explaining application-defined resource bottlenecks.
- [Neuro-Symbolic Proof Generation](Program-Analysis-Specification-Verification-And-Reasoning.md) is canonical under verification.

## Evaluation Checklist

| Dimension | Required evidence |
| --- | --- |
| Correctness | equivalence checks, comprehensive tests, or a formal argument |
| Performance | repeated measurements, hardware/runtime specification, variance, and baseline |
| Search cost | model calls, compiler/profiler executions, wall time, and energy where possible |
| Deployment | rejected candidates, review effort, rollbacks, and post-deployment monitoring |
| Generality | multiple languages, workloads, architectures, and optimization classes |

## Boundary Notes

LLM inference-serving engines, KV-cache schedulers, parallel-training systems, and generic model-runtime optimizers are excluded unless their primary contribution is helping analyze or improve software.

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Kim2024LlmCompilerParallel | [An LLM Compiler for Parallel Function Calling](<https://proceedings.mlr.press/v235/kim24y.html>) | 2024 | ICML / proceedings | Performance Optimization And Compilation | Introduces or evaluates an LLM Compiler for Parallel Function Calling; abstract-level contribution review remains pending. | formal-venue |
| Coignion2025WhenFasterIsn | [When Faster Isn't Greener: The Hidden Costs of LLM-Based Code Optimization](<https://conf.researchr.org/track/ase-2025/ase-2025-papers#event-e9046a67-af99-4302-af19-35941ab5fbd6>) | 2025 | ASE / accepted-program | Performance Optimization And Compilation | Introduces or evaluates when Faster Isn't Greener: The Hidden Costs of LLM-Based Code Optimization; abstract-level contribution review remains pending. | formal-venue |
| Erhabor2025MeasuringRuntimePerformance | [Measuring the Runtime Performance of C++ Code Written by Humans Using Github Copilot.](<https://doi.org/10.1109/ICSE55347.2025.00059>) | 2025 | ICSE / proceedings | Performance Optimization And Compilation | Introduces or evaluates measuring the Runtime Performance of C++ Code Written by Humans Using Github Copilot; abstract-level contribution review remains pending. | formal-venue |
| Gao2025ClozemasterFuzzingRust | [Clozemaster: Fuzzing Rust Compiler by Harnessing Llms for Infilling Masked Real Programs.](<https://doi.org/10.1109/ICSE55347.2025.00175>) | 2025 | ICSE / proceedings | Performance Optimization And Compilation | Introduces or evaluates clozemaster: Fuzzing Rust Compiler by Harnessing Llms for Infilling Masked Real Programs; abstract-level contribution review remains pending. | formal-venue |
| Wang2025FixingBrokenGraphs | [Fixing Broken Graphs: LLM-Powered Automatic Code Optimization for DNN Programs](<https://conf.researchr.org/track/ase-2025/ase-2025-papers#event-3142eb3c-af48-44ae-9168-64a343d6c75d>) | 2025 | ASE / accepted-program | Performance Optimization And Compilation | Introduces or evaluates fixing Broken Graphs: LLM-Powered Automatic Code Optimization for DNN Programs; abstract-level contribution review remains pending. | formal-venue |
| Angermeir2026ReflectionsReproducibilityCommercial | [Reflections on the Reproducibility of Commercial LLM Performance in Empirical Software Engineering Studies](<https://conf.researchr.org/track/icse-2026/icse-2026-research-track#event-e27ce9f6-bac5-4ba7-ac06-5cea632737cf>) | 2026 | ICSE / accepted-program | Performance Optimization And Compilation | Benchmarks or evaluates reflections on the Reproducibility of Commercial LLM Performance in Empirical Software Engineering Studies; abstract-level contribution review remains pending. | formal-venue |
| Lu2026RiceHarnessingLlms | [RICE: Harnessing LLMs and Historical Issues to Discover Internal Rust Compiler Errors](<https://conf.researchr.org/track/issta-2026/issta-2026-research-papers#event-bd60da02-efdf-49f9-bac3-3145aed7e87c>) | 2026 | ISSTA / accepted-program | Performance Optimization And Compilation | Introduces or evaluates rICE: Harnessing LLMs and Historical Issues to Discover Internal Rust Compiler Errors; abstract-level contribution review remains pending. | formal-venue |
| Ran2026KernelbandSteeringLlm | [KernelBand: Steering LLM-based Kernel Optimization via Hardware-Aware Multi-Armed Bandits](<https://icml.cc/virtual/2026/poster/62803>) | 2026 | ICML / accepted-program | Performance Optimization And Compilation | Introduces or evaluates kernelBand: Steering LLM-based Kernel Optimization via Hardware-Aware Multi-Armed Bandits; abstract-level contribution review remains pending. | formal-venue |
| Shi2026CompilingCodeLlms | [Compiling Code LLMs into Lightweight Executables](<https://conf.researchr.org/track/fse-2026/fse-2026-research-papers#event-c32fbb26-37fd-465e-a13e-38a443d8f93c>) | 2026 | FSE/PACMSE / accepted-program | Performance Optimization And Compilation | Introduces or evaluates compiling Code LLMs into Lightweight Executables; abstract-level contribution review remains pending. | formal-venue |
| zhang2026StillManualAutomated | [Still Manual? Automated Linter Configuration via DSL-Based LLM Compilation of Coding Standards](<https://conf.researchr.org/track/fse-2026/fse-2026-research-papers#event-e6d96a82-8c7b-4c36-8dd5-d330f5261f04>) | 2026 | FSE/PACMSE / accepted-program | Performance Optimization And Compilation | Introduces or evaluates still Manual? Automated Linter Configuration via DSL-Based LLM Compilation of Coding Standards; abstract-level contribution review remains pending. | formal-venue |

### Frontier Preprints

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Yu2026EnablingPerformantFlexible | [Enabling Performant and Flexible Model-Internal Observability for LLM Inference](<https://arxiv.org/abs/2605.11093>) | 2026 | arXiv / frontier-preprint | Performance Optimization And Compilation | Present DMI-Lib, a high-speed deep model inspector that treats internal observability as a first-class systems primitive, decoupling it from the inference hot path via…. | frontier-preprint |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
