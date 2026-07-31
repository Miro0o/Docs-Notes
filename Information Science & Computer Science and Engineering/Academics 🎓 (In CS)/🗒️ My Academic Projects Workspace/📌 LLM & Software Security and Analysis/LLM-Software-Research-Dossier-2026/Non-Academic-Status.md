---
ai-generated: true
last-reviewed: 2026-07-30
---

# Non-Academic Status

Home: [LLM-Software-Research-Dossier-2026.md](LLM-Software-Research-Dossier-2026.md)

Scope: industry field studies, developer surveys, product and platform measurements, practitioner reports, and deployment signals about LLM-assisted software work. These sources are useful for timeliness and scale but are not substitutes for peer-reviewed causal or correctness evidence.

## Current Position

LLM coding products have shifted from completion and chat toward repository-aware agents that search, edit, run commands, execute tests, and open change proposals. Product capability moves faster than the academic publication cycle, but vendor success rates are difficult to compare because models, scaffolds, task selection, network access, and human intervention differ.

The most important non-academic tension is between perceived speed and measured end-to-end work. Developers often report convenience and local acceleration, while controlled or field evidence can show substantial verification and integration costs. Both can be true for different tasks and users.

## Evidence Signals

| Signal | Date | Source type | What it contributes | Main caution |
| --- | ---: | --- | --- | --- |
| [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | 2025 | METR randomized study/report | Measures end-to-end task time for experienced developers working in familiar repositories. | Limited task/user/tool setting; update conclusions as tools change. |
| [2025 Stack Overflow Developer Survey: AI](https://survey.stackoverflow.co/2025/ai) | 2025 | Large developer survey | Tracks adoption, sentiment, trust, and perceived accuracy. | Self-report and respondent-selection bias; not a causal productivity estimate. |
| [DORA research program](https://dora.dev/research/) | 2024-2026 | Industry research and reports | Connects AI adoption to delivery, organizational, and developer-experience outcomes. | Organizational correlations require cautious causal interpretation. |
| [Anthropic Economic Index](https://www.anthropic.com/economic-index) | 2025-2026 | Provider usage analysis | Shows how coding and software tasks appear in real model usage. | One provider's visibility; task labels and customer mix shape results. |
| [SWE-bench leaderboards](https://www.swebench.com/) | current | Community benchmark | Rapid signal on model-agent systems and repository issue resolution. | Scores depend on benchmark version, scaffold, cost, and contamination. |
| [GitHub Copilot research](https://github.com/features/copilot) | current | Vendor product/research portal | Product capabilities and vendor-reported developer evidence. | Marketing and product evidence must be separated from independent replication. |

## Product-Capability Checklist

When recording an agent or coding-assistant claim, capture:

- product and model version;
- date of observation;
- completion, chat, edit, or autonomous-agent mode;
- repository indexing and retrieval behavior;
- shell, browser, package-manager, and network access;
- sandbox and approval policy;
- test/build execution;
- human intervention;
- task selection and excluded failures;
- token, time, and price budget;
- artifact or patch availability.

## Industry Evidence Hierarchy

1. Reproducible public task, environment, trajectory, and accepted patch.
2. Controlled field experiment with transparent sampling and outcome definitions.
3. Independently audited deployment measurement.
4. Large survey with questionnaire and sampling details.
5. Vendor telemetry with disclosed denominators and failure handling.
6. Product demo, anecdote, or marketing claim.

Lower levels remain useful as watch signals but should not support strong causal or reliability claims.

## Practitioner Adoption Questions

- Does the tool reduce cycle time after review and rework?
- Does code quality hold under hidden tests, static analysis, and later changes?
- Who is accountable for generated dependencies, licenses, and design decisions?
- Can teams reproduce the agent's environment and reasoning trail?
- Are permissions least-privileged and are actions reversible?
- How are secrets, proprietary code, and telemetry handled?
- What happens when the model or product version changes?
- Can an organization measure downstream maintenance and incident impact?

## Watchlist

- verified repository-agent patches rather than headline leaderboard movement;
- benchmarks with continuously refreshed tasks and reproducible containers;
- production optimization evidence comparable to OSDI 2026 ECO;
- code-review workload and defect-escape measurements;
- regional and language-specific developer studies;
- changes in pricing, context limits, tool permissions, and data-retention policy;
- evidence of durable maintenance outcomes six to twelve months after generation.

## Boundary

Security incident reports, vulnerability discovery products, autonomous pentesting, and secure-coding attack surfaces belong in the sibling [LLM Software Security Research Dossier](../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md).
