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

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| 00012024ZkllmZeroKnowledge | [zkLLM: Zero Knowledge Proofs for Large Language Models.](<https://doi.org/10.1145/3658644.3670334>) | 2024 | ACM CCS / proceedings | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates zkLLM: Zero Knowledge Proofs for Large Language Models; abstract-level contribution review remains pending. | formal-venue |
| Lin2024FvelInteractiveFormal | [FVEL: Interactive Formal Verification Environment with Large Language Models via Theorem Proving.](<http://papers.nips.cc/paper_files/paper/2024/hash/62c6d7893b13a13c659cb815852dd00d-Abstract-Datasets_and_Benchmarks_Track.html>) | 2024 | NeurIPS / proceedings | Formalization Proof Engineering And Verified Reasoning | Studies fVEL: Interactive Formal Verification Environment with Large Language Models via Theorem Proving; abstract-level contribution review remains pending. | formal-venue |
| Lu2024ProofAutomationLarge | [Proof Automation with Large Language Models.](<https://doi.org/10.1145/3691620.3695521>) | 2024 | ASE / proceedings | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates proof Automation with Large Language Models; abstract-level contribution review remains pending. | formal-venue |
| Zhou2024DonTTrust | [Don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization](<https://openreview.net/forum?id=V5tdi14ple>) | 2024 | ICLR / accepted-program | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates don't Trust: Verify -- Grounding LLM Quantitative Reasoning with Autoformalization; abstract-level contribution review remains pending. | formal-venue |
| 00012025ZkgptEfficientNon | [zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference.](<https://www.usenix.org/conference/usenixsecurity25/presentation/qu-zkgpt>) | 2025 | USENIX Security / proceedings | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference; abstract-level contribution review remains pending. | formal-venue |
| Balunovic2025MathconstructChallengingLlm | [MathConstruct: Challenging LLM Reasoning with Constructive Proofs](<https://proceedings.mlr.press/v267/balunovic25a.html>) | 2025 | ICML / proceedings | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates mathConstruct: Challenging LLM Reasoning with Constructive Proofs; abstract-level contribution review remains pending. | formal-venue |
| Dong2025StpSelfPlay | [STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving](<https://proceedings.mlr.press/v267/dong25h.html>) | 2025 | ICML / proceedings | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates sTP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving; abstract-level contribution review remains pending. | formal-venue |
| Hao2025PlanningAnythingRigor | [Planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming](<https://openreview.net/forum?id=0K1OaL6XuK>) | 2025 | ICLR / accepted-program | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming; abstract-level contribution review remains pending. | formal-venue |
| Sheng2025LearningTheoremRationale | [Learning Theorem Rationale for Improving the Mathematical Reasoning Capability of Large Language Models.](<https://doi.org/10.1609/aaai.v39i14.33662>) | 2025 | AAAI / proceedings | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates learning Theorem Rationale for Improving the Mathematical Reasoning Capability of Large Language Models; abstract-level contribution review remains pending. | formal-venue |
| Sheng2025SolvingInequalityProofs | [Solving Inequality Proofs with Large Language Models.](<http://papers.nips.cc/paper_files/paper/2025/hash/c7931e2bb473bdf628b1c1a1dc9e1442-Abstract-Datasets_and_Benchmarks_Track.html>) | 2025 | NeurIPS / proceedings | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates solving Inequality Proofs with Large Language Models; abstract-level contribution review remains pending. | formal-venue |
| Lan2026TemplateTheoremsGraph | [Template-Theorems Graph Construction to Enhance Mathematical Reasoning Capabilities of LLM.](<https://doi.org/10.1609/aaai.v40i37.40411>) | 2026 | AAAI / proceedings | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates template-Theorems Graph Construction to Enhance Mathematical Reasoning Capabilities of LLM; abstract-level contribution review remains pending. | formal-venue |
| Mendoza2026AutomatingRequirementsFormalization | [Automating Requirements Formalization: Using LLMs and Low-Complexity Distinguishing Traces for Semantic Validation](<https://conf.researchr.org/track/icse-2026/icse-2026-research-track#event-4c47acb2-027b-4001-afbf-1b6fdda81ede>) | 2026 | ICSE / accepted-program | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates automating Requirements Formalization: Using LLMs and Low-Complexity Distinguishing Traces for Semantic Validation; abstract-level contribution review remains pending. | formal-venue |
| Tithy2026PoceAutomatedProof | [PoCE: Automated Proof-of-Concept Synthesis using Large Language Models for Robust Validation](<https://conf.researchr.org/track/issta-2026/issta-2026-research-papers#event-0d37006b-8fb8-42ca-989f-cee9ff082c8d>) | 2026 | ISSTA / accepted-program | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates poCE: Automated Proof-of-Concept Synthesis using Large Language Models for Robust Validation; abstract-level contribution review remains pending. | formal-venue |
| normalization2026AutomatedFormalProofs | [Automated Formal Proofs of Combinatorial Identities via Wilf–Zeilberger Guidance and LLMs](<https://icml.cc/virtual/2026/poster/63340>) | 2026 | ICML / accepted-program | Formalization Proof Engineering And Verified Reasoning | Introduces or evaluates automated Formal Proofs of Combinatorial Identities via Wilf–Zeilberger Guidance and LLMs; abstract-level contribution review remains pending. | formal-venue |
| normalization2026BrokenmathBenchmarkSycophancy | [BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs](<https://icml.cc/virtual/2026/poster/63323>) | 2026 | ICML / accepted-program | Formalization Proof Engineering And Verified Reasoning | Benchmarks or evaluates brokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs; abstract-level contribution review remains pending. | formal-venue |
| normalization2026CanLlmsReason8947455 | [Can LLMs Reason Like Automated Theorem Provers for Rust Verification? VCoT-Bench: Evaluating via Verification Chain of Thought](<https://icml.cc/virtual/2026/poster/63236>) | 2026 | ICML / accepted-program | Formalization Proof Engineering And Verified Reasoning | Benchmarks or evaluates can LLMs Reason Like Automated Theorem Provers for Rust Verification? VCoT-Bench: Evaluating via Verification Chain of Thought; abstract-level contribution review remains pending. | formal-venue |
| normalization2026Minif2FDafnyLlm | [miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification](<https://icml.cc/virtual/2026/poster/62536>) | 2026 | ICML / accepted-program | Formalization Proof Engineering And Verified Reasoning | Studies miniF2F-Dafny: LLM-Guided Mathematical Theorem Proving via Auto-Active Verification; abstract-level contribution review remains pending. | formal-venue |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
