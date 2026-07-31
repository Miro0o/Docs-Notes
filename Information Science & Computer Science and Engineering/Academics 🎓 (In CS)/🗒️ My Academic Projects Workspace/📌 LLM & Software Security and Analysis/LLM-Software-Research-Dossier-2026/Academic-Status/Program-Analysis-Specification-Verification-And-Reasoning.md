---
ai-generated: true
last-reviewed: 2026-07-30
---

# Program Analysis, Specification, Verification, and Reasoning

Back: [Academic Status](Academic-Status.md)

Scope: non-security static and symbolic analysis, semantic reasoning, abstract interpretation, runtime-behavior reasoning, and neuro-symbolic verification. Existing specification and proof rows are preserved here as foundations; new work whose primary claim is requirements formalization, proof retrieval, proof repair, or formal-model engineering belongs in [Formalization, Proof Engineering, and Verified Reasoning](Formalization-Proof-Engineering-And-Verified-Reasoning.md).

## Status

This is the clearest home for the “LLM proposes, formal tool checks” pattern. The model helps infer abstractions, invariants, specifications, intermediate steps, or code semantics; analyzers and proof systems retain authority over soundness and correctness.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Li2024StaticBugDetection | [Enhancing Static Analysis for Practical Bug Detection: An LLM-Integrated Approach](https://doi.org/10.1145/3649828) | 2024 | OOPSLA/PACMPL / DOI | LLift integrates LLM semantic reasoning with static analysis for practical bug finding. | Published |
| Blinn2024TypedHoles | [Statically Contextualizing Large Language Models with Typed Holes](https://2024.splashcon.org/track/splash-2024-OOPSLA) | 2024 | OOPSLA / official program | Uses typed holes to give LLMs statically meaningful program context. | Published |
| Cai2025Refine4LLM | [Automated Program Refinement: Guide and Verify Code Large Language Model with Refinement Calculus](https://popl25.sigplan.org/details/POPL-2025-popl-research-papers/69/Automated-Program-Refinement-Guide-and-Verify-Code-Large-Language-Model-with-Refinem) | 2025 | POPL / official program | Guides and verifies generated code through refinement calculus. | Published |
| Mugnier2025Laurel | [Laurel: Unblocking Automated Verification with Large Language Models](https://dblp.org/rec/journals/pacmpl/MugnierGPJY25) | 2025 | OOPSLA/PACMPL / proceedings | Uses LLM assistance to synthesize missing proof-relevant material that blocks verification. | Published |
| Li2025LLMSymbolicExecution | [Large Language Model Powered Symbolic Execution](https://dblp.org/rec/journals/pacmpl/LiMD25) | 2025 | OOPSLA/PACMPL / proceedings | Uses LLM reasoning to assist symbolic execution. | Published |
| Ma2025SpecGen | [SpecGen: Automated Generation of Formal Program Specifications via Large Language Models](https://doi.org/10.1109/ICSE55347.2025.00129) | 2025 | ICSE / DOI | Generates formal specifications for programs and evaluates their utility. | Published |
| Thompson2025Rango | [Rango: Adaptive Retrieval-Augmented Proving for Automated Software Verification](https://dblp.org/rec/conf/icse/ThompsonSCFSB0L25) | 2025 | ICSE / proceedings | Retrieves proof-relevant context for automated verification. | Published |
| Patel2025RuntimeErrorStaticDetection | [Planning a Large Language Model for Static Detection of Runtime Errors in Code Snippets](https://doi.org/10.1109/ICSE55347.2025.00102) | 2025 | ICSE / DOI | Uses planned reasoning for static detection of runtime errors. | Published |
| Chen2025RuntimeBehavior | [Reasoning Runtime Behavior of a Program with LLM: How Far are We?](https://doi.org/10.1109/ICSE55347.2025.00012) | 2025 | ICSE / DOI | Measures limits of LLM reasoning about program execution. | Published / Evaluation |
| Fein2025LitterBoxPlus | [LitterBox+: An Extensible Framework for LLM-enhanced Scratch Static Code Analysis](https://dblp.org/rec/conf/kbse/FeinOF25) | 2025 | ASE / proceedings | Adds LLM-generated explanations and extensibility to educational static analysis. | Published |
| Gu2026SAIL | [SAIL: Sound Abstract Interpreters with LLMs](https://doi.org/10.1145/3808308) | 2026 | PLDI/PACMPL / DOI | Synthesizes abstract transformers while hard semantic checks and an unsoundness cost guide refinement. | Published |
| Lee2026Expecto | [Expecto: Extracting Formal Specifications from Natural Language Description for Trustworthy Oracles](https://doi.org/10.1145/3808332) | 2026 | PLDI/PACMPL / DOI | Converts natural-language intent into formal specifications using a neuro-symbolic synthesis loop. | Published |
| Roy2026CodeSense | [CodeSense: a Real-World Benchmark and Dataset for Code Semantic Reasoning](https://openreview.net/forum?id=ehXVDJm0PS) | 2026 | ICLR Poster / official record | Uses execution traces from real Python, C, and Java projects to evaluate fine-grained semantic reasoning. | Published / Evaluation |
| He2026NeuroSymbolicProof | [Neuro-Symbolic Proof Generation for Scaling Systems Software Verification](https://www.usenix.org/conference/osdi26/presentation/he-baoding) | 2026 | OSDI / official proceedings | Proposes proof steps with an LLM and repairs, filters, and discharges them in Isabelle on systems software. | Published |
| ISSTA2026AutoCodeSherpa | [AutoCodeSherpa](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers) | 2026 | ISSTA Research Papers / accepted, conference upcoming | Official-program index record for symbolic program explanation; normalize full title, authors, and DOI after proceedings. | Accepted |

## Evidence Checklist

- define the formal object generated by the model;
- state which syntactic and semantic checks are sound;
- separate proof search success from proof validity;
- report false positives, timeouts, and human repair;
- preserve analyzer/prover versions and replay artifacts;
- test distribution shift across languages, libraries, and codebases.

## Boundary Notes

Vulnerability detection, security taint analysis, protocol security, and exploit-oriented symbolic execution remain in the [security dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md). This page owns general correctness and program-understanding claims.

For future additions, route static-analysis and semantic-reasoning contributions here, and route natural-language-to-formal, theorem-proving workflow, and proof-maintenance contributions to the focused [formalization and proof-engineering shelf](Formalization-Proof-Engineering-And-Verified-Reasoning.md).

## Research Gaps

- soundness-preserving synthesis beyond narrow domains;
- proof and specification reuse across repository evolution;
- calibrated abstention when a model cannot supply a valid intermediate;
- whole-program reasoning across foreign functions, concurrency, and reflection;
- benchmarks that distinguish reasoning from memorized code patterns.
