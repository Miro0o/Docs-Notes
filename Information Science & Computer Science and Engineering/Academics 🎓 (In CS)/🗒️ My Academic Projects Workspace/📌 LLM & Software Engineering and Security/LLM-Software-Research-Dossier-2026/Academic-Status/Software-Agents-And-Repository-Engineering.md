---
ai-generated: true
last-reviewed: 2026-07-30
---

# Software Agents and Repository Engineering

Back: [Academic Status](Academic-Status.md)

Scope: repository navigation, issue resolution, planning, agent-computer interfaces, tool use, builds, long-horizon state, multi-agent coordination, and repository-level evaluation.

## Status

Repository tasks turn code generation into a systems problem. An agent must discover relevant files, interpret an issue, preserve repository conventions, operate tools, build and test, recover from failure, and stop with an auditable patch. Results therefore depend heavily on environment images, interfaces, retrieval, trajectory budgets, and test quality.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Jimenez2024SWEBench | [SWE-bench: Can Language Models Resolve Real-world GitHub Issues?](https://dblp.org/rec/conf/iclr/JimenezYWYPPN24) | 2024 | ICLR Oral / proceedings | Establishes real GitHub issue resolution as a repository-scale evaluation task. | Published / Evaluation |
| Yang2024SWEAgent | [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html) | 2024 | NeurIPS / proceedings | Shows that agent-computer interface design materially changes repository-task performance. | Published |
| Bairi2024CodePlan | [CodePlan: Repository-Level Coding using LLMs and Planning](https://dblp.org/rec/journals/pacmse/BairiSKCIPRAS24) | 2024 | FSE/PACMSE / proceedings | Decomposes repository changes into an explicit plan. | Published |
| Antoniades2025SWESearch | [SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement](https://dblp.org/rec/conf/iclr/AntoniadesOZXGW25) | 2025 | ICLR Poster / proceedings | Applies tree search and iterative refinement to repository agents. | Published |
| Xia2025SEAgents | [Demystifying LLM-Based Software Engineering Agents](https://dblp.org/rec/journals/pacmse/XiaDDZ25) | 2025 | FSE/PACMSE / proceedings | Characterizes agent behavior, design choices, and limits. | Published / Evaluation |
| Yu2025CXXCrafter | [CXXCrafter: An LLM-Based Agent for Automated C/C++ Open Source Software Building](https://dblp.org/rec/journals/pacmse/YuZWNZY25) | 2025 | FSE/PACMSE / proceedings | Automates dependency and build repair for C/C++ projects. | Published |
| Ma2025SWEGPT | [SWE-GPT: A Process-Centric Language Model for Automated Software Improvement](https://dblp.org/rec/journals/pacmse/MaCCZCLLLHL25) | 2025 | FSE/PACMSE / proceedings | Models software-improvement processes rather than isolated edits. | Published |
| Badertdinov2025SWERebench | [SWE-rebench: An Automated Pipeline for Task Collection and Decontaminated Evaluation of Software Engineering Agents](https://proceedings.neurips.cc/paper_files/paper/2025/hash/21bec6ace947b1b58967b945c8ac0f10-Abstract-Datasets_and_Benchmarks_Track.html) | 2025 | NeurIPS Datasets & Benchmarks / proceedings | Continuously collects fresh interactive tasks and supports decontaminated evaluation. | Published / Evaluation |
| Zan2025MultiSWEBench | [Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5afa9cb1e917b898ad418216dc726fbd-Abstract-Datasets_and_Benchmarks_Track.html) | 2025 | NeurIPS Datasets & Benchmarks / proceedings | Broadens repository-agent evaluation across languages and projects. | Published / Evaluation |
| Zhou2026FeatureBench | [FeatureBench: Benchmarking Agentic Coding for Complex Feature Development](https://openreview.net/forum?id=41xrZ3uGuI) | 2026 | ICLR Poster / official record | Evaluates feature implementation spanning commits and pull requests with executable, test-derived environments. | Published / Evaluation |
| ICSE2026RepoScope | [RepoScope](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Repository-scope context and reasoning for software agents; DOI metadata pending in this snapshot. | Accepted |

Testing-oriented agent evaluation, including SWT-Bench, is canonical in [Testing, Debugging, and General Repair](Testing-Debugging-And-General-Repair.md).

EvoMAC and DEI are evaluated on software-development tasks, but their primary contributions organize or evolve the agent system itself. Their canonical records therefore live under the inverse dossier’s [Architecture, Evolution, and Operations](../../Software-For-LLM-Agent-Systems-Research-Dossier-2026/Academic-Status/Architecture-Evolution-And-Operations.md) shelf.

RefAgent is canonical on [Quality, Refactoring, Technical Debt, and Code Smells](Quality-Refactoring-Technical-Debt-And-Code-Smells.md) because its primary outcome is behavior-preserving software refactoring rather than general issue resolution.

## Evaluation Requirements

| Dimension | Record explicitly |
| --- | --- |
| Task | issue source, repository revision, language, and task freshness |
| Environment | container/build image, dependency availability, network policy, and flaky-test handling |
| Agent | model version, interface, retrieval, tools, trajectory budget, retries, and human intervention |
| Oracle | test patch provenance, hidden tests, build result, regression policy, and patch applicability |
| Cost | tokens, wall time, compute, tool calls, and failed trajectories |
| Auditability | complete trajectory, file changes, commands, test output, and stop reason |

## Research Gaps

- fresh, continuously refreshed tasks with reproducible dependency environments;
- reliable context selection across very large, polyglot repositories;
- agent recovery from build, tool, and environment failures;
- evaluation of patch readability, architectural fit, and long-term ownership;
- safe division of labor between multiple agents and human reviewers;
- consistent cost and latency reporting.
