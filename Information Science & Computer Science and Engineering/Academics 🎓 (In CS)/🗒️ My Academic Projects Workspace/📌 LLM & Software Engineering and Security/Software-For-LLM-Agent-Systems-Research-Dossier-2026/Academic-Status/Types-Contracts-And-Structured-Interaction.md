---
ai-generated: true
last-reviewed: 2026-07-30
---

# Types, Contracts, and Structured Interaction

Back: [Academic Status](Academic-Status.md)

Scope: formal output languages, schemas, semantic interfaces, data protocols, and other contracts that make model and agent interactions machine-checkable and interoperable.

## Status

Reliable agent software needs more than valid JSON. It needs contracts for syntax, tool arguments, state transitions, action/observation trajectories, versioning, and eventually effects and permissions. Present top-venue work is strongest on grammar-constrained generation and representation interoperability; behavioral contracts remain a major gap.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| BeurerKellner2024DOMINO | [Guiding LLMs the Right Way: Fast, Non-Invasive Constrained Generation](https://proceedings.mlr.press/v235/beurer-kellner24a.html) | 2024 | ICML / proceedings | Introduces DOMINO, a subword-aligned constrained-decoding algorithm designed to preserve accuracy while reducing constraint overhead. | Published |
| Dong2025XGrammar | [XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models](https://proceedings.mlsys.org/paper_files/paper/2025/hash/5c20ca4b0b20b0bd2f1d839dc605e70f-Abstract-Conference.html) | 2025 | MLSys / proceedings | Implements context-free-grammar execution with prechecking, caching, persistent stacks, and inference-engine co-design for low-overhead structured output. | Published / Systems |
| Song2026ADP | [Agent Data Protocol: Unifying Datasets for Diverse, Effective Fine-tuning of LLM Agents](https://openreview.net/forum?id=tG6301ORHd) | 2026 | ICLR Oral / official conference paper | Defines a lightweight interlingua for agent actions, observations, APIs, code, and messages; unifies 13 datasets for downstream training pipelines. | Published / Protocol |

## Contract Layers

| Layer | Example obligation | Current maturity |
| --- | --- | --- |
| Lexical/syntactic | output parses under a grammar or schema | comparatively mature |
| Structural | required fields and tool arguments are present and typed | widely deployed, unevenly evaluated |
| Semantic | values satisfy domain constraints and cross-field invariants | early |
| Behavioral | permitted action order and state transitions are respected | early |
| Effect/permission | external effects, authority, and approval requirements are explicit | research gap |
| Reliability | uncertainty, retry, abstention, and fallback obligations are specified | research gap |
| Interoperability | trajectories round-trip across frameworks and versions | emerging |

## Evaluation Checklist

- define the accepted formal language precisely;
- report schema/grammar coverage and unsupported constructs;
- test tokenizer/subword alignment and Unicode edge cases;
- separate syntactic conformance from semantic correctness;
- measure compile/precomputation cost and per-token overhead;
- include invalid, ambiguous, recursive, and adversarially large schemas;
- for protocols, test lossless round trips across independent implementations;
- document version negotiation and backward compatibility;
- avoid treating a single successful parse as a behavioral guarantee.

## Research Directions

- refinement types for tool arguments and returned state;
- session types for multi-agent protocols;
- effect systems for external calls, state mutation, and irreversible actions;
- contracts that combine deterministic validators with calibrated uncertainty;
- temporal specifications for long-horizon workflows;
- protocol conformance suites and differential testing;
- provenance and causality fields that survive framework conversion;
- typed fallback, retry, compensation, and human-approval policies.

## Boundary

Security policy enforcement is cross-cutting. Work whose main result is attack prevention, authorization, or adversarial robustness belongs in the security dossier. General structured interaction and interoperability remain here.
