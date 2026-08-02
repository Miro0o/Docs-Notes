---
ai-generated: true
last-reviewed: 2026-07-30
---

# Requirements, Design, Maintenance, and Evolution

Back: [Academic Status](Academic-Status.md)

Scope: intent and requirements, specification alignment, architecture recovery and conformance, design-issue localization, process models, API and dependency evolution, release work, and migration. Refactoring and structural-quality work belongs in [Quality, Refactoring, Technical Debt, and Code Smells](Quality-Refactoring-Technical-Debt-And-Code-Smells.md). Existing documentation, comment, intent-extraction, and summarization rows are preserved here; new work whose primary claim is code comprehension, retrieval, summaries, documentation, or API knowledge belongs in [Program Comprehension, Search, Retrieval, Documentation, and APIs](Program-Comprehension-Search-Retrieval-Documentation-And-APIs.md).

## Status

Maintenance is where short-term generation gains meet long-term software costs. Models must reason about missing and ambiguous intent, architectural structure, compatibility, deprecation, documentation, release conventions, and branch-specific context. Evaluation should therefore measure requirements fidelity, architectural conformance, future-facing correctness, and reviewer burden rather than only whether an edit passes today's tests.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Wang2025DeprecatedAPI | [LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-Based Code Completion](https://doi.org/10.1109/ICSE55347.2025.00245) | 2025 | ICSE / DOI | Tests whether completion adapts to API deprecation and library evolution. | Published / Evaluation |
| Tinnes2025ModelEvolution | [Software Model Evolution with Large Language Models: Experiments on Simulated, Public, and Industrial Datasets](https://doi.org/10.1109/ICSE55347.2025.00112) | 2025 | ICSE / DOI | Evaluates LLM-assisted evolution of software models across data sources. | Published |
| Ruan2025SpecRover | [SpecRover: Code Intent Extraction via Large Language Models](https://doi.org/10.1109/ICSE55347.2025.00080) | 2025 | ICSE / DOI | Extracts code intent to guide software change. | Published |
| Batole2025DesignIssue | [An LLM-Based Agent-Oriented Approach for Automated Code Design Issue Localization](https://doi.org/10.1109/ICSE55347.2025.00100) | 2025 | ICSE / DOI | Localizes design issues with an agent-oriented workflow. | Published |
| Rong2025CommentConsistency | [Code Comment Inconsistency Detection and Rectification](https://doi.org/10.1109/ICSE55347.2025.00035) | 2025 | ICSE / DOI | Detects and rectifies divergence between code and comments. | Published |
| Sun2025CodeSummarization | [Source Code Summarization in the Era of Large Language Models](https://doi.org/10.1109/ICSE55347.2025.00034) | 2025 | ICSE / DOI | Evaluates and improves summaries used for program comprehension and maintenance. | Published |
| Lin2025SOEN101 | [SOEN-101: Code Agents for Software Process Models](https://doi.org/10.1109/ICSE55347.2025.00140) | 2025 | ICSE / DOI | Applies agents to structured software-process work. | Published |
| Daneshyan2025SmartNote | [SmartNote: An LLM-Powered, Personalised Release Note Generator That Just Works](https://conf.researchr.org/track/fse-2025/fse-2025-research-papers) | 2025 | FSE Research Papers / official program | Generates personalized release notes from project changes. | Official program |
| Fruntke2025DependencyRepair | [Automatically Fixing Dependency Breaking Changes](https://conf.researchr.org/details/fse-2025/fse-2025-research-papers/38/Automatically-fixing-dependency-breaking-changes) | 2025 | FSE / official program | Compares agentic and iterative repair of dependency-update breakage. | Official program |
| Kang2026Pig | [Pig: Leveraging Large Language Models for Python Library Migrations](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Supports cross-version or cross-library Python migration. | Official program |
| ICSE2026Depradar | [Depradar](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Targets deprecated API detection/evolution; normalize full metadata after proceedings. | Accepted |
| Tian2026Specine | [Aligning Requirement for Large Language Model's Code Generation](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/55/Aligning-Requirement-for-Large-Language-Model-s-Code-Generation) | 2026 | ICSE Research Track / official program | Specine identifies, lifts, and aligns a model's perceived specification with the stated requirement before code generation. | Official program |
| Wu2026ReqCompleter | [Unlocking the Silent Needs: Business-Logic-Driven Iterative Requirements Auto-completion](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/68/Unlocking-the-Silent-Needs-Business-Logic-Driven-Iterative-Requirements-Auto-complet) | 2026 | ICSE Research Track / official program | Combines use cases, entity-relationship diagrams, and CRUD matrices to detect and complete missing business functions. | Official program |
| Singh2026Speculate | [Speculate: Generating REST API Specifications Using LLMs](https://doi.org/10.1145/3797118) | 2026 | FSE/PACMSE / DOI | Combines lightweight static analysis with an LLM to recover OpenAPI specifications across languages and frameworks. | Published |
| Zhang2026SemRef | [Semantic-Enhanced Automatic Refinement of Architecture Recovery Results Using LLMs](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/72/Semantic-Enhanced-Automatic-Refinement-of-Architecture-Recovery-Results-Using-LLMs) | 2026 | ICSE Research Track / official program | Combines LLM-derived semantics with dependencies to refine architecture-recovery results against known architectures. | Official program |

## Evaluation Checklist

- identify the historical revision and future API/library version;
- measure behavioral preservation, migration completeness, and rollback;
- report generated-document factuality and audience usefulness;
- include architectural/design context, not only local diffs;
- evaluate recovered or generated requirements against independently checked business rules and trace links;
- compare recovered architecture with published ground truth and test conformance after subsequent edits;
- measure review, future modification, and ownership cost;
- distinguish model knowledge from retrieved current documentation.

## Research Gaps

- long-term field studies of AI-authored code ownership;
- reliable requirements-to-specification traceability;
- architectural conformance across multi-file agent edits;
- migrations across concurrency, memory-management, and ecosystem semantics;
- project-specific documentation style and factuality;
- dependency evolution under incomplete or conflicting documentation.

## Routing Note

This shelf owns intent, architecture, and change-over-time claims. The focused [program-comprehension shelf](Program-Comprehension-Search-Retrieval-Documentation-And-APIs.md) owns new information-access and documentation-first claims, while the [quality and refactoring shelf](Quality-Refactoring-Technical-Debt-And-Code-Smells.md) owns behavior-preserving structural improvement. Future refreshes should not add the same paper to more than one page.

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Ma2024EurekaHumanLevel | [Eureka: Human-Level Reward Design via Coding Large Language Models](<https://openreview.net/forum?id=IEduRUO55F>) | 2024 | ICLR / accepted-program | Requirements Design Maintenance And Evolution | Introduces or evaluates eureka: Human-Level Reward Design via Coding Large Language Models; abstract-level contribution review remains pending. | formal-venue |
| Chen2025RiseDownBabel | [The Rise and Down of Babel Tower: Investigating the Evolution Process of Multilingual Code Large Language Model](<https://openreview.net/forum?id=eznTVIM3bs>) | 2025 | ICLR / accepted-program | Requirements Design Maintenance And Evolution | Introduces or evaluates the Rise and Down of Babel Tower: Investigating the Evolution Process of Multilingual Code Large Language Model; abstract-level contribution review remains pending. | formal-venue |
| Dang2025MiggptHarnessingLarge | [MigGPT: Harnessing Large Language Models for Automated Migration of Out-of-Tree Linux Kernel Patches Across Versions.](<http://papers.nips.cc/paper_files/paper/2025/hash/3760dbb5835bf0b771c3f83cb27ef2c0-Abstract-Conference.html>) | 2025 | NeurIPS / proceedings | Requirements Design Maintenance And Evolution | Introduces or evaluates migGPT: Harnessing Large Language Models for Automated Migration of Out-of-Tree Linux Kernel Patches Across Versions; abstract-level contribution review remains pending. | formal-venue |
| Wang2025CodesyncSynchronizingLarge | [CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale](<https://proceedings.mlr.press/v267/wang25t.html>) | 2025 | ICML / proceedings | Requirements Design Maintenance And Evolution | Introduces or evaluates codeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale; abstract-level contribution review remains pending. | formal-venue |
| Wang2025LlmAugmentedChemical | [LLM-Augmented Chemical Synthesis and Design Decision Programs](<https://proceedings.mlr.press/v267/wang25ag.html>) | 2025 | ICML / proceedings | Requirements Design Maintenance And Evolution | Introduces or evaluates lLM-Augmented Chemical Synthesis and Design Decision Programs; abstract-level contribution review remains pending. | formal-venue |
| Kaya2026RoleLargeLanguage | [On the Role of Large Language Models in Robustness-Guided Requirement Falsification](<https://conf.researchr.org/track/issta-2026/issta-2026-research-papers#event-f699be3f-3c9a-4305-af5e-5f83cfc37201>) | 2026 | ISSTA / accepted-program | Requirements Design Maintenance And Evolution | Introduces or evaluates on the Role of Large Language Models in Robustness-Guided Requirement Falsification; abstract-level contribution review remains pending. | formal-venue |
| Rontogiannis2026InteractiveEvaluationLarge | [Interactive Evaluation of Large Language Models for Multi-Requirement Software Engineering Tasks.](<https://doi.org/10.1609/aaai.v40i39.40564>) | 2026 | AAAI / proceedings | Requirements Design Maintenance And Evolution | Benchmarks or evaluates interactive Evaluation of Large Language Models for Multi-Requirement Software Engineering Tasks; abstract-level contribution review remains pending. | formal-venue |
| Sadikov2026LlmGuidedEvolutionary | [LLM-Guided Evolutionary Program Synthesis for Quasi-Monte Carlo Design](<https://openreview.net/forum?id=6L8fgclOTS>) | 2026 | ICLR / accepted-program | Requirements Design Maintenance And Evolution | Introduces or evaluates lLM-Guided Evolutionary Program Synthesis for Quasi-Monte Carlo Design; abstract-level contribution review remains pending. | formal-venue |
| Zhang2026RethinkingCodeSimilarity | [Rethinking Code Similarity for Automated Algorithm Design with LLMs](<https://openreview.net/forum?id=HIUqeO9OOr>) | 2026 | ICLR / accepted-program | Requirements Design Maintenance And Evolution | Introduces or evaluates rethinking Code Similarity for Automated Algorithm Design with LLMs; abstract-level contribution review remains pending. | formal-venue |
| normalization20262DeptLarge | [$A_2$DEPT: Large Language Model–Driven Automated Algorithm Design via Evolutionary Program Trees](<https://icml.cc/virtual/2026/poster/64869>) | 2026 | ICML / accepted-program | Requirements Design Maintenance And Evolution | Introduces or evaluates $A_2$DEPT: Large Language Model–Driven Automated Algorithm Design via Evolutionary Program Trees; abstract-level contribution review remains pending. | formal-venue |

### Frontier Preprints

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Rocha2026FromAwarenessAction | [From Awareness to Action: How Developers Engage with Accessibility Innovation in LLM-Assisted Development](<https://arxiv.org/abs/2606.10311>) | 2026 | arXiv / frontier-preprint | Requirements Design Maintenance And Evolution | Developers often struggle to design truly accessible digital solutions in corporate environments. | frontier-preprint |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
