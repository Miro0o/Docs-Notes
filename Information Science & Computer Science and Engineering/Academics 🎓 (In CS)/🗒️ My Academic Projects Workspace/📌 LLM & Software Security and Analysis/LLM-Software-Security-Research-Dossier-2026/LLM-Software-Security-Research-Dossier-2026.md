---
ai-generated: true
---

# LLMs For Software Security, Program Analysis, Fuzzing, And Cyber Reasoning

Date: 2026-06-06

Scope: curated 2024-2026 literature on LLMs in software engineering, program analysis, fuzzing, vulnerability detection, repair, reverse engineering, CTF/pentesting, cyber reasoning systems, and security risks introduced by LLM-based coding and security tools.

This dossier is written at research/evaluation level. Dual-use papers are included because they shape defensive evaluation, triage, vulnerability validation, and secure orchestration; operational exploit details are intentionally not reproduced.

## Dossier Map

- [Academic Status](Academic-Status/Academic-Status.md): peer-reviewed and preprint literature, method patterns, benchmarks, reading plan, and research gaps.
- [Human Factor](Human-Factor.md): human-AI collaboration, developer/SOC/reverse-engineering studies, country and sector map, and human-centered research questions.
- [Non-Academic Status](Non-Academic-Status.md): capability boundary, model reports, contests, threat-intelligence signals, policy guidance, and China-focused activity.
- [BibTeX Bibliography](LLM-Software-Security-Research-Dossier-2026.bib): citation support file moved with this dossier.
- [Source Literature Sweep](LLM-Software-Security-Literature-Sweep-2026-06-06.md): source sweep merged into this decomposed dossier.

## Academic Writing Workflow

Use the [Academic Writing Workflow scaffold](<../../_Academic Writing Workflow/README.md>) as a template, but keep the active manuscript workflow inside the local LLM/software-security project directory:

`Information Science & Computer Science and Engineering/Academics 🎓 (In CS)/🗒️ My Academic Projects Workspace/📌 LLM & Software Security and Analysis`

The project-local workflow should have this structure:

- `Writing/`: manuscript drafts.
- `References/library.bib`: project bibliography source of truth.
- `References/Paper Notes/`: one literature note per source.
- `References/PDFs/`: paper PDFs linked from literature notes.
- `Exports/`: generated PDF/DOCX exports.
- `CSL/`: citation styles such as `ieee.csl` and `apa.csl`.
- `Templates/`: copied manuscript and literature-note templates.

Initial setup from the project directory:

```sh
cd "Information Science & Computer Science and Engineering/Academics 🎓 (In CS)/🗒️ My Academic Projects Workspace/📌 LLM & Software Security and Analysis"

mkdir -p "Writing" "References/Paper Notes" "References/PDFs" "Exports" "CSL" "Templates"

cp "../_Academic Writing Workflow/Templates/manuscript.md" "Templates/manuscript.md"
cp "../_Academic Writing Workflow/Templates/literature-note.md" "Templates/literature-note.md"
cp "../_Academic Writing Workflow/CSL/ieee.csl" "CSL/ieee.csl"
cp "../_Academic Writing Workflow/CSL/apa.csl" "CSL/apa.csl"

cp "LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.bib" "References/library.bib"
cp "Templates/manuscript.md" "Writing/llm-software-security-manuscript.md"
```

Project manuscript frontmatter should stay relative to `Writing/`:

```yaml
---
title: LLMs for Software Security and Analysis
author:
bibliography: ../References/library.bib
csl: ../CSL/ieee.csl
link-citations: true
---
```

Use Pandoc citation syntax in the manuscript:

```md
LLMs are more reliable inside verified analysis loops than as standalone vulnerability oracles [@Lekssays2025LLMxCPG; @Li2024IRIS].
```

Export from `Writing/`:

```sh
cd "Information Science & Computer Science and Engineering/Academics 🎓 (In CS)/🗒️ My Academic Projects Workspace/📌 LLM & Software Security and Analysis/Writing"
pandoc llm-software-security-manuscript.md --citeproc -o ../Exports/llm-software-security-manuscript.pdf
```

Terminal export follows the local manuscript frontmatter. If exporting or completing citations from Obsidian plugin commands, repoint the plugin settings from `_Academic Writing Workflow/...` to this project-local `References/library.bib`, `CSL/ieee.csl`, `References/Paper Notes`, and `Exports`.

## Executive Summary

The field has moved past the simple question "can an LLM find a bug?" The strongest 2025-2026 work treats an LLM as a semantic component inside a larger evidence-producing system: static analysis supplies structure, fuzzers and test suites supply concrete oracles, taint/symbolic/concolic engines constrain reasoning, and the LLM fills gaps that used to require expert-written specifications or hand-built harnesses.

The dominant trend is hybridization. LLMxCPG, IRIS, LATTE, FirmAgent, PANGOLIN, BSFuzzer, ProtocolGuard, ConcoLLMic, Cottontail, PILOT, APPATCH, SAN2PATCH, PORTGPT, ATLANTIS, and FuzzingBrain all point in the same direction: LLMs are useful for semantic hypothesis generation, context summarization, source/sink inference, harness/input synthesis, path explanation, and patch drafting. They are much less reliable as standalone vulnerability oracles.

The main open problems are evaluation trustworthiness, whole-repository context management, exploitability and reachability triage, patch validation, secure agent orchestration, and robustness against adversarial code transformations, prompt/tool injection, package hallucination, and data/RAG poisoning. Mature evidence increasingly comes from top security and SE venues, while the most speculative frontier is AIxCC-style end-to-end cyber reasoning systems and agentic offensive-security benchmarks. Non-academic signals now matter too: government evaluations, model-provider system cards, bug-bounty telemetry, CTF results, and Chinese-language safety benchmarks often reveal frontier capability shifts months before papers appear.

As of 2026-06-06, the practical capability boundary is: frontier AI has crossed the threshold for useful autonomous cyber reasoning in bounded environments, including CTFs, vulnerability discovery, triage, patching, and some exploit construction, but it is not yet a reliable open-world operator against arbitrary hardened targets with active defenders.

## Updated One-Sentence Thesis

The most promising research direction is not "LLM replaces program analysis", but "LLM supplies hard-to-manualize semantic hypotheses inside a verified cyber reasoning loop that produces reproducible evidence, validated patches, and auditable decisions."

## Search Taxonomy From The Local Note

- LLM architecture and attention: especially attention behavior that affects vulnerability auditing, long context, code attention, and MoE/security behavior.
- LLM utilization: agents, loop design, orchestration, prompt/context/harness engineering, reasoning and acting, skills/tool use.
- LLM for SE: code generation, issue repair, repository-level coding agents, secure code generation.
- LLM for PL/program analysis: static analysis, taint analysis, symbolic execution, fuzzing, decompilation, code property graphs.
- LLM for CTF/pentesting: CTF benchmarks, autonomous pentesting systems, cyber skill benchmarks.
- LLM for vulnerabilities: detection, localization, triage, exploration, exploitability reasoning, PoC generation, patching.
- End-to-end security delivery: agentic cyber reasoning systems, AIxCC-style pipelines, SOC/vulnerability management, secure deployment of LLM-integrated apps.

## Merge Note

The 2026-06-06 literature sweep has been folded into this dossier. The academic file keeps the sweep's current-development synthesis, research gaps, benchmark table, method-pattern taxonomy, saturated-topic list, candidate-topic table, and updated reading priority. The original dossier's broader human-factors and non-academic signal sections are preserved in separate files.

## Source Log

Venue pages and official sources checked:

- USENIX Security 2024 presentation/session pages for PentestGPT, vulnerability management, code analysis, and CodeBreaker.
- USENIX Security 2025 paper pages for LLMxCPG, APPATCH, SAN2PATCH, package hallucinations, and HyLLfuzz.
- USENIX Security 2026 Cycle 1 accepted papers for PANGOLIN, AgentDoS, NOIR, and PHILTER.
- IEEE S&P 2024 accepted papers for zero-shot vulnerability repair and LLMIF.
- IEEE S&P 2025 accepted papers and linked PDFs/arXiv for Flashboom, SV-TrustEval-C, and cybersecurity-expert evaluation.
- IEEE S&P 2026 accepted papers for PORTGPT, Agentic Concolic Execution, PILOT, SpecAuditor, DNS LLM-guided analysis, agent permissions, WebCloak, and SOC study.
- NDSS 2024/2025/2026 paper and program pages for protocol fuzzing, DeGPT, IsolateGPT, Raconteur, From Large to Mammoth, FirmAgent, BSFuzzer, ProtocolGuard, IoTBec, LogicFuzz, Trust Me, FidelityGPT, human-LLM software reverse engineering, LLM-resistant reverse-engineering protections, and LLM-based decompilation work.
- ACM CCS 2024/2025 program/DBLP/arXiv pages for PromSec, ProphetFuzz, LiftFuzz, Prompt Fuzzing, LLMSmith, ReSym, PLeak, CodeGuarder, CTFKnow/CTFAgent, PromeFuzz, and JsDeObsBench.
- ICSE/ISSTA/ICLR/NeurIPS official or DOI pages for Fuzz4All, FuzzGPT, fuzz-driver evaluation, CoSec, SWE-bench, and SWE-agent.
- arXiv pages for CyberSecEval 2/3, Cybench, NYU CTF Bench, IRIS, SafeGenBench, SeCodePLT, SecureVibeBench, CKG-LLM, web PoC study, FuzzingBrain, ATLANTIS, OSS-CRS, AIxCC SoK, GONDAR, detector evasion, secure-code-generation robustness, ExploitBench, and CyberGym.
- Human-factors and socio-technical sources: Stanford and NYU secure-coding user studies; UCF SEAL and Paderborn developer-training/secure-prompting studies; CSIRO Data61 and eSentire live-SOC studies; USC ISI / USF / KU / Resideo practitioner-centered SOC work; EURECOM / ASU / Padua human-LLM software reverse-engineering work; UCLA agent-human interaction security; HAT-Lab agent-mediated deception; CHI 2026 dark-pattern GUI-agent oversight; PLOS ONE / IBM / CSCW AI red-teaming studies; IRT SystemX / Airbus Protect / RTE SOC human-AI collaboration; and official/group pages for UK AISI, LASR, PEASEC, MLSEC, CISPA, moosec, KASTEL, RESIST, Cybercampus Sverige, NTU, Data61, HASP Lab, and related national AI/cyber labs.
- Non-academic model/report/activity sources: UK AISI GPT-5.5 and cyber time-horizon reports; METR frontier-risk/time-horizon report; Anthropic Project Glasswing, Claude Mythos Preview red-team writeup, cyber competition writeup, and GTG-1002 threat-intelligence report; OpenAI GPT-5.5 Trusted Access for Cyber, GPT-5.5-Cyber, Daybreak, Codex Security, and malicious-use disruption reports; Google Project Zero Big Sleep, Google DeepMind CodeMender, Google AI VRP/SAIF 2.0, and GTIG AI Threat Tracker reports; ExploitBench and Bugcrowd commentary; HackerOne 2025 AI vulnerability report; DARPA AIxCC final results; OpenSSF OSS-CRS transition and CRS development materials; Palisade CTF elicitation and AI-agent experiment posts; Hack The Box MCP and AI red-teaming CTF materials; MITRE ATT&CK C0062; NIST CAISI AI-agent RFI; Five Eyes careful-adoption guidance for agentic AI.
- Chinese-language benchmark and contest sources: CS-Eval/CyberSec-Eval GitHub and platform pages; LiveSecBench; Tsinghua report on 2025 天网杯大模型赛道; Alibaba Cloud 2025 "AI安全" 全球挑战赛 and public contest result reports; 中国互联网协会 AI领航杯 "AI+安全" track; 金灵光杯 generative-AI security track; XCTF CVE-range platform; aggregator traces for CySecEval-53K pending primary-source verification.

Search query families used:

- `LLM vulnerability detection`, `LLM software security`, `LLM code auditor evasion`, `LLM vulnerability repair`, `LLM patch validation`, `LLM program analysis`, `LLM static analysis`, `LLM taint analysis`, `LLM concolic execution`, `LLM fuzzing`, `LLM fuzz harness generation`, `LLM protocol fuzzing`, `LLM IoT firmware fuzzing`, `LLM CTF benchmark`, `LLM pentesting`, `cyber reasoning system`, `AIxCC`, `LLM supply chain security`, `package hallucination`, `RAG code generation security`, and per-venue accepted-paper searches.
- Additional non-paper query families: `GPT-5.5 cyber evaluation`, `Claude Mythos Preview cybersecurity`, `Project Glasswing`, `AISI cyber time horizon`, `METR frontier risk cyber`, `OpenAI Daybreak`, `Codex Security`, `Google CodeMender`, `Big Sleep vulnerability`, `GTIG AI Threat Tracker`, `ExploitBench`, `HackerOne autonomous Hackbots`, `XBOW HackerOne leaderboard`, `AIxCC results`, `OSS-CRS OpenSSF`, `Hack The Box MCP CTF`, `AI-orchestrated cyber espionage`, `Gemini threat actor misuse`, `agentic AI guidance`, `大模型 网络安全 能力评测`, `网络安全大模型 榜单`, `大模型赛道 天网杯`, `AI安全 全球挑战赛`, `金灵光杯 人工智能安全`, `安全大模型 评测报告`, `大模型 攻防赛`, `AI生成漏洞 靶场`.
- Human-factors query families: `human factors LLM cybersecurity`, `human-AI collaboration cybersecurity`, `LLMs in the SOC`, `LLM SOC analyst study`, `LLM-assisted secure coding user study`, `secure prompting developer study`, `human-LLM reverse engineering`, `LLM agent security human approval`, `agent-mediated deception LLM`, `dark patterns GUI agents human oversight`, `LLM red teaming socio-technical`, `AI red teaming human factor`, `usable security LLM software security`, `human-centered cybersecurity LLM`, plus country-specific variants for the U.S., Canada, UK, Australia, France, Germany, Italy, Denmark, Sweden, Spain, China, Singapore, Japan, South Korea, India, Israel, UAE/Gulf, and New Zealand.

Local notes cross-checked:

- `Information Science & Computer Science and Engineering/Academics .../LLM & Software Security and Analysis.md`
- `Information Science & Computer Science and Engineering/Academics .../LLM & Fuzzing.md`
- `Information Science & Computer Science and Engineering/Academics .../LLM & Supply Chain Security.md`
- `Information Science & Computer Science and Engineering/Academics .../LLM-Software-Security-Literature-Sweep-2026-06-06.md`
