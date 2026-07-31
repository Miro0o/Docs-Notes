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
