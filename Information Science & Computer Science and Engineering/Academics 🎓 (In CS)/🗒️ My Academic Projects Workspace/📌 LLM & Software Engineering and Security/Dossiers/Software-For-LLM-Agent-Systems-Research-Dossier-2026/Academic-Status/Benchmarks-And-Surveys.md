---
ai-generated: true
last-reviewed: 2026-07-30
---

# Benchmarks and Surveys

Back: [Academic Status](Academic-Status.md)

Scope: executable environments, evaluation frameworks, reliability metrics, and syntheses that help assess LLM/agent software rather than only a base model.

## Status

Success rate alone hides partial progress, invalid actions, inconsistent retries, state corruption, policy violations, and human handoff failures. Stronger benchmarks expose programmatic state, tools, multi-turn interaction, and long-horizon work, then evaluate repeated runs and intermediate progress.

## Canonical Benchmarks

| Key | Paper | Year | Venue / evidence | Evaluation contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Ma2024AgentBoard | [AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/hash/877b40688e330a0e2a3fc24084208dfa-Abstract-Datasets_and_Benchmarks_Track.html) | 2024 | NeurIPS Datasets & Benchmarks / proceedings | Adds fine-grained progress rate and an analytical evaluation/visualization framework across multi-turn environments. | Published / Benchmark |
| Yao2025TauBench | [τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://openreview.net/forum?id=roNSXZpUDN) | 2025 | ICLR / official conference paper | Evaluates agents interacting with simulated users and domain APIs against database end states and repeated-run reliability. | Published / Benchmark |
| Jha2025ITBench | [ITBench: Evaluating AI Agents across Diverse Real-World IT Automation Tasks](https://proceedings.mlr.press/v267/jha25a.html) | 2025 | ICML / proceedings | Provides executable SRE, CISO, and FinOps scenarios with interpretable metrics. Only the non-security SRE/FinOps slices are canonical to this dossier. | Published / Benchmark |
| Xu2025TheAgentCompany | [TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks](https://papers.neurips.cc/paper_files/paper/2025/hash/0d744742f6fac4d1134c019b7cef3c8a-Abstract-Datasets_and_Benchmarks_Track.html) | 2025 | NeurIPS Datasets & Benchmarks / proceedings | Builds a self-contained simulated software company with web, coding, communication, and stateful workplace tasks. | Published / Benchmark |

## Survey and Field Synthesis

| Key | Work | Year | Venue / evidence | Value | Label |
| --- | --- | ---: | --- | --- | --- |
| Gonzalez2026TestingAIware | [Testing AIware Systems: A Software Engineering Survey](https://doi.org/10.1145/3805760.3814894) | 2026 | ACM AIware / DOI; specialized venue co-located with FSE | Surveys software-testing approaches for AIware and received an AIware honorable mention. | Published / Survey |

The field-map paper *Software Engineering and Foundation Models* is canonical on [Architecture, Evolution, and Operations](Architecture-Evolution-And-Operations.md); use it as practitioner-disclosure evidence, not as a controlled causal study.

## Benchmark Selection Matrix

| Question | Suitable anchor |
| --- | --- |
| Does the agent make measurable progress before task completion? | AgentBoard |
| Does the agent interact with a user and follow domain policy while changing backend state? | τ-bench |
| Can an agent perform reproducible SRE or FinOps work in realistic IT environments? | ITBench non-security slices |
| Can an agent complete long-horizon work across software-company services? | TheAgentCompany |
| Is the target framework itself testable and diagnosable? | Use [Testing, Debugging, and Observability](Testing-Debugging-And-Observability.md), not only a capability benchmark |

## Evaluation Checklist

- pin benchmark, environment, model, agent framework, prompts, and tool versions;
- disclose network access, credentials, retries, human intervention, and budget;
- use environment state or executable checks where possible;
- run multiple trials and report consistency, not only the best attempt;
- measure partial progress without allowing reward hacking;
- retain full trajectories and failure categories;
- separate invalid format/tool calls from reasoning failures;
- report latency, token/model calls, monetary cost, and infrastructure;
- document contamination and task freshness;
- test sensitivity to harmless wording, ordering, and environment changes.

## Survey Checklist

- state databases, search strings, dates, inclusion criteria, and deduplication;
- separate `LLM for software` from `software for LLM/agent systems`;
- retain exact peer-review and venue status;
- distinguish frameworks, research prototypes, standards, and products;
- include negative and operational evidence;
- publish the extraction sheet and taxonomy;
- avoid counting the same preprint and proceedings version twice.

## Research Directions

- framework-level conformance and interoperability suites;
- benchmarks that independently vary model, prompt program, runtime, tool set, and environment;
- longitudinal benchmarks under model and API evolution;
- failure-preserving replay bundles and portable incident artifacts;
- reliability curves across retry and cost budgets;
- benchmarks for rollback, compensation, and human escalation;
- energy and resource measurement for complete agent workflows;
- benchmark governance that records task changes and leaderboard comparability.

## Boundary

AgentDojo and other security-first benchmarks are excluded from this page even when they contain ordinary task-success measurements; their primary claim belongs in the security dossier.

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Jin2026FinrptDatasetEvaluation | [FinRpt: Dataset, Evaluation System and LLM-based Multi-agent Framework for Equity Research Report Generation.](<https://doi.org/10.1609/aaai.v40i1.37014>) | 2026 | AAAI / proceedings | Benchmarks And Surveys | Benchmarks or evaluates finRpt: Dataset, Evaluation System and LLM-based Multi-agent Framework for Equity Research Report Generation; abstract-level contribution review remains pending. | formal-venue |
| Wang2026McpBenchBenchmarking | [MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers](<https://openreview.net/forum?id=fe8mzHwMxN>) | 2026 | ICLR / accepted-program | Benchmarks And Surveys | Introduces or evaluates mCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers; abstract-level contribution review remains pending. | formal-venue |
| normalization2026AgentnoisebenchBenchmarkingRobustness | [AgentNoiseBench: Benchmarking Robustness of Tool-Using LLM Agents Under Noisy Condition](<https://icml.cc/virtual/2026/poster/64355>) | 2026 | ICML / accepted-program | Benchmarks And Surveys | Introduces or evaluates agentNoiseBench: Benchmarking Robustness of Tool-Using LLM Agents Under Noisy Condition; abstract-level contribution review remains pending. | formal-venue |

### Frontier Preprints

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Caumartin2026RetrievalOrientedCode | [Retrieval-Oriented Code Representations in Agentic Bug Localization](<https://arxiv.org/abs/2607.11046>) | 2026 | arXiv / frontier-preprint | Benchmarks And Surveys | Study file-level bug localization as a representation-driven retrieval problem. | frontier-preprint |
| Chen2026CodecompStructuralKv | [CodeComp: Structural KV Cache Compression for Agentic Coding](<https://arxiv.org/abs/2604.10235>) | 2026 | arXiv / frontier-preprint | Benchmarks And Surveys | Present CodeComp, a training-free KV cache compression framework that incorporates static program analysis into LLM inference via Code Property Graph priors extracted by Joern. | frontier-preprint |
| Hofer2026AssessingAutomatedPrompt | [Assessing Automated Prompt Injection Attacks in Agentic Environments](<https://arxiv.org/abs/2606.10525>) | 2026 | arXiv / frontier-preprint | Benchmarks And Surveys | Present a comprehensive empirical evaluation of automated prompt injection attacks against LLM agents, adapting both white-box (GCG) and black-box (TAP) methods to the agentic…. | frontier-preprint |
| Lu2026LeanRefactorMulti | [Lean Refactor: Multi-Objective Controllable Proof Optimization via Agentic Strategy Search](<https://arxiv.org/abs/2605.20244>) | 2026 | arXiv / frontier-preprint | Benchmarks And Surveys | Present Lean Refactor, a plug-and-play retrieval-augmented agentic framework for multi-objective, controllable, and version-robust refactoring of Lean proofs. | frontier-preprint |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
