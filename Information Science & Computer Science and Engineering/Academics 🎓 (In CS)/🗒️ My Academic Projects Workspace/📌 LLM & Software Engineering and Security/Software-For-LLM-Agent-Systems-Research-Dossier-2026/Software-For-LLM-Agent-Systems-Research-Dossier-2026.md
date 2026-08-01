---
ai-generated: true
last-reviewed: 2026-07-31
---

# Software for LLM and Agent Systems Research Dossier 2026

Date: 2026-07-31

Scope: 2024-present research that applies programming-languages, software-engineering, and systems ideas to the construction of LLM-integrated applications and agent systems. The object being engineered is the LLM application, prompt program, tool-using agent, multi-agent workflow, or its supporting runtime—not ordinary source code produced by an LLM.

## Boundary

This dossier covers the inverse direction often called `SE4FM`, `software for LLMs`, `AIware engineering`, or `agentware engineering`:

- languages, DSLs, programming models, and intermediate representations for LLM applications;
- compilers, runtimes, schedulers, and declarative orchestration for model-and-tool workflows;
- types, contracts, grammars, protocols, and structured agent interaction;
- testing, debugging, tracing, observability, and failure attribution for agent systems;
- architecture, lifecycle, evolution, deployment, and operational practices for LLM-integrated software;
- benchmarks and surveys that evaluate these software abstractions and engineering processes.

It excludes:

- using an LLM to generate, analyze, repair, test, verify, optimize, or maintain ordinary software; use [LLM Software Research Dossier 2026](../LLM-Software-Research-Dossier-2026/LLM-Software-Research-Dossier-2026.md);
- code-specific model training, adaptation data, and learned code representations whose outcome is software capability; use the [code-model shelf](../LLM-Software-Research-Dossier-2026/Academic-Status/Code-Model-Training-Adaptation-Data-And-Representation.md);
- vulnerability discovery, attacks, security-first testing, secure-code generation, or security-first agent research; use [LLM Software Security Research Dossier 2026](../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md);
- generic model training, inference serving, KV-cache management, and hardware scheduling unless the primary scientific contribution exposes a programming abstraction or optimizes an application-level agent workflow;
- papers about model capability alone without a reusable software abstraction, engineering method, or systems contribution.

A paper receives one canonical shelf. Cross-topic pages link to it rather than repeating the full record.

## Executive Snapshot

LLM applications are becoming programs with probabilistic components rather than collections of prompt strings. The strongest work makes their structure explicit: declarative modules, typed or meaning-bearing interfaces, control flow, dataflow, grammars, tool schemas, traces, and replayable trajectories.

Four trends stand out. First, language design is moving above raw API calls: DSPy, MTP, APPL, Opportunistically Parallel Lambda Calculus, and the foundational LMQL line treat prompts, model invocations, and expensive external calls as programmable objects with increasingly explicit semantics. Second, systems work is using exposed workflow and program structure to optimize whole applications: SGLang, Parrot, Murakkab, and Agentix couple programming abstractions or program-level context with specialized runtimes. Third, testing is moving from final-answer scoring toward trajectory diagnosis and active intervention: Watson, DoVer, AgenTracer, and accepted ISSTA 2026 work make agent failures observable and testable. Fourth, agent organization is becoming an evolvable architecture: EvoMAC adapts collaboration networks, while DEI manages collectives of heterogeneous software-engineering agents.

The field is still immature. Many evaluations conflate model quality with framework quality; swap models without controlling prompts or tools; omit failure taxonomies; and report average task success without reproducible traces, cost, variance, or recovery behavior.

## Dossier Map

- [Academic Status](Academic-Status/Academic-Status.md): synthesis, labels, taxonomy, venue coverage, and research gaps.
- [Trends and Research Frontiers](Trends-And-Research-Frontiers.md): cross-cutting trajectory and high-value open problems without duplicate paper records.
- [Languages, DSLs, and Programming Models](Academic-Status/Languages-DSLs-And-Programming-Models.md)
- [Compilers, Runtimes, and Workflow Orchestration](Academic-Status/Compilers-Runtimes-And-Workflow-Orchestration.md)
- [Types, Contracts, and Structured Interaction](Academic-Status/Types-Contracts-And-Structured-Interaction.md)
- [Testing, Debugging, and Observability](Academic-Status/Testing-Debugging-And-Observability.md)
- [Architecture, Evolution, and Operations](Academic-Status/Architecture-Evolution-And-Operations.md)
- [Benchmarks and Surveys](Academic-Status/Benchmarks-And-Surveys.md)
- [Shared Human Factor](../LLM-Software-Security-Research-Dossier-2026/Human-Factor.md): how people and organizations design, test, inspect, operate, secure, supervise, and remain accountable for LLM-integrated software and agent systems.
- [Non-Academic Status](Non-Academic-Status.md): standards, open protocols, frameworks, and practitioner signals.
- [Canonical Corpus Map](Canonical-Corpus-Map.md): generated formal-venue, frontier-preprint, and supplementary rows with one canonical mapping per record.
- [Mapped BibTeX](Software-For-LLM-Agent-Systems-Research-Dossier-2026.bib): every record assigned to this dossier, with preserved supplementary material.
- [Shared Literature Corpus](../Literature-Corpus/README.md): exhaustive formal-venue source corpus, manifest, screening decisions, cross-dossier mappings, and reproducible build scripts.

## Canonical Taxonomy

| Canonical shelf | Owns | Does not own |
| --- | --- | --- |
| Languages, DSLs, and programming models | syntax and semantics for model calls, prompt programs, agent actions, and declarative LM pipelines | ordinary code generation by an LLM |
| Compilers, runtimes, and orchestration | compilation, dataflow optimization, caching, parallelism, placement, and SLO-aware execution of explicit workflows | generic inference engines with no application abstraction |
| Types, contracts, and structured interaction | output grammars, schemas, protocol representations, semantic interfaces, and interaction constraints | security policies whose primary claim is attack resistance |
| Testing, debugging, and observability | framework testing, trajectory tracing, failure attribution, replay, intervention, and behavioral diagnosis | LLM-generated tests for ordinary software |
| Architecture, evolution, and operations | reference architectures, agent roles and collaboration topology, prompt lifecycle, component evolution, deployment, and AIware engineering practices | model architecture research or training recipes |
| Benchmarks and surveys | evaluation environments, reliability metrics, methodological syntheses, and field maps | duplicate descriptions of primary systems |

## Research Dashboard

| Layer | Current direction | Evidence to prefer |
| --- | --- | --- |
| Programming abstraction | From template strings toward declarative modules, language constructs, and programmable agent actions. | expressiveness, semantics, maintainability, and controlled developer studies |
| Compilation/runtime | From per-request serving toward whole-workflow dataflow, first-class agent programs, and cross-layer optimization. | end-to-end latency, program throughput, cost, energy, fairness, and output-quality constraints |
| Interfaces/contracts | From best-effort parsing toward grammar-constrained outputs and interoperable trajectory/action formats. | coverage of real schemas, conformance, overhead, and failure behavior |
| Testing/debugging | From final-answer inspection toward replay, counterfactual intervention, and component-level attribution. | seeded and natural failures, diagnosis accuracy, repair success, and reproducible traces |
| Architecture/lifecycle | From ad hoc prompt files and fixed agent roles toward versioned components, adaptive collectives, reference architectures, and release/rollback practices. | controlled topology/membership changes, compute budgets, longitudinal drift, incidents, and maintenance cost |
| Evaluation | From static success rate toward progress, consistency, state correctness, policy compliance, and long-horizon recovery. | executable environments, repeated trials, partial credit, and version-pinned artifacts |

## Reading Route

1. Start with [Trends and Research Frontiers](Trends-And-Research-Frontiers.md) for the cross-cutting map, then [Benchmarks and Surveys](Academic-Status/Benchmarks-And-Surveys.md) for evaluation limits.
2. Read [Languages, DSLs, and Programming Models](Academic-Status/Languages-DSLs-And-Programming-Models.md): LMQL, DSPy, MTP, Opportunistically Parallel Lambda Calculus, and APPL.
3. Continue with [Types, Contracts, and Structured Interaction](Academic-Status/Types-Contracts-And-Structured-Interaction.md): DOMINO, XGrammar, and Agent Data Protocol.
4. Read [Compilers, Runtimes, and Workflow Orchestration](Academic-Status/Compilers-Runtimes-And-Workflow-Orchestration.md): SGLang, Parrot, Murakkab, and Agentix.
5. Read [Testing, Debugging, and Observability](Academic-Status/Testing-Debugging-And-Observability.md): Watson, DoVer, AgenTracer, and ISSTA 2026 accepted work.
6. Finish with [Architecture, Evolution, and Operations](Academic-Status/Architecture-Evolution-And-Operations.md), including EvoMAC and DEI, then the [shared Human Factor](../LLM-Software-Security-Research-Dossier-2026/Human-Factor.md) and [Non-Academic Status](Non-Academic-Status.md).

## Bibliographic Policy

The [BibTeX file](Software-For-LLM-Agent-Systems-Research-Dossier-2026.bib) contains every record assigned to this dossier by the frozen [shared corpus](../Literature-Corpus/README.md), plus clearly labeled supplementary records retained from the earlier dossier. The [canonical corpus map](Canonical-Corpus-Map.md) is the row-level audit index; topic pages are the interpreted reading route. `Published` requires proceedings or DOI evidence. Official accepted-paper pages justify `Accepted`, not invented page or DOI metadata. Preprints remain `Frontier` even when influential. Foundational pre-2024 work is separated from the 2024-present core.

## Current Thesis

Agent systems become engineerable when their implicit prompt-and-tool behavior is turned into explicit software structure that can be compiled, constrained, observed, replayed, tested, and evolved.
