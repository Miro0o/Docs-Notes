---
ai-generated: true
last-reviewed: 2026-07-30
---

# Architecture, Evolution, and Operations

Back: [Academic Status](Academic-Status.md)

Scope: component structure, agent roles and collaboration topology, prompt and model lifecycle, reference architectures, deployment, maintenance, and operational practice for LLM-integrated software and agents.

## Status

Architecture and lifecycle evidence trails language and runtime work. Deployed systems combine prompts, models, retrieval, memory, tools, evaluators, conventional services, and human gates, yet many papers treat this composition as incidental scaffolding. The most useful SE work makes these components and their evolution first-class.

Multi-agent architecture is also becoming adaptive rather than entirely hand-designed. Recent work treats collaboration topology, agent selection, and collective expertise as system-level artifacts that can be evolved or composed, although evaluations must separate architectural gains from extra models, calls, tokens, and test-time compute.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Liang2025PromptsPrograms | [Prompts Are Programs Too! Understanding How Developers Build Software Containing Prompts](https://doi.org/10.1145/3729342) | 2025 | FSE/PACMSE / DOI | Interviews prompt developers and shows that prompt programming has distinctive mental-model, iteration, and tooling problems. | Published / Human study |
| Bucaioni2025ReferenceArchitecture | [A Functional Software Reference Architecture for LLM-Integrated Systems](https://conf.researchr.org/details/icsa-2025/icsa-2025-new-and-emerging-ideas/3/A-Functional-Software-Reference-Architecture-for-LLM-Integrated-Systems) | 2025 | ICSA New and Emerging Ideas / official program | Proposes a preliminary functional reference architecture and evaluates its applicability on three open-source systems. | Official program / NIER |
| Li2025SEFoundationModels | [Software Engineering and Foundation Models: Insights from Industry Blogs Using a Jury of Foundation Models](https://doi.org/10.1109/ICSE-SEIP66354.2025.00033) | 2025 | ICSE-SEIP / DOI | Maps 155 FM4SE and 997 SE4FM industry posts; finds deployment/operation and architecture/orchestration dominate SE4FM practice signals. | Published / Field map |
| Hu2025MultiAgentSE | [Self-Evolving Multi-Agent Collaboration Networks for Software Development](https://proceedings.iclr.cc/paper_files/paper/2025/hash/39af4f2f9399122a14ccf95e2d2e7122-Abstract-Conference.html) | 2025 | ICLR / proceedings | Introduces EvoMAC, which uses text-based environmental feedback and textual backpropagation to evolve a multi-agent collaboration network; also contributes the requirement-oriented, software-level RSD-Bench evaluation environment. | Published |
| Zhang2025SoftwareAgents | [Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d7b50b8ac2c781a12f26155f48310d8d-Abstract-Conference.html) | 2025 | ICLR / proceedings | Introduces DEI, a meta-module above heterogeneous software-engineering agent frameworks that manages agent collectives to exploit complementary expertise. | Published |

## Placement Note

EvoMAC and DEI are evaluated on software-development tasks, but their primary artifacts are mechanisms for organizing and evolving agent systems. They are therefore canonical here rather than in the LLM-for-software dossier. The task domain does not override the engineered-artifact test; secondary benchmark or code-generation implications should be cross-linked without duplicating full rows.

## Venue and Agenda Signals

- [RAISE 2026](https://conf.researchr.org/home/icse-2026/raise-2026) is an ICSE workshop, not a main-track paper. Its agenda identifies requirements-as-code, AIware lifecycle, cognitive architecture, performance engineering, and human-agent collaboration as emerging requirements-engineering concerns.
- [AIware 2026](https://conf.researchr.org/home/aiware-2026) is a specialized ACM conference co-located with FSE. Its Promptware/Agentware framing is a field signal; individual papers retain the exact venue label rather than being presented as FSE main-track work.
- [Murakkab](Compilers-Runtimes-And-Workflow-Orchestration.md) is canonical under runtimes but is also evidence that architecture must separate workflow intent from execution configuration.

## Lifecycle Model

| Artifact | Evolution concern | Evidence to retain |
| --- | --- | --- |
| Prompt/program | edits can change behavior nonlocally | version, diff, test set, model/version |
| Model/provider | quality, price, latency, and policy drift | release identifier, migration result, rollback |
| Retrieval/memory | corpus and index drift | data snapshot, embedding/index version, lineage |
| Tool/API | schema and semantic change | contract version, compatibility tests, deprecation |
| Orchestration | changed order, roles, retry, or routing | graph/config diff and trajectory regression |
| Agent collective | roles, topology, membership, selection, or collaboration policy evolve | collective/config version, change rationale, budget, and controlled comparison |
| Evaluator | circular or drifting quality judgments | evaluator version, calibration, human audit |
| Runtime | performance and scheduling changes | workload, SLOs, resource profile, canary result |
| Human control | approval and responsibility changes | policy version, owner, escalation and audit trail |

## Evaluation Checklist

- specify component boundaries and dependency versions;
- distinguish prompt, model, data, tool, and orchestration changes;
- include regression sets plus production or field evidence where possible;
- report migration and rollback behavior, not only steady-state accuracy;
- evaluate quality attributes beyond task success: modifiability, interoperability, observability, cost, and recovery;
- measure delayed maintenance and incident work;
- compare adaptive or collective agent designs with the best individual agent and budget-matched ensembles;
- attribute gains to organization, selection, or evolution rather than additional calls, tokens, or models;
- record organizational context and developer roles in practice studies;
- separate architecture proposals, NIER records, workshops, and mature evaluated systems.

## Research Directions

- reference architectures validated across independent domains and organizations;
- architecture decision records for model, memory, tool, and evaluator choices;
- semantic versioning for prompts, agent protocols, and behavior contracts;
- impact analysis across prompt/model/data/tool dependency graphs;
- adaptive agent organizations with explicit objectives, constraints, provenance, and rollback;
- causal evaluation of role, topology, membership, and routing changes;
- release-readiness gates and automated regression selection;
- canarying, rollback, and compensation for agents that alter external state;
- technical-debt models for promptware and agentware;
- operational SLOs combining task quality, latency, cost, and recovery;
- long-term studies of model/API drift and framework churn.

## Boundary

Architecting or evolving an LLM-integrated product or agent collective belongs here, even when software development is the evaluation task. Using an LLM to propose a conventional software architecture or directly improve ordinary code belongs in the LLM-for-software dossier.

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| 00032024MagisLlmBased | [MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution.](<http://papers.nips.cc/paper_files/paper/2024/hash/5d1f02132ef51602adf07000ca5b6138-Abstract-Conference.html>) | 2024 | NeurIPS / proceedings | Architecture Evolution And Operations | Introduces or evaluates mAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution; abstract-level contribution review remains pending. | formal-venue |
| 00012025LessonsLearnedMulti | [Lessons Learned: A Multi-Agent Framework for Code LLMs to Learn and Improve.](<http://papers.nips.cc/paper_files/paper/2025/hash/9d5d8162d91727959aa1a47e5d15dd50-Abstract-Conference.html>) | 2025 | NeurIPS / proceedings | Architecture Evolution And Operations | Introduces or evaluates lessons Learned: A Multi-Agent Framework for Code LLMs to Learn and Improve; abstract-level contribution review remains pending. | formal-venue |
| Bui2025LlmBasedMulti | [An LLM-based multi-agent framework for agile effort estimation](<https://conf.researchr.org/track/ase-2025/ase-2025-papers#event-e8db40c9-f85b-4ed9-9109-f33c654d0cb4>) | 2025 | ASE / accepted-program | Architecture Evolution And Operations | Introduces or evaluates an LLM-based multi-agent framework for agile effort estimation; abstract-level contribution review remains pending. | formal-venue |
| Yu2025OrcalocaLlmAgent | [OrcaLoca: An LLM Agent Framework for Software Issue Localization](<https://proceedings.mlr.press/v267/yu25x.html>) | 2025 | ICML / proceedings | Architecture Evolution And Operations | Introduces or evaluates orcaLoca: An LLM Agent Framework for Software Issue Localization; abstract-level contribution review remains pending. | formal-venue |
| Zhang2025AdaptiveSelfImprovement | [Adaptive Self-improvement LLM Agentic System for ML Library Development](<https://proceedings.mlr.press/v267/zhang25at.html>) | 2025 | ICML / proceedings | Architecture Evolution And Operations | Introduces or evaluates adaptive Self-improvement LLM Agentic System for ML Library Development; abstract-level contribution review remains pending. | formal-venue |
| Li2026SculptorEmpoweringLlms | [Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management](<https://openreview.net/forum?id=HPeiH7da0Z>) | 2026 | ICLR / accepted-program | Architecture Evolution And Operations | Introduces or evaluates sculptor: Empowering LLMs with Cognitive Agency via Active Context Management; abstract-level contribution review remains pending. | formal-venue |
| Wang2026ShadowsCodeExploring | [Shadows in the Code: Exploring the Risks and Defenses of LLM-based Multi-Agent Software Development Systems.](<https://doi.org/10.1609/aaai.v40i44.41134>) | 2026 | AAAI / proceedings | Architecture Evolution And Operations | Introduces or evaluates shadows in the Code: Exploring the Risks and Defenses of LLM-based Multi-Agent Software Development Systems; abstract-level contribution review remains pending. | formal-venue |
| Zhu2026AtomizerLlmBased | [Atomizer: An LLM-based Collaborative Multi-Agent Framework for Intent-Driven Commit Untangling](<https://conf.researchr.org/track/icse-2026/icse-2026-research-track#event-860ec6b8-0d27-4f0b-83dc-55232327aebc>) | 2026 | ICSE / accepted-program | Architecture Evolution And Operations | Introduces or evaluates atomizer: An LLM-based Collaborative Multi-Agent Framework for Intent-Driven Commit Untangling; abstract-level contribution review remains pending. | formal-venue |
| normalization2026AgenttailorSemanticAware | [AgentTailor: A Semantic-Aware LLM-Based Multi-Agent System with Actor-Critic Structure](<https://icml.cc/virtual/2026/poster/60754>) | 2026 | ICML / accepted-program | Architecture Evolution And Operations | Introduces or evaluates agentTailor: A Semantic-Aware LLM-Based Multi-Agent System with Actor-Critic Structure; abstract-level contribution review remains pending. | formal-venue |

### Frontier Preprints

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Apostolou2026AssistanceAutonomySystematic | [Assistance to Autonomy: A Systematic Literature Review of Agentic AI across the Software Development Life Cycle](<https://arxiv.org/abs/2605.15245>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Agentic AI in software product development is increasingly adopted by organizations, yet the field lacks a consolidated synthesis of where adoption is mature, which…. | frontier-preprint |
| Ding2026SagaSyntheticAgentic | [SAGA: Synthetic Agentic Graph Architecture for Temporal Benchmark Generation](<https://arxiv.org/abs/2607.17288>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Present SAGA (Synthetic Agentic Graph Architecture), a system for generating large-scale, semantically rich temporal graphs via a four-phase pipeline. | frontier-preprint |
| GLM5Team2026Glm5From | [GLM-5: from Vibe Coding to Agentic Engineering](<https://arxiv.org/abs/2602.15763>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Present GLM-5, a next-generation foundation model designed to transition the paradigm of vibe coding to agentic engineering. | frontier-preprint |
| Kanamarlapudi2026LlmConsortiumSoftware | [LLM Consortium for Software Design Refinement: A Controlled Experiment on Multi-Agent Collaboration Topologies](<https://arxiv.org/abs/2606.01490>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Present a controlled experiment evaluating 12 multi-agent LLM collaboration topologies for software architecture design. | frontier-preprint |
| Lee2026OverthinkingLoopsAgents | [Overthinking Loops in Agents: A Structural Risk via MCP Tools](<https://arxiv.org/abs/2602.14798>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Tool-using LLM agents increasingly coordinate real workloads by selecting and chaining third-party tools based on text-visible metadata such as tool names, descriptions, and return…. | frontier-preprint |
| Li2026CoopaModularLlm | [COOPA: A Modular LLM Agent Architecture for Operations Research Problems](<https://arxiv.org/abs/2606.27611>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Propose COOPA (COoperative OPerations Agent), a modular LLM-agent architecture for interpretable and scalable OR decision support. | frontier-preprint |
| Liu2026HimeRealTime | [HiMe: Real-Time Self-Hosted Personal Agent Platform for Health Insights with Wearable Devices](<https://arxiv.org/abs/2607.21019>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Present HiMe, a locally deployable, privacy-first agent platform that is fully compatible with real-time health data ecosystems across a wide range of wearable devices. | frontier-preprint |
| Nguyen2026PrivacyassistUserCentric | [PrivacyAssist: A User-Centric Agent Framework for Detecting Privacy Inconsistencies in Android Apps](<https://arxiv.org/abs/2604.23248>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | This paper presents PrivacyAssist, a multi-agent LLM-based platform that detects inconsistencies between user-granted permissions and developers' declared sensitive data collection and sharing practices. | frontier-preprint |
| Park2026AgenticFuzzingOpportunities | [Agentic Fuzzing: Opportunities and Challenges](<https://arxiv.org/abs/2605.10074>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Propose agentic fuzzing, a bug-finding approach seeded by historical bugs in which deep agents perform the reasoning directly. | frontier-preprint |
| Shi2026AgenticszzTemporalKnowledge | [AgenticSZZ: Temporal Knowledge Graph-Guided Agentic Bug-Inducing Commit Identification](<https://arxiv.org/abs/2602.02934>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Present AgenticSZZ, the first approach to apply Temporal Knowledge Graphs (TKGs) to software evolution analysis. | frontier-preprint |
| Siu2026FrameworkFormalizingLlm | [A Framework for Formalizing LLM Agent Security](<https://arxiv.org/abs/2603.19469>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Present a framework that systematizes existing attacks and defenses from the perspective of contextual security. | frontier-preprint |
| Sivaroopan2026ShieldAutoHealing | [SHIELD: An Auto-Healing Agentic Defense Framework for LLM Resource Exhaustion Attacks](<https://arxiv.org/abs/2601.19174>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Introduce SHIELD, a multi-agent, auto-healing defense framework centered on a three-stage Defense Agent that integrates semantic similarity retrieval, pattern matching, and LLM-based reasoning. | frontier-preprint |
| Tan2026FromPromptInjection | [From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors](<https://arxiv.org/abs/2605.31042>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | To reveal this threat, we introduce ClawTrojan, a benchmark designed to identify multi-step trojan attacks in local agentic harnesses. | frontier-preprint |
| Team2026YetEvenLess | [Yet Even Less Is Even Better For Agentic, Reasoning, and Coding LLMs](<https://arxiv.org/abs/2604.00824>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Inspired by the "Less-Is-More" hypothesis in mathematical reasoning, we investigate its extension to agentic scenarios and propose an end-to-end training framework that achieves superior…. | frontier-preprint |
| Wang2026PlanflipAttackingMulti | [PlanFlip: Attacking Multi-Agent LLM Systems via Planning-Phase Prompt Injection](<https://arxiv.org/abs/2607.16199>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Introduce PlanFlip, a framework comprising four planning-phase prompt injection attacks -- GoalSubstitution (PF-1), PriorityInversion (PF-2), ContextPollution (PF-3), and RoleConfusion (PF-4) -- each disguised as…. | frontier-preprint |
| Zhu2026YourAgentIs | [Your Agent is More Brittle Than You Think: Uncovering Indirect Injection Vulnerabilities in Agentic LLMs](<https://arxiv.org/abs/2604.03870>) | 2026 | arXiv / frontier-preprint | Architecture Evolution And Operations | Crucially, we conduct our evaluation entirely within dynamic multi-step tool-calling environments to capture the true attack surface of modern autonomous agents. | frontier-preprint |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
