---
ai-generated: true
last-reviewed: 2026-07-30
---

# Security Of LLM Software: Coding, Dependencies, And Supply Chain

Back: [Academic Status](../Academic-Status.md)

Scope: security of AI-assisted code generation and review, poisoned or misleading coding context, generated dependencies, package hallucination, privacy-preserving code generation, and software-supply-chain consequences.

Checked: 2026-07-30. Generic code-agent capability papers belong in the sibling software-research dossier; this page requires an explicit security, privacy, or supply-chain outcome.

## Secure And Adversarial Code Generation

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Yan2024CodeBreaker | [An LLM-Assisted Easy-to-Trigger Backdoor Attack on Code Completion Models](https://dblp.org/rec/conf/uss/YanWDHLKH24) | 2024 | USENIX Security / DBLP | Code-model poisoning | Constructs easy-to-trigger backdoors in code-completion models. | Core |
| Li2025CodeGuarder | [Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection](https://dblp.org/rec/conf/ccs/LinWQCM25) | 2025 | ACM CCS / DBLP | Secure RAG coding | Injects security knowledge into retrieval-augmented generation. | Core |
| Ye2025ImportSnare | [ImportSnare: Directed “Code Manual” Hijacking in Retrieval-Augmented Code Generation](https://dblp.org/rec/conf/ccs/YeSQ25) | 2025 | ACM CCS / DBLP | RAG/code poisoning | Hijacks retrieved code manuals to steer generated programs. | Core |
| Nguyen2026NOIR | [NOIR: Privacy-Preserving Generation of Code with Open-Source LLMs](https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers) | 2026 | USENIX Security | Code privacy | Protects sensitive programming context in open-model code generation. | Accepted/program record |
| Thang2026GoodVibe | [GoodVibe: Security-by-Vibe for LLM-Based Code Generation](https://www.usenix.org/conference/usenixsecurity26/presentation/thang) | 2026 | USENIX Security | Secure generation | Adds security-oriented feedback to model-assisted code generation. | Accepted/program record |
| Sun2026IoTRAGuarder | [Securing Retrieval-Augmented Code Generation via Contextual Knowledge Injection: A Case for Embedded IoT Applications](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) | 2026 | USENIX Security | Embedded secure RAG | Uses contextual security knowledge to guard RAG code generation for embedded IoT. | Accepted/program record |
| Yu2026SecCodePRM | [SecCodePRM: A Process Reward Model for Code Security](https://arxiv.org/abs/2602.10418) | 2026 | ICML / arXiv | Security process reward | Supplies prefix-level security feedback for vulnerability detection and secure generation. | Accepted/program record |
| PrivCode2026 | [PrivCode: When Code Generation Meets Differential Privacy](https://doi.org/10.14722/ndss.2026.240936) | 2026 | NDSS | Code privacy | Studies differential privacy for code-generation workflows. | Core |
| Zhang2026SecureCodeGeneration | [How Secure is Secure Code Generation?](https://arxiv.org/abs/2601.07084) | 2026 | arXiv | Robustness evaluation | Tests whether claimed secure-generation behavior survives adversarial prompting. | Negative/Evaluation |

## Dependencies, Packages, And Developer-Facing Agents

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Spracklen2025PackageHallucinations | [We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs](https://dblp.org/rec/conf/uss/SpracklenWSMV25) | 2025 | USENIX Security / DBLP | Dependency supply chain | Measures hallucinated package names and the resulting attack opportunity. | Core |
| 2602.20717 | [PackMonitor: Enabling Zero Package Hallucinations Through Decoding-Time Monitoring](https://arxiv.org/abs/2602.20717) | 2026 | arXiv | Package defense | Monitors dependency suggestions during decoding. | Frontier |
| 2606.05647 | [Coding with “Enemy”: Can Human Developers Detect AI Agent Sabotage?](https://arxiv.org/abs/2606.05647) | 2026 | arXiv | Coding-agent sabotage | Measures whether developers detect malicious code-agent behavior. | Frontier |

## Cross-Cutting Evaluation

- Risky code execution and generation: `Guo2024RedCode`.
- Secure-generation platforms: `Wang2024SeCodePLT`, `Zhou2025SafeGenBench`, and `Ali2025SecureVibeBench`.
- Their canonical rows live in [Security Benchmarks And Evaluation](../Cross-Cutting/Security-Benchmarks-And-Evaluation.md).
- Human practice around coding assistants is maintained in [Human Factor](../../Human-Factor.md).
