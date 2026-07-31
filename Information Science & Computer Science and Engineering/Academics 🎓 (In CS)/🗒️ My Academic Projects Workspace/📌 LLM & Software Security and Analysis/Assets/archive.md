---
archived: true
last-reviewed: 2026-07-30
---

# LLM + Software Security and Analysis Literature Sweep

> [!warning] Archived source sweep
> This June 2026 snapshot is retained for provenance and is not the current classification. Use the maintained [software-security dossier](../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md) and [general software dossier](../LLM-Software-Research-Dossier-2026/LLM-Software-Research-Dossier-2026.md). Generic software-engineering papers were moved to the latter; fuzzing is classified beneath security program analysis in the former.

Date: 2026-06-06

Scope: latest work on LLMs for code, software engineering, program analysis, penetration testing, CTF/cyber benchmarks, vulnerability detection, vulnerability exploration, repair, and end-to-end security workflows. Priority was given to top security venues: USENIX Security, IEEE S&P, ACM CCS, NDSS. Secondary sources were major SE/PL/AI venues and arXiv/OpenReview for fast-moving work.

This is a research-level map, not an operational exploitation guide.

## Search Taxonomy From The Local Note

- LLM architecture and attention: especially attention behavior that affects vulnerability auditing, long context, code attention, and MoE/security behavior.
- LLM utilization: agents, loop design, orchestration, prompt/context/harness engineering, reasoning and acting, skills/tool use.
- LLM for SE: code generation, issue repair, repository-level coding agents, secure code generation.
- LLM for PL/program analysis: static analysis, taint analysis, symbolic execution, fuzzing, decompilation, code property graphs.
- LLM for CTF/pentesting: CTF benchmarks, autonomous pentesting systems, cyber skill benchmarks.
- LLM for vulnerabilities: detection, localization, triage, exploration, exploitability reasoning, PoC generation, patching.
- End-to-end security delivery: agentic cyber reasoning systems, AIxCC-style pipelines, SOC/vulnerability management, secure deployment of LLM-integrated apps.

## High-Confidence Core Papers

### Top Security Venues

| Area                               | Paper                                                                                                                                                                                         |                 Venue / Year | Main Signal                                                                                                                                         |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Automated pentesting               | [PentestGPT: Evaluating and Harnessing Large Language Models for Automated Penetration Testing](https://www.usenix.org/conference/usenixsecurity24/presentation/deng)                         |         USENIX Security 2024 | Modular LLM pentesting framework; reports 228.6% task-completion increase over GPT-3.5 baseline on its benchmark targets.                           |
| LLM code analysis reliability      | [LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?)](https://arxiv.org/abs/2312.12575)                                                                            |                IEEE S&P 2024 | Important negative result: LLMs struggle as general-purpose vulnerability reasoners.                                                                |
| Vulnerability repair               | [Examining Zero-Shot Vulnerability Repair with Large Language Models](https://sp2024.ieee-security.org/program-papers.html)                                                                   |                IEEE S&P 2024 | Early rigorous look at zero-shot repair limits.                                                                                                     |
| Code model poisoning/backdoors     | [An LLM-Assisted Easy-to-Trigger Backdoor Attack on Code Completion Models](https://www.usenix.org/conference/usenixsecurity24/presentation/yan)                                              |         USENIX Security 2024 | LLM-assisted payload transformation can hide injected vulnerabilities in code-completion models.                                                    |
| Secure code generation             | [PromSec: Prompt Optimization for Secure Generation of Functional Source Code with LLMs](https://www.sigsac.org/ccs/CCS2024/program/accepted-papers.html)                                     |                     CCS 2024 | Prompt optimization for improving security of generated code.                                                                                       |
| Fuzzing with LLMs                  | [LIFTFUZZ: Validating Binary Lifters through Context-aware Fuzzing with GPT](https://www.sigsac.org/ccs/CCS2024/program/accepted-papers.html)                                                 |                     CCS 2024 | LLM-assisted/context-aware fuzzing for binary lifter validation.                                                                                    |
| Fuzzing with documentation         | [ProphetFuzz: Fully Automated Prediction and Fuzzing of High-Risk Option Combinations with Only Documentation via LLM](https://www.sigsac.org/ccs/CCS2024/program/accepted-papers.html)       |                     CCS 2024 | Uses documentation and LLMs to infer risky option combinations for fuzzing.                                                                         |
| LLM-integrated app security        | [Demystifying RCE Vulnerabilities in LLM-Integrated Apps](https://lyutoon.github.io/papers/LLMSmith-CCS.pdf)                                                                                  |                     CCS 2024 | Shows RCE/arbitrary file risks in LLM apps, a core end-to-end security-delivery topic.                                                              |
| Vulnerability detection            | [LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided LLMs](https://www.usenix.org/conference/usenixsecurity25/presentation/lekssays)                            |         USENIX Security 2025 | CPG slicing reduces input size and improves robustness; reports 15-40% F1 improvements over baselines.                                              |
| Vulnerability patching             | [APPATCH: Automated Adaptive Prompting LLMs for Real-World Software Vulnerability Patching](https://www.usenix.org/conference/usenixsecurity25/presentation/nong)                             |         USENIX Security 2025 | Adaptive prompting and vulnerability-semantics reasoning for patching real-world vulnerabilities.                                                   |
| Vulnerability patching             | [Logs In, Patches Out: Automated Vulnerability Repair via Tree-of-Thought LLM Analysis](https://www.usenix.org/conference/usenixsecurity25/presentation/kim-youngjoon)                        |         USENIX Security 2025 | Uses sanitizer logs and source code; reports 79.5% patch success on VulnLoc.                                                                        |
| Supply-chain risk from code LLMs   | [We Have a Package for You! Package Hallucinations by Code Generating LLMs](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen)                                        |         USENIX Security 2025 | Large-scale study of hallucinated packages as package-confusion attack surface.                                                                     |
| Code-auditor evasion               | [Flashboom: Blinding LLM-Based Code Auditors](https://cs.nju.edu.cn/fxu/static/papers/featured/flashboom-sp2025.pdf)                                                                          |                IEEE S&P 2025 | Attention-diversion attack against LLM code auditors; reports high blinding success on evaluated models.                                            |
| Vulnerability-reasoning benchmark  | [SV-TrustEval-C](https://arxiv.org/abs/2505.20630)                                                                                                                                            |                IEEE S&P 2025 | Benchmark for structure and semantic reasoning in C vulnerability analysis; finds pattern-matching over robust reasoning.                           |
| Cybersecurity-role evaluation      | [The Digital Cybersecurity Expert: How Far Have We Come?](https://arxiv.org/abs/2504.11783)                                                                                                   |                IEEE S&P 2025 | Fine-grained cybersecurity knowledge benchmark and role alignment analysis.                                                                         |
| LLM app/agent isolation            | [IsolateGPT](https://www.ndss-symposium.org/ndss-program/symposium-2025/)                                                                                                                     |                    NDSS 2025 | Execution isolation architecture for LLM-based agentic systems.                                                                                     |
| Shell-command analysis             | [RACONTEUR](https://www.ndss-symposium.org/ndss-program/symposium-2025/)                                                                                                                      |                    NDSS 2025 | LLM-powered shell command explainer for analysts.                                                                                                   |
| Vulnerability detection evaluation | [From Large to Mammoth](https://www.ndss-symposium.org/ndss-paper/from-large-to-mammoth-a-comparative-evaluation-of-large-language-models-in-vulnerability-detection/)                        |                    NDSS 2025 | Broad comparison of LLMs for vulnerability detection; finds strong dependence on language, model, context window, quantization, and prompting mode. |
| Protocol fuzzing                   | [Large Language Model Guided Protocol Fuzzing](https://www.ndss-symposium.org/wp-content/uploads/2024-556-paper.pdf)                                                                          |                    NDSS 2024 | LLMs help infer protocol semantics and guide fuzzing.                                                                                               |
| Firmware vulnerability discovery   | [FirmAgent: Leveraging Fuzzing to Assist LLM Agents with IoT Firmware Vulnerability Discovery](https://www.ndss-symposium.org/wp-content/uploads/2026-s1943-paper.pdf)                        |                    NDSS 2026 | Hybrid fuzzing plus LLM taint/path reasoning; reports 182 vulnerabilities, 140 previously unknown, 17 CVEs.                                         |
| BLE fuzzing                        | [BSFuzzer: Context-Aware Semantic Fuzzing for BLE Logic Flaw Detection](https://www.ndss-symposium.org/ndss-paper/bsfuzzer-context-aware-semantic-fuzzing-for-ble-logic-flaw-detection/)      |                    NDSS 2026 | LLM agent parses Bluetooth specs, generates semantic mutations, validates responses; reports 36 issues, 34 new bugs, 9 CVEs.                        |
| LLM static-analysis attack         | [Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias](https://www.ndss-symposium.org/ndss-paper/trust-me-i-know-this-function-hijacking-llm-static-analysis-using-bias/) |                    NDSS 2026 | Identifies abstraction bias causing LLM static analysis to miss small meaningful bugs.                                                              |
| Multilingual IoT fuzzing           | [PANGOLIN: Fuzzing Multilingual IoT Firmware with LLM-Driven Code Analysis](https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_jia.pdf)                             | USENIX Security 2026 Cycle 1 | LLMs extract cross-language interfaces/specs; reports 68 zero-day vulnerabilities and 31 assigned IDs.                                              |
| Agent DoS                          | [Autonomy Comes with Costs: Detecting DoS Vulnerabilities in LLM-based Agents](https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_luo.pdf)                          | USENIX Security 2026 Cycle 1 | Resource-lifecycle-guided fuzzing of LLM agents; reports 36 zero-days across 16 agents and 15 CVEs.                                                 |
| Private code generation            | [NOIR: Privacy-Preserving Generation of Code with Open-Source LLMs](https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers)                                                | USENIX Security 2026 Cycle 1 | Protects client prompts/generated code from the cloud via embedding/tokenization privacy mechanisms.                                                |

### SE / PL / AI Venue And arXiv Core

| Area | Paper | Venue / Year | Main Signal |
|---|---|---:|---|
| Real-world SE benchmark | [SWE-bench](https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html) | ICLR 2024 | 2,294 GitHub issue/PR tasks; initial best model solved only 1.96%, establishing repo-level SE as hard. |
| Agentic SE | [SWE-agent](https://openreview.net/forum?id=mXpq6ut8J3) | NeurIPS 2024 | Agent-computer interfaces strongly improve repository editing/test execution. |
| Static analysis | [IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities](https://openreview.net/forum?id=9LdJDU7E91) | ICLR 2025 | Neuro-symbolic whole-repository vulnerability detection; LLMs infer taint specs and contextual analysis. |
| Binary taint analysis | [LATTE: LLM-Powered Static Binary Taint Analysis](https://dl.acm.org/doi/10.1145/3711816) | TOSEM 2025 | LLM-assisted binary taint analysis; automates rules that previously needed expert customization. |
| Hybrid fuzzing | [Large Language Model Assisted Hybrid Fuzzing](https://arxiv.org/abs/2412.15931) | arXiv 2024 | Uses LLM as a solver for input modifications when fuzzing reaches coverage roadblocks. |
| Cyber benchmark | [Cybench](https://arxiv.org/abs/2408.08926) | arXiv 2024 | CTF/cyber benchmark for LLM agents; useful for CTF/pentest capability measurement. |
| Secure-code benchmark | [SafeGenBench](https://arxiv.org/abs/2506.05692) | arXiv 2025 | Benchmark framework for vulnerability detection in LLM-generated code. |
| Smart-contract analysis | [CKG-LLM](https://arxiv.org/abs/2512.06846) | arXiv 2025 | Converts natural-language vulnerability patterns into executable knowledge-graph queries. |
| PoC generation | [A Systematic Study on Generating Web Vulnerability PoCs Using LLMs](https://arxiv.org/abs/2510.10148) | arXiv 2025 | Studies LLM PoC generation over disclosure stages; highly relevant but dual-use sensitive. |
| Robustness of secure generation | [How Secure is Secure Code Generation?](https://arxiv.org/abs/2601.07084) | arXiv 2026 | Adversarial prompts expose robustness gaps in secure-code-generation defenses. |
| Detector evasion | [Syntax- and Compilation-Preserving Evasion of LLM Vulnerability Detectors](https://arxiv.org/abs/2602.00305) | arXiv 2026 | Shows syntax/compilation-preserving edits can evade LLM vulnerability detectors. |

### Surveys And Framing Papers

- [LLMs in Software Security: A Survey of Vulnerability Detection Techniques and Insights](https://doi.org/10.48550/arXiv.2502.07049), already in the local note.
- [When Software Security Meets Large Language Models: A Survey](https://doi.org/10.1109/JAS.2024.124971), already in the local note.
- [Large Language Model Supply Chain: A Research Agenda](https://doi.org/10.1145/3708531), TOSEM 2025.

## Current Development Status

### 1. Pure prompting is no longer the serious baseline

The strongest 2025-2026 systems increasingly combine LLMs with concrete program artifacts: CPGs, taint flows, sanitizer logs, fuzzing traces, API specifications, protocol documents, execution feedback, and tests. LLMxCPG, IRIS, LATTE, FirmAgent, PANGOLIN, BSFuzzer, and HyLLfuzz all point in the same direction: LLMs are useful as semantic components inside program-analysis systems, not as standalone oracles.

### 2. LLMs are useful for "semantic glue"

The recurring pattern is: traditional analysis handles sound-ish structure, and LLMs fill the semantic gaps that are expensive to manually specify. Examples:

- infer taint sources/sinks/specifications;
- interpret API/protocol documentation;
- summarize or rename decompiled/binary artifacts;
- generate or refine fuzzing inputs/drivers;
- explain shell commands or analyst artifacts;
- turn vulnerability patterns into structured queries.

This is a high-value research direction because it preserves engineering leverage while avoiding the weakest assumption: that an LLM alone can reason soundly over a large codebase.

### 3. Repository-level and whole-system reasoning remains hard

SWE-bench and IRIS both show the key bottleneck: real software tasks require multi-file context, build/test execution, issue interpretation, and state management. Vulnerability analysis is even harder because ground truth is sparse, labels are noisy, and a model must distinguish vulnerable, patched, unreachable, and functionally broken variants.

### 4. Security benchmarks are becoming more realistic

The field is moving from synthetic code snippets toward:

- real GitHub issue/PR tasks: SWE-bench;
- manually validated repository vulnerabilities: CWE-Bench-Java in IRIS;
- CTF/cyber tasks: Cybench;
- structure/semantic perturbation benchmarks: SV-TrustEval-C;
- real firmware/devices: FirmAgent, PANGOLIN, BSFuzzer;
- agent and app security: AgentDoS, IsolateGPT, LLMSmith.

This is good, but evaluation is still fragile: benchmark contamination, patch-equivalence ambiguity, exploitability validation, and generated-test quality remain major open problems.

### 5. The best vulnerability-discovery work is hybrid and evidence-driven

The newest top-venue papers do not just ask a model "is this vulnerable?" They build pipelines that collect evidence and use the LLM to reduce search space or reason over candidate paths. The most credible systems produce artifacts such as reachable paths, PoCs, sanitizer logs, validated patches, device responses, or CVEs.

### 6. LLM-based security tools create new attack surfaces

Important negative/attack results are now central:

- Flashboom and Trust Me show LLM code auditors can be biased or blinded.
- CodeBreaker shows code-completion models can be backdoored to emit disguised vulnerabilities.
- Package hallucination work shows generated code can create supply-chain attack opportunities.
- LLMSmith, IsolateGPT, and AgentDoS show LLM apps/agents inherit conventional software risks plus new natural-language/tool-use failure modes.

This means "LLM for security" and "security for LLM-based software" are now inseparable.

### 7. Patching is promising but still risky

APPATCH and SAN2PATCH show strong progress, especially when LLMs are guided by vulnerability semantics, sanitizer logs, and validation. The hard part is not producing a plausible patch; it is proving that the patch is correct, preserves behavior, addresses root cause, and does not introduce a new vulnerability. This makes patch validation and regression-test synthesis an important research gap.

### 8. Pentesting and CTF agents are improving, but orchestration matters more than raw model choice

PentestGPT and newer agentic security work suggest LLMs can help with tool use, output interpretation, next-action planning, and CTF-like workflows. The main bottlenecks are long-horizon memory, context loss, environment grounding, safe tool execution, and reliable stopping criteria. Multi-agent frameworks are promising but raise security/isolation issues.

## Research Gaps And Promising Directions

### A. LLM + program analysis with explicit guarantees

Most current systems are empirically strong but not sound. A strong research direction is to let LLMs propose hypotheses and let symbolic/static/dynamic analyses verify them. Examples:

- LLM proposes source/sink specs; static analysis verifies flows.
- LLM proposes path constraints or input mutations; fuzzing validates coverage/crashes.
- LLM translates vulnerability patterns; query engine executes and explains matches.
- LLM suggests patches; tests, sanitizer replay, differential execution, and static checks validate.

### B. Vulnerability reasoning benchmarks that test causality, not pattern matching

SV-TrustEval-C is a good start. More work is needed on benchmarks that include:

- paired vulnerable/patched/semantics-preserving variants;
- reachability and exploitability labels;
- multi-file and dependency-sensitive context;
- adversarial transformations that preserve behavior;
- role-specific metrics for security researcher, maintainer, SOC analyst, and attacker-model perspectives.

### C. Agentic cyber systems with secure execution boundaries

Future systems will combine LLM planning with shells, browsers, fuzzers, debuggers, static analyzers, package managers, and cloud APIs. The research problem is no longer only model accuracy; it is secure orchestration:

- permission models for tools;
- sandboxing and isolation;
- resource governance;
- audit trails;
- prompt/tool injection resistance;
- replayable evidence chains.

### D. LLMs for exploitability and vulnerability triage

There is room for work between "detect a bug" and "generate an exploit." Defensively useful questions include:

- Is the reported flow reachable?
- What preconditions are necessary?
- Which assets are affected?
- Is the vulnerability likely exploitable under standard mitigations?
- What temporary mitigation can block exploitation before patching?

This can be framed safely as exploitability assessment and mitigation prioritization rather than operational exploitation.

### E. Domain-specific targets are high-value

The strongest recent results often focus on specific domains: IoT firmware, BLE, web apps, Java APIs, binaries, smart contracts, shell commands, package ecosystems. This suggests a good PhD/research strategy: pick a domain where formal structure exists but expert annotations are expensive, then use LLMs to bridge that semantic gap.

## Suggested Reading Order

1. Surveys: arXiv 2502.07049 and JAS 2025 survey.
2. Negative baseline: S&P 2024 "LLMs Cannot Reliably..." and NDSS 2025 "From Large to Mammoth."
3. Program-analysis hybrids: IRIS, LATTE, LLMxCPG, HyLLfuzz.
4. Fuzzing/vulnerability discovery: LLM-guided protocol fuzzing, FirmAgent, BSFuzzer, PANGOLIN.
5. Patching: APPATCH, SAN2PATCH, S&P 2024 zero-shot repair.
6. Agents/pentest/CTF: PentestGPT, SWE-agent, Cybench, AgentDoS, IsolateGPT.
7. Failure/attack surfaces: Flashboom, Trust Me, CodeBreaker, package hallucinations, LLMSmith.

## Concise Research Thesis

The field is shifting from "Can LLMs find bugs?" to "How do we build verified, evidence-producing cyber reasoning systems where LLMs supply semantic inference inside a secure program-analysis loop?" The strongest work in 2025-2026 is hybrid, domain-specific, and validation-heavy. The biggest open problems are trustworthy evaluation, whole-repository reasoning, exploitability assessment, secure agent orchestration, and robust patch validation.

## Round 2: Expanded Citation Map

This second pass expands the first paper set with a stricter cluster view. The most important update is that 2026 work is now strongly centered on agentic program analysis: LLMs are connected to fuzzers, concolic execution, CodeQL/static analysis, backporting tools, compilers, runtime feedback, and cyber-reasoning-system orchestration.

### 1. Top-Venue Additions By Cluster

| Cluster                       | Paper                                                                                                                                                                                                                                          |         Venue / Year | Why It Matters                                                                                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Vulnerability management      | [Exploring ChatGPT's Capabilities on Vulnerability Management](https://www.usenix.org/conference/usenixsecurity24/presentation/liu-peiyu)                                                                                                      | USENIX Security 2024 | Evaluates six vulnerability-management tasks on 70k+ samples; useful baseline for triage, patch correctness, security relevance, and report processing. |
| Code analysis evaluation      | [Large Language Models for Code Analysis: Do LLMs Really Do Their Job?](https://www.usenix.org/conference/usenixsecurity24/presentation/fang)                                                                                                  | USENIX Security 2024 | Evaluates LLM code-analysis ability, including obfuscated code; important for reverse-engineering and auditor-assistant claims.                         |
| IoT fuzzing                   | [LLMIF: Augmented Large Language Model for Fuzzing IoT Devices](https://sp2024.ieee-security.org/accepted-papers.html)                                                                                                                         |        IEEE S&P 2024 | Early top-venue LLM-assisted IoT fuzzing paper; bridges documentation/semantics and device testing.                                                     |
| Secure patch migration        | [PORTGPT: Towards Automated Backporting Using Large Language Models](https://arxiv.org/abs/2510.22396)                                                                                                                                         |        IEEE S&P 2026 | LLM-agent for security patch backporting; combines code access, Git history, compiler feedback, and iterative repair.                                   |
| Concolic execution            | [ConcoLLMic: Agentic Concolic Execution](https://concollmic.github.io/)                                                                                                                                                                        |        IEEE S&P 2026 | LLM-agent concolic testing that aims to reduce environment-modeling burden and support multi-language workflows.                                        |
| CLI fuzzing                   | [PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting](https://sp2026.ieee-security.org/accepted-papers.html)                                                                                       |        IEEE S&P 2026 | Uses call-path context and iterative feedback to generate CLI options and input files; reports many zero-day findings in preprint summaries.            |
| Java vuln discovery           | [Contextualizing Sink Knowledge for Java Vulnerability Discovery](https://arxiv.org/abs/2604.01645)                                                                                                                                            |        IEEE S&P 2026 | GONDAR uses sink semantics, LLM-assisted filtering, and fuzzer feedback for reachability/exploitability-aware Java vulnerability discovery.             |
| Rust memory safety            | [deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses](https://arxiv.org/abs/2506.15648)                                                                                                          |        IEEE S&P 2026 | Static analysis plus LLM-augmented harness generation for unsafe Rust; strong example of LLMs handling type/generic/trait complexity.                   |
| CTF agents                    | [Measuring and Augmenting Large Language Models for Solving Capture-the-Flag Challenges](https://arxiv.org/abs/2506.17644)                                                                                                                     |             CCS 2025 | Introduces CTFKnow and CTFAgent; distinguishes knowledge, reasoning, and environment interaction.                                                       |
| Fuzz harness generation       | [PromeFuzz: A Knowledge-Driven Approach to Fuzzing Harness Generation with Large Language Models](https://dblp.org/db/conf/ccs/ccs2025.html)                                                                                                   |             CCS 2025 | LLM-assisted fuzzing harness generation; directly relevant to AIxCC-style automated vulnerability discovery.                                            |
| Secure RAG code generation    | [Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection](https://arxiv.org/abs/2504.16429)                                                                                                          |             CCS 2025 | CodeGuarder retrieves both functional examples and security knowledge to harden RAG-based code generation, including poisoning scenarios.               |
| JS reverse engineering        | [JsDeObsBench: Measuring and Benchmarking LLMs for JavaScript Deobfuscation](https://arxiv.org/abs/2506.20170)                                                                                                                                 |             CCS 2025 | Benchmark for LLM-based JavaScript deobfuscation, useful for web malware and reverse-engineering workflows.                                             |
| Firmware discovery            | [FirmAgent](https://www.ndss-symposium.org/ndss-paper/firmagent-leveraging-fuzzing-to-assist-llm-agents-with-iot-firmware-vulnerability-discovery/)                                                                                            |            NDSS 2026 | Combines fuzzing-identified input-related code points with LLM static/path reasoning; one of the clearest hybrid templates.                             |
| Protocol/app fuzzing          | [ProtocolGuard](https://www.ndss-symposium.org/wp-content/uploads/2026-f521-paper.pdf)                                                                                                                                                         |            NDSS 2026 | LLM-guided static analysis plus fuzzing-based dynamic verification for protocol vulnerabilities.                                                        |
| PLC fuzzing                   | [LogicFuzz: An LLM-Driven Fuzzing Framework for Detecting Logic Instruction Bugs in PLCs](https://www.ndss-symposium.org/wp-content/uploads/2026-f1081-paper.pdf)                                                                              |            NDSS 2026 | Domain-specific industrial-control fuzzing using semantic dependency graphs and LLM-guided seed/program generation.                                     |
| Human-LLM reverse engineering | [Decompiling the Synergy: An Empirical Study of Human-LLM Teaming in Software Reverse Engineering](https://www.ndss-symposium.org/ndss-paper/decompiling-the-synergy-an-empirical-study-of-human-llm-teaming-in-software-reverse-engineering/) |            NDSS 2026 | Studies analyst plus LLM workflows for reverse engineering, not only fully autonomous tools.                                                            |
| Decompilation                 | [DeGPT: Optimizing Decompiler Output with LLM](https://www.ndss-symposium.org/ndss-paper/degpt-optimizing-decompiler-output-with-llm/)                                                                                                         |            NDSS 2026 | LLM post-processing of decompiler output; relevant to binary analysis, malware analysis, and vulnerability discovery.                                   |
| LLM-resistant protection      | [Towards LLM-Resistant Software Protection: Agent Failure Patterns in CTF Reverse Engineering](https://www.ndss-symposium.org/ndss-paper/auto-draft-657/)                                                                                      |        NDSS BAR 2026 | Analyzes where LLM agents fail in reverse-engineering CTF tasks; useful for capability boundaries and benchmark design.                                 |

### 2. Benchmarks And Evaluation Datasets

| Benchmark                      | Link                                                                                                                      | Main Use                                                                                                                                            |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| CyberSecEval 2                 | [arXiv:2404.13161](https://arxiv.org/abs/2404.13161)                                                                      | Broad LLM cyber-risk and capability evaluation, including prompt injection, code interpreter abuse, false refusals, and exploit-generation tasks.   |
| CyberSecEval 3                 | [arXiv:2408.01605](https://arxiv.org/abs/2408.01605)                                                                      | Expanded cybersecurity evaluation suite for LLM risks and capabilities.                                                                             |
| NYU CTF Bench                  | [arXiv:2406.05590](https://arxiv.org/abs/2406.05590)                                                                      | Open benchmark for LLM offensive-security/CTF capability.                                                                                           |
| Cybench                        | [arXiv:2408.08926](https://arxiv.org/abs/2408.08926)                                                                      | Professional-level CTF/cybersecurity task benchmark for agents.                                                                                     |
| CTFKnow / CTFAgent             | [arXiv:2506.17644](https://arxiv.org/abs/2506.17644)                                                                      | Separates CTF technical knowledge from environment-grounded task solving.                                                                           |
| SV-TrustEval-C                 | [arXiv:2505.20630](https://arxiv.org/abs/2505.20630)                                                                      | Source-code vulnerability reasoning benchmark focused on structure and semantics.                                                                   |
| SafeGenBench                   | [arXiv:2506.05692](https://arxiv.org/abs/2506.05692)                                                                      | Security vulnerability detection in LLM-generated code.                                                                                             |
| SeCodePLT                      | [arXiv:2410.11096](https://arxiv.org/abs/2410.11096)                                                                      | Unified evaluation platform for security of code GenAI; reports security relevance improvements over CyberSecEval-style tests.                      |
| SecureVibeBench                | [arXiv:2509.22097](https://arxiv.org/abs/2509.22097)                                                                      | Realistic multi-file secure coding tasks based on vulnerability-introducing scenarios; evaluates code agents using functional and security oracles. |
| ExploitBench                   | [arXiv:2605.14153](https://arxiv.org/abs/2605.14153)                                                                      | Capability-ladder benchmark for exploit agents, decomposing progress into measurable exploitation capabilities instead of binary crash success.     |
| SWE-bench / SWE-bench Verified | [SWE-bench](https://www.swebench.com/) / [OpenAI Verified note](https://openai.com/index/introducing-swe-bench-verified/) | Repository-level issue resolution; important adjacent benchmark for repair agents, but not security-specific.                                       |
| SWE-Bench+                     | [arXiv:2410.06992](https://arxiv.org/abs/2410.06992)                                                                      | Audits and improves SWE-bench-style evaluation quality; important warning for test-suite-based claims.                                              |

Evaluation trend: the serious benchmarks are moving from one-shot function classification toward multi-file repositories, real vulnerabilities, dynamic oracles, deterministic validators, CTF environments, and vulnerability-introducing histories. The key research question is no longer only "did the model output the right label?" but "can we verify that the agent reached, reproduced, fixed, or mitigated the vulnerability under a reproducible oracle?"

### 3. Method Patterns That Now Dominate

1. LLM as specification miner.
   Examples: LLMxCPG, IRIS, GONDAR, LogicFuzz, BSFuzzer, ProtocolGuard. The LLM extracts or contextualizes semantics from code, API docs, protocols, or vulnerability patterns.

2. LLM as harness/input generator.
   Examples: PromeFuzz, deepSURF, PILOT, HyLLfuzz, ProphetFuzz. The LLM creates structured inputs, valid harnesses, or option/file combinations that random mutation struggles to produce.

3. LLM as taint/sink/source assistant.
   Examples: IRIS, LATTE, GONDAR. The LLM helps infer security-sensitive APIs, sources, sinks, or propagation rules, while static analysis and fuzzing validate.

4. LLM as repair/backporting agent.
   Examples: APPATCH, SAN2PATCH, PORTGPT, SWE-agent/Agentless adjacent work. The main issue is validating correctness and non-regression, not patch synthesis itself.

5. LLM as reverse-engineering assistant.
   Examples: DeGPT, JsDeObsBench, Raconteur, human-LLM reverse-engineering studies. This is a promising but under-theorized area because analyst usefulness is not captured well by standard exact-match metrics.

6. LLM as cyber reasoning system component.
   Examples: ATLANTIS, OSS-CRS, FuzzingBrain, AIxCC systems. These combine many subsystems: fuzzing, static analysis, symbolic execution, LLM planning, patching, validation, and disclosure workflow.

### 4. AIxCC And End-to-End Security Delivery

AIxCC is now the strongest real-world signal for end-to-end LLM-assisted software security. DARPA reported that Team Atlanta won the 2025 final, and the competition showed cyber reasoning systems automatically finding and patching vulnerabilities in open-source software. The public writeups and preprints suggest the winning direction is not a pure LLM agent. It is a CRS pipeline that combines:

- fuzzing for concrete evidence;
- symbolic execution and directed analysis for path reasoning;
- static analysis for candidate discovery and pruning;
- LLMs for semantic interpretation, prioritization, triage, and patch generation;
- validation loops for reproducing crashes and checking patches;
- workflow support for disclosure and maintainer-facing reporting.

Key follow-up readings:

- [ATLANTIS: AI-driven Threat Localization, Analysis, and Triage Intelligence System](https://arxiv.org/abs/2509.14589)
- [OSS-CRS: Liberating AIxCC Cyber Reasoning Systems for Real-World Open-Source Security](https://arxiv.org/abs/2603.08566)
- [SoK: DARPA's AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned](https://arxiv.org/abs/2602.07666)
- [All You Need Is A Fuzzing Brain](https://arxiv.org/abs/2509.07225)
- [DARPA AIxCC results](https://www.darpa.mil/news/2025/aixcc-results)
- [OpenSSF CRS collaboration](https://openssf.org/tag/cyber-reasoning-systems/)

Research implication: end-to-end security delivery is becoming a systems problem. Good papers will likely need to show orchestration design, evidence quality, patch validation, responsible-disclosure handling, and maintainability, not just model accuracy.

### 5. What Seems Saturated

- Simple zero-shot "is this vulnerable?" classification on isolated functions.
- Prompt-only secure code generation without execution tests.
- LLM-as-a-judge evaluation without independent static/dynamic oracle.
- Small synthetic benchmarks where labels are obvious from CWE keywords.
- Claims of autonomous pentesting without environment control, logging, and reproducibility.

These topics can still be useful as baselines, but they are no longer enough for a strong top-security paper.

### 6. What Looks Promising

1. Verified semantic bridge for program analysis.
   Use LLMs to propose sources, sinks, path summaries, type constraints, protocol states, or harnesses; verify them with CodeQL, fuzzing, symbolic execution, sanitizers, or differential execution.

2. Vulnerability exploration after detection.
   Study the middle layer between a bug report and exploit generation: reachability, preconditions, affected configurations, mitigations, likely exploitability, and patch priority.

3. Patch validation beyond green tests.
   Combine generated regression tests, sanitizer replay, property checks, differential execution, static checks, and patch minimality. This is especially relevant after APPATCH, SAN2PATCH, PORTGPT, and AIxCC.

4. Domain-specific LLM-assisted analysis.
   Pick a domain with rich but hard-to-operationalize semantics: Java deserialization, unsafe Rust, IoT firmware, BLE/PLC protocols, JS malware, smart contracts, shell commands, or package ecosystems.

5. Secure orchestration of cyber agents.
   Study permission models, isolation, resource governance, prompt/tool injection, evidence trails, and failure recovery in LLM agents that run security tools.

6. Benchmark design for adversarial robustness.
   Build paired vulnerable/patched/semantics-preserving variants, benchmark contamination controls, multi-file contexts, and deterministic oracles for causality rather than pattern matching.

### 7. Research Direction Candidates

| Candidate Topic | Core Question | Why It Could Be Strong |
|---|---|---|
| LLM-verified sink exploration for Java/web apps | Can an agent move from candidate sink to reachable, validated vulnerability with fuzzer feedback? | Extends GONDAR/IRIS into practical exploitability triage without relying on pure model judgment. |
| LLM-assisted patch validation benchmark | Can we detect when a generated patch only hides the symptom or breaks intended behavior? | Patching is active, but validation is underdeveloped and very publishable. |
| Robust vulnerability detector under semantics-preserving transformations | Can detector results remain stable under realistic refactors/obfuscations? | Directly responds to Flashboom, Trust Me, and detector-evasion preprints. |
| Human-LLM reverse-engineering assistant evaluation | What workflows actually improve analyst speed/accuracy on binaries or obfuscated JS? | Topical after DeGPT, JsDeObsBench, and NDSS human-LLM SRE work; metrics are still immature. |
| Secure CRS orchestration layer | How should an AIxCC-style CRS manage permissions, evidence, tool calls, costs, and disclosure? | Moves from model-centric to systems-centric security research. |
| LLM-assisted fuzz harness synthesis for unsafe Rust or C++ libraries | Can LLMs generate type-correct, behaviorally meaningful harnesses that reach unsafe paths? | deepSURF/PromeFuzz show momentum; language-specific constraints are still hard. |
| RAG poisoning defenses for code-generation assistants | Can retrieval systems prevent vulnerable examples from steering generated code? | Strong link between software supply chain, code generation, and LLM app security. |

### 8. Updated Reading Priority

1. Read the negative and benchmark papers first: S&P 2024 "LLMs Cannot Reliably...", SV-TrustEval-C, From Large to Mammoth, SeCodePLT, SecureVibeBench, ExploitBench.
2. Then read the hybrid program-analysis papers: IRIS, LLMxCPG, LATTE, GONDAR, ConcoLLMic.
3. Then read fuzzing/harness papers: LLM-guided protocol fuzzing, PromeFuzz, deepSURF, PILOT, FirmAgent, BSFuzzer, PANGOLIN, LogicFuzz.
4. Then read repair and delivery: APPATCH, SAN2PATCH, PORTGPT, ATLANTIS, OSS-CRS, AIxCC SoK.
5. Finally read reverse engineering and agent security: DeGPT, JsDeObsBench, Raconteur, IsolateGPT, AgentDoS, PromptPeek, Flashboom, Trust Me.

### 9. Updated One-Sentence Thesis

The most promising research direction is not "LLM replaces program analysis", but "LLM supplies hard-to-manualize semantic hypotheses inside a verified cyber reasoning loop that produces reproducible evidence, validated patches, and auditable decisions."
