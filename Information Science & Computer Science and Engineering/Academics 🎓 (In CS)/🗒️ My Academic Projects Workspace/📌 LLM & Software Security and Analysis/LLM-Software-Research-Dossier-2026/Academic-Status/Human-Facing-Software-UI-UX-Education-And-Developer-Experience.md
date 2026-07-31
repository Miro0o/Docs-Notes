---
ai-generated: true
last-reviewed: 2026-07-30
---

# Human-Facing Software, UI/UX, Education, and Developer Experience

Back: [Academic Status](Academic-Status.md)

Scope: multimodal and visual software engineering, UI-to-code, usability analysis, video-grounded bug work, software-engineering education, and empirical evidence about how people frame, learn, review, and collaborate with LLM-assisted software systems. The cross-cutting synthesis remains in [Human Factor](../Human-Factor.md).

## Status

Human-facing software is not reducible to token-level code generation. A model must connect screenshots, layout, interaction state, video, accessibility, task intent, and user expectations to executable behavior. At the same time, developer studies show that useful assistance depends on clarification, team norms, expertise, review, and learning—not only model accuracy.

## UI, UX, and Multimodal Software

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Wu2025UI2Code | [MLLM-Based UI2Code Automation Guided by UI Layout Information](https://conf.researchr.org/track/issta-2025/issta-2025-papers) | 2025 | ISSTA Research Papers / official program | Uses inferred layout structure to guide code generation from webpage images. | Official program |
| He2026ReFLAIR | [ReFLAIR: Detecting Responsive Layout Reflow Issues using Multimodal Generative AI](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Detects responsive-layout and reflow failures with multimodal evidence. | Official program |
| Lubos2026Usability | [Recommending Usability Improvements with Multimodal Large Language Models](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Studies multimodal recommendations for concrete usability improvements. | Official program |
| Feng2026ViBR | [ViBR: Automated Bug Replay from Video-based Reports Using Vision-Language Models](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Converts video bug reports into replayable interaction evidence. | Official program |
| Peng2026PlayCoder | [PlayCoder: Making LLM-Generated GUI Code Playable](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Targets executable, interactive behavior rather than screenshot similarity alone. | Official program |
| Aggarwal2026ProgrammingPixels | [Programming with Pixels: Can Computer-Use Agents do Software Engineering?](https://iclr.cc/virtual/2026/poster/10011120) | 2026 | ICLR Poster / official record | Evaluates agents that visually operate an IDE and compares visual interaction with direct software-tool APIs. | Published / Evaluation |

## Education, Collaboration, and Developer Experience

| Key | Paper | Year | Venue / evidence | Human question | Label |
| --- | --- | ---: | --- | --- | --- |
| Vijayvargiya2026Underspecificity | [Interactive Agents to Overcome Underspecificity in Software Engineering](https://iclr.cc/virtual/2026/poster/10009007) | 2026 | ICLR Poster / official record | Can an agent detect missing information, ask a targeted question, and use the answer? | Published / Evaluation |
| Kumar2025DeveloperAgentCollaboration | [Why AI Agents Still Need You: Findings from Developer-Agent Collaborations in the Wild](https://conf.researchr.org/track/ase-2025/ase-2025-papers) | 2025 | ASE Research Papers / official program | Where and why do deployed coding agents still require developer intervention? | Official program / Evaluation |
| Welter2025PairProgrammingTransfer | [An Empirical Study of Knowledge Transfer in AI Pair Programming](https://conf.researchr.org/track/ase-2025/ase-2025-papers) | 2025 | ASE Research Papers / official program | Does working with an AI partner transfer knowledge to the developer? | Official program / Evaluation |
| Miller2026TeamDrivers | [“Maybe We Need Some More Examples:” Individual and Team Drivers of Developer GenAI Tool Use](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program; Distinguished Paper | How do individual and team conditions shape adoption and use? | Official program / Evaluation |
| Sergeyuk2026DeveloperLogs | [Evolving with AI: A Longitudinal Analysis of Developer Logs](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | How does developer behavior change over time rather than in a one-session study? | Official program / Evaluation |
| Yang2026TestingEducation | [Large Language Models for Software Testing Education: an Experience Report](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Software Engineering Education / official program | What changes when LLM assistance is integrated into software-testing instruction? | Official program / Experience |
| Wang2026GenAICourse | [From Specifications to Implementation in the Gen-AI Era: Lessons from a Project-based Software Engineering Course](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | How should project-based courses preserve specification, design, and implementation learning? | Official program / Education |

## Evaluation Checklist

- evaluate interaction state and behavior, not only screenshot or text similarity;
- preserve viewport, platform, accessibility, and device context for UI claims;
- record whether agents receive visual-only access or direct file, shell, and IDE APIs;
- measure clarification quality and downstream benefit, including unnecessary questions;
- report participant experience, team setting, prior tool use, and task authenticity;
- measure learning retention, review cost, maintainability, and future task performance;
- separate a completed deliverable from demonstrated understanding.

## Boundary Notes

This page owns human-facing software and use of LLMs in software-engineering work or education. It does not own attacks on visual agents, privacy leakage, deceptive interfaces, or other security-first claims; those remain in the [security dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md).

## Research Gaps

- executable and accessibility-aware UI oracles beyond pixel similarity;
- multimodal requirements that preserve interaction state across long workflows;
- longitudinal evidence on skill formation, deskilling, and knowledge transfer;
- team-level studies that include review, ownership, and coordination costs;
- inclusive evaluation across disability, language, geography, and experience;
- principled autonomy settings that adapt to task ambiguity and developer expertise.
