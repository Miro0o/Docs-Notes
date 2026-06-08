---
ai-generated: true
---

# LLM For Repair And Patch Validation

Back: [Academic Status](Academic-Status.md)

Scope: automated vulnerability repair, general program repair when it informs security patching, backporting, patch classification, test generation for fixes, and validation of generated patches.

Sources/time: 2024-present, checked on 2026-06-06. Formal entries draw from top security (IEEE S&P, USENIX Security, ACM CCS, NDSS), SE (ICSE, ESEC/FSE and FSE/PACMSE, ASE, ISSTA), PL (POPL, PLDI, OOPSLA, ICFP, primarily through PACMPL and relevant DBLP venue pages), and AI (NeurIPS, ICML, ICLR, AAAI) venues, plus selected journal, DBLP, DOI, or official accepted-paper/program pages when noted. arXiv entries come from targeted frontier sweeps over `cs.CR`, `cs.SE`, `cs.PL`, `cs.AI`, `cs.LG`, and `cs.CL`.

## Formal Published / Accepted Papers

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Pearce2024ZeroShotRepair | [Examining Zero-Shot Vulnerability Repair with Large Language Models](https://sp2024.ieee-security.org/program-papers.html) | 2024 | IEEE S&P | Vulnerability repair baseline | Establishes that plausible patches need independent validation. | Core |
| Hossain2024BugLocalizationRepair | [A Deep Dive into Large Language Models for Automated Bug Localization and Repair](https://dblp.org/rec/journals/pacmse/Hossain0Z0CLNT24) | 2024 | FSE/PACMSE / DBLP | Bug repair survey/eval | Studies LLMs for localization and repair in SE workflows. | Adjacent |
| Tang2024RepairTradeoff | [Code Repair with LLMs gives an Exploration-Exploitation Tradeoff](https://dblp.org/rec/conf/nips/TangHZZZSE24) | 2024 | NeurIPS / DBLP | Repair search | Frames LLM code repair as an exploration/exploitation problem. | Adjacent |
| Nong2025APPATCH | [APPATCH: Automated Adaptive Prompting Large Language Models for Real-World Software Vulnerability Patching](https://dblp.org/rec/conf/uss/NongY0HC25) | 2025 | USENIX Security / DBLP | Vulnerability patching | Uses adaptive prompting and vulnerability semantics for real-world patches. | Core |
| Kim2025SAN2PATCH | [Logs In, Patches Out: Automated Vulnerability Repair via Tree-of-Thought LLM Analysis](https://dblp.org/rec/conf/uss/Kim0KY25) | 2025 | USENIX Security / DBLP | Sanitizer-guided repair | Uses sanitizer logs and tree-of-thought repair. | Core |
| Li2026PORTGPT | [PORTGPT: Towards Automated Backporting Using Large Language Models](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | Security backporting | Moves from patch generation to branch-aware backporting and validation. | Core |
| PATCHAGENT2025 | [PATCHAGENT: A Practical Program Repair Agent Mimicking Human Expertise](https://dblp.org/rec/conf/uss/0003G00XM0025) | 2025 | USENIX Security / DBLP | Program repair agent | Agentic repair system modeled after expert workflows. | Core |
| Hu2025AVRSoK | [SoK: Automated Vulnerability Repair: Methods, Tools, and Assessments](https://dblp.org/rec/conf/uss/Hu0SGZXY025) | 2025 | USENIX Security / DBLP | Repair SoK | Systematizes automated vulnerability repair methods and assessment. | Survey |
| SoK2025EffectiveAVR | [SoK: Towards Effective Automated Vulnerability Repair](https://dblp.org/rec/conf/uss/0095SW0025) | 2025 | USENIX Security / DBLP | Repair SoK | Reviews requirements for effective vulnerability repair. | Survey |
| Sun2025DISPATCH | [DISPATCH: Unraveling Security Patches from Entangled Code Changes](https://dblp.org/rec/conf/uss/SunX00L025) | 2025 | USENIX Security / DBLP | Patch identification | Separates security patch logic from entangled commits. | Core |
| Xu2025RepairObjective | [Aligning the Objective of LLM-Based Program Repair](https://dblp.org/rec/conf/icse/XuFTH25) | 2025 | ICSE / DBLP | Repair objective | Studies objective alignment in LLM-based repair. | Core |
| Parasaram2025FactSelection | [The Fact Selection Problem in LLM-Based Program Repair](https://dblp.org/rec/conf/icse/ParasaramYYFQZB25) | 2025 | ICSE / DBLP | Repair context | Studies which facts should enter LLM repair prompts. | Core |
| Bouzenia2025RepairAgent | [RepairAgent: An Autonomous, LLM-Based Agent for Program Repair](https://dblp.org/rec/conf/icse/BouzeniaDP25) | 2025 | ICSE / DBLP | Repair agent | Autonomous repair agent for program fixes. | Core |
| Ke2025NIODebugger | [NIODebugger: A Novel Approach to Repair Non-Idempotent-Outcome Tests with LLM-Based Agent](https://dblp.org/rec/conf/icse/Ke25) | 2025 | ICSE / DBLP | Test repair | Repairs unstable/non-idempotent tests. | Adjacent |
| Rahman2025UTFix | [UTFix: Change Aware Unit Test Repairing using LLM](https://dblp.org/rec/journals/pacmpl/RahmanKCGWMDR25) | 2025 | PACMPL / DBLP | Test repair | Repairs unit tests in response to code changes. | Adjacent |
| Xie2025PReMM | [PReMM: LLM-Based Program Repair for Multi-method Bugs via Divide and Conquer](https://dblp.org/rec/journals/pacmpl/XieL0WL0L25) | 2025 | PACMPL / DBLP | Multi-method repair | Decomposes multi-method bugs for LLM repair. | Core |
| Wu2025Mystique | [Mystique: Automated Vulnerability Patch Porting with Semantic and Syntactic-Enhanced LLM](https://dblp.org/rec/journals/pacmse/WuWCCZHZP25) | 2025 | FSE/PACMSE / DBLP | Patch porting | Ports vulnerability patches using semantic/syntactic enhancement. | Core |
| Liu2025PatchScope | [PatchScope: LLM-Enhanced Fine-Grained Stable Patch Classification for Linux Kernel](https://dblp.org/rec/journals/pacmse/LiuSLHLSWSJ25) | 2025 | FSE/PACMSE / DBLP | Patch classification | Classifies Linux kernel stable patches. | Core |
| Ye2025AdverIntentAgent | [AdverIntent-Agent: Adversarial Reasoning for Repair Based on Inferred Program Intent](https://dblp.org/rec/journals/pacmse/YeYHWZG25) | 2025 | FSE/PACMSE / DBLP | Intent-based repair | Uses inferred program intent and adversarial reasoning for repair. | Core |
| Chi2025REACCEPT | [REACCEPT: Automated Co-evolution of Production and Test Code Based on Dynamic Validation and Large Language Models](https://dblp.org/rec/journals/pacmse/ChiWHYCSS25) | 2025 | FSE/PACMSE / DBLP | Dynamic validation | Co-evolves production/test code with dynamic validation. | Core |
| Li2026WhatTheyFix | [What Do They Fix? LLM-Aided Categorization of Security Patches for Critical Memory Bugs](https://dblp.org/rec/conf/ndss/LiPWZZWZHDQLJLK26) | 2026 | NDSS / DBLP | Patch categorization | Categorizes what memory-bug patches actually fix. | Frontier |
| Lutalo2026HTNRepair | [Automated Repair of Totally-Ordered Hierarchical Task Network Domains via Context-Free Grammars with Large Language Model Support](https://dblp.org/rec/conf/aaai/LutaloB26) | 2026 | AAAI / DBLP | Repair adjacent | LLM-assisted repair outside code; useful for structured repair analogies. | Adjacent |

## arXiv / Frontier Preprints

| Key | Paper | Year | Source | Area fit | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| 2604.03610 | [DebugHarness: Emulating Human Dynamic Debugging for Autonomous Program Repair](https://arxiv.org/abs/2604.03610) | 2026 | arXiv | Dynamic debugging | Emulates human debugging for severe software flaws. | Frontier |
| 2602.08263 | [Specification Vibing for Automated Program Repair](https://arxiv.org/abs/2602.08263) | 2026 | arXiv | Spec-based repair | Moves repair from code rewriting toward spec-guided repair. | Frontier |
| 2602.13574 | [Execution-State-Aware LLM Reasoning for Automated Proof-of-Vulnerability Generation](https://arxiv.org/abs/2602.13574) | 2026 | arXiv | Patch validation | PoV generation can support validation and false-positive reduction. | Frontier |

## Notes

- Validation is the hard problem: green tests are not enough for security patches.
- Prefer papers that replay evidence, generate regression tests, classify root cause, or support backporting under branch drift.
