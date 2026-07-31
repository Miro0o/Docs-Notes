---
ai-generated: true
last-reviewed: 2026-07-30
---

# Formalization, Proof Engineering, and Verified Reasoning

Back: [Academic Status](Academic-Status.md)

Scope: translating informal software intent into formal models or temporal logic, synthesizing invariants and proof steps, retrieving proof knowledge, repairing formal artifacts, and using model checkers or proof assistants as the final authority.

## Status

The strongest pattern is a checked translation pipeline: an LLM decomposes intent or proposes a formal artifact, while a parser, model checker, solver, proof assistant, counterexample, or distinguishing trace validates it. Recent work also treats proof engineering as a repository task involving retrieval, repair, and collaboration rather than a single tactic prediction.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Cao2025Clause2Inv | [Clause2Inv: A Generate-Combine-Check Framework for Loop Invariant Inference](https://doi.org/10.1145/3728920) | 2025 | ISSTA/PACMSE / DOI | Decomposes candidate invariants into clauses and repeatedly generates, combines, and checks them. | Published |
| Ma2025Req2LTL | [Bridging Natural Language and Formal Specification—Automated Translation of Software Requirements to LTL via Hierarchical Semantics Decomposition Using LLMs](https://doi.org/10.1109/ASE63991.2025.00104) | 2025 | ASE / DOI; Distinguished Paper | Uses a structured intermediate representation and deterministic synthesis to translate requirements into LTL. | Published |
| Zuo2025PATAgent | [PAT-Agent: Autoformalization for Model Checking](https://doi.org/10.1109/ASE63991.2025.00176) | 2025 | ASE / DOI | Generates formal models from natural language and repairs them using model-checker counterexamples. | Published |
| Hu2026ADARULE | [ADARULE: LLM-Driven Natural Language to LTL Conversion via Pattern-Adaptive Rule Induction](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Induces adaptable translation rules for natural-language-to-LTL conversion. | Official program |
| Mendoza2026ARTEMIS | [Automating Requirements Formalization: Using LLMs and Low-Complexity Distinguishing Traces for Semantic Validation](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/287/Automating-Requirements-Formalization-Using-LLMs-and-Low-Complexity-Distinguishing-T) | 2026 | ICSE Research Track / official program | Uses structured translation and distinguishing traces to reduce semantic-validation effort. | Official program |
| Wang2026EventBAgent | [Event-B Agent: Towards LLM Agent for Formal Model Synthesis and Repair](https://conf.researchr.org/details/fse-2026/fse-2026-research-papers/211/Event-B-Agent-Towards-LLM-Agent-for-Formal-Model-Synthesis-and-Repair) | 2026 | FSE Research Papers / official program | Interleaves Event-B model synthesis, model checking, theorem proving, and repair. | Official program |
| Zhang2026ProofFusion | [ProofFusion: Improving Neural Theorem Proving via Adaptive Retrieval-Augmented Reasoning](https://doi.org/10.1145/3797139) | 2026 | FSE/PACMSE / DOI | Retrieves semantically related proof states and adaptively fuses their tactics with neural predictions. | Published |
| ICSE2026ProofCoop | [ProofCoop: Collaborative Automated Formal Verification](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Frames formal verification as a collaborative automated workflow; normalized proceedings metadata remains pending here. | Official program |

## Workshop and Frontier Signal

| Key | Work | Year | Evidence | Why watch it |
| --- | --- | ---: | --- | --- |
| He2025RankingFormalSpecs | [Ranking Formal Specifications using LLMs](https://conf.researchr.org/details/icfp-splash-2025/lmpl-2025-papers/10/Ranking-Formal-Specifications-using-LLMs) | 2025 | LMPL workshop position paper / official program | Treats specification triage and prioritization as a distinct proof-engineering problem; it is not a main OOPSLA paper. |

## Existing Foundations on the Analysis Shelf

SpecGen, Rango, Laurel, refinement calculus, SAIL, Expecto, and neuro-symbolic systems-software verification retain their existing canonical rows under [Program Analysis, Specification, Verification, and Reasoning](Program-Analysis-Specification-Verification-And-Reasoning.md). This page adds the missing formalization and proof-engineering thread without duplicating them.

## Evaluation Checklist

- distinguish syntactic validity, semantic fidelity, provability, and proof validity;
- identify the exact trusted checker and replay every accepted artifact;
- expose failed proof attempts, timeouts, counterexamples, and human repairs;
- test ambiguity and underspecification rather than only curated requirements;
- measure proof maintenance after the program or specification changes;
- keep generated tests or traces independent enough to detect translation mistakes.

## Boundary Notes

Formal verification of ordinary functionality and correctness belongs here. Verification whose primary claim is vulnerability discovery, exploitability, protocol security, or security patching belongs in the [security dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md).

## Research Gaps

- semantic validation for requirements with missing domain assumptions;
- proof repair across commits, dependency changes, and refactoring;
- repository-scale theorem retrieval with transparent provenance;
- formalization of concurrency, distributed failures, and environment behavior;
- calibrated abstention before an invalid formal artifact enters a trusted workflow;
- longitudinal evidence that LLM assistance lowers total proof-maintenance cost.
