---
ai-generated: true
last-reviewed: 2026-07-30
---

# Cross-Cutting: Security Benchmarks, Datasets, And Evaluation

Back: [Academic Status](../Academic-Status.md)

Scope: security-specific benchmarks and datasets for vulnerability reasoning, secure code generation, cyber agents, security-targeted reverse engineering, detection engineering, and agent/tool security. Generic coding, decompilation, and software-engineering benchmarks belong in the sibling software-research dossier.

Checked: 2026-07-30. These are canonical rows. Topic pages refer to these keys or this page rather than reproducing the paper row.

## Canonical Benchmark And Dataset Papers

| Key | Benchmark / paper | Year | Source | Evaluates | Independent evidence | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Zhang2024NYUCTF | [NYU CTF Bench: A Scalable Open-Source Benchmark Dataset for Evaluating LLMs in Offensive Security](https://dblp.org/rec/conf/nips/ShaoJUDxM0YGKKK24) | 2024 | NeurIPS / DBLP | Offensive-security CTF tasks | Executable challenge environments | Core |
| Alam2024CTIBench | [CTIBench: A Benchmark for Evaluating LLMs in Cyber Threat Intelligence](https://dblp.org/rec/conf/nips/AlamBNR24) | 2024 | NeurIPS / DBLP | Cyber threat intelligence | Task-specific answer sets and metrics | Core |
| Guo2024RedCode | [RedCode: Risky Code Execution and Generation Benchmark for Code Agents](https://dblp.org/rec/conf/nips/GuoLXZZ0SL24) | 2024 | NeurIPS / DBLP | Risky agent code behavior | Controlled execution/generation cases | Core |
| Bhatt2024CyberSecEval2 | [CyberSecEval 2: A Wide-Ranging Cybersecurity Evaluation Suite for Large Language Models](https://arxiv.org/abs/2404.13161) | 2024 | arXiv | Cyber risks and capabilities | Multi-task evaluation suite | Negative/Evaluation |
| Bhatt2024CyberSecEval3 | [CYBERSECEVAL 3: Advancing the Evaluation of Cybersecurity Risks and Capabilities in Large Language Models](https://arxiv.org/abs/2408.01605) | 2024 | arXiv | Cyber risks and capabilities | Expanded evaluation suite | Negative/Evaluation |
| Zhang2024Cybench | [Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models](https://arxiv.org/abs/2408.08926) | 2024 | arXiv | Cybersecurity agents | Interactive tasks and environment feedback | Core |
| Wang2024SeCodePLT | [SeCodePLT](https://arxiv.org/abs/2410.11096) | 2024 | arXiv | Security of code GenAI | Unified secure-code evaluation platform | Negative/Evaluation |
| Xu2025SVTrustEvalC | [SV-TrustEval-C: Evaluating Structure and Semantic Reasoning in Large Language Models for Source Code Vulnerability Analysis](https://dblp.org/rec/conf/sp/LiBHMKJJ25) | 2025 | IEEE S&P / DBLP | Vulnerability reasoning | Structural and semantic perturbations | Negative/Evaluation |
| Zhang2025ASB | [Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5750f91d8fb9d5c02bd8ad2c3b44456b-Abstract-Conference.html) | 2025 | ICLR / official proceedings | Agent attacks and defenses | Ten scenarios, more than 400 tools, attack/defense suites, and utility-security metrics | Core |
| Wei2025JsDeObsBench | [JsDeObsBench: Measuring and Benchmarking LLMs for JavaScript Deobfuscation](https://arxiv.org/abs/2506.20170) | 2025 | ACM CCS / arXiv | JavaScript deobfuscation | Curated deobfuscation tasks | Core |
| Zhou2025SafeGenBench | [SafeGenBench](https://arxiv.org/abs/2506.05692) | 2025 | arXiv | Security of generated code | Vulnerability-focused generation tests | Negative/Evaluation |
| Ali2025SecureVibeBench | [SecureVibeBench](https://arxiv.org/abs/2509.22097) | 2025 | arXiv | Multi-file secure coding | Functional and security oracles | Frontier |
| Shao2025CyberGym | [CyberGym: Evaluating AI Agents on Real-World Vulnerabilities Across Massive Codebases](https://arxiv.org/abs/2506.02548) | 2025 | arXiv | Repository-scale cyber agents | Real vulnerabilities and environments | Frontier |
| Nishizaka2026LLMResistantProtection | [Towards LLM-Resistant Software Protection: Agent Failure Patterns in CTF Reverse Engineering](https://www.ndss-symposium.org/ndss-paper/auto-draft-657/) | 2026 | NDSS BAR | Reverse-engineering agents | CTF failure-pattern analysis | Frontier |
| Patel2026ExploitBench | [ExploitBench: A Capability-Ladder Benchmark for Exploit Agents](https://arxiv.org/abs/2605.14153) | 2026 | arXiv | Exploit agents | Intermediate capability ladder | Frontier |
| 2603.10969 | [TOSSS: a CVE-based Software Security Benchmark for Large Language Models](https://arxiv.org/abs/2603.10969) | 2026 | arXiv | CVE-based security tasks | CVE-grounded examples | Frontier |
| 2604.03750 | [CREBench: Evaluating Large Language Models in Cryptographic Binary Reverse Engineering](https://arxiv.org/abs/2604.03750) | 2026 | arXiv | Cryptographic binary RE | Domain-specific binary tasks | Frontier |
| 2606.05844 | [GenTI: Benchmarking LLMs for Autonomous IDPS Rule Generation for Unseen Attacks](https://arxiv.org/abs/2606.05844) | 2026 | arXiv | IDPS rule generation | Unseen-attack rule evaluation | Frontier |
| 2606.05493 | [REStack: A Large-Scale Dataset of Reverse Engineering Discussions from Stack Exchange](https://arxiv.org/abs/2606.05493) | 2026 | arXiv | Reverse-engineering knowledge | Large analyst-discussion dataset | Frontier |

## Cross-Cutting Indexes Without Duplicate Paper Rows

| View | Canonical primary homes |
| --- | --- |
| Static-analysis benchmarks | `Xu2025SVTrustEvalC`, `2603.10969`; methods in [Program Analysis](../Security-Analysis/Program-Analysis.md) |
| Secure code generation | `Guo2024RedCode`, `Wang2024SeCodePLT`, `Zhou2025SafeGenBench`, `Ali2025SecureVibeBench`; methods in [Coding, Dependency, And Supply Chain](../Security-Of-LLM-Software/Coding-Dependency-And-Supply-Chain.md) |
| CTF and offensive agents | `Zhang2024NYUCTF`, `Bhatt2024CyberSecEval2`, `Bhatt2024CyberSecEval3`, `Zhang2024Cybench`, `Shao2025CyberGym`, `Patel2026ExploitBench`; systems in [Offensive, CTF, And Pentesting](../Cyber-Operations/Offensive-CTF-And-Pentesting.md) |
| SOC and CTI | `Alam2024CTIBench`, `2606.05844`; systems in [Defensive SOC And CTI](../Cyber-Operations/Defensive-SOC-And-CTI.md) |
| Security-targeted reverse engineering | `Wei2025JsDeObsBench`, `Nishizaka2026LLMResistantProtection`, `2604.03750`, `2606.05493`; methods in [Program Analysis](../Security-Analysis/Program-Analysis.md). Generic decompilation evaluation, including `Jiang2026IRDecompilation`, is canonical in the sibling [software-research dossier](../../../LLM-Software-Research-Dossier-2026/Academic-Status/Program-Understanding-Binary-Analysis-Decompilation-And-Reverse-Engineering.md). |
| Agent/tool security | `Zhang2025ASB`; MCP description/code measurement and MATEBench are components of papers canonically filed in [Apps, RAG, Agents, MCP, And Tool Runtimes](../Security-Of-LLM-Software/App-RAG-Agent-And-Tool-Runtimes.md) |

## Evaluation Minimum

- Prefer real repositories, validated vulnerabilities, executable environments, and deterministic security oracles.
- Report contamination checks, prompt/scaffold budget, retries, tool access, human intervention, and failure distributions.
- Separate vulnerability classification, reachability, reproduction, exploitability, patch correctness, and operational usefulness.
- Treat an LLM-as-judge score as supporting evidence, never the only oracle.

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Asare2024UserCenteredSecurity | [A User-centered Security Evaluation of Copilot.](<https://doi.org/10.1145/3597503.3639154>) | 2024 | ICSE / proceedings | Security Benchmarks And Evaluation | Benchmarks or evaluates a User-centered Security Evaluation of Copilot; abstract-level contribution review remains pending. | formal-venue |
| Chao2024JailbreakbenchOpenRobustness | [JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models.](<http://papers.nips.cc/paper_files/paper/2024/hash/63092d79154adebd7305dfd498cbff70-Abstract-Datasets_and_Benchmarks_Track.html>) | 2024 | NeurIPS / proceedings | Security Benchmarks And Evaluation | Benchmarks or evaluates jailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models; abstract-level contribution review remains pending. | formal-venue |
| Xu2024BagTricksBenchmarking | [Bag of Tricks: Benchmarking of Jailbreak Attacks on LLMs.](<http://papers.nips.cc/paper_files/paper/2024/hash/38c1dfb4f7625907b15e9515365e7803-Abstract-Datasets_and_Benchmarks_Track.html>) | 2024 | NeurIPS / proceedings | Security Benchmarks And Evaluation | Introduces or evaluates bag of Tricks: Benchmarking of Jailbreak Attacks on LLMs; abstract-level contribution review remains pending. | formal-venue |
| Cao2026SafedialbenchFineGrained | [SafeDialBench: A Fine-Grained Safety Evaluation Benchmark for Large Language Models in Multi-Turn Dialogues with Diverse Jailbreak Attacks](<https://openreview.net/forum?id=KFjtRqVnKH>) | 2026 | ICLR / accepted-program | Security Benchmarks And Evaluation | Benchmarks or evaluates safeDialBench: A Fine-Grained Safety Evaluation Benchmark for Large Language Models in Multi-Turn Dialogues with Diverse Jailbreak Attacks; abstract-level contribution review remains pending. | formal-venue |
| German2026TabMiaBenchmark | [Tab-MIA: A Benchmark Dataset for Membership Inference Attacks on Tabular Data in LLMs](<https://openreview.net/forum?id=ioYdy7aghG>) | 2026 | ICLR / accepted-program | Security Benchmarks And Evaluation | Benchmarks or evaluates tab-MIA: A Benchmark Dataset for Membership Inference Attacks on Tabular Data in LLMs; abstract-level contribution review remains pending. | formal-venue |
| HUANG2026GuidedbenchMeasuringMitigating | [GuidedBench: Measuring and Mitigating the Evaluation Discrepancies of In-the-wild LLM Jailbreak Methods](<https://openreview.net/forum?id=ZVg8y3ibyM>) | 2026 | ICLR / accepted-program | Security Benchmarks And Evaluation | Benchmarks or evaluates guidedBench: Measuring and Mitigating the Evaluation Discrepancies of In-the-wild LLM Jailbreak Methods; abstract-level contribution review remains pending. | formal-venue |
| Marek2026BenchmarkingEmpiricalPrivacy | [Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models](<https://openreview.net/forum?id=jY7fAo9rfK>) | 2026 | ICLR / accepted-program | Security Benchmarks And Evaluation | Benchmarks or evaluates benchmarking Empirical Privacy Protection for Adaptations of Large Language Models; abstract-level contribution review remains pending. | formal-venue |
| Shen2026MeasuringPhysicalWorld | [Measuring Physical-World Privacy Awareness of Large Language Models: An Evaluation Benchmark](<https://openreview.net/forum?id=WSpDZVEGNi>) | 2026 | ICLR / accepted-program | Security Benchmarks And Evaluation | Benchmarks or evaluates measuring Physical-World Privacy Awareness of Large Language Models: An Evaluation Benchmark; abstract-level contribution review remains pending. | formal-venue |
| Wang2026CognitionFromEvaluation | [COGNITION: From Evaluation to Defense against Multimodal LLM CAPTCHA Solvers](<https://www.usenix.org/conference/usenixsecurity26/presentation/wang-junyu>) | 2026 | USENIX Security / proceedings | Security Benchmarks And Evaluation | Benchmarks or evaluates cOGNITION: From Evaluation to Defense against Multimodal LLM CAPTCHA Solvers; abstract-level contribution review remains pending. | formal-venue |
| Yuan2026TowardsSecureLogging | [Towards Secure Logging: Characterizing and Benchmarking Logging Code Security Issues with LLMs](<https://conf.researchr.org/track/fse-2026/fse-2026-research-papers#event-3a94c929-baf0-41e2-8e83-0dd71c724b2f>) | 2026 | FSE/PACMSE / accepted-program | Security Benchmarks And Evaluation | Introduces or evaluates towards Secure Logging: Characterizing and Benchmarking Logging Code Security Issues with LLMs; abstract-level contribution review remains pending. | formal-venue |
| normalization2026MultibreakScalableDiverse | [MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark for Evaluating LLM Safety](<https://icml.cc/virtual/2026/poster/63523>) | 2026 | ICML / accepted-program | Security Benchmarks And Evaluation | Benchmarks or evaluates multiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark for Evaluating LLM Safety; abstract-level contribution review remains pending. | formal-venue |

### Frontier Preprints

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Hu2026CogateConfidenceGated | [CoGate: Confidence-Gated Co-Decoding for Secure Code Generation](<https://arxiv.org/abs/2607.28529>) | 2026 | arXiv / frontier-preprint | Security Benchmarks And Evaluation | To address the challenge, we propose CoGate, a confidence-gated co-decoding approach that controls the expert's influence on the co-decoding process based on its confidence. | frontier-preprint |
| Keppler2026CybercertbenchEvaluatingLlms | [CyberCertBench: Evaluating LLMs in Cybersecurity Certification Knowledge](<https://arxiv.org/abs/2604.20389>) | 2026 | arXiv / frontier-preprint | Security Benchmarks And Evaluation | Concurrently, we propose and validate a novel Proposer-Verifier framework, a methodology to generate interpretable,natural language explanations for model performance. | frontier-preprint |
| Rezakhani2026SafetuneMitigatingData | [SafeTune: Mitigating Data Poisoning in LLM Fine-Tuning for RTL Code Generation](<https://arxiv.org/abs/2604.27238>) | 2026 | arXiv / frontier-preprint | Security Benchmarks And Evaluation | To address this, we present SafeTune, a framework designed to harden LLM-based RTL generation against poisoning, specifically focusing on hardware Trojan (HT) insertion. | frontier-preprint |
| Yin2026CompilingActivationSteering | [Compiling Activation Steering into Weights via Null-Space Constraints for Stealthy Backdoors](<https://arxiv.org/abs/2604.12359>) | 2026 | arXiv / frontier-preprint | Security Benchmarks And Evaluation | Across multiple safety-aligned LLMs and jailbreak benchmarks, our method achieves high triggered attack success while maintaining non-triggered safety and general utility. | frontier-preprint |
| Zhang2026BurnAfterUse | [Burn-After-Use for Preventing Data Leakage through a Secure Multi-Tenant Architecture in Enterprise LLM](<https://arxiv.org/abs/2601.06627>) | 2026 | arXiv / frontier-preprint | Security Benchmarks And Evaluation | This study presents a Secure Multi-Tenant Architecture (SMTA) combined with a novel concept Burn-After-Use (BAU) mechanism for enterprise LLM environments to effectively prevent data…. | frontier-preprint |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
