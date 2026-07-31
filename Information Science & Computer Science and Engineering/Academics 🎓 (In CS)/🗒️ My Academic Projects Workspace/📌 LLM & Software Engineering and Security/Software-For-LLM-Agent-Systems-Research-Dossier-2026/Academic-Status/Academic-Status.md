---
ai-generated: true
last-reviewed: 2026-07-31
---

# Academic Status: Software for LLM and Agent Systems

Date: 2026-07-31

Home: [Software-For-LLM-Agent-Systems-Research-Dossier-2026.md](../Software-For-LLM-Agent-Systems-Research-Dossier-2026.md)

This hub summarizes PL, SE, and systems research for constructing LLM-integrated applications and agents. Full records live on one canonical topic page each.

Cross-cutting synthesis: [Trends and Research Frontiers](../Trends-And-Research-Frontiers.md).

## Evidence Labels

- `Published`: DOI or official proceedings record exists.
- `Official program`: an official conference program confirms the work, but normalized proceedings metadata is not recorded here.
- `Accepted`: an official accepted-paper page confirms acceptance; final proceedings metadata may be pending.
- `Frontier`: public preprint without verified peer-reviewed publication.
- `Foundational`: pre-2024 work retained to explain the research lineage, outside the 2024-present core count.
- `Benchmark`, `Survey`, `Human study`, and `Systems`: evidence-role qualifiers, not publication statuses.

The inclusion test is artifact-first: the work must contribute a language, programming abstraction, runtime, protocol, engineering method, diagnostic technique, architecture, or evaluation system for LLM applications or agents.

## Direction Test

| Primary question | Destination |
| --- | --- |
| Can an LLM improve ordinary software or code? | [LLM Software Research Dossier](../../LLM-Software-Research-Dossier-2026/LLM-Software-Research-Dossier-2026.md) |
| Is the primary artifact a code-specific model, corpus/recipe, adaptation method, or learned code representation? | [Code-Model Training, Adaptation, Data, and Representation](../../LLM-Software-Research-Dossier-2026/Academic-Status/Code-Model-Training-Adaptation-Data-And-Representation.md) |
| Can an LLM attack, defend, or analyze software security, or is the agent-security property primary? | [LLM Software Security Research Dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md) |
| Can PL, SE, or systems techniques make an LLM application or agent more programmable, testable, maintainable, interoperable, or efficient? | This dossier |
| Is the main result only generic non-code model training or generic inference throughput? | Outside all three unless a software/workflow abstraction is primary |

## Area Map

| Area | Primary question | Representative anchors | File |
| --- | --- | --- | --- |
| Languages and DSLs | What should it mean to program an LLM application or agent? | DSPy, MTP, Opportunistically Parallel Lambda Calculus, APPL; LMQL as foundation. | [Languages, DSLs, and Programming Models](Languages-DSLs-And-Programming-Models.md) |
| Compilers and runtimes | How can explicit workflow and program structure support whole-application optimization? | SGLang, Parrot, Murakkab, Agentix. | [Compilers, Runtimes, and Workflow Orchestration](Compilers-Runtimes-And-Workflow-Orchestration.md) |
| Types and contracts | How can interfaces constrain outputs and normalize interactions? | DOMINO, XGrammar, Agent Data Protocol. | [Types, Contracts, and Structured Interaction](Types-Contracts-And-Structured-Interaction.md) |
| Testing and diagnosis | How can failures be reproduced, localized, attributed, and repaired? | Watson, DoVer, AgenTracer, LogicHunter. | [Testing, Debugging, and Observability](Testing-Debugging-And-Observability.md) |
| Architecture and lifecycle | How should promptware, agent roles, collectives, and operational components be structured and evolved? | Prompts Are Programs Too, EvoMAC, DEI, reference architecture, ICSE-SEIP field study. | [Architecture, Evolution, and Operations](Architecture-Evolution-And-Operations.md) |
| Evaluation and synthesis | Which environments and metrics separate model, framework, and workflow quality? | AgentBoard, τ-bench, ITBench, TheAgentCompany. | [Benchmarks and Surveys](Benchmarks-And-Surveys.md) |

## Current Status

The field has moved beyond prompt templates but has not converged on one abstraction. PL work explores query languages, declarative signatures, meaning-typed invocation, Python-integrated prompt languages, and formal evaluation strategies for expensive external calls. Systems work exploits application structure for caching, parallelism, placement, program-aware scheduling, and SLO-aware orchestration. Agent architecture work now treats collaboration networks and heterogeneous collectives as configurable or evolvable artifacts. SE work is only beginning to establish mature testing, observability, release, and evolution practices.

Evaluation remains the weakest shared layer. A framework can appear better because it uses a stronger model, receives more tokens, retries more often, or has a more permissive environment. Repeated trials, cost budgets, trajectory logs, explicit state checks, and controlled model/framework ablations are therefore necessary.

## Agenda Signal: LMPL 2026

[LMPL 2026](https://conf.researchr.org/home/splash-issta-2026/lmpl-2026) is a workshop agenda and call for papers, not a publication corpus or evidence that any particular contribution has been accepted. Its official scope makes the direction boundary explicit:

- `LLMs for PL tasks` includes LLM-driven analysis, verification, optimization, code generation, repair, and testing; those non-security papers belong in the LLM-for-software dossier.
- `PL techniques for LLM applications` includes harness engineering and agent design; those papers belong in this software-for-LLM-and-agent-systems dossier when the programming or engineering artifact is primary.
- security-first attacks, defenses, and secure-code work still route to the security dossier regardless of workshop category.

The agenda validates the need to track both directions separately; it does not replace paper-level classification by primary artifact and claim.

## Venue-Coverage Ledger

| Community | Target venues | Verified coverage in this snapshot | Next check |
| --- | --- | --- | --- |
| PL | POPL, PLDI, OOPSLA/PACMPL, ICFP/PACMPL | Every available 2024–2026 archival record is in the shared source corpus; foundational LMQL remains supplementary. | OOPSLA 2026 is pending; normalize final 2026 program records. |
| AI/ML | ICLR, ICML, NeurIPS, AAAI | Every available 2024–2026 archival record is in the shared source corpus; only application/programming/runtime contributions are mapped here. ACL and MLSys evidence, when retained, is supplementary and off-ledger. | NeurIPS 2026 is pending; normalize remaining ICML 2026 program-record authors. |
| SE | ICSE, FSE/PACMSE, ASE, ISSTA | Every available 2024–2026 archival research record is in the shared source corpus. ICSA evidence remains supplementary and off-ledger. | ASE 2026 is pending; normalize accepted-program records after proceedings appear. |
| OS/systems | OSDI, SOSP, EuroSys, USENIX ATC, FAST; ASPLOS adjacent | Every available 2024–2026 archival record is in the shared source corpus. NSDI evidence, when retained, is supplementary and off-ledger. | SOSP and USENIX ATC 2026 are pending. |
| Security | IEEE S&P, USENIX Security, CCS, NDSS | Monitored only to enforce the boundary. | Move security-first protocols, attacks, and defenses to the security dossier. |

Exhaustiveness applies to the [shared source corpus](../../Literature-Corpus/README.md), not to a requirement that every venue contribute a paper to this dossier. All formal records are present in the exhaustive bibliography; adjudicated in-scope records are mapped here, while unresolved high-recall candidates remain visible in the screening table.

## Ownership Rules

1. Classify by the engineered artifact and primary claim.
2. Keep one full paper row on one topic page.
3. Cross-link secondary aspects without duplicating the full record.
4. A language with a runtime is canonical under languages when its main novelty is syntax/semantics; it is canonical under runtimes when whole-workflow execution is primary.
5. Structured decoding belongs under contracts when the output interface is primary, even if implemented inside an inference engine.
6. Agent testing belongs here; LLM-generated tests for ordinary programs belong in the LLM-for-software dossier.
7. Security as one quality attribute does not automatically make a paper security-first. Quasar remains a frontier language record here, with a boundary note.
8. A software-development benchmark does not make an agent-organization paper LLM-for-software; classify adaptive roles, collaboration networks, and collective-management mechanisms under architecture.

## Evaluation Checklist

| Claim | Minimum evidence |
| --- | --- |
| A language improves development | comparable tasks, implementation completeness, developer effort, readability/maintainability, and model-quality controls |
| A compiler improves an LM program | stable task quality plus compilation cost, model calls, and end-to-end latency/cost |
| A runtime improves a workflow | full-workflow throughput/latency, resource use, workload details, and quality/SLO preservation |
| A contract guarantees structure | formal accepted language, parser/schema conformance, subword alignment, coverage, and decoding overhead |
| A protocol improves interoperability | representational coverage, round-trip fidelity, versioning, and multiple independent producers/consumers |
| A debugger localizes failures | natural or seeded failures, reproducible traces, component/step ground truth, and useful downstream repair |
| An intervention repairs an agent | repeated failed trials, controlled intervention, success/progress change, and false-intervention cost |
| An agent collective improves results | best-individual and budget-matched baselines, controlled membership/topology changes, repeated trials, and total model-call/token cost |
| A benchmark measures agents | executable environment, state-based oracle, repeated trials, partial progress, version pinning, and cost |

## Reading Order

1. [Trends and Research Frontiers](../Trends-And-Research-Frontiers.md)
2. [Benchmarks and Surveys](Benchmarks-And-Surveys.md)
3. [Languages, DSLs, and Programming Models](Languages-DSLs-And-Programming-Models.md)
4. [Types, Contracts, and Structured Interaction](Types-Contracts-And-Structured-Interaction.md)
5. [Compilers, Runtimes, and Workflow Orchestration](Compilers-Runtimes-And-Workflow-Orchestration.md)
6. [Testing, Debugging, and Observability](Testing-Debugging-And-Observability.md)
7. [Architecture, Evolution, and Operations](Architecture-Evolution-And-Operations.md)
8. [Human Factor](../Human-Factor.md) and [Non-Academic Status](../Non-Academic-Status.md)

## Research Gaps

- language semantics that expose uncertainty, effects, permissions, cost, latency, and nondeterminism without overfitting to one provider;
- type-and-effect systems for tool calls, state mutation, retries, compensation, and human approval;
- stable IRs between agent languages, compilers, runtimes, traces, and training data;
- compositional testing that separates model, prompt, tool, memory, orchestration, and environment faults;
- differential and metamorphic testing across models, framework versions, and prompt/program revisions;
- causal debugging and active intervention with realistic ground truth;
- adaptive agent organizations whose topology and membership can evolve without hiding cost, regressions, or accountability;
- longitudinal promptware/agentware evolution studies under model and API drift;
- reproducible operational benchmarks with latency, energy, money, reliability, and recovery trade-offs;
- independent replications of language usability and runtime claims;
- interoperable standards with conformance suites rather than specification text alone.

## Source Discipline

Prefer official proceedings and DOI records. Official conference programs support `Accepted` or `Official program`. Preprints remain `Frontier`; a submission label is never treated as acceptance. Product documentation and standards belong in [Non-Academic Status](../Non-Academic-Status.md). The generated [canonical corpus map](../Canonical-Corpus-Map.md), [mapped BibTeX](../Software-For-LLM-Agent-Systems-Research-Dossier-2026.bib), and [shared screening and manifest files](../../Literature-Corpus/README.md) are the audit trail for this narrative hub.
