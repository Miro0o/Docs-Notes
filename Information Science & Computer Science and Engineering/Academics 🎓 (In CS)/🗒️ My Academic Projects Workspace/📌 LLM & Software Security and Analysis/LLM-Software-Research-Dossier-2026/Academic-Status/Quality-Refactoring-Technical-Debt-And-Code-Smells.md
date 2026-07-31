---
ai-generated: true
last-reviewed: 2026-07-30
---

# Quality, Refactoring, Technical Debt, and Code Smells

Back: [Academic Status](Academic-Status.md)

Scope: behavior-preserving refactoring, structural code quality, technical-debt reduction, and detection or repair of code and comment smells in ordinary software. Behavior-changing bug repair remains on the testing-and-repair shelf.

## Status

LLM-assisted quality work is shifting from isolated rewrite prompts to checked, repository-aware workflows. Credible evidence must distinguish a cleaner-looking diff from a behavior-preserving improvement and account for tests, metric validity, project conventions, review cost, and smells introduced by generated code itself.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Guo2024CodeRefinement | [Exploring the Potential of ChatGPT in Automated Code Refinement: An Empirical Study](https://doi.org/10.1145/3597503.3623306) | 2024 | ICSE / DOI | Evaluates ChatGPT for refinement-oriented transformations and identifies correctness and quality limitations. | Published / Evaluation |
| Caglar2025InlineCommentSmells | [Automated Inline Comment Smell Detection and Repair with Large Language Models](https://conf.researchr.org/details/ase-2025/ase-2025-papers/36/Automated-Inline-Comment-Smell-Detection-and-Repair-with-Large-Language-Models) | 2025 | ASE Research Papers / official program | Studies LLM-based detection and repair of inline-comment smells. | Official program |
| Oueslati2026RefAgent | [RefAgent: A Multi-agent LLM-based Framework for Automatic Software Refactoring](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/111/RefAgent-A-Multi-agent-LLM-based-Framework-for-Automatic-Software-Refactoring) | 2026 | ICSE Research Track / official program | Coordinates planning, execution, testing, and refinement agents for repository-level Java refactoring. | Official program |
| Velasco2026GeneratedCodeSmells | [A Causal Perspective on Measuring, Explaining and Mitigating Smells in LLM-Generated Code](https://doi.org/10.1145/3744916.3773164) | 2026 | ICSE / DOI | Defines a smell-propensity measure, causally analyzes generation factors, and evaluates mitigation strategies. | Published / Evaluation |

## Evaluation Checklist

- state whether the transformation must preserve behavior or intentionally change it;
- run independent regression tests and static checks before and after the edit;
- justify smell and quality metrics against developer judgments and project conventions;
- measure diff size, readability, review effort, and later maintainability;
- test interactions among refactorings instead of scoring isolated edits only;
- report rejected, reverted, uncompilable, and behavior-changing transformations.

## Boundary and Cross-Links

- Behavior-changing defect repair belongs in [Testing, Debugging, and General Repair](Testing-Debugging-And-General-Repair.md).
- Comment consistency tied to code evolution remains in [Requirements, Design, Maintenance, and Evolution](Requirements-Design-Maintenance-And-Evolution.md); comment-smell detection and repair is canonical here.
- Performance-first refactoring belongs in [Performance Optimization and Compilation](Performance-Optimization-And-Compilation.md).
- Architecture recovery and conformance belong in [Requirements, Design, Maintenance, and Evolution](Requirements-Design-Maintenance-And-Evolution.md).
- Secure refactoring, vulnerability patch quality, and security smells belong in the [software-security dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md).

## Research Gaps

- longitudinal measurement of technical-debt repayment versus debt displacement;
- reliable behavior preservation for multi-file and concurrency-sensitive refactorings;
- project-specific quality rules without circular LLM judging;
- interaction between generated-code volume and human review capacity;
- benchmarks with independently validated smells, fixes, and maintenance outcomes.
