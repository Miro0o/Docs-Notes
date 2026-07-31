---
ai-generated: true
last-reviewed: 2026-07-30
---

# Human Factor: LLMs For Software Security And Analysis

Date: 2026-07-30

Home: [LLM-Software-Security-Research-Dossier-2026.md](LLM-Software-Security-Research-Dossier-2026.md)

This file covers the socio-technical layer of LLMs for software security and analysis: developer behavior, SOC analyst collaboration, reverse-engineering assistance, red-team labor, bug-bounty and maintainer workflows, oversight, approval burden, trust calibration, and the research ecosystem around human-facing security systems.

## Main Focus: United States And China As Of 2026-07-30

The United States and China should be treated as the primary country pair for this dossier.

- The United States has the densest direct evidence for human factors: controlled secure-coding user studies, human-LLM reverse-engineering experiments, SOC fieldwork, HCI work on LLM red teaming, agent-approval research, AIxCC-style cyber reasoning systems, bug-bounty telemetry, and large security-product deployments.
- China has the densest non-U.S. ecosystem around Chinese-language cybersecurity benchmarks, model-safety contests, public generative-AI security regulation, code/agent platforms, and security vendors. Direct published human-subject work on LLM + software security is thinner than in the United States, so China should be mapped as a mixed evidence base: benchmark/contest/platform/guidance evidence plus a watchlist of labs and companies likely to produce human-facing studies.
- For both countries, the practical unit of analysis is not just the model. It is the human plus model plus scaffold plus tool permissions plus UI plus audit logs plus validation harness plus organizational governance.

### Confidence Labels Used Below

- `Core`: direct LLM + security + human/organizational evidence, or an official source that directly shapes human-facing deployment.
- `Strong adjacent`: active in LLM/software/security or AI security with clear human-factor relevance, but not always a human-subject study.
- `Watch`: important ecosystem actor whose public record is relevant but where direct human-factors evidence needs follow-up before citation in a paper.

## Core Human-Factors Threads

These threads summarize the evidence that should be mapped back to the institution, lab, unit, or platform entries below. They are synthesis, not the organizing spine of the file.

- Secure coding with AI assistants: Stanford's controlled study found that AI-assistant access can make users write less secure code while also increasing their confidence that the code is secure; prompt behavior and trust mattered. NYU's `Lost at C` study found a smaller effect in a C/pointer task, which is useful because it shows that task design, participant skill, interface, and language strongly shape results. Sources: https://arxiv.org/abs/2211.03622 ; https://par.nsf.gov/biblio/10472129-do-users-write-more-insecure-code-ai-assistants ; https://arxiv.org/abs/2208.09727 ; https://zenodo.org/record/7187358.
- Developer training and secure prompting: newer studies are shifting from "does the model emit insecure code?" to "can developers be trained to use LLM assistance more safely?" UCF SEAL work reports a quasi-experimental developer study where targeted security training reduced validated weaknesses in LLM-assisted backend code. Sources: https://seal.cs.ucf.edu/ ; https://arxiv.org/abs/2604.17763.
- SOC analyst collaboration: the strongest empirical line is in-the-wild SOC work. CSIRO Data61's study analyzes real analyst LLM use over time; USF / KU / USC ISI / Resideo work uses practitioner-centered SOC field methods to study whether LLM tools can be introduced without disrupting high-stress operational workflows. Sources: https://arxiv.org/abs/2508.18947 ; https://www.isi.edu/results/publications/65207/a-sociotechnical-practitioner-centered-approach-to-technology-adoption-in-cybersecurity-operations-an-llm-case ; https://www.ndss-symposium.org/ndss-paper/auto-draft-741/.
- Reverse engineering and analyst tooling: the NDSS 2026 human-LLM software reverse-engineering study surveyed practitioners and ran a controlled LLM-assisted reverse-engineering experiment, finding that LLMs can narrow novice/expert gaps while still misleading analysts through hallucinated or overconfident explanations. Sources: https://www.eurecom.fr/en/publication/8548 ; https://adamdoupe.com/publications/decompiling-synergy-ndss2026.pdf.
- Agent-human interaction security: UCLA's 2026 work argues that LLM-agent security is an agent-human interaction problem because production systems rely heavily on policy specification, runtime approval, and scope configuration, creating approval-fatigue and cognitive-burden tradeoffs. Sources: https://arxiv.org/abs/2605.24309 ; https://ucla-sec-lab.netlify.app/.
- Human susceptibility to compromised agents: HAT-Lab work on agent-mediated deception studies how users perceive attacks mediated by trusted LLM agents, including professional scenarios such as software development. Source: https://arxiv.org/abs/2602.21127.
- GUI-agent oversight and deceptive interfaces: CHI 2026 work on dark patterns and GUI agents shows that neither humans nor agents are uniformly resilient; human oversight can improve outcomes but also introduces attentional tunneling and cognitive-load costs. Sources: https://arxiv.org/abs/2509.10723 ; https://doi.org/10.1145/3772318.3791568.
- Red teaming as human work: AI red teaming is becoming a socio-technical labor practice involving dataset design, practitioner judgment, risk framing, and evaluation standards, not only jailbreak success rates. Sources: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0314658 ; https://research.ibm.com/publications/red-teaming-llms-as-socio-technical-practice-from-exploration-and-data-creation-to-evaluation ; https://doi.org/10.1145/3772318.3790792.
- Human oversight in cyber reasoning systems: AIxCC, OSS-CRS, foundation-model cyber programs, bug-bounty platforms, and autonomous pentesting tools all show that humans remain essential at target selection, policy setting, result triage, patch review, coordinated disclosure, and maintainer acceptance. Sources: https://www.darpa.mil/research/programs/ai-cyber ; https://www.darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33 ; https://openssf.org/tag/cyber-reasoning-systems/ ; https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy.

## United States Detailed Record

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

#### Microsoft

##### Microsoft Security Copilot

- `Homepage`: https://learn.microsoft.com/en-us/copilot/security/
- `Label`: `Core`
- `Focused area`: SOC copilot workflows, incident response, threat hunting, policy management, plugins, connectors, promptbooks, and custom agents.
- `Human-factor relevance`: Security Copilot is a major production example of LLM assistance for named security personas. Track evidence visibility, analyst authority, generated KQL/query trust, plugin grounding, and auditability.
- `Activities / evidence`: embedded Defender/Sentinel/Entra/Purview experiences, custom agents, promptbooks, audit-log features.
- `Sources`: https://learn.microsoft.com/en-us/copilot/security/ ; https://learn.microsoft.com/en-us/security-copilot/microsoft-security-copilot.

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

#### UC San Diego

##### Center for Machine-Intelligence, Computing and Security

- `Homepage`: https://mics.ucsd.edu/node/267
- `Label`: `Watch`
- `Focused area`: machine intelligence, computing systems, security and privacy, hardware/software/data integration, and cyber-physical security.
- `Human-factor relevance`: UCSD should not be represented by only a CSE research-area page. MICS is a more concrete center for AI/security/system integration; track whether security-AI tools are evaluated with expert users, not only benchmark labels.
- `Sources`: https://mics.ucsd.edu/node/267.

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

#### Princeton University

##### Center for Information Technology Policy

- `Homepage`: https://citp.princeton.edu/
- `Label`: `Watch`
- `Focused area`: AI governance, platform policy, security, privacy, and accountability.
- `Human-factor relevance`: CITP matters for accountability when AI-generated code or AI-generated vulnerability reports cause downstream harm.

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

### USA: Main Focus Areas To Track

- Developer secure-code behavior: over-trust, prompt quality, AI-suggestion acceptance, generated-dependency risk, insecure code review, and training interventions.
- SOC analyst work: alert fatigue, situation awareness, evidence grounding, analyst authority, low-level telemetry interpretation, and handoff between AI summaries and human decisions.
- Reverse engineering and binary analysis: LLM-generated symbol names, type recovery, decompiler comments, explanation confidence, hallucinated control-flow summaries, and novice/expert gap reduction.
- Agent oversight: policy specification, runtime approval, scope configuration, audit logs, identity, data-access permissions, tool-call transparency, and approval fatigue.
- Red-team labor: who creates adversarial examples, how risk categories are chosen, how datasets become benchmarks, and whether model providers ignore user specificity and interaction context.
- Bug-bounty and maintainer workflows: AI-generated report volume, invalid-report burden, agentic validation, coordinated disclosure, and evidence thresholds for maintainers.

## China Detailed Record

China should be treated as the second main focus, but with a different evidence profile. The public record is strongest in Chinese-language cybersecurity benchmarks, model-safety evaluation platforms, contests, standards, AI coding products, and security-vendor ecosystems. Direct human-subject studies on LLM-assisted secure coding, SOC analysts, or reverse engineering are less visible than in the United States, so many entries are marked `Strong adjacent` or `Watch`. Entries below are organized by institution, lab, company, standards body, or platform; projects and contests appear as activities unless the host institution is not yet clear enough.

### China: Companies, Platforms, Standards Bodies, And Security Ecosystem

#### Alibaba (阿里巴巴)

##### Alibaba Security (阿里巴巴安全)

- `Homepage`: https://security.alibaba.com/
- `Label`: `Core`
- `Focused area`: industry security research, vulnerability response, platform security, AI security evaluation, and cybersecurity benchmarking.
- `Human-factor relevance`: Alibaba Security should host the CS-Eval evidence in the China map because it connects benchmark design to operational security categories used by practitioners.
- `Activities / evidence`: CS-Eval / CyberSec-Eval collaboration, Alibaba Cloud AI security challenge, security platform work.
- `Sources`: https://security.alibaba.com/ ; https://cs-eval.com/ ; https://github.com/CS-EVAL/CS-Eval.

##### Alibaba Cloud Tongyi Lingma (阿里云通义灵码)

- `Homepage`: https://tongyi.aliyun.com/lingma/
- `Label`: `Strong adjacent`
- `Focused area`: AI coding assistant, code generation, enterprise developer tools, and developer workflow.
- `Human-factor relevance`: Tongyi Lingma is the developer-facing workflow surface. Track secure-code suggestions, repository context, code privacy, generated-code review, and enterprise governance.

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

#### Huawei Cloud (华为云)

##### Pangu Large Models (盘古大模型)

- `Homepage`: https://www.huaweicloud.com/intl/en-us/product/pangu.html
- `Label`: `Strong adjacent`
- `Focused area`: enterprise foundation models, cloud AI deployment, private deployment, and industry-specific model services.
- `Human-factor relevance`: Huawei Cloud is important for regulated-sector and enterprise adoption. Track how private/cloud deployment, access control, and auditability affect organizational willingness to use LLMs for security or code work.

#### Baidu (百度)

##### ERNIE / Qianfan (文心一言 / 千帆)

- `Homepage`: https://qianfan.cloud.baidu.com/
- `Label`: `Strong adjacent`
- `Focused area`: foundation models, model platform services, public-facing assistants, and enterprise AI deployment.
- `Human-factor relevance`: Baidu should be tracked for model-platform governance and developer/SOC-facing AI integrations, especially access, logging, approval, content reliability, and user-facing assistant design.

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

#### Ant Group (蚂蚁集团)

##### Ant Ling / LingGuang (Ant Ling / 灵光) / Privacy-Preserving AI

- `Homepage`: https://www.antgroup.com/en/technology
- `Label`: `Strong adjacent`
- `Focused area`: financial technology, privacy-preserving AI, enterprise AI services, assistant workflows, and natural-language app generation.
- `Human-factor relevance`: Ant Group is a strong watch actor because financial and consumer contexts require trust, privacy, and user comprehension. Natural-language-to-app workflows raise software-security questions around auth, data flow, and permissions.

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

#### Fudan University (复旦大学)

##### System Software and Security Lab (系统软件与安全实验室) / Whitzard-AI

- `Homepage`: https://mi-zhang-fdu.github.io/index.html
- `Label`: `Core`
- `People`: Mi Zhang and Whitzard-AI / SSS Lab contributors.
- `Focused area`: LLM/MM-LLM security, agent security, intelligent system security, ML/DL security, AI for security, and Chinese-language safety evaluation.
- `Human-factor relevance`: This is a primary China group for Chinese-language LLM safety evaluation. JADE should be treated as an activity under the Fudan SSS/Whitzard-AI profile, not as the profile itself.
- `Activities / evidence`: JADE safety evaluation platform, JADE-DB, TC260 standards participation, CS-Eval collaboration.
- `Sources`: https://mi-zhang-fdu.github.io/index.html ; https://whitzard-ai.github.io/jade_en.html ; https://cs-eval.com/.

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
- `Focused area`: automated reliable intelligent software engineering, software quality, intelligent SE, reliability, and LLM/software-engineering methods.
- `Human-factor relevance`: ARISE is the concrete CUHK software-engineering lab for future code-LLM mapping. Human-factor questions include how developers review generated tests, explanations, and reliability evidence.
- `Sources`: https://ariselab.cse.cuhk.edu.hk/.

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
- AI coding assistants and code models: Alibaba Lingma/Qwen, ByteDance Trae, DeepSeek-Coder, Huawei/Baidu/Tencent/Ant model platforms. Focus on code privacy, context retention, generated dependency risk, secure-code prompts, and enterprise governance.
- Model safety red teaming: JADE, Tianwang Cup large-model track, Tencent Zhuque, Alibaba/Tencent/Baidu/DeepSeek safety activity. Focus on prompt injection, jailbreaks, data leakage, content reliability, model supply-chain attacks, and how human judges score reports.
- SOC and security-vendor deployment: Qihoo 360, Qi-Anxin, NSFOCUS, Sangfor, Topsec, DBAPPSecurity, Chaitin, Knownsec, ThreatBook, Alibaba/Tencent/Huawei/Baidu cloud security. Focus on analyst workload, false positives, incident explanation quality, and Chinese enterprise compliance.
- Governance and standards: CAC generative-AI measures, TC260 basic security requirements, CAICT vulnerability/security evaluation, Chinese AI Safety Network. Focus on how security assessment requirements shape human approval, content review, and operational auditability.
- Research gap: China has strong technical capability and benchmark/contest signals, but public direct human-subject studies for LLM-assisted secure coding, SOC, reverse engineering, and bug-bounty triage are still much less visible than in the U.S. This is a high-value research gap.

## USA-China Comparison For Human Factors

| Human-factor layer | United States | China | Research implication |
| --- | --- | --- | --- |
| Secure coding with AI | Strong direct user-study base from Stanford, NYU, UCF, plus broad GitHub/Copilot and AI IDE deployment | Strong model/platform base through Qwen/Lingma, Trae, DeepSeek-Coder, Code LLM labs; fewer visible controlled human studies | Replicate secure-coding user studies in Chinese developer settings and compare language, IDE, task, and training effects. |
| SOC analyst collaboration | Direct fieldwork from Data61/eSentire and USF/KU/USC ISI/Resideo lines; major U.S. SOC vendors productizing copilots | Large security-vendor and MSSP ecosystem, but fewer public in-the-wild SOC LLM studies | Study Chinese SOC adoption with ethnographic and query-log methods, especially under regulatory and data-localization constraints. |
| Reverse engineering | ASU/EURECOM/Padua NDSS 2026 gives direct human-LLM evidence | Strong binary/software-security labs and CTF teams; direct human-LLM reverse-engineering evidence appears thinner | Run controlled bilingual reverse-engineering experiments with Chinese analysts, decompilers, and local tooling. |
| Agent oversight | UCLA, NIST CAISI, UW, CMU SEI, OWASP/CSA focus on runtime approval, permissions, identity, auditability | CAC/TC260/CAICT governance plus Tencent Zhuque/OpenClaw and platform security activity | Compare user approval UX and institutional approval requirements: individual runtime approval versus provider/security-assessment regimes. |
| Red teaming | Strong HCI/social-science evidence on red-team labor, data practices, and motivations | Strong contest and platform activity around jailbreak, prompt injection, and model safety | Connect Chinese contest artifacts to socio-technical red-team labor studies; measure how scoring rules shape attack creativity and report quality. |
| Bug-bounty and maintainer handoff | HackerOne, Bugcrowd, OpenSSF, AIxCC, OSS-CRS make report quality and maintainer acceptance central | More contest/range and vendor-centered signals; public bug-bounty telemetry is less visible | Compare whether AI increases invalid-report burden differently in platform bounty versus contest/range ecosystems. |
| Governance | NIST CAISI, CISA, DARPA, MITRE, OpenSSF, OWASP/CSA practitioner guidance | CAC, TC260, CAICT, Chinese AI Safety Network, model-service security assessments | Treat governance as part of the human factor: it determines who must approve, audit, file, disclose, and take responsibility. |

## Secondary Country Profiles

These profiles are kept as secondary context. The USA and China sections above remain the main focus, but the broader map is useful for tracking collaborators, comparative case studies, and non-U.S./non-China deployment patterns.

### Canada

- `Core` eSentire / University of Waterloo / SpyCloud-associated SOC research: Martin Lochner, Keegan Keplinger and collaborators. Live SOC LLM use, topic modeling of analyst queries, and human expert validation in MDR workflows. Sources: https://arxiv.org/abs/2508.18488 ; https://www.esentire.com/.
- `Strong adjacent` University of Waterloo Cheriton School of Computer Science: Meng Xu, Sihang Liu and collaborators on LLM-agent security against malicious or vulnerable tools. Source: https://uwaterloo.ca/computer-science/news/meng-xu-sihang-liu-254k-funding-national-cybersecurity-consortium-strengthen-security-llm-agents.
- `Watch` Queen's University L1NNA Lab, Concordia SPNET, University of Toronto / Schwartz Reisman Institute / Vector Institute, University of British Columbia, McGill, Carleton, Royal Military College of Canada. Track for AI security, human-AI collaboration, autonomous-system policy, and critical-infrastructure security.
- `Companies/sectors` eSentire, BlackBerry Cylance, OpenText Cybersecurity, Arctic Wolf Canada presence, Cohere, National Cybersecurity Consortium, and Canadian Centre for Cyber Security.

### United Kingdom

- `Core/strong adjacent` UK AI Security Institute: frontier model cyber evaluations, human-influence risk, pre-release testing, and government-facing safety science. Source: https://www.aisi.gov.uk/about.
- `Core/strong adjacent` Laboratory for AI Security Research (LASR): UK public-private AI-security partnership connecting academia, industry, and government. Source: https://lasr.ac.uk/.
- `Strong adjacent` King's College London Cybersecurity Group: AI/ML for cybersecurity, verification/testing, trust, explainability, and human factors. Source: https://www.kcl.ac.uk/research/cys.
- `Strong adjacent` Imperial College London AI Security and Privacy Lab: privacy and safety of AI systems, LLMs, and agentic systems. Source: https://aisp.doc.ic.ac.uk/.
- `Watch` RISCS, UCL human-centered security, University of Bristol cyber/human factors, Newcastle Secure and Resilient Systems, University of Oxford Cyber Security Centre, University of Cambridge, University of Edinburgh, University of Sheffield, University of Southampton, Royal Holloway.
- `Companies/sectors` NCSC, Darktrace, NCC Group, PortSwigger, Mind Foundry, OutThink, BT Security, BAE Systems Digital Intelligence, GCHQ/NCSC ecosystem, Plexal, Cisco UK, and UK defense/critical-infrastructure AI-security suppliers.

### Australia

- `Core` CSIRO Data61: Shahroz Tariq, Ronal Singh, Fatemeh Jalalvand, Mohan Baruwal Chhetri, Surya Nepal, Cecile Paris, Martin Lochner and collaborators. Human-AI collaboration in SOCs, alert fatigue, expertise-gap studies, and responsible AI/software-systems engineering. Sources: https://arxiv.org/abs/2508.18947 ; https://arxiv.org/abs/2505.03179 ; https://research.csiro.au/ss/ ; https://www.csiro.au/en/about/people/research-units/Data61.
- `Watch` Cyber Security Cooperative Research Centre, UNSW Canberra Cyber, University of Melbourne, Monash, University of Adelaide/AIML, RMIT, University of Queensland, Macquarie, Australian National University. Track for human-centered cybersecurity, AI safety, cyber ranges, and critical-infrastructure security.
- `Government/industry` ASD Australian Cyber Security Centre, Home Affairs, CSIRO, CyberCX, Telstra, Atlassian, Canva, and Australian financial/critical-infrastructure SOCs. Five Eyes guidance makes Australia important for secure agentic-AI adoption in operational settings. Source: https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services.

### France

- `Core` IRT SystemX / Airbus Protect / Reseau de Transport d'Electricite (RTE): Reda Yaich, Alexandre Balondrade, Antoine Sicard, Christelle Fouquiau, Guillaume Giraud, Kahina Amokrane-Ferka, Emmanuel Arbaretier. Human-AI SOC collaboration, cognitive profiling, agentic coordination, and VOWEL+U oversight framework. Source: https://ojs.aaai.org/index.php/AAAI-SS/article/download/36072/38227/40160.
- `Core` EURECOM: Simone Aonzo and collaborators in the human-LLM software reverse-engineering study. Source: https://www.eurecom.fr/en/publication/8548.
- `Watch` INRIA, CEA LIST, CNRS, ANSSI, Institut Polytechnique de Paris, Sorbonne Universite, Grenoble Alpes, Telecom Paris, EURECOM, SystemX. Track for AI security, formal methods, SOC/critical-infrastructure cyber, and human-machine teaming.
- `Companies/sectors` Airbus Protect / Airbus Defence and Space Cyber, Mistral AI, Thales, Dassault, Orange Cyberdefense, Capgemini, Atos/Eviden, Quarkslab, Stormshield, RTE and energy-sector SOCs. Source: https://cyber.airbus.com/en/offers/artificial-intelligence-in-cybersecurity.

### Germany

- `Core/strong adjacent` TU Darmstadt PEASEC / ATHENE HAICC: explicit `Human-AI Collaboration for Cybersecurity` work, cybersecurity/privacy, HCI, and peace/security studies. Source: https://peasec.de/.
- `Core/strong adjacent` TU Berlin MLSEC: Konrad Rieck's group works at the ML/security intersection and includes LLMs in security, vulnerability discovery, and related evaluation. Source: https://mlsec.org/.
- `Core/strong adjacent` CISPA Helmholtz Center / moosec: ML security, LLM security, agent systems, vulnerability analysis, fuzzing, and malware classification. Sources: https://cispa.de/en ; https://moosec.org/.
- `Watch` KIT / KASTEL Security Research Labs, Fraunhofer AISEC/SIT, Ruhr University Bochum CASA/RC Trust/AISOC, Max Planck Institute for Security and Privacy, h_da User-Centered Security, TU Munich, Saarland University. Sources: https://intellisec.de/ ; https://kastel-labs.de/about-kastel/ ; https://informatik.rub.de/aisoc/.
- `Companies/sectors` Aleph Alpha, SAP Security Research, Siemens, Bosch, Deutsche Telekom/T-Systems, Rohde & Schwarz, secunet, Fraunhofer transfer ecosystem, industrial/automotive/OT security vendors.

### Italy

- `Core` University of Padua: Samuele Doria, Eleonora Losiouk and collaborators in the NDSS 2026 human-LLM reverse-engineering study. Source: https://www.research.unipd.it/handle/11577/3588620.
- `Watch` Politecnico di Milano, University of Trento, Sapienza University of Rome, University of Cagliari, IMT Lucca, FBK. Track for software security, HCI/security, AI assurance, and cyber ranges.
- `Companies/sectors` Leonardo, Engineering Group, Reply, Yarix/Var Group, Italian National Cybersecurity Agency ecosystem.

### Denmark

- `Core` IT University of Copenhagen: Nanna Inie and Leon Derczynski's grounded-theory work on LLM red teaming; Leon Derczynski also has NVIDIA affiliation. Source: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0314658.
- `Watch` University of Copenhagen, Aalborg University, Aarhus University, Technical University of Denmark, Alexandra Institute. Track for HCI, NLP, trustworthy AI, cybersecurity, and human-centered security.
- `Companies/sectors` Nordic financial SOCs, TDC NET, Trifork, Systematic, LEGO/enterprise secure AI adoption, and Danish Centre for AI Innovation / national AI-safety activity.

### Sweden And Nordics

- `Core/strong adjacent` KTH Royal Institute of Technology / NTU / William & Mary HAT-Lab collaboration: public coverage identifies KTH as part of the agent-mediated-deception user study, making it a direct Nordic signal for human-centric agent security. Sources: https://arxiv.org/abs/2602.21127 ; https://www.secrss.com/articles/89556.
- `Watch` Linkoping University RESIST Center, KTH Cybercampus Sverige / CDIS / Royal Hacking Lab, Orebro University MPI Lab, Chalmers, Lund University, Stockholm University, Uppsala University, RISE Research Institutes of Sweden, Karlstad University SIGS-CyberSec. Sources: https://resist-center.se/en ; https://lab.cybercampus.se/ ; https://mpi.aass.oru.se/ ; https://sola.kau.se/sigscybersec/.
- `Companies/sectors` Ericsson, Saab, Sectra, Combitech, Truesec, Recorded Future, Nordic Sentinel, Swedish telecom/defense/industrial SOCs, and Nordic financial-sector security teams.

### Spain

- `Core/strong adjacent` HASP Lab at INGENIO / CSIC / Universitat Politecnica de Valencia: human-centered AI security, ethics, privacy, HCI, and work on malicious LLM-based conversational AI. Source: https://hasp-lab.github.io/.
- `Core/strong adjacent` Universidad Politecnica de Madrid: AI-augmented cybersecurity requirements generation evaluated against human expert ground truth. Source: https://portalcientifico.upm.es/en/ipublic/item/10450496.
- `Watch` INCIBE, Universidad Carlos III de Madrid, Universidad de Malaga, University of Granada, Barcelona Supercomputing Center, Spanish AI and cybersecurity research networks.
- `Companies/sectors` Telefonica Tech, Indra/Minsait, S2 Grupo, GMV, BBVA/Santander security labs, IBM Spain language-model collaboration ecosystem.

### Netherlands, Switzerland, Belgium, And EU-Level Actors

- `Watch` TU Delft, University of Twente, Radboud, Eindhoven University of Technology, Leiden, KU Leuven, Vrije Universiteit Brussel, ETH Zurich, EPFL, University of Zurich, IBM Research Zurich, Cyber-Defence Campus armasuisse. Track for usable security, privacy engineering, software verification, AI safety, and human-centered AI.
- `EU-level` ENISA, European Cybersecurity Competence Centre, European AI Office, Europol EC3, NATO CCDCOE, ELLIS, CLAIRE, Horizon Europe AI/cyber programs. These matter for governance, certification, incident reporting, cyber ranges, and human-in-the-loop assurance requirements.

### Singapore

- `Core/strong adjacent` NTU Cyber Security Lab, NTU Digital Trust Centre, NTU/Singtel SCALE, Imperial-NTU IN-CYPHER. Track for AI for cybersecurity, trustworthy AI, health cybersecurity, automation, vulnerability discovery, and human/machine verification. Sources: https://www.ntu.edu.sg/computing/research/institutes-centres/csl ; https://www.ntu.edu.sg/dtc ; https://www.imperial.ac.uk/about/global/singapore/research/in-cypher/.
- `Core/strong adjacent` NTU / KTH / William & Mary HAT-Lab collaboration: agent-mediated deception and human perception vulnerability in LLM-driven agentic systems. Source: https://arxiv.org/abs/2602.21127.
- `Watch` National University of Singapore, SUTD iTrust, Singapore Management University, AI Singapore, Centre for Strategic Infocomm Technologies, DSO National Laboratories, GovTech. Track for secure software engineering, cyber ranges, AI governance, and trustworthy AI.
- `Companies/sectors` Singtel/NCS, ST Engineering, Mastercard-NTU lab, Ant International-NTU PET/LLM collaboration, financial-sector SOCs, CSA Singapore and Digital Trust Centre ecosystem.

### Japan

- `Watch` NICT Cybersecurity Research Institute / CREATE, AIST Intelligent Platform Research Institute, University of Tokyo, Kyoto University, Osaka University, Waseda, Keio, Tokyo Institute of Science, JAIST. Track for AI security, LLM evaluation, cybersecurity training, human resources, and industry-government collaboration. Sources: https://www.nict.go.jp/en/research/index.html ; https://create.nict.go.jp/en/ ; https://unit.aist.go.jp/ipri/en/.
- `Companies/sectors` NTT, NEC, Fujitsu, Hitachi, KDDI, Rakuten, Trend Micro Japan, Preferred Networks, automotive/robotics/OT security suppliers, JPCERT/CC and NISC ecosystem.

### South Korea

- `Core/strong adjacent` Ewha Womans University / Kumoh National Institute of Technology / Coretrustlink: Gyuyeon Na, Minjung Park, Hyeonjeong Cha, Sangmi Chai on a human-centered LLM-agent system for digital-asset anomaly detection. Source: https://arxiv.org/abs/2510.20102.
- `Watch` KAIST, Korea University AIR Lab / cyber defense, Seoul National University HCI+AI, Sogang HAICoLab, Sungkyunkwan University InfoLab, POSTECH, Yonsei. Track for human-AI collaboration, AI for cybersecurity, trustworthy AI, and LLM-based agents. Sources: https://air.korea.ac.kr/ ; https://haicolab.sogang.ac.kr/.
- `Companies/sectors` Samsung Research, LG AI Research, Naver, Kakao, SK Telecom, AhnLab, KISA, KOTRA cyber export ecosystem, Korean financial/blockchain security vendors.

### India

- `Watch` IISc, IIT Madras, IIT Bombay, IIT Delhi, IIT Kanpur, IIT Kharagpur, IIIT Hyderabad, C-DAC, DRDO/CAIR, CERT-In-linked academic programs. Track for software security, AI security, secure code generation, and national cyber ranges; direct human-factors LLM-security work was not prominent in the current pass.
- `Companies/sectors` TCS, Infosys, Wipro, HCLTech, Tech Mahindra, Zoho, Razorpay/financial security teams, and Indian SOC/MSSP vendors adopting LLM-assisted triage.

### Israel

- `Watch` Tel Aviv University, Technion, Hebrew University, Ben-Gurion University of the Negev, Reichman University. Track for AI security, web/app security, human-centered security, and cyber operations.
- `Companies/sectors` Check Point, CyberArk, Wiz, Cato Networks, Checkmarx, Snyk Israel ecosystem, Orca Security, SentinelOne Israel R&D, Microsoft/Google/IBM Israeli security labs.

### United Arab Emirates And Gulf

- `Watch` NYU Abu Dhabi, MBZUAI, Khalifa University, UAE Cyber Security Council-linked research, Qatar Computing Research Institute, KAUST in Saudi Arabia. Direct human-factors LLM-security evidence is sparse, but AI/security investment and cyber-range activity make the region worth monitoring.
- `Companies/sectors` G42, Core42, Presight, DarkMatter legacy ecosystem, regional sovereign-cloud and critical-infrastructure SOC operators.

### New Zealand

- `Watch` Massey University, University of Auckland, University of Waikato, Victoria University of Wellington, CERT NZ / NCSC NZ ecosystem. Watch for human-AI SOC, digital-risk protection, and Five Eyes agentic-AI adoption guidance.

## Practical Research Questions For The Human-Factors Layer

- Which security tasks benefit from LLM collaboration, and which tasks should remain human-authoritative?
- What UI patterns reduce over-trust without creating approval fatigue?
- How should AI coding assistants present uncertainty, provenance, dependency authenticity, data-use policy, and security caveats to developers?
- How should SOC copilots preserve analyst situation awareness and skill development instead of hiding the reasoning path?
- What is the right evidence handoff from AI vulnerability agents to maintainers, bounty triagers, vendors, and disclosure coordinators?
- How can reverse-engineering assistants expose enough intermediate reasoning for analysts to detect hallucinated symbols, types, comments, or control-flow summaries?
- How should organizations train developers, SOC analysts, reverse engineers, and red teamers to challenge LLM output instead of merely consuming it?
- What metrics capture human-AI complementarity: speed, accuracy, evidence quality, exploitability validation, skill transfer, cognitive load, false-positive burden, safe escalation, and auditability?
- For USA-China comparison, which differences come from model capability, which from developer/SOC culture, which from platform design, and which from governance?
