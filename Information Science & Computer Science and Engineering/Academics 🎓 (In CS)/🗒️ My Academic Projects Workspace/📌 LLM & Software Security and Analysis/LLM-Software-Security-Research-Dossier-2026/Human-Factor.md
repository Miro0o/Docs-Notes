---
ai-generated: true
---

# Human Factor: LLMs For Software Security And Analysis

Date: 2026-06-06

Home: [LLM-Software-Security-Research-Dossier-2026.md](LLM-Software-Security-Research-Dossier-2026.md)

This file covers the socio-technical layer of LLMs for software security and analysis: developer behavior, SOC analyst collaboration, reverse-engineering assistance, red-team labor, bug-bounty and maintainer workflows, oversight, approval burden, trust calibration, and the research ecosystem around human-facing security systems.

## Main Focus: United States And China As Of 2026-06-06

The United States and China should be treated as the primary country pair for this dossier.

- The United States has the densest direct evidence for human factors: controlled secure-coding user studies, human-LLM reverse-engineering experiments, SOC fieldwork, HCI work on LLM red teaming, agent-approval research, AIxCC-style cyber reasoning systems, bug-bounty telemetry, and large security-product deployments.
- China has the densest non-U.S. ecosystem around Chinese-language cybersecurity benchmarks, model-safety contests, public generative-AI security regulation, code/agent platforms, and security vendors. Direct published human-subject work on LLM + software security is thinner than in the United States, so China should be mapped as a mixed evidence base: benchmark/contest/platform/guidance evidence plus a watchlist of labs and companies likely to produce human-facing studies.
- For both countries, the practical unit of analysis is not just the model. It is the human plus model plus scaffold plus tool permissions plus UI plus audit logs plus validation harness plus organizational governance.

### Confidence Labels Used Below

- `Core`: direct LLM + security + human/organizational evidence, or an official source that directly shapes human-facing deployment.
- `Strong adjacent`: active in LLM/software/security or AI security with clear human-factor relevance, but not always a human-subject study.
- `Watch`: important ecosystem actor whose public record is relevant but where direct human-factors evidence needs follow-up before citation in a paper.

## Core Human-Factors Threads

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

The U.S. record should be the main direct-human-evidence record. It contains controlled user studies, practitioner-centered SOC work, analyst-facing reverse-engineering studies, AI red-team labor studies, agent security governance, AIxCC/OSS-CRS systems, bug-bounty workflow changes, and commercial SOC/developer-tool deployments.

### USA: Universities, Labs, And Research Groups

Each entry is separated by institution and group. Cross-institution papers are decomposed by the role each group plays in the human-factor layer.

#### Stanford University

##### Computer Security / Applied Cryptography Ecosystem

- `Label`: `Core`
- `People`: Neil Perry, Megha Srivastava, Deepak Kumar, Dan Boneh.
- `Focused area`: AI-assisted secure coding, user interaction with code assistants, trust and overconfidence in generated code.
- `Specific analysis`: Stanford's contribution is the clearest U.S. baseline for developer over-trust. The study is valuable because it measures not just vulnerability outcomes, but the human belief state after using an assistant: participants with AI access could be more confident that their code was secure even when it was less secure. For this dossier, Stanford should anchor any section on trust calibration, AI-assisted secure-code training, and whether warnings or prompting affordances can make developers more skeptical without destroying productivity.
- `Sources`: https://arxiv.org/abs/2211.03622 ; https://par.nsf.gov/biblio/10472129-do-users-write-more-insecure-code-ai-assistants.

#### New York University / NYU Tandon

##### Center for Cybersecurity

- `Label`: `Core`
- `People`: Gustavo Sandoval, Hammond Pearce, Teo Nys, Ramesh Karri, Siddharth Garg, Brendan Dolan-Gavitt.
- `Focused area`: LLM code-assistant security in low-level C tasks, security-critical bugs, code-assistant impact under controlled programming conditions.
- `Specific analysis`: NYU's `Lost at C` line should be treated as a methodological counterweight to Stanford rather than as a contradiction. It shows that the measured security harm of AI assistance depends on language, task, participant population, interface, and bug class. This makes NYU important for designing future human studies: a secure-coding experiment should vary task domain, programming language, developer skill, and whether the assistant is autocomplete-like, chat-like, or agentic.
- `Sources`: https://arxiv.org/abs/2208.09727 ; https://zenodo.org/record/7187358.

#### Arizona State University

##### SEFCOM

- `Label`: `Core`
- `People`: Adam Doupe, Yan Shoshitaishvili, Ruoyu Wang, Tiffany Bao, Zion Leonahenahe Basque, Ananta Soneji, Wil Gibbs and collaborators.
- `Focused area`: human-LLM software reverse engineering, binary analysis, vulnerability education, CTF-style security reasoning.
- `Specific analysis`: ASU SEFCOM is the strongest U.S. node for the analyst-facing reverse-engineering human-factor question: when does an LLM help a human understand binaries, and when does it create false confidence? The NDSS 2026 human-LLM SRE study matters because it examines instrumented analyst work rather than only benchmark accuracy. For this dossier, ASU should be tracked for novice/expert gap reduction, hallucinated function explanations, decompiler-comment trust, and how LLM assistance changes reverse-engineering strategy.
- `Sources`: https://www.eurecom.fr/en/publication/8548 ; https://adamdoupe.com/publications/ ; https://sefcom.asu.edu/people.html.

##### pwn.college

- `Label`: `Core`
- `People`: Yan Shoshitaishvili and the pwn.college education ecosystem.
- `Focused area`: applied cybersecurity education, CTF training, hands-on exploit and reverse-engineering learning.
- `Specific analysis`: pwn.college should be separated from SEFCOM's research output because its human-factor role is training and skill formation. It is relevant to LLM security because coding and reverse-engineering assistants can either accelerate learning or create shortcut dependency. A useful research question for this group is whether LLM tutors preserve the learner's mental model of exploitation, memory corruption, and debugging, or whether they merely produce answers that pass challenge checks.
- `Sources`: https://news.asu.edu/20240319-science-and-technology-next-generation-cybersecurity-pros-drill-dojo ; https://sefcom.asu.edu/publications/sensai-sigcse25.pdf.

#### University of California, Santa Barbara

##### Shellphish

- `Label`: `Core/strong adjacent`
- `People`: Shellphish members and collaborators; track teams connected to AIxCC and CTF research.
- `Focused area`: CTF competition, automated vulnerability discovery, cyber reasoning systems, exploit education.
- `Specific analysis`: Shellphish is important because it represents the bridge between human competitive security culture and automated cyber reasoning systems. For human factors, its relevance is not only model performance. It is how expert teams encode tacit CTF and vulnerability-discovery knowledge into scaffolds, prompts, fuzzing loops, and triage pipelines. This makes Shellphish a useful case for studying how human expertise becomes automation design.
- `Sources`: https://www.darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33 ; https://www.darpa.mil/news/2024/ai-cyber-challenge-cybersecurity.

#### UCLA

##### Security Lab

- `Label`: `Core`
- `People`: Yuan Tian, Peiran Wang, Ying Li.
- `Focused area`: LLM-agent security, agent-human interaction, runtime approval, scope configuration, policy specification, authorization/provenance.
- `Specific analysis`: UCLA's key contribution is to move agent security away from a purely model-centric framing. Their work identifies the production mechanisms that humans actually see: policy setup, runtime approvals, and scope controls. This is central for coding agents and SOC agents because the user often approves a natural-language summary of a tool action rather than the raw action itself. Track this group for research on approval fatigue, action provenance, agent permission granularity, and usable authorization.
- `Sources`: https://arxiv.org/abs/2605.24309 ; https://arxiv.org/abs/2605.26497 ; https://ucla-sec-lab.netlify.app/.

#### William & Mary

##### HAT-Lab / Agent-Mediated Deception Line

- `Label`: `Core`
- `People`: Xinfeng Li and collaborators including Shenyu Dai, Kelong Zheng, Yue Xiao, Gelei Deng, Wei Dong, Xiaofeng Wang.
- `Focused area`: human perception vulnerability in LLM-driven agentic systems, agent-mediated deception, trusted-agent attacks.
- `Specific analysis`: This group should be tracked for the failure mode where the agent itself becomes the social-engineering interface. Its relevance to software security is direct: developers, SOC analysts, and enterprise users increasingly delegate tool use to agents that can summarize, recommend, and act. If a compromised or manipulated agent can lower attack perception, then runtime approval alone is weak unless the approval UI exposes verifiable action details and adversarial context.
- `Sources`: https://arxiv.org/abs/2602.21127.

#### University of South Florida

##### SOC Sociotechnical Fieldwork

- `Label`: `Core`
- `People`: Daniel Lende, Xinming Ou, Francis Hahn, Mohd Mamoon and collaborators.
- `Focused area`: practitioner-centered SOC adoption, anthropological and sociotechnical methods, workflow-aware LLM introduction.
- `Specific analysis`: USF's role is the social-science and SOC-practice lens. It matters because SOCs are high-pressure workplaces with tacit routines, interruptions, and communication norms that are invisible in offline benchmarks. Track this group for methods: observation, co-design, practitioner interviews, and how AI tools are introduced without breaking existing incident-response tempo.
- `Sources`: https://www.isi.edu/results/publications/65207/a-sociotechnical-practitioner-centered-approach-to-technology-adoption-in-cybersecurity-operations-an-llm-case ; https://www.ndss-symposium.org/ndss-paper/auto-draft-741/.

#### University of Kansas

##### Cybersecurity Operations Collaboration

- `Label`: `Core`
- `People`: Alexandru G. Bardas, Jaclyn Lauren Dudek and collaborators.
- `Focused area`: SOC workflow adoption, security operations research, practitioner co-creation.
- `Specific analysis`: Kansas should be tracked as a separate SOC-operations partner rather than merged into the USF line. Its value is the engineering/security-operations side of the same fieldwork: which SOC tasks are appropriate for LLM companions, how analysts validate generated explanations, and what kinds of generated guidance are disruptive versus operationally useful.
- `Sources`: https://www.ndss-symposium.org/ndss-paper/auto-draft-741/.

#### USC Information Sciences Institute

##### Security Operations And Applied AI

- `Label`: `Core`
- `People`: Michael Collins and collaborators.
- `Focused area`: applied cybersecurity operations, LLM adoption in SOC settings, practitioner-centered deployment.
- `Specific analysis`: USC ISI is important because it connects academic sociotechnical research with operational security systems. For the dossier, track ISI for evidence about how LLM tools are evaluated in realistic SOC environments, especially how generated summaries, correlations, and recommendations are checked by analysts before action.
- `Sources`: https://www.isi.edu/results/publications/65207/a-sociotechnical-practitioner-centered-approach-to-technology-adoption-in-cybersecurity-operations-an-llm-case.

#### University of Central Florida

##### SEAL Lab

- `Label`: `Core`
- `People`: David Mohaisen, Mohammed Kharma, Ahmed Sabbah, Mohammad Alkhanafseh and collaborators.
- `Focused area`: secure LLM-generated code, developer security training, trustworthy AI and software security.
- `Specific analysis`: UCF SEAL is important because it moves from observing insecure AI-assisted code to testing an intervention: security training for LLM-assisted development. This makes it useful for dissertation or paper design. The key question is whether trained developers use different prompts, inspect different code regions, ask for security constraints more often, or reject insecure model outputs more reliably.
- `Sources`: https://seal.cs.ucf.edu/ ; https://arxiv.org/abs/2604.17763.

#### IBM Research

##### Responsible AI / Red-Team Data Practices

- `Label`: `Core`
- `People`: Adriana Alvarado Garcia, Ruyuan Wan, Ozioma Collins Oguine, Karla Badillo-Urquiola and IBM-affiliated collaborators.
- `Focused area`: AI red-team data practices, socio-technical evaluation, responsible AI, dataset creation and review.
- `Specific analysis`: IBM Research should be tracked for the labor side of AI red teaming. Its value is showing that red-team datasets are not neutral technical artifacts: they encode practitioner assumptions about risk, context, user type, and interaction format. For software security, the same issue appears when cyber benchmarks flatten real triage work into attack success rates.
- `Sources`: https://research.ibm.com/publications/red-teaming-llms-as-socio-technical-practice-from-exploration-and-data-creation-to-evaluation ; https://doi.org/10.1145/3772318.3790792.

#### University of Notre Dame

##### Karla Badillo-Urquiola / Responsible AI And HCI

- `Label`: `Core`
- `People`: Karla Badillo-Urquiola and collaborators.
- `Focused area`: responsible AI, socio-technical red teaming, human-centered evaluation.
- `Specific analysis`: Notre Dame's role in the red-team data-practices line should be kept separate from IBM because it grounds the work in HCI and human-centered research. For this dossier, the Notre Dame contribution helps explain how red-team artifacts should account for vulnerable users, interaction context, and situated harms rather than only prompt strings and model outputs.
- `Sources`: https://doi.org/10.1145/3772318.3790792.

##### Toby Jia-Jun Li / GUI Agent Oversight

- `Label`: `Core`
- `People`: Toby Jia-Jun Li, Jingyu Tang, Chaoran Chen and collaborators.
- `Focused area`: GUI agents, dark patterns, human oversight, human-agent teamwork.
- `Specific analysis`: This Notre Dame line is separate from the red-team line. It matters for software security because many agentic workflows are GUI-bound: browser agents approve purchases, access dashboards, read tickets, and trigger actions. The specific human-factor issue is whether a human overseer can notice manipulative UI or prompt-injected instructions while also supervising an agent's task progress.
- `Sources`: https://arxiv.org/abs/2509.10723 ; https://doi.org/10.1145/3772318.3791568.

#### Pennsylvania State University

##### Red-Team Evaluation Collaboration

- `Label`: `Core/strong adjacent`
- `People`: Track Penn State collaborators in the CHI 2026 red-team practice line.
- `Focused area`: practitioner interviews, responsible-AI evaluation, socio-technical red-team standards.
- `Specific analysis`: Penn State should be tracked as a separate contributor to the red-team practice line because distributed authorship indicates this topic is not confined to model providers. The useful angle is how academic HCI researchers can audit the way industry constructs red-team datasets and evaluation taxonomies.
- `Sources`: https://doi.org/10.1145/3772318.3790792.

#### University of Michigan

##### Human-AI Interaction And GUI-Agent Collaboration

- `Label`: `Core`
- `People`: Jiawen Li, Dakuo Wang, Tianshi Li and collaborators in the dark-pattern GUI-agent line.
- `Focused area`: human-AI collaboration, oversight cost, interface-mediated manipulation.
- `Specific analysis`: Michigan's relevance is the human-AI teamwork portion of GUI-agent security. In software-security settings, analysts and developers rarely supervise a single clean model response; they supervise a sequence of interface actions. Track this group for measures of cognitive load, attentional tunneling, and how oversight changes when the human must monitor both a task goal and a security boundary.
- `Sources`: https://arxiv.org/abs/2509.10723 ; https://cse.engin.umich.edu/stories/u-m-presents-62-papers-at-chi-2026-19-by-cse.

#### Northeastern University

##### Khoury College / GUI-Agent Dark Patterns

- `Label`: `Core`
- `People`: Zhiping Zhang and collaborators.
- `Focused area`: GUI-agent susceptibility to manipulative interfaces, HCI/security failure modes.
- `Specific analysis`: Northeastern is useful because its public coverage frames dark patterns as a risk that now affects both humans and agents. For software security, this supports a broader point: agent security cannot be separated from UI security. A coding or SOC agent may correctly reason over text but still fail when the interface hides risk in layout, fine print, or misleading controls.
- `Sources`: https://www.khoury.northeastern.edu/dark-patterns-have-long-manipulated-human-behavior-online-now-ai-agents-are-falling-for-them-too/ ; https://doi.org/10.1145/3772318.3791568.

#### Johns Hopkins University

##### HCI / Agent Oversight Collaboration

- `Label`: `Core/strong adjacent`
- `People`: Ziang Xiao, Yaxing Yao and collaborators.
- `Focused area`: GUI agents, human oversight, transparency and accountability in human-agent systems.
- `Specific analysis`: Johns Hopkins should be separated because the dark-pattern study includes authors focused on human-centered AI and accountability. Its relevance is in designing oversight interfaces that do not make the human approve an agent's own unverifiable summary. Track for future work on transparency, redress, and accountability in delegated agent actions.
- `Sources`: https://doi.org/10.1145/3772318.3791568.

#### UC Berkeley

##### CHAI / Human-Compatible AI

- `Label`: `Core`
- `People`: Jonathan Stray and collaborators.
- `Focused area`: grounded theory of LLM red teaming, human motivations and strategies, AI safety practice.
- `Specific analysis`: UC Berkeley CHAI is important for conceptual framing. It helps translate red teaming from a cybersecurity metaphor into an empirical human practice: people choose targets, invent tactics, share examples, seek status, and define what "bad" means. For software-security research, this suggests cyber red-team benchmarks should document human strategy and motivation, not only attack success.
- `Sources`: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0314658.

#### University of Washington

##### Red-Team And Human-AI Collaboration Line

- `Label`: `Core/strong adjacent`
- `People`: Track University of Washington collaborators in LLM red-team and human-AI collaboration work.
- `Focused area`: human-AI collaboration, AI red-team practice, sociotechnical evaluation.
- `Specific analysis`: UW's role should not be hidden inside the Berkeley/NVIDIA/Denmark collaboration. It is a strong place to watch for methods that combine HCI, social computing, and security practice. For the dossier, UW is relevant to how red-team results are collected, interpreted, and converted into safety policy.
- `Sources`: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0314658.

##### Tech Policy Lab / AI Agent Permissions

- `Label`: `Strong adjacent`
- `People`: Track UW Tech Policy Lab and AI-agent permission authors.
- `Focused area`: data-access permissions, user approval, under-permissioning and over-permissioning in AI agents.
- `Specific analysis`: This is highly relevant to software security because coding agents and SOC agents request access to repositories, files, logs, tickets, email, cloud dashboards, and command execution. The human-factor question is how users specify permission boundaries before they know what the agent will need. Track this work for permission automation, delegation UI, and safe defaults.
- `Sources`: https://techpolicylab.uw.edu/wp-content/uploads/2026/02/2511.17959v1.pdf.

#### Carnegie Mellon University

##### Software Engineering Institute

- `Label`: `Strong adjacent`
- `People`: SEI AI Engineering and security researchers.
- `Focused area`: LLM-agent security SoK, secure AI engineering, bridge from academic papers to operational controls.
- `Specific analysis`: SEI is important for translating agent-security research into practitioner categories. Its value for human factors is taxonomy and governance: what controls are deployable, who is responsible for them, and how a security engineer should reason about LLM agents as software systems with users, permissions, logs, and failure modes.
- `Sources`: https://www.sei.cmu.edu/library/bridging-research-and-practice-in-llm-agent-security/.

#### Georgia Tech

##### Team Atlanta / AIxCC

- `Label`: `Core/strong adjacent`
- `People`: Taesoo Kim and Team Atlanta collaborators.
- `Focused area`: AIxCC cyber reasoning systems, automated vulnerability discovery and patching.
- `Specific analysis`: Georgia Tech's Team Atlanta work is relevant because it turns expert vulnerability-discovery practice into a CRS pipeline. The human factor is downstream: maintainers and triagers need evidence, not just model claims. Track this group for how CRS outputs are packaged into proof, patches, confidence, and disclosure-ready artifacts.
- `Sources`: https://www.darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33 ; https://www.darpa.mil/news/podcast/aixcc-challenge-89.

#### Purdue University

##### AIxCC / Cyber Reasoning Watch

- `Label`: `Watch`
- `People`: Track Purdue security and software-engineering researchers connected to CRS, fuzzing, and program analysis.
- `Focused area`: cyber reasoning systems, software security, program analysis, automated patch validation.
- `Specific analysis`: Purdue should be tracked as a separate watch institution rather than folded into a broad AIxCC ecosystem. The likely human-factor angle is patch trust: when automated systems produce candidate fixes, human reviewers need tests, traces, minimized reproductions, and clear root-cause explanations.

#### MIT

##### CSAIL - AI/Software/Security Watch

- `Label`: `Watch`
- `People`: Track CSAIL researchers in AI agents, program analysis, software engineering, and security.
- `Focused area`: agentic software engineering, program synthesis, verification, security evaluation.
- `Specific analysis`: MIT is a high-probability source of future work on verification-backed coding agents. The human-factor angle to watch is whether formal or test-grounded evidence can reduce reviewer burden when agents produce large patches.

#### UC San Diego

##### Systems And Security Watch

- `Label`: `Watch`
- `People`: Track UCSD systems, security, and HCI/security researchers.
- `Focused area`: systems security, usable security, program analysis, AI for security.
- `Specific analysis`: UCSD is relevant as a likely source of empirical security-tool studies. The specific angle to watch is how LLM explanations affect expert trust in low-level systems security tasks.

#### University of Chicago

##### Security, Policy, And Human Factors Watch

- `Label`: `Watch`
- `People`: Track security, policy, and human-centered AI researchers.
- `Focused area`: privacy/security, AI governance, human behavior in security systems.
- `Specific analysis`: Chicago is relevant for policy and human behavior around security tools. The useful future direction is measuring how organizational policy changes developer use of AI coding tools and shadow AI.

#### University of Illinois Urbana-Champaign

##### Security And Software Engineering Watch

- `Label`: `Watch`
- `People`: Track UIUC security, software engineering, and ML researchers.
- `Focused area`: software security, formal methods, AI-assisted development, trustworthy AI.
- `Specific analysis`: UIUC is a strong watch node for tool-backed code analysis. The human-factor angle is how developers respond when LLM output is paired with formal or static-analysis evidence.

#### Princeton University

##### CITP - Policy And Socio-Technical Security Watch

- `Label`: `Watch`
- `People`: Track CITP researchers working on AI governance, privacy, security, and platform accountability.
- `Focused area`: AI governance, platform policy, security and privacy.
- `Specific analysis`: Princeton CITP matters for the regulatory and social layer of AI coding/security tools. Track for work on accountability when AI-generated code or AI-generated vulnerability reports cause downstream harm.

#### Cornell Tech

##### AI, Security, And Usable Systems Watch

- `Label`: `Watch`
- `People`: Track Cornell Tech security, privacy, and human-centered computing researchers.
- `Focused area`: usable security, AI systems, privacy, developer tools.
- `Specific analysis`: Cornell Tech is a likely source for studies of real developer workflows and AI-assisted engineering. The human-factor angle is enterprise adoption: what security controls developers will actually tolerate.

#### University of Maryland

##### HCIL / Usable Security Watch

- `Label`: `Watch`
- `People`: Track HCIL and usable-security researchers.
- `Focused area`: human-computer interaction, usable privacy and security, security warnings.
- `Specific analysis`: Maryland HCIL is relevant because AI-agent approval prompts are a new kind of security warning. The research question is whether established warning-design lessons transfer to dynamic, model-generated, multi-step agent actions.

### USA: Companies, Platforms, Standards Bodies, And Independent Ecosystems

#### OpenAI

##### Cybersecurity Grant Program / Security / Codex-Oriented Tooling

- `Label`: `Core`
- `Units`: Security, Preparedness, Cybersecurity Grant Program, Codex/security tooling teams.
- `Focused area`: defensive cyber agents, secure code assistance, model safeguards, grant-funded cyber research.
- `Specific analysis`: OpenAI's human-factor relevance is access design. Cyber-capable models and coding agents require a boundary between legitimate defensive work and misuse. Track OpenAI for trusted-access models, evidence handoff in code security tools, model behavior around vulnerability requests, and how product UI keeps humans responsible for patches and disclosures.
- `Sources`: https://openai.com/index/openai-cybersecurity-grant-program/ ; https://openai.com/index/empowering-defenders-through-our-cybersecurity-grant-program/ ; https://openai.com/index/security-on-the-path-to-agi/.

#### Anthropic

##### Project Glasswing / Frontier Red Team

- `Label`: `Core`
- `Units`: Frontier Red Team, Project Glasswing, Cyber Verification Program.
- `Focused area`: restricted cyber-capable model access, AI-assisted vulnerability discovery, coordinated disclosure.
- `Specific analysis`: Anthropic's key human-factor issue is that discovery can outpace validation and patching. Project Glasswing should be read as a human workflow problem: who receives findings, who verifies them, who prioritizes patches, and how maintainers avoid being overwhelmed by AI-generated vulnerability volume.
- `Sources`: https://www.anthropic.com/glasswing ; https://www.anthropic.com/research/glasswing-initial-update ; https://www.anthropic.com/news/expanding-project-glasswing.

#### Google

##### Google DeepMind - CodeMender

- `Label`: `Core`
- `Units`: Google DeepMind security/code-agent teams.
- `Focused area`: AI-assisted patch generation, static/dynamic analysis, fuzzing, SMT-style reasoning, critique agents.
- `Specific analysis`: CodeMender is important because it foregrounds patch validation and expert review. The human factor is not whether an AI can write a patch, but whether the patch comes with enough evidence that a maintainer can trust it without repeating the whole investigation.
- `Sources`: https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/.

##### Google Project Zero - Big Sleep

- `Label`: `Core`
- `Units`: Project Zero, Big Sleep collaboration.
- `Focused area`: AI-assisted vulnerability discovery in real software.
- `Specific analysis`: Project Zero's role is credibility and disclosure discipline. Big Sleep should be tracked for how AI findings are converted into high-quality vulnerability reports, how human researchers verify exploitability, and how disclosure norms change when discovery volume increases.
- `Sources`: https://projectzero.google/2024/10/from-naptime-to-big-sleep.html.

##### Google Mandiant / GTIG

- `Label`: `Core/strong adjacent`
- `Units`: Google Threat Intelligence Group, Mandiant.
- `Focused area`: threat intelligence on AI misuse, SOC and incident-response context.
- `Specific analysis`: GTIG/Mandiant matters because it observes attacker and defender behavior in the field. The human-factor angle is how analysts interpret AI-enabled threat activity, distinguish model-assisted work from ordinary automation, and avoid over-attributing capability based on vendor claims.
- `Sources`: https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai ; https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools/.

#### Microsoft

##### Security Copilot

- `Label`: `Core`
- `Units`: Microsoft Security Copilot, Defender, Sentinel, Entra, Purview integrations.
- `Focused area`: SOC copilot workflows, guided response, investigation summarization, security automation.
- `Specific analysis`: Microsoft Security Copilot is important because it operationalizes LLM assistance for named security personas: SOC analysts, compliance analysts, IT admins, data security admins, identity admins, and CISOs. Track how its workflow design preserves analyst authority, shows evidence, handles uncertainty, and prevents generated recommendations from becoming unreviewed action.
- `Sources`: https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot ; https://learn.microsoft.com/en-us/security-copilot/workflows-overview.

##### GitHub - Copilot / Advanced Security / CodeQL Ecosystem

- `Label`: `Core`
- `Units`: GitHub Copilot, Copilot code review, Advanced Security, CodeQL.
- `Focused area`: AI coding assistance, code review, SAST explanations, repository security.
- `Specific analysis`: GitHub is the central developer-workflow platform for studying AI-assisted secure coding at scale. The key human-factor issues are suggestion acceptance, code-review dilution, attribution, generated issue/PR burden, and whether security explanations make developers better reviewers or merely faster acceptors.
- `Sources`: https://arxiv.org/abs/2211.03622 ; https://arxiv.org/abs/2208.09727.

#### HackerOne

##### Hackbots / Agentic Validation

- `Label`: `Core`
- `Units`: HackerOne platform, Hai, hackbots, agentic validation, researcher programs.
- `Focused area`: AI-assisted vulnerability reports, autonomous bug finding, triage, validation.
- `Specific analysis`: HackerOne is the best U.S. platform signal for how AI changes vulnerability-report labor. It exposes the triager burden problem: AI can increase report volume, but humans still need validity, impact, reproduction, scope compliance, and remediation clarity. Track agentic validation as a human-review support system, not as a replacement for bounty triage.
- `Sources`: https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy ; https://www.hackerone.com/blog/2025-hpsr-researcher-signals ; https://docs.hackerone.com/en/articles/13603896-agentic-validation.

#### DARPA

##### AI Cyber Challenge

- `Label`: `Core`
- `Units`: AIxCC, DARPA Information Innovation Office, ARPA-H collaboration.
- `Focused area`: cyber reasoning systems, automated vulnerability discovery and patching.
- `Specific analysis`: DARPA's AIxCC should be treated as an experiment in automating expert security labor. The human-factor bottleneck is after the CRS runs: maintainers need credible reports, safe patches, and accountability. Track scoring rules, disclosure rules, and how CRS teams explain their outputs to humans.
- `Sources`: https://www.darpa.mil/research/programs/ai-cyber ; https://www.darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33.

#### OpenSSF / Linux Foundation

##### OSS-CRS

- `Label`: `Core`
- `Units`: OSS-CRS, OpenSSF, OSS-Fuzz-compatible CRS campaigns, maintainer-facing security infrastructure.
- `Focused area`: post-AIxCC open-source CRS infrastructure, verified issue submission, automated patching.
- `Specific analysis`: OpenSSF is the maintainer-facing side of the CRS story. Its human-factor importance is evidence hygiene: automated systems must produce findings that maintainers can reproduce, prioritize, and patch without being flooded by false positives or opaque claims.
- `Sources`: https://openssf.org/tag/cyber-reasoning-systems/ ; https://oss-crs.openssf.org/docs/crs-development-guide.

#### NIST

##### CAISI - AI Agent Security And Evaluation

- `Label`: `Core`
- `Units`: Center for AI Standards and Innovation, NCCoE, agent security RFI.
- `Focused area`: AI-agent standards, evaluations, identity, authorization, security measurement.
- `Specific analysis`: CAISI is central to the governance side of human factors. It asks what secure agent deployment means when an agent can act without constant human oversight. Track CAISI for definitions of human authorization, agent identity, behavioral transparency, audit logs, and reproducible evaluation.
- `Sources`: https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems ; https://www.nist.gov/caisi.

#### CISA

##### Secure Deployment And Critical Infrastructure Guidance

- `Label`: `Strong adjacent`
- `Units`: CISA secure-by-design and critical-infrastructure security programs.
- `Focused area`: operational guidance, critical-infrastructure adoption, incident reporting.
- `Specific analysis`: CISA matters because it shapes organizational adoption norms. For LLM security tools, the human-factor question is how agencies and critical-infrastructure operators define acceptable human oversight, escalation, logging, and procurement requirements.

#### MITRE

##### ATT&CK / ATLAS

- `Label`: `Strong adjacent`
- `Units`: MITRE ATT&CK, MITRE ATLAS, cyber evaluation programs.
- `Focused area`: adversary behavior taxonomies, AI threat modeling, security evaluation.
- `Specific analysis`: MITRE is relevant because SOC analysts and tool vendors need shared language for AI-enabled threats. Track whether ATLAS/ATT&CK-style taxonomies help humans classify AI-agent attacks or whether new categories are needed for prompt injection, tool misuse, and agent-mediated deception.

#### CrowdStrike

##### XDR / Threat Intelligence

- `Label`: `Strong adjacent`
- `Units`: CrowdStrike Falcon, XDR, threat intelligence and AI security research.
- `Focused area`: SOC automation, threat detection, AI-assisted analyst workflows.
- `Specific analysis`: CrowdStrike should be tracked for field evidence about how analysts use AI summaries during incident response. The human-factor issue is whether AI speeds triage while preserving analyst skepticism about attribution, severity, and recommended containment.

#### Palo Alto Networks

##### Cortex / Unit 42

- `Label`: `Strong adjacent`
- `Units`: Cortex, Unit 42, cloud and SOC automation products.
- `Focused area`: SOC automation, threat intelligence, AI-assisted detection and response.
- `Specific analysis`: Palo Alto is relevant because it combines SOC tooling with threat intelligence. Track how its AI features present evidence chains and whether analysts can inspect the basis for generated conclusions before response actions.

#### SentinelOne

##### Purple AI / Endpoint Security

- `Label`: `Strong adjacent`
- `Units`: SentinelOne endpoint and AI analyst tooling.
- `Focused area`: endpoint telemetry, AI-assisted investigation, autonomous response.
- `Specific analysis`: SentinelOne is a watch point for the boundary between recommendation and automated response. Human factors include when analysts are asked to approve containment, how the system communicates uncertainty, and whether automation hides causal evidence.

#### Splunk / Cisco

##### Security Operations Analytics

- `Label`: `Strong adjacent`
- `Units`: Splunk Enterprise Security, Cisco security integrations.
- `Focused area`: log analytics, SOC dashboards, investigation workflows.
- `Specific analysis`: Splunk/Cisco matters because LLM copilots often sit on top of log-search and dashboard workflows. The human-factor question is whether natural-language interfaces improve analyst search or obscure the exact query logic and data filters used.

#### Elastic

##### Elastic Security

- `Label`: `Strong adjacent`
- `Units`: Elastic Security, search and SIEM tooling.
- `Focused area`: log search, endpoint/security analytics, analyst investigation.
- `Specific analysis`: Elastic is relevant for evidence traceability. If LLM assistance generates queries or summarizes telemetry, analysts need visibility into the underlying search, time windows, indices, and assumptions.

#### Rapid7

##### Vulnerability Management / Detection Products

- `Label`: `Strong adjacent`
- `Units`: Insight platform, vulnerability management and detection products.
- `Focused area`: vulnerability prioritization, exposure management, SOC workflows.
- `Specific analysis`: Rapid7 is a useful watch point for human prioritization. LLMs may summarize vulnerabilities and remediation plans, but humans still need business context, asset criticality, exploitability, and compensating controls.

#### Tenable

##### Exposure Management

- `Label`: `Strong adjacent`
- `Units`: exposure management and vulnerability scanning products.
- `Focused area`: vulnerability management, prioritization, AI risk posture.
- `Specific analysis`: Tenable matters because vulnerability management is already a human overload problem. LLM features can help explain findings, but they can also create false confidence if generated remediation steps are not tied to asset-specific evidence.

#### Wiz

##### Cloud Security / Exposure Management

- `Label`: `Strong adjacent`
- `Units`: cloud security and exposure management products.
- `Focused area`: cloud risk, attack path analysis, prioritization.
- `Specific analysis`: Wiz is relevant for cloud-security human factors: AI can generate attack-path explanations, but human cloud teams need to verify ownership, blast radius, and remediation feasibility across accounts and teams.

#### Snyk

##### Developer Security Platform

- `Label`: `Strong adjacent`
- `Units`: developer security, dependency and code scanning products.
- `Focused area`: AppSec, dependency risk, developer remediation.
- `Specific analysis`: Snyk should be tracked for developer-facing remediation UX. The core human-factor issue is whether generated fixes educate developers about root cause or encourage shallow dependency/code changes that pass a scanner without reducing risk.

#### Semgrep

##### Code Scanning / AppSec Workflows

- `Label`: `Strong adjacent`
- `Units`: Semgrep code scanning and AppSec workflows.
- `Focused area`: SAST, rule-based detection, code review, developer education.
- `Specific analysis`: Semgrep is useful because it already centers human-readable rules. LLM integration should be judged by whether it improves rule authoring and triage explanations without making developers trust unverified natural-language vulnerability claims.

#### Checkmarx

##### AppSec Platform

- `Label`: `Strong adjacent`
- `Units`: AppSec platform, code/security scanning products.
- `Focused area`: secure code review, SAST, software supply chain security.
- `Specific analysis`: Checkmarx is relevant to enterprise AppSec review burden. Track how AI explanations affect developer acceptance of findings, security-team review time, and false-positive handling.

#### Veracode

##### Application Security Testing

- `Label`: `Strong adjacent`
- `Units`: application security testing and secure coding analytics.
- `Focused area`: code security measurement, secure-code education, enterprise AppSec.
- `Specific analysis`: Veracode is a useful source for longitudinal code-security telemetry. The human-factor angle is whether AI coding changes secure development maturity, training needs, and remediation patterns across organizations.

#### Trail of Bits

##### AIxCC / Buttercup CRS / Security Engineering

- `Label`: `Core/strong adjacent`
- `Units`: AIxCC team, Buttercup CRS, security engineering practice.
- `Focused area`: cyber reasoning systems, audits, exploitability validation.
- `Specific analysis`: Trail of Bits should be treated separately because it combines elite human audit practice with CRS automation. The relevant question is how expert audit judgment is embedded in tools and how CRS output is reviewed before disclosure or patch acceptance.
- `Sources`: https://www.darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33.

#### Theori

##### AIxCC / Offensive Security

- `Label`: `Core/strong adjacent`
- `Units`: AIxCC team, browser/blockchain/offensive security teams.
- `Focused area`: autonomous vulnerability discovery, CTF expertise, exploit validation.
- `Specific analysis`: Theori is a strong case for competition-grade offensive expertise entering CRS design. Track how their systems distinguish plausible bugs from exploitable bugs and how human experts validate generated exploit chains.
- `Sources`: https://www.darpa.mil/news/2025/ai-cyber-challenge-winners-def-con-33.

#### Kudu Dynamics

##### Cyber Research / Vulnerability Discovery

- `Label`: `Strong adjacent`
- `Units`: cyber research and vulnerability discovery teams.
- `Focused area`: advanced security research, fuzzing, exploit development, CRS-style automation.
- `Specific analysis`: Kudu Dynamics is relevant as an expert-security-labor organization. Track how AI changes internal analyst workflows, especially the division between automated search and human exploitability judgment.

#### ForAllSecure

##### Mayhem / Fuzzing / Automated Testing

- `Label`: `Strong adjacent`
- `Units`: Mayhem/fuzzing and automated testing ecosystem.
- `Focused area`: fuzzing, automated vulnerability discovery, test generation.
- `Specific analysis`: ForAllSecure matters because fuzzing is one of the concrete oracles that can ground LLM claims. Human factors include how developers interpret fuzzing-backed AI findings and how much evidence is enough to accept a generated patch.

#### Bishop Fox

##### Offensive Security / Attack-Surface Management

- `Label`: `Strong adjacent`
- `Units`: offensive security and attack-surface management teams.
- `Focused area`: pentesting, attack-surface management, AI-assisted validation.
- `Specific analysis`: Bishop Fox is a watch point for human-led pentesting augmented by AI. Track whether AI reduces reconnaissance time while keeping human testers responsible for scope, authorization, and exploit safety.

#### Cobalt

##### Pentest-As-A-Service Platform

- `Label`: `Strong adjacent`
- `Units`: pentest-as-a-service platform and researcher network.
- `Focused area`: human pentesting workflows, report generation, triage.
- `Specific analysis`: Cobalt is relevant to how AI changes report-writing and validation labor in managed pentest platforms. The risk is polished but weak reports; the opportunity is faster evidence collection and clearer remediation.

#### XBOW

##### Autonomous Pentesting / Vulnerability Discovery

- `Label`: `Strong adjacent`
- `Units`: autonomous pentesting / vulnerability discovery platform.
- `Focused area`: AI-driven bug finding, platform-based vulnerability research.
- `Specific analysis`: XBOW is important because it represents the "AI researcher" role entering public vulnerability platforms. Human factors include rules of engagement, researcher attribution, proof quality, and how platforms prevent automated low-quality submissions.

#### Bugcrowd

##### Bug-Bounty Platform / AI Benchmarking

- `Label`: `Strong adjacent`
- `Units`: bug-bounty platform, AI benchmarking and researcher ecosystem.
- `Focused area`: bounty triage, AI-assisted reports, exploitability benchmarks.
- `Specific analysis`: Bugcrowd should be tracked alongside HackerOne but separately. Its value is comparative platform policy: how different bounty platforms handle AI-generated reports, valid-report thresholds, and researcher incentives.

#### Anysphere

##### Cursor

- `Label`: `Strong adjacent`
- `Units`: Cursor AI IDE and coding-agent workflows.
- `Focused area`: repository-level coding agents, developer prompting, command execution.
- `Specific analysis`: Cursor is relevant because it shifts the assistant from autocomplete to agentic editing. Human factors include repository context trust, approval of terminal commands, generated dependency changes, and whether developers review large AI-authored diffs carefully.

#### Sourcegraph

##### Cody

- `Label`: `Strong adjacent`
- `Units`: Cody, code search, repository context systems.
- `Focused area`: repository-level code understanding, search, AI coding assistance.
- `Specific analysis`: Sourcegraph matters because context retrieval is a human-factor issue. Developers need to know which code the assistant actually used. Track provenance display, context selection, and whether AI answers cite relevant files accurately.

#### Replit

##### Replit Agent / Cloud Coding Environment

- `Label`: `Strong adjacent`
- `Units`: Replit Agent and cloud coding environment.
- `Focused area`: AI-assisted software creation, deployment, novice developers.
- `Specific analysis`: Replit is relevant to novice and nontraditional developers. The human-factor concern is that users may deploy working but insecure systems without understanding authentication, secrets, data handling, or dependency risk.

#### Codeium / Windsurf

##### Windsurf AI IDE

- `Label`: `Strong adjacent`
- `Units`: Windsurf IDE, Codeium assistant.
- `Focused area`: AI coding assistant, agentic development workflow.
- `Specific analysis`: Windsurf is a watch point for flow-based coding agents. Track how approval, review, and context visibility are designed when the assistant edits multiple files over multiple steps.

#### Tabnine

##### Enterprise AI Coding Assistant

- `Label`: `Strong adjacent`
- `Units`: enterprise AI coding assistant.
- `Focused area`: code completion, private deployment, enterprise controls.
- `Specific analysis`: Tabnine is relevant to enterprise security teams because local/private deployment claims can change trust and policy decisions. Human factors include whether developers assume private deployment also means generated code is secure.

#### JetBrains

##### JetBrains AI

- `Label`: `Strong adjacent`
- `Units`: JetBrains IDE AI features.
- `Focused area`: IDE-native AI assistance, refactoring, code explanation.
- `Specific analysis`: JetBrains AI matters because many professional developers live inside IDE affordances. Track how security warnings, inspections, and AI suggestions interact inside the same development environment.

#### SANS / GIAC

##### Cybersecurity Training And Certification

- `Label`: `Strong adjacent`
- `Units`: SANS courses, GIAC certifications.
- `Focused area`: cybersecurity training and certification.
- `Specific analysis`: SANS/GIAC is relevant to workforce readiness. The human-factor question is how curricula should teach analysts and developers to use LLMs without outsourcing judgment, especially in incident response and secure coding.

#### Security Journey

##### Developer Security Training

- `Label`: `Strong adjacent`
- `Units`: developer security training platform.
- `Focused area`: secure coding education, developer behavior change.
- `Specific analysis`: Security Journey is relevant for teaching prompt discipline and review habits to ordinary developers. Track whether training content evolves from generic secure coding to AI-assisted secure coding.

#### Secure Code Warrior

##### Developer Secure-Code Training

- `Label`: `Strong adjacent`
- `Units`: developer secure-code training and labs.
- `Focused area`: secure coding, developer upskilling, remediation practice.
- `Specific analysis`: Secure Code Warrior should be tracked for whether interactive training can prepare developers to spot insecure AI-generated code rather than only hand-written vulnerable snippets.

#### Immersive Labs

##### Cyber Workforce Training

- `Label`: `Strong adjacent`
- `Units`: cyber workforce training and crisis simulation.
- `Focused area`: cyber ranges, SOC readiness, incident response training.
- `Specific analysis`: Immersive Labs matters for analyst skill retention. LLM copilots may reduce routine workload, but training systems need to ensure analysts can still reason when the copilot is wrong or unavailable.

#### Hack The Box

##### CTF Platform / AI Red-Teaming CTF Activity

- `Label`: `Strong adjacent`
- `Units`: HTB Academy, CTF platform, AI red-teaming CTF activity.
- `Focused area`: CTF training, AI-enabled cyber skill development.
- `Specific analysis`: Hack The Box is relevant because CTF platforms are adapting to agentic AI. Track whether AI-assisted players learn transferable security reasoning or mainly optimize prompt/scaffold use.

#### TryHackMe

##### Cyber Learning Paths And Labs

- `Label`: `Strong adjacent`
- `Units`: cyber learning paths and labs.
- `Focused area`: entry-level and intermediate cyber training.
- `Specific analysis`: TryHackMe is a watch point for novice security learning with AI help. The human-factor issue is whether LLM hints improve learning or reduce the struggle needed to build durable mental models.

#### OWASP

##### GenAI Security Project

- `Label`: `Strong adjacent`
- `Units`: OWASP Top 10 for LLM Apps, agent/security guidance.
- `Focused area`: practitioner controls for LLM apps and agents.
- `Specific analysis`: OWASP is important because developers actually use its lists. Track how human approval, prompt injection, insecure output handling, excessive agency, and supply-chain issues are translated into actionable controls.

#### Cloud Security Alliance

##### AI And Agentic Security Working Groups

- `Label`: `Strong adjacent`
- `Units`: CSA AI safety and agentic AI security working groups.
- `Focused area`: cloud AI governance, agent security, enterprise guidance.
- `Specific analysis`: CSA matters for enterprise security teams adopting agents across SaaS and cloud. The human-factor issue is organizational control: who owns agents, who approves integrations, and how incidents are investigated.

### USA: Main Focus Areas To Track

- Developer secure-code behavior: over-trust, prompt quality, AI-suggestion acceptance, generated-dependency risk, insecure code review, and training interventions.
- SOC analyst work: alert fatigue, situation awareness, evidence grounding, analyst authority, low-level telemetry interpretation, and handoff between AI summaries and human decisions.
- Reverse engineering and binary analysis: LLM-generated symbol names, type recovery, decompiler comments, explanation confidence, hallucinated control-flow summaries, and novice/expert gap reduction.
- Agent oversight: policy specification, runtime approval, scope configuration, audit logs, identity, data-access permissions, tool-call transparency, and approval fatigue.
- Red-team labor: who creates adversarial examples, how risk categories are chosen, how datasets become benchmarks, and whether model providers ignore user specificity and interaction context.
- Bug-bounty and maintainer workflows: AI-generated report volume, invalid-report burden, agentic validation, coordinated disclosure, and evidence thresholds for maintainers.

## China Detailed Record

China should be treated as the second main focus, but with a different evidence profile. The public record is strongest in Chinese-language cybersecurity benchmarks, model-safety evaluation platforms, contests, standards, AI coding products, and security-vendor ecosystems. Direct human-subject studies on LLM-assisted secure coding, SOC analysts, or reverse engineering are less visible than in the United States, so many China entries are marked `Strong adjacent` or `Watch`.

### China: Universities, Labs, Research Institutes, And Researchers

Each entry is separated by institution and group. Cross-institution benchmarks are decomposed by the role each institution or group plays.

#### Alibaba Security (阿里巴巴安全)

##### CS-Eval Collaborator

- `Label`: `Core`
- `People`: Zhengmin Yu, Jiutian Zeng, Siyi Chen, Wenhan Xu, Dandan Xu, Xiangyu Liu, Zonghao Ying, Nan Wang, Yuan Zhang, Min Yang.
- `Focused area`: CyberSec-Eval / CS-Eval, bilingual cybersecurity LLM capability benchmarking.
- `Specific analysis`: Alibaba Security's role in CS-Eval is important because it connects benchmark design to industry cybersecurity practice. For human factors, the key question is whether the benchmark reflects tasks that Chinese security practitioners actually perform, such as vulnerability management, penetration-testing knowledge, infrastructure security, and incident response. Track Alibaba Security for the operational categories and cognitive levels used to define "cybersecurity capability" in Chinese/English LLMs.
- `Sources`: https://cs-eval.com/ ; https://arxiv.org/abs/2411.16239 ; https://github.com/CS-EVAL/CS-Eval.

#### Fudan University (复旦大学)

##### CS-Eval Collaborator

- `Label`: `Core`
- `People`: Track Fudan-affiliated CS-Eval authors and cybersecurity/AI evaluation collaborators.
- `Focused area`: bilingual cybersecurity benchmark construction, LLM evaluation, Chinese-language security knowledge.
- `Specific analysis`: Fudan's role in CS-Eval should be tracked separately from Alibaba because it represents the academic evaluation side of the benchmark. The human-factor value is curriculum and expertise mapping: the categories in CS-Eval show what knowledge Chinese researchers consider relevant for security professionals interacting with LLMs.
- `Sources`: https://cs-eval.com/ ; https://arxiv.org/abs/2411.16239.

##### System Software and Security Lab (系统软件与安全实验室) / Whitzard-AI

- `Label`: `Core`
- `People`: Mi Zhang and Whitzard-AI / S3 Lab contributors.
- `Focused area`: JADE linguistic safety evaluation, Chinese open-source LLM safety testing, human-expert-aligned evaluation.
- `Specific analysis`: Fudan's JADE line is important because it focuses on Chinese-language linguistic variation rather than generic jailbreak strings. The human-factor angle is evaluator judgment: JADE explicitly tries to align evaluation with human expert judgment while generating natural language variants. This is directly relevant to Chinese developer and security-user settings where semantic meaning can remain constant while syntax changes enough to bypass guardrails.
- `Sources`: https://whitzard-ai.github.io/jade_en.html.

#### University of Chinese Academy of Sciences (中国科学院大学)

##### CS-Eval Collaborator

- `Label`: `Core`
- `People`: Track UCAS-affiliated CS-Eval authors and CAS/UCAS security researchers.
- `Focused area`: cybersecurity capability evaluation, academic benchmark design, national research infrastructure.
- `Specific analysis`: UCAS matters because it connects CS-Eval to the Chinese Academy of Sciences ecosystem. For human factors, this makes CS-Eval more than a platform benchmark: it is a signal of how national research infrastructure may evaluate security LLMs for education, public-sector use, and industry adoption.
- `Sources`: https://cs-eval.com/ ; https://arxiv.org/abs/2411.16239.

#### Tsinghua University (清华大学)

##### Institute for Network Sciences and Cyberspace (网络科学与网络空间研究院)

- `Label`: `Core`
- `People`: Redbud student team, Blue-Lotus CTF/security ecosystem, INSC faculty and students.
- `Focused area`: Tianwang Cup large-model track, prompt injection, jailbreak, data leakage, reliability, model supply-chain attacks.
- `Specific analysis`: Tsinghua INSC is a core China signal because its public contest work explicitly evaluates LLM security through human team performance: attack sample construction, on-site reproduction, technical defense, and report quality. This makes it valuable for studying how Chinese security education and contest culture define AI-security competence.
- `Sources`: https://www.insc.tsinghua.edu.cn/info/1183/4112.htm ; https://twcup.cverc.org.cn/ ; https://www.insc.tsinghua.edu.cn/inscen/.

##### IIIS Xu Wei Research Group (交叉信息研究院许伟课题组)

- `Label`: `Strong adjacent`
- `People`: Xu Wei group.
- `Focused area`: secure and robust AI applications, AI security, privacy-preserving applications, high-performance distributed LLM training and inference.
- `Specific analysis`: The Xu Wei group is relevant to deployment infrastructure rather than direct human-subject work. Its human-factor importance is that secure and efficient LLM deployment changes what organizations can safely run locally, what data can stay private, and how much control developers or security teams have over model behavior and inference context.
- `Sources`: https://iiis.tsinghua.edu.cn/en/Research/Research_Groups/xuwei_0709.htm.

##### AI International Governance Institute (人工智能国际治理研究院)

- `Label`: `Strong adjacent`
- `People`: Xue Lan, Tang Jie and governance collaborators.
- `Focused area`: AI safety governance, international AI governance, policy frameworks.
- `Specific analysis`: Tsinghua AIIG should be separated from technical cyber labs because its role is governance. For human factors, it helps define who is responsible for safe model deployment and how public-facing LLM services should be evaluated, approved, and audited. This is especially relevant in China, where public generative-AI deployment is tied to security assessment and filing requirements.
- `Sources`: https://www.tsinghua.edu.cn/info/1182/116933.htm.

#### Chinese AI Safety Network (中国人工智能安全网络)

##### China-Facing Safety Coordination

- `Label`: `Strong adjacent`
- `People`: Participating institutions include CAS, CAICT, PKU, Tsinghua, Shanghai AI Lab, BAAI, Beijing-AISI, CUHK, Lingnan University, China Information Technology Security Evaluation Center, CLAI, Alibaba, Ant Group, SenseTime and others.
- `Focused area`: Chinese AI safety coordination, governance, safety attitudes, model deployment norms.
- `Specific analysis`: This network should be tracked as a coordination layer, not as a single lab. Its human-factor role is shaping consensus about safety governance and model-service responsibility. It can influence what Chinese researchers consider acceptable human oversight, evaluation, and risk-management practice for LLM services.
- `Sources`: https://chinese-ai-safety.institute/.

#### Peking University (北京大学)

##### Knowledge Computing Lab (知识计算实验室)

- `Label`: `Strong adjacent`
- `People`: KCL / National Engineering Research Center for Software Engineering researchers.
- `Focused area`: Code LLMs, programming language comprehension, LLM evaluation, software and system security, human-machine integration.
- `Specific analysis`: PKU KCL is relevant because it sits at the intersection of code models and software-engineering infrastructure. For human factors, watch for work on how programmers understand model-generated code, how code LLMs support comprehension, and whether evaluation includes developer-facing usefulness rather than only benchmark scores.
- `Sources`: https://seeeeeeven7.github.io/kcl-homepage.

##### OSS-Lab (开源软件数据分析实验室) / Software Engineering Institute (软件工程研究所)

- `Label`: `Strong adjacent`
- `People`: OSS-Lab@PKU-SEI researchers.
- `Focused area`: open-source software analytics, developer behavior, repository mining.
- `Specific analysis`: PKU OSS-Lab is a separate human-factor node because it studies software repositories and developer life through data. It is useful for future work on whether AI coding assistants change open-source maintainer burden, PR review behavior, issue quality, vulnerability fix patterns, and contributor dynamics in Chinese and global OSS.
- `Sources`: https://osslab-pku.org/.

#### Shanghai Jiao Tong University (上海交通大学)

##### LLM for Software Engineering Lab (大语言模型软件工程实验室)

- `Label`: `Strong adjacent`
- `People`: Beijun Shen, Xiaodong Gu, Yuling Shi and LLMSE members.
- `Focused area`: code LLMs, code generation, code translation, defect detection and repair.
- `Specific analysis`: SJTU LLMSE should be a primary China watch group for LLM-for-code. Its human-factor importance is developer interaction with code agents: how context is selected, how generated repairs are reviewed, and whether defect-detection outputs are actionable for human developers. Track for repository-level coding, code translation, and defect repair work that can be extended into secure-coding studies.
- `Sources`: https://base.sjtu.edu.cn/home/.

##### GoSec

- `Label`: `Strong adjacent`
- `People`: GoSec@CS.SJTU researchers.
- `Focused area`: system and software security, trusted execution, binary analysis, secure compilation.
- `Specific analysis`: GoSec should be tracked separately from LLMSE because it provides the software-security and binary-analysis substrate. The human-factor question is whether LLM assistants can help security experts reason over binaries, compiler artifacts, TEEs, or low-level system code without creating misleading summaries.
- `Sources`: https://gosec.sjtu.edu.cn/.

##### NSEC - Network Security and Privacy Protection Lab (网络安全与隐私保护实验室)

- `Label`: `Strong adjacent`
- `People`: Network Security and Privacy Protection Lab researchers.
- `Focused area`: network security, privacy protection, mobile and wireless network security.
- `Specific analysis`: NSEC is relevant to SOC and network-security uses of LLMs. Track for future work on analyst support for network telemetry, privacy-preserving security analysis, and LLM explanations over network attack evidence.
- `Sources`: https://nsec.sjtu.edu.cn/.

#### Zhejiang University (浙江大学)

##### Ubiquitous System Security Lab (泛在系统安全实验室)

- `Label`: `Strong adjacent`
- `People`: USSLab researchers.
- `Focused area`: ubiquitous system security, IoT/security, system security.
- `Specific analysis`: ZJU USSLab is relevant to LLM security because many agentic security tasks involve cyber-physical, IoT, and mobile contexts where evidence is messy and environment-specific. The human-factor question is how LLMs help analysts interpret device behavior without hallucinating device state or exploitability.
- `Sources`: https://usslab.org/contact.html.

##### LLM4VFD / Vulnerability Fix Detection Line

- `Label`: `Strong adjacent`
- `People`: Track LLM4VFD authors and ZJU software-security collaborators.
- `Focused area`: vulnerability fix detection using code change intention, artifacts, history, and LLM-generated analysis.
- `Specific analysis`: This line is important because it reports a security-expert user study. It should be tracked for whether LLM-generated explanations help humans classify vulnerability fixes more efficiently. The key human-factor measure is actionability: does the generated analysis help experts make better decisions, or only make them feel faster?
- `Sources`: https://colab.ws/articles/10.1145%2F3715738.

#### University of Hong Kong (香港大学)

##### JC STEM Lab of Intelligent Cybersecurity (JC STEM 智能网络安全实验室)

- `Label`: `Strong adjacent`
- `People`: HKU intelligent cybersecurity researchers.
- `Focused area`: AI-driven security and software engineering.
- `Specific analysis`: HKU is relevant as a Hong Kong bridge between software engineering, AI, and cybersecurity. Its explicit AI-driven security/software-engineering focus makes it a watch node for human-facing tools that support vulnerability analysis, code repair, and cyber operations.
- `Sources`: https://sec.hku.hk/research.

#### HKUST - Hong Kong University of Science and Technology (香港科技大学)

##### Software Security / Program Analysis Watch

- `Label`: `Watch`
- `People`: Track HKUST software security, testing, and program-analysis researchers.
- `Focused area`: LLM-assisted program analysis, software testing, fuzzing, vulnerability detection.
- `Specific analysis`: HKUST should be kept separate because Hong Kong universities often publish in top software-engineering and security venues. The human-factor angle to watch is whether LLM program-analysis tools are evaluated with expert users rather than only benchmark labels.

#### Chinese University of Hong Kong (香港中文大学)

##### AI / Security / HCI Watch

- `Label`: `Watch`
- `People`: Track CUHK researchers in AI safety, software engineering, and security.
- `Focused area`: AI security, software engineering, human-AI interaction.
- `Specific analysis`: CUHK is relevant because it appears in Chinese AI Safety Network context and has strong AI/security capacity. Watch for bilingual human-subject studies and governance work connecting mainland and Hong Kong deployment contexts.

#### City University of Hong Kong (香港城市大学)

##### Software And System Security Watch

- `Label`: `Watch`
- `People`: Track CityU software security, systems, privacy, and AI researchers.
- `Focused area`: program analysis, system security, AI security.
- `Specific analysis`: CityU should be tracked for technical LLM-security work that could become human-facing analyst tooling. The main evidence gap is whether tools are tested with developers or security analysts.

#### Hong Kong Polytechnic University (香港理工大学)

##### Computing And Information Security Watch

- `Label`: `Watch`
- `People`: Track PolyU computing/security/HCI researchers.
- `Focused area`: software engineering, mobile/internet security, privacy, AI systems.
- `Specific analysis`: PolyU is relevant because it has strong computing and applied security capacity. Watch for studies of LLM-assisted mobile/IoT security analysis and human-facing developer tools.

#### Chinese Academy of Sciences (中国科学院)

##### Institute of Information Engineering (信息工程研究所)

- `Label`: `Watch`
- `People`: CAS/IIE security and AI researchers.
- `Focused area`: national cybersecurity research, vulnerability analysis, AI security, benchmark infrastructure.
- `Specific analysis`: CAS/IIE should be tracked separately from UCAS because it is a research-institute layer rather than a university teaching layer. For human factors, the likely relevance is national-scale evaluation, security assessment, and tooling for practitioners in government or critical infrastructure.

#### Nanjing University (南京大学)

##### Software Engineering And Security Watch

- `Label`: `Watch`
- `People`: Track NJU software engineering, program analysis, and cybersecurity researchers.
- `Focused area`: software analysis, testing, vulnerability detection, LLM-for-code.
- `Specific analysis`: Nanjing University is a high-probability source for future LLM software-security studies. The human-factor angle is how developers use LLM-generated analysis during debugging, testing, and vulnerability repair.

#### Beihang University (北京航空航天大学)

##### Cybersecurity And Software Systems Watch

- `Label`: `Watch`
- `People`: Track Beihang cybersecurity, systems, and AI researchers.
- `Focused area`: software security, systems security, AI security.
- `Specific analysis`: Beihang is relevant because of its engineering and aerospace/critical-systems orientation. For human factors, watch for LLM tools in high-assurance or safety-critical software review where human approval standards are stricter.

#### Huazhong University of Science and Technology (华中科技大学)

##### Security Watch

- `Label`: `Watch`
- `People`: Track HUST network/security/software researchers.
- `Focused area`: vulnerability analysis, cyber ranges, AI for security.
- `Specific analysis`: HUST is a watch node for Chinese cyber-range and network-security work. The human-factor issue is whether LLMs help students and analysts learn attack/defense reasoning or mainly automate answer generation.

#### Wuhan University (武汉大学)

##### Cybersecurity Watch

- `Label`: `Watch`
- `People`: Track Wuhan University cybersecurity and AI researchers.
- `Focused area`: network security, software security, AI-assisted analysis.
- `Specific analysis`: Wuhan University should be tracked for regional cybersecurity research and education. The specific question is how LLMs are integrated into training, SOC-like labs, and vulnerability-analysis workflows.

#### Xidian University (西安电子科技大学)

##### Cybersecurity Education And Research Watch

- `Label`: `Watch`
- `People`: Track Xidian cybersecurity, network security, and AI researchers.
- `Focused area`: cyber education, network security, vulnerability analysis.
- `Specific analysis`: Xidian is relevant because of its cybersecurity education strength. Watch for LLM-assisted teaching, CTF training, and secure-coding education studies with Chinese students.

#### Harbin Institute of Technology (哈尔滨工业大学)

##### AI / Cybersecurity Watch

- `Label`: `Watch`
- `People`: Track HIT AI, software engineering, and cybersecurity researchers.
- `Focused area`: LLMs, software engineering, security evaluation, cyber-physical systems.
- `Specific analysis`: HIT should be tracked for AI and engineering-heavy security work. The human-factor angle is whether LLM security tools can be trusted in complex engineering software rather than only web/application examples.

#### University of Science and Technology of China (中国科学技术大学)

##### AI Safety / Cybersecurity Watch

- `Label`: `Watch`
- `People`: Track USTC cyber, AI safety, and software-security researchers.
- `Focused area`: AI safety, LLM evaluation, cybersecurity, software security.
- `Specific analysis`: USTC is a high-priority watch node because it has strong AI and cybersecurity capacity. For this dossier, watch for Chinese-language model safety evaluations that include coding, cyber misuse, and human review.

### China: Companies, Platforms, Standards Bodies, And Security Ecosystem

#### Alibaba (阿里巴巴)

##### Alibaba Cloud (阿里云) - Tongyi Lingma (通义灵码)

- `Label`: `Core`
- `Units`: Lingma AI Coding Assistant, Alibaba Cloud developer tooling.
- `Focused area`: AI coding assistant, code completion, debugging, multi-file collaboration, enterprise development.
- `Specific analysis`: Lingma should be separated from Qwen because it is the developer-facing workflow surface. Human factors include code privacy, context boundaries, enterprise governance, generated-code review, and whether developers understand when suggestions are model guesses versus project-grounded edits.
- `Sources`: https://www.alibabacloud.com/en/product/lingma ; https://docs.qwencloud.com/developer-guides/clients-and-developer-tools/lingma.

##### Alibaba Cloud / Qwen Team (通义千问团队) - Qwen Code And Model Platform

- `Label`: `Core`
- `Units`: Qwen model family, Qwen Cloud, Model Studio.
- `Focused area`: code models, agentic model access, model APIs, developer integrations.
- `Specific analysis`: Qwen is the model layer behind many Chinese developer workflows. Its human-factor importance is model selection and trust: developers may use Qwen locally, through cloud APIs, or through coding plans, each with different privacy, logging, and governance assumptions.
- `Sources`: https://docs.qwencloud.com/developer-guides/security-compliance/data-security ; https://qwen.readthedocs.io/_/downloads/en/v1.5/pdf/.

##### Alibaba Security (阿里巴巴安全) - Cybersecurity Benchmark And Evaluation

- `Label`: `Core`
- `Units`: Alibaba Security, CS-Eval collaboration.
- `Focused area`: cybersecurity capability evaluation, benchmark design, industry security tasks.
- `Specific analysis`: Alibaba Security should also be tracked as a company actor, not only an academic collaborator. Its key value is translating real security domains into benchmark categories. The human-factor issue is whether benchmark categories align with analyst and developer workflows or simply test abstract cyber knowledge.
- `Sources`: https://cs-eval.com/ ; https://github.com/CS-EVAL/CS-Eval.

#### Tencent (腾讯)

##### Zhuque Lab (腾讯朱雀实验室)

- `Label`: `Core`
- `Units`: Tencent Security Platform Department, Zhuque Lab.
- `Focused area`: practical offense-defense, AI security, LLM and agent vulnerabilities, vendor/open-source vulnerability research.
- `Specific analysis`: Zhuque Lab is a core Chinese AI-security actor because it explicitly focuses on practical AI security rather than only model development. Human-factor relevance includes red-team methodology, responsible disclosure, and how AI-security findings are communicated to vendors, open-source maintainers, and internal product teams.
- `Sources`: https://matrix.tencent.com/en/about.

##### Hunyuan (腾讯混元)

- `Label`: `Strong adjacent`
- `Units`: Hunyuan foundation model team and Tencent Cloud.
- `Focused area`: Chinese foundation models, enterprise deployment, assistant features.
- `Specific analysis`: Hunyuan should be separated from Zhuque because it is a model/provider surface. For human factors, track how Tencent balances consumer/enterprise productivity with privacy, security, and content-safety requirements, especially when Hunyuan is embedded into business workflows.
- `Sources`: https://www.tencent.com/en-us/articles/2201685.html.

#### Huawei Cloud (华为云)

##### Pangu Large Models (盘古大模型)

- `Label`: `Strong adjacent`
- `Units`: Pangu Large Models, Huawei Cloud ModelArts Studio.
- `Focused area`: enterprise large models, private deployment, domain-specific AI, cloud security responsibility.
- `Specific analysis`: Huawei Pangu matters for enterprise and critical-sector adoption. The human-factor issue is operational trust: private deployment can reduce data-leakage concerns, but human operators still need governance over model outputs, tool permissions, and generated code or security actions.
- `Sources`: https://www.huaweicloud.com/intl/en-us/product/pangu.html ; https://support.huawei.com/enterprise/en/doc/EDOC1100404294/378246d7/overview.

#### Baidu (百度)

##### ERNIE / Qianfan (文心一言 / 千帆)

- `Label`: `Strong adjacent`
- `Units`: ERNIE Bot, Baidu AI Cloud Qianfan.
- `Focused area`: public-facing and enterprise LLM services, Chinese-language model deployment.
- `Specific analysis`: Baidu is important because ERNIE is one of China's major public-facing LLM systems. For human factors, track how public service security review, content reliability, and user-facing assistant design affect developer and enterprise trust in LLM outputs.
- `Sources`: https://yiyan.baidu.com/blog/about/ ; https://apnews.com/article/e7fa36ad28215db42f720a3ac028e2c4.

#### ByteDance (字节跳动)

##### Software Engineering Lab (软件工程实验室)

- `Label`: `Strong adjacent`
- `Units`: ByteDance SE Lab.
- `Focused area`: safe and trusted intelligent automated software engineering.
- `Specific analysis`: ByteDance SE Lab is relevant because it explicitly frames automated software engineering as safe and trusted. The human-factor issue is how software-engineering agents allocate work between human developers and automated repair/localization systems, especially under real product constraints.
- `Sources`: https://se-research.bytedance.com/.

##### Trae AI IDE

- `Label`: `Strong adjacent`
- `Units`: Trae AI IDE, Trae Agent.
- `Focused area`: adaptive AI IDE, coding agents, test-time scaling for software engineering.
- `Specific analysis`: Trae should be separated from ByteDance SE Lab because it is the developer-facing product surface. For human factors, track multi-step code edits, test execution, user approval, rollback, and whether generated changes are understandable enough for code review.
- `Sources`: https://se-research.bytedance.com/ ; https://arxiv.org/abs/2507.23370.

#### Ant Group (蚂蚁集团)

##### Ant Ling / LingGuang (Ant Ling / 灵光) / Privacy-Preserving AI

- `Label`: `Strong adjacent`
- `Units`: Ant Ling AI Model Family, LingGuang, privacy-preserving computing platforms.
- `Focused area`: AI assistant, natural-language app generation, secure/reliable user experience, privacy-preserving AI.
- `Specific analysis`: Ant Group is a strong human-factor watch because its AI systems operate in financial and consumer contexts where trust, privacy, and user comprehension matter. The natural-language-to-app workflow raises software-security questions: users may create functional mini-apps without understanding authentication, data flow, or permission boundaries.
- `Sources`: https://www.antgroup.com/en/technology.

#### DeepSeek (深度求索)

##### Code Models And Open-Weight Ecosystem

- `Label`: `Strong adjacent`
- `Units`: DeepSeek models, DeepSeek-Coder, open-weight model releases.
- `Focused area`: code intelligence, open-weight coding models, model safety and deployment risk.
- `Specific analysis`: DeepSeek matters because its models are widely used by developers and security researchers. For human factors, the key issue is deployment context: running open weights locally changes data-governance risk but does not automatically solve generated-code security, alignment, or censorship/content-policy issues.
- `Sources`: https://cdn.deepseek.com/policies/en-US/model-algorithm-disclosure.html ; https://arxiv.org/abs/2401.14196 ; https://www.nist.gov/news-events/news/2025/09/caisi-evaluation-deepseek-ai-models-finds-shortcomings-and-risks.

#### Qihoo 360 / 360 Digital Security (奇虎360 / 360数字安全集团)

##### SOC / Security Products / AI Security Assistant Ecosystem

- `Label`: `Strong adjacent`
- `Units`: 360 security products, enterprise security services, AI security assistant ecosystem.
- `Focused area`: SOC/security products, threat detection, AI-assisted security operations, vulnerability research.
- `Specific analysis`: Qihoo 360 is a major Chinese security-vendor actor. Its human-factor relevance is SOC and enterprise deployment: how AI assistants are integrated into security operations, how analysts validate outputs, and how product security incidents affect trust in security AI systems.
- `Sources`: https://www.360.cn/about/index_eng.html.

#### CAICT - China Academy of Information and Communications Technology (中国信息通信研究院)

##### AI Product Security And Evaluation

- `Label`: `Strong adjacent`
- `Units`: China Academy of Information and Communications Technology, AI product security evaluation activity.
- `Focused area`: AI product security, trusted AI evaluation, vulnerability databases, industry assessment.
- `Specific analysis`: CAICT is important because it can turn AI security concerns into evaluation programs and industry practice. The human-factor issue is institutional assurance: what evidence must vendors provide, who reviews it, and how evaluation results shape enterprise adoption.
- `Sources`: https://www.aibase.com/news/23731 ; https://www.exportsemi.com/company-post/caict-announces-first-round-of-trusted-ai-code-large-language-model/.

#### TC260 - National Technical Committee 260 on Cybersecurity (全国网络安全标准化技术委员会)

##### Generative AI Security Requirements

- `Label`: `Core/strong adjacent`
- `Units`: National Technical Committee 260 on Cybersecurity.
- `Focused area`: basic security requirements for generative AI services, training data security, model security, supply-chain assessment.
- `Specific analysis`: TC260 is a standards actor rather than a product group. Its human-factor relevance is that it shapes what providers must document and review before deployment. Track requirements that force human review of training data, model outputs, supply-chain risk, complaint handling, and security assessments.
- `Sources`: https://cset.georgetown.edu/publication/china-safety-requirements-for-generative-ai-final/ ; https://www.dataguidance.com/news/china-tc260-publishes-basic-security-requirements.

#### Cyberspace Administration of China (国家互联网信息办公室)

##### Generative AI Service Governance

- `Label`: `Core/strong adjacent`
- `Units`: CAC and co-issuing ministries for generative-AI service measures.
- `Focused area`: public generative-AI service security assessments, algorithm filing, provider responsibility.
- `Specific analysis`: CAC is central to China's governance model. Human factors include provider accountability, user-facing content reliability, complaint mechanisms, and security review before public launch. This is different from the U.S. pattern: human oversight is partly institutionalized at provider/regulator level rather than only inside product UI.
- `Sources`: https://regulations.ai/regulations/china-2023-7-generative-ai.

#### China Information Technology Security Evaluation Center (中国信息安全测评中心)

##### Security Evaluation / Procurement Assurance

- `Label`: `Watch`
- `Units`: China Information Technology Security Evaluation Center.
- `Focused area`: technology security evaluation, procurement/security assessment, AI hardware/software certification.
- `Specific analysis`: This actor matters for the procurement and assurance layer. For human factors, security evaluation decisions influence which AI tools enterprises and public bodies trust, deploy, or ban.

#### Qi-Anxin (奇安信)

##### Enterprise Cybersecurity Products And Services

- `Label`: `Watch`
- `Units`: Qi-Anxin enterprise cybersecurity products and services.
- `Focused area`: SOC, endpoint, threat intelligence, enterprise security operations.
- `Specific analysis`: Qi-Anxin is a likely deployment surface for LLM-assisted SOC and enterprise security workflows. Track analyst-facing AI features, false-positive handling, and whether reports include evidence suitable for human verification.

#### NSFOCUS (绿盟科技)

##### Vulnerability Management / DDoS / Threat Intelligence

- `Label`: `Watch`
- `Units`: NSFOCUS security products and managed services.
- `Focused area`: vulnerability management, DDoS, threat intelligence, SOC services.
- `Specific analysis`: NSFOCUS is relevant to vulnerability-management human factors. The key question is whether LLM explanations reduce triage time while preserving accurate exploitability and asset-context judgments.

#### VenusTech (启明星辰)

##### Enterprise Network Security / SOC

- `Label`: `Watch`
- `Units`: VenusTech security products and services.
- `Focused area`: enterprise network security, SOC, threat detection.
- `Specific analysis`: VenusTech should be watched for AI-assisted SOC adoption in Chinese enterprises. Human factors include alert prioritization, analyst workload, and explainability in regulated environments.

#### Sangfor (深信服)

##### Security / Cloud / Infrastructure Products

- `Label`: `Watch`
- `Units`: Sangfor security, cloud, and infrastructure products.
- `Focused area`: enterprise security, cloud security, infrastructure operations.
- `Specific analysis`: Sangfor is relevant because LLM security assistants may be embedded in infrastructure operations, not only code review. Track how human admins approve remediation, policy changes, and incident-response actions.

#### Topsec (天融信)

##### Enterprise Security Operations / Compliance

- `Label`: `Watch`
- `Units`: Topsec security products and services.
- `Focused area`: enterprise security operations, threat defense, compliance.
- `Specific analysis`: Topsec is a watch actor for Chinese compliance-heavy security workflows. The human-factor issue is whether AI-generated explanations align with audit and compliance requirements.

#### DBAPPSecurity (安恒信息)

##### Data Security / AppSec / Threat Intelligence

- `Label`: `Watch`
- `Units`: DBAPPSecurity products and research.
- `Focused area`: data security, application security, threat intelligence.
- `Specific analysis`: DBAPPSecurity is relevant to AI-assisted data and AppSec workflows. Track whether LLM tools help humans classify sensitive data exposure and validate application vulnerabilities.

#### Chaitin Tech (长亭科技)

##### Web Security / Vulnerability Research

- `Label`: `Watch`
- `Units`: Chaitin security research and product teams.
- `Focused area`: web security, vulnerability research, attack-defense technology.
- `Specific analysis`: Chaitin is relevant because of its technical security research orientation. The human-factor angle is how AI affects expert web vulnerability analysis, PoC validation, and report quality.

#### Knownsec (知道创宇)

##### Threat Intelligence / Incident Response

- `Label`: `Watch`
- `Units`: Knownsec security research and threat-intelligence teams.
- `Focused area`: threat intelligence, vulnerability research, incident response.
- `Specific analysis`: Knownsec should be tracked for threat-intelligence workflows. LLMs can summarize intelligence, but human analysts must validate sources, attribution, and operational relevance.

#### Hillstone Networks (山石网科)

##### Network Security / Cloud Security

- `Label`: `Watch`
- `Units`: Hillstone network security products.
- `Focused area`: network security, cloud security, threat detection.
- `Specific analysis`: Hillstone is a watch point for network-security AI assistance. Human factors include whether generated network-threat explanations are grounded in packet/log evidence and whether admins understand recommended policy changes.

#### ThreatBook (微步在线)

##### Threat Intelligence Platform

- `Label`: `Watch`
- `Units`: ThreatBook threat-intelligence platform.
- `Focused area`: threat intelligence, IOC analysis, attack attribution.
- `Specific analysis`: ThreatBook is relevant because LLMs are well suited to summarization but risky for attribution. Human factors include source transparency, confidence labels, and preventing analysts from over-trusting generated actor narratives.

#### Tophant (斗象科技)

##### Vulnerability Intelligence / Attack-Surface Management

- `Label`: `Watch`
- `Units`: Tophant security intelligence and attack-surface products.
- `Focused area`: vulnerability intelligence, attack-surface management, threat analysis.
- `Specific analysis`: Tophant is a watch actor for AI-assisted exposure management. Track how AI prioritizes assets and whether human teams can inspect the reasoning behind risk rankings.

#### Zhipu AI (智谱AI)

##### ChatGLM / GLM Model Platform

- `Label`: `Watch`
- `Units`: ChatGLM and Zhipu model platform.
- `Focused area`: Chinese LLM services, code and agent capabilities, safety evaluations.
- `Specific analysis`: Zhipu should be tracked for Chinese-language coding and agent behavior. Human factors include developer trust, public-service compliance, and model behavior under cyber/security prompts.

#### Moonshot AI (月之暗面)

##### Kimi

- `Label`: `Watch`
- `Units`: Kimi model platform.
- `Focused area`: long-context Chinese LLMs, productivity and coding use cases.
- `Specific analysis`: Kimi is relevant because long context changes software-security workflows: users may upload larger codebases or documents. Track privacy, context provenance, and whether long-context summaries improve or distort security review.

#### MiniMax (稀宇科技)

##### Model Platform

- `Label`: `Watch`
- `Units`: MiniMax model platform.
- `Focused area`: consumer and enterprise LLM services.
- `Specific analysis`: MiniMax should be watched for user-facing agent and assistant workflows. Human factors include how non-expert users interpret generated code or security advice.

#### Baichuan (百川智能)

##### Model Platform

- `Label`: `Watch`
- `Units`: Baichuan model family and platform.
- `Focused area`: Chinese foundation models, enterprise deployment.
- `Specific analysis`: Baichuan is relevant as part of China's model-provider ecosystem. Track whether safety evaluations include secure coding, cyber misuse, and human-facing explanation quality.

#### SenseTime (商汤科技)

##### Model And AI Platform Ecosystem

- `Label`: `Watch`
- `Units`: SenseTime model and AI platform ecosystem.
- `Focused area`: multimodal AI, enterprise AI, AI safety participation.
- `Specific analysis`: SenseTime's relevance is multimodal and enterprise deployment. For software security, watch future agent systems that combine visual UI control with code/security tasks.

#### iFlytek (科大讯飞)

##### Spark / AI Assistant Ecosystem

- `Label`: `Watch`
- `Units`: Spark and iFlytek AI platforms.
- `Focused area`: Chinese-language AI assistants, enterprise and education contexts.
- `Specific analysis`: iFlytek is relevant to education and public-facing AI. Track whether AI-assisted secure-coding education or cybersecurity training appears in its ecosystem.

#### 01.AI (零一万物)

##### Yi Model Family

- `Label`: `Watch`
- `Units`: Yi model family and related platform.
- `Focused area`: Chinese open/model platform ecosystem.
- `Specific analysis`: 01.AI should be watched for developer adoption and open-model use. The human-factor issue is whether smaller/open models are used locally for security work without adequate evaluation.

#### Tianwang Cup (天网杯)

##### Large-Model Track

- `Label`: `Core`
- `Units`: Tianwang Cup organizers, participating university and industry teams.
- `Focused area`: LLM security competition, prompt injection, jailbreak, data leakage, reliability, model supply-chain attack samples.
- `Specific analysis`: Tianwang Cup is a direct Chinese human-factor signal because scoring includes human-produced artifacts: attack samples, reproduction, report quality, and technical defense. It is a useful case for studying how contests train red-team labor and shape what Chinese teams consider high-quality AI-security evidence.
- `Sources`: https://twcup.cverc.org.cn/ ; https://www.insc.tsinghua.edu.cn/info/1183/4112.htm.

#### Alibaba AI Security Challenge (阿里云AI安全全球挑战赛)

##### AI Security Challenge

- `Label`: `Watch`
- `Units`: Alibaba Cloud / Alibaba Security challenge ecosystem.
- `Focused area`: AI security challenge tasks, model attack and defense, security evaluation.
- `Specific analysis`: Alibaba's challenge activity should be tracked separately from CS-Eval. The human-factor value is competition design: what artifacts teams must submit, how judges evaluate attack quality, and whether defense strategies are rewarded alongside attack success.

#### AI Linghang Cup (AI领航杯)

##### AI + Security Track

- `Label`: `Watch`
- `Units`: China Internet Association and contest participants.
- `Focused area`: AI + security competition, applied security innovation.
- `Specific analysis`: AI Linghang Cup is relevant to applied workforce development. Track whether the competition produces reusable datasets, reports, or training patterns for LLM-assisted security operations.

#### Jinlingguang Cup (金灵光杯)

##### Generative-AI Security Track

- `Label`: `Watch`
- `Units`: Jinlingguang Cup organizers and participating teams.
- `Focused area`: generative-AI security, model attack/defense, safety testing.
- `Specific analysis`: Jinlingguang Cup should be tracked for Chinese-language AI safety red-team practices. The human-factor question is how teams document attacks and whether judge scoring values reproducibility and remediation guidance.

#### XCTF / CVE-Range Platforms (XCTF联赛 / CVE靶场)

##### CTF And Vulnerability-Range Platforms

- `Label`: `Watch`
- `Units`: XCTF, CVE-range and cyber-range platforms.
- `Focused area`: CTF training, vulnerability ranges, AI-assisted attack/defense learning.
- `Specific analysis`: XCTF-style ranges matter because they define the learning environment for many Chinese security students and practitioners. As LLM agents enter CTF workflows, track whether the platforms add rules, telemetry, or evaluation criteria that distinguish human skill from agent scaffolding.

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
