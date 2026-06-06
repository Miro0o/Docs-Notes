---
ai-generated: true
---

# Academic Status: LLMs For Software Security, Program Analysis, Fuzzing, And Cyber Reasoning

Date: 2026-06-06

Home: [LLM-Software-Security-Research-Dossier-2026.md](LLM-Software-Security-Research-Dossier-2026.md)

This file covers academic and research-status material: venue literature, preprints, benchmarks, method patterns, research gaps, promising directions, AIxCC-style systems, reading priority, and citation criteria.

## Inclusion Criteria And Confidence Labels

Included work is from 2024-present, as checked on 2026-06-06, and directly touches at least one of: LLMs for code/software engineering; program analysis; fuzzing; vulnerability detection/localization/triage/repair; reverse engineering; CTF/pentesting/cyber agents; cyber reasoning systems; or security of LLM-based coding/security tools.

Venue scope is now intentionally broader than the earlier security-focused sweep. Top security venues remain the primary source of truth, and related papers from top SE, PL, and AI venues are included when they match the dossier's research areas.

- Security primary: IEEE S&P, USENIX Security, ACM CCS, NDSS.
- SE: ICSE, FSE/PACMSE, ASE, ISSTA.
- PL: PLDI, POPL, OOPSLA through PACMPL.
- AI: NeurIPS, ICML, ICLR, AAAI.
- Frontier preprints: targeted 2026 arXiv sweep across `cs.CR`, `cs.SE`, `cs.PL`, `cs.AI`, `cs.LG`, and `cs.CL`.

Labels:

- `Core`: central to LLM + software/security research and backed by strong venue/source confidence.
- `Frontier`: promising recent preprint or newly accepted paper that needs follow-up verification.
- `Adjacent`: useful context, but not specific enough to be a central software-security method paper.
- `Survey`: broad mapping paper.
- `Negative/Evaluation`: mainly establishes limits, benchmarks, or failure modes.

Metadata note: for accepted 2026 papers, venue status is taken from official accepted-paper/program pages where available. Some arXiv-only and newly accepted papers have incomplete DOI/page metadata; those are marked as `Frontier` or noted in the entry.

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

## Benchmarks And Evaluation Datasets

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

## Method Patterns That Now Dominate

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

## What Seems Saturated

- Simple zero-shot "is this vulnerable?" classification on isolated functions.
- Prompt-only secure code generation without execution tests.
- LLM-as-a-judge evaluation without independent static/dynamic oracle.
- Small synthetic benchmarks where labels are obvious from CWE keywords.
- Claims of autonomous pentesting without environment control, logging, and reproducibility.

These topics can still be useful as baselines, but they are no longer enough for a strong top-security paper.

## What Looks Promising

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

## Research Direction Candidates

| Candidate Topic | Core Question | Why It Could Be Strong |
|---|---|---|
| LLM-verified sink exploration for Java/web apps | Can an agent move from candidate sink to reachable, validated vulnerability with fuzzer feedback? | Extends GONDAR/IRIS into practical exploitability triage without relying on pure model judgment. |
| LLM-assisted patch validation benchmark | Can we detect when a generated patch only hides the symptom or breaks intended behavior? | Patching is active, but validation is underdeveloped and very publishable. |
| Robust vulnerability detector under semantics-preserving transformations | Can detector results remain stable under realistic refactors/obfuscations? | Directly responds to Flashboom, Trust Me, and detector-evasion preprints. |
| Human-LLM reverse-engineering assistant evaluation | What workflows actually improve analyst speed/accuracy on binaries or obfuscated JS? | Topical after DeGPT, JsDeObsBench, and NDSS human-LLM SRE work; metrics are still immature. |
| Secure CRS orchestration layer | How should an AIxCC-style CRS manage permissions, evidence, tool calls, costs, and disclosure? | Moves from model-centric to systems-centric security research. |
| LLM-assisted fuzz harness synthesis for unsafe Rust or C++ libraries | Can LLMs generate type-correct, behaviorally meaningful harnesses that reach unsafe paths? | deepSURF/PromeFuzz show momentum; language-specific constraints are still hard. |
| RAG poisoning defenses for code-generation assistants | Can retrieval systems prevent vulnerable examples from steering generated code? | Strong link between software supply chain, code generation, and LLM app security. |

## Updated Reading Priority

1. Read the negative and benchmark papers first: S&P 2024 "LLMs Cannot Reliably...", SV-TrustEval-C, From Large to Mammoth, SeCodePLT, SecureVibeBench, ExploitBench.
2. Then read the hybrid program-analysis papers: IRIS, LLMxCPG, LATTE, GONDAR, ConcoLLMic.
3. Then read fuzzing/harness papers: LLM-guided protocol fuzzing, PromeFuzz, deepSURF, PILOT, FirmAgent, BSFuzzer, PANGOLIN, LogicFuzz.
4. Then read repair and delivery: APPATCH, SAN2PATCH, PORTGPT, ATLANTIS, OSS-CRS, AIxCC SoK.
5. Finally read reverse engineering and agent security: DeGPT, JsDeObsBench, Raconteur, IsolateGPT, AgentDoS, PromptPeek, Flashboom, Trust Me.

## Updated One-Sentence Thesis

The most promising research direction is not "LLM replaces program analysis", but "LLM supplies hard-to-manualize semantic hypotheses inside a verified cyber reasoning loop that produces reproducible evidence, validated patches, and auditable decisions."

## Area Literature Index

The expanded paper body now lives under [Academic-Status/](Academic-Status/). These files are grouped by this dossier's research-question areas, not by venue discipline. Most method papers are placed in their primary-read area; benchmark, survey, and cross-cutting system papers may be repeated where that makes the area file more useful.

| Area | File | Focus |
| --- | --- | --- |
| LLM for SE and code agents | [LLM-For-SE-And-Code-Agents.md](Academic-Status/LLM-For-SE-And-Code-Agents.md) | Repository-level coding, code agents, code generation, root-cause localization, code-agent benchmarks. |
| LLM for program analysis | [LLM-For-Program-Analysis.md](Academic-Status/LLM-For-Program-Analysis.md) | Static analysis, taint, symbolic/concolic execution, formal verification, specification mining. |
| LLM for fuzzing and dynamic analysis | [LLM-For-Fuzzing-And-Dynamic-Analysis.md](Academic-Status/LLM-For-Fuzzing-And-Dynamic-Analysis.md) | Fuzzing, harness generation, structured input generation, firmware/protocol/device fuzzing. |
| LLM for vulnerability detection and reasoning | [LLM-For-Vulnerability-Detection-And-Reasoning.md](Academic-Status/LLM-For-Vulnerability-Detection-And-Reasoning.md) | Detection, localization, reachability, exploitability reasoning, detector robustness. |
| LLM for repair and patch validation | [LLM-For-Repair-And-Patch-Validation.md](Academic-Status/LLM-For-Repair-And-Patch-Validation.md) | Repair, backporting, patch classification, validation, generated regression tests. |
| LLM for CTF, pentesting, and cyber agents | [LLM-For-CTF-Pentesting-And-Cyber-Agents.md](Academic-Status/LLM-For-CTF-Pentesting-And-Cyber-Agents.md) | CTF/pentesting agents, cyber reasoning, SOC/CTI automation, AIxCC-style systems. |
| LLM for reverse engineering and binary analysis | [LLM-For-Reverse-Engineering-And-Binary-Analysis.md](Academic-Status/LLM-For-Reverse-Engineering-And-Binary-Analysis.md) | Decompilation, symbol recovery, binary taint, deobfuscation, analyst assistance. |
| LLM app, agent, and security-tool attack surfaces | [LLM-App-Agent-And-Security-Tool-Attack-Surfaces.md](Academic-Status/LLM-App-Agent-And-Security-Tool-Attack-Surfaces.md) | LLM-integrated app risks, MCP/tool security, permissions, RAG poisoning, coding-assistant supply chain. |
| Benchmarks, datasets, and evaluation | [Benchmarks-Datasets-And-Evaluation.md](Academic-Status/Benchmarks-Datasets-And-Evaluation.md) | Benchmarks and evaluation platforms for code, security, CTF, agents, and reverse engineering. |
| Surveys and systematization | [Surveys-And-Systematization.md](Academic-Status/Surveys-And-Systematization.md) | Surveys, SoKs, roadmaps, and meta-evaluation papers. |

## Sweep Method And Source Log

DBLP was used as the main source for the focused venue set. The primary DBLP host was intermittently unavailable during the sweep, so the Trier mirror was used for table-of-contents pages where needed. DBLP paths checked include:

- Security: [USENIX Security 2024](https://dblp.org/db/conf/uss/uss2024.html), [USENIX Security 2025](https://dblp.org/db/conf/uss/uss2025.html), [IEEE S&P 2024](https://dblp.org/db/conf/sp/sp2024.html), [IEEE S&P 2025](https://dblp.org/db/conf/sp/sp2025.html), [ACM CCS 2024](https://dblp.org/db/conf/ccs/ccs2024.html), [ACM CCS 2025](https://dblp.org/db/conf/ccs/ccs2025.html), [NDSS 2024](https://dblp.org/db/conf/ndss/ndss2024.html), [NDSS 2025](https://dblp.org/db/conf/ndss/ndss2025.html), [NDSS 2026](https://dblp.org/db/conf/ndss/ndss2026.html).
- SE: [ICSE 2024](https://dblp.org/db/conf/icse/icse2024.html), [ICSE 2025](https://dblp.org/db/conf/icse/icse2025.html), [ASE 2024](https://dblp.org/db/conf/kbse/ase2024.html), [ASE 2025](https://dblp.org/db/conf/kbse/ase2025.html), [ISSTA 2024](https://dblp.org/db/conf/issta/issta2024.html), [ISSTA 2025 Companion](https://dblp.org/db/conf/issta/issta2025c.html), [PACMSE Volume 1](https://dblp.org/db/journals/pacmse/pacmse1.html), [PACMSE Volume 2](https://dblp.org/db/journals/pacmse/pacmse2.html).
- PL: [PACMPL Volume 8](https://dblp.org/db/journals/pacmpl/pacmpl8.html), [PACMPL Volume 9](https://dblp.org/db/journals/pacmpl/pacmpl9.html), [PACMPL Volume 10](https://dblp.org/db/journals/pacmpl/pacmpl10.html), covering POPL/PLDI/OOPSLA-era PACMPL publication.
- AI: [ICLR 2024](https://dblp.org/db/conf/iclr/iclr2024.html), [ICLR 2025](https://dblp.org/db/conf/iclr/iclr2025.html), [ICML 2024](https://dblp.org/db/conf/icml/icml2024.html), [ICML 2025](https://dblp.org/db/conf/icml/icml2025.html), [NeurIPS 2024](https://dblp.org/db/conf/nips/neurips2024.html), [AAAI 2024](https://dblp.org/db/conf/aaai/aaai2024.html), [AAAI 2025](https://dblp.org/db/conf/aaai/aaai2025.html), [AAAI 2026](https://dblp.org/db/conf/aaai/aaai2026.html).

The 2026 arXiv sweep used the official arXiv API with submitted-date filters from 2026-01-01 through 2026-06-06 and keyword families for LLM/software security, vulnerability, fuzzing, program analysis, static analysis, cyber agents, code agents, MCP, and secure code generation. arXiv-only entries are labeled `Frontier` unless venue acceptance is independently verified.

## Updated Category Read Order

1. Foundations and reality checks: `SWE-bench`, `SWE-agent`, `LLMs Cannot Reliably...`, `From Large to Mammoth`, `SV-TrustEval-C`, `CyberSecEval`, `Cybench`.
2. Core hybrid methods: IRIS, LLMxCPG, LATTE, LLM-assisted taint/spec generation, Fuzz4All, HyLLfuzz, GONDAR, FirmAgent, PANGOLIN, BSFuzzer, ProtocolGuard.
3. Repair and validation: zero-shot repair, APPATCH, SAN2PATCH, PORTGPT, PATCHAGENT, Mystique, PReMM, AIxCC/OSS-CRS systems.
4. Agent and tool security: CodeBreaker, Flashboom, Trust Me, package hallucinations, LLMSmith, IsolateGPT, AgentDoS, ACE/SAGA, MCP security papers, SkillGuard, Agent libOS.
5. Frontier 2026 arXiv: prioritize papers that add new datasets, evidence-producing pipelines, MCP/agent-security models, or reproducible vulnerability validation rather than generic LLM safety papers.

## Paper Index

Legacy compact snapshot. The expanded and venue-broadened paper body is now the split area index above.

| Key                                 | Paper                                                                                                                                        | Year | Venue/source            | Category                                       | Artifact/dataset                               | Method                                                                                                  | Evaluation target                                                 | Key result / contribution                                                                                               | Label               | Link                                                                                                                                          |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---: | ----------------------- | ---------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Deng2024PentestGPT                  | PentestGPT: Evaluating and Harnessing Large Language Models for Automated Penetration Testing                                                | 2024 | USENIX Security         | CTF/pentesting/cyber agents                    | Open-source framework, benchmark targets       | Modular LLM pentesting agent with task-specific memory modules                                          | Penetration-testing targets and CTF tasks                         | Shows strong gains over direct GPT-3.5-style use, but also context-loss limits                                          | Core                | https://www.usenix.org/conference/usenixsecurity24/presentation/deng                                                                          |
| Liu2024VulnerabilityManagement      | Exploring ChatGPT's Capabilities on Vulnerability Management                                                                                 | 2024 | USENIX Security         | Vulnerability management                       | Large vulnerability-management samples         | Task-specific ChatGPT evaluation                                                                        | Severity, patch, security relevance, report-processing tasks      | Useful baseline for where LLMs help or fail in triage workflows                                                         | Negative/Evaluation | https://www.usenix.org/conference/usenixsecurity24/presentation/liu-peiyu                                                                     |
| Fang2024CodeAnalysis                | Large Language Models for Code Analysis: Do LLMs Really Do Their Job?                                                                        | 2024 | USENIX Security         | Code analysis evaluation                       | Code-analysis test cases including obfuscation | Empirical LLM code-analysis study                                                                       | Program understanding and code analysis                           | Highlights brittleness of generic LLM code understanding, especially under obfuscation                                  | Negative/Evaluation | https://www.usenix.org/conference/usenixsecurity24/presentation/fang                                                                          |
| Yan2024CodeBreaker                  | An LLM-Assisted Easy-to-Trigger Backdoor Attack on Code Completion Models                                                                    | 2024 | USENIX Security         | Code-model poisoning                           | Poisoned code-completion data                  | LLM-transformed disguised vulnerable payloads                                                           | Code completion models and vulnerability detectors                | Shows LLM assistance can make backdoor payloads easier to trigger and harder to detect                                  | Core                | https://www.usenix.org/system/files/usenixsecurity24-yan.pdf                                                                                  |
| Pearce2024ZeroShotRepair            | Examining Zero-Shot Vulnerability Repair with Large Language Models                                                                          | 2024 | IEEE S&P                | Repair/patching                                | Vulnerability repair benchmark                 | Zero-shot LLM repair evaluation                                                                         | Vulnerable code patches                                           | Early rigorous evidence that plausible repair needs validation and is not enough                                        | Core                | https://sp2024.ieee-security.org/program-papers.html                                                                                          |
| Zhou2024LLMIF                       | LLMIF: Augmented Large Language Model for Fuzzing IoT Devices                                                                                | 2024 | IEEE S&P                | Fuzzing/dynamic analysis                       | IoT-device fuzzing setup                       | LLM-augmented fuzzing                                                                                   | IoT devices                                                       | Early top-venue example of LLMs bringing semantic guidance into IoT fuzzing                                             | Core                | https://www4.comp.polyu.edu.hk/~csxluo/LLMIF.pdf                                                                                              |
| Steenhoek2024LLMsCannot             | LLMs Cannot Reliably Identify and Reason About Security Vulnerabilities (Yet?)                                                               | 2024 | IEEE S&P / arXiv        | Vulnerability reasoning                        | Vulnerability reasoning benchmark              | Controlled empirical evaluation                                                                         | Security vulnerability identification and reasoning               | Important negative result: current LLMs are unreliable as standalone security reasoners                                 | Negative/Evaluation | https://arxiv.org/abs/2312.12575                                                                                                              |
| Meng2024ProtocolFuzzing             | Large Language Model Guided Protocol Fuzzing                                                                                                 | 2024 | NDSS                    | Fuzzing/dynamic analysis                       | Protocol fuzzing system                        | LLM-guided protocol semantics inference                                                                 | Network protocols                                                 | Uses LLMs to infer protocol structure and guide fuzzing beyond random mutation                                          | Core                | https://www.ndss-symposium.org/wp-content/uploads/2024-556-paper.pdf                                                                          |
| Hu2024DeGPT                         | DeGPT: Optimizing Decompiler Output with LLM                                                                                                 | 2024 | NDSS                    | Reverse engineering/binary analysis            | Decompiler-output datasets, user study         | Multi-role LLM post-processing for decompiler output                                                    | Ghidra/decompiler output, malware and tools                       | Improves readability with variable renaming, simplification, and comments while checking semantics                      | Core                | https://www.ndss-symposium.org/ndss-paper/degpt-optimizing-decompiler-output-with-llm/                                                        |
| Lyu2024LiftFuzz                     | LiftFuzz: Validating Binary Lifters through Context-aware Fuzzing with GPT                                                                   | 2024 | ACM CCS                 | Fuzzing/reverse engineering                    | Binary lifter validation target                | GPT-assisted context-aware fuzzing                                                                      | Binary lifters                                                    | Applies LLM-generated context to validate lifter correctness                                                            | Core                | https://dblp.org/db/conf/ccs/ccs2024                                                                                                          |
| Wang2024ProphetFuzz                 | ProphetFuzz: Fully Automated Prediction and Fuzzing of High-Risk Option Combinations with Only Documentation via LLM                         | 2024 | ACM CCS                 | Fuzzing/dynamic analysis                       | Tool plus CVE findings                         | LLM mines documentation for risky option combinations                                                   | CLI tools and document-driven option spaces                       | Shows documentation-only LLM guidance can find high-risk fuzzing configurations                                         | Core                | https://arxiv.org/abs/2409.00922                                                                                                              |
| Lyu2024PromptFuzzing                | Prompt Fuzzing for Fuzz Driver Generation                                                                                                    | 2024 | ACM CCS / arXiv         | Fuzz harness generation                        | Fuzz-driver generation pipeline                | Prompt strategy for generating fuzz drivers                                                             | Library APIs                                                      | Demonstrates LLMs can draft fuzz drivers, with compile/runtime feedback still essential                                 | Core                | https://arxiv.org/abs/2312.17677                                                                                                              |
| Zeng2024PromSec                     | PromSec: Prompt Optimization for Secure Generation of Functional Source Code with LLMs                                                       | 2024 | ACM CCS                 | Secure code generation                         | Prompt-optimization method                     | Security-aware prompt optimization                                                                      | Generated source code                                             | Improves secure functional code generation but remains prompt-level mitigation                                          | Core                | https://arxiv.org/abs/2409.12699                                                                                                              |
| Liu2024LLMSmith                     | Demystifying RCE Vulnerabilities in LLM-Integrated Apps                                                                                      | 2024 | ACM CCS                 | LLM app/tool attack surface                    | LLMSmith                                       | Analysis of LLM app RCE/file-risk patterns                                                              | LLM-integrated applications                                       | Shows LLM app orchestration can surface conventional RCE and arbitrary-file risks                                       | Core                | https://lyutoon.github.io/papers/LLMSmith-CCS.pdf                                                                                             |
| Xie2024ReSym                        | ReSym: Harnessing LLMs to Recover Variable and Data Structure Symbols from Stripped Binaries                                                 | 2024 | ACM CCS                 | Reverse engineering/binary analysis            | Symbol recovery system                         | LLM-based symbol recovery                                                                               | Stripped binaries                                                 | Uses LLMs to restore analyst-meaningful names and structures                                                            | Core                | https://www.sigsac.org/ccs/CCS2024/program/accepted-papers.html                                                                               |
| Hui2024PLeak                        | PLeak: Prompt Leaking Attacks against Large Language Model Applications                                                                      | 2024 | ACM CCS                 | LLM app/tool attack surface                    | Attack/evaluation suite                        | Prompt extraction attack analysis                                                                       | LLM applications                                                  | Relevant to security of coding/security assistants that hide system prompts or policies                                 | Adjacent            | https://www.sigsac.org/ccs/CCS2024/program/accepted-papers.html                                                                               |
| Xia2024Fuzz4All                     | Fuzz4All: Universal Fuzzing with Large Language Models                                                                                       | 2024 | ICSE                    | Fuzzing/dynamic analysis                       | Fuzz4All                                       | LLM-based universal input generation and autoprompting                                                  | Compilers, solvers, runtimes, libraries                           | Finds many confirmed bugs across multiple input languages and systems                                                   | Core                | https://doi.org/10.1145/3597503.3639121                                                                                                       |
| Deng2024FuzzGPT                     | Large Language Models are Edge-Case Generators: Crafting Unusual Programs for Fuzzing Deep Learning Libraries                                | 2024 | ICSE                    | Fuzzing/dynamic analysis                       | FuzzGPT                                        | Historical bug-guided LLM generation                                                                    | Deep learning libraries                                           | Shifts LLM generation toward unusual bug-triggering programs                                                            | Core                | https://doi.org/10.1145/3597503.3623343                                                                                                       |
| Zhang2024FuzzDrivers                | How Effective Are They? Exploring Large Language Model Based Fuzz Driver Generation                                                          | 2024 | ISSTA                   | Fuzz harness generation                        | Fuzz-driver benchmark                          | Empirical evaluation of LLM-generated fuzz drivers                                                      | Library APIs                                                      | Clarifies compile, API-use, and false-positive limits in generated drivers                                              | Negative/Evaluation | https://doi.org/10.1145/3650212.3680355                                                                                                       |
| Li2024CoSec                         | CoSec: On-the-Fly Security Hardening of Code LLMs via Supervised Co-decoding                                                                 | 2024 | ISSTA                   | Secure code generation                         | Security co-decoding model                     | Small secure model guides base model decoding                                                           | CodeGen, StarCoder, DeepSeek-Coder style models                   | Improves security ratio while preserving functional correctness in evaluated models                                     | Core                | https://doi.org/10.1145/3650212.3680371                                                                                                       |
| Jimenez2024SWEBench                 | SWE-bench: Can Language Models Resolve Real-world GitHub Issues?                                                                             | 2024 | ICLR                    | SE/code agents, benchmark                      | 2,294 GitHub issue/PR tasks                    | Repository-level issue-resolution benchmark                                                             | Python repositories                                               | Establishes repo-level coding as much harder than function-level coding                                                 | Core                | https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html                             |
| Yang2024SWEAgent                    | SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering                                                                   | 2024 | NeurIPS                 | SE/code agents                                 | SWE-agent                                      | Agent-computer interface for repo editing and test execution                                            | SWE-bench tasks                                                   | Shows interface and tool design matter as much as model choice                                                          | Core                | https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html                          |
| Bhatt2024CyberSecEval2              | CyberSecEval 2: A Wide-Ranging Cybersecurity Evaluation Suite for Large Language Models                                                      | 2024 | arXiv                   | Benchmarks/evaluation                          | CyberSecEval 2                                 | Cyber risk/capability benchmark suite                                                                   | Prompt injection, code interpreter, insecure code and cyber tasks | Broad benchmark for LLM cybersecurity risk and capability measurement                                                   | Negative/Evaluation | https://arxiv.org/abs/2404.13161                                                                                                              |
| Bhatt2024CyberSecEval3              | CYBERSECEVAL 3: Advancing the Evaluation of Cybersecurity Risks and Capabilities in Large Language Models                                    | 2024 | arXiv                   | Benchmarks/evaluation                          | CyberSecEval 3                                 | Expanded cybersecurity evaluation suite                                                                 | Offensive/defensive cyber-risk tasks                              | Updates CyberSecEval with broader capability/risk coverage                                                              | Negative/Evaluation | https://arxiv.org/abs/2408.01605                                                                                                              |
| Zhang2024NYUCTF                     | NYU CTF Bench: A Scalable Open-Source Benchmark Dataset for Evaluating LLMs in Offensive Security                                            | 2024 | arXiv                   | CTF/pentesting/cyber agents                    | CTF benchmark                                  | Standardized CTF task evaluation                                                                        | Offensive-security challenge tasks                                | Provides open benchmark context for controlled cyber-agent evaluation                                                   | Negative/Evaluation | https://arxiv.org/abs/2406.05590                                                                                                              |
| Zhang2024Cybench                    | Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models                                                  | 2024 | arXiv                   | CTF/pentesting/cyber agents                    | Cybench                                        | Agent benchmark over cybersecurity tasks                                                                | Professional CTF/cyber tasks                                      | Evaluates multiple frontier/open models under interactive cyber tasks                                                   | Core                | https://arxiv.org/abs/2408.08926                                                                                                              |
| Li2024IRIS                          | IRIS: LLM-Assisted Static Analysis for Detecting Security Vulnerabilities                                                                    | 2025 | ICLR / arXiv            | Program analysis/static analysis               | CWE-Bench-Java, code                           | LLM-inferred taint specs plus static analysis                                                           | Whole Java repositories                                           | Shows LLMs can infer sources/sinks/context while CodeQL-style analysis verifies flows                                   | Core                | https://arxiv.org/abs/2405.17238                                                                                                              |
| Lekssays2025LLMxCPG                 | LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided LLMs                                                       | 2025 | USENIX Security         | Vulnerability detection                        | CPG-guided pipeline                            | CPG slicing plus LLM classification/reasoning                                                           | Source-code vulnerabilities                                       | Improves context efficiency and vulnerability detection robustness                                                      | Core                | https://www.usenix.org/conference/usenixsecurity25/presentation/lekssays                                                                      |
| Nong2025APPATCH                     | APPATCH: Automated Adaptive Prompting LLMs for Real-World Software Vulnerability Patching                                                    | 2025 | USENIX Security         | Repair/patching                                | APPATCH                                        | Adaptive prompting with vulnerability semantics                                                         | Real-world vulnerability patches                                  | Shows semantic/adaptive prompting helps real-world patch generation                                                     | Core                | https://www.usenix.org/conference/usenixsecurity25/presentation/nong                                                                          |
| Kim2025SAN2PATCH                    | Logs In, Patches Out: Automated Vulnerability Repair via Tree-of-Thought LLM Analysis                                                        | 2025 | USENIX Security         | Repair/patching                                | SAN2PATCH / VulnLoc-style data                 | Sanitizer-log guided tree-of-thought repair                                                             | Vulnerable C/C++ code with sanitizer evidence                     | Uses crash logs as evidence to guide patch generation and validation                                                    | Core                | https://www.usenix.org/conference/usenixsecurity25/presentation/kim-youngjoon                                                                 |
| Spracklen2025PackageHallucinations  | We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs                                        | 2025 | USENIX Security         | Supply chain / secure code generation          | Large package-hallucination corpus             | Empirical package recommendation study                                                                  | Python/JavaScript package ecosystems                              | Shows hallucinated package names are frequent and persistent enough to become supply-chain attack surface               | Core                | https://www.usenix.org/publications/loginonline/we-have-package-you-comprehensive-analysis-package-hallucinations-code                        |
| Yang2025HyLLFuzz                    | Hybrid Language Processor Fuzzing via LLM-Based Constraint Solving                                                                           | 2025 | USENIX Security         | Fuzzing/concolic-adjacent                      | HyLLfuzz                                       | LLM as constraint solver with prioritization/context expansion                                          | Language processors                                               | Uses LLMs to solve semantic constraints random mutation and symbolic execution struggle with                            | Core                | https://www.usenix.org/conference/usenixsecurity25/presentation/yang-yupeng                                                                   |
| Liu2025Flashboom                    | Make a Feint to the East While Attacking in the West: Blinding LLM-Based Code Auditors with Flashboom Attacks                                | 2025 | IEEE S&P                | LLM code-auditor attack surface                | Flashboom attacks                              | Attention-diversion/adversarial code context                                                            | LLM code auditors                                                 | Shows LLM auditors can be blinded by semantically distracting code transformations                                      | Core                | https://cs.nju.edu.cn/fxu/static/papers/featured/flashboom-sp2025.pdf                                                                         |
| Xu2025SVTrustEvalC                  | SV-TrustEval-C: Evaluating Structure and Semantic Reasoning in LLMs for Source Code Vulnerability Analysis                                   | 2025 | IEEE S&P / arXiv        | Benchmarks/evaluation                          | SV-TrustEval-C                                 | Structure and semantic perturbation benchmark                                                           | C vulnerability reasoning                                         | Tests whether models reason causally or pattern-match vulnerability cues                                                | Negative/Evaluation | https://arxiv.org/abs/2505.20630                                                                                                              |
| Tihanyi2025DigitalCyberExpert       | The Digital Cybersecurity Expert: How Far Have We Come?                                                                                      | 2025 | IEEE S&P / arXiv        | Benchmarks/evaluation                          | Cybersecurity role/knowledge benchmark         | Role-specific capability evaluation                                                                     | Cybersecurity tasks                                               | Measures cybersecurity expertise more finely than generic QA                                                            | Negative/Evaluation | https://arxiv.org/abs/2504.11783                                                                                                              |
| Lin2025FromLargeToMammoth           | From Large to Mammoth: A Comparative Evaluation of Large Language Models in Vulnerability Detection                                          | 2025 | NDSS                    | Vulnerability detection evaluation             | Java and C/C++ vulnerability samples           | Large comparative LLM evaluation                                                                        | File-level vulnerability detection                                | Finds performance depends heavily on language, context, model family, quantization, and prompting                       | Negative/Evaluation | https://www.ndss-symposium.org/ndss-paper/from-large-to-mammoth-a-comparative-evaluation-of-large-language-models-in-vulnerability-detection/ |
| Deng2025Raconteur                   | RACONTEUR: A Knowledgeable, Insightful, and Portable LLM-Powered Shell Command Explainer                                                     | 2025 | NDSS                    | Analyst assistance / reverse engineering       | Shell command explanation dataset              | Expert-knowledge LLM explainer                                                                          | Malicious shell commands                                          | Improves analyst-oriented explanation of complex shell commands                                                         | Core                | https://raconteur-ndss.github.io/                                                                                                             |
| Zhang2025IsolateGPT                 | IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems                                                                | 2025 | NDSS                    | LLM app/agent security                         | Isolation architecture                         | Execution isolation for LLM systems                                                                     | Tool-using LLM agents                                             | Makes isolation a first-class security property for LLM-based systems                                                   | Core                | https://www.ndss-symposium.org/wp-content/uploads/2025-1131-paper.pdf                                                                         |
| Zhou2025LATTE                       | LATTE: LLM-Powered Static Binary Taint Analysis                                                                                              | 2025 | ACM TOSEM               | Program analysis/binary analysis               | LATTE                                          | LLM-assisted taint rule/specification inference                                                         | Binary programs                                                   | Automates parts of binary taint analysis that need expert rules                                                         | Core                | https://dl.acm.org/doi/10.1145/3711816                                                                                                        |
| Li2025CodeGuarder                   | Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection                                            | 2025 | ACM CCS / arXiv         | RAG/supply-chain/security                      | CodeGuarder                                    | Retrieves security knowledge plus examples                                                              | RAG-based code generation                                         | Hardens RAG code generation and evaluates poisoned retrieval scenarios                                                  | Core                | https://arxiv.org/abs/2504.16429                                                                                                              |
| Chen2025CTFKnow                     | Measuring and Augmenting Large Language Models for Solving Capture-the-Flag Challenges                                                       | 2025 | ACM CCS / arXiv         | CTF/pentesting/cyber agents                    | CTFKnow, CTFAgent                              | Knowledge benchmark plus agent augmentation                                                             | CTF tasks                                                         | Separates cyber knowledge from environment-grounded CTF solving                                                         | Core                | https://arxiv.org/abs/2506.17644                                                                                                              |
| Zhang2025PromeFuzz                  | PromeFuzz: A Knowledge-Driven Approach to Fuzzing Harness Generation with Large Language Models                                              | 2025 | ACM CCS                 | Fuzz harness generation                        | PromeFuzz                                      | Knowledge-driven harness synthesis                                                                      | Library fuzzing                                                   | Directly targets one of the biggest practical blockers for fuzzing at scale                                             | Core                | https://dblp.org/db/conf/ccs/ccs2025.html                                                                                                     |
| Wei2025JsDeObsBench                 | JsDeObsBench: Measuring and Benchmarking LLMs for JavaScript Deobfuscation                                                                   | 2025 | ACM CCS / arXiv         | Reverse engineering / benchmark                | JsDeObsBench                                   | Deobfuscation benchmark                                                                                 | Obfuscated JavaScript                                             | Evaluates LLM usefulness for JS malware/web reverse-engineering workflows                                               | Negative/Evaluation | https://arxiv.org/abs/2506.20170                                                                                                              |
| Fan2025LLMSupplyChainAgenda         | Large Language Model Supply Chain: A Research Agenda                                                                                         | 2025 | ACM TOSEM               | Supply chain / position                        | Research agenda                                | Systematization and agenda                                                                              | LLM supply-chain risks                                            | Frames supply-chain risks across model/data/tool dependencies                                                           | Survey              | https://doi.org/10.1145/3708531                                                                                                               |
| Sheng2025LLMSoftwareSecuritySurvey  | LLMs in Software Security: A Survey of Vulnerability Detection Techniques and Insights                                                       | 2025 | arXiv                   | Survey                                         | Survey taxonomy                                | Literature survey                                                                                       | Vulnerability detection techniques                                | Broad map for LLM vulnerability-detection work                                                                          | Survey              | https://doi.org/10.48550/arXiv.2502.07049                                                                                                     |
| Zhu2025SoftwareSecuritySurvey       | When Software Security Meets Large Language Models: A Survey                                                                                 | 2025 | IEEE/CAA JAS            | Survey                                         | Survey taxonomy                                | Literature survey                                                                                       | Software-security applications of LLMs                            | Useful high-level survey for LLM + software security                                                                    | Survey              | https://doi.org/10.1109/JAS.2024.124971                                                                                                       |
| Zhou2025SafeGenBench                | SafeGenBench: Benchmarking Security Vulnerability Detection in LLM-Generated Code                                                            | 2025 | arXiv                   | Benchmarks/evaluation                          | SafeGenBench                                   | Benchmark framework                                                                                     | LLM-generated code                                                | Evaluates vulnerability detection on code produced by LLMs                                                              | Frontier            | https://arxiv.org/abs/2506.05692                                                                                                              |
| Wang2024SeCodePLT                   | SeCodePLT: A Unified Platform for Evaluating Security of Code GenAI                                                                          | 2024 | arXiv                   | Benchmarks/evaluation                          | SeCodePLT                                      | Evaluation platform                                                                                     | Code-generation security                                          | Emphasizes security relevance and benchmark quality in generated-code evaluation                                        | Frontier            | https://arxiv.org/abs/2410.11096                                                                                                              |
| Ali2025SecureVibeBench              | SecureVibeBench: Multi-file Secure Coding Tasks for Code Agents                                                                              | 2025 | arXiv                   | Benchmarks/evaluation                          | SecureVibeBench                                | Multi-file benchmark with functional/security oracles                                                   | Code agents on vulnerability-introducing scenarios                | Moves secure-code evaluation toward realistic multi-file tasks                                                          | Frontier            | https://arxiv.org/abs/2509.22097                                                                                                              |
| Liang2025CKGLLM                     | CKG-LLM: Natural-Language Vulnerability Patterns to Knowledge-Graph Queries                                                                  | 2025 | arXiv                   | Program analysis / smart contracts             | Contract knowledge graph                       | LLM translates NL patterns to executable graph queries                                                  | Smart contracts                                                   | Promising pattern-to-query direction; arXiv-only metadata should be rechecked                                           | Frontier            | https://arxiv.org/abs/2512.06846                                                                                                              |
| Zhao2025WebPoCStudy                 | A Systematic Study on Generating Web Vulnerability PoCs Using LLMs                                                                           | 2025 | arXiv                   | Vulnerability validation / dual-use evaluation | Web vulnerability PoC dataset                  | Disclosure-stage study of LLM PoC generation                                                            | Web vulnerabilities                                               | Important for defensive validation and policy, but dual-use and arXiv-only                                              | Frontier            | https://arxiv.org/abs/2510.10148                                                                                                              |
| Sheng2025FuzzingBrain               | All You Need Is A Fuzzing Brain: An LLM-Powered System for Automated Vulnerability Detection and Patching                                    | 2025 | arXiv / AIxCC           | Cyber reasoning systems                        | Open CRS, leaderboard                          | Fuzzing-centered CRS with LLM components                                                                | AIxCC vulnerability discovery and patching                        | AIxCC finalist system: strong example of end-to-end hybrid vulnerability discovery/repair                               | Frontier            | https://arxiv.org/abs/2509.07225                                                                                                              |
| Kim2025ATLANTIS                     | ATLANTIS: AI-driven Threat Localization, Analysis, and Triage Intelligence System                                                            | 2025 | arXiv / AIxCC           | Cyber reasoning systems                        | Team Atlanta CRS                               | Multi-component CRS for localization, analysis, triage, patching                                        | AIxCC final                                                       | Describes winning AIxCC CRS; key signal for end-to-end systems direction                                                | Frontier            | https://arxiv.org/abs/2509.14589                                                                                                              |
| Team2026OSSCRS                      | OSS-CRS: Liberating AIxCC Cyber Reasoning Systems for Real-World Open-Source Security                                                        | 2026 | arXiv                   | Cyber reasoning systems                        | OSS CRS                                        | CRS adaptation to real open-source workflows                                                            | Open-source security targets                                      | Extends AIxCC CRS ideas toward practical OSS security                                                                   | Frontier            | https://arxiv.org/abs/2603.08566                                                                                                              |
| SoK2026AIxCC                        | SoK: DARPA's AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned                                              | 2026 | arXiv                   | Cyber reasoning systems / SoK                  | AIxCC lessons                                  | Systematization                                                                                         | AIxCC architectures and scoring                                   | Useful architecture-level view of CRS design and evaluation                                                             | Survey              | https://arxiv.org/abs/2602.07666                                                                                                              |
| Li2026PORTGPT                       | PORTGPT: Towards Automated Backporting Using Large Language Models                                                                           | 2026 | IEEE S&P                | Repair/backporting                             | PORTGPT                                        | LLM agent using code, Git history, build/compiler feedback                                              | Security patch backporting                                        | Moves repair research from fresh patches to long-lived branch maintenance                                               | Core                | https://sp2026.ieee-security.org/accepted-papers.html                                                                                         |
| Luo2026ConcoLLMic                   | Agentic Concolic Execution                                                                                                                   | 2026 | IEEE S&P                | Program analysis / concolic execution          | ConcoLLMic                                     | LLM agents perform language/theory-agnostic concolic workflows                                          | Multi-language programs                                           | Reduces environment-modeling burden and improves coverage over classic baselines                                        | Core                | https://concollmic.github.io/                                                                                                                 |
| Tu2026Cottontail                    | Large Language Model-Driven Concolic Execution for Highly Structured Test Input Generation                                                   | 2026 | IEEE S&P / arXiv        | Program analysis / concolic execution          | Cottontail                                     | LLM-driven constraint solving and seed acquisition                                                      | XML, SQL, JavaScript, JSON parsers/libraries                      | Generates structured inputs that satisfy path constraints and syntax                                                    | Core                | https://arxiv.org/abs/2504.17542                                                                                                              |
| Fleischer2026GONDAR                 | Contextualizing Sink Knowledge for Java Vulnerability Discovery                                                                              | 2026 | IEEE S&P / arXiv        | Vulnerability discovery / fuzzing              | GONDAR                                         | Sink-centric scanning, LLM-assisted filtering, exploration/exploitation agents, coverage-guided fuzzing | Java applications and security-sensitive sink APIs                | Connects sink semantics, reachability, exploitability conditions, and runtime feedback; strong AIxCC/OSS-CRS link       | Core                | https://arxiv.org/abs/2604.01645                                                                                                              |
| Shiraishi2026PILOT                  | PILOT: Command-line Interface Fuzzing via Path-Guided, Iterative Large Language Model Prompting                                              | 2026 | IEEE S&P                | Fuzzing/dynamic analysis                       | PILOT                                          | Call-path context plus iterative LLM prompting                                                          | CLI programs                                                      | LLM generates option/input combinations guided by path feedback                                                         | Core                | https://sp2026.ieee-security.org/accepted-papers.html                                                                                         |
| Li2026DeepSURF                      | deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses                                            | 2026 | IEEE S&P / arXiv        | Fuzz harness generation                        | deepSURF                                       | Static analysis plus LLM-generated Rust fuzz harnesses                                                  | Unsafe Rust code                                                  | Targets hard Rust-specific harness problems around types, generics, traits, and unsafe blocks                           | Core                | https://arxiv.org/abs/2506.15648                                                                                                              |
| Lin2026SpecAuditor                  | SpecAuditor: Generating Audit Specifications for LLM-Driven Bug Detection                                                                    | 2026 | IEEE S&P                | Program analysis / audit specs                 | Artifact on Zenodo                             | LLM-generated audit specifications                                                                      | Bug detection workflows                                           | Strong signal that specification generation is becoming a central LLM role                                              | Frontier            | https://sp2026.ieee-security.org/accepted-papers.html                                                                                         |
| Qiu2026DNSLLM                       | Knocking on the Front Door: An LLM-Guided Systematic Analysis of DNS Query Processing Vulnerabilities                                        | 2026 | IEEE S&P                | Vulnerability discovery                        | DNS analysis system                            | LLM-guided systematic protocol analysis                                                                 | DNS query processing                                              | Domain-specific LLM-guided vulnerability analysis for network infrastructure                                            | Core                | https://sp2026.ieee-security.org/accepted-papers.html                                                                                         |
| Wu2026AgentPermissions              | Towards Automating Data Access Permissions in AI Agents                                                                                      | 2026 | IEEE S&P                | LLM app/agent security                         | Permission model                               | Data access permission automation                                                                       | AI agents                                                         | Treats agent data access as a security problem rather than only a UX problem                                            | Core                | https://sp2026.ieee-security.org/accepted-papers.html                                                                                         |
| Li2026WebCloak                      | WebCloak: Characterizing and Mitigating Threats from LLM-Driven Web Agents as Intelligent Scrapers                                           | 2026 | IEEE S&P                | LLM app/agent security                         | Web agent attack/defense study                 | Characterization and mitigation                                                                         | Web agents                                                        | Shows web agents introduce scraping/automation threat patterns that need defenses                                       | Core                | https://sp2026.ieee-security.org/accepted-papers.html                                                                                         |
| Mustafa2026LLMSOC                   | LLMs in the SOC: An Empirical Study of Human-AI Collaboration in Security Operations Centres                                                 | 2026 | IEEE S&P                | Analyst assistance / SOC                       | SOC study                                      | Human-AI collaboration study                                                                            | Security operations centres                                       | Important human-factors evidence for analyst-facing LLM tools                                                           | Adjacent            | https://sp2026.ieee-security.org/accepted-papers.html                                                                                         |
| Jia2026PANGOLIN                     | PANGOLIN: Fuzzing Multilingual IoT Firmware with LLM-Driven Code Analysis                                                                    | 2026 | USENIX Security Cycle 1 | Fuzzing/static analysis                        | PANGOLIN                                       | LLM extracts cross-language interfaces/specs                                                            | Multilingual IoT firmware                                         | Finds zero-day firmware vulnerabilities by bridging C and scripting-language logic                                      | Core                | https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers                                                                     |
| Luo2026AgentDoS                     | Autonomy Comes with Costs: Detecting DoS Vulnerabilities in LLM-based Agents                                                                 | 2026 | USENIX Security Cycle 1 | LLM app/agent security                         | AgentDoS                                       | Resource-lifecycle-guided fuzzing                                                                       | LLM-based agents                                                  | Finds DoS-style failures across real agent systems; shows autonomy adds resource-governance risks                       | Core                | https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers                                                                     |
| Zhang2026NOIR                       | NOIR: Privacy-Preserving Generation of Code with Open-Source LLMs                                                                            | 2026 | USENIX Security Cycle 1 | Privacy / code generation                      | NOIR                                           | Privacy-preserving code-generation protocol                                                             | Cloud-assisted open-source LLM code generation                    | Relevant where code prompts and outputs are sensitive IP/security artifacts                                             | Adjacent            | https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers                                                                     |
| Alam2026PHILTER                     | SoK: PHILTER: Uncovering Security and Functional Gaps in AI-based Phishing Website Detection Literature via an LLM-based Reasoning Framework | 2026 | USENIX Security Cycle 1 | SoK / LLM-assisted review                      | PHILTER                                        | LLM-assisted literature assessment with expert validation                                               | Phishing detection literature                                     | Shows a careful pattern for using LLMs in systematic review without delegating final judgment                           | Adjacent            | https://www.usenix.org/conference/usenixsecurity26/cycle1-accepted-papers                                                                     |
| Ji2026FirmAgent                     | FirmAgent: Leveraging Fuzzing to Assist LLM Agents with IoT Firmware Vulnerability Discovery                                                 | 2026 | NDSS                    | Fuzzing/static analysis                        | FirmAgent                                      | Fuzzing identifies input points; LLM agents perform taint/path analysis and testcase refinement         | IoT firmware                                                      | Reports high-precision vulnerability discovery and many new firmware bugs                                               | Core                | https://www.ndss-symposium.org/ndss-paper/firmagent-leveraging-fuzzing-to-assist-llm-agents-with-iot-firmware-vulnerability-discovery/        |
| Yang2026BSFuzzer                    | BSFuzzer: Context-Aware Semantic Fuzzing for BLE Logic Flaw Detection                                                                        | 2026 | NDSS                    | Fuzzing/protocol analysis                      | BSFuzzer                                       | LLM agent parses Bluetooth spec and validates responses                                                 | BLE devices                                                       | Finds logic flaws that conventional fuzzing/formal analysis miss                                                        | Core                | https://www.ndss-symposium.org/ndss-paper/bsfuzzer-context-aware-semantic-fuzzing-for-ble-logic-flaw-detection/                               |
| Song2026ProtocolGuard               | ProtocolGuard: Detecting Protocol Non-compliance Bugs via LLM-guided Static Analysis and Dynamic Verification                                | 2026 | NDSS                    | Program analysis/fuzzing                       | ProtocolGuard                                  | LLM-guided slicing, rule inconsistency detection, dynamic verification                                  | Protocol implementations                                          | Strong template: LLM extracts/specifies rules, program analysis narrows code, fuzzing verifies                          | Core                | https://www.ndss-symposium.org/wp-content/uploads/2026-f521-paper.pdf                                                                         |
| Liu2026IoTBec                       | IoTBec: Firmware- and Source-Code-Independent Recurring Vulnerability Detection with LLM-Driven Fuzzing                                      | 2026 | NDSS                    | Fuzzing/vulnerability discovery                | IoTBec                                         | Black-box interface signatures plus LLM-driven fuzzing                                                  | IoT devices                                                       | Finds recurring and variant vulnerabilities without firmware/source access                                              | Core                | https://www.ndss-symposium.org/ndss-program/symposium-2026/                                                                                   |
| Zhang2026LogicFuzz                  | LogicFuzz: An LLM-Driven Fuzzing Framework for Detecting Logic Instruction Bugs in PLCs                                                      | 2026 | NDSS                    | Fuzzing/industrial control                     | LogicFuzz                                      | Semantic dependency graphs and LLM-guided seed/program generation                                       | PLC firmware                                                      | Domain-specific LLM fuzzing for industrial control logic bugs                                                           | Core                | https://www.ndss-symposium.org/wp-content/uploads/2026-f1081-paper.pdf                                                                        |
| Xu2026TrustMe                       | Trust Me, I Know This Function: Hijacking LLM Static Analysis using Bias                                                                     | 2026 | NDSS                    | LLM code-auditor attack surface                | Attack/evaluation suite                        | Bias/abstraction attack on LLM static analysis                                                          | LLM static-analysis assistants                                    | Shows small meaningful bugs can be hidden by misleading function-level priors                                           | Core                | https://www.ndss-symposium.org/ndss-paper/trust-me-i-know-this-function-hijacking-llm-static-analysis-using-bias/                             |
| Li2026FidelityGPT                   | FidelityGPT: Correcting Decompilation Distortions with Retrieval Augmented Generation                                                        | 2026 | NDSS                    | Reverse engineering/binary analysis            | FidelityGPT                                    | RAG-based correction of decompiler distortion                                                           | Decompiled code                                                   | Improves fidelity/readability beyond DeGPT-style post-processing                                                        | Frontier            | https://www.ndss-symposium.org/ndss-paper/fidelitygpt-correcting-decompilation-distortions-with-retrieval-augmented-generation/               |
| Doupe2026HumanLLMSRE                | Decompiling the Synergy: An Empirical Study of Human-LLM Teaming in Software Reverse Engineering                                             | 2026 | NDSS                    | Reverse engineering / human factors            | Controlled reverse-engineering study           | Human-LLM collaboration evaluation                                                                      | Software reverse-engineering tasks                                | Provides controlled evidence for when LLM assistance helps or hurts analysts, beyond anecdotal tool demos               | Adjacent            | https://adamdoupe.com/publications/decompiling-synergy-ndss2026.pdf                                                                           |
| Jiang2026IRDecompilation            | Does Representation Matter? Evaluating IRs for LLM-based Binary Decompilation                                                                | 2026 | NDSS BAR                | Reverse engineering/binary analysis            | IR benchmark                                   | Systematic evaluation of IR choices                                                                     | LLM decompilation                                                 | Highlights that representation choice matters for neural/LLM decompilation                                              | Frontier            | https://www.ndss-symposium.org/ndss-paper/auto-draft-654/                                                                                     |
| Nishizaka2026LLMResistantProtection | Towards LLM-Resistant Software Protection: Agent Failure Patterns in CTF Reverse Engineering                                                 | 2026 | NDSS BAR                | Reverse engineering / benchmark                | 24 CTF reverse-engineering tasks               | Failure-pattern analysis of LLM agents                                                                  | Software protections and CTF reverse engineering                  | Maps agent weaknesses such as over-trust, context limits, and plan persistence; useful for adversarial benchmark design | Frontier            | https://www.ndss-symposium.org/ndss-paper/auto-draft-657/                                                                                     |
| Lyu2026DetectorEvasion              | Syntax- and Compilation-Preserving Evasion of LLM Vulnerability Detectors                                                                    | 2026 | arXiv                   | LLM detector robustness                        | Evasion transformations                        | Semantics-preserving source transformations                                                             | LLM vulnerability detectors                                       | Frontier evidence that detector robustness must be tested under realistic refactors                                     | Frontier            | https://arxiv.org/abs/2602.00305                                                                                                              |
| Zhang2026SecureCodeGeneration       | How Secure is Secure Code Generation?                                                                                                        | 2026 | arXiv                   | Secure code generation robustness              | Adversarial prompt set                         | Robustness testing                                                                                      | Secure-code-generation systems                                    | Tests whether secure-generation defenses survive adversarial prompting                                                  | Frontier            | https://arxiv.org/abs/2601.07084                                                                                                              |
| Patel2026ExploitBench               | ExploitBench: A Capability-Ladder Benchmark for Exploit Agents                                                                               | 2026 | arXiv                   | Benchmarks/evaluation                          | ExploitBench                                   | Stepwise capability decomposition                                                                       | Exploit-agent workflows                                           | Useful because it decomposes capability rather than scoring only final exploit success                                  | Frontier            | https://arxiv.org/abs/2605.14153                                                                                                              |
| Shao2025CyberGym                    | CyberGym: Evaluating AI Agents on Real-World Vulnerabilities Across Massive Codebases                                                        | 2025 | arXiv                   | Benchmarks/evaluation                          | CyberGym                                       | Real-vulnerability benchmark with execution oracles                                                     | Large codebases                                                   | Pushes cyber-agent evaluation toward realistic codebase scale                                                           | Frontier            | https://arxiv.org/abs/2506.02548                                                                                                              |

## Category Index

### LLM For SE And Code Agents

Start with SWE-bench and SWE-agent because they explain why security agents are difficult: real tasks require repository navigation, editing, testing, and state management. The security-specific implication is that vulnerability analysis cannot be reduced to single-function classification. PORTGPT, SecureVibeBench, CyberGym, and AIxCC systems extend this repo-level view into security patching and CRS workflows.

Key reads: `Jimenez2024SWEBench`, `Yang2024SWEAgent`, `Li2026PORTGPT`, `Ali2025SecureVibeBench`, `Shao2025CyberGym`.

### LLM For Program Analysis

The strongest pattern is LLM-as-specification-miner plus analysis-as-verifier. IRIS infers taint specs and contextual information for CodeQL-style analysis. LLMxCPG uses code property graphs to select context. LATTE applies LLM support to binary taint rules. GONDAR adds sink-centric Java vulnerability exploration, where LLM-assisted filtering and agents work with fuzzer feedback. SpecAuditor, ProtocolGuard, DNS LLM-guided analysis, ConcoLLMic, and Cottontail all fit the broader direction: the LLM proposes semantics, constraints, or audit rules; a symbolic/static/dynamic substrate checks them.

Key reads: `Li2024IRIS`, `Lekssays2025LLMxCPG`, `Zhou2025LATTE`, `Fleischer2026GONDAR`, `Lin2026SpecAuditor`, `Luo2026ConcoLLMic`, `Tu2026Cottontail`.

### LLM For Fuzzing And Dynamic Analysis

LLMs are valuable where fuzzers struggle with semantics: grammar-like inputs, protocol states, API usage, harnesses, option combinations, sink reachability, and device-specific behavior. Fuzz4All and FuzzGPT show broad input generation. ProphetFuzz mines documentation. HyLLfuzz, ConcoLLMic, Cottontail, GONDAR, and PILOT attack hard constraints. FirmAgent, PANGOLIN, BSFuzzer, ProtocolGuard, IoTBec, and LogicFuzz are domain-specific systems where fuzzing provides the concrete oracle and the LLM provides semantic guidance.

Key reads: `Xia2024Fuzz4All`, `Wang2024ProphetFuzz`, `Yang2025HyLLFuzz`, `Fleischer2026GONDAR`, `Ji2026FirmAgent`, `Jia2026PANGOLIN`, `Yang2026BSFuzzer`, `Song2026ProtocolGuard`.

### LLM For Vulnerability Detection And Reasoning

The mature lesson is negative as much as positive. Standalone LLM vulnerability detectors are brittle, while structured hybrids are improving. `Steenhoek2024LLMsCannot`, `Lin2025FromLargeToMammoth`, and `Xu2025SVTrustEvalC` should be read before claims-heavy detector papers. Then read IRIS, LLMxCPG, LATTE, SpecAuditor, and domain-specific systems.

Key reads: `Steenhoek2024LLMsCannot`, `Lin2025FromLargeToMammoth`, `Xu2025SVTrustEvalC`, `Li2024IRIS`, `Lekssays2025LLMxCPG`.

### LLM For Repair, Backporting, And Patch Validation

Repair papers are promising but must be read through a validation lens. Zero-shot repair establishes a weak baseline. APPATCH and SAN2PATCH show that vulnerability semantics and sanitizer logs improve repair. PORTGPT moves to backporting, where Git history, compiler feedback, branch divergence, and regression risk matter.

Key reads: `Pearce2024ZeroShotRepair`, `Nong2025APPATCH`, `Kim2025SAN2PATCH`, `Li2026PORTGPT`, plus AIxCC systems.

### LLM For CTF, Pentesting, And Cyber Agents

PentestGPT remains a useful architecture paper because it identifies subtask competence and long-context failure. Cybench, NYU CTF Bench, CTFKnow/CTFAgent, CyberSecEval, ExploitBench, and CyberGym show benchmark maturation. The key shift is from "can a model answer cyber questions?" to "can an agent safely act, observe, recover, and produce evidence in a controlled environment?"

Key reads: `Deng2024PentestGPT`, `Zhang2024Cybench`, `Chen2025CTFKnow`, `Bhatt2024CyberSecEval3`, `Patel2026ExploitBench`.

### LLM For Reverse Engineering And Binary Analysis

Reverse engineering work clusters around explanation, symbol recovery, taint, decompilation readability, analyst workflows, and agent failure modes. DeGPT, ReSym, LATTE, RACONTEUR, FidelityGPT, IR representation studies, JsDeObsBench, human-LLM SRE studies, and LLM-resistant protection work are the core cluster. The open problem is evaluation: exact-match metrics do not capture whether analysts actually become faster and more accurate, or whether protections fail differently against humans and agents.

Key reads: `Hu2024DeGPT`, `Xie2024ReSym`, `Zhou2025LATTE`, `Deng2025Raconteur`, `Li2026FidelityGPT`, `Wei2025JsDeObsBench`, `Doupe2026HumanLLMSRE`, `Nishizaka2026LLMResistantProtection`.

### LLM App, Agent, And Security-Tool Attack Surfaces

LLM-based security tools create their own vulnerabilities. CodeBreaker poisons code completion. Flashboom and Trust Me attack LLM auditors. Package hallucinations create supply-chain risk. LLMSmith analyzes RCE risks in LLM-integrated apps. IsolateGPT, AgentDoS, agent-permission work, WebCloak, PLeak, and RAG poisoning defenses show that secure orchestration is now part of software-security research.

Key reads: `Yan2024CodeBreaker`, `Liu2025Flashboom`, `Xu2026TrustMe`, `Spracklen2025PackageHallucinations`, `Liu2024LLMSmith`, `Zhang2025IsolateGPT`, `Luo2026AgentDoS`, `Wu2026AgentPermissions`.

### Benchmarks, Datasets, And Evaluation Platforms

The benchmark frontier is moving toward multi-file repositories, real vulnerabilities, dynamic oracles, CTF environments, semantic perturbations, and role-specific evaluation. Weak benchmarks ask for labels on obvious snippets. Strong benchmarks force the agent to reproduce, reach, patch, or justify a vulnerability under a deterministic oracle.

Key reads: `Jimenez2024SWEBench`, `Zhang2024Cybench`, `Xu2025SVTrustEvalC`, `Wang2024SeCodePLT`, `Zhou2025SafeGenBench`, `Ali2025SecureVibeBench`, `Shao2025CyberGym`, `Patel2026ExploitBench`.

### Surveys And Systematization

Use surveys to orient, not to decide technical bets. The most useful surveys are `Sheng2025LLMSoftwareSecuritySurvey`, `Zhu2025SoftwareSecuritySurvey`, `Fan2025LLMSupplyChainAgenda`, and `SoK2026AIxCC`. PHILTER is adjacent but useful as an example of LLM-assisted systematic literature review with expert validation.

## Highlighted Promising Directions

### Verified LLM + Program Analysis Loops

Most credible systems no longer ask the model to be right by itself. They use the model to produce a hypothesis and then check it. IRIS, LLMxCPG, LATTE, SpecAuditor, ProtocolGuard, ConcoLLMic, Cottontail, DNS LLM-guided analysis, and FirmAgent all instantiate this pattern.

Promising research question: how can an LLM propose source/sink specs, protocol rules, path summaries, audit predicates, or harnesses while a verifier records which parts were actually checked?

### LLM-Assisted Fuzzing And Harness Generation

Harnesses, structured inputs, and semantic states remain bottlenecks in fuzzing. Fuzz4All, ProphetFuzz, Prompt Fuzzing, PromeFuzz, deepSURF, PILOT, HyLLfuzz, FirmAgent, PANGOLIN, BSFuzzer, ProtocolGuard, IoTBec, and LogicFuzz show strong momentum.

Promising research question: how can fuzzing pipelines use LLMs to generate semantically valid inputs while keeping reproducibility, deduplication, and false-positive control?

### Vulnerability Exploration And Exploitability Triage

Defensive teams need the middle layer between "bug found" and "weaponized exploit": reachability, preconditions, affected configurations, mitigations, likelihood under deployed defenses, and patch priority. FirmAgent, ProtocolGuard, GONDAR, IRIS, LLMxCPG, CyberGym, AIxCC systems, and PoC-generation studies all touch this space.

Promising research question: can an LLM-assisted system produce a bounded, reproducible evidence chain for exploitability without becoming an uncontrolled exploit generator?

### Patch Validation And Secure Backporting

The hard problem is not producing a patch-shaped diff. It is proving that the diff fixes root cause, preserves behavior, does not hide the symptom, and can be backported safely. APPATCH, SAN2PATCH, PORTGPT, SWE-bench/SWE-agent, SecureVibeBench, and AIxCC systems make this a strong 2026 direction.

Promising research question: can sanitizer replay, differential tests, static checks, generated regression tests, and patch-minimality constraints catch plausible-but-wrong LLM patches?

### Reverse Engineering And Deobfuscation Assistance

DeGPT, ReSym, LATTE, Raconteur, JsDeObsBench, FidelityGPT, human-LLM SRE studies, LLM-resistant protection work, and IR-representation studies show that LLMs are useful for analyst-facing understanding tasks and that agent failure modes deserve first-class evaluation.

Promising research question: what interaction patterns measurably improve analyst speed and accuracy on binaries, scripts, malware, and stripped/obfuscated code, and which protections reliably create evidence-preserving failure modes for LLM agents?

### Secure Orchestration For Cyber Reasoning Systems

AIxCC shifted attention from single tools to cyber reasoning systems. ATLANTIS, FuzzingBrain, OSS-CRS, IsolateGPT, AgentDoS, AI-agent permission work, and WebCloak show that orchestration is security-critical.

Promising research question: what permission model, sandbox design, logging schema, cost budget, and evidence ledger should a CRS use when it runs fuzzers, shells, package managers, browsers, and patching tools?

### Robustness And Evasion Of LLM Vulnerability Detectors

Flashboom, Trust Me, SV-TrustEval-C, detector-evasion preprints, and From Large to Mammoth all indicate that LLM security tools are vulnerable to prompt/context/code transformations. Detector evaluation must include semantics-preserving rewrites, misleading abstractions, obfuscation, and paired vulnerable/patched variants.

Promising research question: can vulnerability detectors be stable under refactoring, renaming, decomposition, dead-code insertion, misleading helper functions, and benign-looking abstraction layers?

### RAG And Supply-Chain Security For Coding Assistants

Package hallucinations, CodeGuarder, LLM supply-chain agenda work, CodeBreaker, PLeak, and LLMSmith show that coding assistants connect model failure modes with package ecosystems, retrieval corpora, and tool execution.

Promising research question: can a coding assistant prove that retrieved examples, package names, and generated dependencies are authentic, non-poisoned, and policy-compliant before suggesting executable code?

## General Reader Summary

Researchers are trying to use LLMs to make software security work faster and broader: finding vulnerabilities, explaining suspicious code, creating fuzzing inputs, generating test harnesses, drafting patches, backporting fixes, and helping security analysts operate tools. The early hope was that a strong model could read code and directly answer whether it was vulnerable. The evidence now says that is unreliable.

What works better is a hybrid system. Static analysis knows program structure but often lacks semantic rules. Fuzzing gives concrete crashes but struggles to reach deep states. Symbolic and concolic execution reason about paths but often need environment models and constraint solvers. LLMs are useful where humans usually write glue: identifying likely sources and sinks, interpreting documentation, naming decompiled variables, drafting harnesses, describing shell commands, proposing patches, or suggesting path constraints.

What fails is treating the model as an oracle. LLMs can hallucinate packages, miss small bugs, over-trust misleading helper names, be distracted by irrelevant code, produce plausible but wrong patches, and lose context in long workflows. They also create new attack surfaces when connected to tools: prompt leakage, RCE in LLM apps, resource-exhaustion in agents, unsafe package suggestions, and poisoned retrieval.

The field is shifting toward systems that produce evidence. A credible LLM-assisted security tool should not just say "this is vulnerable"; it should show the path, reproduce the crash, run a checker, validate the patch, log tool calls, and preserve enough context for a human to audit the result.

## Top-Venue Promising-Direction Synthesis

Top security and SE venues are converging on the same architecture: LLMs are semantic adapters inside verified loops.

The strongest vulnerability-detection cluster is neuro-symbolic and graph-guided. IRIS and LLMxCPG use LLMs to infer or select analysis-relevant semantics, but they lean on static-analysis structure to avoid feeding whole repositories into a model. LATTE applies the same idea to binary taint analysis. SpecAuditor suggests that audit-spec generation itself is becoming a core abstraction.

The strongest fuzzing cluster uses LLMs to cross semantic barriers. Fuzz4All and FuzzGPT showed that models can generate unusual and structured programs. ProphetFuzz, HyLLfuzz, PILOT, Cottontail, deepSURF, FirmAgent, PANGOLIN, BSFuzzer, ProtocolGuard, IoTBec, and LogicFuzz show the next step: use LLMs only where random mutation, grammars, or symbolic constraints hit semantic walls, then verify with execution.

The strongest repair cluster is validation-oriented. Zero-shot repair is a weak baseline; APPATCH and SAN2PATCH improve by adding vulnerability semantics and sanitizer logs. PORTGPT raises the bar by addressing backporting, where correctness depends on branch-specific context and compiler/build feedback. AIxCC systems reinforce the lesson: patching without reproducible validation is not enough.

The strongest agent/security-tool cluster treats the assistant itself as attack surface. CodeBreaker, Flashboom, Trust Me, package hallucination studies, LLMSmith, IsolateGPT, AgentDoS, AI-agent permission work, and WebCloak show that LLM-assisted security systems need conventional security engineering plus model-specific defenses. Mature work in this space will likely look more like systems security than prompt engineering.

Speculative but important frontier work is AIxCC-style CRS. ATLANTIS, FuzzingBrain, OSS-CRS, and the AIxCC SoK suggest a future where fuzzing, static analysis, symbolic execution, LLM reasoning, patch generation, validation, and reporting are orchestrated as one pipeline. The most publishable questions are not "which model wins?" but "which architecture reliably produces auditable evidence and safe patches under realistic cost, isolation, and disclosure constraints?"

## AIxCC And End-To-End Security Delivery

AIxCC is the strongest public contest signal for end-to-end LLM-assisted software security. DARPA reported Team Atlanta as the 2025 final winner, but the larger lesson is architectural: the leading systems were not pure chat agents. They were cyber reasoning systems that combined fuzzing, static analysis, symbolic or directed analysis, LLM planning, patch generation, validation, and report production.

The repeatable pattern is:

- fuzzing provides concrete reachability and crash evidence;
- static analysis and slicing identify candidate code regions and prune search;
- symbolic, concolic, or path-guided components reason about hard-to-reach states;
- LLMs interpret code, docs, traces, sinks, failures, and patch intent;
- validation loops reproduce bugs and check candidate fixes;
- the CRS produces maintainer-facing evidence, not just a vulnerability label.

Key follow-up readings: `Kim2025ATLANTIS`, `Sheng2025FuzzingBrain`, `Team2026OSSCRS`, `SoK2026AIxCC`, and `Fleischer2026GONDAR`.

Research implication: end-to-end security delivery is becoming a systems problem. Strong work should show orchestration design, evidence quality, patch validation, responsible-disclosure handling, and maintainability rather than only model accuracy.

## Three-Tier Reading Plan

### Tier 1: Foundations And Reality Checks

Read these first to avoid overestimating LLMs:

- `Jimenez2024SWEBench`
- `Yang2024SWEAgent`
- `Steenhoek2024LLMsCannot`
- `Lin2025FromLargeToMammoth`
- `Xu2025SVTrustEvalC`
- `Bhatt2024CyberSecEval2`
- `Zhang2024Cybench`

### Tier 2: Core Hybrid Methods

Read these to understand the strongest technical pattern:

- `Li2024IRIS`
- `Lekssays2025LLMxCPG`
- `Zhou2025LATTE`
- `Xia2024Fuzz4All`
- `Yang2025HyLLFuzz`
- `Fleischer2026GONDAR`
- `Ji2026FirmAgent`
- `Yang2026BSFuzzer`
- `Song2026ProtocolGuard`
- `Luo2026ConcoLLMic`
- `Tu2026Cottontail`

### Tier 3: Frontier Systems And Attack Surfaces

Read these once the hybrid pattern is clear:

- `Nong2025APPATCH`
- `Kim2025SAN2PATCH`
- `Li2026PORTGPT`
- `Kim2025ATLANTIS`
- `Sheng2025FuzzingBrain`
- `SoK2026AIxCC`
- `Yan2024CodeBreaker`
- `Liu2025Flashboom`
- `Xu2026TrustMe`
- `Spracklen2025PackageHallucinations`
- `Luo2026AgentDoS`
- `Wu2026AgentPermissions`
- `Doupe2026HumanLLMSRE`
- `Nishizaka2026LLMResistantProtection`
