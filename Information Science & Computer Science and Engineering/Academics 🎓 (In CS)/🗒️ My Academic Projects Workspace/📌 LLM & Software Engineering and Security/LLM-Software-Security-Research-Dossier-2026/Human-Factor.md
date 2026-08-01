---
ai-generated: true
last-reviewed: 2026-08-01
---

# Human Factor: LLMs, Software Engineering, Systems, And Security

Date: 2026-08-01

Dossier homes:

- [LLMs for software engineering](LLM-Software-Research-Dossier-2026/LLM-Software-Research-Dossier-2026.md)
- [LLMs and software security](LLM-Software-Security-Research-Dossier-2026.md)
- [Software for LLM and agent systems](Software-For-LLM-Agent-Systems-Research-Dossier-2026/Software-For-LLM-Agent-Systems-Research-Dossier-2026.md)

This is the shared socio-technical and people/ecosystem map for all three dossiers. It covers both directions:

1. **LLMs for software**: requirements, architecture, generation, comprehension, search, review, testing, debugging, repair, maintenance, migration, refactoring, verification, formalization, compilation, performance optimization, systems/OS/cloud operations, security work, education, and developer experience.
2. **Software engineering, systems, and security for LLMs**: languages, runtimes, orchestration, testing, observability, evaluation, incident response, supply-chain assurance, privacy, access control, agent permissions, model/tool/data provenance, deployment, evolution, efficiency, reliability, safety, and governance.

The unit of analysis is therefore not a model in isolation. It is a person or team working through a model, interface, repository context, retrieval layer, toolchain, tests and verifiers, runtime permissions, organizational process, and accountability structure. A system can generate locally correct code yet reduce overall quality through review overload, weak requirements, architectural drift, performance regressions, insecure dependencies, loss of team knowledge, or unowned operational risk.

This file keeps the existing institution → group/unit → people → focus → relevance → evidence → sources structure. Academic `People` fields name current principal investigators or directly relevant faculty where an official group or personal page supports the association; they are discovery leads, not claims that every named person has published an LLM paper. Company records name product or research units rather than inferring a PI. First-party institution, group, product, and personal pages are preferred; papers and independent reports are used for empirical claims.


## Intro
### Main Focus: United States And China As Of 2026-08-01

The United States and China should be treated as the primary country pair for this dossier.

- The United States has the densest direct evidence for human factors: controlled coding studies, developer telemetry, DORA-style organizational research, human-LLM program-comprehension and reverse-engineering experiments, software-engineering-agent evaluations, SOC fieldwork, HCI work on red teaming and approval, AIxCC-style cyber reasoning systems, and large developer/security product deployments.
- China has the densest non-U.S. combination of code-model research, AI-for-SE and SE-for-AI laboratories, large domestic coding-agent deployments, systems and compiler work, Chinese-language software/security benchmarks, model-safety contests, security regulation, and security vendors. Direct public human-subject evidence is still thinner than the platform and technical record, so controlled and longitudinal studies of Chinese developer and operator practice remain a priority.
- For both countries, the practical unit of analysis is not just the model. It is the human plus model plus scaffold plus tool permissions plus UI plus audit logs plus validation harness plus organizational governance.

#### Confidence Labels Used Below

- `Core`: direct human/organizational evidence about LLM-assisted software work, or direct work at the LLM × software-engineering/systems/security intersection with an identifiable human-facing workflow.
- `Core/strong adjacent`: a mixed record: at least one direct intersection plus a broader program whose human evidence is incomplete.
- `Strong adjacent`: a leading PL, OS/systems, SE, security, AI, HCI, or formal-methods group with a clear route into this topic, but no direct human-subject result should be inferred.
- `Watch`: an important ecosystem actor, product, platform, contest, or general research group whose specific intersection or human evidence needs confirmation before it is cited as direct evidence.

Labels apply to relevance for this map, not institutional quality. Product claims, benchmark scores, telemetry, interviews, controlled experiments, ethnography, and peer-reviewed field studies are different evidence classes and must not be collapsed.

### Core Human-Factors Threads

These threads summarize the evidence that should be mapped back to the institution, lab, unit, or platform entries below. They are synthesis, not the organizing spine of the file.

- End-to-end engineering value: the outcome is accepted, correct, maintainable, efficient, secure, and operable software—not tokens generated or suggestions accepted. Measure requirements clarification, implementation, test and verification effort, review load, rework, incidents, handoff, and later change cost.
- Correctness and reliability: syntactic validity and passing visible tests are weak proxies. Human reviewers need specifications, generated-test provenance, semantic checks, differential/metamorphic tests, static analysis, proof obligations, uncertainty signals, and clear abstention. Automation can move defects from typing time into review, integration, or production.
- Performance and optimization: LLMs can propose algorithms, compiler transformations, kernels, configurations, and database/cloud changes, but plausible speedups may be input-specific, numerically unstable, non-portable, or obtained by weakening correctness. Evaluation needs workload provenance, baselines, semantic equivalence, cost/energy, hardware and compiler versions, and regression envelopes.
- Systems, OS, cloud, and operations: assistants act on logs, traces, configurations, infrastructure-as-code, incident tickets, shell commands, and production controls. Situation awareness, rollback, blast radius, least privilege, change windows, escalation, post-incident learning, and durable operator skill matter as much as diagnosis accuracy.
- Maintenance and evolution: repository-scale agents change how teams understand architecture, migrate APIs, refactor, review, document, and own code. Study architectural drift, duplicated logic, dependency choices, traceability, contributor attribution, review bottlenecks, and whether future maintainers can reconstruct intent.
- Formal methods and proof engineering: proof assistants, constraint solvers, types, static analyzers, model checkers, and executable specifications can ground LLM output. The human question is whether generated lemmas, invariants, repairs, and explanations reduce proof effort while preserving a small trusted base and auditable proof lineage.
- Software for LLM and agent systems: prompt programs, retrieval pipelines, memory, tool schemas, orchestration graphs, model routing, guardrails, evaluators, and fallbacks are software artifacts. Engineers need debuggable traces, reproducible replays, typed/contracted interfaces, versioning, test coverage, release gates, and clear ownership of stochastic behavior.
- Security, privacy, and supply chain for AI software: model weights, datasets, prompts, vector stores, plugins/MCP servers, generated dependencies, containers, CI/CD, telemetry, and third-party APIs form an attack surface. Secure-by-design work must include developer usability, permission comprehension, secret handling, provenance, incident reporting, and patch acceptance.
- Secure coding with AI assistants: Stanford's controlled study found that AI-assistant access can make users write less secure code while also increasing their confidence that the code is secure; prompt behavior and trust mattered. NYU's `Lost at C` study found a smaller effect in a C/pointer task, which is useful because it shows that task design, participant skill, interface, and language strongly shape results. Sources: https://arxiv.org/abs/2211.03622 ; https://par.nsf.gov/biblio/10472129-do-users-write-more-insecure-code-ai-assistants ; https://arxiv.org/abs/2208.09727 ; https://zenodo.org/record/7187358.
- Developer training and secure prompting: newer studies are shifting from "does the model emit insecure code?" to "can developers be trained to use LLM assistance more safely?" UCF SEAL work reports a quasi-experimental developer study where targeted security training reduced validated weaknesses in LLM-assisted backend code. Sources: https://seal.cs.ucf.edu/ ; https://arxiv.org/abs/2604.17763.
- Professional developer productivity: Google’s internal hybrid completion study, DORA’s qualitative and survey programs, GitHub research, and IDE-vendor studies show why perceived speed, suggestion acceptance, and organizational delivery metrics must be separated. AI frequently acts as an amplifier of repository health, platform quality, review culture, and organizational capability rather than an independent productivity treatment. Sources: https://research.google/blog/ml-enhanced-code-completion-improves-developer-productivity/ ; https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/ ; https://research.google/pubs/dora-impact-of-generative-ai-in-software-development/ ; https://lp.jetbrains.com/research/hax/.
- Program comprehension, scientific software, and expertise: LLMs can help users cross unfamiliar APIs, languages, and domains, but explanations may hide incorrect assumptions and erode learning. Studies should distinguish experts, professional developers, students, scientists who program, operators, security analysts, and end-user programmers, and include delayed recall, transfer, and handoff measures.
- Code review and team coordination: AI increases the volume and breadth of proposed changes. Review tooling must surface intent, provenance, affected invariants, test adequacy, security and performance evidence, and unresolved uncertainty; otherwise nominal human approval becomes a throughput bottleneck or rubber stamp.
- Education and skill formation: tutoring, explanation, example generation, and feedback can widen access, while answer substitution can weaken debugging, decomposition, and security judgment. Measure learning gains and unaided transfer, not assignment completion alone.
- SOC analyst collaboration: the strongest empirical line is in-the-wild SOC work. CSIRO Data61's study analyzes real analyst LLM use over time; USF / KU / USC ISI / Resideo work uses practitioner-centered SOC field methods to study whether LLM tools can be introduced without disrupting high-stress operational workflows. Sources: https://arxiv.org/abs/2508.18947 ; https://www.isi.edu/results/publications/65207/a-sociotechnical-practitioner-centered-approach-to-technology-adoption-in-cybersecurity-operations-an-llm-case ; https://www.ndss-symposium.org/ndss-paper/auto-draft-741/.
- Reverse engineering and analyst tooling: the NDSS 2026 human-LLM software reverse-engineering study surveyed practitioners and ran a controlled LLM-assisted reverse-engineering experiment, finding that LLMs can narrow novice/expert gaps while still misleading analysts through hallucinated or overconfident explanations. Sources: https://www.eurecom.fr/en/publication/8548 ; https://adamdoupe.com/publications/decompiling-synergy-ndss2026.pdf.
- Agent-human interaction security: UCLA's 2026 work argues that LLM-agent security is an agent-human interaction problem because production systems rely heavily on policy specification, runtime approval, and scope configuration, creating approval-fatigue and cognitive-burden tradeoffs. Sources: https://arxiv.org/abs/2605.24309 ; https://ucla-sec-lab.netlify.app/.
- Human susceptibility to compromised agents: HAT-Lab work on agent-mediated deception studies how users perceive attacks mediated by trusted LLM agents, including professional scenarios such as software development. Source: https://arxiv.org/abs/2602.21127.
- GUI-agent oversight and deceptive interfaces: CHI 2026 work on dark patterns and GUI agents shows that neither humans nor agents are uniformly resilient; human oversight can improve outcomes but also introduces attentional tunneling and cognitive-load costs. Sources: https://arxiv.org/abs/2509.10723 ; https://doi.org/10.1145/3772318.3791568.
- Red teaming as human work: AI red teaming is becoming a socio-technical labor practice involving dataset design, practitioner judgment, risk framing, and evaluation standards, not only jailbreak success rates. Sources: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0314658 ; https://research.ibm.com/publications/red-teaming-llms-as-socio-technical-practice-from-exploration-and-data-creation-to-evaluation ; https://doi.org/10.1145/3772318.3790792.
- Human oversight in cyber reasoning systems: AIxCC, OSS-CRS, foundation-model cyber programs, bug-bounty platforms, and autonomous pentesting tools all show that humans remain essential at target selection, policy setting, result triage, patch review, coordinated disclosure, and maintainer acceptance. Sources: https://www.darpa.mil/research/programs/ai-cyber ; https://www.darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33 ; https://openssf.org/tag/cyber-reasoning-systems/ ; https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy.

#### Shared Human-Control Model

| Lifecycle stage | Human responsibility | LLM/software-system risk | Minimum evidence |
| --- | --- | --- | --- |
| Intent and requirements | state goals, constraints, forbidden outcomes, priorities, and acceptance criteria | ambiguity becomes latent behavior or silently narrowed scope | original request, clarifications, requirement versions, decision owner |
| Architecture and composition | select components, models, tools, data, memory, permissions, and trust boundaries | hidden coupling, architectural drift, incompatible assumptions, excessive privilege | architecture record, dependency/model/tool inventory, threat model |
| Implementation and optimization | choose or approve code, transformations, kernels, configurations, and migrations | plausible but incorrect code; benchmark gaming; non-portable optimization | diff/provenance, build, semantic checks, representative workloads |
| Verification and review | design tests and proof obligations; challenge generated evidence | automation bias, test overfitting, reviewer overload, correlated generator/evaluator errors | independent oracles, coverage, static/formal checks, rejected alternatives |
| Deployment and operation | set rollout, monitoring, escalation, rollback, and incident policy | blast-radius expansion, alert flooding, loss of situation awareness | staged rollout, audit log, observability, rollback rehearsal, named owner |
| Maintenance and learning | preserve intent, update assets, hand off knowledge, learn from incidents | model/API/data drift, skill atrophy, orphaned generated systems | versioned prompts/configuration, regression history, incident record, handoff test |

#### Evidence And Study-Design Requirements

- identify participant population, expertise, domain knowledge, language/ecosystem, accessibility needs, and prior tool exposure;
- record model, version, interface, context/retrieval policy, autonomy, permissions, tools, prompts/rules/skills, repository state, and hardware/runtime where relevant;
- compare equivalent task scope and assurance standards, not raw output volume;
- separate perceived productivity, acceptance rate, task completion, functional correctness, security, performance, maintainability, learning, and organizational delivery;
- include verification and review time, false-positive burden, rework, escalation, coordination, and delayed maintenance or handoff;
- use representative hidden tests and independent oracles; disclose when the same model generates and judges;
- for optimization, report semantic equivalence, workload distribution, variance, cost, energy, and portability;
- for agent systems, log tool calls, denied actions, approvals, retries, failures, state changes, and rollback;
- report non-use, rejection, workarounds, and harmful or low-value assistance, not only successful interactions;
- distinguish peer-reviewed evidence from vendor telemetry, marketing claims, contests, benchmarks, standards, and informed watchlist status.

## 🇺‍🇸 United States Detailed Record

The U.S. record is organized by institution, lab, product group, standards body, or platform. Homepages are the first source for the profile; papers, contests, grants, and product launches are listed as activities or evidence under the host group. The order is loosely influence-weighted rather than alphabetical.

### USA: Companies, Platforms, Standards Bodies, And Independent Ecosystems

#### OpenAI

##### OpenAI Research

- `Homepage`: https://openai.com/research/index/
- `Label`: `Core`
- `Focused area`: frontier model research, system cards, safety/capability releases, model behavior, and research-indexed product work.
- `Human-factor relevance`: OpenAI Research anchors the OpenAI profile because it frames the model behavior, evaluation, memory, personalization, system cards, and capability releases that downstream developers and security practitioners experience.
- `Activities / evidence`: cybersecurity grant activity, Codex/security system cards, trusted-access cyber work, and malicious-use disruption reports should be mapped back here or to the safety/security units below rather than treated as standalone headings.
- `Sources`: https://openai.com/research/index/ ; https://openai.com/index/openai-cybersecurity-grant-program/.

##### OpenAI Safety, Preparedness, And Deployment Safety

- `Homepage`: https://openai.com/safety/
- `Label`: `Core`
- `Focused area`: model safeguards, red teaming, preparedness evaluations, system cards, deployment safety, and trusted access.
- `Human-factor relevance`: This unit matters for access design: cyber-capable models and coding agents require release gating, expert review, feedback channels, and clear boundaries between legitimate defensive work and misuse.
- `Activities / evidence`: preparedness framework materials, deployment safety materials, system cards, cyber access communications.
- `Sources`: https://openai.com/safety/ ; https://deploymentsafety.openai.com/.

##### OpenAI Security And Privacy

- `Homepage`: https://openai.com/security-and-privacy/
- `Label`: `Core`
- `Focused area`: product security, privacy controls, enterprise security, audit logs, compliance, responsible model development, and bug bounty.
- `Human-factor relevance`: This sector is directly tied to user trust, enterprise adoption, data-handling decisions, security researcher reporting, and the controls humans see when using OpenAI products in development or security workflows.
- `Activities / evidence`: enterprise controls, audit logging, data residency, bug bounty, and security whitepapers.
- `Sources`: https://openai.com/security-and-privacy/.

##### OpenAI Developer Platform And Codex

- `Homepage`: https://developers.openai.com/
- `Label`: `Core`
- `Focused area`: developer APIs, coding agents, repository editing, tool use, product documentation, and Codex-oriented workflows.
- `Human-factor relevance`: Developer-facing OpenAI products are where secure coding, tool-call approval, diff review, prompt quality, and trust calibration become everyday practice.
- `Activities / evidence`: Codex product materials, code-security system cards, developer documentation, and cyber grant outputs.
- `Sources`: https://developers.openai.com/ ; https://openai.com/research/index/.

#### Anthropic

##### Anthropic Research

- `Homepage`: https://www.anthropic.com/research
- `Label`: `Core`
- `Focused area`: frontier model safety, interpretability, societal impacts, real-world AI use, cyber capability evaluation, and red teaming.
- `Human-factor relevance`: Anthropic Research is the institution-level home for Project Glasswing and cyber verification work. The human-factor issue is how restricted access, evaluation, and disclosure workflows shape safe use of cyber-capable models.
- `Activities / evidence`: Frontier Red Team work, responsible scaling, cyber evaluation, Project Glasswing updates.
- `Sources`: https://www.anthropic.com/research ; https://www.anthropic.com/glasswing.

##### Anthropic Frontier Red Team

- `Homepage`: https://www.anthropic.com/research
- `Label`: `Core`
- `Focused area`: cybersecurity, biosecurity, autonomous systems, adversarial evaluation, and restricted model access.
- `Human-factor relevance`: This group should be tracked for who gets access, how findings are validated, how maintainers receive evidence, and how red-team labor becomes release policy.
- `Activities / evidence`: Project Glasswing, Cyber Verification Program, model-access controls.
- `Sources`: https://www.anthropic.com/glasswing ; https://www.anthropic.com/research.

#### Google

##### Google DeepMind

- `Homepage`: https://deepmind.google/
- `Label`: `Core`
- `Focused area`: frontier AI research, code/security agents, reasoning models, vulnerability repair, and AI-assisted analysis.
- `Human-factor relevance`: DeepMind matters for maintainer-facing patch trust. CodeMender-style systems should be analyzed as evidence-producing assistants, not only as autonomous patch generators.
- `Activities / evidence`: CodeMender, Gemini-based code/security work, OSS-Fuzz/Big Sleep adjacent activity.
- `Sources`: https://deepmind.google/ ; https://deepmind.google/en/blog/introducing-codemender-an-ai-agent-for-code-security/.

##### Google Project Zero

- `Homepage`: https://projectzero.google/
- `Label`: `Core`
- `Focused area`: high-quality vulnerability research, coordinated disclosure, exploitability analysis, and AI-assisted bug finding.
- `Human-factor relevance`: Project Zero provides the disclosure-discipline side of AI-assisted vulnerability discovery: human verification, report quality, patch coordination, and credibility.
- `Activities / evidence`: Big Sleep and AI-assisted real-software vulnerability discovery.
- `Sources`: https://projectzero.google/ ; https://projectzero.google/2024/10/from-naptime-to-big-sleep.html.

##### Google Threat Intelligence Group And Mandiant

- `Homepage`: https://cloud.google.com/security/resources/google-threat-intelligence
- `Label`: `Core/strong adjacent`
- `Focused area`: threat intelligence, incident response, AI misuse reporting, and SOC context.
- `Human-factor relevance`: GTIG/Mandiant should be tracked for how analysts interpret AI-enabled threats in the field, avoid over-attribution, and convert generated summaries into defensible response decisions.
- `Activities / evidence`: adversarial misuse reports and threat actor AI-use analysis.
- `Sources`: https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai ; https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools/.

##### Google Research Software Engineering And Programming Languages

- `Homepage`: https://research.google/teams/software-engineering-and-programming-languages/
- `Label`: `Core`
- `People`: Satish Chandra, Maxim Tabachnyk, Petros Maniatis, Ciera Jaspan, Caitlin Sadowski and collaborators across Google developer infrastructure.
- `Focused area`: developer tools, productivity, program analysis and refactoring, ML for code, language design, testing, CI, and large-repository engineering.
- `Human-factor relevance`: This is the Google unit most directly suited to studying whether AI improves professional engineering rather than merely generating plausible code. Its official program explicitly combines interviews, surveys, experiments, telemetry, formal models, and tool building.
- `Activities / evidence`: hybrid semantic/ML completion study with more than 10,000 internal developers; AI across Google’s IDE, review, search, bug-management, and planning surfaces; cross-tool development logs.
- `Sources`: https://research.google/teams/software-engineering-and-programming-languages/ ; https://research.google/blog/ml-enhanced-code-completion-improves-developer-productivity/ ; https://www.research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/.

##### DORA And Developer Productivity Research

- `Homepage`: https://dora.dev/
- `Label`: `Core`
- `People`: Derek DeBellis, Kevin Storer, Nathen Harvey, Ambar Murillo, Eirini Kalliamvakou and report collaborators.
- `Focused area`: organizational software delivery, developer experience, platform engineering, AI adoption, team performance, and mixed-method industry research.
- `Human-factor relevance`: DORA supplies the organizational level missing from task benchmarks. Its 2025 evidence treats AI as an amplifier of the surrounding system, making platform quality, work visibility, review culture, and organizational capability part of the causal model.
- `Activities / evidence`: 2025 State of AI-assisted Software Development; developer interviews and survey work on perceived and realized value.
- `Sources`: https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/ ; https://research.google/pubs/dora-impact-of-generative-ai-in-software-development/ ; https://research.google/pubs/how-gen-ai-affects-the-value-of-development-work/.

##### Google Research Scientific And Data Software

- `Homepage`: https://research.google/
- `Label`: `Core/strong adjacent`
- `People`: Michael Brenner, Lizzie Dorfman, John Platt and collaborators.
- `Focused area`: expert scientific coding, computational experiments, data analysis, optimization, and AI-assisted scientific discovery.
- `Human-factor relevance`: Scientific users often program without identifying primarily as software engineers. Study domain correctness, reproducibility, library/API understanding, computational cost, provenance, and whether an expert can audit or reproduce generated experiments.
- `Activities / evidence`: Empirical Research Assistance and Computational Discovery trusted-tester work.
- `Sources`: https://research.google/blog/empirical-research-assistance-era-from-nature-publication-to-catalyzing-computational-discovery/.

#### Microsoft

##### Microsoft Security Copilot

- `Homepage`: https://learn.microsoft.com/en-us/copilot/security/
- `Label`: `Core`
- `Focused area`: SOC copilot workflows, incident response, threat hunting, policy management, plugins, connectors, promptbooks, and custom agents.
- `Human-factor relevance`: Security Copilot is a major production example of LLM assistance for named security personas. Track evidence visibility, analyst authority, generated KQL/query trust, plugin grounding, and auditability.
- `Activities / evidence`: embedded Defender/Sentinel/Entra/Purview experiences, custom agents, promptbooks, audit-log features.
- `Sources`: https://learn.microsoft.com/en-us/copilot/security/ ; https://learn.microsoft.com/en-us/security-copilot/microsoft-security-copilot.

##### Microsoft Research AI-Driven Software Engineering

- `Homepage`: https://www.microsoft.com/en-us/research/project/967350/
- `Label`: `Core`
- `People`: Sriram Rajamani, Akash Lal, Arun Iyer, Aseem Rastogi, Pantazis Deligiannis, Sameer Segal and the AI-Driven Software Engineering team.
- `Focused area`: AI assistance across the software lifecycle, repository-scale reasoning, code transformation, testing, verification, developer tools, and trustworthy agentic engineering.
- `Human-factor relevance`: This group joins code-model capability with program analysis and professional workflows. Track how formal/static evidence, repository context, and human review are composed, and whether developer effort moves from construction into specification and assurance.
- `Activities / evidence`: archived AI-Driven Software Engineering project (the official page says the project has concluded); RiSE work on trustworthy code generation, proof/invariant generation, migration, and software agents.
- `Sources`: https://www.microsoft.com/en-us/research/project/967350/ ; https://www.microsoft.com/en-us/research/project/967350/people/ ; https://www.microsoft.com/en-us/research/research-area/programming-languages-software-engineering/.

##### Microsoft Research Developer Experience, HCI, And Empirical SE

- `Homepage`: https://www.microsoft.com/en-us/research/research-area/human-computer-interaction/
- `Label`: `Core/strong adjacent`
- `People`: Advait Sarkar, Denae Ford, Thomas Zimmermann, Eirini Kalliamvakou and collaborators across HCI, developer productivity, and software engineering.
- `Focused area`: developer experience, AI-assisted work, programming interfaces, empirical software engineering, collaboration, inclusion, and productivity measurement.
- `Human-factor relevance`: This is the Microsoft-side bridge between technical coding agents and their effects on professional work. Relevant outcomes include cognitive load, interruption, agency, inclusion, review behavior, team coordination, and what developers consider valuable work.
- `Sources`: https://www.microsoft.com/en-us/research/research-area/human-computer-interaction/ ; https://www.microsoft.com/en-us/research/research-area/programming-languages-software-engineering/.

##### Azure Reliability, AIOps, And Automated Incident Response

- `Homepage`: https://azure.microsoft.com/
- `Label`: `Core/strong adjacent`
- `Focused area`: cloud operations, incident diagnosis, reliability engineering, safe automation, configuration, rollout, observability, and operational copilots.
- `Human-factor relevance`: Production operations turn generated advice into state changes with real blast radius. Track evidence-linked diagnosis, operator situation awareness, approval boundaries, rollback, postmortem quality, and skill retention.
- `Activities / evidence`: Azure incident-management and AIOps research should be separated from product marketing and mapped to public empirical or peer-reviewed evidence when available.
- `Sources`: https://www.microsoft.com/en-us/research/research-area/systems-and-networking/ ; https://azure.microsoft.com/en-us/products/monitor.

#### GitHub

##### GitHub Advanced Security, CodeQL, And Security Lab

- `Homepage`: https://github.com/security/advanced-security
- `Label`: `Core`
- `Focused area`: CodeQL, code scanning, secret protection, dependency alerts, Copilot Autofix, and security researcher workflows.
- `Human-factor relevance`: GitHub is the core developer-workflow platform for studying AI-assisted secure coding, code review, alert triage, and maintainer burden. CodeQL evidence and Copilot-generated fixes need to be separated from ungrounded natural-language claims.
- `Activities / evidence`: Copilot Autofix, GitHub Security Lab, CodeQL, Advanced Security.
- `Sources`: https://github.com/security/advanced-security ; https://github.com/github/codeql ; https://github.com/GitHubSecurityLab.

##### GitHub Copilot

- `Homepage`: https://github.com/features/copilot
- `Label`: `Core`
- `Focused area`: coding assistance, code review, agentic development, repository context, and developer productivity.
- `Human-factor relevance`: Copilot is central to secure-coding human studies because suggestion acceptance, review dilution, and confidence changes are observable developer behaviors.
- `Activities / evidence`: Stanford and NYU secure-coding user studies, Copilot code-review/security evaluation work, platform telemetry where available.
- `Sources`: https://github.com/features/copilot ; https://arxiv.org/abs/2211.03622 ; https://arxiv.org/abs/2208.09727.

#### DARPA

##### AI Cyber Challenge

- `Homepage`: https://www.darpa.mil/research/programs/ai-cyber
- `Label`: `Core`
- `Focused area`: cyber reasoning systems, automated vulnerability discovery, patching, competition evaluation, and CRS handoff.
- `Human-factor relevance`: AIxCC is a public experiment in automating expert cyber labor. Human factors appear in scoring rules, CRS explanations, maintainer evidence, patch review, disclosure, and post-competition transition.
- `Activities / evidence`: AIxCC final results and team technical reports.
- `Sources`: https://www.darpa.mil/research/programs/ai-cyber ; https://www.darpa.mil/news/2025/aixcc-results.

#### OpenSSF

##### OSS-CRS

- `Homepage`: https://oss-crs.openssf.org/
- `Label`: `Core`
- `Focused area`: post-AIxCC open-source CRS infrastructure, OSS-Fuzz integration, verified findings, and maintainer-facing automation.
- `Human-factor relevance`: OSS-CRS is the maintainer handoff layer: automated systems must produce reproducible issues, minimized evidence, safe patches, and confidence signals that humans can act on.
- `Activities / evidence`: CRS development guide, OpenSSF CRS transition materials, OSS-Fuzz-oriented campaigns.
- `Sources`: https://oss-crs.openssf.org/ ; https://openssf.org/tag/cyber-reasoning-systems/.

#### NIST

##### Center for AI Standards and Innovation

- `Homepage`: https://www.nist.gov/caisi
- `Label`: `Core`
- `Focused area`: AI standards, agent security, evaluations, identity, authorization, and measurement.
- `Human-factor relevance`: CAISI should be tracked for definitions of secure agent deployment, human authorization, agent identity, transparency, audit logs, and reproducible evaluation.
- `Activities / evidence`: AI-agent security RFI, NCCoE work, standards activity.
- `Sources`: https://www.nist.gov/caisi ; https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems.

#### MITRE

##### MITRE ATT&CK

- `Homepage`: https://attack.mitre.org/
- `Label`: `Strong adjacent`
- `Focused area`: adversary behavior taxonomies, SOC analyst language, detection/response mapping.
- `Human-factor relevance`: ATT&CK shapes how analysts and vendors describe AI-enabled activity in operational settings.

##### MITRE ATLAS

- `Homepage`: https://atlas.mitre.org/
- `Label`: `Strong adjacent`
- `Focused area`: AI threat modeling, adversarial ML tactics, and AI-system risk taxonomy.
- `Human-factor relevance`: ATLAS is relevant for teaching humans to classify prompt injection, model misuse, and agent-mediated attacks with a shared vocabulary.

#### CISA

##### Secure By Design And Critical Infrastructure Guidance

- `Homepage`: https://www.cisa.gov/securebydesign
- `Label`: `Strong adjacent`
- `Focused area`: secure-by-design guidance, critical infrastructure security, incident reporting, cyber hygiene, and public-sector adoption norms.
- `Human-factor relevance`: CISA shapes procurement, escalation, reporting, and oversight expectations for organizations adopting AI coding and security tools.

#### IBM Research

##### Responsible AI And Red-Team Practice

- `Homepage`: https://research.ibm.com/topics/fairness-accountability-transparency
- `Label`: `Core`
- `Focused area`: responsible AI, AI red teaming, socio-technical evaluation, data practices, fairness, accountability, and transparency.
- `Human-factor relevance`: IBM Research is a primary U.S. node for the labor and dataset-design side of AI red teaming: who creates adversarial examples, which harms are prioritized, and how evaluation artifacts encode practitioner assumptions.
- `Activities / evidence`: `Red Teaming LLMs as Socio-Technical Practice`, DARE red teaming, IBM red-team methodology posts.
- `Sources`: https://research.ibm.com/topics/fairness-accountability-transparency ; https://research.ibm.com/publications/red-teaming-llms-as-socio-technical-practice-from-exploration-and-data-creation-to-evaluation.

##### IBM Research AI For Code

- `Homepage`: https://research.ibm.com/topics/ai-for-code
- `Label`: `Core`
- `People`: Saurabh Sinha, Ruchir Puri, Vaibhav Saxena and collaborators in IBM Research AI for Code.
- `Focused area`: enterprise code modernization, code understanding, refactoring, translation, testing, program analysis, software agents, and legacy/mainframe software.
- `Human-factor relevance`: Enterprise modernization is a long-horizon human problem: generated translations must preserve business rules, integrate with tests and operations, remain reviewable by scarce legacy experts, and transfer knowledge rather than merely replace syntax.
- `Activities / evidence`: Granite code models, software-engineering agents, code modernization and analysis for enterprise languages.
- `Sources`: https://research.ibm.com/topics/ai-for-code ; https://research.ibm.com/people/saurabh-sinha.

#### Amazon / AWS

##### Amazon Science Automated Reasoning And AWS Developer Tools

- `Homepage`: https://www.amazon.science/research-areas/automated-reasoning
- `Label`: `Core/strong adjacent`
- `Focused area`: automated reasoning, formal verification, cloud policy and configuration, code development, software agents, and operational assurance.
- `Human-factor relevance`: AWS is important in both directions: assistants help developers build and operate cloud software, while formal reasoning and policy analysis can constrain high-impact changes. Study whether explanations and counterexamples help users understand permissions, configurations, and proof-backed findings.
- `Activities / evidence`: Amazon Q Developer, automated reasoning for cloud security and policy, code-development planning and agent research.
- `Sources`: https://www.amazon.science/research-areas/automated-reasoning ; https://aws.amazon.com/q/developer/.

#### Meta

##### Meta AI And Developer Infrastructure

- `Homepage`: https://ai.meta.com/research/
- `Label`: `Strong adjacent`
- `Focused area`: code models, software testing and analysis, compiler/runtime efficiency, ML systems, generated-code evaluation, and large-scale developer infrastructure.
- `Human-factor relevance`: Meta is a watch point for combining learned code generation with mature static analysis, testing, and performance infrastructure. Public evidence should distinguish model capability from effects on engineers, code review, quality, and production reliability.
- `Activities / evidence`: Code Llama and successor code-model work, Infer static analysis, Sapienz-style testing, internal developer tooling.
- `Sources`: https://ai.meta.com/research/ ; https://engineering.fb.com/2023/08/24/developer-tools/code-llama-ai-for-coding/ ; https://fbinfer.com/.

#### Galois

##### Formal Methods And High-Assurance Software

- `Homepage`: https://galois.com/
- `Label`: `Strong adjacent`
- `Focused area`: formal methods, programming languages, verification, secure systems, cryptography, and high-assurance engineering.
- `Human-factor relevance`: Galois represents the assurance counterweight to unconstrained generation. Track tools that make formal specifications, proofs, and verified components usable in AI-assisted workflows while keeping a small trusted base and explicit responsibility.
- `Sources`: https://galois.com/ ; https://galois.com/research/.

#### HackerOne

##### Hai And Agentic Validation

- `Homepage`: https://www.hackerone.com/platform/hai/agentic-validation
- `Label`: `Core`
- `Focused area`: AI-assisted triage, validation, prioritization, vulnerability report workflow, and autonomous pentesting.
- `Human-factor relevance`: HackerOne is the best platform signal for how AI changes bounty labor: report volume, triager burden, proof quality, scope compliance, and remediation clarity.
- `Activities / evidence`: Hai, Agentic Validation, autonomous pentesting, AI vulnerability report telemetry.
- `Sources`: https://www.hackerone.com/platform/hai/agentic-validation ; https://docs.hackerone.com/en/articles/13603896-agentic-validation.

#### Bugcrowd

##### Bugcrowd Platform And AI Security Activity

- `Homepage`: https://www.bugcrowd.com/products/platform/
- `Label`: `Strong adjacent`
- `Focused area`: bug bounty, crowdsourced security, AI-assisted reports, exploitability validation, and platform policy.
- `Human-factor relevance`: Track separately from HackerOne to compare bounty-platform incentives, AI-generated report rules, triage thresholds, and researcher attribution.
- `Activities / evidence`: Bugcrowd AI triage/analytics and AI safety/security solution pages should be mapped here as platform activity.
- `Sources`: https://www.bugcrowd.com/products/platform/ ; https://www.bugcrowd.com/products/ai-powered-security-intelligence/ ; https://www.bugcrowd.com/solutions/ai/.

#### Trail of Bits

##### Security Engineering And Buttercup CRS

- `Homepage`: `To verify - Buttercup CRS public group page not located`
- `Label`: `Core/strong adjacent`
- `Focused area`: audits, vulnerability research, formal methods, CRS automation, exploitability validation, and AIxCC.
- `Human-factor relevance`: Trail of Bits combines elite human audit practice with CRS automation. Track how expert audit judgment is embedded in tools and how CRS output is reviewed before disclosure or patch acceptance.
- `Activities / evidence`: Buttercup CRS and AIxCC work.
- `Sources`: https://www.trailofbits.com/ ; https://www.darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33.

#### Theori

##### Offensive Security Research

- `Homepage`: https://theori.io/
- `Label`: `Core/strong adjacent`
- `Focused area`: offensive security, browser/blockchain security, CTF expertise, AIxCC systems, and exploit validation.
- `Human-factor relevance`: Theori is a strong case for competition-grade offensive expertise entering CRS design. Track how human experts validate generated exploit chains and distinguish plausible bugs from exploitable bugs.
- `Sources`: https://theori.io/ ; https://www.darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33.

#### CrowdStrike

##### Falcon, XDR, And Threat Intelligence

- `Homepage`: https://www.crowdstrike.com/en-us/products/falcon-platform/
- `Label`: `Strong adjacent`
- `Focused area`: SOC automation, endpoint telemetry, threat detection, incident response, and AI-assisted analyst workflows.
- `Human-factor relevance`: Track field evidence about how analysts use AI summaries during incident response while preserving skepticism about attribution, severity, and recommended containment.

#### Palo Alto Networks

##### Cortex

- `Homepage`: https://www.paloaltonetworks.com/cortex
- `Label`: `Strong adjacent`
- `Focused area`: SOC automation, extended detection/response, cloud security operations, and AI-assisted detection and response.
- `Human-factor relevance`: Cortex is the analyst-facing product surface. Track whether AI features expose evidence chains clearly enough for analysts to inspect generated conclusions before response actions.

##### Unit 42

- `Homepage`: https://unit42.paloaltonetworks.com/
- `Label`: `Strong adjacent`
- `Focused area`: threat intelligence, incident response, adversary research, and managed security expertise.
- `Human-factor relevance`: Unit 42 should be separate from Cortex because it represents expert investigation and reporting rather than the product workflow itself.

#### SentinelOne

##### Purple AI And Endpoint Security

- `Homepage`: https://www.sentinelone.com/platform/purple-ai/
- `Label`: `Strong adjacent`
- `Focused area`: endpoint telemetry, AI-assisted investigation, autonomous response, and security operations.
- `Human-factor relevance`: SentinelOne is a watch point for the boundary between recommendation and automated response: approval timing, uncertainty communication, and whether automation hides causal evidence.

#### Splunk

##### Security Operations Analytics

- `Homepage`: https://www.splunk.com/en_us/solutions/security.html
- `Label`: `Strong adjacent`
- `Focused area`: log analytics, SOC dashboards, investigation workflows, SIEM, and natural-language search.
- `Human-factor relevance`: Splunk matters because LLM copilots often sit on top of log-search workflows. Track whether natural-language interfaces improve analyst search or obscure exact query logic and data filters.

#### Cisco

##### Security Operations Analytics

- `Homepage`: https://www.cisco.com/site/us/en/products/security/index.html
- `Label`: `Strong adjacent`
- `Focused area`: security products, network/security telemetry, SOC dashboards, investigation workflows, and analyst-facing integrations.
- `Human-factor relevance`: Cisco should be tracked separately from Splunk because its network telemetry and product ecosystem create different evidence, response, and approval surfaces.

#### Elastic

##### Elastic Security

- `Homepage`: https://www.elastic.co/security
- `Label`: `Strong adjacent`
- `Focused area`: log search, endpoint/security analytics, SIEM, and analyst investigation.
- `Human-factor relevance`: Elastic is relevant for evidence traceability: analysts need visibility into generated searches, time windows, indices, and assumptions.

#### Rapid7

##### Vulnerability Management And Detection Products

- `Homepage`: https://www.rapid7.com/products/insightvm/
- `Label`: `Strong adjacent`
- `Focused area`: vulnerability prioritization, exposure management, detection products, and SOC workflows.
- `Human-factor relevance`: Rapid7 is a watch point for human prioritization: AI remediation summaries still need asset criticality, exploitability, business context, and compensating controls.

#### Tenable

##### Exposure Management

- `Homepage`: https://www.tenable.com/exposure-management
- `Label`: `Strong adjacent`
- `Focused area`: vulnerability management, exposure management, scanning, prioritization, and AI risk posture.
- `Human-factor relevance`: Tenable matters because vulnerability management is already a human overload problem. Generated remediation must be tied to asset-specific evidence.

#### Wiz

##### Cloud Security And Exposure Management

- `Homepage`: https://www.wiz.io/platform
- `Label`: `Strong adjacent`
- `Focused area`: cloud risk, attack path analysis, exposure management, and prioritization.
- `Human-factor relevance`: Wiz is relevant for cloud-security human factors: generated attack-path explanations must be checked against ownership, blast radius, and remediation feasibility across teams.

#### Snyk

##### Developer Security Platform

- `Homepage`: https://snyk.io/
- `Label`: `Strong adjacent`
- `Focused area`: AppSec, dependency risk, code scanning, developer remediation, and secure development.
- `Human-factor relevance`: Track whether generated fixes educate developers about root cause or encourage shallow changes that pass scanners without reducing risk.

#### Semgrep

##### Code Scanning And AppSec Workflows

- `Homepage`: https://semgrep.dev/
- `Label`: `Strong adjacent`
- `Focused area`: SAST, rule-based detection, code review, AppSec workflows, and developer education.
- `Human-factor relevance`: Semgrep is useful because it centers human-readable rules. LLM integration should be judged by whether it improves rule authoring and triage explanations without making developers trust unverified claims.

#### Checkmarx

##### AppSec Platform

- `Homepage`: https://checkmarx.com/platform/
- `Label`: `Strong adjacent`
- `Focused area`: secure code review, SAST, AppSec platform workflows, and software supply chain security.
- `Human-factor relevance`: Track how AI explanations affect developer acceptance of findings, security-team review time, and false-positive handling.

#### Veracode

##### Application Security Testing

- `Homepage`: https://www.veracode.com/products/
- `Label`: `Strong adjacent`
- `Focused area`: application security testing, secure coding analytics, code security measurement, and enterprise AppSec.
- `Human-factor relevance`: Veracode is useful for longitudinal code-security telemetry and for tracking whether AI coding changes training needs and remediation patterns.

#### Kudu Dynamics

##### Cyber Research And Vulnerability Discovery

- `Homepage`: https://kududyn.com/
- `Label`: `Strong adjacent`
- `Focused area`: advanced security research, fuzzing, exploit development, and CRS-style automation.
- `Human-factor relevance`: Track how AI changes internal analyst workflows, especially the boundary between automated search and human exploitability judgment.

#### ForAllSecure

##### Mayhem And Automated Testing

- `Homepage`: https://forallsecure.com/
- `Label`: `Strong adjacent`
- `Focused area`: fuzzing, automated vulnerability discovery, test generation, and Mayhem.
- `Human-factor relevance`: Fuzzing is a concrete oracle that can ground LLM claims. Track how developers interpret fuzzing-backed AI findings and how much evidence is enough to accept a generated patch.

#### Bishop Fox

##### Offensive Security And Attack-Surface Management

- `Homepage`: https://bishopfox.com/
- `Label`: `Strong adjacent`
- `Focused area`: pentesting, offensive security, attack-surface management, and AI-assisted validation.
- `Human-factor relevance`: Track whether AI reduces reconnaissance time while keeping human testers responsible for scope, authorization, and exploit safety.

#### Cobalt

##### Pentest-As-A-Service Platform

- `Homepage`: https://www.cobalt.io/platform
- `Label`: `Strong adjacent`
- `Focused area`: managed pentesting, researcher networks, report generation, and triage.
- `Human-factor relevance`: Track how AI changes report-writing and validation labor; polished reports can still be weak if evidence is thin.

#### XBOW

##### Autonomous Pentesting And Vulnerability Discovery

- `Homepage`: https://xbow.com/
- `Label`: `Strong adjacent`
- `Focused area`: autonomous vulnerability discovery, AI-driven testing, and platform-based vulnerability research.
- `Human-factor relevance`: XBOW represents the "AI researcher" role entering public vulnerability platforms. Human factors include rules of engagement, proof quality, attribution, and platform throttling of low-quality submissions.

#### Anysphere

##### Cursor

- `Homepage`: https://www.cursor.com/
- `Label`: `Strong adjacent`
- `Focused area`: repository-level coding agents, developer prompting, diff generation, and command execution.
- `Human-factor relevance`: Cursor shifts assistance from autocomplete to agentic editing. Track repository context trust, terminal approval, generated dependency changes, and review of large AI-authored diffs.

#### Sourcegraph

##### Cody

- `Homepage`: https://sourcegraph.com/cody
- `Label`: `Strong adjacent`
- `Focused area`: repository-level code understanding, code search, context retrieval, and AI coding assistance.
- `Human-factor relevance`: Context retrieval is a human-factor issue: developers need to know which code the assistant used and whether cited files support the answer.

#### Replit

##### Replit Agent

- `Homepage`: https://replit.com/agent
- `Label`: `Strong adjacent`
- `Focused area`: AI-assisted software creation, deployment, cloud coding, and novice developers.
- `Human-factor relevance`: Replit is relevant to novice and nontraditional developers who may deploy working but insecure systems without understanding auth, secrets, data handling, or dependency risk.

#### Windsurf

##### Windsurf AI IDE

- `Homepage`: https://windsurf.com/
- `Label`: `Strong adjacent`
- `Focused area`: AI IDE workflows, agentic development, multi-file editing, and coding-assistant continuity.
- `Human-factor relevance`: Track approval, review, and context visibility when the assistant edits multiple files over multiple steps.

#### Tabnine

##### Enterprise AI Coding Assistant

- `Homepage`: https://www.tabnine.com/enterprise
- `Label`: `Strong adjacent`
- `Focused area`: code completion, private deployment, enterprise controls, and developer productivity.
- `Human-factor relevance`: Tabnine is relevant because private/local deployment claims can change trust and policy decisions; private does not automatically mean secure.

#### JetBrains

##### JetBrains AI

- `Homepage`: https://www.jetbrains.com/ai/
- `Label`: `Strong adjacent`
- `Focused area`: IDE-native AI assistance, refactoring, code explanation, and inspections.
- `Human-factor relevance`: Track how security warnings, inspections, and AI suggestions interact inside professional IDE workflows.

##### JetBrains Research: AI For SE And Human-AI Experience

- `Homepage`: https://www.jetbrains.com/research/
- `Label`: `Core`
- `People`: Timofey Bryksin, Maliheh Izadi, Agnia Sergeyuk, Ekaterina Koshchenko and collaborators across JetBrains Research and academic partners.
- `Focused area`: AI in software engineering, human-AI experience, testing, collaboration, education, IDE instrumentation, context engineering, agent evaluation, and developer surveys.
- `Human-factor relevance`: JetBrains provides unusually direct access to professional IDE workflows. Its HAX program explicitly studies mental models, developer satisfaction, longitudinal logs, AI-generated-code review, reasoning handoff, and in-IDE interaction rather than treating model score as the endpoint.
- `Activities / evidence`: HAX Research; AI4SE partnership with TU Delft; runtime traces for software agents; AI debugging; code-review and developer-needs studies.
- `Sources`: https://www.jetbrains.com/research/ ; https://lp.jetbrains.com/research/software-engineering/ ; https://lp.jetbrains.com/research/hax/ ; https://lp.jetbrains.com/research/ai-for-se/.

#### SANS

##### SANS Cybersecurity Training

- `Homepage`: https://www.sans.org/cyber-security-training/
- `Label`: `Strong adjacent`
- `Focused area`: cybersecurity training, incident-response training, secure coding, and GIAC certification.
- `Human-factor relevance`: Track how curricula teach analysts and developers to use LLMs without outsourcing judgment.

##### GIAC Certifications

- `Homepage`: https://www.giac.org/
- `Label`: `Strong adjacent`
- `Focused area`: cybersecurity certification, skills validation, practitioner assessment, and workforce credentials.
- `Human-factor relevance`: GIAC should be separate from SANS training because certification changes incentives: it measures whether humans retain and can demonstrate security skills in an AI-assisted environment.

#### Security Journey

##### Developer Security Training

- `Homepage`: https://www.securityjourney.com/solutions
- `Label`: `Strong adjacent`
- `Focused area`: secure coding education, developer behavior change, and training programs.
- `Human-factor relevance`: Track whether training evolves from generic secure coding to AI-assisted secure-coding review and prompt discipline.

#### Secure Code Warrior

##### Developer Secure-Code Training

- `Homepage`: https://www.securecodewarrior.com/product/learning-platform
- `Label`: `Strong adjacent`
- `Focused area`: secure coding, developer upskilling, remediation practice, and labs.
- `Human-factor relevance`: Track whether interactive training prepares developers to spot insecure AI-generated code rather than only hand-written vulnerable snippets.

#### Immersive Labs

##### Cyber Workforce Training

- `Homepage`: https://www.immersivelabs.com/platform/
- `Label`: `Strong adjacent`
- `Focused area`: cyber ranges, SOC readiness, crisis simulation, and incident response training.
- `Human-factor relevance`: Track skill retention when LLM copilots reduce routine work but analysts must still reason when the assistant is wrong or unavailable.

#### Hack The Box

##### CTF Platform And AI Red-Team Training

- `Homepage`: https://www.hackthebox.ai/
- `Label`: `Strong adjacent`
- `Focused area`: CTF training, HTB Academy, cyber labs, and AI red-team practice.
- `Human-factor relevance`: Track whether AI-assisted players learn transferable security reasoning or mainly optimize prompt/scaffold use. The AI-specific platform should be separate from the generic CTF/training site when studying agent red-team evaluation.
- `Sources`: https://www.hackthebox.ai/ ; https://resources.hackthebox.com/cyber-performance-center.

#### TryHackMe

##### Cyber Learning Paths And Labs

- `Homepage`: https://tryhackme.com/
- `Label`: `Strong adjacent`
- `Focused area`: entry-level and intermediate cyber training, learning paths, and hands-on labs.
- `Human-factor relevance`: Track whether LLM hints improve learning or reduce the struggle needed to build durable mental models.

#### OWASP

##### GenAI Security Project

- `Homepage`: https://genai.owasp.org/
- `Label`: `Strong adjacent`
- `Focused area`: practitioner controls for LLM apps, agents, prompt injection, excessive agency, insecure output handling, and supply-chain issues.
- `Human-factor relevance`: OWASP is important because developers actually use its lists; track whether agent approval and prompt-injection guidance becomes actionable in engineering workflows.

#### Cloud Security Alliance

##### AI And Agentic Security Working Groups

- `Homepage`: https://cloudsecurityalliance.org/research/working-groups/ai-safety
- `Label`: `Strong adjacent`
- `Focused area`: cloud AI governance, agent security, enterprise guidance, and working-group standards.
- `Human-factor relevance`: CSA matters for enterprise ownership of agents: who approves integrations, who owns logs, and how incidents are investigated.
- `Sources`: https://cloudsecurityalliance.org/research/working-groups/ai-safety ; https://labs.cloudsecurityalliance.org/agentic/.

### USA: Universities, Labs, And Research Groups

#### Stanford University

##### Applied Cryptography Group / Stanford Computer Security Lab

- `Homepage`: https://crypto.stanford.edu/
- `Label`: `Core`
- `People`: Neil Perry, Megha Srivastava, Deepak Kumar, Dan Boneh and collaborators.
- `Focused area`: applied cryptography, computer security, AI-assisted secure coding, user interaction with code assistants, and overconfidence in generated code.
- `Human-factor relevance`: Stanford anchors the developer over-trust thread. The secure-coding study should be treated as evidence under this security ecosystem, not as the whole profile.
- `Activities / evidence`: controlled AI-assisted secure-coding study.
- `Sources`: https://crypto.stanford.edu/ ; https://arxiv.org/abs/2211.03622.

##### Stanford Institute for Human-Centered AI

- `Homepage`: https://hai.stanford.edu/
- `Label`: `Core/strong adjacent`
- `Focused area`: human-centered AI research, education, policy, practice, and societal impact.
- `Human-factor relevance`: HAI supplies the institutional human-centered AI frame: augmentation, organizational impact, trust, and policy.
- `Sources`: https://hai.stanford.edu/about/.

##### Stanford AI Lab

- `Homepage`: https://ai.stanford.edu/
- `Label`: `Strong adjacent`
- `Focused area`: AI research, agents, learning, NLP, robotics, and AI systems.
- `Human-factor relevance`: SAIL is a watch group for future agentic software/security work and human-AI collaboration methods.

##### Stanford Programming Languages, Compilers, And Pervasive Parallelism

- `Homepage`: https://ppl.stanford.edu/
- `Label`: `Core/strong adjacent`
- `People`: Alex Aiken, Kunle Olukotun and collaborators in programming languages, compilers, systems, and AI-assisted optimization.
- `Focused area`: program analysis and verification, compilers, parallel and heterogeneous systems, code reasoning, kernel and accelerator optimization, and self-improving agentic systems.
- `Human-factor relevance`: Optimization agents need a stricter evidence contract than ordinary code completion: semantic equivalence, workload coverage, hardware/compiler versions, energy and cost, and a reviewer-visible account of what changed. The group is also a strong node for joining LLM reasoning with established program semantics.
- `Activities / evidence`: LLMs for program reasoning and optimization; agentic compiler/library development; GPU-kernel and accelerator optimization.
- `Sources`: https://ppl.stanford.edu/ ; https://theory.stanford.edu/~aiken/ ; https://cs.stanford.edu/~anjiang/.

#### New York University / NYU Tandon

##### Center for Cybersecurity

- `Homepage`: https://cyber.nyu.edu/home-page/
- `Label`: `Core`
- `People`: Gustavo Sandoval, Hammond Pearce, Teo Nys, Ramesh Karri, Siddharth Garg, Brendan Dolan-Gavitt and collaborators.
- `Focused area`: cybersecurity research, secure code assistants, low-level C tasks, hardware/software security, digital forensics, and policy.
- `Human-factor relevance`: NYU's `Lost at C` line is a methodological counterweight for secure-coding human studies because task, language, interface, and participant skill affect measured harm.
- `Activities / evidence`: `Lost at C`, code-assistant security work, CCS-affiliated security education.
- `Sources`: https://cyber.nyu.edu/home-page/ ; https://arxiv.org/abs/2208.09727.

##### EnSuRe Research Group

- `Homepage`: https://research.engineering.nyu.edu/garg/
- `Label`: `Strong adjacent`
- `Focused area`: energy-aware, secure, and reliable computing; hardware security; ML and secure hardware.
- `Human-factor relevance`: Relevant for AI-assisted hardware/security design, where human reviewers may miss subtle generated hardware vulnerabilities.

##### Analysis of Computer Systems Group

- `Homepage`: https://cs.nyu.edu/acsys/
- `Label`: `Strong adjacent`
- `People`: Patrick Cousot, Thibault Dardinier, Benjamin Goldberg, Joseph Tassarotti, Sam Westrick, Thomas Wies and collaborators.
- `Focused area`: formal methods, programming languages, verification, abstract interpretation, compilers, concurrency, and reliable systems.
- `Human-factor relevance`: ACSys is a grounding and assurance node for LLM-generated code, invariants, optimizations, and system changes. Track whether generated proof obligations and counterexamples reduce expert effort without disguising assumptions or expanding the trusted base.
- `Sources`: https://cs.nyu.edu/acsys/ ; https://cs.nyu.edu/dynamic/people/faculty/type/20/?area=Formal+Methods%2C+Verification%2C+and+Programming+Languages ; https://cs.nyu.edu/~pcousot/researchinterests.html ; https://cs.nyu.edu/~jt4767/.

#### Arizona State University

##### SEFCOM

- `Homepage`: https://sefcom.asu.edu/
- `Label`: `Core`
- `People`: Adam Doupe, Yan Shoshitaishvili, Ruoyu Wang, Tiffany Bao and collaborators.
- `Focused area`: program analysis, vulnerability detection/exploitation/mitigation, access control, network/systems security, and hands-on security training.
- `Human-factor relevance`: SEFCOM is a core U.S. node for analyst-facing reverse engineering, CTF-style skill formation, and LLM-assisted binary-analysis workflows.
- `Activities / evidence`: NDSS 2026 human-LLM reverse-engineering study, CTF/security education, AIxCC-adjacent work.
- `Sources`: https://sefcom.asu.edu/ ; https://adamdoupe.com/publications/.

##### pwn.college

- `Homepage`: https://pwn.college/
- `Label`: `Core`
- `Focused area`: hands-on cybersecurity education, exploitation, reverse engineering, CTF training, and skill scaffolding.
- `Human-factor relevance`: pwn.college should be treated as a training and skill-formation platform. Track whether LLM tutors accelerate learning or create shortcut dependency.
- `Sources`: https://pwn.college/.

#### University of California, Santa Barbara

##### Shellphish

- `Homepage`: https://shellphish.net/
- `Label`: `Core/strong adjacent`
- `Focused area`: CTF, hacking science, automated cyber reasoning, vulnerability discovery, and exploit education.
- `Human-factor relevance`: Shellphish bridges expert CTF culture and cyber reasoning systems. The human-factor object is tacit expert knowledge becoming prompts, scaffolds, fuzzing loops, and triage pipelines.
- `Sources`: https://shellphish.net/.

#### UCLA

##### UCLA Security Lab

- `Homepage`: https://ucla-sec-lab.netlify.app/
- `Label`: `Core`
- `People`: Yuan Tian, Peiran Wang, Ying Li and collaborators.
- `Focused area`: security/privacy, computer systems, machine learning, HCI, LLM-agent security, and agent-human interaction.
- `Human-factor relevance`: UCLA anchors the agent-human interaction security thread: policy specification, runtime approval, scope configuration, authorization/provenance, and approval fatigue.
- `Sources`: https://ucla-sec-lab.netlify.app/ ; https://arxiv.org/abs/2605.24309.

#### University of Central Florida

##### SEAL Lab

- `Homepage`: https://seal.cs.ucf.edu/
- `Label`: `Core`
- `People`: David Mohaisen, Mohammed Kharma, Ahmed Sabbah, Mohammad Alkhanafseh and collaborators.
- `Focused area`: software engineering, applied security, secure LLM-generated code, developer security training, and trustworthy AI.
- `Human-factor relevance`: SEAL is important because it tests an intervention: training developers to use LLM assistance more securely.
- `Activities / evidence`: quasi-experimental developer security-training study.
- `Sources`: https://seal.cs.ucf.edu/ ; https://arxiv.org/abs/2604.17763.

#### UC Berkeley

##### Center for Human-Compatible AI

- `Homepage`: https://chai.berkeley.edu/
- `Label`: `Core`
- `People`: Jonathan Stray and collaborators.
- `Focused area`: beneficial AI, human-compatible systems, alignment, bounded rationality, human-robot cooperation, and adversarial testing.
- `Human-factor relevance`: CHAI is the conceptual human-centered safety anchor for red-teaming practice, control, and systems that remain beneficial under human uncertainty.
- `Activities / evidence`: grounded-theory work on LLM red teaming.
- `Sources`: https://chai.berkeley.edu/about ; https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0314658.

##### Berkeley AI Research Lab

- `Homepage`: https://bair.berkeley.edu/
- `Label`: `Strong adjacent`
- `Focused area`: AI research, agents, learning, responsible AI, and human-in-the-loop evaluation.
- `Human-factor relevance`: BAIR is a watch group for agentic software engineering and safety work that may become security-facing.

##### Berkeley Programming Systems Research

- `Homepage`: https://ps.berkeley.edu/
- `Label`: `Core/strong adjacent`
- `People`: Sarah Chasins, Alvin Cheung, Koushik Sen, Sanjit Seshia, Max Willsey, Katherine Yelick and affiliated faculty.
- `Focused area`: formal methods, programming environments, human factors, compilers, runtimes, testing, synthesis, language design, optimization, and education.
- `Human-factor relevance`: This umbrella is directly aligned with the broadened map because it connects human-facing programming environments to semantic assurance and efficient execution. It is a high-value discovery node for verified generation, debugging, testing, and end-user programming.
- `Sources`: https://ps.berkeley.edu/ ; https://www2.eecs.berkeley.edu/Research/Areas/PS/.

##### Sky Computing Lab / AI Systems And LLM Programs

- `Homepage`: https://sky.cs.berkeley.edu/
- `Label`: `Core/strong adjacent`
- `People`: Ion Stoica, Matei Zaharia and Sky Lab collaborators.
- `Focused area`: cloud and AI systems, LLM-program frameworks, optimization, semantic data systems, efficient runtimes, and production deployment.
- `Human-factor relevance`: Frameworks such as DSPy make prompts, modules, optimizers, and evaluators into software artifacts. Study debuggability, provenance, evaluator validity, cost control, version drift, and whether engineers can understand the optimized program they deploy.
- `Sources`: https://sky.cs.berkeley.edu/ ; https://people.eecs.berkeley.edu/~matei/.

#### Carnegie Mellon University

##### Software Engineering Institute

- `Homepage`: https://www.sei.cmu.edu/
- `Label`: `Core/strong adjacent`
- `Focused area`: software engineering, AI engineering, cybersecurity, acquisition, CERT/CC, and operational security guidance.
- `Human-factor relevance`: SEI translates LLM-agent security into practitioner categories: controls, responsibility, lifecycle governance, logs, permissions, and operational adoption.
- `Sources`: https://www.sei.cmu.edu/ ; https://www.sei.cmu.edu/library/bridging-research-and-practice-in-llm-agent-security/.

##### CyLab Usable Privacy and Security Laboratory

- `Homepage`: https://cups.cs.cmu.edu/
- `Label`: `Strong adjacent`
- `Focused area`: usable privacy/security, security warnings, privacy tools, IoT labels, and user studies.
- `Human-factor relevance`: Agent approval prompts and AI-generated security explanations are new forms of usable-security warning and consent design.

##### Software And Societal Systems Department

- `Homepage`: https://s3d.cmu.edu/
- `Label`: `Core`
- `People`: Claire Le Goues, Bogdan Vasilescu and collaborators across software engineering, program repair, empirical SE, AI engineering, and societal computing.
- `Focused area`: construction, maintenance, evolution, repair, assurance, developer productivity, open-source communities, team processes, and responsible software systems.
- `Human-factor relevance`: S3D joins technical repair and assurance with the social organization of software work. It is central for studying whether coding agents improve accepted repairs and team outcomes, how generated contributions affect review and governance, and how benefits or burdens are distributed.
- `Sources`: https://s3d.cmu.edu/ ; https://s3d.cmu.edu/people/core-faculty/legoues-claire.html ; https://sc.cs.cmu.edu/people/faculty/vasilescu-bogdan.html.

#### Georgia Tech

##### Team Atlanta

- `Homepage`: https://team-atlanta.github.io/
- `Label`: `Core`
- `People`: Taesoo Kim and Team Atlanta collaborators.
- `Focused area`: AIxCC, ATLANTIS CRS, automated vulnerability discovery/remediation, and AI-powered security automation.
- `Human-factor relevance`: Team Atlanta is a high-influence CRS group. The human-facing issue is how ATLANTIS-style outputs become proof, patch proposals, confidence, and maintainer-ready artifacts.
- `Sources`: https://team-atlanta.github.io/ ; https://www.cc.gatech.edu/news/georgia-tech-makes-history-wins-darpa-challenge.

##### School of Cybersecurity and Privacy

- `Homepage`: https://scp.cc.gatech.edu/
- `Label`: `Strong adjacent`
- `Focused area`: interdisciplinary cybersecurity, privacy, critical infrastructure, and cyber defense.
- `Human-factor relevance`: Track for broader Georgia Tech cybersecurity groups that may produce human-facing deployment or evaluation work beyond Team Atlanta.

#### University of Washington

##### Tech Policy Lab

- `Homepage`: https://techpolicylab.uw.edu/
- `Label`: `Core/strong adjacent`
- `Focused area`: technology policy, AI governance, privacy/security, and policy-oriented human studies.
- `Human-factor relevance`: The AI-agent permissions line belongs here: users over-permission or under-permission agents because they cannot foresee future data needs.
- `Sources`: https://techpolicylab.uw.edu/ ; https://techpolicylab.uw.edu/wp-content/uploads/2026/02/2511.17959v1.pdf.

##### Security and Privacy Research Lab

- `Homepage`: https://seclab.cs.washington.edu/
- `Label`: `Strong adjacent`
- `Focused area`: emerging-technology security and privacy, agentic security, usable security, and AR/security.
- `Human-factor relevance`: Track for agentic-security work where human oversight, privacy, and system permissions interact.
- `Sources`: https://seclab.cs.washington.edu/ ; https://agent-security.cs.washington.edu/.

##### Programming Languages And Software Engineering Group

- `Homepage`: https://www.cs.washington.edu/research/software-hardware-systems/
- `Label`: `Strong adjacent`
- `People`: Michael Ernst, Dan Grossman, Zachary Tatlock, Alvin Cheung, Emina Torlak and PLSE collaborators.
- `Focused area`: programming environments, analysis, language design, synthesis, compilers, testing, verification, security, and programmer productivity.
- `Human-factor relevance`: PLSE supplies semantic and tooling foundations for making generated software correct and understandable. Track LLM-assisted specification, test and invariant generation, compiler correctness, repository tools, and interfaces that expose proof or analysis results to developers.
- `Sources`: https://www.cs.washington.edu/research/software-hardware-systems/ ; https://homes.cs.washington.edu/~mernst/research/ ; https://homes.cs.washington.edu/~djg/ ; https://homes.cs.washington.edu/~ztatlock/.

##### Code And Cognition Lab / Human-Centered Software Development

- `Homepage`: https://faculty.washington.edu/ajko/
- `Label`: `Core/strong adjacent`
- `People`: Amy J. Ko and collaborators in the Code & Cognition Lab and developer education.
- `Focused area`: programming cognition, developer tools, debugging, programming education, accessibility, inclusion, and human-centered software engineering.
- `Human-factor relevance`: This line is essential for separating task completion from durable comprehension and learning. LLM tools should be evaluated for debugging skill, transfer, accessibility, self-efficacy, and who gains or loses agency.
- `Sources`: https://faculty.washington.edu/ajko/.

#### University of Notre Dame

##### Human-Centered Responsible AI Lab

- `Homepage`: https://lucyinstitute.nd.edu/centers-and-labs/human-centered-responsible-ai-hrai-lab/
- `Label`: `Core/strong adjacent`
- `Focused area`: responsible AI, human-centered AI systems, AI literacy, ethics, collaboration, and community benefit.
- `Human-factor relevance`: HRAI is the Notre Dame unit for responsible AI and human-AI collaboration context.
- `Sources`: https://lucyinstitute.nd.edu/centers-and-labs/human-centered-responsible-ai-hrai-lab/hrai-research/.

##### SaNDwich Lab

- `Homepage`: https://hci.nd.edu/people/professors/toby-jia-jun-li/
- `Label`: `Core`
- `People`: Toby Jia-Jun Li, Jingyu Tang, Chaoran Chen and collaborators.
- `Focused area`: HCI, end-user software engineering, human-AI interaction, GUI agents, and AI-powered interactive systems.
- `Human-factor relevance`: This is the correct Notre Dame lab context for GUI-agent oversight and dark-pattern work.
- `Sources`: https://hci.nd.edu/people/professors/toby-jia-jun-li/ ; https://arxiv.org/abs/2509.10723.

##### EPOCH Research Lab

- `Homepage`: https://www.epochlab.org/
- `Label`: `Core/strong adjacent`
- `People`: Karla Badillo-Urquiola and collaborators.
- `Focused area`: HCI, online safety, usable privacy/security, responsible computing, youth and marginalized populations.
- `Human-factor relevance`: EPOCH is relevant to socio-technical red-team practice, vulnerable users, AI literacy, and human-centered evaluation.
- `Sources`: https://www.epochlab.org/team.html ; https://doi.org/10.1145/3772318.3790792.

#### University of Michigan

##### Intelligence And Human Augmentation Lab

- `Homepage`: https://ihub.engin.umich.edu/
- `Label`: `Strong adjacent`
- `People`: Dakuo Wang and collaborators in human-AI teamwork.
- `Focused area`: human-AI mutual understanding, human-AI teaming, transparency, and human-centric engineering.
- `Human-factor relevance`: Michigan's GUI-agent and human-AI teamwork contribution should be mapped to labs that study oversight cost, transparency, and cognitive load.
- `Sources`: https://ihub.engin.umich.edu/ ; https://arxiv.org/abs/2509.10723.

#### Northeastern University

##### Cybersecurity and Privacy Institute

- `Homepage`: https://cyber.northeastern.edu/
- `Label`: `Core/strong adjacent`
- `Focused area`: privacy, security, AI agents, dark patterns, platform accountability, and applied cybersecurity.
- `Human-factor relevance`: Northeastern is relevant to dark patterns as a security issue for both humans and GUI agents.
- `Sources`: https://cyber.northeastern.edu/ ; https://www.khoury.northeastern.edu/dark-patterns-have-long-manipulated-human-behavior-online-now-ai-agents-are-falling-for-them-too/.

#### University of South Florida

##### Xinming Ou Security Research Group / Rapid7 Cyber Threat Intelligence Lab

- `Homepage`: https://cse.usf.edu/~xou/
- `Label`: `Core`
- `People`: Daniel Lende, Xinming Ou, Francis Hahn, Mohd Mamoon and collaborators.
- `Focused area`: human-centric cybersecurity, SOC operations, cyber operator training, practitioner-centered security technology adoption, and human-machine teaming for defense.
- `Human-factor relevance`: USF should be anchored to Ou's security group rather than to the university homepage. The group explicitly frames cybersecurity inside human/social contexts, including SOCs and software development companies.
- `Activities / evidence`: sociotechnical LLM adoption in SOCs, agentic AI for tooling gaps in SOCs, cyber-operator training with Rapid7.
- `Sources`: https://cse.usf.edu/~xou/ ; https://cse.usf.edu/~xou/publications.html ; https://www.usf.edu/news/2023/usf-and-rapid7-to-launch-cyber-training-initiative-through-1-5-million-federal-grant.aspx.

#### University of Kansas

##### Alexandru Bardas Cybersecurity Research Group

- `Homepage`: https://www.ittc.ku.edu/~alexbardas/
- `Label`: `Core`
- `People`: Alexandru G. Bardas, Jaclyn Lauren Dudek and collaborators.
- `Focused area`: systems and network security, security operations under uncertainty, usable security, and practical cybersecurity research.
- `Human-factor relevance`: KU should be tracked separately for the security-operations side of SOC fieldwork: task fit, validation of generated explanations, and operational disruption risk.
- `Activities / evidence`: WOSOC/SOC work with USF and USC ISI on non-disruptive LLM introduction and practitioner-centered adoption.
- `Sources`: https://www.ittc.ku.edu/~alexbardas/ ; https://engr.ku.edu/research-areas/cybersecurity ; https://www.ndss-symposium.org/ndss-paper/auto-draft-741/.

#### USC Information Sciences Institute

##### ISI Networking And Cybersecurity Featured Labs / ANT Lab

- `Homepage`: https://www.isi.edu/nc/research-areas/featured-labs/
- `Label`: `Core`
- `People`: Michael Collins and collaborators.
- `Focused area`: networking and cybersecurity, internet measurement, network-based cyber attacks, human aspects of cybersecurity, embedded cybersecurity, and binary analysis.
- `Human-factor relevance`: ISI should be mapped through its networking/cybersecurity lab structure, not the institute homepage. The SOC LLM work belongs here as evidence of operational deployment and analyst validation problems.
- `Activities / evidence`: practitioner-centered SOC LLM adoption work; future mapping should identify the exact ISI lab/personnel lineage for each SOC paper.
- `Sources`: https://www.isi.edu/nc/research-areas/featured-labs/ ; https://www.isi.edu/results/publications/65207/a-sociotechnical-practitioner-centered-approach-to-technology-adoption-in-cybersecurity-operations-an-llm-case.

##### Center for Computer Systems Security

- `Homepage`: https://ccss.usc.edu/
- `Label`: `Strong adjacent`
- `Focused area`: computer systems security, cyber-security testbeds, security experimentation, and applied defense infrastructure.
- `Human-factor relevance`: CCSS is relevant as an experimentation and testbed context for human-facing cyber tools: analysts and researchers need reproducible environments before trusting AI-generated cyber evidence.

#### William & Mary

##### Xinfeng Li Trustworthy Agentic Systems Group / HAT-Lab Project

- `Homepage`: https://letterligo.netlify.app/
- `Label`: `Core`
- `People`: Xinfeng Li and collaborators including Shenyu Dai, Kelong Zheng, Yue Xiao, Gelei Deng, Wei Dong, Xiaofeng Wang.
- `Focused area`: human perception vulnerability in LLM-driven agentic systems, agent-mediated deception, trusted-agent attacks.
- `Human-factor relevance`: This should not point to the W&M root page. The durable public host I found is Li's research homepage; HAT-Lab is currently best treated as a project/platform under that researcher/group line until a separate lab homepage is verified.
- `Activities / evidence`: empirical HAT-Lab study of human susceptibility to agent-mediated deception, including software-development scenarios.
- `Sources`: https://letterligo.netlify.app/ ; https://arxiv.org/abs/2602.21127.

##### Humans and Technology Laboratory

- `Homepage`: https://hatlab.org/
- `Label`: `Strong adjacent`
- `Focused area`: human-centered computing, human factors, HCI, usable privacy/security, privacy-enhancing technologies, and empirical methods.
- `Human-factor relevance`: This HATLab is a separate human-factors lab signal and should not be conflated with the HAT-Lab agent-mediated deception platform unless author/lab membership is confirmed.
- `Sources`: https://hatlab.org/.

##### SEMERU - Software Engineering Maintenance And Evolution Research Unit

- `Homepage`: https://www.cs.wm.edu/semeru/
- `Label`: `Core`
- `People`: Denys Poshyvanyk and SEMERU collaborators.
- `Focused area`: maintenance and evolution, program comprehension, traceability, repository mining, testing, privacy, licensing, neural code models, generated-code smells, hallucination analysis, and human-centered explanation.
- `Human-factor relevance`: SEMERU is a direct broadened-scope node: it studies code-model reliability and interpretability alongside the long-term work of understanding, reviewing, licensing, testing, and maintaining software.
- `Activities / evidence`: human-centered explanations for code/test generation; trust mapping for LLMs in SE; developer perspectives on generative-AI licensing; deterministic AST checks for hallucinated code; maintenance and evolution tooling.
- `Sources`: https://www.cs.wm.edu/semeru/ ; https://www.cs.wm.edu/~denys/research.html ; https://www.cs.wm.edu/~denys/publications.html.

#### Pennsylvania State University

##### PLAINTEXT Lab

- `Homepage`: https://plaintext.psu.edu/about/
- `Label`: `Core/strong adjacent`
- `Focused area`: responsible AI, human-centered AI, ethical and practical AI systems, transparency, and accessibility.
- `Human-factor relevance`: Penn State should be mapped through specific responsible-AI and human-centered-computing groups. PLAINTEXT is relevant to how AI evaluations, explanations, and standards become usable by real people rather than only benchmark designers.
- `Activities / evidence`: socio-technical red-team practice evidence remains mapped as a cross-institution activity until the exact Penn State author-to-lab host is verified.
- `Sources`: https://plaintext.psu.edu/about/ ; https://doi.org/10.1145/3772318.3790792.

##### Department of Human-Centered Computing And Social Informatics

- `Homepage`: https://ist.psu.edu/about/departments/department-human-centered-computing-social-informatics
- `Label`: `Strong adjacent`
- `Focused area`: human-computer interaction, human-centered design, usability, human-centered AI, information ethics, and social-organizational informatics.
- `Human-factor relevance`: Keep this as a department-level host only for Penn State human-centered AI work that cannot yet be mapped to a smaller lab. It is more precise than the university homepage and should be decomposed further as papers are mapped.

#### Johns Hopkins University

##### Ziang Xiao Human-AI Interaction Research Group

- `Homepage`: https://www.cs.jhu.edu/faculty/ziang-xiao/
- `Label`: `Core/strong adjacent`
- `People`: Ziang Xiao, Yaxing Yao and collaborators.
- `Focused area`: HCI, human-AI interaction, human-centered model evaluation, online information seeking, AI for social science, and agent oversight.
- `Human-factor relevance`: Track for oversight interfaces that do not force humans to approve an agent's unverifiable summary.
- `Activities / evidence`: GUI-agent oversight and dark-pattern work should be mapped here when Xiao is the JHU host.
- `Sources`: https://www.cs.jhu.edu/faculty/ziang-xiao/ ; https://doi.org/10.1145/3772318.3791568.

#### Purdue University

##### ASSET Research Lab

- `Homepage`: https://lt-asset.github.io/
- `Label`: `Strong adjacent`
- `Focused area`: AI-software synergy, LLMs for code generation and understanding, automated program repair, vulnerability fixing, binary analysis, and testing deep-learning systems.
- `Human-factor relevance`: ASSET is the specific Purdue group to watch for human-facing developer effects: generated repairs need reviewer-visible tests, traces, root-cause explanations, and trust calibration.
- `Sources`: https://lt-asset.github.io/.

##### CERIAS - Center for Education and Research in Information Assurance and Security

- `Homepage`: https://www.cerias.purdue.edu/
- `Label`: `Strong adjacent`
- `Focused area`: information assurance, end-system security, human-centric security, prevention/detection/response, security awareness, education, and training.
- `Human-factor relevance`: CERIAS is the broader Purdue security center; keep it separate from ASSET because its human-centric security and training focus is organizational rather than code-agent-specific.
- `Sources`: https://www.cerias.purdue.edu/.

##### Human-Centered Software Systems Lab

- `Homepage`: https://hcss.cs.purdue.edu/
- `Label`: `Core`
- `People`: Tianyi Zhang and HCSS collaborators.
- `Focused area`: software engineering, HCI, AI-assisted programming, code visualization, debugging, human expertise, programmer productivity, robustness, and developer decision support.
- `Human-factor relevance`: HCSS is a direct fit for the broadened dossier because it treats developers as partners in intelligent systems. Track repair strategies, mental models, explanation, code search, robustness, and when proactive assistance helps or interrupts.
- `Sources`: https://hcss.cs.purdue.edu/ ; https://www.cs.purdue.edu/research/software-engineering.html.

##### Software Reliability And Large Language Models

- `Homepage`: https://www.cs.purdue.edu/homes/lintan/
- `Label`: `Core`
- `People`: Lin Tan and collaborators in software reliability, agents, code reasoning, testing, review, and vulnerability repair.
- `Focused area`: LLMs and agents across requirements, design, generation, test generation, review, bug/security detection and repair, binary code, and software benchmarks.
- `Human-factor relevance`: The research line explicitly spans the whole lifecycle; human evaluation should test whether agent outputs support root-cause understanding, reviewer confidence, maintainable repairs, and safe use across source, binary, and robotic software.
- `Sources`: https://www.cs.purdue.edu/homes/lintan/ ; https://www.cs.purdue.edu/homes/lintan/ongoingProjects.html.

##### PurPL And Reliable Systems

- `Homepage`: https://purpl.cs.purdue.edu/
- `Label`: `Strong adjacent`
- `People`: Milind Kulkarni, Tiark Rompf, Suresh Jagannathan, Xiangyu Zhang, Pedro Fonseca and associated faculty.
- `Focused area`: programming languages, compilers, formal methods, systems, software engineering, optimization, verification, secure and reliable systems.
- `Human-factor relevance`: This is a discovery umbrella for grounding code agents with language/system semantics and for evaluating AI-generated optimizations and systems changes under correctness, performance, and reliability constraints.
- `Sources`: https://purpl.cs.purdue.edu/ ; https://www.cs.purdue.edu/homes/pfonseca/ ; https://www.cs.purdue.edu/research/software-engineering.html.

#### MIT

##### CSAIL Computer Systems Security Group

- `Homepage`: https://css.csail.mit.edu/
- `Label`: `Watch`
- `Focused area`: secure systems, operating systems, computer architecture, distributed systems, programming languages, and web-browser security.
- `Human-factor relevance`: The MIT security entry should be lab-specific. For human factors, the key question is whether secure-system evidence can be exposed in forms that developers and reviewers can understand and act on.
- `Sources`: https://css.csail.mit.edu/.

##### CSAIL Parallel And Distributed Operating Systems Group

- `Homepage`: https://pdos.csail.mit.edu/
- `Label`: `Watch`
- `Focused area`: parallel/distributed systems, systems verification, operating systems, scalability, security, networking, mobile computing, language and compiler design.
- `Human-factor relevance`: PDOS is relevant when AI-assisted coding or cyber reasoning produces formally grounded artifacts. Track whether verification-backed outputs reduce human review burden or simply move the cognitive burden to proof interpretation.
- `Sources`: https://pdos.csail.mit.edu/.

##### CSAIL Programming Languages And Software Engineering

- `Homepage`: https://projects.csail.mit.edu/pl/
- `Label`: `Core/strong adjacent`
- `People`: Saman Amarasinghe, Michael Carbin, Martin Rinard, Armando Solar-Lezama, Adam Chlipala and collaborators.
- `Focused area`: program synthesis, analysis and transformation, compilers, resilient and efficient systems, language design, proof engineering, security, and human-facing programming tools.
- `Human-factor relevance`: MIT’s umbrella makes the key complementarity explicit: LLMs broaden specifications and search, while program analysis, synthesis, compilers, and theorem proving can enforce semantics. Evaluate whether the resulting tools help humans express intent and audit results.
- `Sources`: https://projects.csail.mit.edu/pl/ ; https://www.csail.mit.edu/research/computer-aided-programming ; https://www.csail.mit.edu/research/programming-languages-verification.

##### Computer-Aided Programming Group

- `Homepage`: https://www.csail.mit.edu/research/computer-aided-programming
- `Label`: `Core`
- `People`: Armando Solar-Lezama and group collaborators.
- `Focused area`: program synthesis, intent specification, executable constraints, neuro-symbolic programming, verification-guided generation, and programming tools.
- `Human-factor relevance`: This group directly targets the hardest human question in code generation: how a user conveys intent when natural-language specifications are incomplete or ambiguous. Study clarification, counterexample interaction, specification repair, and confidence grounded in execution or proof.
- `Sources`: https://www.csail.mit.edu/research/computer-aided-programming ; https://people.csail.mit.edu/asolar/SynthesisCourse/index.htm.

##### Commit Compiler Research Group

- `Homepage`: https://commit.csail.mit.edu/
- `Label`: `Core/strong adjacent`
- `People`: Saman Amarasinghe and Commit collaborators.
- `Focused area`: high-performance languages and compilers, program optimization, DSLs, autotuning, dynamic analysis, and LLM-integrated programming.
- `Human-factor relevance`: Performance assistance should reduce optimization expertise barriers without producing opaque, fragile, or input-specific speedups. Track specification of numerical/performance goals, semantic equivalence, tuning cost, portability, and maintainers’ ability to understand generated optimizations.
- `Sources`: https://commit.csail.mit.edu/ ; https://people.csail.mit.edu/saman/.

#### UC San Diego

##### Center for Machine-Intelligence, Computing and Security

- `Homepage`: https://mics.ucsd.edu/node/267
- `Label`: `Watch`
- `Focused area`: machine intelligence, computing systems, security and privacy, hardware/software/data integration, and cyber-physical security.
- `Human-factor relevance`: UCSD should not be represented by only a CSE research-area page. MICS is a more concrete center for AI/security/system integration; track whether security-AI tools are evaluated with expert users, not only benchmark labels.
- `Sources`: https://mics.ucsd.edu/node/267.

##### Programming Systems Group / Trustworthy Code Generation

- `Homepage`: https://cseweb.ucsd.edu/~ldantoni/
- `Label`: `Core`
- `People`: Loris D'Antoni and Programming Systems collaborators.
- `Focused area`: specification-aligned language models, formal constraints, synthesis, personalized compilers, compiler fuzzing, and code that satisfies semantic requirements.
- `Human-factor relevance`: This line treats correctness constraints as a first-class interface between humans and generators. Study whether developers can author, inspect, and repair the specifications; whether constrained decoding gives calibrated confidence; and how compiler personalization affects portability and ownership.
- `Sources`: https://cseweb.ucsd.edu/~ldantoni/.

#### University of Chicago

##### SUPERgroup - Security, Usability, And Privacy Education And Research

- `Homepage`: https://super.cs.uchicago.edu/
- `Label`: `Watch`
- `Focused area`: usable security, privacy, AI ethics, HCI, data-driven online safety/privacy methods, and interaction for machine-learning/language-model systems.
- `Human-factor relevance`: SUPERgroup is the concrete UChicago host for the human/security/privacy side. Track how warnings, policy, and interface design affect trust in AI-generated security actions.
- `Sources`: https://super.cs.uchicago.edu/.

#### University of Illinois Urbana-Champaign

##### SALT Lab - Social Computing Systems Lab

- `Homepage`: https://salt.ischool.illinois.edu/
- `Label`: `Strong adjacent`
- `Focused area`: social computing, usable privacy/security, security education, AI ethics, and empathy-driven hands-on security/AI projects.
- `Human-factor relevance`: UIUC should not be a generic CS-security placeholder here. SALT is the specific human-facing security group identified in this pass; future technical security groups should be added only with their own pages.
- `Sources`: https://salt.ischool.illinois.edu/.

##### Code Intelligence, Software Reliability, And LLM Agents

- `Homepage`: https://lingming.cs.illinois.edu/
- `Label`: `Core`
- `People`: Lingming Zhang and collaborators in software engineering, programming languages, ML, formal methods, systems, and security.
- `Focused area`: code models and agents, software testing, analysis, repair, synthesis, fuzzing, AI for systems/security, and open code models.
- `Human-factor relevance`: The technical breadth makes this a major source of agent and oracle designs, but human benefit must be measured separately from benchmark performance: reviewability, failure detection, cost, maintainability, and deployment effects remain open.
- `Activities / evidence`: TitanFuzz, AlphaRepair, ChatRepair, Agentless, code-world-model work, LLM-agent software-engineering courses.
- `Sources`: https://lingming.cs.illinois.edu/ ; https://grainger.illinois.edu/about/directory/faculty/lingming.

#### Princeton University

##### Center for Information Technology Policy

- `Homepage`: https://citp.princeton.edu/
- `Label`: `Watch`
- `Focused area`: AI governance, platform policy, security, privacy, and accountability.
- `Human-factor relevance`: CITP matters for accountability when AI-generated code or AI-generated vulnerability reports cause downstream harm.

##### Princeton Programming Languages Group

- `Homepage`: https://pl.cs.princeton.edu/
- `Label`: `Strong adjacent`
- `People`: Aarti Gupta, Zachary Kincaid, Mae Milano, David Walker and collaborators; Andrew Appel is emeritus.
- `Focused area`: semantics, analysis, verification, decision procedures, defect detection, design, implementation, optimization, DSLs, theorem proving, and verified software toolchains.
- `Human-factor relevance`: Princeton is a grounding node for generated code, proofs, and systems artifacts. Track whether LLM-assisted proof and specification work reduces expert labor while preserving checkability, modularity, and end-to-end guarantees.
- `Sources`: https://pl.cs.princeton.edu/ ; https://vst.cs.princeton.edu/ ; https://www.cs.princeton.edu/~appel/.

#### Cornell University

##### Programming Languages Group

- `Homepage`: https://pl.cs.cornell.edu/
- `Label`: `Strong adjacent`
- `People`: Nate Foster, Adrian Sampson, Andrew Myers, Ross Tate, Alexandra Silva, François Guimbretière and affiliated collaborators.
- `Focused area`: language design, semantics, security, synthesis, verification, compilers, networks, systems, and human-facing programming abstractions.
- `Human-factor relevance`: Cornell is a broad PL/systems discovery node for reliable agent interfaces, language-based security, provenance, and formally grounded generation. Add a `Core` label only when a direct LLM/software or human study is mapped.
- `Sources`: https://pl.cs.cornell.edu/.

#### Cornell Tech

##### Security, Trust, And Safety Initiative

- `Homepage`: https://tech.cornell.edu/impact/security-trust-and-safety-sets/
- `Label`: `Watch`
- `Focused area`: cybersecurity, privacy, trust and safety, AI-agent risks, online harms, and cross-disciplinary security practice.
- `Human-factor relevance`: SETS is a better host than the Cornell Tech root page because it directly names security, trust, and safety. Track semi-autonomous AI-agent subversion, human review, and organizational trust processes.
- `Sources`: https://tech.cornell.edu/impact/security-trust-and-safety-sets/.

##### Security And Privacy Research Area

- `Homepage`: https://tech.cornell.edu/research/security-privacy/
- `Label`: `Strong adjacent`
- `Focused area`: security, privacy, cryptography, usable security, HCI, AI/ethics, and industry-informed security research.
- `Human-factor relevance`: Keep this separate from SETS because it is the academic research-area page listing relevant faculty and labs. It is useful for mapping future publications to individual Cornell Tech groups.
- `Sources`: https://tech.cornell.edu/research/security-privacy/.

##### People-Aware Computing Lab

- `Homepage`: https://pac.cs.cornell.edu/
- `Label`: `Watch`
- `Focused area`: human-AI interaction, responsible machine learning, multimodal sensing, conversational agents, and real-world AI deployment.
- `Human-factor relevance`: PAC is a concrete human-AI interaction lab at Cornell Tech. It is adjacent to software security through agent safety, trust, and real-world deployment constraints rather than vulnerability analysis itself.
- `Sources`: https://pac.cs.cornell.edu/.

#### University of Maryland

##### Human-Computer Interaction Lab

- `Homepage`: https://hcil.umd.edu/
- `Label`: `Watch`
- `Focused area`: HCI, usable privacy/security, security warnings, and human-centered systems.
- `Human-factor relevance`: AI-agent approval prompts are a new kind of security warning; track whether warning-design lessons transfer to dynamic, model-generated actions.

#### University of California, Irvine

##### STAIRS Lab

- `Homepage`: https://stairs.ics.uci.edu/
- `Label`: `Core`
- `People`: Iftekhar Ahmed and STAIRS collaborators.
- `Focused area`: AI-assisted software engineering and testing, agentic and multi-agent methods, maintainability, accessibility, reliability, interpretability, and quality of AI-integrated systems.
- `Human-factor relevance`: STAIRS explicitly frames LLM software work around empowering developers and maintaining human values. Track explanation, robust testing, accessible tooling, bias, and whether agent efficiency translates into maintainable and reliable software.
- `Sources`: https://stairs.ics.uci.edu/.

##### CRADL - Collaboration Research In Action, Design, And Learning

- `Homepage`: https://cradl.ics.uci.edu/
- `Label`: `Strong adjacent`
- `People`: David Redmiles and collaborators.
- `Focused area`: collaborative software engineering, design work, reflection, learning, and interdisciplinary study of development teams.
- `Human-factor relevance`: Coding agents change coordination and reflection, not only individual typing. CRADL is a discovery node for team-level methods, handoffs, awareness, and how organizations learn from failed AI-assisted work.
- `Sources`: https://cradl.ics.uci.edu/.

#### University of Texas at Austin

##### Trishul Lab / Programming Languages And Formal Methods

- `Homepage`: https://www.cs.utexas.edu/~swarat/
- `Label`: `Core`
- `People`: Swarat Chaudhuri and Trishul collaborators; Isil Dillig and the broader PL/formal-methods community are relevant adjacent leads.
- `Focused area`: program synthesis, automated reasoning, neurosymbolic programming, LLM agents for theorem proving, formally verified code generation, trustworthy AI, and safe systems.
- `Human-factor relevance`: Trishul connects natural-language and learned search with specifications and proof. The human questions are how users state intent, inspect generated arguments, repair failed specifications, and retain authority when an assistant handles low-level code or proof steps.
- `Activities / evidence`: Copra; CLEVER; LLM-aided synthesis and reasoning; AI for code, systems, math, and science.
- `Sources`: https://www.cs.utexas.edu/~swarat/ ; https://www.cs.utexas.edu/~swarat/pubs/index.html.

#### Columbia University

##### Software Systems And Programming Systems Laboratory

- `Homepage`: https://www.cs.columbia.edu/areas/software/
- `Label`: `Core/strong adjacent`
- `People`: Baishakhi Ray, Gail Kaiser, Ronghui Gu, Suman Jana, Junfeng Yang and collaborators across software systems, programming systems, languages, compilers, and security.
- `Focused area`: software design, implementation, analysis, verification and evaluation; program analysis, testing, binaries, AI4SE, systems, security, and developer tooling.
- `Human-factor relevance`: Columbia spans generated-code quality, systems correctness, security, and developer-facing tooling. Track whether AI-generated changes are testable and explainable across source and binary artifacts and whether review evidence survives deployment.
- `Sources`: https://www.cs.columbia.edu/areas/software/ ; https://psl.cs.columbia.edu/.

### USA: Main Focus Areas To Track

- Developer work and organizational delivery: requirements, architecture, code generation, comprehension, search, documentation, review, maintenance, coordination, perceived versus realized productivity, and distribution of gains and burdens.
- Correctness and reliability: specification quality, generated tests, independent oracles, static/formal evidence, repair validation, regressions, incidents, and long-term maintainability.
- Performance and efficiency: semantic equivalence, workload coverage, compiler/kernel/database/cloud optimization, latency, throughput, energy, cost, portability, and performance-review expertise.
- Systems, OS, cloud, and operations: configuration, infrastructure-as-code, diagnosis, incident response, rollout, situation awareness, least privilege, blast radius, escalation, and rollback.
- Developer secure-code behavior: over-trust, prompt quality, AI-suggestion acceptance, generated-dependency risk, insecure code review, and training interventions.
- SOC analyst work: alert fatigue, situation awareness, evidence grounding, analyst authority, low-level telemetry interpretation, and handoff between AI summaries and human decisions.
- Reverse engineering and binary analysis: LLM-generated symbol names, type recovery, decompiler comments, explanation confidence, hallucinated control-flow summaries, and novice/expert gap reduction.
- Agent oversight: policy specification, runtime approval, scope configuration, audit logs, identity, data-access permissions, tool-call transparency, and approval fatigue.
- Red-team labor: who creates adversarial examples, how risk categories are chosen, how datasets become benchmarks, and whether model providers ignore user specificity and interaction context.
- Bug-bounty and maintainer workflows: AI-generated report volume, invalid-report burden, agentic validation, coordinated disclosure, and evidence thresholds for maintainers.
- Software for LLM systems: prompt/program debugging, orchestration, evaluation, observability, provenance, model/data/tool drift, release governance, and ownership.
- Education, inclusion, and expertise: durable learning, novice/expert differences, scientific and end-user programming, accessibility, skill atrophy, unaided transfer, and equitable access to review and assurance capacity.

## 🇨🇳 China Detailed Record

China should be treated as the second main focus, but with a different evidence profile. The public record is strongest in code models and agents, AI4SE/SE4AI research, repository and software-lifecycle tooling, compiler and systems work, Chinese-language software/security benchmarks, model-safety evaluation platforms, contests, standards, and security-vendor ecosystems. Direct human-subject studies of developer, reviewer, operator, or analyst work are less visible than in the United States, so many entries are marked `Strong adjacent` or `Watch`. Entries below are organized by institution, lab, company, standards body, or platform; projects and contests appear as activities unless the host institution is not yet clear enough.

### China: Companies, Platforms, Standards Bodies, And Security Ecosystem

#### Alibaba (阿里巴巴)

##### Alibaba Security (阿里巴巴安全)

- `Homepage`: https://security.alibaba.com/
- `Label`: `Core`
- `Focused area`: industry security research, vulnerability response, platform security, AI security evaluation, and cybersecurity benchmarking.
- `Human-factor relevance`: Alibaba Security should host the CS-Eval evidence in the China map because it connects benchmark design to operational security categories used by practitioners.
- `Activities / evidence`: CS-Eval / CyberSec-Eval collaboration, Alibaba Cloud AI security challenge, security platform work.
- `Sources`: https://security.alibaba.com/ ; https://cs-eval.com/ ; https://github.com/CS-EVAL/CS-Eval.

##### Alibaba Cloud Qoder CN / Former Tongyi Lingma (阿里云 Qoder CN / 原通义灵码)

- `Homepage`: https://www.alibabacloud.com/help/en/lingma/product-overview/introduction-of-lingma
- `Label`: `Core/strong adjacent`
- `Focused area`: lifecycle-wide coding agents, IDE and CLI workflows, enterprise private knowledge, multi-model selection, regulated-industry deployment, code generation, testing, and repository work.
- `Human-factor relevance`: The suite is a large Chinese developer-workflow surface. Track task clarification, autonomous long-running work, code and terminal permissions, use of private repositories, generated-diff review, tests, enterprise filtering, behavior telemetry, and whether domestic deployment changes trust and compliance decisions.
- `Activities / evidence`: Tongyi Lingma was renamed Qoder CN in May 2026; the suite now spans coding, CLI, cloud agents, and enterprise deployment.
- `Sources`: https://www.alibabacloud.com/help/en/lingma/product-overview/introduction-of-lingma ; https://www.alibabacloud.com/help/en/lingma/product-overview/changelogs-of-202602.

##### Qwen Team (通义千问团队)

- `Homepage`: https://qwenlm.github.io/
- `Label`: `Strong adjacent`
- `Focused area`: foundation models, code models, open model ecosystem, model APIs, and agent/tool use.
- `Human-factor relevance`: Qwen is the model layer behind many Chinese developer workflows. Track how open code models are integrated into local IDEs, security tools, and enterprise deployments.

#### Tencent (腾讯)

##### Zhuque Lab (腾讯朱雀实验室)

- `Homepage`: https://zhuque.tencent.com/
- `Label`: `Core/strong adjacent`
- `Focused area`: AI security, model safety, offensive/defensive research, LLM security evaluation, and vulnerability research.
- `Human-factor relevance`: Zhuque Lab should be tracked as Tencent's AI/security lab rather than merged into Hunyuan. It is relevant to red-team methodology, responsible disclosure, and how model-safety findings are communicated to developers and security engineers.

##### Hunyuan (腾讯混元)

- `Homepage`: https://hunyuan.tencent.com/
- `Label`: `Strong adjacent`
- `Focused area`: foundation models, coding/productivity tools, enterprise AI deployment.
- `Human-factor relevance`: Hunyuan is the model/provider surface. Track safeguards, enterprise deployment controls, and whether coding/security assistants expose evidence and uncertainty to users.

##### Tencent Cloud CodeBuddy

- `Homepage`: https://www.codebuddy.cn/
- `Label`: `Core/strong adjacent`
- `Focused area`: AI IDE, CLI and plugins, multi-file coding agents, code completion, unit tests, intelligent review and repair, MCP integration, mini-program development, and enterprise R&D.
- `Human-factor relevance`: CodeBuddy is a major current Chinese coding-agent surface. Track how professional and novice developers review multi-file changes, how Skills/MCP expand authority, whether generated tests are independent, and how product telemetry, retention, and benchmark results relate to correctness and maintainability.
- `Activities / evidence`: CodeBuddy 4.3 for WeChat development; WorkBuddy/CodeBuddy agent stack; Tencent WorkBuddy Bench.
- `Sources`: https://www.codebuddy.cn/ ; https://cloud.tencent.com/document/product/1749/111914 ; https://intl.cloud.tencent.com/document/product/1300/81494.

#### Huawei Cloud (华为云)

##### Pangu Large Models (盘古大模型)

- `Homepage`: https://www.huaweicloud.com/intl/en-us/product/pangu.html
- `Label`: `Strong adjacent`
- `Focused area`: enterprise foundation models, cloud AI deployment, private deployment, and industry-specific model services.
- `Human-factor relevance`: Huawei Cloud is important for regulated-sector and enterprise adoption. Track how private/cloud deployment, access control, and auditability affect organizational willingness to use LLMs for security or code work.

##### Huawei Cloud CodeArts / CodeArts Snap (华为云码道 / 智能开发助手)

- `Homepage`: https://www.huaweicloud.com/intl/en-us/product/codearts/ai.html
- `Label`: `Core/strong adjacent`
- `Focused area`: AI-native IDE and coding agent, specification-guided development, enterprise codebases, generation, explanation, debugging, translation, checks, optimization, unit tests, Skills, and repository indexing.
- `Human-factor relevance`: CodeArts is the human-facing Huawei engineering surface. Track whether organizational standards and private knowledge actually improve generated changes, how users inspect unit tests and optimization claims, and how HarmonyOS/enterprise specialists supervise autonomous work.
- `Activities / evidence`: 2026 CodeArts coding-agent public beta and commercial release; existing CodeArts Snap workflows.
- `Sources`: https://www.huaweicloud.com/intl/en-us/product/codearts/ai.html ; https://www.huaweicloud.com/news/2026/20260226150052593.html.

#### Baidu (百度)

##### ERNIE / Qianfan (文心一言 / 千帆)

- `Homepage`: https://qianfan.cloud.baidu.com/
- `Label`: `Strong adjacent`
- `Focused area`: foundation models, model platform services, public-facing assistants, and enterprise AI deployment.
- `Human-factor relevance`: Baidu should be tracked for model-platform governance and developer/SOC-facing AI integrations, especially access, logging, approval, content reliability, and user-facing assistant design.

##### Baidu Comate (文心快码)

- `Homepage`: https://cloud.baidu.com/doc/COMATE/index.html
- `Label`: `Core/strong adjacent`
- `Focused area`: AI IDE and plugins, repository exploration, code generation and editing, tests, refactoring, debugging, custom agents, subagents, Skills, Rules, MCP, memory, automation, enterprise deployment, and R&D-efficiency measurement.
- `Human-factor relevance`: Comate exposes many control dimensions that human studies should record rather than hide under “AI assistance”: Agent/Plan/Ask modes, subagent delegation, remembered context, custom rules, tool access, model choice, and queued/asynchronous work. Enterprise telemetry should be analyzed separately from developer benefit and software quality.
- `Activities / evidence`: Comate 4.0 and AI IDE; enterprise SaaS/hybrid/private deployment; internal adoption claims should remain vendor telemetry until independently studied.
- `Sources`: https://cloud.baidu.com/doc/COMATE/s/xlnvqe047 ; https://cloud.baidu.com/doc/COMATE/s/qm7yrpa11 ; https://cloud.baidu.com/doc/COMATE/s/2mjzerjsp.

#### ByteDance (字节跳动)

##### Software Engineering Lab (软件工程实验室)

- `Homepage`: https://se-research.bytedance.com/
- `Label`: `Strong adjacent`
- `Focused area`: safe and trusted intelligent automated software engineering, code intelligence, and developer tooling.
- `Human-factor relevance`: ByteDance SE Lab is relevant because it explicitly frames automated software engineering as safe and trusted. Track how software-engineering agents allocate work between human developers and automated repair/localization systems.

##### Trae AI IDE

- `Homepage`: https://www.trae.ai/
- `Label`: `Strong adjacent`
- `Focused area`: AI IDE, coding agents, repository editing, developer workflow, and multi-step code changes.
- `Human-factor relevance`: Trae is the developer-facing product surface. Track approval design, generated-diff review, context display, test execution, rollback, and secure-coding support.

##### ByteDance Seed / Seed-Coder

- `Homepage`: https://seed.bytedance.com/direction/llm
- `Label`: `Strong adjacent`
- `Focused area`: code models, code-data curation, generation, completion, editing, reasoning, software-engineering tasks, agents, inference efficiency, and open models.
- `Human-factor relevance`: Seed is the model/research layer beneath developer products. Model-centric data curation raises provenance and feedback-loop questions; faster generation changes review pressure but does not establish correctness. Track downstream use in Trae and enterprise tooling separately from benchmark results.
- `Sources`: https://seed.bytedance.com/direction/llm ; https://seed.bytedance.com/en/blog/seed-coder-open-sourced-llm-based-code-data-building-method-validated ; https://github.com/ByteDance-Seed/Seed-Coder.

#### Ant Group (蚂蚁集团)

##### Ant Ling / LingGuang (Ant Ling / 灵光) / Privacy-Preserving AI

- `Homepage`: https://www.antgroup.com/en/technology
- `Label`: `Strong adjacent`
- `Focused area`: financial technology, privacy-preserving AI, enterprise AI services, assistant workflows, and natural-language app generation.
- `Human-factor relevance`: Ant Group is a strong watch actor because financial and consumer contexts require trust, privacy, and user comprehension. Natural-language-to-app workflows raise software-security questions around auth, data flow, and permissions.

##### CodeFuse

- `Homepage`: https://codefuse.ai/
- `Label`: `Core/strong adjacent`
- `Focused area`: code models and AI-native software development across requirements, coding, testing, build, deployment, operations, insight analysis, IDEs, DevOps, and agent frameworks.
- `Human-factor relevance`: CodeFuse is a direct full-lifecycle China node. Its public record is valuable for studying enterprise human feedback, how agents cross lifecycle boundaries, and whether DevOps and testing integrations produce auditable evidence rather than only more generated artifacts.
- `Activities / evidence`: CodeFuse models and IDE plugins; CodeFuse-DevOps, TestGPU, muAgent, and full-lifecycle tooling.
- `Sources`: https://codefuse.ai/aboutDocs/aboutdocs/ ; https://github.com/codefuse-ai.

#### DeepSeek (深度求索)

##### Code Models And Open-Weight Ecosystem

- `Homepage`: https://platform.deepseek.com/api-docs
- `Label`: `Strong adjacent`
- `Focused area`: code models, open-weight models, reasoning models, developer/security workflows.
- `Human-factor relevance`: DeepSeek models are widely reused by developers and security researchers. Local deployment changes data-governance risk but does not solve generated-code security, alignment, provenance, or tool-permission issues.

#### Qihoo 360 / 360 Digital Security (奇虎360 / 360数字安全集团)

##### SOC / Security Products / AI Security Assistant Ecosystem

- `Homepage`: https://www.360.cn/
- `Label`: `Strong adjacent`
- `Focused area`: SOC products, threat intelligence, enterprise security, AI-assisted security operations, vulnerability research.
- `Human-factor relevance`: 360 is a likely source of Chinese SOC/product evidence about analyst-AI collaboration. Track how AI assistants are inserted into SOC workflows and how findings are validated by human analysts.

#### CAICT - China Academy of Information and Communications Technology (中国信息通信研究院)

##### AI Product Security And Evaluation

- `Homepage`: https://www.caict.ac.cn/english/
- `Label`: `Strong adjacent`
- `Focused area`: ICT policy, AI product evaluation, trusted AI testing, standards support, and certification.
- `Human-factor relevance`: CAICT can turn AI security concerns into evaluation programs and industry practice. Track what evidence vendors must provide and how evaluation results shape enterprise adoption.

#### TC260 - National Technical Committee 260 on Cybersecurity (全国网络安全标准化技术委员会)

##### Generative AI Security Requirements

- `Homepage`: https://www.tc260.org.cn/
- `Label`: `Core`
- `Focused area`: cybersecurity standards, generative-AI service security requirements, training-data security, model security, content labeling, and supply-chain assessment.
- `Human-factor relevance`: TC260 shapes what providers must document and review before deployment. Track requirements that force human review of training data, model outputs, supply-chain risk, complaint handling, and security assessments.

#### Cyberspace Administration of China (国家互联网信息办公室)

##### Generative AI Service Governance

- `Homepage`: https://www.cac.gov.cn/
- `Label`: `Core`
- `Focused area`: public generative-AI service regulation, algorithm filing, provider responsibility, security assessment, and content governance.
- `Human-factor relevance`: CAC policy shapes the organizational human layer around LLM deployment in China: approval, accountability, complaint mechanisms, security review, and when a service can be public.

#### China Information Technology Security Evaluation Center (中国信息安全测评中心)

##### Security Evaluation / Procurement Assurance

- `Homepage`: https://www.itsec.gov.cn/
- `Label`: `Strong adjacent`
- `Focused area`: information security evaluation, assurance, procurement-related security, testing, and certification.
- `Human-factor relevance`: This actor matters for institutional trust. Security evaluation decisions influence which AI tools enterprises and public bodies trust, deploy, or ban.

#### Qi-Anxin (奇安信)

##### AI-Enabled Cybersecurity System / AISOC

- `Homepage`: https://www.qianxin.com/topics/aiforsecurity
- `Label`: `Strong adjacent`
- `Focused area`: QAX-GPT-backed AI for security, AISOC, alert-noise reduction, incident response, EDR/SOC product linkage, and enterprise security operations.
- `Human-factor relevance`: Qi-Anxin should be mapped to the AI-for-security/SOC topic page rather than the company homepage. Track how analysts validate generated incident narratives and whether AI reduces or simply reshapes false-positive work.
- `Sources`: https://www.qianxin.com/topics/aiforsecurity.

#### NSFOCUS (绿盟科技)

##### Network Detection And Response

- `Homepage`: https://nsfocusglobal.com/products/network-detection-and-response/
- `Label`: `Strong adjacent`
- `Focused area`: AI-driven network detection and response, investigation, response, operation, network/data/5G/cloud/industrial-control traffic monitoring.
- `Human-factor relevance`: NSFOCUS should be tracked through analyst-facing NDR/SOC surfaces, not the corporate homepage. Track how AI-driven investigation presents evidence to humans.
- `Activities / evidence`: NSFOCUS Agentic SOC / ASOC discussion should be recorded as activity until a durable product unit page is mapped.
- `Sources`: https://nsfocusglobal.com/products/network-detection-and-response/ ; https://blog.nsfocus.net/%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E5%8D%8F%E5%90%8C%EF%BC%8C%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E5%BC%80%E5%90%AFagentic-soc%E6%96%B0%E8%8C%83%E5%BC%8F/.

#### VenusTech (启明星辰)

##### ADLab - Active Defense Laboratory

- `Homepage`: https://www.venustech.com.cn/new_type/cxtd/
- `Label`: `Strong adjacent`
- `Focused area`: offensive/defensive security research, basic security, 5G security, AI + security, industrial-control security, vehicle security, cloud security, mobile/IoT security, wireless security, and advanced threats.
- `Human-factor relevance`: VenusTech should be represented through ADLab, a named innovation/security research lab, rather than the corporate homepage. Track how research-lab outputs enter SOC products and analyst workflows.
- `Sources`: https://www.venustech.com.cn/new_type/cxtd/.

#### Sangfor (深信服)

##### Security GPT / Security Operation GPT

- `Homepage`: https://www.sangfor.com/cybersecurity/innovations/security-gpt
- `Label`: `Strong adjacent`
- `Focused area`: generative-AI security operations assistant, Detection GPT, Security Operation GPT, assisted operation, autonomous investigation, alert analysis, response recommendations, and proactive response actions.
- `Human-factor relevance`: Sangfor is directly relevant to SOC human factors because Security GPT exposes a chat-based analyst workflow and an autonomous-operation path. Track approval timing, evidence display, and whether human operators can inspect why an alert is considered an incident.
- `Sources`: https://www.sangfor.com/cybersecurity/innovations/security-gpt ; https://www.sangfor.com.cn/AIfirst/AIsec.

#### Topsec (天融信)

##### LLM Security Gateway System

- `Homepage`: https://www.topsecgroup.com/products/TopLMG.html
- `Label`: `Strong adjacent`
- `Focused area`: large-model session parsing, application/API protection, prompt-injection protection, AI recognition, and value-oriented content filtering for large-model applications.
- `Human-factor relevance`: Topsec should be represented here by the LLM gateway rather than the corporate homepage. Track how enterprise admins configure policies and interpret blocked or allowed agent/model actions.
- `Sources`: https://www.topsecgroup.com/products/TopLMG.html.

#### DBAPPSecurity (安恒信息)

##### Hengnao Security Domain Model And AI Security Services

- `Homepage`: https://www.dbappsecurity.com/service/
- `Label`: `Strong adjacent`
- `Focused area`: security vertical large model, AI model risk evaluation, AI security consulting, security operations, red/blue/purple-team services, and AI-assisted service delivery.
- `Human-factor relevance`: DBAPPSecurity should be mapped to its service/model page rather than the company homepage. Track how AI-assisted service teams validate results and communicate uncertainty to customers.
- `Sources`: https://www.dbappsecurity.com/service/.

##### DBAPPSecurity Threat Intelligence Center

- `Homepage`: https://ti.dbappsecurity.com.cn/
- `Label`: `Strong adjacent`
- `Focused area`: threat intelligence aggregation, network-threat analysis, APT tracking, vulnerability intelligence, IOC APIs, and AI-assisted intelligence judgment.
- `Human-factor relevance`: Keep threat intelligence separate from AI model/security services because analyst trust problems differ: source provenance, attribution confidence, and IOC context matter more than generated remediation.
- `Sources`: https://ti.dbappsecurity.com.cn/.

#### Chaitin Tech (长亭科技)

##### ChaitinAI And Insight

- `Homepage`: https://www.chaitin.cn/en/
- `Label`: `Strong adjacent`
- `Focused area`: security-enhanced LLM, AI vulnerability risk management, web security, vulnerability research, application security, and attack-defense technology.
- `Human-factor relevance`: Chaitin is relevant because it exposes AI-specific security products alongside expert vulnerability work. Track how AI-assisted findings are validated by human auditors and whether customer-facing reports remain reproducible.
- `Sources`: https://www.chaitin.cn/en/.

#### Knownsec (知道创宇)

##### Threat Intelligence / Incident Response

- `Homepage`: `To verify - specific threat-intelligence or incident-response unit page not located`
- `Label`: `Strong adjacent`
- `Focused area`: threat intelligence, vulnerability research, incident response, and cloud/security services.
- `Human-factor relevance`: Knownsec should be tracked for threat-intelligence workflows. LLMs can summarize intelligence, but human analysts must validate sources, attribution, and operational relevance.

#### Hillstone Networks (山石网科)

##### Hillstone iSource / Network Security Management

- `Homepage`: https://www.hillstonenet.com/products/network-security-management/
- `Label`: `Strong adjacent`
- `Focused area`: AI-powered XDR, network security management, threat intelligence, cloud/network/endpoint correlation, and SOC tooling.
- `Human-factor relevance`: Hillstone should be mapped to iSource/network-security management rather than the corporate homepage. Track whether generated explanations are grounded in packet/log evidence and whether analysts can inspect correlation logic.
- `Sources`: https://www.hillstonenet.com/products/network-security-management/ ; https://www.hillstonenet.com/wp-content/uploads/Hillstone_iSource-2.0R5_EN.pdf.

#### ThreatBook (微步在线)

##### ThreatBook ATI / Advanced Threat Intelligence

- `Homepage`: https://threatbook.io/product/threatbook-ati
- `Label`: `Strong adjacent`
- `Focused area`: advanced threat intelligence, IOC analysis, APAC threat coverage, curated detection rules, security-stack feeds, and analyst-facing intelligence portals.
- `Human-factor relevance`: ThreatBook is relevant because AI summarization can distort attribution. Track source transparency, confidence labels, and analyst over-trust in generated actor narratives.
- `Sources`: https://threatbook.io/product/threatbook-ati ; https://www.threatbook.com/en.

##### Flocks Agentic SecOps Platform

- `Homepage`: https://threatbook.io/
- `Label`: `Strong adjacent`
- `Focused area`: agentic SecOps, multi-agent triage/correlation/response, tool coordination, and AI-agent security.
- `Human-factor relevance`: Keep Flocks separate from ATI because it is an agentic operation surface, not only a threat-intelligence feed. Track human-in-the-loop checkpoints, scope controls, and response approvals.
- `Sources`: https://threatbook.io/.

#### Tophant (斗象科技)

##### AI-Native Online Security Operations Platform

- `Homepage`: https://www.tophant.com/about
- `Label`: `Strong adjacent`
- `Focused area`: AI-era intelligent security platform, online security operations, AI agents, white-hat community collaboration, attack-defense exercise platforms, and AI/agent protection.
- `Human-factor relevance`: Tophant is relevant to human prioritization in exposure management and attack-defense exercises. Track whether teams can inspect reasoning behind AI-generated risk rankings and whether exercise platforms audit participant behavior.
- `Sources`: https://www.tophant.com/about ; https://www.tophant.com/.

#### Zhipu AI (智谱AI)

##### ChatGLM / GLM Model Platform

- `Homepage`: https://open.bigmodel.cn/
- `Label`: `Strong adjacent`
- `Focused area`: Chinese LLM services, code and agent capabilities, enterprise AI platform, safety evaluations.
- `Human-factor relevance`: Zhipu should be tracked for Chinese-language coding and agent behavior, developer trust, public-service compliance, and model behavior under cyber/security prompts.

#### Moonshot AI (月之暗面)

##### Kimi

- `Homepage`: https://www.kimi.com/help/getting-started/overview
- `Label`: `Strong adjacent`
- `Focused area`: long-context Chinese LLMs, productivity workflows, coding/document analysis.
- `Human-factor relevance`: Kimi is relevant because long context changes software-security workflows: users may upload larger codebases or documents, making privacy, context provenance, and summary distortion central.

#### MiniMax (稀宇科技)

##### Model Platform

- `Homepage`: https://www.minimaxi.com/
- `Label`: `Watch`
- `Focused area`: consumer and enterprise LLM services, model platform, agents.
- `Human-factor relevance`: MiniMax should be watched for user-facing agent and assistant workflows. Human factors include how non-expert users interpret generated code or security advice.

#### Baichuan (百川智能)

##### Model Platform

- `Homepage`: https://www.baichuan-ai.com/
- `Label`: `Watch`
- `Focused area`: Chinese foundation models, enterprise deployment, and model-platform governance.
- `Human-factor relevance`: Track whether safety evaluations include secure coding, cyber misuse, and human-facing explanation quality.

#### SenseTime (商汤科技)

##### Model And AI Platform Ecosystem

- `Homepage`: https://www.sensetime.com/
- `Label`: `Watch`
- `Focused area`: multimodal AI, enterprise AI, model services, and AI safety participation.
- `Human-factor relevance`: SenseTime's relevance is multimodal and enterprise deployment. Watch future agent systems that combine visual UI control with code/security tasks.

#### iFlytek (科大讯飞)

##### Spark / AI Assistant Ecosystem

- `Homepage`: https://xinghuo.xfyun.cn/
- `Label`: `Watch`
- `Focused area`: Chinese-language AI assistants, education/workplace AI, model platform.
- `Human-factor relevance`: iFlytek is relevant to education and public-facing AI, especially whether AI-assisted secure-coding education or cybersecurity training appears in its ecosystem.

#### 01.AI (零一万物)

##### Yi Model Family

- `Homepage`: https://github.com/01-ai/yi
- `Label`: `Watch`
- `Focused area`: Chinese open/model platform ecosystem, Yi model family, and developer adoption.
- `Human-factor relevance`: 01.AI should be watched for open-model use in local developer/security tooling and whether smaller/open models are used without adequate evaluation.
- `Sources`: https://github.com/01-ai/yi ; https://platform.01.ai/termsPage.html.

### China: Universities, Labs, Research Institutes, And Researchers

#### Tsinghua University (清华大学)

##### Institute for Network Sciences and Cyberspace (网络科学与网络空间研究院)

- `Homepage`: https://www.insc.tsinghua.edu.cn/inscen/
- `Label`: `Core`
- `People`: Redbud student team, Blue-Lotus CTF/security ecosystem, INSC faculty and students.
- `Focused area`: network science, cyberspace security, network/system security, cryptography, network applications/security, and competition-based security education.
- `Human-factor relevance`: INSC is a core China signal because its contest work evaluates human team performance: attack sample construction, reproduction, technical defense, and report quality.
- `Activities / evidence`: Tianwang Cup large-model track, Redbud team, Blue-Lotus CTF activity.
- `Sources`: https://www.insc.tsinghua.edu.cn/inscen/ ; https://www.insc.tsinghua.edu.cn/info/1183/4112.htm.

##### IIIS Xu Wei Research Group (交叉信息研究院许伟课题组)

- `Homepage`: https://iiis.tsinghua.edu.cn/en/Research/Research_Groups/xuwei_0709.htm
- `Label`: `Strong adjacent`
- `Focused area`: secure and robust AI applications, AI security, privacy-preserving applications, distributed LLM training and inference.
- `Human-factor relevance`: This group shapes deployment conditions: local/private inference, privacy-preserving AI, AI security, and hallucination/jailbreak risk in practical applications.

##### Institute for AI International Governance (人工智能国际治理研究院)

- `Homepage`: https://aiig.tsinghua.edu.cn/en/About/Overview.htm
- `Label`: `Strong adjacent`
- `Focused area`: AI governance, international cooperation, policy frameworks, and AI governance forums.
- `Human-factor relevance`: AIIG should be kept separate from technical cyber labs. It is relevant to responsibility, auditing, filing/approval norms, and governance of public LLM services.

##### T-ISE - Intelligent Software Engineering Research Group (智能化软件工程课题组)

- `Homepage`: https://collegeai.tsinghua.edu.cn/en/Research/Research_Groups/Tsinghua_Intelligent_Software_Engineering_Lab.htm
- `Label`: `Core`
- `People`: Jia Li (PI), Ge Li, Zhi Jin and collaborators.
- `Focused area`: AI for software engineering and software engineering for AI; reliable, efficient and secure code generation, testing and repair; hallucination, alignment, code models, and repository-grounded evaluation.
- `Human-factor relevance`: T-ISE is almost exactly the broadened scope of this page. It should be a primary China node for studying how developers use reliable code generation and how SE methods make AI systems performant, efficient, secure, evaluable, and maintainable.
- `Activities / evidence`: DevEval, EvoCodeBench, aiXcoder, code editing/search/translation, poisoning and detection, real-repository evaluation.
- `Sources`: https://collegeai.tsinghua.edu.cn/en/Research/Research_Groups/Tsinghua_Intelligent_Software_Engineering_Lab.htm ; https://lj2lijia.github.io/.

##### Knowledge Engineering Group / CodeGeeX (知识工程实验室)

- `Homepage`: https://keg.cs.tsinghua.edu.cn/
- `Label`: `Strong adjacent`
- `People`: Jie Tang and KEG/CodeGeeX collaborators.
- `Focused area`: knowledge engineering, foundation models, code models, multilingual generation, developer tools, and open model ecosystems.
- `Human-factor relevance`: CodeGeeX is a major China-facing code-model and deployment line. Track multilingual developer behavior, privacy and provenance, IDE integration, suggestion review, and whether model evaluation predicts repository work.
- `Sources`: https://keg.cs.tsinghua.edu.cn/ ; https://keg.cs.tsinghua.edu.cn/codegeex/index_zh.html.

#### Fudan University (复旦大学)

##### System Software and Security Lab (系统软件与安全实验室) / Whitzard-AI

- `Homepage`: https://mi-zhang-fdu.github.io/index.html
- `Label`: `Core`
- `People`: Mi Zhang and Whitzard-AI / SSS Lab contributors.
- `Focused area`: LLM/MM-LLM security, agent security, intelligent system security, ML/DL security, AI for security, and Chinese-language safety evaluation.
- `Human-factor relevance`: This is a primary China group for Chinese-language LLM safety evaluation. JADE should be treated as an activity under the Fudan SSS/Whitzard-AI profile, not as the profile itself.
- `Activities / evidence`: JADE safety evaluation platform, JADE-DB, TC260 standards participation, CS-Eval collaboration.
- `Sources`: https://mi-zhang-fdu.github.io/index.html ; https://whitzard-ai.github.io/jade_en.html ; https://cs-eval.com/.

##### Software Engineering Lab / CodeWisdom (软件工程实验室)

- `Homepage`: https://www.se.fudan.edu.cn/
- `Label`: `Core`
- `People`: Xin Peng, Wenyun Zhao and CodeWisdom collaborators.
- `Focused area`: AI4SE and SE4AI; intelligent development and operations, program analysis and testing, repository mining, software supply-chain governance, AI-system engineering, inference/compiler optimization, robotics, embedded and industrial software.
- `Human-factor relevance`: This is one of the broadest China records in the target space. It connects human-machine collaborative development with quality, maintenance, operations, supply chains, AI-system reliability and efficiency, and deployment in enterprise and industrial contexts.
- `Activities / evidence`: code digital twins and context; repository-scale assistance; program analysis plus LLMs; AIOps; software-supply-chain risk; AI-system quality and efficient deployment.
- `Sources`: https://www.se.fudan.edu.cn/ ; http://cspengxin.github.io/.

#### Peking University (北京大学)

##### Knowledge Computing Lab (知识计算实验室)

- `Homepage`: https://seeeeeeven7.github.io/kcl-homepage/
- `Label`: `Strong adjacent`
- `Focused area`: code LLMs, LLM evaluation, programming-language comprehension, multimodal LLMs, CodeShell, and human-machine integration.
- `Human-factor relevance`: PKU KCL is relevant to developer-facing code LLMs and evaluation. Future mapping should ask whether CodeShell-style systems are studied with human developers, not only benchmarked.

##### Software Engineering Institute (软件工程研究所)

- `Homepage`: https://www.sei.pku.edu.cn/About.htm
- `Label`: `Strong adjacent`
- `Focused area`: software engineering, systems engineering, knowledge engineering, programming languages, and high-confidence software.
- `Human-factor relevance`: PKU-SEI provides the institutional software-engineering context for OSS-Lab and KCL work.

##### OSS-Lab (开源软件数据分析实验室)

- `Homepage`: https://osslab-pku.org/
- `Label`: `Strong adjacent`
- `Focused area`: open-source software analytics, repository mining, developer behavior, and software ecosystems.
- `Human-factor relevance`: OSS-Lab is a natural China node for studying whether AI coding changes maintainer burden, PR review behavior, vulnerability fix patterns, and contributor dynamics.

##### Laboratory For Future Networks / Hui Li Group (未来网络实验设施 / 李挥团队)

- `Homepage`: https://www.ece.pku.edu.cn/en/info/1029/1429.htm
- `Label`: `Core/strong adjacent`
- `People`: Hui Li, Bin Wang and collaborators.
- `Focused area`: software engineering, networked systems, LLM-assisted security-code generation, sensitive-information leakage detection, directed fuzzing, and multi-agent security.
- `Human-factor relevance`: This line joins repository engineering and security with agent workflows. Track how developers and security reviewers interpret leakage findings, fuzzing guidance, and generated security code, and how evidence is reproduced.
- `Sources`: https://www.ece.pku.edu.cn/en/info/1029/1429.htm.

#### Shanghai Jiao Tong University (上海交通大学)

##### LLM for Software Engineering Lab (大语言模型软件工程实验室)

- `Homepage`: https://base.sjtu.edu.cn/home/
- `Label`: `Strong adjacent`
- `People`: Beijun Shen, Xiaodong Gu, Yuling Shi and LLMSE members.
- `Focused area`: large language models for code, code generation, code translation, defect detection, and repair.
- `Human-factor relevance`: SJTU LLMSE is a primary China watch group for developer interaction with code LLMs, generated repair review, and repository-level coding assistance.

##### GoSec

- `Homepage`: https://gosec.sjtu.edu.cn/
- `Label`: `Strong adjacent`
- `Focused area`: system security, software security, trusted execution, binary analysis, and secure compilation.
- `Human-factor relevance`: GoSec supplies the low-level software-security substrate for future human-LLM reverse-engineering and binary-analysis work.

##### NSEC - Network Security and Privacy Protection Lab (网络安全与隐私保护实验室)

- `Homepage`: https://nsec.sjtu.edu.cn/
- `Label`: `Strong adjacent`
- `Focused area`: network security, privacy protection, mobile/wireless network security.
- `Human-factor relevance`: NSEC is relevant to SOC/network-security uses of LLMs, especially analyst interpretation of network telemetry.

##### IPADS - Institute Of Parallel And Distributed Systems

- `Homepage`: https://ipads.se.sjtu.edu.cn/
- `Label`: `Strong adjacent`
- `People`: Haibo Chen and IPADS collaborators.
- `Focused area`: operating systems, distributed systems, virtualization, architecture, security, reliability, performance, and system software.
- `Human-factor relevance`: IPADS is a high-priority OS/systems discovery node. Add direct LLM entries when work uses models for kernel/configuration/code generation, diagnosis, or optimization; evaluate generated changes for correctness, performance portability, operability, and expert review.
- `Sources`: https://ipads.se.sjtu.edu.cn/.

##### Efficient Computing Hardware And System Lab

- `Homepage`: https://sites.gc.sjtu.edu.cn/zouan/
- `Label`: `Core/strong adjacent`
- `People`: An Zou and collaborators.
- `Focused area`: architecture, circuits, low-level software, efficient/reliable computing, compilers, CUDA programming, and LLM-assisted systems development.
- `Human-factor relevance`: This line extends the map beyond application code. AI-assisted CUDA and low-level optimization requires expert-visible equivalence, numerical validation, workload/hardware disclosure, and maintainable generated kernels.
- `Activities / evidence`: 2026 work on LLMs for CUDA programming.
- `Sources`: https://sites.gc.sjtu.edu.cn/zouan/.

#### Zhejiang University (浙江大学)

##### Ubiquitous System Security Lab (泛在系统安全实验室)

- `Homepage`: https://usslab.org/contact.html
- `Label`: `Strong adjacent`
- `Focused area`: IoT security, embedded system security, ubiquitous system security, and attack/defense.
- `Human-factor relevance`: ZJU USSLab is relevant to human-facing analysis of cyber-physical, IoT, and embedded environments where model explanations can hallucinate device state.

##### Network System Security And Privacy Lab

- `Homepage`: https://nesa.zju.edu.cn/index.html
- `Label`: `Strong adjacent`
- `Focused area`: data-driven security, AI and security, software/system security, and big-data mining.
- `Human-factor relevance`: NESA should be tracked for AI/security work that could become SOC or analyst tooling.

##### LLM4VFD / Vulnerability Fix Detection Line

- `Homepage`: `To verify - durable lab host not located`
- `Label`: `Strong adjacent`
- `Focused area`: vulnerability fix detection using code change intention, artifacts, history, and LLM-generated analysis.
- `Human-factor relevance`: Keep this as a project/activity line until the durable lab host is verified. It reports a security-expert user study, so it matters for whether LLM-generated explanations help humans classify vulnerability fixes more efficiently.
- `Sources`: https://colab.ws/articles/10.1145%2F3715738.

#### University of Hong Kong (香港大学)

##### JC STEM Lab of Intelligent Cybersecurity (JC STEM 智能网络安全实验室)

- `Homepage`: https://sec.hku.hk/
- `Label`: `Strong adjacent`
- `Focused area`: machine learning for security, security/privacy/robustness of machine learning, intelligent cybersecurity, and AI-driven security/software engineering.
- `Human-factor relevance`: HKU is a Hong Kong bridge between AI and cybersecurity. Track for human-facing vulnerability analysis, code repair, and cyber operations tools.

#### University of Chinese Academy of Sciences (中国科学院大学)

##### School of Computer And Control Engineering

- `Homepage`: https://scce.ucas.ac.cn/index.php/en/about-us/introduction
- `Label`: `Strong adjacent`
- `Focused area`: computer and control engineering, information security technology, data-control-bus technology, and UCAS computing education/research infrastructure.
- `Human-factor relevance`: UCAS should not be represented by the university root page. SCCE is the concrete school-level host to map before trying to assign CS-Eval authors to a smaller lab.
- `Activities / evidence`: CS-Eval participation should be treated as benchmark/platform evidence until the exact UCAS lab host is verified.
- `Sources`: https://scce.ucas.ac.cn/index.php/en/about-us/introduction ; https://cs-eval.com/.

##### CS-Eval Project

- `Homepage`: https://cs-eval.com/
- `Label`: `Core/strong adjacent`
- `Focused area`: bilingual LLM cybersecurity capability evaluation, 11 cybersecurity categories, 42 subcategories, knowledge/application tasks, and benchmark-driven model comparison.
- `Human-factor relevance`: This remains a project heading because the durable UCAS lab host is not yet mapped. It matters for education and enterprise adoption because benchmark structure shapes what humans believe a cyber-capable model can do.
- `Sources`: https://cs-eval.com/ ; https://github.com/CS-EVAL/CS-Eval.

#### Chinese Academy of Sciences (中国科学院)

##### Institute of Information Engineering (信息工程研究所)

- `Homepage`: https://english.iie.cas.cn/
- `Label`: `Watch`
- `Focused area`: national cybersecurity research, vulnerability analysis, AI security, and benchmark infrastructure.
- `Human-factor relevance`: CAS IIE is a high-priority watch institution for national evaluation infrastructure and analyst-facing security-AI systems.

##### Institute Of Computing Technology: Advanced Computer Systems And Processor-Chip Labs

- `Homepage`: https://acs.ict.ac.cn/english/aboutacs_acs_en/overview_acs_en/
- `Label`: `Core/strong adjacent`
- `People`: Qi Guo and collaborators across the Center for Advanced Computer Systems and processor-chip research.
- `Focused area`: AI/system software-hardware co-design, open-source systems and chips, compilers, OS configuration, ML for systems, LLM-generated high-performance kernels and toolchains, and benchmark engineering.
- `Human-factor relevance`: This is a key China node for efficiency and optimization. Claims must retain semantic correctness, workload/hardware context, search cost, energy, portability, and human maintenance; automatically generated OS/compiler settings can create hard-to-diagnose operational failures even when benchmarks improve.
- `Activities / evidence`: LLM-guided OS-kernel configuration; generated compiler toolchains; high-performance matrix multiplication; LLM-oriented compiler and IR data.
- `Sources`: https://acs.ict.ac.cn/english/aboutacs_acs_en/overview_acs_en/ ; https://novel.ict.ac.cn/qguo/ ; https://sklp.ict.ac.cn/xwzx/202505/t20250509_542558.html.

#### HKUST - Hong Kong University of Science and Technology (香港科技大学)

##### Cybersecurity Lab

- `Homepage`: https://cse.hkust.edu.hk/pg/research/labs/
- `Label`: `Watch`
- `Focused area`: cybersecurity research inside HKUST CSE, including software/system security topics that may later host LLM-assisted vulnerability work.
- `Human-factor relevance`: This replaces the generic CSE homepage. The current source is HKUST CSE's research-lab directory; future work should follow the directory into individual lab subpages and map papers there.
- `Sources`: https://cse.hkust.edu.hk/pg/research/labs/.

##### Human-Computer Interaction Initiative

- `Homepage`: https://cse.hkust.edu.hk/pg/research/labs/
- `Label`: `Watch`
- `Focused area`: HCI and human-centered computing within HKUST CSE.
- `Human-factor relevance`: Track this separately from Cybersecurity Lab because human-AI/agent oversight evidence belongs in HCI, not in a generic HKUST entry.
- `Sources`: https://cse.hkust.edu.hk/pg/research/labs/.

##### Ren.AI Lab on Human-Centric Trustworthy Reasoning And Agents

- `Homepage`: https://cse.hkust.edu.hk/pg/research/labs/
- `Label`: `Strong adjacent`
- `Focused area`: human-centric trustworthy reasoning, agents, and AI systems.
- `Human-factor relevance`: This is the strongest HKUST lab-directory signal for human-facing LLM agents. It should be prioritized for paper-to-lab mapping.
- `Sources`: https://cse.hkust.edu.hk/pg/research/labs/.

##### TACO Lab - Types, Abstraction, Compilers And Optimization

- `Homepage`: https://home.cse.ust.hk/~parreaux/
- `Label`: `Strong adjacent`
- `People`: Lionel Parreaux and TACO collaborators.
- `Focused area`: type systems, language abstraction, compilers, optimization, safety, reliability, and performance.
- `Human-factor relevance`: TACO is an assurance/efficiency node for AI-generated software and agent languages. Track whether types and abstractions make generated behavior comprehensible and whether compiler optimizations remain inspectable and portable.
- `Sources`: https://home.cse.ust.hk/~parreaux/.

##### Security And Machine Learning / LLM Security Group

- `Homepage`: https://home.cse.ust.hk/~dongdong/
- `Label`: `Core`
- `People`: Dongdong She, Shuai Wang and collaborators.
- `Focused area`: LLM and agent security, security of LLM harnesses, prompt injection against coding agents, semantic-cache attacks, LLMs for vulnerability discovery, program analysis, causality-based evaluation, and fuzzing.
- `Human-factor relevance`: This group spans both directions in the dossier. Track how developers understand harness and cache trust boundaries, how coding-agent attacks are surfaced, and how security findings are reproduced and handed to maintainers.
- `Sources`: https://home.cse.ust.hk/~dongdong/ ; https://home.cse.ust.hk/~shuaiw/.

#### Chinese University of Hong Kong (香港中文大学)

##### Computer Security Lab

- `Homepage`: https://seclab.cse.cuhk.edu.hk/
- `Label`: `Watch`
- `Focused area`: security and privacy challenges in computer systems and applications, programming languages, software engineering, operating systems, and computer networks.
- `Human-factor relevance`: This is the specific CUHK security lab that should replace the generic CSE link. Track whether LLM-assisted analysis outputs are evaluated with human security analysts or developers.
- `Sources`: https://seclab.cse.cuhk.edu.hk/.

##### ARISE Lab - Automated Reliable Intelligent Software Engineering

- `Homepage`: https://ariselab.cse.cuhk.edu.hk/
- `Label`: `Strong adjacent`
- `People`: Michael R. Lyu and ARISE members.
- `Focused area`: automated reliable intelligent software engineering, software quality, code intelligence, AIOps, failure analysis, cloud reliability, LLM training failures, UI code, and reliability engineering for code models.
- `Human-factor relevance`: ARISE is a primary reliability node: human-factor questions include how developers review generated tests, explanations and UI code; how operators use RAG/root-cause assistance; and whether LLM training and production failures become diagnosable and actionable.
- `Activities / evidence`: active projects on evaluation and reliability engineering for LLM code intelligence; AIOps and LLM-training-failure diagnosis; interactive code-generation evaluation.
- `Sources`: https://ariselab.cse.cuhk.edu.hk/ ; https://research.cuhk.edu.hk/en/persons/rung-tsong-michael-lyu/.

##### Human-Computer Interaction Research Area

- `Homepage`: https://www.cse.cuhk.edu.hk/research/artificial-intelligence/human-computer-interaction/
- `Label`: `Strong adjacent`
- `Focused area`: HCI, AR/VR, visualization, human-centered AI, and interactive systems.
- `Human-factor relevance`: CUHK HCI should be separate from security/software labs. Agent approval, oversight, trust, and warning design belong here unless a specific security-HCI lab host is found.
- `Sources`: https://www.cse.cuhk.edu.hk/research/artificial-intelligence/human-computer-interaction/.

##### MoE-Microsoft Key Laboratory of Human-Centric Computing And Interface Technologies

- `Homepage`: https://moe.se.cuhk.edu.hk/en/content/mission
- `Label`: `Strong adjacent`
- `Focused area`: human-centric computing, interface technologies, computer vision, computer graphics, speech/multimodal HCI, multimedia retrieval, and wireless networking.
- `Human-factor relevance`: This is a named CUHK human-centric computing lab. Keep it separate from CSE HCI area because it is an institutional lab structure rather than a research-area listing.
- `Sources`: https://moe.se.cuhk.edu.hk/en/content/mission.

#### City University of Hong Kong (香港城市大学)

##### Information Security Research Area / Information Security Laboratory

- `Homepage`: https://www.cs.cityu.edu.hk/research/research-areas/information-security
- `Label`: `Watch`
- `Focused area`: information security, security/privacy faculty groups, and security laboratory activity within CityU CS.
- `Human-factor relevance`: This is the concrete CityU security host for future mapping. Track whether tools move from technical security evaluation into analyst/developer-facing workflows.
- `Sources`: https://www.cs.cityu.edu.hk/research/research-areas/information-security.

##### Human-Computer Interaction Group

- `Homepage`: https://www.cs.cityu.edu.hk/en/research/research-areas/human-computer-interaction-hci
- `Label`: `Strong adjacent`
- `Focused area`: HCI, user experience, human factors engineering, multimodal interaction, social computing, human-centered AI, explainable AI, and human-AI collaboration.
- `Human-factor relevance`: CityU HCI is directly relevant to agent oversight, trust calibration, and human-centered evaluation. Keep it separate from information security.
- `Sources`: https://www.cs.cityu.edu.hk/en/research/research-areas/human-computer-interaction-hci.

##### Software Engineering Research Area / Laboratory of Software Engineering And Methodology

- `Homepage`: https://www.cs.cityu.edu.hk/en/research/research-areas/software-engineering
- `Label`: `Watch`
- `Focused area`: software engineering, testing, program analysis, and security testing.
- `Human-factor relevance`: This is the CityU software-engineering host to watch for LLM-for-SE work that reaches developers.
- `Sources`: https://www.cs.cityu.edu.hk/en/research/research-areas/software-engineering.

##### Kowloon Interaction Center

- `Homepage`: https://klic.space/
- `Label`: `Watch`
- `Focused area`: HCI community building, cross-lab collaboration, interaction research at CityU.
- `Human-factor relevance`: KLIC is a named HCI group/community. It is adjacent to LLM security through human-AI interaction methods rather than security tooling itself.
- `Sources`: https://klic.space/.

#### Hong Kong Polytechnic University (香港理工大学)

##### Trustworthy AI And Autonomous Systems Laboratory

- `Homepage`: https://polyu-taslab.github.io/
- `Label`: `Watch`
- `Focused area`: trustworthy AI, autonomous systems, cybersecurity, human-system interaction, safety, reliability, and ethics.
- `Human-factor relevance`: TAS Lab is the most explicit PolyU human-AI/security lab found in this pass. Track trust, safety, and human-system interaction in autonomous/agentic settings.
- `Sources`: https://polyu-taslab.github.io/.

##### Internet And Mobile Computing Laboratory

- `Homepage`: https://web.comp.polyu.edu.hk/labimcl/index.html
- `Label`: `Watch`
- `Focused area`: internet and mobile computing, mobile/internet systems, and applied computing.
- `Human-factor relevance`: IMCL is relevant if LLM-assisted mobile or IoT security analysis becomes user-facing.
- `Sources`: https://web.comp.polyu.edu.hk/labimcl/index.html.

##### Advanced Network Monitoring And Measurement Laboratory

- `Homepage`: https://anemol.comp.polyu.edu.hk/
- `Label`: `Watch`
- `Focused area`: network monitoring, measurement, reliability, quality, and security-related network diagnosis.
- `Human-factor relevance`: ANEMOL is relevant to SOC/network-operator workflows where LLM summaries may interpret network evidence.
- `Sources`: https://anemol.comp.polyu.edu.hk/.

##### Database Research Group

- `Homepage`: https://dbgroup.comp.polyu.edu.hk/?page_id=20
- `Label`: `Watch`
- `Focused area`: database systems, information-system infrastructure, data integrity, and confidentiality.
- `Human-factor relevance`: Track if database/privacy/security work becomes LLM-assisted data-governance or security-review tooling.
- `Sources`: https://dbgroup.comp.polyu.edu.hk/?page_id=20.

#### Nanjing University (南京大学)

##### State Key Laboratory for Novel Software Technology

- `Homepage`: https://stuex.nju.edu.cn/en_/66/2c/c23274a353836/page.psp/1000/main.htm
- `Label`: `Watch`
- `Focused area`: novel software technology, software quality assurance, automation, operating systems, information security, intelligent software, and multimedia software.
- `Human-factor relevance`: This is the primary NJU lab-level host rather than the CS department homepage. Map LLM-for-SE papers here or to smaller groups below.
- `Sources`: https://stuex.nju.edu.cn/en_/66/2c/c23274a353836/page.psp/1000/main.htm.

##### Software Engineering Group

- `Homepage`: https://seg.nju.edu.cn/aboutSEG.jsp
- `Label`: `Strong adjacent`
- `Focused area`: software analysis, verification, testing, model-driven engineering, runtime verification, pointer analysis, and software trustworthiness.
- `Human-factor relevance`: SEG is the concrete NJU software-engineering group for future developer-facing LLM work.
- `Sources`: https://seg.nju.edu.cn/aboutSEG.jsp.

##### Intelligent Software Engineering Lab / Deep Learning Testing Group

- `Homepage`: https://nju-ise.github.io/
- `Label`: `Strong adjacent`
- `Focused area`: intelligent software engineering, testing deep-learning systems, AI infrastructure testing, deep-learning compilers, and reliable AI systems.
- `Human-factor relevance`: This lab is relevant to LLM/AI system reliability and to whether developers can interpret AI-infrastructure test evidence.
- `Sources`: https://nju-ise.github.io/.

##### LAMDA - Learning And Mining from DatA

- `Homepage`: https://www.lamda.nju.edu.cn/MainPage.ashx
- `Label`: `Strong adjacent`
- `Focused area`: machine learning, data mining, pattern recognition, information retrieval, and AI methods.
- `Human-factor relevance`: LAMDA is adjacent rather than software-security-specific; track it when AI evaluation, robustness, or model methods feed human-facing security systems.
- `Sources`: https://www.lamda.nju.edu.cn/MainPage.ashx.

##### NJU-LINK Lab - Large-scale Intelligence And Knowledge Lab

- `Homepage`: https://www.nju-link.com/en/
- `Label`: `Watch`
- `Focused area`: large language models, multimodal large models, embodied intelligence, world models, training, inference, and evaluation.
- `Human-factor relevance`: NJU-LINK is relevant to LLM/agent capability and evaluation; add security-specific evidence only when publications connect to cyber or developer workflows.
- `Sources`: https://www.nju-link.com/en/.

##### Nanjing University Large-Model Collaborative Innovation Center

- `Homepage`: https://cs.nju.edu.cn/lm/
- `Label`: `Core/strong adjacent`
- `People`: faculty and groups across NJU computer science, software, AI, systems, and formal methods; map individual work to the smaller host group when possible.
- `Focused area`: scalable LLM systems, efficient learning/platforms, code translation, scientific and embodied models, agents, neuro-symbolic reasoning, and automated formal proof for foundational software.
- `Human-factor relevance`: The center connects model/system infrastructure with code and proof. Track proof-author review, trusted kernels, reproducibility, system efficiency, and how generated proofs for seL4/distributed protocols change expert workload.
- `Activities / evidence`: 2026 neuro-symbolic automated proof work; code translation; large-model systems and agents.
- `Sources`: https://cs.nju.edu.cn/lm/.

#### Beihang University (北京航空航天大学)

##### State Key Laboratory of Software Development Environment

- `Homepage`: https://scse.buaa.edu.cn/info/1127/2316.htm
- `Label`: `Watch`
- `Focused area`: software development environment, internet/information/communication technologies, software tools, and software-development research infrastructure.
- `Human-factor relevance`: This is the Beihang software-systems lab host for high-assurance software questions. Human factors enter through review, certification, and acceptance of generated code or patches.
- `Sources`: https://scse.buaa.edu.cn/info/1127/2316.htm.

##### Computational Intelligence Laboratory

- `Homepage`: https://www.ci-lab.net/
- `Label`: `Watch`
- `Focused area`: efficient intelligent computing systems, machine-learning systems, systems for LLM inference, privacy computing systems, and hardware/software co-design.
- `Human-factor relevance`: CI Lab is relevant to deployment constraints around local/private LLM inference, where data governance and security review affect user trust.
- `Sources`: https://www.ci-lab.net/ ; https://www.ci-lab.net/research/.

##### Robust And Secure Vision Lab

- `Homepage`: https://rose-vision.github.io/
- `Label`: `Watch`
- `Focused area`: robust and secure visual perception, adversarial environments, safety-critical visual AI, autonomous driving, remote sensing, facial recognition, and public security.
- `Human-factor relevance`: ROSE Vision is adjacent to multimodal agent/security work; track if visual agents enter software/security operations or safety-critical approval workflows.
- `Sources`: https://rose-vision.github.io/.

#### Huazhong University of Science and Technology (华中科技大学)

##### ONE Lab

- `Homepage`: https://oneslab.github.io/
- `Label`: `Watch`
- `Focused area`: code intelligence, code LLMs, multimodal models, language models, UI intelligence, and trustworthy AI.
- `Human-factor relevance`: ONE Lab is the concrete HUST lab for code-LLM and UI-intelligence work. Track developer-facing automation, prompt/workflow design, and reliability evidence.
- `Sources`: https://oneslab.github.io/.

##### OS3Lab / LLM4S2 Project

- `Homepage`: https://github.com/HUSTSeclab/LLM4S2
- `Label`: `Watch`
- `Focused area`: LLM for system/software security, bug detection, fuzzing, decompilation, vulnerability analysis, and program repair.
- `Human-factor relevance`: Keep this as a project heading because a stable OS3Lab homepage was not located in this pass. It is still relevant because it explicitly says LLMs assist initial code analysis and reverse engineering rather than replace experts.
- `Sources`: https://github.com/HUSTSeclab/LLM4S2.

#### Wuhan University (武汉大学)

##### Evolving Systems Lab

- `Homepage`: https://whues.org/
- `Label`: `Watch`
- `Focused area`: system and IoT security, coding agents, agent and embodied-AI security, LLM + CodeQL vulnerability detection, intelligent software development, and trustworthy intelligent systems.
- `Human-factor relevance`: WHU-ES is a strong China watch node because it explicitly links LLMs to code/security workflows and agent security. Track whether its tools expose evidence that developers/security analysts can verify.
- `Sources`: https://whues.org/.

##### Trusted Computing And Security Lab

- `Homepage`: https://www.tcaslab.com/
- `Label`: `Strong adjacent`
- `Focused area`: trusted computing, security, AI security, aerospace information security, and trustworthy systems.
- `Human-factor relevance`: TC&S is relevant to trust and assurance in AI/security systems, especially where human operators must decide whether generated evidence is trustworthy.
- `Sources`: https://www.tcaslab.com/.

##### Data Security Lab

- `Homepage`: https://datasec.whu.edu.cn/
- `Label`: `Watch`
- `Focused area`: data security, privacy, and cybersecurity research.
- `Human-factor relevance`: Track data-security and privacy tooling that uses LLM summarization or classification, where human reviewers need source transparency.
- `Sources`: https://datasec.whu.edu.cn/.

##### Software Service Engineering And Application Lab

- `Homepage`: https://ssea-lab.github.io/
- `Label`: `Watch`
- `Focused area`: software service engineering, empirical software engineering, and domain-specific intelligent software services.
- `Human-factor relevance`: SSEA is relevant to LLM-for-SE human factors when software agents are studied as service-engineering tools used by developers.
- `Sources`: https://ssea-lab.github.io/.

#### Xidian University (西安电子科技大学)

##### Intelligent Information Processing Lab

- `Homepage`: https://iip-xdu.github.io/
- `Label`: `Watch`
- `Focused area`: credible AI, AIGC, intelligent information processing, and AI methods under the ISN State Key Laboratory.
- `Human-factor relevance`: IIP is the concrete Xidian AI/security-adjacent group identified in this pass. Track credible-AI and AIGC work that affects user trust and security decision-making.
- `Sources`: https://iip-xdu.github.io/.

##### School of Cyber Engineering

- `Homepage`: https://en.xidian.edu.cn/info/1003/2045.htm
- `Label`: `Watch`
- `Focused area`: cyber-security education, talent cultivation, teaching/research/industry integration, competitions, and cyber practice.
- `Human-factor relevance`: This is a school-level host rather than a lab, but it is still more precise than the university homepage. Use it for Xidian security-education and contest-culture evidence until smaller lab pages are mapped.
- `Sources`: https://en.xidian.edu.cn/info/1003/2045.htm.

##### Chenxi Zhang AIOps / LLM4Ops Research Line

- `Homepage`: https://zchenxi.github.io/
- `Label`: `Watch`
- `Focused area`: software engineering, AIOps, cloud-native systems, software testing, LLM4Ops, and AgentOps.
- `Human-factor relevance`: This is a researcher/group page rather than a lab page. Keep it because it is a concrete host for human-facing operations/developer automation questions at Xidian.
- `Sources`: https://zchenxi.github.io/.

#### Harbin Institute of Technology (哈尔滨工业大学)

##### HIT-SCIR - Research Center for Social Computing And Interactive Robotics

- `Homepage`: https://ir.hit.edu.cn/
- `Label`: `Watch`
- `Focused area`: social computing, interactive robotics, language understanding, knowledge mining, NLP, and Chinese-language AI systems.
- `Human-factor relevance`: HIT should be represented through SCIR rather than the university homepage for LLM/NLP work. Track whether Chinese-language agent/coding/security assistants are evaluated with humans.
- `Sources`: https://ir.hit.edu.cn/.

##### SCIR Trustworthy Generation Group

- `Homepage`: https://hit-scir-tg.netlify.app/
- `Label`: `Strong adjacent`
- `Focused area`: trustworthy generation, LLM safety, language models, and evaluation.
- `Human-factor relevance`: This is the more specific HIT LLM safety group signal. Track jailbreak, hallucination, and human evaluation evidence when it intersects software/security workflows.
- `Sources`: https://hit-scir-tg.netlify.app/.

#### University of Science and Technology of China (中国科学技术大学)

##### Computer Systems And Security Group

- `Homepage`: https://csslab-ustc.github.io/
- `Label`: `Strong adjacent`
- `Focused area`: computer systems, security, programming languages, compilers, type systems, verification, software engineering, and AI infrastructure.
- `Human-factor relevance`: CSS Group is the concrete USTC host for systems/software-security work. Track whether LLM outputs are paired with compiler/program-analysis evidence that humans can inspect.
- `Sources`: https://csslab-ustc.github.io/.

##### AlphaLab

- `Homepage`: https://alphalab-ustc.github.io/
- `Label`: `Watch`
- `Focused area`: foundation models, large language models, multimodal AI, reasoning, alignment, personalization, agentic AI, and trustworthy AI.
- `Human-factor relevance`: AlphaLab is an LLM/foundation-model lab; connect it to software security only when agentic AI, alignment, or evaluation work touches developer/security workflows.
- `Sources`: https://alphalab-ustc.github.io/.

##### Information Network Laboratory

- `Homepage`: https://if.ustc.edu.cn/english.php
- `Label`: `Watch`
- `Focused area`: information networks, network protocols, network security protocols, network teaching, and communications infrastructure.
- `Human-factor relevance`: InfoNet is relevant to SOC/network-security workflows if LLMs are used to explain protocol evidence or network telemetry.
- `Sources`: https://if.ustc.edu.cn/english.php.

#### Chinese AI Safety Network (中国人工智能安全网络)

##### China-Facing Safety Coordination

- `Homepage`: https://chinese-ai-safety.institute/
- `Label`: `Strong adjacent`
- `Focused area`: Chinese AI safety coordination, governance, safety attitudes, model deployment norms.
- `Human-factor relevance`: This is a network rather than a lab. Its role is shaping consensus about safety governance and model-service responsibility.

### China: Contest And Platform Evidence Without Stable Lab Mapping

#### Tianwang Cup (天网杯)

##### Large-Model Track

- `Homepage`: https://twcup.cverc.org.cn/
- `Label`: `Core/strong adjacent`
- `Focused area`: LLM security competition, prompt injection, jailbreak, data leakage, reliability, model supply-chain attack samples.
- `Human-factor relevance`: Tianwang Cup is a direct Chinese human-factor signal because scoring includes human-produced artifacts: attack samples, reproduction, report quality, and technical defense. When citing specific Tsinghua participation, map that activity back to Tsinghua INSC.
- `Sources`: https://twcup.cverc.org.cn/ ; https://www.insc.tsinghua.edu.cn/info/1183/4112.htm.

#### Alibaba AI Security Challenge (阿里云AI安全全球挑战赛)

##### AI Security Challenge

- `Homepage`: https://security.alibaba.com/
- `Label`: `Strong adjacent`
- `Focused area`: AI security challenge tasks, model attack and defense, security evaluation.
- `Human-factor relevance`: This belongs under Alibaba when enough source detail is available. It is useful contest evidence for how Chinese practitioners operationalize AI-security tasks and scoring.

#### AI Linghang Cup (AI领航杯)

##### AI + Security Track

- `Homepage`: `To verify`
- `Label`: `Watch`
- `Focused area`: AI + security competition, applied security innovation.
- `Human-factor relevance`: Keep as a project/contest heading until the durable host page is verified. Track whether it produces reusable datasets, reports, or training patterns for LLM-assisted security operations.

#### Jinlingguang Cup (金灵光杯)

##### Generative-AI Security Track

- `Homepage`: `To verify`
- `Label`: `Watch`
- `Focused area`: generative-AI security, model attack/defense, safety testing.
- `Human-factor relevance`: Keep as contest evidence for Chinese-language AI safety red-team practices; track whether judging values reproducibility and remediation guidance.

#### XCTF / CVE-Range Platforms (XCTF联赛 / CVE靶场)

##### CTF And Vulnerability-Range Platforms

- `Homepage`: https://www.xctf.org.cn/
- `Label`: `Watch`
- `Focused area`: CTF training, vulnerability ranges, AI-assisted attack/defense learning.
- `Human-factor relevance`: XCTF-style ranges define the learning environment for many Chinese security students and practitioners. Track whether platforms distinguish human skill from agent scaffolding as LLM agents enter CTF workflows.

### China: Main Focus Areas To Track

- Chinese-language cybersecurity evaluation: CS-Eval/CyberSec-Eval, SecBench-like efforts, LiveSecBench-style dynamic safety benchmarks, and contest datasets. Focus on whether tasks measure knowledge recall, reasoning, operational action, or human-usefulness.
- AI coding assistants and code models: Alibaba Qoder CN/Qwen, Tencent CodeBuddy, Huawei CodeArts, Baidu Comate, ByteDance Trae/Seed, Ant CodeFuse, DeepSeek-Coder, and academic code-model groups. Focus on requirements clarification, repository context, code privacy, generated dependency risk, test and review quality, maintenance, enterprise governance, and the difference between adoption telemetry and delivered value.
- AI4SE and SE4AI: Tsinghua T-ISE, Fudan CodeWisdom, SJTU LLMSE, CUHK ARISE, NJU ISE/large-model center, PKU groups, ByteDance SE Lab, and Ant CodeFuse. Focus on lifecycle coverage, software quality and reliability, hallucination and alignment, AI-system testing, observability, provenance, supply chains, and ownership.
- Systems, compilers, OS, and performance: CAS ICT, SJTU IPADS/efficient computing, Fudan systems/AI engineering, HUST OS3/ONE, Beihang, USTC, Huawei and domestic hardware/software ecosystems. Require semantic equivalence, workload and hardware provenance, energy/cost, portability, rollback, and expert review of generated configurations, kernels, and toolchains.
- Open-source and organizational work: PKU OSS-Lab, Fudan CodeWisdom, university-industry laboratories, Gitee/OpenAtom ecosystems, and large enterprise developer platforms. Study maintainer burden, review throughput, contributor attribution, licensing, team knowledge, and how agent-generated changes affect open-source governance.
- Model safety red teaming: JADE, Tianwang Cup large-model track, Tencent Zhuque, Alibaba/Tencent/Baidu/DeepSeek safety activity. Focus on prompt injection, jailbreaks, data leakage, content reliability, model supply-chain attacks, and how human judges score reports.
- SOC and security-vendor deployment: Qihoo 360, Qi-Anxin, NSFOCUS, Sangfor, Topsec, DBAPPSecurity, Chaitin, Knownsec, ThreatBook, Alibaba/Tencent/Huawei/Baidu cloud security. Focus on analyst workload, false positives, incident explanation quality, and Chinese enterprise compliance.
- Governance and standards: CAC generative-AI measures, TC260 basic security requirements, CAICT vulnerability/security evaluation, Chinese AI Safety Network. Focus on how security assessment requirements shape human approval, content review, and operational auditability.
- Education and expertise: CTF/range platforms, university SE/PL/OS courses, coding-agent use by students and professional developers, and Chinese-language documentation. Measure unaided learning, debugging and review skill, not only completion.
- Research gap: China has strong technical, platform, benchmark, contest, and enterprise signals, but public direct human-subject and longitudinal studies of coding, review, maintenance, AIOps, optimization, secure coding, SOC, reverse engineering, and bug-bounty triage remain much less visible than in the U.S. This is a high-value bilingual and cross-organizational research opportunity.

## USA-China Comparison For Human Factors

| Human-factor layer | United States | China | Research implication |
| --- | --- | --- | --- |
| Developer productivity and work design | Google/DORA, Microsoft Research, GitHub, JetBrains, IBM and academic HCI/SE groups provide telemetry, surveys, interviews and controlled studies | Large deployment surfaces through Qoder CN, CodeBuddy, CodeArts, Comate, Trae and CodeFuse; public causal and longitudinal human evidence is thinner | Use comparable professional tasks and organizational measures; separate acceptance/adoption from correctness, review, delivery, learning and maintenance. |
| Correctness, testing and repair | Strong PL/SE/formal-methods ecosystem plus code-agent, program-repair and developer-study lines | Strong AI4SE groups at Tsinghua, Fudan, SJTU, NJU, CUHK, HKUST and industry; many benchmark/tool results | Compare independent oracles, human review effort, repair acceptance, regression rates and delayed maintenance, including bilingual requirements and codebases. |
| Performance, compilers and systems | MIT, Stanford, Berkeley, UCSD, Microsoft, Google, IBM and systems/PL groups join generation with analysis and optimization | CAS ICT, SJTU, Fudan, HUST, Huawei and other systems groups provide strong OS/compiler/hardware-software work | Require equivalence, workload/hardware provenance, energy/cost, portability and operator review; study whether speedups survive real workloads and handoff. |
| Software for LLM and agent systems | Strong work on languages, orchestration, observability, evaluation, permissions and production AI engineering | Growing SE4AI programs, agent platforms and enterprise private deployment; standards and compliance are prominent | Compare debugging, trace inspection, release gates, provenance, model/tool/data drift, incident response and responsibility allocation. |
| Secure coding with AI | Strong direct user-study base from Stanford, NYU, UCF, plus broad GitHub/Copilot and AI IDE deployment | Strong model/platform base through Qwen/Lingma, Trae, DeepSeek-Coder, Code LLM labs; fewer visible controlled human studies | Replicate secure-coding user studies in Chinese developer settings and compare language, IDE, task, and training effects. |
| SOC analyst collaboration | Direct fieldwork from Data61/eSentire and USF/KU/USC ISI/Resideo lines; major U.S. SOC vendors productizing copilots | Large security-vendor and MSSP ecosystem, but fewer public in-the-wild SOC LLM studies | Study Chinese SOC adoption with ethnographic and query-log methods, especially under regulatory and data-localization constraints. |
| Reverse engineering | ASU/EURECOM/Padua NDSS 2026 gives direct human-LLM evidence | Strong binary/software-security labs and CTF teams; direct human-LLM reverse-engineering evidence appears thinner | Run controlled bilingual reverse-engineering experiments with Chinese analysts, decompilers, and local tooling. |
| Agent oversight | UCLA, NIST CAISI, UW, CMU SEI, OWASP/CSA focus on runtime approval, permissions, identity, auditability | CAC/TC260/CAICT governance plus Tencent Zhuque/OpenClaw and platform security activity | Compare user approval UX and institutional approval requirements: individual runtime approval versus provider/security-assessment regimes. |
| Red teaming | Strong HCI/social-science evidence on red-team labor, data practices, and motivations | Strong contest and platform activity around jailbreak, prompt injection, and model safety | Connect Chinese contest artifacts to socio-technical red-team labor studies; measure how scoring rules shape attack creativity and report quality. |
| Bug-bounty and maintainer handoff | HackerOne, Bugcrowd, OpenSSF, AIxCC, OSS-CRS make report quality and maintainer acceptance central | More contest/range and vendor-centered signals; public bug-bounty telemetry is less visible | Compare whether AI increases invalid-report burden differently in platform bounty versus contest/range ecosystems. |
| Governance | NIST CAISI, CISA, DARPA, MITRE, OpenSSF, OWASP/CSA practitioner guidance | CAC, TC260, CAICT, Chinese AI Safety Network, model-service security assessments | Treat governance as part of the human factor: it determines who must approve, audit, file, disclose, and take responsibility. |

## Secondary Country Profiles

These profiles are ordered by **relevance to this dossier**, not by a general national ranking. The working priority combines four signals: direct human/organizational evidence, depth across PL/OS/systems/SE/security/AI, identifiable LLM-for-software or software-for-LLM programs, and access to consequential industry or government deployment. Close ranks are judgment calls and should be updated as field evidence changes.

| Country or ecosystem | Why it ranks here |
| --- | --- |
| Germany | unusually dense security, PL, software-analysis, human-centered security, and explicit human-AI cybersecurity infrastructure |
| Singapore | concentrated NUS/NTU/SMU/SUTD programs spanning AI-for-code, formal methods, intelligent SE, agent security, digital trust, and national deployment |
| Canada | direct SOC evidence plus Waterloo-centered software reliability, maintenance, AIOps, formal methods, and agent security |
| United Kingdom | national AI-security evaluation plus major PL/systems/security/RSE institutions and operational cyber organizations |
| Switzerland | ETH, EPFL, UZH, IBM Research Zurich, and armasuisse provide exceptional depth in trustworthy AI, PL, systems, optimization, verification, and security |
| Netherlands | TU Delft provides one of the clearest integrated AI4SE, empirical SE, testing, DevOps, and secure-code-model programs outside the U.S. |
| Australia | direct SOC studies, Data61 operational research, and Monash's human-centered AI software-engineering program |
| France | direct SOC and reverse-engineering human studies plus INRIA/CEA/EURECOM/SystemX and a large critical-systems industrial base |
| Israel | globally significant software-security industry and strong academic security/systems research, with human-factor evidence still needing fuller mapping |
| Japan | deep systems, software quality, formal methods, AI, and industrial R&D; direct public human-LLM evidence is comparatively fragmented |
| South Korea | strong industrial AI/software ecosystem and emerging direct human-centered agent/security work |
| Taiwan research ecosystem | strategically important systems, hardware/software co-design, AI, and security research; direct human-factor evidence remains thin |
| Sweden | strong software systems, telecom, dependable systems, Cybercampus, and emerging LLM/software-security work |
| Denmark | unusually direct qualitative LLM-red-team evidence, plus strong PL, HCI, and software-engineering communities |
| Italy | direct reverse-engineering human study plus strong software security, formal methods, HCI, and cyber-range activity |
| Spain | human-centered AI security and expert-grounded security-requirements work, with a substantial national cyber ecosystem |
| Finland | strong Aalto/Helsinki software, usable security, systems, HCI, and AI research with major security-industry transfer |
| Belgium | direct 2025-2029 programs on safe AI coding assistants and engineering secure LLM applications |
| India | very large software-services and technical-education base with strong security/AI institutions, but less visible causal human-factor evidence |
| Austria | strong formal methods, PL, software engineering, systems, and security, including TU Wien and ISTA |
| Ireland | Lero provides a national software-research network with explicit LLM requirements-engineering work |
| Norway | NTNU explicitly covers AI for SE and SE for AI; operational and human-factor evidence remains emerging |
| Brazil | the largest Latin-American CS ecosystem, with strong critical systems, formal methods, SE, AI, and emerging agent research |
| Poland | substantial PL, verification, software engineering, security, and industrial R&D; direct mapped human evidence is limited |
| Czech Republic | strong usable security, cryptography, systems, and formal methods centered around Masaryk, CTU, and national cyber institutions |
| Portugal | INESC-ID, University of Lisbon, University of Porto, and Minho provide relevant SE, PL, dependable-systems, AI, and security work |
| Russia | large software/AI/security research and product ecosystem, with current public evidence and cross-border comparability requiring careful qualification |
| Turkey | strong systems-security, requirements, software-engineering, and defense/industrial deployment base |
| South Africa | the leading Sub-Saharan African operational cyber-research ecosystem and an essential multilingual/Global-South comparison |
| Mexico | large developer and higher-education population with relevant UNAM/CINVESTAV/Tec research and nearshore software-engineering industry |
| United Arab Emirates and Gulf | fast-growing sovereign AI, cyber-range, and critical-infrastructure deployment with a thinner public human-study record |
| New Zealand | smaller ecosystem but important for Five Eyes guidance, usable security, research software, and operational adoption comparisons |

### Germany

Additional institutions to track: Max Planck Institute for Security and Privacy, Saarland University, KIT/KASTEL, Fraunhofer AISEC and SIT, TU Munich, LMU Munich, h_da User-Centered Security, TU Braunschweig, and DFKI. Industry includes SAP, Siemens, Bosch, Deutsche Telekom/T-Systems, Aleph Alpha, Rohde & Schwarz, secunet, and the German automotive/industrial/OT ecosystem.

#### TU Darmstadt / ATHENE

##### Human-AI Collaboration For Cybersecurity (HAICC)

- `Homepage`: https://www.informatik.tu-darmstadt.de/haicc/about_haicc/index.en.jsp
- `Label`: `Core`
- `People`: Iryna Gurevych (project lead), Christian Reuter / PEASEC, Mira Mezini, Kristian Kersting, Michael Waidner, and the HAICC work-package PIs.
- `Focused area`: co-constructive cybersecurity agents, expert preference modeling, structured memory, multimodal security data and code, explainability, advisability, agent integrity, security configuration, and realistic expert workflows.
- `Human-factor relevance`: HAICC directly asks how AI agents can complement security experts without displacing expert judgment or compromising agent integrity. Its work packages explicitly cover interaction protocols, trust in explanations, expert feedback, objective manipulation, and cross-application operational work.
- `Activities / evidence`: ATHENE-funded program launched in 2026; planned benchmark and reusable framework; scenarios include vulnerability and protocol analysis, access-control and firewall configuration, SIEM work, and human-AI co-construction.
- `Sources`: https://www.informatik.tu-darmstadt.de/haicc/about_haicc/index.en.jsp ; https://www.informatik.tu-darmstadt.de/haicc/research_haicc/index.en.jsp ; https://www.tu-darmstadt.de/universitaet/aktuelles_meldungen/einzelansicht_561280.en.jsp.

#### CISPA Helmholtz Center For Information Security

##### Software, LLM, And Agent Security Groups

- `Homepage`: https://cispa.de/en/research/research-groups
- `Label`: `Core/strong adjacent`
- `People`: Andreas Zeller, Michael Pradel, Thorsten Holz, Mario Fritz, Lea Schönherr, Ben Stock, Christian Rossow, Fanny Lalande, Bernd Finkbeiner, and associated group leaders.
- `Focused area`: software testing, program analysis, vulnerability discovery and repair, fuzzing, web and systems security, formal methods, ML/LLM security, agent security, and evaluation rigor.
- `Human-factor relevance`: CISPA connects AI-based reasoning about software with concrete developer/security workflows and is also a leading source of methodological criticism about unreliable LLM evaluation. Track analyst review, false-positive burden, reproducibility, and how AI-native security tools integrate with real development.
- `Activities / evidence`: C-Mind-Security for contextual vulnerability analysis and remediation; SiSWiss for secure language models; LLM-security projects; work on pitfalls in LLM security and software-engineering research; software-analysis groups with direct AI-agent agendas.
- `Sources`: https://cispa.de/en/research/research-groups ; https://cispa.de/en/ndss-2026 ; https://career.cispa.de/jobs/group-pradel-2025-75.

#### TU Berlin

##### Machine Learning And Security (MLSEC)

- `Homepage`: https://www.tu.berlin/mlsec
- `Label`: `Core/strong adjacent`
- `People`: Konrad Rieck and MLSEC collaborators.
- `Focused area`: intelligent attack detection, vulnerability discovery, malware analysis, learning-system security and privacy, and rigorous evaluation of ML/LLM use in security.
- `Human-factor relevance`: MLSEC supplies the technical and methodological layer needed to study when analysts can trust learned detectors, explanations, and LLM-supported vulnerability workflows rather than merely consume model scores.
- `Activities / evidence`: research at the AI × security boundary; collaborations across BIFOLD, CASA, CISPA, and German security institutions.
- `Sources`: https://www.tu.berlin/mlsec ; https://mlsec.org/.

#### Ruhr University Bochum

##### CASA / RC Trust / AI And Society

- `Homepage`: https://casa.rub.de/en/research
- `Label`: `Core/strong adjacent`
- `People`: Thorsten Holz, Bilal Zafar, Christof Paar, Angela Sasse and collaborators across CASA's research hubs.
- `Focused area`: security from hardware and trustworthy systems through human-centered security, societal trust, and trustworthy AI.
- `Human-factor relevance`: CASA's current structure explicitly spans software platforms, users, and society, making it an unusually complete environment for studying how AI security tools affect users, operators, organizations, and public trust.
- `Activities / evidence`: six research hubs including Trustworthy Systems, Human-Centered Security and Privacy, and Security & Societal Trust in Emerging Technologies; AISOC research on LLM understanding and trustworthy AI.
- `Sources`: https://casa.rub.de/en/research ; https://informatik.rub.de/aisoc/ ; https://casa.rub.de/en/research/publications/detail/dos-and-donts-of-machine-learning-in-computer-security.

### Singapore

Additional institutions and sectors: AI Singapore, CSIT, DSO National Laboratories, GovTech, CSA Singapore, Singtel/NCS, ST Engineering, Mastercard-NTU, Ant International-NTU, and financial-sector SOCs.

#### Singapore Management University

##### Centre For Research On Intelligent Software Engineering (RISE)

- `Homepage`: https://rise.smu.edu.sg/
- `Label`: `Core`
- `People`: David Lo, Lingxiao Jiang, Sun Jun, Xiaofei Xie, Christoph Treude and affiliated faculty.
- `Focused area`: AI × software engineering × cybersecurity; reliable, secure, efficient, maintainable, and intelligent software systems; program analysis, testing, empirical SE, code models, and human-AI collaboration.
- `Human-factor relevance`: RISE is directly aligned with this dossier's expanded scope and explicitly targets practitioner productivity, software reliability and security, and industrial application rather than isolated model accuracy.
- `Activities / evidence`: nationally and industrially funded centre; LLM4Code robustness/security/privacy; AI4SE; software analytics; work on programmer adoption of AI-generated code and taxonomies of human-AI collaboration in SE.
- `Sources`: https://rise.smu.edu.sg/ ; https://computing.smu.edu.sg/research ; https://news.smu.edu.sg/news/2023/07/24/rising-build-better-faster-and-cheaper-software ; https://ink.library.smu.edu.sg/etd_coll/666/.

#### National University Of Singapore

##### Trustworthy And Secure Software / AI For Code / PLSE

- `Homepage`: https://www.comp.nus.edu.sg/cs/research/plse/
- `Label`: `Core`
- `People`: Abhik Roychoudhury, Ilya Sergey, Joxan Jaffar, Hugh Anderson, Wei-Ngan Chin, Shengchao Qin and collaborators in programming languages, software engineering, and trustworthy software.
- `Focused area`: program analysis, testing, verification, concurrency, language-based security, compilers, code agents, automated repair, and trustworthy AI software engineering.
- `Human-factor relevance`: NUS combines analysis-backed code agents with correctness and security machinery that can give developers inspectable evidence. It is a key site for studying how humans review repository-scale repairs, tests, and formal/static evidence.
- `Activities / evidence`: AutoCodeRover and repository-level issue resolution; Singapore Manifesto on AI-driven innovations for code; PLSE and FOCS programs; practitioner and industry engagement.
- `Sources`: https://www.comp.nus.edu.sg/cs/research/plse/ ; https://www.comp.nus.edu.sg/features/ai-in-sw-development-autocoderover/ ; https://ai.nus.edu.sg/singapore-manifesto-on-ai-driven-innovations-for-code/ ; https://focs-lab.comp.nus.edu.sg/.

#### Nanyang Technological University

##### Digital Trust Centre / Cyber Security Lab

- `Homepage`: https://www.ntu.edu.sg/dtc
- `Label`: `Core/strong adjacent`
- `People`: Kwok Yan Lam, Luke Ong, Anwitaman Datta, Jun Luo, Dusit Niyato, Tianwei Zhang, and researchers listed by DTC and the Cyber Security Lab.
- `Focused area`: AI safety, digital trust, privacy-enhancing technologies, AI/LLM security, agent red teaming, OS and cloud security, cyber risk governance, and translation to government and industry.
- `Human-factor relevance`: DTC houses the Singapore AI Safety Institute and explicitly mixes technical research, sandboxes, governance, industry problem statements, and user-centered design. This creates a strong setting for studying operational adoption and responsibility.
- `Activities / evidence`: national centre funded by IMDA/NRF; AI-safety and trust-technology programs; publications on agent workflows and security; NTU/Singtel SCALE and Imperial-NTU IN-CYPHER collaborations.
- `Sources`: https://www.ntu.edu.sg/dtc/about-us ; https://www.ntu.edu.sg/dtc/our-people ; https://www.ntu.edu.sg/dtc/publications ; https://www.ntu.edu.sg/computing/research/institutes-centres/csl ; https://www.imperial.ac.uk/about/global/singapore/research/in-cypher/.

##### Agent-Mediated Deception Collaboration

- `Homepage`: https://arxiv.org/abs/2602.21127
- `Label`: `Core`
- `People`: NTU, KTH, and William & Mary HAT-Lab collaborators.
- `Focused area`: how users perceive and respond to deception mediated through trusted LLM agents, including professional software-development scenarios.
- `Human-factor relevance`: this is direct human-subject evidence about compromised agents, trust transfer, user susceptibility, and the limits of oversight.
- `Activities / evidence`: cross-national user study and attack scenarios involving agent-mediated behavior.
- `Sources`: https://arxiv.org/abs/2602.21127 ; https://www.ntu.edu.sg/dtc.

#### Singapore University Of Technology And Design

##### iTrust Centre For Research In Cyber Security

- `Homepage`: https://www.sutd.edu.sg/itrust/
- `Label`: `Strong adjacent`
- `People`: Aditya Mathur and iTrust faculty and researchers.
- `Focused area`: cyber-physical and critical-infrastructure security, testbeds, threat modeling, digital forensics, and operational cyber exercises.
- `Human-factor relevance`: iTrust provides realistic infrastructure and operator contexts for testing LLM agents, incident assistance, and human override under physical consequences.
- `Activities / evidence`: sector-scale testbeds and national/industry cyber collaborations.
- `Sources`: https://www.sutd.edu.sg/itrust/.

### Canada

Additional institutions: University of Toronto PL/systems/SE and Schwartz Reisman Institute, Vector Institute, Queen's L1NNA Lab, Concordia SPNET, UBC, McGill, Carleton, and Royal Military College. Industry/government includes BlackBerry Cylance, OpenText Cybersecurity, Arctic Wolf, Cohere, the National Cybersecurity Consortium, and the Canadian Centre for Cyber Security.

#### eSentire / University Of Waterloo Partner Line

##### Live MDR/SOC LLM-Use Research

- `Homepage`: https://www.esentire.com/
- `Label`: `Core`
- `People`: Martin Lochner, Keegan Keplinger and academic/industry collaborators.
- `Focused area`: live SOC LLM queries, topic modeling, expert validation, managed detection and response, and analyst practice.
- `Human-factor relevance`: the work observes what analysts actually ask LLMs inside an operational environment, rather than inferring use from benchmarks. It supports studies of task mix, expertise, validation, and organizational controls.
- `Activities / evidence`: analysis of real analyst interaction data with human expert interpretation.
- `Sources`: https://arxiv.org/abs/2508.18488 ; https://www.esentire.com/.

#### University Of Waterloo

##### SENSE Lab

- `Homepage`: https://sense.eng.uwaterloo.ca/
- `Label`: `Core/strong adjacent`
- `People`: Weiyi Shang and SENSE Lab collaborators.
- `Focused area`: software logs, performance assurance, AIOps, release engineering, maintainability, observability, and AI-assisted software development.
- `Human-factor relevance`: SENSE connects LLM assistance to reliability and operational evidence. Relevant measures include diagnostic effort, alert comprehension, performance-regression review, and whether operators retain causal understanding.
- `Activities / evidence`: empirical studies and tools for large-scale software systems, logs, performance, and operations.
- `Sources`: https://sense.eng.uwaterloo.ca/.

##### Software Engineering, SWAG, WatForm, WISE, And Software REBELs

- `Homepage`: https://uwaterloo.ca/computer-science/research/research-areas/software-engineering
- `Label`: `Core/strong adjacent`
- `People`: Joanne Atlee, Michael Godfrey, Shane McIntosh, Mei Nagappan, Krzysztof Czarnecki, Patrick Lam, Weiyi Shang and collaborators.
- `Focused area`: requirements, architecture, evolution, mining repositories, release engineering, formal methods, safety, intelligent systems, testing, and maintenance.
- `Human-factor relevance`: Waterloo has breadth across the lifecycle needed to evaluate whether coding agents improve long-term software outcomes or merely accelerate local edits.
- `Activities / evidence`: multiple dedicated labs and industry-facing SE programs; direct work on LLM-agent security against malicious or vulnerable tools.
- `Sources`: https://se.uwaterloo.ca/ ; https://uwaterloo.ca/waterloo-intelligent-systems-engineering-lab/ ; https://rebels.cs.uwaterloo.ca/ ; https://uwaterloo.ca/computer-science/news/meng-xu-sihang-liu-254k-funding-national-cybersecurity-consortium-strengthen-security-llm-agents.

### United Kingdom

Additional institutions: Cambridge PL/Security/Systems groups, Oxford PL and cyber security, UCL CREST and usable security, Imperial AI Security and Privacy Lab and software systems, King's Cybersecurity Group, Edinburgh PL/AI, Bristol, Newcastle, Southampton, Sheffield, Royal Holloway, and the Software Sustainability Institute. Operational actors include NCSC, GCHQ, Darktrace, NCC Group, PortSwigger, BT Security, and BAE Systems Digital Intelligence.

#### UK AI Security Institute

##### Frontier-Model Security Evaluation

- `Homepage`: https://www.aisi.gov.uk/about
- `Label`: `Core/strong adjacent`
- `People`: institutional evaluation, safeguards, and research teams; use official staff/project pages for individual attribution.
- `Focused area`: frontier-model cyber capabilities, safeguards, human-influence risk, pre-release evaluation, and government-facing safety science.
- `Human-factor relevance`: AISI shapes which model and agent behaviors are tested before deployment and how evidence reaches policy and operational decision makers. It is relevant to evaluator judgment, reproducibility, disclosure, and governance.
- `Activities / evidence`: model evaluations, research collaborations, evaluation tooling, and public technical reports.
- `Sources`: https://www.aisi.gov.uk/about.

#### Laboratory For AI Security Research

##### LASR Public-Private Research Program

- `Homepage`: https://lasr.ac.uk/
- `Label`: `Core/strong adjacent`
- `People`: participating UK academic, government, and industry researchers; attribute project leadership from the relevant LASR project page.
- `Focused area`: AI security, resilient systems, evaluation, national-security applications, and translation across academia, industry, and government.
- `Human-factor relevance`: LASR is a natural site for studying how assurance evidence is shared across institutions and how responsibility is allocated when agentic systems enter high-consequence workflows.
- `Activities / evidence`: coordinated research calls, test and evaluation programs, and public-private partnership.
- `Sources`: https://lasr.ac.uk/.

#### University Of Cambridge

##### Research Software Engineering Community And Research Computing Services

- `Homepage`: https://rse.group.cam.ac.uk/
- `Label`: `Core/strong adjacent`
- `People`: Christopher Edsall, the Research Computing Services RSE team, departmental RSEs, and Institute of Computing for Climate Science contributors.
- `Focused area`: scientific-software design, refactoring, legacy modernization, HPC/GPU migration, performance optimization, training, and collaboration with domain researchers.
- `Human-factor relevance`: Cambridge provides a high-value population often omitted from coding-assistant studies: scientists and RSEs maintaining performance-sensitive, reproducible software whose requirements are distributed across code and domain knowledge.
- `Activities / evidence`: RSE consulting and delivery; optimization and modernization projects; community seminars; research/industry collaborations.
- `Sources`: https://rse.group.cam.ac.uk/ ; https://rse.group.cam.ac.uk/people ; https://www.csd3.cam.ac.uk/research-software-engineering ; https://www.hpc.cam.ac.uk/team.

### Switzerland

Additional actors: armasuisse Cyber-Defence Campus, the Swiss National Cyber Security Centre, Idiap, CERN's research-software ecosystem, Sonar, Proton, Scandit, and Swiss financial/pharmaceutical engineering and security teams.

#### ETH Zurich

##### Secure, Reliable, And Intelligent Systems (SRI) Lab

- `Homepage`: https://www.sri.inf.ethz.ch/
- `Label`: `Core`
- `People`: Martin Vechev and SRI researchers.
- `Focused area`: reliable, secure, and trustworthy ML/LLMs; coding and mathematical reasoning; controllability, security, privacy, evaluation, program analysis, synthesis, and rigorous software engineering.
- `Human-factor relevance`: SRI directly joins AI for code, security for agents, and formal/software assurance. Its spin-off record also exposes a path from research prototypes to developer tools and operational agent security.
- `Activities / evidence`: BigCode/statistical programming engines, DeepCode, LogicStar, Invariant Labs, secure AI agents, and courses/research on reliable AI and software engineering.
- `Sources`: https://www.sri.inf.ethz.ch/ ; https://www.sri.inf.ethz.ch/research/plml ; https://www.sri.inf.ethz.ch/teaching/.

##### Programming Languages And Software Engineering Area

- `Homepage`: https://inf.ethz.ch/research/programming-languages-software-engineering.html
- `Label`: `Strong adjacent`
- `People`: David Basin, Torsten Hoefler, Ralf Jung, Michalis Kokologiannakis, Peter Müller, Markus Püschel, Shweta Shinde, Zhendong Su, Martin Vechev, April Yi Wang and associated faculty.
- `Focused area`: verification, testing, program generation, compilers, optimization, concurrency, systems security, trustworthy AI, HCI for programming, and computing education.
- `Human-factor relevance`: the area covers nearly every assurance mechanism needed to ground LLM-produced software, as well as the human interfaces and education questions around programming with AI.
- `Activities / evidence`: SRI, Advanced Software Technologies, Programming Language Foundations, verification, high-performance computing, security, and educational-technology groups.
- `Sources`: https://inf.ethz.ch/research/programming-languages-software-engineering.html ; https://plf.inf.ethz.ch/ ; https://ast.ethz.ch/.

#### EPFL

##### Dependable Systems, HexHive, And SYSTEMF

- `Homepage`: https://www.epfl.ch/schools/ic/research/
- `Label`: `Core/strong adjacent`
- `People`: George Candea, Mathias Payer, Clément Pit-Claudel and collaborators.
- `Focused area`: dependable and efficient systems, automated testing, software and systems security, fuzzing, formal verification, compilers, interactive theorem proving, and full-assurance system components.
- `Human-factor relevance`: these labs provide complementary evidence channels for coding agents: security testing, performance contracts, machine-checked correctness, and interactive proof/programming interfaces.
- `Activities / evidence`: verified systems components, automated testing and symbolic execution, HexHive software-security tooling, and SYSTEMF's verified critical-systems work.
- `Sources`: https://dslab.epfl.ch/ ; https://hexhive.epfl.ch/ ; https://systemf.epfl.ch/ ; https://www.epfl.ch/schools/ic/education/master/cyber-security/projects-labs-cs/.

#### University Of Zurich

##### Software Evolution And Architecture Lab (SEAL)

- `Homepage`: https://www.ifi.uzh.ch/en/seal.html
- `Label`: `Core/strong adjacent`
- `People`: Thomas Fritz, Harald Gall and SEAL collaborators.
- `Focused area`: software evolution, architecture, repository mining, developer productivity, multi-team development, software quality, and AI-assisted software engineering.
- `Human-factor relevance`: SEAL is especially relevant to long-term maintenance, developer cognition, coordination, and whether AI-generated changes preserve architectural and organizational knowledge.
- `Activities / evidence`: empirical software engineering, developer studies, software analytics, and industry collaboration.
- `Sources`: https://www.ifi.uzh.ch/en/seal.html.

#### IBM Research Europe - Zurich

##### AI, Security, And Systems Research

- `Homepage`: https://research.ibm.com/labs/zurich
- `Label`: `Strong adjacent`
- `People`: Teodoro Laino, Elli Androulaki and Zurich research teams; AI-for-Code work is organized across IBM Research locations.
- `Focused area`: AI and novel algorithms for engineering simulation, optimization, system/software security analysis, robust AI, and next-generation computing.
- `Human-factor relevance`: IBM Zurich adds enterprise deployment, scientific/engineering optimization, and security-assurance contexts to the Swiss academic map.
- `Activities / evidence`: AI for engineering simulations, security research, EU projects, and IBM-wide AI-for-Code modernization.
- `Sources`: https://research.ibm.com/labs/zurich ; https://research.ibm.com/topics/ai-for-code.

### Netherlands

Additional institutions: Vrije Universiteit Amsterdam (systems/security/software analytics), University of Twente, Radboud University, Eindhoven University of Technology, Leiden University, Centrum Wiskunde & Informatica, and TNO. Industry includes JetBrains Amsterdam, ING, ASML, Philips, Booking.com, Adyen, and Dutch critical-infrastructure operators.

#### Delft University Of Technology

##### Software Engineering Research Group / AI4SE / FUSE

- `Homepage`: https://serg.ewi.tudelft.nl/
- `Label`: `Core`
- `People`: Arie van Deursen, Andy Zaidman, Annibale Panichella, Luis Cruz, Sebastian Proksch, Maliheh Izadi, Georgios Gousios and collaborators.
- `Focused area`: empirical and human-centered SE, AI4SE, SE4AI, software testing, DevOps, evolution, architecture, software analytics, green AI/software, and secure LLMs for code.
- `Human-factor relevance`: TU Delft explicitly studies how people build and evolve software and couples that mission to AI-enabled development and secure-code-model research. It is a primary comparative site for developer productivity, review, testing, maintenance, and organizational adoption.
- `Activities / evidence`: SERG research lines, AI4SE, AISE, CISELab, FUSE secure-LLM track, and partnerships with software-tool companies and industrial developers.
- `Sources`: https://serg.ewi.tudelft.nl/about/ ; https://serg.ewi.tudelft.nl/members/ ; https://se.ewi.tudelft.nl/ai4se/ ; https://se.ewi.tudelft.nl/fuse-lab/tracks/05_secure_llms4code/.

### Australia

Additional institutions: UNSW/UNSW Canberra Cyber, University of Melbourne, University of Adelaide/AIML, RMIT, Australian National University, University of Queensland, Macquarie, and the Cyber Security CRC. Industry/government includes ASD/ACSC, Home Affairs, Atlassian, Canva, CyberCX, Telstra, banks, and critical-infrastructure SOCs. Source: https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services.

#### CSIRO Data61

##### Software And Computational Systems / Cybersecurity

- `Homepage`: https://www.csiro.au/en/about/people/research-units/Data61
- `Label`: `Core`
- `People`: Shahroz Tariq, Ronal Singh, Fatemeh Jalalvand, Mohan Baruwal Chhetri, Surya Nepal, Cecile Paris, Sharif Abuadbba, Jon Whittle, and collaborators.
- `Focused area`: human-AI SOC collaboration, alert fatigue, distributed and secure systems, AI-generated-code security, threat modeling, software engineering for AI, and responsible AI.
- `Human-factor relevance`: Data61 combines direct analyst studies with technical software/security research and public-sector deployment. It is one of the strongest non-U.S. sources for operational human-LLM evidence.
- `Activities / evidence`: in-the-wild SOC study; expertise-gap and alert-fatigue work; AI assurance; collaborative intelligence for AI-generated-code security; ThreatModelling-GPT and distributed-systems security projects.
- `Sources`: https://arxiv.org/abs/2508.18947 ; https://arxiv.org/abs/2505.03179 ; https://research.csiro.au/ss/ ; https://people.csiro.au/A/S/sharif-abuadbba ; https://www.csiro.au/en/about/people/research-units/Data61.

#### Monash University

##### HumanAISE And Software Engineering

- `Homepage`: https://www.monash.edu/it/humanaise-lab/home
- `Label`: `Core`
- `People`: Rashina Hoda, Chetan Arora, John Grundy, Aldeida Aleti, Chakkrit Tantithamthavorn, Markus Wagner and collaborators.
- `Focused area`: human-centric AI software engineering, AI × SE, requirements, software quality, testing, agile work, human values, trustworthy AI software, and socio-technical methods.
- `Human-factor relevance`: HumanAISE places engineers, users, organizations, and social values at the center of AI software engineering. It supports qualitative and mixed-method work on how GenAI changes roles, skills, projects, and software outcomes.
- `Activities / evidence`: renewed HumanAISE program; prior HumaniSE living-lab work; projects on GenAI effects in agile software work; roadmap on software engineering by and for humans in an AI era.
- `Sources`: https://www.monash.edu/it/humanaise-lab/home ; https://www.monash.edu/it/humanaise-lab/people ; https://www.monash.edu/it/ssc/software-engineering ; https://research.monash.edu/en/publications/software-engineering-by-and-for-humans-in-an-ai-era/.

### France

Additional institutions: INRIA, CEA LIST, CNRS, ANSSI, Institut Polytechnique de Paris, Télécom Paris, Sorbonne Université, Université Grenoble Alpes, and Paris-Saclay. Industry includes Mistral AI, Thales, Dassault Systèmes, Orange Cyberdefense, Capgemini, Eviden, Quarkslab, Stormshield, Airbus, and RTE.

#### IRT SystemX / Airbus Protect / RTE

##### Human-AI SOC Collaboration

- `Homepage`: https://www.irt-systemx.fr/en/
- `Label`: `Core`
- `People`: Reda Yaich, Alexandre Balondrade, Antoine Sicard, Christelle Fouquiau, Guillaume Giraud, Kahina Amokrane-Ferka, Emmanuel Arbaretier and collaborators.
- `Focused area`: SOC analyst collaboration, cognitive profiling, agentic coordination, critical-infrastructure cybersecurity, and the VOWEL+U oversight framework.
- `Human-factor relevance`: this line treats the SOC as a distributed human-agent organization and makes operator cognition, coordination, authority, and explainability part of system design.
- `Activities / evidence`: applied research with Airbus Protect and the French electricity-transmission operator; published framework and operational scenarios.
- `Sources`: https://www.irt-systemx.fr/en/ ; https://ojs.aaai.org/index.php/AAAI-SS/article/download/36072/38227/40160 ; https://cyber.airbus.com/en/offers/artificial-intelligence-in-cybersecurity.

#### EURECOM

##### Software And System Security / Human-LLM Reverse Engineering

- `Homepage`: https://www.eurecom.fr/en/research
- `Label`: `Core`
- `People`: Simone Aonzo and collaborators with Arizona State University and the University of Padua.
- `Focused area`: reverse engineering, malware and mobile security, binary analysis, and empirical human-LLM teaming.
- `Human-factor relevance`: the NDSS 2026 study directly compares novice and expert reverse engineers working with LLM support, exposing gains, hallucination risks, and expertise effects.
- `Activities / evidence`: practitioner survey and controlled study with 48 participants across novice/expert groups.
- `Sources`: https://www.eurecom.fr/en/research ; https://www.eurecom.fr/en/research/networking-and-security-department/directory ; https://www.eurecom.fr/en/publication/8548 ; https://s3.eurecom.fr/docs/ndss26_basque.pdf.

### Israel

- `Priority basis`: globally influential software-security and cloud-security industry; strong systems, PL, cryptography, web security, and human-centered security academia; extensive multinational R&D. Direct public studies of humans using LLM software/security agents remain less consolidated than the underlying ecosystem.
- `Major institutions`: Tel Aviv University, Technion, Hebrew University, Ben-Gurion University of the Negev, Weizmann Institute, Reichman University, and Bar-Ilan University.
- `Research directions`: AI and agent security, web/application security, usable security, vulnerability research, formal methods, cloud and identity security, cyber operations, and software supply chain.
- `Companies/sectors`: Check Point, CyberArk, Wiz, Cato Networks, Checkmarx, Snyk's Israeli ecosystem, Orca Security, SentinelOne Israel R&D, Aqua Security, Armis, Torq, Microsoft/Google/IBM security labs, and the national cyber ecosystem.
- `Evidence gap`: map current labs and PIs to direct developer, SOC, incident-response, or agent-oversight studies before promoting them to `Core`.

### Japan

- `Priority basis`: deep software-quality, systems, compilers, formal-methods, robotics, AI, and industrial R&D capacity; a large population of professional developers and high-reliability engineering domains; fragmented public human-LLM evidence.
- `Major institutions`: NICT Cybersecurity Research Institute and CREATE, AIST Intelligent Platform Research Institute, National Institute of Informatics, University of Tokyo, Kyoto University, Osaka University, Waseda, Keio, Tokyo Institute of Science, JAIST, Nara Institute of Science and Technology, and RIKEN.
- `Research directions`: AI security, code intelligence, testing and repair, formal verification, dependable/embedded systems, HCI, LLM evaluation, cyber training, and research-software productivity.
- `Companies/sectors`: NTT, NEC, Fujitsu, Hitachi, KDDI, Rakuten, Trend Micro, Preferred Networks, Toyota and automotive suppliers, robotics/OT vendors, JPCERT/CC and NISC.
- `Sources`: https://www.nict.go.jp/en/research/index.html ; https://create.nict.go.jp/en/ ; https://unit.aist.go.jp/ipri/en/.

### South Korea

Additional institutions: KAIST, Korea University AIR Lab and cyber defense, Seoul National University, Sogang HAICoLab, Sungkyunkwan University, POSTECH, Yonsei, and ETRI. Industry includes Samsung Research, LG AI Research, Naver, Kakao, SK Telecom, AhnLab, and KISA. Sources: https://air.korea.ac.kr/ ; https://haicolab.sogang.ac.kr/.

#### Ewha Womans University / Kumoh National Institute Of Technology / Coretrustlink

##### Human-Centered LLM Agent For Anomaly Detection

- `Homepage`: https://arxiv.org/abs/2510.20102
- `Label`: `Core/strong adjacent`
- `People`: Gyuyeon Na, Minjung Park, Hyeonjeong Cha, Sangmi Chai and collaborators.
- `Focused area`: human-centered LLM-agent support for digital-asset anomaly detection and expert decision support.
- `Human-factor relevance`: direct attention to how an agent presents anomalies and supports human interpretation in a consequential financial/security domain.
- `Activities / evidence`: designed and evaluated agent workflow; follow-up should verify participant population, longitudinal use, and operational deployment.
- `Sources`: https://arxiv.org/abs/2510.20102.

### Taiwan (China)

- `Priority basis`: world-leading semiconductor and systems industry, strong hardware/software co-design, systems, PL, security, and AI research, and strategically important supply-chain assurance. This heading describes a research ecosystem and does not make a political-status claim.
- `Major institutions`: Academia Sinica Institute of Information Science, National Taiwan University, National Tsing Hua University, National Yang Ming Chiao Tung University, National Cheng Kung University, and National Taiwan University of Science and Technology.
- `Research directions`: secure and efficient AI systems, compilers, systems security, hardware/software verification, EDA, vulnerability analysis, trustworthy AI, and semiconductor/software supply chains.
- `Companies/sectors`: TSMC, MediaTek, ASUS, Acer, Synopsys/Silicon Valley R&D links, Trend Micro, TeamT5, DEVCORE, and Taiwan's semiconductor-security ecosystem.
- `Evidence gap`: identify current human-subject studies of coding agents, SOC copilots, and AI-assisted hardware/software design before assigning `Core`.

### Sweden

Additional institutions: Linköping RESIST, Chalmers, Lund, Stockholm University, Uppsala, Örebro MPI Lab, RISE Research Institutes of Sweden, Karlstad SIGS-CyberSec, and Blekinge Institute of Technology. Industry includes Ericsson, Saab, Sectra, Combitech, Truesec, and Recorded Future.

#### KTH Royal Institute Of Technology

##### Software And Computer Systems / Cybercampus / Agent-Security Collaboration

- `Homepage`: https://www.kth.se/scs/
- `Label`: `Core/strong adjacent`
- `People`: David Broman and KTH Software and Computer Systems researchers; KTH collaborators in the NTU/William & Mary agent-mediated-deception study.
- `Focused area`: software engineering, cloud and networked systems, security, applied AI, LLMs for code, network configuration, vulnerability detection, and national cybersecurity training.
- `Human-factor relevance`: KTH couples direct agent-deception evidence with systems and software research, creating a route from user susceptibility to secure configuration, resilient infrastructure, and developer tooling.
- `Activities / evidence`: LLM4Code work, LLM-powered vulnerability and configuration studies, Cybercampus graduate projects, and cross-national agent-security collaboration.
- `Sources`: https://www.kth.se/scs/ ; https://www.kth.se/en/2.101513/research/cybercampus-graduate ; https://arxiv.org/abs/2602.21127.

### Denmark

Additional institutions: University of Copenhagen, DTU, Aalborg, Aarhus, and the Alexandra Institute. Industry includes TDC NET, Trifork, Systematic, LEGO, Danish financial SOCs, and national AI-compute/safety initiatives.

#### IT University Of Copenhagen

##### LLM Red Teaming And Human-AI Interaction

- `Homepage`: https://en.itu.dk/
- `Label`: `Core`
- `People`: Nanna Inie, Leon Derczynski, Paolo Tell, Claus Brabrand and relevant ITU Software Engineering, NLP, HCI, and computing-education collaborators.
- `Focused area`: human practices of LLM red teaming, generative-AI interaction, software teamwork, software processes, computing education, and security probing.
- `Human-factor relevance`: the grounded-theory study directly investigates who red-teams LLMs, why they do it, and which strategies and social practices they use. This is stronger evidence than a jailbreak benchmark alone.
- `Activities / evidence`: interviews with dozens of practitioners; grounded theory of LLM red teaming; garak security-probing framework; related human-AI and education research.
- `Sources`: https://en.itu.dk/About-ITU/Press/News-from-ITU/2025/New-ITU-research-analyses-attacks-on-Large-Language-Models/ ; https://pure.itu.dk/en/publications/summon-a-demon-and-bind-it-a-grounded-theory-of-llm-red-teaming/ ; https://pure.itu.dk/en/persons/leon-derczynski/.

### Italy

Additional institutions: Politecnico di Milano, University of Trento, Sapienza University of Rome, University of Cagliari, IMT Lucca, University of Pisa/CNR-ISTI, and FBK. Industry includes Leonardo, Engineering Group, Reply, Yarix/Var Group, and the Italian National Cybersecurity Agency ecosystem.

#### University Of Padua

##### Human-LLM Software Reverse Engineering

- `Homepage`: https://www.math.unipd.it/~elosiouk/
- `Label`: `Core`
- `People`: Samuele Doria, Eleonora Losiouk and collaborators with Arizona State University and EURECOM.
- `Focused area`: software reverse engineering, mobile and application security, vulnerability repair, malware defense, and human-LLM teaming.
- `Human-factor relevance`: Padua contributes the direct human-study and user-security expertise in the NDSS 2026 reverse-engineering work and connects it to broader software-security research.
- `Activities / evidence`: controlled novice/expert reverse-engineering study; work on LLM vulnerability repair and user-centric malware defenses.
- `Sources`: https://www.research.unipd.it/handle/11577/3588620 ; https://www.math.unipd.it/~elosiouk/publications.html.

### Spain

Additional institutions: INCIBE, Universidad Carlos III de Madrid, University of Málaga, University of Granada, Barcelona Supercomputing Center, and Spanish AI/cybersecurity networks. Industry includes Telefónica Tech, Indra/Minsait, S2 Grupo, GMV, and banking security labs.

#### INGENIO / CSIC / Universitat Politècnica De València

##### Human-Centered AI Security And Privacy (HASP) Lab

- `Homepage`: https://hasp-lab.github.io/
- `Label`: `Core/strong adjacent`
- `People`: HASP Lab faculty and collaborators listed on the group site.
- `Focused area`: human-centered AI security, ethics, privacy, HCI, and malicious or manipulative LLM-based conversational systems.
- `Human-factor relevance`: HASP treats AI security as a user, organizational, and societal problem rather than only a model attack surface.
- `Activities / evidence`: interdisciplinary human-centered AI and security projects and publications.
- `Sources`: https://hasp-lab.github.io/.

#### Universidad Politécnica De Madrid

##### AI-Augmented Cybersecurity Requirements

- `Homepage`: https://portalcientifico.upm.es/en/ipublic/item/10450496
- `Label`: `Core/strong adjacent`
- `People`: authors and UPM research groups identified on the official project/publication record.
- `Focused area`: LLM/AI support for cybersecurity requirements generation and comparison with human expert ground truth.
- `Human-factor relevance`: requirements work exposes whether AI expands coverage, introduces irrelevant controls, or changes expert review effort before code is written.
- `Activities / evidence`: expert-grounded evaluation of generated security requirements.
- `Sources`: https://portalcientifico.upm.es/en/ipublic/item/10450496.

### Finland

- `Priority basis`: Aalto/Helsinki provide strong software engineering, usable security, computing systems, HCI, AI, education, and national cybersecurity research; Finland also has an unusually important security-product ecosystem.
- `Major institutions`: Aalto University Software and Service Engineering, Secure Systems Group, Helsinki-Aalto Institute for Cybersecurity, Finnish Center for AI, University of Helsinki, VTT, University of Oulu, and Tampere University.
- `Research directions`: secure and usable systems, software/service engineering, AI engineering, human-computer interaction, privacy, computing education, dependable automation, and AI for industrial systems.
- `Companies/sectors`: WithSecure/F-Secure, Nokia, SSH Communications Security, Relex, Silo AI/AMD, and Finnish telecom/industrial SOCs.
- `Sources`: https://research.aalto.fi/en/organisations/department-of-computer-science/ ; https://ssg.aalto.fi/.

### Belgium

Additional institutions: KU Leuven HCI and DTAI, VUB Software Languages Lab, imec, Ghent University, Université catholique de Louvain, and University of Antwerp. Industry/government includes Sirris, Agoria, Proximus, financial institutions, and the Centre for Cybersecurity Belgium.

#### KU Leuven / Vrije Universiteit Brussel

##### DistriNet, Software Languages Lab, CODEGUARD, And LISA

- `Homepage`: https://distrinet.cs.kuleuven.be/research/research
- `Label`: `Core`
- `People`: Bert Lagaisse, Wouter Joosen, Lieven Desmet, Stijn Volckaert, Tom Van Cutsem, Coen De Roover and collaborating researchers.
- `Focused area`: secure software engineering, secure languages and compilation, distributed systems, AI code-assistant security, LLM application engineering, DevOps, testing, performance, reliability, and industrial knowledge transfer.
- `Human-factor relevance`: CODEGUARD explicitly targets safe, efficient, responsible company adoption of AI code assistants, including workshops, demonstrators, guardrails, and recommendations. LISA translates SE/DevOps practice to secure LLM applications.
- `Activities / evidence`: 2026-2029 CODEGUARD project; 2025-2027 LISA project; company-facing training and integration; static/dynamic analysis guardrails; secure software and distributed-systems research.
- `Sources`: https://research.kuleuven.be/portal/en/project/3E260103 ; https://research.kuleuven.be/portal/en/project/3E250235 ; https://distrinet.cs.kuleuven.be/research/research ; https://iiw.kuleuven.be/nieuws-en-agenda/kalender/secure-software-engineering-in-a-genai-world.

### India

- `Priority basis`: enormous professional-developer and software-services population, strong technical institutions, national digital infrastructure, and rapidly growing GenAI deployment; the public record needs more controlled and longitudinal human-factor studies.
- `Major institutions`: IISc, IIT Madras, IIT Bombay, IIT Delhi, IIT Kanpur, IIT Kharagpur, IIIT Hyderabad, IIIT Bangalore, C-DAC, and DRDO/CAIR.
- `Research directions`: secure code generation, program analysis, formal methods, AI systems, multilingual developer tools, cyber ranges, software maintenance, and large-scale enterprise adoption.
- `Companies/sectors`: TCS, Infosys, Wipro, HCLTech, Tech Mahindra, Zoho, Freshworks, Razorpay and financial-security teams, CERT-In, and Indian SOC/MSSP vendors.
- `Evidence gap`: measure effects across outsourcing/product teams, multilingual requirements, review hierarchies, education and reskilling, and high-volume maintenance work.

### Austria

- `Priority basis`: strong formal methods, verification, PL, software engineering, systems, and security, with direct participation in critiques of LLM-security methodology.
- `Major institutions`: TU Wien Software Engineering, Security and Privacy, and formal-methods groups; Institute of Science and Technology Austria; University of Vienna; Graz University of Technology/IAIK; Johannes Kepler University Linz; and SBA Research.
- `Research directions`: program analysis, probabilistic programming, verification, compilers, systems security, cryptography, AI assurance, and empirical SE.
- `Companies/sectors`: Dynatrace, Frequentis, Siemens Austria, A1, and critical-infrastructure/security vendors.
- `Evidence gap`: connect strong technical assurance research to developer and operator studies of LLM-assisted workflows.

### Ireland

Additional institutions: University of Limerick, Trinity College Dublin, University College Dublin, University College Cork, Dublin City University, and Galway. Industry includes Microsoft Ireland, IBM Ireland, Intercom, Workhuman, Stripe, and multinational software/security engineering centers.

#### Lero - The Irish Software Research Centre

##### LLMs For Requirements And Trustworthy AI-Enabled Software

- `Homepage`: https://lero.ie/
- `Label`: `Core/strong adjacent`
- `People`: Alessio Ferrari, Jacek Dąbrowski, Amel Bennaceur, Faeq Alrimawi and the distributed Lero investigator network.
- `Focused area`: requirements engineering, software processes, trustworthy AI-enabled systems, LLM agents for elicitation and specification, safety-critical software, and industry collaboration.
- `Human-factor relevance`: requirements agents directly affect stakeholder interviews, ambiguity resolution, traceability, and responsibility for what a system is supposed to do. Lero offers access to industry and safety-critical contexts.
- `Activities / evidence`: `Prompt Me` intelligent requirements agent; LLM/NLP support for ambiguity and communication defects; national software-research and industry network.
- `Sources`: https://symeco.lero.ie/fellows/dr-jacek-dabrowski/ ; https://rosetta.lero.ie/dr-alessio-ferrari/ ; https://lero.ie/.

### Norway

- `Priority basis`: NTNU explicitly covers AI in software development and software engineering for AI systems; Norway also offers safety-critical maritime, energy, telecom, and public-sector contexts.
- `Major institutions`: NTNU Software Engineering and Information Security groups, University of Oslo, Simula Research Laboratory, SINTEF, University of Bergen, and Norwegian University of Life Sciences.
- `Research directions`: AI4SE, SE4AI, software quality/security/reliability, model-driven engineering, socio-technical software work, dependable systems, and critical infrastructure.
- `Companies/sectors`: DNV, Equinor, Telenor, Kongsberg, mnemonic, and Norwegian energy/maritime SOCs.
- `Sources`: https://www.ntnu.edu/idi/se ; https://www.ntnu.edu/idi/about.

### Brazil

- `Priority basis`: largest Latin-American CS and software ecosystem, strong universities, critical/embedded systems, formal methods, SE, and an emerging agent/AI-safety research line.
- `Major institutions`: University of São Paulo, UNICAMP, Federal University of Minas Gerais, Federal University of Pernambuco/CIn, Federal University of Rio de Janeiro/COPPE, PUC-Rio, and Federal University of Rio Grande do Sul.
- `Research directions`: agentic systems and AI auditing, formal methods, critical embedded systems, software reliability, mining software repositories, testing, security, and AI-assisted engineering.
- `Activities / evidence`: USP Agentic Complex Systems work on multi-agent systems and alignment auditing; USP LSEC on secure/dependable critical systems; LIAMF on logic, AI, planning, NLP, and formal methods.
- `Sources`: https://acs.ime.usp.br/ ; https://www.lsec.icmc.usp.br/en/ ; https://liamf.ime.usp.br/ ; https://ciaam.usp.br/en/.

### Poland

- `Priority basis`: substantial PL, formal methods, algorithms, software engineering, security, and multinational product R&D, but no single direct human-factor LLM program was strong enough in this pass for `Core`.
- `Major institutions`: University of Warsaw, Warsaw University of Technology, AGH University of Krakow, Wrocław University of Science and Technology, Poznań University of Technology, Jagiellonian University, and NASK.
- `Research directions`: verification, language tooling, compilers, software analytics, cryptography, secure systems, AI engineering, and developer tools.
- `Companies/sectors`: Google Warsaw, Microsoft, Samsung R&D Poland, Intel, Allegro, CD Projekt, Comarch, and Poland's large software-outsourcing/product-engineering sector.

### Czech Republic

- `Priority basis`: strong usable security, cryptography, systems, and formal methods with a mature national cyber-security environment.
- `Major institutions`: Masaryk University Centre for Research on Cryptography and Security, Czech Technical University in Prague, Charles University, Brno University of Technology, and Czech Technical University AI Center.
- `Research directions`: usable authentication, security measurement, formal verification, program analysis, AI security, malware, and cyber exercises.
- `Companies/sectors`: Avast/Gen, Red Hat Brno, GoodData, Productboard, and the Czech National Cyber and Information Security Agency ecosystem.

### Portugal

- `Priority basis`: relevant SE, PL, dependable distributed systems, AI, HCI, and cybersecurity groups, plus a growing engineering-services and product sector.
- `Major institutions`: INESC-ID / Instituto Superior Técnico, University of Lisbon, University of Porto, University of Minho, NOVA University Lisbon, and INESC TEC.
- `Research directions`: software evolution, formal methods, dependable systems, compilers, security, AI engineering, human-centered computing, and critical systems.
- `Companies/sectors`: Feedzai, OutSystems, Critical Software, Unbabel, Sword Health, and national cyber institutions.

### Russia

- `Priority basis`: large AI, software engineering, systems, cybersecurity, formal-methods, and developer-tool ecosystem. Current institutional affiliations, public datasets, international access, and comparability must be checked carefully because the research and product environment is affected by geopolitical and regulatory constraints.
- `Major institutions`: HSE University School of Software Engineering, ITMO School of Computer Technologies and Control, Skoltech Artificial Intelligence and Engineering centers, Moscow Institute of Physics and Technology, Innopolis University, Ivannikov Institute for System Programming of the Russian Academy of Sciences, and Moscow State University.
- `Research directions`: software and process engineering, AI systems security, MLOps/AIOps, multi-agent security, cyber-physical systems, program analysis and verification, compilers, and high-performance systems.
- `Companies/sectors`: Yandex, Kaspersky, Positive Technologies, Sber AI, VK, MTS, JetBrains researchers with historical Russian links, and large finance/telecom/industrial engineering organizations.
- `Evidence gap`: independent human-subject and organizational studies, transparent datasets, reproducible evaluation, and current institution/company relationships need verification before promotion to `Core`.
- `Sources`: https://cs.hse.ru/en/dse/ ; https://en.itmo.ru/en/faculty/1/School_of_Computer_Technologies_and_Control.htm ; https://news.itmo.ru/en/education/students/news/14767/ ; https://www.skoltech.ru/en/center/ai.

### Turkey

- `Priority basis`: substantial computer-systems, security, software-engineering, requirements, and defense/industrial research, with direct 2025-2026 work on LLM security requirements and people/management debt in ML-integrated projects.
- `Major institutions`: Middle East Technical University, Bilkent University, Boğaziçi University, Koç University, Sabancı University, Istanbul Technical University, and TÜBİTAK BİLGEM.
- `Research directions`: systems and cloud security, autonomous-system security, security requirements, software process and management debt, formal modeling, AI engineering, cyber-physical systems, and human-computer interaction.
- `Activities / evidence`: METU S2RL spans cloud, IoT, autonomous systems, access control, digital forensics, and formal security policies; METU records include LLM-based implicit-security-requirements classification and industry studies of ML-integrated software projects.
- `Companies/sectors`: ASELSAN, HAVELSAN, Turkish Aerospace, Turkcell, Trendyol, Getir, and finance/telecom SOCs.
- `Sources`: https://s2rl.iam.metu.edu.tr/ ; https://avesis.metu.edu.tr/ttemizel/yayinlar ; https://ceng.metu.edu.tr/en/node/216.

### South Africa

- `Priority basis`: the most important missing Sub-Saharan African comparison, combining national cyber R&D, digital forensics, cyber ranges, software development, critical infrastructure, skills development, and multilingual/social context.
- `Major institutions`: CSIR Information and Cybersecurity Research Centre, University of Cape Town, University of the Witwatersrand, Stellenbosch University, University of Pretoria, and University of Johannesburg.
- `Research directions`: sovereign cybersecurity, cybercrime and digital forensics, malware and dark-web analysis, critical infrastructure, cyber ranges, secure software, AI/ML security, human capacity, and public-sector deployment.
- `Human-factor relevance`: South Africa enables study of skills shortages, uneven access to AI tooling, multilingual workflows, public-sector constraints, and whether LLM assistance broadens capability without increasing dependence or risk.
- `Companies/sectors`: banks and fintech, telecom operators, mining/energy operators, Orange Cyberdefense/SensePost heritage, and national cyber institutions.
- `Sources`: https://wwwprod.csir.co.za/information-and-cybersecurity-research-centre ; https://www.csir.co.za/what-we-do/defence-and-security/information-and-cybersecurity/cybersecurity-systems.

### Mexico

- `Priority basis`: large software-development, nearshore, higher-education, manufacturing, and financial-technology ecosystem; direct LLM/software human-factor evidence was not sufficiently consolidated in this pass.
- `Major institutions`: National Autonomous University of Mexico, CINVESTAV, Tecnológico de Monterrey, Instituto Politécnico Nacional, and Centro de Investigación en Computación.
- `Research directions`: software engineering, formal methods, cybersecurity, AI, embedded/industrial systems, HCI, and Spanish-language developer tooling.
- `Companies/sectors`: nearshore software engineering, automotive and electronics manufacturing, banks/fintech, telecom, IBM/Microsoft/Oracle engineering centers, and national incident-response institutions.
- `Evidence gap`: current group/PI mapping and first-party evidence for coding agents, SOC copilots, and SE for production LLM systems.
- `Sources`: https://www.pcic.unam.mx/ ; https://www.seguridad.unam.mx/proyectos ; https://www.icat.unam.mx/en/information-technology-educational-processes/ ; https://tec.mx/es/investigacion/innovacion-en-tecnologias-e-infraestructuras-digitales-inteligentes.

### United Arab Emirates And Gulf

- `Priority basis`: rapid sovereign-AI and cyber investment, model deployment, critical-infrastructure operations, and cyber ranges; public human-study and software-maintenance evidence is still sparse.
- `Major institutions`: MBZUAI, NYU Abu Dhabi, Khalifa University, Technology Innovation Institute, Qatar Computing Research Institute, Carnegie Mellon University Qatar, and KAUST in Saudi Arabia.
- `Research directions`: foundation-model engineering, AI safety/security, systems, cyber operations, Arabic-language software and security tooling, and critical infrastructure.
- `Companies/sectors`: G42, Core42, Presight, TII, Saudi Aramco and energy SOCs, regional sovereign clouds, and the UAE Cyber Security Council ecosystem.
- `Evidence gap`: study operator authority, multilingual interfaces, sovereign-cloud constraints, procurement, and responsibility allocation.

### New Zealand

- `Priority basis`: smaller research population but useful Five Eyes, public-sector, indigenous-data, usable-security, and operational-comparison context.
- `Major institutions`: University of Auckland, University of Waikato, Victoria University of Wellington, University of Canterbury, University of Otago, and Massey University.
- `Research directions`: software engineering, HCI, usable security, AI governance, research software, digital-risk protection, and critical infrastructure.
- `Companies/sectors`: NCSC New Zealand, CERT NZ functions, Datacom, Spark, Xero, Aura Information Security, and financial/telecom SOCs.

### EU-Level Actors Across The European Profiles

- `Strong adjacent`: ENISA, the European Cybersecurity Competence Centre, European AI Office, Europol EC3, NATO CCDCOE, ELLIS, CLAIRE, and Horizon Europe AI/cyber programs.
- `Additional national nodes`: Luxembourg's University of Luxembourg/SnT; Estonia's University of Tartu, TalTech, and NATO CCDCOE ecosystem; Greece's FORTH, National Technical University of Athens, and University of Athens; and Romania's University Politehnica of Bucharest and national cyber research should be tracked in the next institution-level pass.
- `Human-factor relevance`: EU rules and institutions determine who evaluates, documents, certifies, reports, audits, and takes responsibility for AI-enabled software. They should be treated as workflow and organizational variables, not merely background regulation.
- `Research need`: compare how EU conformity, incident-reporting, data-governance, worker-consultation, and cyber-resilience duties alter developer and security-operator behavior across the countries above.
 For The Human-Factors Layer

- Which requirements, design, coding, comprehension, review, testing, debugging, repair, migration, optimization, operations, and security tasks benefit from LLM collaboration, and which decisions should remain human-authoritative?
- Does an assistant reduce end-to-end delivery time after clarification, context preparation, test generation, review, integration, rework, incident risk, and later maintenance are counted?
- When does an agent improve software correctness, reliability, maintainability, security, and performance rather than merely increase change volume?
- What UI patterns reduce over-trust without creating approval fatigue, and which actions should be blocked, confirmed, sampled, independently verified, staged, or automatically rolled back?
- How should coding agents present intent, uncertainty, provenance, retrieved context, dependency authenticity, license/data-use policy, test adequacy, security findings, performance evidence, and unresolved assumptions?
- How can reviewers efficiently evaluate large multi-file agent changes without diff fatigue, shallow approval, or loss of architectural awareness?
- Which combinations of execution, types, static analysis, model checking, theorem proving, differential/metamorphic tests, fuzzing, and independent models provide useful assurance without overwhelming developers?
- Can generated proofs, invariants, specifications, counterexamples, and explanations reduce formal-methods effort while preserving a small trusted base and understandable proof lineage?
- How should performance agents demonstrate semantic equivalence, numerical stability, representative workload gains, cost/energy effects, and portability across compilers and hardware?
- How should OS/cloud/AIOps assistants preserve operator situation awareness, least privilege, blast-radius control, escalation, rollback, and post-incident learning?
- How should prompt programs, RAG, memory, tool schemas, MCP servers, model routing, orchestration, evaluators, and guardrails be versioned, tested, reviewed, observed, and owned as software?
- What evidence detects correlated failure when the same model family writes code, tests it, reviews it, explains it, and decides whether it is correct?
- How do model, API, data, retrieval, tool, and environment drift alter previously accepted software behavior, and who owns regression detection and remediation?
- How should AI coding assistants handle secrets, personal/proprietary code, training-data provenance, generated packages, licenses, model/tool supply chains, and incident disclosure?
- How should SOC copilots preserve analyst situation awareness and skill development instead of hiding the reasoning path?
- What is the right evidence handoff from AI vulnerability agents to maintainers, bounty triagers, vendors, and disclosure coordinators?
- How can reverse-engineering assistants expose enough intermediate reasoning for analysts to detect hallucinated symbols, types, comments, or control-flow summaries?
- How should organizations train developers, reviewers, operators, scientists, students, SOC analysts, reverse engineers, and red teamers to challenge LLM output instead of merely consuming it?
- Which interaction styles support durable learning and unaided transfer for novices without frustrating experts, and how do accessibility, language, culture, and domain background change the result?
- How does agent-generated work redistribute credit, accountability, job design, onboarding, code ownership, and maintenance burden across teams and open-source communities?
- What metrics capture human-AI complementarity: delivered value, correctness, review acceptance, reliability, maintainability, performance, energy/cost, evidence quality, exploitability validation, skill transfer, cognitive load, false-positive burden, safe escalation, rollback, and auditability?
- Which findings replicate across professional and student populations, open and proprietary repositories, source and binary work, application and system software, English and Chinese, and chat/IDE/CLI/agent interfaces?
- For USA-China comparison, which differences come from model capability, which from developer/SOC culture, which from platform design, and which from governance?

The practical test is:

`engineering value = accepted behavior and organizational learning − specification/context effort − verification/review/rework cost − operational and security risk − future evolution cost`

Shorter code, higher benchmark scores, more accepted suggestions, and faster first drafts are useful measurements, but none is a complete measure of engineerability.
