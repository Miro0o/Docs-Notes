---
ai-generated: true
last-reviewed: 2026-07-30
---

# Testing, Debugging, and Observability

Back: [Academic Status](Academic-Status.md)

Scope: analysis and testing of LLM applications and agent systems, including framework testing, trajectory observability, failure attribution, counterfactual replay, and intervention-driven debugging.

## Status

Agent failures are distributed across prompts, models, memories, tools, orchestration, environment state, and interactions between agents. Final-answer logs are insufficient. The strongest new methods preserve trajectories, test counterfactual hypotheses, or intervene on messages and plans to distinguish plausible explanations from repairs that actually change outcomes.

ISSTA 2026 makes the directional distinction explicit in its official call: “AI for Analysis and Testing” is separate from “Analysis and Testing for AI,” including testing and analysis of agents and agentic systems.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Rombaut2025Watson | [Watson: A Cognitive Observability Framework for the Reasoning of LLM-Powered Agents](https://doi.org/10.1109/ASE63991.2025.00067) | 2025 | ASE / DOI | Adds cognitive/reasoning observability to conventional operational traces and evaluates diagnostic utility on agentware. | Published |
| Ma2026DoVer | [DoVer: Intervention-Driven Auto Debugging for LLM Multi-Agent Systems](https://iclr.cc/virtual/2026/poster/10007537) | 2026 | ICLR / official poster | Generates failure hypotheses and actively verifies them through targeted interventions; evaluates resolved failures and milestone progress. | Published |
| Zhang2026AgenTracer | [AgenTracer: Who Is Inducing Failure in the LLM Agentic Systems?](https://iclr.cc/virtual/2026/poster/10007726) | 2026 | ICLR / official poster | Builds failure-attribution data through counterfactual replay and fault injection, then trains a lightweight failure tracer. | Published |
| Long2026LogicHunter | [LogicHunter: Testing LLM Agent Frameworks with an Agentic Oracle](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers) | 2026 | ISSTA Research Papers / official accepted list; conference forthcoming | Accepted framework-testing work using an agentic oracle; contribution details should be normalized after proceedings. | Accepted |
| Manke2026AgentInspect | [AgentInspect: Diagnosing Behavioral Failures in Artificial Intelligence Agents](https://conf.researchr.org/track/issta-2026/issta-2026-research-papers) | 2026 | ISSTA Research Papers / official accepted list; conference forthcoming | Accepted behavioral-failure diagnosis work; DOI/pages and detailed claims are intentionally deferred. | Accepted |

## Failure Model

| Fault location | Examples | Useful evidence |
| --- | --- | --- |
| Prompt/program | ambiguous instruction, stale template, hidden coupling | prompt diff, version, expanded input |
| Model | reasoning error, nondeterminism, refusal, context loss | model/version, sampling, repeated trials |
| Memory/retrieval | irrelevant, missing, stale, or conflicting context | retrieved items, scores, write/read history |
| Tool interface | invalid arguments, schema mismatch, tool hallucination | structured call, validator result, tool version |
| Tool/environment | timeout, partial failure, stale external state | external logs, state snapshot, idempotency record |
| Orchestration | wrong order, role confusion, loop, premature termination | causal trace, scheduler decisions, message graph |
| Multi-agent interaction | error propagation, conflicting beliefs, coordination failure | sender/receiver identity, message lineage, replay |
| Human handoff | unclear approval, rejected escalation, misleading explanation | approval event, rationale, responsibility owner |

## Evaluation Checklist

- distinguish natural failures from synthetic fault injection;
- define whether ground truth identifies a faulty component, step, cause, or effective repair;
- record full model, prompt, tool, and environment versions;
- report diagnosis precision/recall and downstream repair/progress separately;
- measure false interventions and regressions introduced by a repair;
- use repeated runs because the same configuration may fail differently;
- include trace storage and instrumentation overhead;
- compare log-only, replay, counterfactual, and active-intervention baselines;
- release failure trajectories with privacy-preserving redaction where possible.

## Research Directions

- causal fault localization for interacting probabilistic components;
- metamorphic tests for invariants that survive model/provider changes;
- differential testing across agent frameworks and orchestration policies;
- coverage criteria over states, tools, roles, and interaction protocols;
- runtime verification of temporal and effect contracts;
- flaky-agent diagnosis and probabilistic regression testing;
- test minimization and failure-preserving trajectory reduction;
- observability schemas that connect traces to source-level prompt programs;
- automated repair with independent validation and rollback.

## Boundary

Testing an agent framework belongs here. Asking an LLM to generate tests for Java, Python, compilers, or libraries belongs in the LLM-for-software dossier. Prompt injection, exploit chains, and security-first agent testing belong in the security dossier.
