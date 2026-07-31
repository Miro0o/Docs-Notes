---
ai-generated: true
last-reviewed: 2026-07-30
---

# Code-Model Training, Adaptation, Data, and Representation

Back: [Academic Status](Academic-Status.md)

Scope: code-specific pretraining and instruction-tuning recipes, code corpora and synthetic-data pipelines, adaptation methods, and learned representations whose primary artifact is a code model or its training substrate. Task-first generation, translation, repair, and repository-agent techniques remain on their task shelves.

## Status

Code-model research is moving from opaque scale-up toward reproducible data recipes, execution-filtered self-alignment, multilingual adaptation, and representations designed for program semantics. The key evaluation question is no longer only whether a checkpoint improves pass@k, but which data, objectives, filtering, and representations produced the gain and whether it transfers across languages and software tasks.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Muennighoff2024OctoPack | [OctoPack: Instruction Tuning Code Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/hash/1ec299a5229034141e58aeded0d0b9de-Abstract-Conference.html) | 2024 | ICLR Spotlight / proceedings | Builds CommitPack from version-control commits across 350 languages and uses it to train and evaluate instruction-following code models. | Published |
| Luo2024WizardCoder | [WizardCoder: Empowering Code Large Language Models with Evol-Instruct](https://openreview.net/forum?id=UnUwSIgK5W) | 2024 | ICLR / official record | Adapts instruction evolution to construct progressively more complex code-instruction data. | Published |
| Wei2024Magicoder | [Magicoder: Empowering Code Generation with OSS-Instruct](https://proceedings.mlr.press/v235/wei24h.html) | 2024 | ICML / proceedings | Introduces OSS-Instruct, which derives synthetic instruction-response pairs from open-source code snippets. | Published |
| Zhang2024CodeSage | [Code Representation Learning at Scale](https://proceedings.iclr.cc/paper_files/paper/2024/hash/cfbba5249393100ada0bfb37557d2fd9-Abstract-Conference.html) | 2024 | ICLR / proceedings | Combines denoising and contrastive objectives to learn reusable code representations at scale. | Published |
| Wei2024SelfCodeAlign | [SelfCodeAlign: Self-Alignment for Code Generation](https://papers.nips.cc/paper_files/paper/2024/hash/72da102da91a8042a0b2aa968429a9f9-Abstract-Conference.html) | 2024 | NeurIPS / proceedings | Lets a base model generate tasks, solutions, and tests, then execution-filters the resulting self-alignment corpus. | Published |
| Huang2025OpenCoder | [OpenCoder: The Open Cookbook for Top-Tier Code Large Language Models](https://aclanthology.org/2025.acl-long.1591/) | 2025 | ACL / proceedings | Opens a reproducible code-model recipe spanning data, training pipeline, checkpoints, and ablations. | Published |
| Yang2025Qwen25xCoder | [Qwen2.5-xCoder: Multi-Agent Collaboration for Multilingual Code Instruction Tuning](https://aclanthology.org/2025.acl-long.642/) | 2025 | ACL / proceedings | Develops multilingual code-model instruction data through collaboration among language-specific agents. | Published |
| Yang2026KimiDev | [Kimi-Dev: Agentless Training as Skill Prior for SWE-agents](https://iclr.cc/virtual/2026/poster/10006967) | 2026 | ICLR Poster / official program | Trains repository-task skill priors through agentless workflows and transfers them into interactive software agents. | Official program |

## What to Measure

- exact base checkpoint, tokenizer, context window, training stages, and compute;
- corpus provenance, licensing, deduplication, temporal cutoffs, and benchmark overlap;
- synthetic-data generator, execution filter, rejection rate, and retained failure modes;
- ablations separating data, objective, representation, scale, and agent scaffold;
- transfer across languages, repositories, generation, understanding, and maintenance tasks;
- reproducibility from released data recipes rather than checkpoint scores alone.

## Boundary and Ownership

- This shelf owns code-specific model, data, adaptation, and learned-representation contributions even when they are evaluated on generation or agents.
- A paper whose primary contribution is a generation method, repository workflow, repair loop, or domain tool remains on that task shelf.
- Generic non-code model pretraining, alignment, and representation learning remain outside this dossier.
- Training or adaptation whose primary outcome is vulnerability discovery, secure-code generation, malware analysis, or security repair belongs in the [software-security dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md).
- Languages, runtimes, and training infrastructure built primarily for LLM applications belong in the [inverse-direction dossier](../../Software-For-LLM-Agent-Systems-Research-Dossier-2026/Software-For-LLM-Agent-Systems-Research-Dossier-2026.md) or outside all three, according to their primary artifact.

## Research Gaps

- transparent data provenance and license-compatible redistribution;
- contamination-resistant evaluations tied to training cutoffs;
- causal attribution of gains to data, objectives, or scale;
- representations that preserve behavior across languages and repository evolution;
- low-resource programming-language adaptation without erasing language-specific semantics;
- energy and compute reporting for code-specific training pipelines.
