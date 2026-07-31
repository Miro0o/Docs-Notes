---
ai-generated: true
last-reviewed: 2026-07-30
---

# Human Factor

Home: [Software-For-LLM-Agent-Systems-Research-Dossier-2026.md](Software-For-LLM-Agent-Systems-Research-Dossier-2026.md)

Scope: how people design, understand, debug, supervise, approve, and remain accountable for LLM-integrated applications and agents. Product telemetry and standards signals live in [Non-Academic Status](Non-Academic-Status.md).

## Current Synthesis

The engineering work shifts from writing deterministic implementations toward specifying behavior, assembling model/tool components, curating examples, diagnosing stochastic traces, and deciding when to accept, retry, escalate, or roll back. This does not remove programming work; it redistributes it across abstractions, evaluation data, observability, and operational control.

The evidence base remains small. MTP reports an encouraging language-level developer study, while the FSE prompt-programming study shows that even experienced prompt developers struggle to form stable mental models. These findings are complementary: an abstraction may reduce local code and time while the underlying behavioral uncertainty still creates debugging and maintenance work.

## Peer-Reviewed Anchors

- [Prompts Are Programs Too!](Academic-Status/Architecture-Evolution-And-Operations.md) is canonical under architecture and asks how developers reason about and iteratively construct prompt-powered software.
- [MTP](Academic-Status/Languages-DSLs-And-Programming-Models.md) is canonical under languages and includes a developer study of a meaning-typed integration abstraction.
- [TheAgentCompany](Academic-Status/Benchmarks-And-Surveys.md) is canonical under benchmarks and supplies workplace-task context; it is not a human-productivity experiment.

## Human-Control Model

| Stage | Human responsibility | Failure to study | Evidence |
| --- | --- | --- | --- |
| Intent/specification | state goals, constraints, and forbidden outcomes | natural-language ambiguity becomes latent behavior | original requirement and clarification history |
| Composition | select models, tools, memory, evaluators, and roles | hidden coupling and incompatible assumptions | architecture and configuration |
| Calibration | create examples, prompts, tests, and thresholds | overfitting to a narrow golden set | evaluation-set provenance and revisions |
| Supervision | approve actions and respond to uncertainty | approval fatigue or automation bias | decision events and rejected actions |
| Diagnosis | interpret traces and test hypotheses | plausible but false causal stories | replay and intervention results |
| Release | accept risk and choose rollout/rollback policy | no accountable owner | release decision and responsible role |
| Maintenance | adapt to model, API, data, and tool drift | undocumented behavioral regression | versions, regression results, incident history |

## Study Design Checklist

- distinguish professional developers, prompt specialists, domain experts, and end-user software makers;
- report prior experience with the models, tools, and target domain;
- compare equivalent functionality and verification standards;
- measure specification, debugging, review, and maintenance effort in addition to initial implementation;
- log model/version, language/framework, prompts, tools, and autonomy settings;
- separate perceived usability from task quality and operational reliability;
- include delayed modification or handoff tasks;
- study error detection, trust calibration, and appropriate abstention;
- disclose whether participants can inspect and override compiled prompts or runtime choices.

## Research Questions

- Which abstractions produce accurate mental models of probabilistic program behavior?
- When should a language surface model uncertainty or hide provider details?
- How should tools explain compiled prompts, routing, and runtime rewrites?
- Which approval boundaries avoid both unsafe autonomy and approval fatigue?
- Can trace visualizations support causal diagnosis rather than post hoc storytelling?
- How do teams review and own prompt programs and agent configurations?
- What documentation and provenance survive model/provider migration?
- How do non-programmer software makers safely participate without becoming nominally accountable for opaque systems?

## Practical Position

Evaluate an abstraction as a human-software system:

`engineering value = delivered behavior − specification effort − diagnosis/review cost − operational risk − future evolution cost`

Shorter code is useful evidence, but it is not a complete measure of engineerability.
