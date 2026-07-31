---
ai-generated: true
last-reviewed: 2026-07-30
---

# Compilers, Runtimes, and Workflow Orchestration

Back: [Academic Status](Academic-Status.md)

Scope: systems that compile or execute structured LLM/agent programs and exploit application-level control flow, dataflow, semantic variables, model choices, tools, and service-level objectives.

## Status

The important systems idea is to optimize a workflow or agent program rather than isolated model requests. This requires an abstraction boundary through which the runtime can see dependencies, reusable prefixes, parallel branches, program-level progress, quality constraints, and model/tool placement choices.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Zheng2024SGLang | [SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/hash/724be4472168f31ba1c9ac630f15dec8-Abstract-Conference.html) | 2024 | NeurIPS / proceedings | Combines a frontend language with a runtime using RadixAttention and structured-output optimizations; reports up to 6.4× throughput on evaluated workloads. | Published / Systems |
| Lin2024Parrot | [Parrot: Efficient Serving of LLM-based Applications with Semantic Variable](https://www.usenix.org/conference/osdi24/presentation/lin-chaofan) | 2024 | OSDI / proceedings | Introduces Semantic Variable to expose application dataflow across model calls, enabling service-level optimization of complete applications. | Published / Systems |
| Chaudhry2026Murakkab | [Murakkab: Resource-Efficient Agentic Workflow Orchestration in Cloud Platforms](https://www.usenix.org/conference/osdi26/presentation/chaudhry) | 2026 | OSDI / proceedings | Uses a declarative workflow abstraction, profile-guided optimizer, and adaptive runtime to map components to models and hardware under SLOs. | Published / Systems |
| Luo2026Agentix | [Agentix: An Efficient Serving Engine for LLM Agents as General Programs](https://www.usenix.org/conference/nsdi26/presentation/luo) | 2026 | NSDI / USENIX proceedings | Treats agent programs as first-class serving units and uses program-level context to preempt and prioritize calls for single-threaded and distributed programs; reports 4–15× program throughput at the same latency in its evaluation. | Published / Systems |

## Cross-Links

- [DSPy](Languages-DSLs-And-Programming-Models.md) has a compiler, but its canonical shelf is language/programming model because the declarative module abstraction is the central contribution.
- [APPL](Languages-DSLs-And-Programming-Models.md) includes an asynchronous runtime and tracing, but its primary contribution is a prompt programming language.
- [Opportunistically Parallel Lambda Calculus](Languages-DSLs-And-Programming-Models.md) evaluates LLM-heavy scripts and supplies an execution strategy, but its canonical contribution is language semantics.
- [XGrammar](Types-Contracts-And-Structured-Interaction.md) is implemented close to inference, but its primary claim is structured-output conformance.

## Runtime Stack

| Layer | Responsibility | Typical evidence |
| --- | --- | --- |
| Program/graph extraction | recover calls, dependencies, control flow, tool use, and output constraints | representational coverage and compilation correctness |
| Optimization | choose parallelism, batching, caching, placement, model variants, and execution order | optimization time and objective improvement |
| Scheduling | allocate model, CPU/GPU, network, and tool resources using request-, workflow-, or program-level context | utilization, queueing delay, fairness, program throughput, and tail latency |
| Execution | run calls and tools while preserving workflow semantics | end-to-end success and conformance |
| Adaptation | react to load, cost, failures, and quality/SLO drift | stability, recovery time, and reconfiguration cost |
| Observability | expose causally connected model/tool events | trace completeness and diagnostic utility |

## Evaluation Checklist

- evaluate whole workflows rather than independent prompts;
- state whether task quality is exactly preserved, statistically comparable, or traded against performance;
- report latency distributions, throughput, cost, energy, and resource utilization;
- include compiler/profiler overhead and warm-up effects;
- specify models, quantization, hardware, cache state, and concurrency;
- compare against strong current runtime baselines with equivalent features;
- test heterogeneous workflows with branches, tools, retrieval, and repeated prefixes;
- report failures caused by stale profiles, model substitution, or load changes.

## Research Directions

- semantic-preserving rewrites for probabilistic workflows;
- cost/quality/latency/energy multi-objective compilation;
- effect-aware scheduling of external tools and stateful operations;
- incremental compilation after prompt, model, or tool-schema changes;
- portable workflow IRs shared across languages and runtimes;
- program-aware scheduling across dynamically discovered agent control flow;
- admission control and rollback for long-horizon workflows;
- deterministic replay despite nondeterministic model and tool responses;
- distributed agent workflow scheduling with explicit failure domains.

## Boundary

A faster attention kernel or generic serving scheduler is outside scope if it sees only model requests. It enters this dossier when the primary contribution exposes and exploits agent-program or workflow structure.
