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
