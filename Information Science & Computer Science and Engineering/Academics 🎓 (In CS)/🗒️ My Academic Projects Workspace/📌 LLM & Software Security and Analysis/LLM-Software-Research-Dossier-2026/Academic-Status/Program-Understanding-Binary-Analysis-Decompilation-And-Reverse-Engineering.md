---
ai-generated: true
last-reviewed: 2026-07-30
---

# Program Understanding, Binary Analysis, Decompilation, and Reverse Engineering

Back: [Academic Status](Academic-Status.md)

Scope: non-security program understanding for binaries and other compiled representations, including decompilation, symbol and type recovery, recompilable reconstruction, semantic-fidelity improvement, and representation evaluation. A paper belongs here when its primary oracle is readability, reconstruction fidelity, compilation, semantic preservation, or analyst comprehension rather than vulnerability, malware, exploit, or defense evidence.

## Status

LLMs can restore names, types, structure, and intent that compilation removes, but plausible reconstructed source is not sufficient evidence. Strong evaluation separately measures syntax, recompilability, behavioral equivalence, recovered abstractions, semantic fidelity, and human comprehension. Publication at a security venue does not by itself make a decompilation paper security-first.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Hu2024DeGPT | [DeGPT: Optimizing Decompiler Output with LLM](https://www.ndss-symposium.org/ndss-paper/degpt-optimizing-decompiler-output-with-llm/) | 2024 | NDSS / official proceedings | Improves the readability and simplicity of decompiler output with role-separated LLM checking. | Published |
| Xie2024ReSym | [ReSym: Harnessing LLMs to Recover Variable and Data Structure Symbols from Stripped Binaries](https://dblp.org/rec/conf/ccs/Xie00X0024) | 2024 | ACM CCS / proceedings | Recovers names and types for local variables and user-defined data structures from stripped binaries. | Published |
| Su2025DiSCo | [DiSCo: Towards Decompiling EVM Bytecode to Source Code using Large Language Models](https://dblp.org/rec/journals/pacmse/SuLWNXZ25) | 2025 | FSE/PACMSE / proceedings | Reconstructs source-like code from EVM bytecode and evaluates decompilation quality. | Published |
| Idioms2026 | [Idioms: A Simple and Effective Framework for Turbo-Charging Local Neural Decompilation with Well-Defined Types](https://doi.org/10.14722/ndss.2026.240795) | 2026 | NDSS / DOI | Generates user-defined type definitions with decompiled code and introduces a realistic typed benchmark. | Published |
| Li2026FidelityGPT | [FidelityGPT: Correcting Decompilation Distortions with Retrieval Augmented Generation](https://www.ndss-symposium.org/ndss-paper/fidelitygpt-correcting-decompilation-distortions-with-retrieval-augmented-generation/) | 2026 | NDSS / official proceedings | Detects and corrects semantic distortions to improve decompiled-code accuracy and readability. | Published |
| Jiang2026IRDecompilation | [Does Representation Matter? Evaluating IRs for LLM-based Binary Decompilation](https://www.ndss-symposium.org/ndss-paper/auto-draft-654/) | 2026 | NDSS BAR / workshop record | Compares intermediate representations for LLM-based binary decompilation under controlled reconstruction metrics. | Frontier |

## Evaluation Checklist

- distinguish readable output from compilable and behaviorally equivalent output;
- report compiler, optimization level, architecture, decompiler, and symbol-stripping configuration;
- evaluate names, types, control structure, data layout, and whole-program context separately;
- replay behavioral tests or equivalence checks rather than relying only on textual similarity;
- measure analyst comprehension with controlled tasks when making human-utility claims;
- test generalization across toolchains, optimization levels, architectures, and unseen binaries.

## Boundary Notes

- Binary taint analysis, malware analysis, malicious-command explanation, protected-code defense, cryptographic reverse engineering, and vulnerability-directed binary analysis remain in the sibling [software-security dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md).
- A security use case may cross-link to a paper here, but the canonical shelf follows the paper's evaluated contribution and oracle.
- Source-level program comprehension and formal reasoning remain in [Program Analysis, Specification, Verification, and Reasoning](Program-Analysis-Specification-Verification-And-Reasoning.md).

## Research Gaps

- whole-program decompilation with recoverable build and dependency context;
- semantics-aware evaluation beyond token and exact-match metrics;
- calibrated uncertainty for hallucinated names, types, and control structure;
- reliable reconstruction across architectures, compilers, and optimization levels;
- longitudinal evidence about analyst productivity and error rates;
- integration with debuggers and analyzers without treating reconstructed source as ground truth.
