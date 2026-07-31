---
ai-generated: true
last-reviewed: 2026-07-30
---

# Testing, Debugging, and General Repair

Back: [Academic Status](Academic-Status.md)

Scope: test and oracle generation, compiler/library fuzzing, bug replay, fault localization, dynamic debugging, test repair, and general automated program repair. Security-oriented fuzzing and vulnerability patching are intentionally excluded.

## Status

Testing provides the most useful grounding signal for generated software, but a passing generated test can be weak or circular. Strong work measures coverage and mutation strength, validates oracles independently, and distinguishes plausible patches from correct repairs. Fuzzing is a subtopic of general testing here; it is not a separate top-level category.

## Published and Accepted Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Xia2024Fuzz4All | [Fuzz4All: Universal Fuzzing with Large Language Models](https://doi.org/10.1145/3597503.3639121) | 2024 | ICSE / DOI | Generates structured inputs across compilers, solvers, runtimes, and libraries. | Published |
| Deng2024FuzzGPT | [Large Language Models are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries](https://doi.org/10.1145/3597503.3623343) | 2024 | ICSE / DOI | Transfers historical bug patterns into unusual DL-library test programs. | Published |
| Feng2024AndroidBugReplay | [Prompting Is All You Need: Automated Android Bug Replay with Large Language Models](https://dblp.org/rec/conf/icse/FengC24) | 2024 | ICSE / proceedings | Reconstructs UI action sequences to replay Android bugs. | Published |
| Yang2024WhiteFox | [WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models](https://dblp.org/rec/journals/pacmpl/YangDLY0J024) | 2024 | OOPSLA/PACMPL / proceedings | Uses compiler internals and LLM generation for targeted compiler testing. | Published |
| Zhang2024FuzzDrivers | [How Effective Are They? Exploring Large Language Model Based Fuzz Driver Generation](https://doi.org/10.1145/3650212.3680355) | 2024 | ISSTA / DOI | Evaluates where generated fuzz drivers compile, exercise APIs, and fail. | Published / Evaluation |
| Jiang2024LeDex | [LeDex: Training LLMs to Better Self-Debug and Explain Code](https://dblp.org/rec/conf/nips/Jiang00ZHRK0D24) | 2024 | NeurIPS / proceedings | Trains models jointly for debugging and explanation. | Published |
| Mundler2024SWTBench | [SWT-Bench: Testing and Validating Real-World Bug-Fixes with Code Agents](https://dblp.org/rec/conf/nips/MundlerMHV24) | 2024 | NeurIPS / proceedings | Evaluates real-world agent bug fixes with stronger validation. | Published / Evaluation |
| Tang2024RepairTradeoff | [Code Repair with LLMs Gives an Exploration-Exploitation Tradeoff](https://dblp.org/rec/conf/nips/TangHZZZSE24) | 2024 | NeurIPS / proceedings | Frames sampling and selection in code repair as an exploration/exploitation problem. | Published |
| Nan2025TestIntention | [Test Intention Guided LLM-Based Unit Test Generation](https://doi.org/10.1109/ICSE55347.2025.00243) | 2025 | ICSE / DOI | Conditions generation on explicit test intent. | Published |
| Hossain2025TOGLL | [TOGLL: Correct and Strong Test Oracle Generation with Large Language Models](https://doi.org/10.1109/ICSE55347.2025.00098) | 2025 | ICSE / DOI | Targets both oracle correctness and fault-revealing strength. | Published |
| Zhang2025ExLong | [exLong: Generating Exceptional Behavior Tests with Large Language Models](https://doi.org/10.1109/ICSE55347.2025.00176) | 2025 | ICSE / DOI | Generates tests for exceptional behavior. | Published |
| Kim2025RESTTesting | [Multi-Agent REST API Testing with Semantic Graphs and LLM Inputs](https://doi.org/10.1109/ICSE55347.2025.00179) | 2025 | ICSE / DOI | Coordinates semantic graphs and multiple agents for REST API testing. | Published |
| Li2025InputPartitioning | [LLM Based Input Space Partitioning Testing for Library APIs](https://doi.org/10.1109/ICSE55347.2025.00153) | 2025 | ICSE / DOI | Partitions API input spaces before test generation. | Published |
| Yadavally2025SafeMinimization | [Large Language Models for Safe Minimization](https://doi.org/10.1109/ICSE55347.2025.00203) | 2025 | ICSE / DOI | Uses LLM reasoning to reduce failure-inducing inputs while preserving behavior. | Published |
| Gao2025Clozemaster | [Clozemaster: Fuzzing Rust Compiler by Harnessing LLMs for Infilling Masked Real Programs](https://doi.org/10.1109/ICSE55347.2025.00175) | 2025 | ICSE / DOI | Infills masked real Rust programs to test the compiler. | Published |
| Bouzenia2025RepairAgent | [RepairAgent: An Autonomous, LLM-Based Agent for Program Repair](https://doi.org/10.1109/ICSE55347.2025.00157) | 2025 | ICSE / DOI | Iteratively explores, edits, builds, and tests candidate repairs. | Published |
| Deligiannis2025RustAssistant | [RustAssistant: Using LLMs to Fix Compilation Errors in Rust Code](https://doi.org/10.1109/ICSE55347.2025.00022) | 2025 | ICSE / DOI | Repairs Rust compiler errors with compiler feedback. | Published |
| Xu2025RepairObjective | [Aligning the Objective of LLM-Based Program Repair](https://doi.org/10.1109/ICSE55347.2025.00169) | 2025 | ICSE / DOI | Examines mismatch between optimization objectives and repair correctness. | Published / Evaluation |
| Parasaram2025FactSelection | [The Fact Selection Problem in LLM-Based Program Repair](https://doi.org/10.1109/ICSE55347.2025.00162) | 2025 | ICSE / DOI | Studies which repository facts should enter a repair context. | Published / Evaluation |
| Ke2025NIODebugger | [NIODebugger: A Novel Approach to Repair Non-Idempotent-Outcome Tests with LLM-Based Agent](https://doi.org/10.1109/ICSE55347.2025.00226) | 2025 | ICSE / DOI | Repairs tests whose outcomes are non-idempotent. | Published |
| Rahman2025UTFix | [UTFix: Change Aware Unit Test Repairing using LLM](https://dblp.org/rec/journals/pacmpl/RahmanKCGWMDR25) | 2025 | OOPSLA/PACMPL / proceedings | Repairs unit tests in response to production-code changes. | Published |
| Xie2025PReMM | [PReMM: LLM-Based Program Repair for Multi-method Bugs via Divide and Conquer](https://dblp.org/rec/journals/pacmpl/XieL0WL0L25) | 2025 | OOPSLA/PACMPL / proceedings | Decomposes multi-method bugs for repair. | Published |
| Chi2025REACCEPT | [REACCEPT: Automated Co-evolution of Production and Test Code Based on Dynamic Validation and Large Language Models](https://dblp.org/rec/journals/pacmse/ChiWHYCSS25) | 2025 | FSE/PACMSE / proceedings | Co-evolves production and test code while dynamic validation checks the pair. | Published |
| ICSE2026BugFixAgents | [LLM-based Agents for Automated Bug Fixing: How Far Are We?](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Evaluates the limits of agentic bug fixing. | Accepted / Evaluation |
| ICSE2026InputReductionRepair | [Input Reduction Enhanced LLM-based Program Repair](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Uses reduced failure-inducing inputs to focus repair. | Accepted |
| ICSE2026CrossLanguageRepair | [Unlocking LLM Repair Capabilities Through Cross-Language Translation and Multi-Agent Refinement](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Combines cross-language representations with multi-agent refinement. | Accepted |
| ICSE2026RepairIngredients | [Repair Ingredients Are All You Need](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Studies the repair value of retrieving appropriate change ingredients. | Accepted |
| FSE2026SQLMetamorphic | [Validating LLM-Generated SQL Queries Through Metamorphic Prompting](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Uses metamorphic relations to validate generated SQL. | Official program |
| FSE2026PersonifiedTesting | [Towards Automated Crowdsourced Testing via Personified-LLM](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Uses personified agents to generate diverse crowdsourced-testing behavior. | Official program |
| FSE2026Clotho | [Clotho: Measuring Task-Specific Pre-Generation Test Adequacy for LLM Inputs](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Estimates whether available tests are adequate before generation. | Official program |
| ISSTA2026NullRepair | [NullRepair: LLM-Based Repair of Static Nullability Errors](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers) | 2026 | ISSTA Research Papers / accepted, conference upcoming | Repairs errors reported by static nullability analysis. | Accepted |
| ISSTA2026CausalRepair | [CausalRepair](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers) | 2026 | ISSTA Research Papers / accepted, conference upcoming | Uses causal information for repair; DOI pending. | Accepted |
| ISSTA2026LLMutantKiller | [LLMutantKiller](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers) | 2026 | ISSTA Research Papers / accepted, conference upcoming | Targets mutation adequacy with LLM assistance. | Accepted |
| ISSTA2026IssueExec | [IssueExec](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers) | 2026 | ISSTA Research Papers / accepted, conference upcoming | Makes issue reports executable for testing and debugging. | Accepted |

## Frontier Preprints

| Key | Paper | Year | Contribution | Label |
| --- | --- | ---: | --- | --- |
| 2603.08616 | [Coverage-Guided Multi-Agent Harness Generation for Java Library Fuzzing](https://arxiv.org/abs/2603.08616) | 2026 | Uses coverage feedback to coordinate harness-generation agents. | Frontier |
| 2602.11209 | [SAFuzz: Semantic-Guided Adaptive Fuzzing for LLM-Generated Code](https://arxiv.org/abs/2602.11209) | 2026 | Tests generated code with semantic-guided adaptive fuzzing. | Frontier |
| 2604.01442 | [Fuzzing with Agents? Generators Are All You Need](https://arxiv.org/abs/2604.01442) | 2026 | Compares complex agentic fuzzing with simpler generator-based alternatives. | Frontier / Evaluation |

## Evidence Checklist

- generated test validity is not enough; measure coverage, mutation score, and revealed faults;
- keep the test/oracle generator independent from the code generator when possible;
- report flaky tests, nondeterminism, and environment failures;
- evaluate repair overfitting with independent or augmented tests;
- preserve failing inputs, compiler diagnostics, traces, patches, and replay steps;
- distinguish compiler/library correctness fuzzing from security-directed fuzzing.

## Boundary Notes

Security fuzzing, vulnerability repair, proof-of-vulnerability generation, and exploit validation live in the [security dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md). `Ma2025OpDiffer` is canonical there because its EVM evaluation reports security impact and vulnerability identifiers; `FSE2026TLR` is canonical there because it repairs vulnerability-relevant C memory errors and reports critical zero-day findings.
