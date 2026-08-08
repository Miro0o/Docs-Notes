---
ai-generated: true
last-reviewed: 2026-07-30
---

# Systems, OS, Cloud, and Infrastructure Software

Back: [Academic Status](Academic-Status.md)

Scope: LLM-assisted reliability, diagnosis, logs, configuration, cloud/IaC, systems-software analysis, and operational tooling. The LLM must help understand, verify, repair, or operate software; generic infrastructure for training or serving models is out of scope.

## Status

OS and systems venues supply a missing bridge between repository research and production operation. The strongest systems papers combine LLM semantic inference with static analysis, fault injection, runtime telemetry, proof assistants, or deployment monitoring. They do not treat generated prose as a diagnostic oracle.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Stoica2024RetryBugs | [If At First You Don't Succeed, Try, Try, Again...? Insights and LLM-informed Tooling for Detecting Retry Bugs in Software Systems](https://doi.org/10.1145/3694715.3695971) | 2024 | SOSP / DOI | Combines empirical study, LLM-informed tooling, analysis, tests, and fault injection for retry bugs. | Published |
| Xu2025OpenRCA | [OpenRCA: Can Large Language Models Locate the Root Cause of Software Failures?](https://dblp.org/rec/conf/iclr/XuZZHZLPHZ025) | 2025 | ICLR / proceedings | Evaluates root-cause localization in software failures. | Published / Evaluation |
| Lian2025ConfigValidators | [Large Language Models as Configuration Validators](https://doi.org/10.1109/ICSE55347.2025.00017) | 2025 | ICSE / DOI | Uses LLMs to validate real configuration semantics. | Published |
| Hu2026GigiProfiler | [Diagnosing Performance Issues in Application-Defined Resources](https://www.usenix.org/conference/osdi26/presentation/hu-yigong) | 2026 | OSDI / official proceedings | gigiprofiler combines LLM semantic inference, static validation, runtime tracking, and code-path attribution. | Published |
| Akewar2026SMARTTalk | [SMARTTalk: Teaching SMART Logs to Talk to LLMs](https://www.usenix.org/conference/osdi26/technical-sessions) | 2026 | OSDI / official proceedings program | Makes storage-device telemetry usable for LLM-assisted operational diagnosis. | Published |
| Asuka2026SWEInfraBench | [SWE-InfraBench: Evaluating Language Models on Cloud Infrastructure Code](https://arxiv.org/abs/2606.05249) | 2026 | arXiv | Evaluates infrastructure-as-code tasks with cloud-specific constraints. | Frontier / Evaluation |
| Tang2026DevOpsGym | [DevOps-Gym: Benchmarking AI Agents in Software DevOps Cycle](https://openreview.net/forum?id=bP48r4dt7Z) | 2026 | ICLR / OpenReview | Evaluates long-horizon agents across build/configuration, monitoring, issue resolution, and test generation in real repositories. | Published / Evaluation |

## OS-Venue Cross-Links

The following OS papers are core to the dossier but have different canonical shelves:

- [QiMeng-Xpiler](Performance-Optimization-And-Compilation.md), OSDI 2025: neural-symbolic tensor-program transcompilation.
- [ECO](Performance-Optimization-And-Compilation.md), OSDI 2026: production code-efficiency optimization.
- [Neuro-Symbolic Proof Generation](Program-Analysis-Specification-Verification-And-Reasoning.md), OSDI 2026: systems-software verification.

These cross-links make the OS-venue evidence explicit without duplicating full records.

## Evaluation Checklist

- real applications, configurations, logs, or failure cases;
- clear separation between candidate inference and analyzer/runtime validation;
- false-positive burden and operational overhead;
- confirmed diagnoses, accepted patches, or production outcomes;
- versioned environments and failure-injection procedures;
- rollback, monitoring, and human escalation policies.

## Exclusions

PowerInfer, LoongServe, NanoFlow, KV-cache schedulers, parallel-training systems, and similar work are not included merely because they appear at OSDI/SOSP. Their main contribution is LLM infrastructure, not LLMs for software or software operations.

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| 00022024KernelLanguageEntropy | [Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities.](<http://papers.nips.cc/paper_files/paper/2024/hash/10c456d2160517581a234dfde15a7505-Abstract-Conference.html>) | 2024 | NeurIPS / proceedings | Systems OS Cloud And Infrastructure Software | Introduces or evaluates kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities; abstract-level contribution review remains pending. | formal-venue |
| Patel2024CharacterizingPowerManagement | [Characterizing Power Management Opportunities for LLMs in the Cloud.](<https://doi.org/10.1145/3620666.3651329>) | 2024 | ASPLOS / proceedings | Systems OS Cloud And Infrastructure Software | Introduces or evaluates characterizing Power Management Opportunities for LLMs in the Cloud; abstract-level contribution review remains pending. | formal-venue |
| Shan2024FaceItYourselves | [Face It Yourselves: An LLM-Based Two-Stage Strategy to Localize Configuration Errors via Logs.](<https://doi.org/10.1145/3650212.3652106>) | 2024 | ISSTA / proceedings | Systems OS Cloud And Infrastructure Software | Introduces or evaluates face It Yourselves: An LLM-Based Two-Stage Strategy to Localize Configuration Errors via Logs; abstract-level contribution review remains pending. | formal-venue |
| Cao2025ObjvariantensembleAdvancingPoint | [ObjVariantEnsemble: Advancing Point Cloud LLM Evaluation in Challenging Scenes with Subtly Distinguished Objects.](<https://doi.org/10.1609/aaai.v39i2.32190>) | 2025 | AAAI / proceedings | Systems OS Cloud And Infrastructure Software | Benchmarks or evaluates objVariantEnsemble: Advancing Point Cloud LLM Evaluation in Challenging Scenes with Subtly Distinguished Objects; abstract-level contribution review remains pending. | formal-venue |
| Lian2025LargeLanguageModels | [Large Language Models as Configuration Validators.](<https://doi.org/10.1109/ICSE55347.2025.00017>) | 2025 | ICSE / proceedings | Systems OS Cloud And Infrastructure Software | Introduces or evaluates large Language Models as Configuration Validators; abstract-level contribution review remains pending. | formal-venue |
| Liu2025PatchscopeLlmEnhanced | [PatchScope: LLM-Enhanced Fine-Grained Stable Patch Classification for Linux Kernel.](<https://doi.org/10.1145/3728944>) | 2025 | ISSTA / proceedings | Systems OS Cloud And Infrastructure Software | Introduces or evaluates patchScope: LLM-Enhanced Fine-Grained Stable Patch Classification for Linux Kernel; abstract-level contribution review remains pending. | formal-venue |
| Ouyang2025KernelbenchCanLlms | [KernelBench: Can LLMs Write Efficient GPU Kernels?](<https://proceedings.mlr.press/v267/ouyang25a.html>) | 2025 | ICML / proceedings | Systems OS Cloud And Infrastructure Software | Introduces or evaluates kernelBench: Can LLMs Write Efficient GPU Kernels?; abstract-level contribution review remains pending. | formal-venue |
| Shao2025AreLlmsCorrectly | [Are LLMs Correctly Integrated into Software Systems?](<https://doi.org/10.1109/ICSE55347.2025.00204>) | 2025 | ICSE / proceedings | Systems OS Cloud And Infrastructure Software | Introduces or evaluates are LLMs Correctly Integrated into Software Systems?; abstract-level contribution review remains pending. | formal-venue |
| Stojkovic2025TapasThermalPower | [TAPAS: Thermal- and Power-Aware Scheduling for LLM Inference in Cloud Platforms.](<https://doi.org/10.1145/3676641.3716025>) | 2025 | ASPLOS / proceedings | Systems OS Cloud And Infrastructure Software | Introduces or evaluates tAPAS: Thermal- and Power-Aware Scheduling for LLM Inference in Cloud Platforms; abstract-level contribution review remains pending. | formal-venue |
| Yang2025KernelgptEnhancedKernel | [KernelGPT: Enhanced Kernel Fuzzing via Large Language Models.](<https://doi.org/10.1145/3676641.3716022>) | 2025 | ASPLOS / proceedings | Systems OS Cloud And Infrastructure Software | Introduces or evaluates kernelGPT: Enhanced Kernel Fuzzing via Large Language Models; abstract-level contribution review remains pending. | formal-venue |
| Chen2026LlmthiefEvaluatingConfiguration | [LLMThief: Evaluating Configuration Leaking Risks in Commercial LLM App Stores.](<https://doi.org/10.1109/SP63933.2026.00195>) | 2026 | IEEE S&P / proceedings | Systems OS Cloud And Infrastructure Software | Benchmarks or evaluates lLMThief: Evaluating Configuration Leaking Risks in Commercial LLM App Stores; abstract-level contribution review remains pending. | formal-venue |
| Drosos2026UnfulfilledPromisesLlm | [Unfulfilled Promises: LLM-Based Detection of OS Compatibility Issues in Infrastructure as Code](<https://conf.researchr.org/track/fse-2026/fse-2026-research-papers#event-c24b4edd-3469-473d-9873-c6935b4d32e6>) | 2026 | FSE/PACMSE / accepted-program | Systems OS Cloud And Infrastructure Software | Introduces or evaluates unfulfilled Promises: LLM-Based Detection of OS Compatibility Issues in Infrastructure as Code; abstract-level contribution review remains pending. | formal-venue |
| Lai2026RadarllmEmpoweringLarge | [RadarLLM: Empowering Large Language Models to Understand Human Motion from Millimeter-wave Point Cloud Sequence.](<https://doi.org/10.1609/aaai.v40i7.37500>) | 2026 | AAAI / proceedings | Systems OS Cloud And Infrastructure Software | Introduces or evaluates radarLLM: Empowering Large Language Models to Understand Human Motion from Millimeter-wave Point Cloud Sequence; abstract-level contribution review remains pending. | formal-venue |
| Wang2026UntanglingGpuPower | [Untangling GPU Power Consumption: Job-Level Inference in Cloud Shared Settings Pierre Jacquet (École de technologie supérieure), Maxime Agusti (Univ Lyon1, Inria, OVHcloud), Eddy Caron (Univ Lyon1, Inria, ENS de Lyon, CNRS), Camille Coti (École de technologie supérieure), Marcos Dias De Assunção (École de technologie supérieure), Laurent Lefèvre (Univ Lyon1, Inria, ENS de Lyon, CNRS), Anne-Cécile Orgerie (CNRS, IRISA, Rennes - France) TZ-LLM: Protecting On-Device Large Language Models with Arm TrustZone](<https://dl.acm.org/doi/10.1145/3767295.3769333>) | 2026 | EuroSys / accepted-program | Systems OS Cloud And Infrastructure Software | Introduces or evaluates untangling GPU Power Consumption: Job-Level Inference in Cloud Shared Settings Pierre Jacquet (École de technologie supérieure), Maxime Agusti (Univ Lyon1, Inria, OVHcloud), Edd…; abstract-level contribution review remains pending. | formal-venue |
| Yi2026PatAcceleratingLlm | [PAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel.](<https://doi.org/10.1145/3779212.3790200>) | 2026 | ASPLOS / proceedings | Systems OS Cloud And Infrastructure Software | Introduces or evaluates pAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel; abstract-level contribution review remains pending. | formal-venue |
| Zhang2026SwiftspecDisaggregatedSpeculative | [SwiftSpec: Disaggregated Speculative Decoding and Fused Kernels for Low-Latency LLM Inference.](<https://doi.org/10.1145/3779212.3790246>) | 2026 | ASPLOS / proceedings | Systems OS Cloud And Infrastructure Software | Introduces or evaluates swiftSpec: Disaggregated Speculative Decoding and Fused Kernels for Low-Latency LLM Inference; abstract-level contribution review remains pending. | formal-venue |
| normalization2026OutrunningLlmCutoffs | [Outrunning LLM Cutoffs: A Live Kernel Crash Resolution Benchmark for All](<https://icml.cc/virtual/2026/poster/63308>) | 2026 | ICML / accepted-program | Systems OS Cloud And Infrastructure Software | Benchmarks or evaluates outrunning LLM Cutoffs: A Live Kernel Crash Resolution Benchmark for All; abstract-level contribution review remains pending. | formal-venue |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
