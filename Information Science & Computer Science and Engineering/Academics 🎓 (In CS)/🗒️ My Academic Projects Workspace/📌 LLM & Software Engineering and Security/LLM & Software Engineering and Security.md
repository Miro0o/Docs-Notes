---
last-reviewed: 2026-07-31
---

# LLM & Software Engineering and Security

[TOC]

## Research Dossiers

| Dossier | Canonical scope | Exclusion rule |
| --- | --- | --- |
| [LLM–Software Security Research Dossier 2026](Dossiers/LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md) | LLMs used for vulnerability discovery, security program analysis, fuzzing, exploitability/triage, security repair, cyber operations, and security of LLM-enabled software | General software quality, correctness, maintenance, and performance work belongs in the software dossier unless the evaluated objective is security |
| [LLM–Software Research Dossier 2026](Dossiers/LLM-Software-Research-Dossier-2026/LLM-Software-Research-Dossier-2026.md) | Code-specific model/data/adaptation/representation research, plus LLMs used to build, understand, review, test, debug, verify, maintain, migrate, and optimize software and systems | Security-goal papers belong in the security dossier; generic non-code model research and request-level serving are outside the three dossiers |
| [Software for LLM Agent Systems Research Dossier 2026](Dossiers/Software-For-LLM-Agent-Systems-Research-Dossier-2026/Software-For-LLM-Agent-Systems-Research-Dossier-2026.md) | Programming languages, software-engineering methods, and systems abstractions used to build, type, test, debug, observe, evolve, and operate LLM applications and agents | LLMs applied to ordinary software belong in the software dossier; security-first attacks and defenses belong in the security dossier; generic model training and request-level serving remain out of scope |

Classification rule: classify first by the direction of the research contribution, then by its evaluated outcome. Each paper has one canonical home; method and domain pages cross-link instead of copying the full record.

| Direction | Canonical home | Deciding test |
| --- | --- | --- |
| `code model/data/representation → software capability` | LLM–Software | Is the primary artifact code-specific training data, an adaptation recipe, a code model, or a learned code representation? |
| `LLM → ordinary software/code` | LLM–Software | Is the model helping produce, understand, test, verify, maintain, optimize, or operate non-security software? |
| `software/PL/systems → LLM applications and agents` | Software for LLM Agent Systems | Is the contribution a language, runtime, contract, harness, testing method, observability mechanism, or lifecycle method for LLM-enabled software? |
| either direction with a security outcome | LLM–Software Security | Is the primary claim evaluated through vulnerabilities, exploitability, malware, attack/defense, security policy, privacy, or validated security repair? |

Fuzzing, reverse engineering, agents, and systems are methods or domains, not automatic security labels. Their canonical home follows the primary claim and oracle.

## Shared 2024–Present Literature Snapshot

The [shared literature corpus](Dossiers/Literature-Corpus/README.md) freezes formal-venue coverage at **2026-07-31**. It contains every normalized record returned by the declared sources for the available cells in the defined 22-venue ledger, a screened formal bibliography, a separately labeled frontier-preprint bibliography, and reproducible screening and dossier-assignment tables. Pending programs and incomplete independent count reconciliation prevent an unconditional exhaustiveness claim.

- [Coverage counts](Dossiers/Literature-Corpus/coverage-counts.md) summarize every venue-year and mark unavailable 2026 programs as pending rather than zero.
- [Venue-year manifest](Dossiers/Literature-Corpus/venue-year-manifest.csv) records sources, status, expected and collected counts, discrepancies, retrieval dates, and unresolved metadata.
- [Screening decisions](Dossiers/Literature-Corpus/screening.csv) make every formal record auditable; unresolved high-recall candidates are visible rather than silently discarded.
- [Dossier mappings](Dossiers/Literature-Corpus/dossier-mapping.csv) resolve every included record to one canonical row in each applicable dossier. Cross-dossier overlap is allowed.
- [Build and validation scripts](Literature-Corpus/scripts/) reproduce the snapshot and enforce BibTeX, identity, mapping, manifest, and local-link invariants.

The frozen snapshot contains 50,727 deduplicated formal records and 1,172 screened formal records. Its two declared 2026 arXiv frontier queries produced 6,636 raw results with 1,077 cross-query overlaps and 5,558 normalized candidates. Conservative primary-object screening retains 1,522 query records and leaves 1,005 candidates unresolved; after cross-year preservation and identity deduplication, the screened frontier bibliography contains 1,539 records. Six 2026 venue-years are explicitly pending because no public archival program was available at the cutoff. The 3,163 dossier mappings are structurally materialized on real `Academic-Status` shelves, while manual screening and contribution-quality review remain incomplete.



## Res
### Related Topics
↗ [Mathematical Logic (Foundations of Mathematics)](../../../🧮%20Mathematics/🤼‍♀️%20Mathematical%20Logic%20(Foundations%20of%20Mathematics)/Mathematical%20Logic%20(Foundations%20of%20Mathematics).md)
- ↗ [Formal System, Formal Logics, and Its Semantics](../../../🧮%20Mathematics/🤼‍♀️%20Mathematical%20Logic%20(Foundations%20of%20Mathematics)/📍%20Formal%20System,%20Formal%20Logics,%20and%20Its%20Semantics/Formal%20System,%20Formal%20Logics,%20and%20Its%20Semantics.md)

↗ [Formal Verification (FV) & Reasoning Systems (Formal Methods)](../../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20Information%20Security%20(InfoSec)/🙇‍♂️%20Formal%20Verification%20(FV)%20&%20Reasoning%20Systems%20(Formal%20Methods)/Formal%20Verification%20(FV)%20&%20Reasoning%20Systems%20(Formal%20Methods).md)
- ↗ [Constraint Solving & Theorem Proving](../../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20Information%20Security%20(InfoSec)/🙇‍♂️%20Formal%20Verification%20(FV)%20&%20Reasoning%20Systems%20(Formal%20Methods)/🎮%20Constraint%20Solving%20&%20Theorem%20Proving/Constraint%20Solving%20&%20Theorem%20Proving.md)

↗ [Computer Languages & Programming Methodology](../../../🔑%20CS%20Core/👩‍💻%20Computer%20Languages%20&%20Programming%20Methodology/Computer%20Languages%20&%20Programming%20Methodology.md)
- ↗ [Programming Language Theory (PLT)](../../../🔑%20CS%20Core/👩‍💻%20Computer%20Languages%20&%20Programming%20Methodology/🐢%20Programming%20Language%20Theory%20(PLT)/Programming%20Language%20Theory%20(PLT).md)

↗ [Software (Program) Techniques & Binary Engineering](../../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20Information%20Security%20(InfoSec)/🍦%20Software%20Security/🪆%20Software%20(Program)%20Techniques%20&%20Binary%20Engineering/Software%20(Program)%20Techniques%20&%20Binary%20Engineering.md)
- ↗ [Program Analysis Basics](../../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20Information%20Security%20(InfoSec)/🍦%20Software%20Security/🪆%20Software%20(Program)%20Techniques%20&%20Binary%20Engineering/📌%20Program%20Analysis%20Basics/Program%20Analysis%20Basics.md)

↗ [Application Security](../../../CyberSecurity/Application%20Security/Application%20Security.md)
↗ [Network (& Communication) Security](../../../CyberSecurity/Network%20(&%20Communication)%20Security/Network%20(&%20Communication)%20Security.md)
↗ [System Security](../../../CyberSecurity/System%20Security/System%20Security.md)
↗ [Reverse & Pwn](../../../CyberSecurity/🏰%20Cybersecurity%20Basics%20&%20Information%20Security%20(InfoSec)/CTF%20&%20AWD/Reverse%20&%20Pwn/Reverse%20&%20Pwn.md)

↗ [Artificial Neural Networks (ANN) & Deep Learning Methods](../../../🧠%20Computing%20Methodologies/👽%20Artificial%20Intelligence/🗝️%20AI%20Basics%20&%20Major%20Techniques/🌌%20Knowledge%20Representation%20(Syntax%20Level)%20and%20Reasoning%20(KRR)/🌊%20Artificial%20Neural%20Networks%20(ANN)%20&%20Deep%20Learning%20Methods/Artificial%20Neural%20Networks%20(ANN)%20&%20Deep%20Learning%20Methods.md)
↗ [Neural Network Models](../../../🧠%20Computing%20Methodologies/👽%20Artificial%20Intelligence/🗝️%20AI%20Basics%20&%20Major%20Techniques/🌌%20Knowledge%20Representation%20(Syntax%20Level)%20and%20Reasoning%20(KRR)/🌊%20Artificial%20Neural%20Networks%20(ANN)%20&%20Deep%20Learning%20Methods/2️⃣%20Neural%20Network%20Models%20🗿/Neural%20Network%20Models.md)
- ↗ [Transformers](../../../🧠%20Computing%20Methodologies/👽%20Artificial%20Intelligence/🗝️%20AI%20Basics%20&%20Major%20Techniques/🌌%20Knowledge%20Representation%20(Syntax%20Level)%20and%20Reasoning%20(KRR)/🌊%20Artificial%20Neural%20Networks%20(ANN)%20&%20Deep%20Learning%20Methods/2️⃣%20Neural%20Network%20Models%20🗿/Transformers/Transformers.md)
	- ↗ [Attention in Transformer & Efficient Implementation](../../../🧠%20Computing%20Methodologies/👽%20Artificial%20Intelligence/🗝️%20AI%20Basics%20&%20Major%20Techniques/🌌%20Knowledge%20Representation%20(Syntax%20Level)%20and%20Reasoning%20(KRR)/🌊%20Artificial%20Neural%20Networks%20(ANN)%20&%20Deep%20Learning%20Methods/2️⃣%20Neural%20Network%20Models%20🗿/Transformers/Attention%20in%20Transformer%20&%20Efficient%20Implementation.md)

↗ [LLM (Large Language Model)](../../../🧠%20Computing%20Methodologies/👽%20Artificial%20Intelligence/Natural%20Language%20Processing%20(NLP)%20&%20Computational%20Linguistics/🦑%20LLM%20(Large%20Language%20Model)/LLM%20(Large%20Language%20Model).md)
- ↗ [LLM Foundation Models List & Evaluation and Benchmarks & Leaderboard](../../../🧠%20Computing%20Methodologies/👽%20Artificial%20Intelligence/Natural%20Language%20Processing%20(NLP)%20&%20Computational%20Linguistics/🦑%20LLM%20(Large%20Language%20Model)/🪜%20LLM%20Foundation%20Models%20List%20&%20Evaluation%20and%20Benchmarks%20&%20Leaderboard/LLM%20Foundation%20Models%20List%20&%20Evaluation%20and%20Benchmarks%20&%20Leaderboard.md)
- ↗ [LLM Utilization & Prompt, Context, and Harness Engineering](../../../🧠%20Computing%20Methodologies/👽%20Artificial%20Intelligence/Natural%20Language%20Processing%20(NLP)%20&%20Computational%20Linguistics/🦑%20LLM%20(Large%20Language%20Model)/LLM%20Training,%20Utilization,%20and%20Evaluation/LLM%20Utilization%20&%20Prompt,%20Context,%20and%20Harness%20Engineering/LLM%20Utilization%20&%20Prompt,%20Context,%20and%20Harness%20Engineering.md)
	- ↗ [Context Engineering & ICL (In-Context Learning)](../../../🧠%20Computing%20Methodologies/👽%20Artificial%20Intelligence/Natural%20Language%20Processing%20(NLP)%20&%20Computational%20Linguistics/🦑%20LLM%20(Large%20Language%20Model)/LLM%20Training,%20Utilization,%20and%20Evaluation/LLM%20Utilization%20&%20Prompt,%20Context,%20and%20Harness%20Engineering/Context%20Engineering%20&%20ICL%20(In-Context%20Learning).md)
- ↗ [LLM Applications & LLM-Driven Automation](../../../🧠%20Computing%20Methodologies/👽%20Artificial%20Intelligence/Natural%20Language%20Processing%20(NLP)%20&%20Computational%20Linguistics/🦑%20LLM%20(Large%20Language%20Model)/🚮%20LLM%20Applications%20&%20LLM-Driven%20Automation/LLM%20Applications%20&%20LLM-Driven%20Automation.md)
	- ↗ [Agentic LLMs & LLM Agent Harness](../../../🧠%20Computing%20Methodologies/👽%20Artificial%20Intelligence/Natural%20Language%20Processing%20(NLP)%20&%20Computational%20Linguistics/🦑%20LLM%20(Large%20Language%20Model)/🚮%20LLM%20Applications%20&%20LLM-Driven%20Automation/🫣%20Agentic%20LLMs%20&%20LLM%20Agent%20Harness/Agentic%20LLMs%20&%20LLM%20Agent%20Harness.md)
		- ↗ [LLM Agentic Reasoning](../../../🧠%20Computing%20Methodologies/👽%20Artificial%20Intelligence/Natural%20Language%20Processing%20(NLP)%20&%20Computational%20Linguistics/🦑%20LLM%20(Large%20Language%20Model)/🚮%20LLM%20Applications%20&%20LLM-Driven%20Automation/🫣%20Agentic%20LLMs%20&%20LLM%20Agent%20Harness/📑%20LLM%20Agentic%20Reasoning/LLM%20Agentic%20Reasoning.md)

↗ [AI4SE](../../../Software%20Engineering/🤖%20AI4SE/AI4SE.md)
- ↗ [AI4Code](../../../Software%20Engineering/🤖%20AI4SE/🤔%20AI4Code/AI4Code.md)

↗ [AI4Security](../../../CyberSecurity/🫧%20AI4Security/AI4Security.md)
- ↗ [LLM For Security](../../../CyberSecurity/🫧%20AI4Security/LLM%20For%20Security/LLM%20For%20Security.md)

↗ [Research Frontiers, Venues, and Humans by CS Areas](../../🧞‍♂️%20Research%20Frontiers,%20Venues,%20and%20Humans%20by%20CS%20Areas/Research%20Frontiers,%20Venues,%20and%20Humans%20by%20CS%20Areas.md)
- System
	- ↗ [Sec (Security) Related Venues and People](../../🧞‍♂️%20Research%20Frontiers,%20Venues,%20and%20Humans%20by%20CS%20Areas/System/Sec%20(Security)%20Related%20Venues%20and%20People.md)
	- ↗ [SE (Software Engineering) Related Venues and People](../../🧞‍♂️%20Research%20Frontiers,%20Venues,%20and%20Humans%20by%20CS%20Areas/System/SE%20(Software%20Engineering)%20Related%20Venues%20and%20People.md)
	- ↗ [PL (Program Languages) Related Venues and People](../../🧞‍♂️%20Research%20Frontiers,%20Venues,%20and%20Humans%20by%20CS%20Areas/System/PL%20(Program%20Languages)%20Related%20Venues%20and%20People.md)
	- ↗ [OS (Operating System) Related Venues and People](../../🧞‍♂️%20Research%20Frontiers,%20Venues,%20and%20Humans%20by%20CS%20Areas/System/OS%20(Operating%20System)%20Related%20Venues%20and%20People.md)
- Application
	- ↗ [Artificial Intelligence Related Venues and People](../../🧞‍♂️%20Research%20Frontiers,%20Venues,%20and%20Humans%20by%20CS%20Areas/Application/Artificial%20Intelligence%20Related%20Venues%20and%20People/Artificial%20Intelligence%20Related%20Venues%20and%20People.md)


### Paper Reading List
Sheng, Z., Chen, Z., Gu, S., Huang, H., Gu, G., & Huang, J. (2025). _LLMs in Software Security: A Survey of Vulnerability Detection Techniques and Insights_ (No. arXiv:2502.07049). arXiv. [https://doi.org/10.48550/arXiv.2502.07049](https://doi.org/10.48550/arXiv.2502.07049)

Zhu, X., Zhou, W., Han, Q.-L., Ma, W., Wen, S., & Xiang, Y. (2025). When Software Security Meets Large Language Models: A Survey. _IEEE/CAA Journal of Automatica Sinica_, _12_(2), 317–334. [https://doi.org/10.1109/JAS.2024.124971](https://doi.org/10.1109/JAS.2024.124971)


### Other Resources



## Intro
### Research Questions

- Code-model foundation: which code-specific data, adaptation methods, objectives, and representations create transferable capability without contamination?
- Software construction: when do generation, completion, translation, repository agents, and build automation produce executable, maintainable changes?
- Correctness and analysis: how should LLM proposals be combined with types, static analysis, symbolic execution, proof assistants, tests, and runtime evidence?
- Testing and repair: which feedback loops improve bug reproduction, oracle quality, debugging, general repair, and regression control?
- Performance and systems: can LLMs reliably localize and implement performance, compiler, OS, cloud, and infrastructure improvements?
- Languages and agent software: which programming models, types, contracts, compilers, runtimes, harnesses, and observability mechanisms make LLM applications dependable and maintainable?
- Security analysis: where do LLMs add value inside static/dynamic analysis, fuzzing, binary analysis, vulnerability triage, and patch validation?
- Cyber operations: what evidence and permission boundaries are needed for CTF, pentesting, SOC, incident-response, and end-to-end cyber agents?
- Security of LLM-enabled software: how should coding assistants, dependencies, RAG, MCP/tool calls, agent runtimes, and generated artifacts be isolated and audited?
- Evaluation: which benchmarks resist contamination, use executable or formal oracles, expose cost and variance, and support independent replication?



## Ref
[机器语言大模型]: https://mlm.lingyiwanwu.com

[2020年上半年我国互联网网络安全监测数据分析报告]: https://www.cac.gov.cn/2020-09/26/c_1602682854845452.htm

[Self-enhancing pattern detection with LLMs: Our answer to uncovering malicious packages at scale]: https://apiiro.com/blog/llm-code-pattern-malicious-package-detection/

[What's a Universal Windows Platform (UWP) app?]: https://learn.microsoft.com/en-us/windows/uwp/get-started/universal-application-platform-guide

[What is Microsoft Security Copilot?]: https://learn.microsoft.com/en-us/security-copilot/microsoft-security-copilot
