---
ai-generated: true
last-reviewed: 2026-07-30
---

# Languages, DSLs, and Programming Models

Back: [Academic Status](Academic-Status.md)

Scope: language-level abstractions for prompts, model calls, tool-using agents, and LLM application pipelines. The primary contribution must be how developers express the application, not how an LLM generates ordinary code.

## Status

The central design shift is from opaque strings and provider SDK calls to named, composable program objects. Current systems occupy different points in the design space: query language, declarative module graph, host-language embedding, new language construct, or a core calculus with an execution strategy for expensive external calls. No design yet provides a generally accepted semantics for probabilistic results, side effects, tool permissions, retries, cost, and human approval.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Khattab2024DSPy | [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f1cf02ce09757f57c3b93c0db83181e0-Abstract-Conference.html) | 2024 | ICLR / proceedings | Represents LM pipelines as declarative modules and parameterized transformation graphs that a compiler can optimize against a metric. | Published |
| Dantanarayana2025MTP | [MTP: A Meaning-Typed Language Abstraction for AI-Integrated Programming](https://doi.org/10.1145/3763092) | 2025 | OOPSLA/PACMPL / DOI | Adds a `by` operator, meaning-oriented IR, and runtime to the Jac Python superset; the official program reports a developer study. | Published / Human study |
| Mell2025OPL | [Opportunistically Parallel Lambda Calculus](https://doi.org/10.1145/3763143) | 2025 | OOPSLA/PACMPL / DOI | Defines a core lambda calculus with opportunistic evaluation that dispatches independent external calls in parallel and streams results; proves confluence and eventual execution, and implements the design as Opp. | Published |
| Dong2025APPL | [APPL: A Prompt Programming Language for Harmonious Integration of Programs and Large Language Model Prompts](https://aclanthology.org/2025.acl-long.63/) | 2025 | ACL / proceedings and DOI | Embeds prompts in Python functions with asynchronous semantics, tracing, diagnosis, and replay. | Published |

## Foundational Work Before 2024

| Key | Paper | Year | Venue / evidence | Why retained | Label |
| --- | --- | ---: | --- | --- | --- |
| BeurerKellner2023LMQL | [Prompting Is Programming: A Query Language for Large Language Models](https://doi.org/10.1145/3591300) | 2023 | PLDI/PACMPL / DOI | Establishes language-model programming through scripted prompts, control flow, constraints, and optimized query execution. | Published / Foundational |

## Frontier Record

| Key | Paper | Year | Evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Mell2025Quasar | [A Fast, Reliable, and Secure Programming Language for LLM Agents with Code Actions](https://arxiv.org/abs/2506.12202) | 2025 | arXiv only | Proposes Quasar for agent code actions with automated parallelization, uncertainty quantification, and approval-oriented security features. | Frontier |

Quasar is retained because its primary artifact is an agent-action language. It must not be described as accepted at ICLR 2026; the verified public record is a preprint. Security is one property, so security-specific implications may be cross-linked from the security dossier without moving the canonical language record.

## Design Space

| Dimension | Questions |
| --- | --- |
| Host integration | Standalone language, embedded DSL, library-level modules, annotations, or operator extension? |
| Semantics | What does a model invocation denote, and what can the programmer rely on? |
| Composition | How are prompts, retrieval, tools, branching, loops, parallel calls, and multi-agent interaction composed? |
| Effects | Can the system track external calls, state mutation, permissions, nondeterminism, cost, and latency? |
| Evaluation strategy | Which external calls may run eagerly, concurrently, or as streams while preserving program meaning? |
| Optimization | Which parts may a compiler rewrite without changing intended behavior? |
| Debuggability | Are prompt expansion, model inputs, tool calls, and intermediate values inspectable and replayable? |
| Portability | Can a program move across models, providers, runtimes, and tool schemas? |
| Evolution | Can prompts and behavior contracts be versioned, regression-tested, and migrated? |

## Evaluation Checklist

- compare against realistic SDK/library baselines, not raw string concatenation alone;
- separate reduced lines of code from reduced conceptual complexity;
- pin model, prompt budget, tools, and task data in developer comparisons;
- measure debugging, modification, and reuse, not only initial implementation time;
- report generated prompts and runtime traces so abstraction leaks are visible;
- test portability across at least two models or providers where claimed;
- distinguish language expressiveness from compiler/runtime speedups;
- include failure cases where the abstraction obscures model behavior.

## Research Directions

- algebraic effects or capabilities for tool calls, permissions, and human approvals;
- gradual or refinement types for probabilistic results and confidence obligations;
- transaction and compensation constructs for agents that mutate external state;
- deterministic replay semantics across changing models and APIs;
- model-independent IRs that preserve developer intent;
- LLM-friendly surface languages whose outputs remain reviewable and formally checkable;
- modularity, testing, package management, and semantic versioning for prompt programs.

## Boundary

Type-constrained generation of ordinary source code belongs in the LLM-for-software dossier. Languages whose purpose is to express LLM applications or agent actions belong here.
