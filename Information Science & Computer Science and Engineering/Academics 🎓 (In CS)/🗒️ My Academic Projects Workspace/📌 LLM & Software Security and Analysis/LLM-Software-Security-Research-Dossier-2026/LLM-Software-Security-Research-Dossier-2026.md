---
ai-generated: true
last-reviewed: 2026-07-30
---

# LLM-Software-Security-Research-Dossier-2026

Date: 2026-07-30

Scope: 2024-2026 research and field signals on LLMs for software security: program analysis evaluated with explicit security oracles, the vulnerability lifecycle, cyber operations, security of LLM-integrated software, and systems/OS security. Fuzzing, binary analysis, and reverse engineering are included only when the primary claim and evaluation concern vulnerabilities, malware, exploitability, protection, or another security property.

General LLM-for-code/software-engineering work is maintained in the sibling [LLM-Software-Research-Dossier-2026](../LLM-Software-Research-Dossier-2026/LLM-Software-Research-Dossier-2026.md), including generic [binary understanding, decompilation, and reverse engineering](../LLM-Software-Research-Dossier-2026/Academic-Status/Program-Understanding-Binary-Analysis-Decompilation-And-Reverse-Engineering.md). Non-security languages, runtimes, contracts, testing, observability, and lifecycle methods for LLM applications and agents belong in [Software for LLM Agent Systems Research Dossier](../Software-For-LLM-Agent-Systems-Research-Dossier-2026/Software-For-LLM-Agent-Systems-Research-Dossier-2026.md). This is a research and evaluation dossier; operational exploit instructions are intentionally out of scope.

## Executive Snapshot

The field has moved past "can an LLM find a bug?" The best 2025-2026 systems treat the LLM as a semantic component inside a checked evidence loop: static analysis supplies structure, fuzzers and tests supply concrete oracles, symbolic/concolic tools constrain paths, and the LLM fills hard-to-manualize gaps such as source/sink inference, harness drafting, protocol/spec interpretation, code summarization, and patch intent.

Current thesis: the strongest research direction is not "LLM replaces program analysis", but "LLM proposes semantic hypotheses inside a verified cyber-reasoning loop that produces reproducible evidence, validated patches, and auditable decisions."

Practical boundary as of 2026-07-30: frontier agents are useful in bounded cyber tasks, vulnerability discovery, triage, patching, CTFs, and controlled red-team studies. Public evidence still does not support treating them as reliable open-world operators against arbitrary hardened targets with active defenders.



## Dossier Map

- [Academic Status](Academic-Status/Academic-Status.md): taxonomy rules, field synthesis, reading plan, venue ledger, and the complete nested map.
  - [Security Analysis / Program Analysis](Academic-Status/Security-Analysis/Program-Analysis.md): static/taint/graph, symbolic/concolic, fuzzing/dynamic, and security-targeted binary/RE.
  - [Vulnerability Lifecycle / Detection And Triage](Academic-Status/Vulnerability-Lifecycle/Detection-Triage-And-Reasoning.md) and [Security Repair](Academic-Status/Vulnerability-Lifecycle/Security-Repair-And-Patch-Validation.md).
  - [Cyber Operations / Offensive](Academic-Status/Cyber-Operations/Offensive-CTF-And-Pentesting.md) and [Defensive SOC/CTI](Academic-Status/Cyber-Operations/Defensive-SOC-And-CTI.md).
  - [Security Of LLM Software / Coding And Supply Chain](Academic-Status/Security-Of-LLM-Software/Coding-Dependency-And-Supply-Chain.md) and [Apps, RAG, Agents, MCP](Academic-Status/Security-Of-LLM-Software/App-RAG-Agent-And-Tool-Runtimes.md).
  - [Systems And OS Security](Academic-Status/Systems-And-OS-Security/Systems-And-OS-Security.md).
  - [Security Benchmarks](Academic-Status/Cross-Cutting/Security-Benchmarks-And-Evaluation.md) and [Surveys/SoKs](Academic-Status/Cross-Cutting/Surveys-And-Systematization.md).
- [Human Factor](Human-Factor.md): human-AI collaboration, developer/SOC/reverse-engineering studies, country and sector map, and human-centered research questions.
- [Non-Academic Status](Non-Academic-Status.md): capability boundary, model reports, contests, threat-intelligence signals, policy guidance, and China-focused activity.
- [BibTeX Bibliography](LLM-Software-Security-Research-Dossier-2026.bib): citation support file for manuscript work.
- [Source Literature Sweep](../Assets/archive.md): archived source sweep folded into this decomposed dossier.



## Status Quo Panel

### Field Dashboard

| Layer                    | Current state                                                                                                                                                                                | Watch next                                                                                                                                                             |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Academic methods         | Hybrid systems dominate: LLM + CPG/taint/static analysis, LLM + fuzzing, LLM + concolic execution, LLM + sanitizer/test validation.                                                          | Whether 2026 systems such as PANGOLIN, SpecAuditor, PILOT, PORTGPT, and agentic concolic execution release reproducible artifacts and survive independent replication. |
| Evaluation               | Stronger benchmarks are moving toward real repositories, dynamic oracles, validated vulnerabilities, CTF ranges, and exploitability ladders.                                                 | Benchmark leakage, LLM-as-judge overuse, shallow snippet classification, and whether "agent" claims record executable evidence.                                        |
| Industry capability      | AIxCC, OSS-CRS, Google Big Sleep/CodeMender, HackerOne telemetry, and model-provider system cards show cyber agents entering real defensive workflows.                                       | The split between useful autonomous assistance and invalid-report flood, plus how vendors gate high-cyber capability access.                                           |
| Threat activity          | Provider and threat-intelligence reports show AI used beyond phishing: reconnaissance, malware/tooling support, vulnerability research, lateral movement support, and agentic orchestration. | Whether reported AI-enabled activity becomes independently reproducible and how MITRE/ATT&CK-style taxonomies adapt to agentic behavior.                               |
| People and organizations | The center of gravity spans security/SE/PL academia, AI labs, bug-bounty platforms, government evaluators, standards bodies, and CRS teams.                                                  | Cross-institution human factors: maintainer handoff, SOC trust calibration, approval fatigue, disclosure, and accountability.                                          |
| Geography                | The U.S. has the densest direct evidence base; China has strong benchmark, contest, model, and security-vendor activity; UK/EU/Australia contribute evaluation and human-factor signals.     | Bilingual and region-specific studies of secure coding, SOC workflows, reverse engineering, bug bounty, and governance.                                                |
|                          |                                                                                                                                                                                              |                                                                                                                                                                        |

### System View

```tikz
\begin{document}
\begin{tikzpicture}[
  box/.style={draw, rounded corners=2pt, align=center, minimum width=3.2cm, minimum height=0.85cm},
  core/.style={box, fill=blue!8},
  check/.style={box, fill=green!8},
  risk/.style={box, fill=red!8},
  actor/.style={box, fill=yellow!12},
  arr/.style={->, thick}
]
\node[core] (llm) at (0,0) {LLM semantic\\engine};
\node[check] (analysis) at (-4.2,0) {Static, taint, CPG,\\symbolic, concolic};
\node[check] (dynamic) at (4.2,0) {Fuzzers, tests,\\sanitizers, replay};
\node[check] (evidence) at (0,-1.7) {Evidence ledger:\\paths, crashes, PoCs, patches};
\node[actor] (humans) at (0,-3.4) {Humans and institutions:\\developers, SOC, maintainers, bounty, governance};
\node[risk] (attack) at (0,1.7) {Agent/tool/RAG/supply-chain\\attack surface};

\draw[arr] (analysis) -- (llm);
\draw[arr] (llm) -- (dynamic);
\draw[arr] (dynamic) -- (evidence);
\draw[arr] (analysis) -- (evidence);
\draw[arr] (evidence) -- (humans);
\draw[arr] (humans) -- (llm);
\draw[arr] (attack) -- (llm);
\draw[arr] (attack) -- (humans);
\end{tikzpicture}
\end{document}
```

### High-Value Research Directions

| Direction                                    | Research question                                                                                                                         | Evidence anchors                                                                                                                            |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Verified LLM + program analysis              | Can LLMs generate specs, summaries, path constraints, source/sink rules, or audit predicates while analyzers prove what was checked?      | IRIS, LLMxCPG, LATTE, SpecAuditor, ProtocolGuard, ConcoLLMic, Cottontail.                                                                   |
| Vulnerability causality benchmarks           | Can benchmarks distinguish vulnerable, patched, unreachable, refactored, and behavior-preserving variants?                                | SV-TrustEval-C, Flashboom, Trust Me, detector-evasion papers, SecureVibeBench.                                                              |
| Exploitability and triage                    | Can systems move from candidate bug to reachability, preconditions, mitigation, priority, and safe evidence without unsafe autonomy?      | CyberGym, ExploitBench, AIxCC, IRIS-style whole-repo reasoning.                                                                             |
| Fuzzing and harness generation               | Can LLMs infer valid structure, hidden interfaces, option combinations, and target-specific harnesses while execution remains the oracle? | ProphetFuzz, PromeFuzz, HyLLfuzz, KernelGPT, StepStone, R1-Fuzz, PANGOLIN, FirmAgent, BSFuzzer, PILOT.                                     |
| Patch validation and backporting             | Can generated patches be validated for root-cause repair, behavioral preservation, branch drift, and regression coverage?                 | APPATCH, SAN2PATCH, PORTGPT, PATCHAGENT, CodeMender, OSS-CRS.                                                                               |
| Secure cyber-agent orchestration             | What permission model, sandbox, evidence ledger, budget control, and audit trail should agents use when running security tools?           | AIxCC, OSS-CRS, NIST CAISI, Five Eyes guidance, AgentDoS, MCP/tool-security work.                                                           |
| Human-AI security workflows                  | How should tools calibrate trust for developers, SOC analysts, reverse engineers, maintainers, and bounty triagers?                       | Stanford/NYU/UCF secure-coding studies, CSIRO/eSentire SOC work, NDSS human-LLM reverse engineering, UCLA agent-human interaction security. |
| LLM app and coding-assistant attack surfaces | How should RAG, package suggestions, MCP/tool calls, prompts, telemetry, and generated dependencies be authenticated and constrained?     | CodeBreaker, package hallucination studies, LLMSmith, IsolateGPT, WebCloak, SAGA, PHILTER.                                                  |
| U.S.-China and multilingual comparison       | How do language, regulation, local models, platforms, contests, and disclosure norms change LLM-assisted security practice?               | CS-Eval, LiveSecBench, Tianwang Cup large-model track, Alibaba AI Security Challenge, U.S. user/SOC studies.                                |

### Important People, Groups, And Institutions To Track

| Cluster                          | People / groups                                                                                                                                                    | Why they matter                                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Cyber reasoning systems          | Team Atlanta / Taesoo Kim; Trail of Bits; Theori; Shellphish; 42-beyond-bug; all_you_need_is_a_fuzzing_brain; Lacrosse.                                            | AIxCC made CRS architectures the clearest public end-to-end signal for autonomous bug finding, patching, reporting, and evidence handoff. |
| Program analysis + LLM           | Mayur Naik, Ziyang Li, Saikat Dutta; QCRI/NJIT/MBZUAI LLMxCPG authors; SpecAuditor and concolic-execution teams.                                                   | They define the "LLM proposes, analyzer verifies" line that looks strongest academically.                                                 |
| Fuzzing + dynamic analysis       | KernelGPT, StepStone, R1-Fuzz, PANGOLIN, FirmAgent, BSFuzzer, ProtocolGuard, IoTBec, LogicFuzz, and Bulbasaur teams.                                             | Fuzzing gives the field executable oracles, not just model labels.                                                                        |
| Repair and patch validation      | APPATCH, SAN2PATCH, PORTGPT, PATCHAGENT, DISPATCH, PatchScope teams; Google DeepMind CodeMender.                                                                   | Patch generation is easy to fake and hard to validate; this cluster attacks the real bottleneck.                                          |
| Reverse engineering and binaries | Adam Doupe, Yan Shoshitaishvili, Ruoyu Wang, Tiffany Bao; Brendan Dolan-Gavitt; EURECOM and University of Padua collaborators.                                     | Reverse engineering is a strong test of explanation, hallucination, analyst trust, and binary-grounded reasoning.                         |
| Human factors                    | Stanford secure-coding line; NYU `Lost at C`; UCF SEAL; CSIRO Data61 and eSentire SOC studies; UCLA security/HCI; IT University of Copenhagen red-teaming work.    | The field needs evidence about people using these systems, not only benchmark scores.                                                     |
| AI labs and security units       | OpenAI Preparedness/Codex/Security; Anthropic Frontier Red Team and Project Glasswing; Google DeepMind, Project Zero, and GTIG; Microsoft Security Copilot/GitHub. | These groups reveal capability, access policy, threat telemetry, and productization before papers stabilize.                              |
| Evaluators and governance        | UK AISI, METR, NIST CAISI, DARPA/ARPA-H, OpenSSF, OWASP, Cloud Security Alliance, MITRE.                                                                           | They shape evaluation methodology, agent-security standards, disclosure norms, and enterprise adoption.                                   |
| China ecosystem                  | Tsinghua INSC, Fudan SSS/Whitzard-AI, SJTU LLMSE, UCAS/CAS security groups, Alibaba Security, CAICT, Tencent, Qi An Xin, 360, XCTF.                                | China has strong model, benchmark, contest, and vendor signals; public human-subject evidence is still a gap worth tracking.              |

## Search Taxonomy

- Security analysis: static/taint/CPG, security specifications, symbolic/concolic execution, security-directed fuzzing/dynamic analysis, security-targeted binary/RE, and malware.
- Vulnerability lifecycle: detection reliability, localization, reachability, reproduction, proof of vulnerability, patching, backporting, validation.
- Cyber operations: CTF and controlled pentesting; SOC, CTI, incident response, threat hunting, and executable security-rule generation.
- Security of LLM software: secure code generation, dependency/package supply chain, prompt/RAG/memory poisoning, app RCE, MCP/tool permissions, provenance, availability.
- Systems and OS security: kernels, drivers, firmware/devices, configuration hardening, security patching, isolation, TEE, and capability-controlled runtimes.
- Cross-cutting: security benchmarks, dynamic oracles, contamination, human factors, surveys, SoKs, and reproducibility.

Primary-home rule: every academic paper has one canonical table row based on its central contribution and evaluation oracle. A security venue, fuzzing method, binary representation, or reverse-engineering workflow does not establish security ownership without an explicit vulnerability, exploitability, malware, protection, privacy, policy, or verified-defense outcome. Cross-cutting and secondary topic views link to the canonical row/key instead of copying it.

## Reading Priority

1. Reality checks and security benchmarks: LLMs Cannot Reliably, Code Analysis: Do LLMs Really Do Their Job?, SV-TrustEval-C, Flashboom, CyberSecEval, Cybench, SecureVibeBench, CyberGym, ExploitBench.
2. Verified analysis: IRIS, LLMxCPG, KNighter, LATTE, SpecAuditor, Neo, ProtocolGuard, agentic concolic execution, and Cottontail.
3. Security fuzzing and OS evidence: ProphetFuzz, HyLLfuzz, KernelGPT, deepSURF, StepStone, R1-Fuzz, Bulbasaur, PANGOLIN, FirmAgent, and BugAuditor.
4. Repair and delivery: ZeroShotRepair, APPATCH, SAN2PATCH, PORTGPT, OSS-Fuzz agentic repair, INTENTFIX, PatchWeaver, and AIxCC/OSS-CRS systems.
5. Operations: PentestGPT, Incalmo, SOC collaboration, LogInject/context contamination, RulePilot, SIGMERGE, and AIOpsDoom.
6. Agent and tool security: CodeBreaker, package hallucination, LLMSmith, IsolateGPT, FragFuse, MATE, MCP toolchain, ThinkTrap, and agentic-AI SoK.
7. Human workflows: secure-coding user studies, SOC studies, reverse-engineering studies, AI red-team labor, approval fatigue, and maintainer handoff.

## Venue Coverage Ledger

| Field | Top venues used | Current coverage through 2026-07-30 |
| --- | --- | --- |
| Security | IEEE S&P, USENIX Security, ACM CCS, NDSS | Highest direct yield; 2026 official programs integrated and provisional metadata labeled. |
| Software Engineering | ICSE, FSE/PACMSE, ASE, ISSTA | Security-specific analysis, repair, review, fuzzing, and rule work retained; generic SE moved to sibling dossier. |
| Programming Languages | POPL, PLDI, OOPSLA, ICFP/PACMPL | Security-relevant taint, symbolic, formal, and repair papers retained. |
| Artificial Intelligence | NeurIPS, ICML, ICLR, AAAI | Security benchmarks, IRIS, cyber agents, and SecCodePRM retained. |
| Operating Systems | OSDI, SOSP, EuroSys, USENIX ATC, FAST; ASPLOS adjacent | SOSP 2025 KNighter is a direct match; OSDI/EuroSys/ATC/FAST yielded no direct canonical match; ASPLOS 2025 KernelGPT is retained as an adjacent-venue match. |

The detailed venue/source policy and links to the repository venue guides are in [Academic Status](Academic-Status/Academic-Status.md#venue-coverage-ledger).

## Automation Proposal For Keeping The Directory Current

This is a proposed next-round implementation, not executed in this cleanup.

Build a small local tracker under `Assets/status_tracker/` with four layers:

| Layer | Files | Role |
| --- | --- | --- |
| Source registry | `sources.yml`, `queries.yml`, `actors.yml` | Whitelisted venue pages, arXiv queries, DBLP/OpenAlex/Crossref endpoints, RSS feeds, model-provider blogs, government evaluators, Chinese-language query sets, people/group pages. |
| Collectors | `collect_arxiv.py`, `collect_venues.py`, `collect_industry.py`, `collect_people.py` | Fetch metadata and page diffs. Prefer primary sources; label secondary sources as watch-only. |
| Normalization | `normalize.py`, `score_signals.py`, `dedupe.py` | Convert records to JSONL, deduplicate by DOI/arXiv/title, assign confidence labels, classify area, detect new people/groups, and rank importance. |
| Rendering | `render_panel.py`, `render_bib.py`, `render_digest.py` | Update the status panel, add candidate BibTeX entries, generate weekly/monthly digests, and optionally render a TikZ/SVG overview. |

Suggested outputs:

- `Assets/status_tracker/data/papers.jsonl`
- `Assets/status_tracker/data/signals.jsonl`
- `Assets/status_tracker/data/actors.jsonl`
- `Assets/status_tracker/snapshots/status-YYYY-MM-DD.md`
- `Assets/status_tracker/generated/status-panel.md`
- `Assets/status_tracker/generated/watchlist-digest.md`

Update cadence:

- Daily light run: arXiv, RSS feeds, official blogs, AIxCC/OpenSSF/NIST/AISI/METR/HackerOne/Bugcrowd/provider updates.
- Weekly synthesis: venue pages, DBLP/OpenAlex/Crossref, new benchmark repos, GitHub releases, selected Chinese-language sources.
- Monthly deep sweep: manual review of important people/groups, country map, source-confidence labels, and bibliography cleanup.

Safety and quality rules:

- Never silently overwrite prose. Generate a candidate diff between markers such as `<!-- status-panel:start -->` and `<!-- status-panel:end -->`.
- Prefer official venue, paper, lab, government, provider, and platform sources. Use news/aggregators only as discovery leads.
- Store `source_url`, `checked_at`, `published_at`, `source_type`, `confidence`, `area`, `region`, and `why_it_matters` for every record.
- Keep dual-use summaries at research/evaluation level. Do not reproduce exploit steps, payloads, or operational instructions.
- Use an LLM only after structured collection and deduplication. Its job should be clustering, concise summarization, and proposed edits, not fact creation.
- Commit generated snapshots separately from hand-written synthesis so trends are auditable over time.

## Writing Workflow

Use the [Academic Writing Workflow scaffold](<../../_Academic Writing Workflow/README.md>) as the template, but keep active manuscript work inside the local LLM/software-security project directory.

Recommended local layout:

- `Writing/`: manuscript drafts.
- `References/library.bib`: bibliography source of truth, initialized from [LLM-Software-Security-Research-Dossier-2026.bib](LLM-Software-Security-Research-Dossier-2026.bib).
- `References/Paper Notes/`: one literature note per source.
- `References/PDFs/`: PDFs linked from literature notes.
- `CSL/`, `Templates/`, `Exports/`: citation styles, writing templates, and generated outputs.

Manuscript frontmatter should point from `Writing/` to `../References/library.bib` and the chosen CSL file. Use Pandoc citation syntax such as `[@Lekssays2025LLMxCPG; @Li2024IRIS]`.

## Current Source Anchors

Detailed source logs live in the linked academic, human-factor, and non-academic files. Current high-signal anchors checked for this top-level panel include:

- Academic venues: [USENIX Security 2026 technical program](https://www.usenix.org/conference/usenixsecurity26/technical-sessions), [IEEE S&P 2026 accepted papers](https://sp2026.ieee-security.org/accepted-papers.html), [USENIX Security 2025 LLMxCPG](https://www.usenix.org/conference/usenixsecurity25/presentation/lekssays), [IRIS arXiv](https://arxiv.org/abs/2405.17238).
- CRS and open-source infrastructure: [DARPA AIxCC final results](https://www.darpa.mil/news/2025/aixcc-results), [OpenSSF OSS-CRS](https://openssf.org/projects/oss-crs/), [OSS-CRS arXiv](https://arxiv.org/abs/2603.08566).
- Capability and governance: [UK AISI GPT-5.5 cyber evaluation](https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities), [UK AISI cyber time horizons](https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing), [METR Frontier Risk Report](https://metr.org/blog/2026-05-19-frontier-risk-report/), [NIST CAISI AI-agent RFI](https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems).
- Industry and threat intelligence: [OpenAI GPT-5.3-Codex System Card](https://openai.com/index/gpt-5-3-codex-system-card/), [OpenAI Cybersecurity in the Intelligence Age](https://openai.com/index/cybersecurity-in-the-intelligence-age/), [OpenAI Frontier Governance Framework](https://openai.com/index/openai-frontier-governance-framework/), [Anthropic AI-enabled cyber threats](https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack), [Google Cybersecurity Forecast 2026](https://cloud.google.com/blog/topics/threat-intelligence/cybersecurity-forecast-2026/), [Google DeepMind CodeMender](https://deepmind.google/en/blog/introducing-codemender-an-ai-agent-for-code-security/), [Google Project Zero Big Sleep](https://projectzero.google/2024/10/from-naptime-to-big-sleep.html), [HackerOne AI vulnerability report](https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy).

## Merge Note

The literature and official-program sweep was consolidated on 2026-07-30. The main file is the control panel; the nested academic taxonomy, human-factor, non-academic, bibliography, and archive files are the evidence shelves.
