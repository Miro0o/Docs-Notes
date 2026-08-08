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

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Bulat2024QbbQuantizationBinary | [QBB: Quantization with Binary Bases for LLMs.](<http://papers.nips.cc/paper_files/paper/2024/hash/05b69cc4c8ff6e24c5de1ecd27223d37-Abstract-Conference.html>) | 2024 | NeurIPS / proceedings | Program Understanding Binary Analysis Decompilation And Reverse Engineering | Introduces or evaluates qBB: Quantization with Binary Bases for LLMs; abstract-level contribution review remains pending. | formal-venue |
| Fang2024StacksightUnveilingWebassembly | [StackSight: Unveiling WebAssembly through Large Language Models and Neurosymbolic Chain-of-Thought Decompilation](<https://proceedings.mlr.press/v235/fang24e.html>) | 2024 | ICML / proceedings | Program Understanding Binary Analysis Decompilation And Reverse Engineering | Introduces or evaluates stackSight: Unveiling WebAssembly through Large Language Models and Neurosymbolic Chain-of-Thought Decompilation; abstract-level contribution review remains pending. | formal-venue |
| She2024WadecDecompilingWebassembly | [WaDec: Decompiling WebAssembly Using Large Language Model.](<https://doi.org/10.1145/3691620.3695020>) | 2024 | ASE / proceedings | Program Understanding Binary Analysis Decompilation And Reverse Engineering | Introduces or evaluates waDec: Decompiling WebAssembly Using Large Language Model; abstract-level contribution review remains pending. | formal-venue |
| Dong2025AdvancingBinaryCode | [Advancing Binary Code Similarity Detection via Context-Content Fusion and LLM Verification](<https://conf.researchr.org/track/ase-2025/ase-2025-papers#event-032d20f3-ea22-44f7-a468-4a268de8445c>) | 2025 | ASE / accepted-program | Program Understanding Binary Analysis Decompilation And Reverse Engineering | Studies advancing Binary Code Similarity Detection via Context-Content Fusion and LLM Verification; abstract-level contribution review remains pending. | formal-venue |
| Dong2025StbllmBreaking1 | [STBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs](<https://openreview.net/forum?id=6XUSDvBFkV>) | 2025 | ICLR / accepted-program | Program Understanding Binary Analysis Decompilation And Reverse Engineering | Introduces or evaluates sTBLLM: Breaking the 1-Bit Barrier with Structured Binary LLMs; abstract-level contribution review remains pending. | formal-venue |
| Sun2025EnhancingLlmDecompile | [Enhancing LLM to Decompile Optimized PTX to Readable CUDA for Tensor Programs](<https://conf.researchr.org/track/ase-2025/ase-2025-papers#event-02e78af2-01b3-4f09-9d02-c0371415ed12>) | 2025 | ASE / accepted-program | Program Understanding Binary Analysis Decompilation And Reverse Engineering | Introduces or evaluates enhancing LLM to Decompile Optimized PTX to Readable CUDA for Tensor Programs; abstract-level contribution review remains pending. | formal-venue |
| Wong2025DecllmLlmAugmented | [DecLLM: LLM-Augmented Recompilable Decompilation for Enabling Programmatic Use of Decompiled Code.](<https://doi.org/10.1145/3728958>) | 2025 | ISSTA / proceedings | Program Understanding Binary Analysis Decompilation And Reverse Engineering | Introduces or evaluates decLLM: LLM-Augmented Recompilable Decompilation for Enabling Programmatic Use of Decompiled Code; abstract-level contribution review remains pending. | formal-venue |
| Basque2026DecompilingSynergyEmpirical | [Decompiling the Synergy: An Empirical Study of Human-LLM Teaming in Software Reverse Engineering.](<https://www.ndss-symposium.org/ndss-paper/decompiling-the-synergy-an-empirical-study-of-human-llm-teaming-in-software-reverse-engineering/>) | 2026 | NDSS / proceedings | Program Understanding Binary Analysis Decompilation And Reverse Engineering | Benchmarks or evaluates decompiling the Synergy: An Empirical Study of Human-LLM Teaming in Software Reverse Engineering; abstract-level contribution review remains pending. | formal-venue |
| Park2026AnybcqHardwareEfficient | [AnyBCQ: Hardware Efficient Flexible Binary-Coded Quantization for Multi-Precision LLMs](<https://openreview.net/forum?id=XPIEkFdEDi>) | 2026 | ICLR / accepted-program | Program Understanding Binary Analysis Decompilation And Reverse Engineering | Introduces or evaluates anyBCQ: Hardware Efficient Flexible Binary-Coded Quantization for Multi-Precision LLMs; abstract-level contribution review remains pending. | formal-venue |
| Tan2026Sk2DecompileLlmBased | [SK2Decompile: LLM-based Two-Phase Binary Decompilation from Skeleton to Skin](<https://openreview.net/forum?id=jSQPqdoidy>) | 2026 | ICLR / accepted-program | Program Understanding Binary Analysis Decompilation And Reverse Engineering | Introduces or evaluates sK2Decompile: LLM-based Two-Phase Binary Decompilation from Skeleton to Skin; abstract-level contribution review remains pending. | formal-venue |
| Wang2026MemebqMemoryEfficient | [MemeBQ: Memory Efficient Binary Quantization of LLMs.](<https://doi.org/10.1609/aaai.v40i31.39881>) | 2026 | AAAI / proceedings | Program Understanding Binary Analysis Decompilation And Reverse Engineering | Introduces or evaluates memeBQ: Memory Efficient Binary Quantization of LLMs; abstract-level contribution review remains pending. | formal-venue |
| normalization2026RabitqcacheRotatedBinary | [RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference](<https://icml.cc/virtual/2026/poster/60504>) | 2026 | ICML / accepted-program | Program Understanding Binary Analysis Decompilation And Reverse Engineering | Introduces or evaluates raBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference; abstract-level contribution review remains pending. | formal-venue |

### Frontier Preprints

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Koller2026ReforgeMethodBenchmarking | [REFORGE: A Method for Benchmarking LLMs' Reverse Engineering Capabilities in Decompiled Binary Function Naming](<https://arxiv.org/abs/2607.07738>) | 2026 | arXiv / frontier-preprint | Program Understanding Binary Analysis Decompilation And Reverse Engineering | This paper presents Reforge, a provenance-tracked pipeline that constructs function-level ground truth from C source through compilation, DWARF and syntactic extraction, alignment, and decompilation…. | frontier-preprint |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
