---
ai-generated: true
last-reviewed: 2026-07-30
---

# Cyber Operations: Defensive SOC, Incident Response, And CTI

Back: [Academic Status](../Academic-Status.md)

Scope: analyst-facing SOC systems, threat-intelligence extraction, alert and incident reasoning, detection-rule authoring, autonomous cyber defense, and attacks against LLM-driven operational tooling.

Checked: 2026-07-30. Human-workflow evidence is maintained in [Human Factor](../../Human-Factor.md); benchmark papers are indexed in [Security Benchmarks And Evaluation](../Cross-Cutting/Security-Benchmarks-And-Evaluation.md).

## Analyst Support, Detection Engineering, And Response

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Mustafa2026LLMSOC | [LLMs in the SOC: An Empirical Study of Human-AI Collaboration in Security Operations Centres](https://sp2026.ieee-security.org/accepted-papers.html) | 2026 | IEEE S&P | SOC collaboration | Studies LLM use with analysts in operational security work. | Accepted/program record |
| Aly2025OCRAPT | [OCR-APT: Reconstructing APT Stories from Audit Logs using Subgraph Anomaly Detection and LLMs](https://dblp.org/rec/conf/ccs/Aly0Y25) | 2025 | ACM CCS / DBLP | Incident reconstruction | Combines graph anomalies and LLM reasoning to reconstruct attack stories. | Core |
| Kiely2025CAGE | [Exploring the Efficacy of Multi-Agent Reinforcement Learning for Autonomous Cyber Defence: A CAGE Challenge 4 Perspective](https://dblp.org/rec/conf/aaai/KielyABBBBCDDEF25) | 2025 | AAAI / DBLP | Autonomous defense | Evaluates multi-agent cyber defense in a controlled challenge setting. | Core |
| IncidentResponse2026 | [Incident Response Planning Using a Lightweight Large Language Model with Reduced Hallucination](https://doi.org/10.14722/ndss.2026.240358) | 2026 | NDSS | Incident-response planning | Uses a lightweight model and explicit hallucination reduction for response plans. | Core |
| Wang2026RulePilot | [RulePilot: An LLM-Powered Agent for Security Rule Generation](https://doi.org/10.1145/3744916.3773249) | 2026 | ICSE | Detection engineering | Generates and converts executable detection rules through a structured intermediate representation. | Core |
| Cai2026SIGMERGE | [From Texts to Rules: Generating Sigma Rules with Large Language Models from Cyber Threat Reports](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) | 2026 | USENIX Security | Detection engineering | Converts threat-report semantics into validated Sigma rules through an intermediate layer. | Accepted/program record |
| 2603.25930 | [AVDA: Autonomous Vibe Detection Authoring for Cybersecurity](https://arxiv.org/abs/2603.25930) | 2026 | arXiv | Detection authoring | Automates iterative detection-engineering workflows. | Frontier |
| 2603.23966 | [Policy-Guided Threat Hunting: An LLM enabled Framework with Splunk SOC Triage](https://arxiv.org/abs/2603.23966) | 2026 | arXiv | Threat hunting | Applies policy constraints to LLM-assisted SOC triage. | Frontier |

## Security Of AI-Driven Operations

| Key | Paper | Year | Source | Security role | Contribution | Label |
| --- | --- | ---: | --- | --- | --- | --- |
| Karanjai2026LogInject | [Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation](https://www.usenix.org/conference/usenixsecurity26/presentation/karanjai) | 2026 | USENIX Security | Log-analysis poisoning | Demonstrates passive prompt injection through attacker-influenced log context and evaluates defenses. | Accepted/program record |
| Pasquini2026AIOpsDoom | [When AIOps Become “AI Oops”: Subverting LLM-driven IT Operations via Telemetry Manipulation](https://www.usenix.org/conference/usenixsecurity26/technical-sessions) | 2026 | USENIX Security | AIOps security | Shows telemetry manipulation can steer remediation agents and evaluates structured sanitization. | Accepted/program record |

## Operational Reading Rules

- Treat model summaries as hypotheses; retain source events, graph edges, queries, rule syntax, and analyst decisions.
- Measure false positives, missed incidents, time-to-decision, confidence calibration, escalation, and operator workload.
- Keep tool permissions, write actions, rollback, and approval paths explicit.
