---
ai-generated: true
---

# Academic Status: LLMs For Software Security, Program Analysis, Fuzzing, And Cyber Reasoning

Date: 2026-06-06

Home: [LLM-Software-Security-Research-Dossier-2026.md](../LLM-Software-Security-Research-Dossier-2026.md)

This is the compact research-status hub for the dossier. Detailed paper lists live in the area files below; this file keeps the scope, current field analysis, research directions, evaluation anchors, reading order, and source log.

## Scope And Labels

Included work is from 2024-present, checked on 2026-06-06. It must directly touch at least one of: LLMs for code/software engineering, program analysis, fuzzing, vulnerability detection/localization/triage/repair, reverse engineering, CTF/pentesting/cyber agents, cyber reasoning systems, or security of LLM-based coding/security tools.

Venue/source scope:

- Security: IEEE S&P, USENIX Security, ACM CCS, NDSS.
- SE: ICSE, ESEC/FSE and FSE/PACMSE, ASE, ISSTA.
- PL: POPL, PLDI, OOPSLA, ICFP, primarily through PACMPL and relevant DBLP venue pages.
- AI: NeurIPS, ICML, ICLR, AAAI.
- Frontier preprints: targeted arXiv sweep across `cs.CR`, `cs.SE`, `cs.PL`, `cs.AI`, `cs.LG`, and `cs.CL`.

Labels:

- `Core`: central to LLM + software/security research and backed by strong venue/source confidence.
- `Frontier`: promising recent preprint or newly accepted paper that needs follow-up verification.
- `Adjacent`: useful context, but not a central software-security method paper.
- `Survey`: broad mapping, SoK, roadmap, or systematic review.
- `Negative/Evaluation`: limits, failure modes, benchmarks, or meta-evaluation.

Metadata note: accepted 2026 papers use official accepted-paper/program pages where available. arXiv-only and newly accepted papers may have incomplete DOI/page metadata; their labels reflect role and confidence in the area files.

## Current Status

The main shift is from prompt-only LLM use to hybrid, evidence-producing systems. Strong 2025-2026 work combines LLMs with CPGs, taint flows, sanitizer logs, fuzzing traces, execution feedback, API specifications, protocol documents, tests, and patch validators. LLMxCPG, IRIS, LATTE, FirmAgent, PANGOLIN, BSFuzzer, HyLLfuzz, ProtocolGuard, and AIxCC-style systems all point to the same pattern: LLMs are useful as semantic components inside analysis systems, not as standalone oracles.

LLMs are most useful as "semantic glue." They infer likely sources/sinks, interpret API or protocol documentation, summarize decompiled artifacts, generate fuzzing harnesses or structured inputs, explain shell commands, propose path constraints, and draft patches. Traditional tools then check reachability, flows, crashes, regressions, or patch behavior.

The hardest open problem is whole-system grounding. Real tasks require multi-file context, build/test execution, issue interpretation, dependency reasoning, long-horizon state, and noisy ground truth. Vulnerability analysis is harder than ordinary code repair because the system must distinguish vulnerable, patched, unreachable, and functionally broken variants.

Benchmarks are improving, but evaluation is still fragile. The field is moving from toy snippets toward real repositories, validated vulnerabilities, dynamic oracles, CTF environments, semantic perturbations, and role-specific tasks. Remaining risks include contamination, patch-equivalence ambiguity, exploitability validation, weak generated tests, and LLM-as-judge leakage.

LLM-based security tools are now security targets. Code auditors, coding assistants, RAG systems, MCP/tool interfaces, code agents, package suggestions, and execution environments create attack surfaces: biased audits, backdoored code completion, package hallucinations, prompt leakage, RCE/file risks, poisoned retrieval, over-privileged tools, and agent resource exhaustion.

Patch generation is promising but not enough. APPATCH, SAN2PATCH, PORTGPT, PATCHAGENT, and AIxCC systems show progress, but the key research problem is validating that a patch fixes root cause, preserves behavior, avoids new vulnerabilities, and can be backported under branch drift.

Cyber agents are orchestration problems. PentestGPT, CTF benchmarks, SOC/CTI work, and CRS systems show that progress depends less on raw model choice and more on tool boundaries, isolation, logging, resource governance, memory, environment grounding, and reliable stopping criteria.

Plain summary: the early hope was that a strong model could read code and directly answer whether it was vulnerable. The evidence says that is unreliable. What works better is a verified loop: LLMs propose semantics, tests, harnesses, patches, or explanations; analyzers, fuzzers, execution, and humans check the result.

## Research Directions

| Direction | Core Question | Why It Matters |
| --- | --- | --- |
| Verified LLM + program analysis loops | Can an LLM propose specs, summaries, sources/sinks, path constraints, audit rules, or harnesses while analyzers record what was actually checked? | Best aligned with IRIS, LLMxCPG, LATTE, SpecAuditor, ProtocolGuard, ConcoLLMic, Cottontail, and GONDAR. |
| Vulnerability causality benchmarks | Can benchmarks distinguish vulnerable, patched, unreachable, refactored, and behavior-preserving variants? | Responds to SV-TrustEval-C, Flashboom, Trust Me, detector-evasion work, and benchmark contamination concerns. |
| Exploitability and triage | Can a system move from candidate bug to reachability, preconditions, mitigation, and priority without unsafe autonomy? | Fills the defensive gap between "bug found" and "weaponized exploit." |
| Patch validation and backporting | Can sanitizer replay, generated tests, differential execution, static checks, and patch-minimality constraints catch plausible-but-wrong fixes? | Directly follows APPATCH, SAN2PATCH, PORTGPT, PATCHAGENT, and AIxCC. |
| Fuzzing and harness synthesis | Can LLMs generate semantically valid inputs, drivers, option combinations, and state transitions while fuzzers keep the oracle concrete? | Strong after Fuzz4All, ProphetFuzz, PromeFuzz, deepSURF, PILOT, HyLLfuzz, FirmAgent, PANGOLIN, BSFuzzer, and LogicFuzz. |
| Domain-specific semantic bridges | Which domains have formal structure but expensive expert annotations? | High-value targets include IoT firmware, BLE/PLC/DNS protocols, Java APIs, unsafe Rust/C++, binaries, smart contracts, shell commands, and package ecosystems. |
| Reverse-engineering assistance | What interaction patterns improve analyst speed, accuracy, and confidence on binaries, scripts, malware, and stripped/obfuscated code? | Exact-match metrics miss analyst usefulness; DeGPT, ReSym, LATTE, Raconteur, JsDeObsBench, FidelityGPT, and human-LLM SRE work point here. |
| Secure cyber-agent orchestration | What permission model, sandbox, evidence ledger, audit trail, and cost budget should agents use when running fuzzers, shells, package managers, browsers, and patching tools? | Turns AIxCC-style CRS work into a systems-security problem. |
| RAG and supply-chain security | Can assistants prove retrieved examples, package names, and generated dependencies are authentic, non-poisoned, and policy-compliant? | Connects CodeBreaker, package hallucination, CodeGuarder, ImportSnare, LLMSmith, PLeak, and RAG poisoning work. |

## Method Patterns And Weak Baselines

| Pattern | Good Use | Representative Signals |
| --- | --- | --- |
| LLM as specification miner | Extract or contextualize sources, sinks, API rules, protocol rules, vulnerability patterns, or audit predicates. | IRIS, LLMxCPG, LATTE, GONDAR, ProtocolGuard, SpecAuditor. |
| LLM as harness/input generator | Draft fuzz drivers, structured inputs, valid option combinations, and target-specific generators. | Fuzz4All, ProphetFuzz, PromeFuzz, deepSURF, PILOT, HyLLfuzz. |
| LLM as taint/source/sink assistant | Fill semantic gaps while static, dynamic, or symbolic tools verify flows. | IRIS, LATTE, GONDAR, STaint, Artemis. |
| LLM as repair/backporting agent | Propose candidate fixes while tests, sanitizers, diff checks, and build feedback validate. | APPATCH, SAN2PATCH, PORTGPT, PATCHAGENT, Mystique. |
| LLM as reverse-engineering assistant | Rename, summarize, deobfuscate, explain, and help analysts inspect artifacts. | DeGPT, ReSym, LATTE, Raconteur, FidelityGPT, JsDeObsBench. |
| LLM as CRS component | Orchestrate fuzzing, analysis, symbolic/concolic execution, patching, validation, and reporting. | ATLANTIS, FuzzingBrain, OSS-CRS, AIxCC SoK. |

Saturated or weak baselines:

- zero-shot "is this vulnerable?" classification on isolated functions;
- prompt-only secure code generation without execution tests;
- LLM-as-a-judge evaluation without an independent oracle;
- small synthetic benchmarks where labels are obvious from CWE keywords;
- autonomous pentesting claims without environment control, logging, and reproducibility.

## Evaluation Anchors

| Benchmark | Main Use |
| --- | --- |
| [SWE-bench](https://www.swebench.com/) / [SWE-Bench+](https://arxiv.org/abs/2410.06992) | Repository-level issue resolution and test-suite-quality warnings. |
| [SWT-Bench](https://dblp.org/rec/conf/nips/MundlerMHV24) | Real-world bug-fix validation with code agents. |
| [CyberSecEval 2](https://arxiv.org/abs/2404.13161) / [CyberSecEval 3](https://arxiv.org/abs/2408.01605) | Broad cyber-risk and capability evaluation. |
| [NYU CTF Bench](https://dblp.org/rec/conf/nips/ShaoJUDxM0YGKKK24) / [Cybench](https://arxiv.org/abs/2408.08926) / [CTFKnow](https://arxiv.org/abs/2506.17644) | CTF/cybersecurity task solving and knowledge-vs-grounded-action separation. |
| [SV-TrustEval-C](https://dblp.org/rec/conf/sp/LiBHMKJJ25) | Structure and semantic reasoning for source-code vulnerability analysis. |
| [SeCodePLT](https://arxiv.org/abs/2410.11096) / [SafeGenBench](https://arxiv.org/abs/2506.05692) | Secure-code-generation and generated-code vulnerability evaluation. |
| [SecureVibeBench](https://arxiv.org/abs/2509.22097) | Multi-file secure coding tasks with functional and security oracles. |
| [CyberGym](https://arxiv.org/abs/2506.02548) | Real vulnerabilities across large codebases. |
| [ExploitBench](https://arxiv.org/abs/2605.14153) | Capability-ladder evaluation for exploit agents. |

Strong benchmarks force a model or agent to reproduce, reach, patch, or justify a vulnerability under a deterministic oracle. Weak benchmarks ask only for labels on obvious snippets.

## AIxCC And End-To-End Delivery

AIxCC is the strongest public signal for end-to-end LLM-assisted software security. DARPA reported Team Atlanta as the 2025 final winner, but the larger lesson is architectural: leading systems were cyber reasoning systems, not pure chat agents.

The repeatable CRS pattern is:

- fuzzing provides reachability and crash evidence;
- static analysis and slicing identify candidate regions and prune search;
- symbolic, concolic, or path-guided components reason about hard-to-reach states;
- LLMs interpret code, docs, traces, sinks, failures, and patch intent;
- validation loops reproduce bugs and check candidate fixes;
- reporting produces maintainer-facing evidence, not just vulnerability labels.

Key follow-up readings: `Kim2025ATLANTIS`, `Sheng2025FuzzingBrain`, `Team2026OSSCRS`, `SoK2026AIxCC`, and `Fleischer2026GONDAR`.

## Area Map

| Area | Why Read It | Key Reads | File |
| --- | --- | --- | --- |
| SE and code agents | Repo navigation, editing, tests, state management, and code-agent risk are prerequisites for security agents. | SWE-bench, SWE-agent, PORTGPT, SecureVibeBench, CyberGym. | [LLM-For-SE-And-Code-Agents.md](LLM-For-SE-And-Code-Agents.md) |
| Program analysis | The strongest pattern is LLM-as-specification-miner plus analyzer-as-verifier. | IRIS, LLMxCPG, LATTE, GONDAR, SpecAuditor, ConcoLLMic, Cottontail. | [LLM-For-Program-Analysis.md](LLM-For-Program-Analysis.md) |
| Fuzzing and dynamic analysis | LLMs help cross semantic barriers in inputs, harnesses, protocols, and device behavior; execution remains the oracle. | Fuzz4All, ProphetFuzz, HyLLfuzz, FirmAgent, PANGOLIN, BSFuzzer, ProtocolGuard. | [LLM-For-Fuzzing-And-Dynamic-Analysis.md](LLM-For-Fuzzing-And-Dynamic-Analysis.md) |
| Vulnerability detection and reasoning | Read negative results before claims-heavy detector papers; structured hybrids are more credible. | LLMs Cannot Reliably..., From Large to Mammoth, SV-TrustEval-C, IRIS, LLMxCPG. | [LLM-For-Vulnerability-Detection-And-Reasoning.md](LLM-For-Vulnerability-Detection-And-Reasoning.md) |
| Repair and patch validation | Repair must be evaluated through root-cause, regression, and backporting risk. | Zero-shot repair, APPATCH, SAN2PATCH, PORTGPT, PATCHAGENT. | [LLM-For-Repair-And-Patch-Validation.md](LLM-For-Repair-And-Patch-Validation.md) |
| CTF, pentesting, and cyber agents | Agent success depends on safe action, observation, recovery, and evidence production. | PentestGPT, Cybench, CTFKnow, CyberSecEval, ExploitBench, AIxCC systems. | [LLM-For-CTF-Pentesting-And-Cyber-Agents.md](LLM-For-CTF-Pentesting-And-Cyber-Agents.md) |
| Reverse engineering and binary analysis | Analyst usefulness, deobfuscation, decompilation, and agent failure modes need better metrics. | DeGPT, ReSym, LATTE, Raconteur, FidelityGPT, JsDeObsBench, human-LLM SRE. | [LLM-For-Reverse-Engineering-And-Binary-Analysis.md](LLM-For-Reverse-Engineering-And-Binary-Analysis.md) |
| LLM app, agent, and tool attack surfaces | LLM-for-security systems inherit conventional software risks plus new tool/RAG/agent failures. | CodeBreaker, Flashboom, Trust Me, package hallucinations, LLMSmith, IsolateGPT, AgentDoS. | [LLM-App-Agent-And-Security-Tool-Attack-Surfaces.md](LLM-App-Agent-And-Security-Tool-Attack-Surfaces.md) |
| Benchmarks and evaluation | Tracks realistic code, security, CTF, agent, and reverse-engineering benchmarks. | SWE-bench, Cybench, SV-TrustEval-C, SeCodePLT, SafeGenBench, SecureVibeBench, ExploitBench. | [Benchmarks-Datasets-And-Evaluation.md](Benchmarks-Datasets-And-Evaluation.md) |
| Surveys and systematization | Good for orientation and source mining, not final evidence for technical claims. | LLM software-security surveys, LLM supply-chain agenda, AIxCC SoK, PHILTER. | [Surveys-And-Systematization.md](Surveys-And-Systematization.md) |

## Reading Order

1. Foundations and reality checks: `SWE-bench`, `SWE-agent`, `LLMs Cannot Reliably...`, `From Large to Mammoth`, `SV-TrustEval-C`, `CyberSecEval`, `Cybench`.
2. Hybrid analysis methods: `IRIS`, `LLMxCPG`, `LATTE`, `GONDAR`, `SpecAuditor`, `ConcoLLMic`, `Cottontail`.
3. Fuzzing and harness generation: `Fuzz4All`, `ProphetFuzz`, `PromeFuzz`, `HyLLfuzz`, `deepSURF`, `PILOT`, `FirmAgent`, `PANGOLIN`, `BSFuzzer`, `ProtocolGuard`.
4. Repair and CRS delivery: `ZeroShotRepair`, `APPATCH`, `SAN2PATCH`, `PORTGPT`, `PATCHAGENT`, `ATLANTIS`, `FuzzingBrain`, `OSS-CRS`, `AIxCC SoK`.
5. Attack surfaces and reverse engineering: `CodeBreaker`, `Flashboom`, `Trust Me`, package hallucination studies, `LLMSmith`, `IsolateGPT`, `AgentDoS`, `DeGPT`, `JsDeObsBench`, `Raconteur`.
6. Frontier arXiv: prioritize papers with new datasets, evidence-producing pipelines, MCP/agent-security models, or reproducible vulnerability validation.

## Source Log

DBLP was the main source for the focused venue set. The primary DBLP host was intermittently unavailable during the sweep, so the Trier mirror was used where needed.

- Security: [USENIX Security 2024](https://dblp.org/db/conf/uss/uss2024.html), [USENIX Security 2025](https://dblp.org/db/conf/uss/uss2025.html), [IEEE S&P 2024](https://dblp.org/db/conf/sp/sp2024.html), [IEEE S&P 2025](https://dblp.org/db/conf/sp/sp2025.html), [ACM CCS 2024](https://dblp.org/db/conf/ccs/ccs2024.html), [ACM CCS 2025](https://dblp.org/db/conf/ccs/ccs2025.html), [NDSS 2024](https://dblp.org/db/conf/ndss/ndss2024.html), [NDSS 2025](https://dblp.org/db/conf/ndss/ndss2025.html), [NDSS 2026](https://dblp.org/db/conf/ndss/ndss2026.html).
- SE: [ICSE 2024](https://dblp.org/db/conf/icse/icse2024.html), [ICSE 2025](https://dblp.org/db/conf/icse/icse2025.html), ESEC/FSE and FSE/PACMSE through PACMSE records, [PACMSE Volume 1](https://dblp.org/db/journals/pacmse/pacmse1.html), [PACMSE Volume 2](https://dblp.org/db/journals/pacmse/pacmse2.html), [PACMSE Volume 3](https://dblp.org/db/journals/pacmse/pacmse3.html), [ASE 2024](https://dblp.org/db/conf/kbse/ase2024.html), [ASE 2025](https://dblp.org/db/conf/kbse/ase2025.html), [ISSTA 2024](https://dblp.org/db/conf/issta/issta2024.html), [ISSTA 2025 Companion](https://dblp.org/db/conf/issta/issta2025c.html).
- PL: [PACMPL Volume 8](https://dblp.org/db/journals/pacmpl/pacmpl8.html), [PACMPL Volume 9](https://dblp.org/db/journals/pacmpl/pacmpl9.html), [PACMPL Volume 10](https://dblp.org/db/journals/pacmpl/pacmpl10.html), covering POPL/PLDI/ICFP/OOPSLA-era PACMPL publication, plus [PLDI 2024](https://dblp.org/db/conf/pldi/pldi2024.html) where needed for cross-checking.
- AI: [ICLR 2024](https://dblp.org/db/conf/iclr/iclr2024.html), [ICLR 2025](https://dblp.org/db/conf/iclr/iclr2025.html), [ICML 2024](https://dblp.org/db/conf/icml/icml2024.html), [ICML 2025](https://dblp.org/db/conf/icml/icml2025.html), [NeurIPS 2024](https://dblp.org/db/conf/nips/neurips2024.html), [AAAI 2024](https://dblp.org/db/conf/aaai/aaai2024.html), [AAAI 2025](https://dblp.org/db/conf/aaai/aaai2025.html), [AAAI 2026](https://dblp.org/db/conf/aaai/aaai2026.html).
- arXiv: official arXiv API, submitted-date filters from 2026-01-01 through 2026-06-06, keyword families for LLM/software security, vulnerability, fuzzing, program analysis, static analysis, cyber agents, code agents, MCP, and secure code generation.

## Thesis

The most promising direction is not "LLM replaces program analysis", but "LLM supplies hard-to-manualize semantic hypotheses inside a verified cyber reasoning loop that produces reproducible evidence, validated patches, and auditable decisions."
