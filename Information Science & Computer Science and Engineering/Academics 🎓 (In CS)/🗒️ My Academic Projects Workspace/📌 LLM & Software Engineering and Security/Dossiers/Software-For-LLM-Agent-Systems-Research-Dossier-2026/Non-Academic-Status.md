---
ai-generated: true
last-reviewed: 2026-07-30
---

# Non-Academic Status

Home: [Software-For-LLM-Agent-Systems-Research-Dossier-2026.md](Software-For-LLM-Agent-Systems-Research-Dossier-2026.md)

Scope: open standards, protocols, production frameworks, SDKs, and practitioner signals for engineering LLM applications and agent systems. These records show convergence and adoption, not peer-reviewed correctness.

## Current Position

Industry is converging on several software layers: model/tool connectivity, agent-to-agent messaging, workflow graphs, structured outputs, traces, and reusable agent SDKs. The standards remain fast-moving. Version pinning and conformance tests matter more than the name of a protocol or framework.

## Standards and Framework Signals

| Signal | Status on 2026-07-30 | Software abstraction | Caution |
| --- | --- | --- | --- |
| [Model Context Protocol specification](https://modelcontextprotocol.io/specification/2025-11-25) | Published stable specification; a [2026-07-28 release candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) is not yet the stable baseline | client/server protocol for tools, resources, prompts, and context | implementations and extensions evolve quickly; test exact version and capabilities |
| [Agent2Agent Protocol specification](https://a2a-protocol.org/latest/specification/) | Open protocol with a versioned specification | discovery and interaction between independent agents | protocol adoption does not establish semantic compatibility or reliable coordination |
| [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) | Development-stage conventions | common trace/log/metric attributes for model and agent operations | field names and stability levels can change; pin schema versions |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | Maintained provider SDK and documentation | agents, tools, handoffs, guardrails, sessions, and tracing | product documentation, not independent evidence; portability must be tested |
| [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) | Widely used open-source orchestration framework | stateful graph execution for long-running agents | API churn and application-specific scaffolding complicate comparisons |

## What to Record for a Framework

- framework and exact version/commit;
- model provider and model release;
- graph, roles, routing, retries, memory, and stopping policy;
- tool schemas and external permissions;
- state persistence and checkpoint behavior;
- tracing schema and redaction policy;
- concurrency, timeout, and failure semantics;
- structured-output and validation behavior;
- cost/token accounting;
- migration and backward-compatibility policy.

## Evidence Hierarchy

1. Versioned specification plus independent conformance suite and multiple implementations.
2. Reproducible production incident or deployment report with denominators and artifacts.
3. Open-source framework with pinned examples, tests, and change history.
4. Vendor documentation with explicit semantics and limitations.
5. Product benchmark with disclosed environment, budget, and failure handling.
6. Demo, launch post, or unversioned compatibility claim.

## Watchlist

- whether MCP's 2026 release candidate stabilizes and gains interoperable conformance tests;
- compatibility and division of responsibility between MCP, A2A, and framework-specific protocols;
- stable OpenTelemetry conventions for agents, tools, memory, and multi-agent causality;
- portable trace and replay bundles across frameworks;
- common schemas for tool effects, permissions, and human approvals;
- semantic versioning for prompt programs and agent behavior;
- convergence between research IRs such as Agent Data Protocol and production protocol formats;
- independent evidence that framework abstractions reduce maintenance and incidents.

## Boundary

Security advisories and protocol attacks belong in the security dossier. This page tracks general programmability, interoperability, lifecycle, and observability signals only.
