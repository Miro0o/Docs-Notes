---
ai-generated: true
last-reviewed: 2026-07-30
---

# Human Factor

Home: [LLM-Software-Research-Dossier-2026.md](LLM-Software-Research-Dossier-2026.md)

Scope: how developers understand, use, verify, review, trust, and remain accountable for LLM-assisted software work. This page separates peer-reviewed human evidence from product telemetry and industry reports, which live in [Non-Academic Status](Non-Academic-Status.md).

Focused records on visual and multimodal software, UI/UX, clarification, software-engineering education, developer-agent field studies, and longitudinal developer behavior live on [Human-Facing Software, UI/UX, Education, and Developer Experience](Academic-Status/Human-Facing-Software-UI-UX-Education-And-Developer-Experience.md). This page retains the cross-cutting human-system model and does not duplicate those canonical rows.

Task-specific review-comment generation, issue-to-commit linkage, change provenance, and governance records live on [Code Review, Change Governance, and Traceability](Academic-Status/Code-Review-Change-Governance-And-Traceability.md). This page retains the cross-cutting questions of reviewer workload, trust, approval, and accountability.

The study of developers building prompt-powered applications, *Prompts Are Programs Too!*, is canonical in the inverse-direction dossier’s [Architecture, Evolution, and Operations](../Software-For-LLM-Agent-Systems-Research-Dossier-2026/Academic-Status/Architecture-Evolution-And-Operations.md) page.

## Current Synthesis

The important outcome is not code produced per minute. It is completed, reviewed, maintainable work after verification and coordination costs. Assistance can reduce blank-page and local implementation effort while increasing time spent checking suggestions, reconstructing intent, debugging plausible failures, and reviewing larger change volumes.

Experience changes the interaction. Experts may reject more suggestions and invest more in repository context; novices may accept plausible output without recognizing hidden requirements. Agentic tools also shift work from typing to task decomposition, environment preparation, supervision, and acceptance decisions.

Recent top-venue evidence strengthens three points: agents should ask targeted questions when intent is underspecified; individual behavior is shaped by team practice and changes over time; and a completed educational deliverable is not evidence of durable understanding or knowledge transfer.

## Peer-Reviewed Anchors

| Key | Work | Year | Venue / evidence | Human question | Label |
| --- | --- | ---: | --- | --- | --- |
| Nam2024CodeUnderstanding | [Using an LLM to Help With Code Understanding](https://dblp.org/rec/conf/icse/NamMHVM24) | 2024 | ICSE / proceedings | How does LLM assistance change comprehension work and outcomes? | Published |
| FSE2024RocksCoding | [Rocks Coding, Not Development—A Human-Centric, Experimental Evaluation of LLM-Supported SE Tasks](https://2024.esec-fse.org/details/fse-2024-research-papers/67/Rocks-Coding-Not-Development-A-Human-Centric-Experimental-Evaluation-of-LLM-Support) | 2024 | FSE / official program | Does assistance transfer from local coding to broader development tasks? | Published / Evaluation |
| ASE2025UserPerception | [Demystifying Users' Perception on AI Coding Assistants](https://conf.researchr.org/track/ase-2025/ase-2025-papers) | 2025 | ASE Research Papers / official program | Which benefits, failures, and trust signals do users perceive? | Published / Evaluation |
| FSE2026PatchAccountability | [Who Wrote This Patch? Toward Accountable Automated Program Repair](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Ideas/Visions/Reflections / official program | Who owns and explains an agent-generated patch? | Position / Agenda |

## Human-System Interaction Model

| Stage | Human work | Common failure | Evidence to collect |
| --- | --- | --- | --- |
| Task framing | state intent, constraints, and acceptance criteria | underspecified goals become plausible but wrong code | original issue, clarifications, prompt changes |
| Context selection | expose files, docs, histories, and tools | missing or excessive context | retrieved artifacts and rejected context |
| Generation/action | supervise edits and commands | silent state drift or unsafe assumptions | full trajectory, permissions, tool output |
| Verification | inspect tests, analysis, performance, and proof | automation bias or circular generated tests | independent checks and uncertainty |
| Review | assess design fit and maintainability | review overload from large/opaque diffs | review time, comments, rework, acceptance |
| Handoff | assign ownership and future maintenance | no accountable author or rationale | provenance, explanation, responsible owner |
| Recovery | roll back, retry, or escalate | repeated unproductive loops | stop rules, rollback record, escalation reason |

## Study Design Checklist

- report participant experience, language/ecosystem familiarity, and prior tool use;
- separate coding, debugging, comprehension, review, and repository tasks;
- measure correctness and maintainability alongside speed and self-reported satisfaction;
- count prompt/context preparation, waiting, review, rework, and abandoned attempts;
- record model/version, interface, autocomplete versus chat versus agent mode, and tool permissions;
- use counterbalanced tasks and report uncertainty, not only average improvement;
- evaluate delayed comprehension and future modification where feasible;
- disclose organizational incentives and whether participants could opt out.

## Research Questions

- Which uncertainty displays help developers calibrate trust without producing alert fatigue?
- When should an agent ask for clarification rather than infer intent?
- How does reviewing generated code differ from reviewing human code of the same quality?
- Which provenance is necessary for accountable code ownership and licensing?
- How should expertise and domain familiarity change autonomy and approval settings?
- Do gains persist when teams maintain the generated change months later?
- How do agent tools affect code review, onboarding, mentoring, and division of labor?
- Which accessibility benefits and participation barriers emerge across languages and regions?

## Practical Position

Treat productivity as a system outcome:

`useful throughput = accepted work − verification cost − rework − future maintenance burden`

No single benchmark or vendor survey can estimate every term. Combine controlled studies, field telemetry, artifact quality, and longitudinal maintenance evidence.
