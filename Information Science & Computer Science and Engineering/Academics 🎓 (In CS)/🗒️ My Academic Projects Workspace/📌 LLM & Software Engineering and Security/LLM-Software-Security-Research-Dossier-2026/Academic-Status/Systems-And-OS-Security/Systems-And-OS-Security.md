---
ai-generated: true
last-reviewed: 2026-07-30
---

# Systems And OS Security

Back: [Academic Status](../Academic-Status.md)

Scope: LLM-assisted kernel, driver, firmware, embedded-device, OS-configuration, patching, isolation, TEE, and runtime-security work. Generic systems-for-LLM performance work is out of scope unless it establishes a security boundary or checks a security property.

Checked: 2026-07-30. The explicit OS venue sweep follows the local venue guide: OSDI, SOSP, EuroSys, USENIX ATC, and FAST, with ASPLOS used as an adjacent architecture venue. Direct matches remain sparse: KNighter (SOSP 2025) is the direct match and KernelGPT (ASPLOS 2025) is an adjacent-venue match; OSDI, EuroSys, USENIX ATC, and FAST produced no direct canonical match in the current sweep. This is a coverage result, not evidence that OS security is unimportant.

## Kernel, Driver, Firmware, And Embedded Systems

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Zhou2024LLMIF | [LLMIF: Augmented Large Language Model for Fuzzing IoT Devices](https://dblp.org/rec/conf/sp/WangYL24) | 2024 | IEEE S&P / DBLP | IoT fuzzing | Adds semantic guidance to black-box IoT-device fuzzing. | Core |
| Asmita2024BusyBox | [Fuzzing BusyBox: Leveraging LLM and Crash Reuse for Embedded Bug Unearthing](https://dblp.org/rec/conf/uss/AsmitaOSTFH24) | 2024 | USENIX Security / DBLP | Embedded fuzzing | Combines model guidance with crash reuse for BusyBox. | Core |
| Ma2024MatterFuzzing | [From One Thousand Pages of Specification to Unveiling Hidden Bugs: Large Language Model Assisted Fuzzing of Matter IoT Devices](https://dblp.org/rec/conf/uss/MaL024) | 2024 | USENIX Security / DBLP | IoT protocol fuzzing | Converts a large device specification into executable fuzzing guidance. | Core |
| Yang2025KernelGPT | [KernelGPT: Enhanced Kernel Fuzzing via Large Language Models](https://doi.org/10.1145/3676641.3716022) | 2025 | ASPLOS | Kernel fuzzing | Generates kernel specifications and programs to expand syscall coverage. | Core |
| Zhang2025KernelRAG | [Unlocking Low Frequency Syscalls in Kernel Fuzzing with Dependency-Based RAG](https://dblp.org/rec/journals/pacmse/ZhangLLC25) | 2025 | FSE/PACMSE / DBLP | Kernel fuzzing | Retrieves syscall dependencies to reach low-frequency kernel behavior. | Core |
| Jia2026PANGOLIN | [PANGOLIN: Fuzzing Multilingual IoT Firmware with LLM-Driven Code Analysis](https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers) | 2026 | USENIX Security | Firmware fuzzing | Connects native and scripting-language logic in IoT firmware. | Accepted/program record |
| Ji2026FirmAgent | [FirmAgent: Leveraging Fuzzing to Assist LLM Agents with IoT Firmware Vulnerability Discovery](https://dblp.org/rec/conf/ndss/JiZGJLLZJ26) | 2026 | NDSS / DBLP | Firmware analysis | Grounds agentic firmware reasoning with fuzzing evidence. | Core |
| Yang2026BSFuzzer | [BSFuzzer: Context-Aware Semantic Fuzzing for BLE Logic Flaw Detection](https://www.ndss-symposium.org/ndss-paper/bsfuzzer-context-aware-semantic-fuzzing-for-ble-logic-flaw-detection/) | 2026 | NDSS | BLE/device fuzzing | Interprets BLE specifications and validates device responses. | Core |
| Liu2026IoTBec | [IoTBec: Firmware- and Source-Code-Independent Recurring Vulnerability Detection with LLM-Driven Fuzzing](https://www.ndss-symposium.org/ndss-program/symposium-2026/) | 2026 | NDSS | Black-box IoT fuzzing | Detects recurring device vulnerabilities without firmware or source. | Core |
| Zhang2026LogicFuzz | [LogicFuzz: An LLM-Driven Fuzzing Framework for Detecting Logic Instruction Bugs in PLCs](https://dblp.org/rec/conf/ndss/ChengZWCWQS26) | 2026 | NDSS / DBLP | Industrial control | Uses semantic fuzzing to find PLC logic-instruction bugs. | Core |
| Zou2026StepStone | [StepStone: LLM-Based GPU Kernel Driver Fuzzing via User-Space Libraries](https://doi.org/10.1109/SP63933.2026.00124) | 2026 | IEEE S&P | GPU driver fuzzing | Bridges user-space libraries to construct semantically meaningful kernel-driver workloads. | Core |
| Lin2026BugAuditor | [BugAuditor: Detecting Bugs via Inconsistent Defensive Code Auditing](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) | 2026 | USENIX Security | Kernel bug detection | Audits inconsistencies in defensive code, including Linux-kernel patterns. | Accepted/program record |
| Dong2026REDOSPECTOR | [Death by a Thousand Drips: Uncovering Critical Resource Leaks in the Windows Ecosystem](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) | 2026 | USENIX Security | Windows service fuzzing | Combines binary telemetry, amplification oracles, static analysis, and LLM-assisted seed generation. | Accepted/program record |

## OS Configuration, Hardening, And Patching

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Liu2025PatchScope | [PatchScope: LLM-Enhanced Fine-Grained Stable Patch Classification for Linux Kernel](https://dblp.org/rec/journals/pacmse/LiuSLHLSWSJ25) | 2025 | FSE/PACMSE / DBLP | Kernel patch classification | Classifies stable kernel patches at fine granularity. | Core |
| 2606.05476 | [SHIELDS: Automating OS Hardening with Iterative Multi-Agent Remediation](https://arxiv.org/abs/2606.05476) | 2026 | arXiv | OS hardening | Applies multi-agent remediation to STIG-style configuration baselines. | Frontier |

PatchWeaver’s canonical row is in [Security Repair And Patch Validation](../Vulnerability-Lifecycle/Security-Repair-And-Patch-Validation.md) because policy-bounded remediation is its main contribution.

## Isolation, TEE, And Capability-Controlled Runtimes

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Zhang2025IsolateGPT | [IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems](https://www.ndss-symposium.org/wp-content/uploads/2025-1131-paper.pdf) | 2025 | NDSS | Agent isolation | Applies systems isolation to tool-using LLM agents. | Core |
| Gadey2026TEEAnnotations | [Automated Code Annotation with LLMs for Establishing TEE Boundaries](https://dblp.org/rec/conf/ndss/GadeyGSSD26) | 2026 | NDSS / DBLP | TEE boundary tooling | Uses LLM assistance to identify and annotate trusted boundaries. | Core |
| Peng2026Kintsugi | [Kintsugi: Empowering LLMs to Mitigate Web Vulnerabilities via Runtime Policy Injection](https://www.usenix.org/conference/usenixsecurity26/presentation/peng-yihao) | 2026 | USENIX Security | Runtime containment | Injects runtime policies to mitigate web vulnerabilities without relying only on source repair. | Accepted/program record |
| 2606.03895 | [Agent libOS: A Library-OS-Inspired Runtime for Long-Running, Capability-Controlled LLM Agents](https://arxiv.org/abs/2606.03895) | 2026 | arXiv | Agent runtime | Applies library-OS ideas to capability-controlled long-running agents. | Frontier |

## OS Cross-Tags

- `Yang2025KNighter` is canonically filed under [Program Analysis](../Security-Analysis/Program-Analysis.md) because its main contribution is LLM-synthesized static checkers; Linux-kernel evaluation makes it the strongest SOSP cross-tag.
- Device/protocol fuzzing remains a child method in [Program Analysis](../Security-Analysis/Program-Analysis.md); this page is its system/domain view.
- Generic serving throughput, scheduling, kernel optimization, and systems-for-LLM papers stay outside this security dossier.

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Frontier Preprints

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Chen2026IterinjectIndirectPrompt | [IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization](<https://arxiv.org/abs/2605.24659>) | 2026 | arXiv / frontier-preprint | Systems And OS Security | Introduce \oursys, a feedback-guided iterative framework that closes the loop between injection, diagnosis, and refinement: a rule-based diagnoser produces structured outcome labels with behavioral…. | frontier-preprint |
| Gong2026LocalalignEnablingGeneralizable | [LocalAlign: Enabling Generalizable Prompt Injection Defense via Generation of Near-Target Adversarial Examples for Alignment Training](<https://arxiv.org/abs/2605.01462>) | 2026 | arXiv / frontier-preprint | Systems And OS Security | To address this challenge, we propose LocalAlign, a more generalizable prompt injection defense inspired by adversarial training. | frontier-preprint |
| He2026DefendingAgainstAdaptive | [Defending against Adaptive Prompt Injection Attacks via Reasoning-enabled Task Alignment](<https://arxiv.org/abs/2606.15441>) | 2026 | arXiv / frontier-preprint | Systems And OS Security | To address these gaps, we propose RETA, a training-based method that grounds defense decisions on the user tasks rather than attacker-controlled data. | frontier-preprint |
| Li2026LlmAsReviewer | [LLM-as-a-Reviewer: Benchmarking Their Ability, Divergence, and Prompt Injection Resistance as Paper Reviewers](<https://arxiv.org/abs/2605.25415>) | 2026 | arXiv / frontier-preprint | Systems And OS Security | Present a systematic benchmark of LLM-as-a-Reviewer on 898 papers stratified from NeurIPS and ICLR, evaluating 12 LLMs along three axes: rating calibration, divergence from…. | frontier-preprint |
| MayoralVilches2026CybersecurityAiGame | [Cybersecurity AI: A Game-Theoretic AI for Guiding Attack and Defense](<https://arxiv.org/abs/2601.05887>) | 2026 | arXiv / frontier-preprint | Systems And OS Security | Present Generative Cut-the-Rope (G-CTR), a game-theoretic guidance layer that extracts attack graphs from agent's context, computes Nash equilibria with effort-aware scoring, and feeds a…. | frontier-preprint |
| Pirch2026TowardSecuringAi | [Toward Securing AI Agents Like Operating Systems](<https://arxiv.org/abs/2605.14932>) | 2026 | arXiv / frontier-preprint | Systems And OS Security | Investigate the security of LLM-based agents through the lens of operating systems. | frontier-preprint |
| Sygletos2026KernelBasedRelu | [Kernel-Based ReLU Approximation for Homomorphic Encryption-Compatible Privacy-preserving Deep Learning Models](<https://arxiv.org/abs/2605.23641>) | 2026 | arXiv / frontier-preprint | Systems And OS Security | This paper proposes a kernel-based approximation of ReLU, enabling its use within HE-constrained settings and thus contributing a critical step toward supporting privacy-preserving LLMs. | frontier-preprint |
| Yang2026DeviceContextProtocol | [Device Context Protocol: A Compact, Safety-First Architecture for LLM-Driven Control of Constrained Devices](<https://arxiv.org/abs/2605.26159>) | 2026 | arXiv / frontier-preprint | Systems And OS Security | Present the Device Context Protocol (DCP): a sub-50-byte typical frame (6-byte header + CBOR payload + optional 16-byte HMAC), a manifest schema in which…. | frontier-preprint |
| Zhao2026AgenticosIntentOriented | [AgenticOS: An Intent-Oriented Secure Operating System Architecture for Autonomous AI Agents](<https://arxiv.org/abs/2606.21129>) | 2026 | arXiv / frontier-preprint | Systems And OS Security | To address this, we propose AgenticOS, an intent-oriented secure OS architecture that consolidates delegable, auditable software capabilities into OS-native ones rather than replacing all…. | frontier-preprint |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
