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

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Huang2026TracecoderTraceDriven | [TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code](<https://conf.researchr.org/track/icse-2026/icse-2026-research-track#event-8b0f9926-8131-4d52-a0a8-650e06fb61e2>) | 2026 | ICSE / accepted-program | Testing Debugging And Observability | Introduces or evaluates traceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code; abstract-level contribution review remains pending. | formal-venue |

### Frontier Preprints

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Alpay2026AgentsecbenchMeasuringPrompt | [AgentSecBench: Measuring Prompt Injection, Privacy Leakage, and Tool-Use Integrity in LLM Agents](<https://arxiv.org/abs/2605.26269>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Introduce AgentSecBench as an empirical instantiation of a formal security framework for this problem. | frontier-preprint |
| Cao2026KnowledgeEnhancedAgentic | [Knowledge-Enhanced Agentic Vulnerability Repair](<https://arxiv.org/abs/2607.00820>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | To address this gap, we propose KeaRepair, a novel agentic AVR approach that grounds patch generation in verified program facts and high-level vulnerability knowledge. | frontier-preprint |
| Chen2026UnderstandingAgentReactive | [Understanding Agent-Reactive Bugs at the Model-Harness Boundary: An Empirical Study of LLM Agent Issue Reports](<https://arxiv.org/abs/2607.15684>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Conduct the first empirical study focused on agent-reactive (AR) bugs. | frontier-preprint |
| Davis2026CheapCodeCostly | [Cheap Code, Costly Judgment: A Case Study on Governable Agentic Software Engineering](<https://arxiv.org/abs/2607.01087>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Study this problem through a first-person case study: a 12-week development effort in which a single expert software engineer used frontier AI coding agents…. | frontier-preprint |
| Duraj2026IteratingTowardBetter | [Iterating Toward Better Search: A Two-Agent Simulation Framework for Evaluating Agentic Search Architectures in E-Commerce](<https://arxiv.org/abs/2606.12924>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Present a modular two-agent simulation framework for evaluating conversational shopping assistant architectures. | frontier-preprint |
| Fan2026AivilizationV0Toward | [AIvilization v0: Toward Large-Scale Artificial Social Simulation with a Unified Agent Architecture and Adaptive Agent Profiles](<https://arxiv.org/abs/2602.10429>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | To mitigate the tension between goal stability and reactive correctness, we introduce (i) a hierarchical branch-thinking planner that decomposes life goals into parallel objective…. | frontier-preprint |
| Feiglin2026SastbenchBenchmarkTesting | [SastBench: A Benchmark for Testing Agentic SAST Triage](<https://arxiv.org/abs/2601.02941>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Introduce SastBench, a benchmark for evaluating SAST triage agents that combines real CVEs as true positives with filtered SAST tool findings as approximate false…. | frontier-preprint |
| Ge2026AgentPsychometricsTask | [Agent psychometrics: Task-level performance prediction in agentic coding benchmarks](<https://arxiv.org/abs/2604.00594>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Present a framework for predicting success or failure on individual tasks tailored to the agentic coding regime. | frontier-preprint |
| Gupta2026ArchagentAgenticAi | [ArchAgent: Agentic AI-driven Computer Architecture Discovery](<https://arxiv.org/abs/2602.22425>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Bridging these worlds, we present ArchAgent, an automated computer architecture discovery system built on AlphaEvolve. | frontier-preprint |
| Koech2026PhoenixSafeGithub | [Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs](<https://arxiv.org/abs/2606.20243>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Present Phoenix, a multi-agent LLM system that resolves GitHub issues from triage through pull-request creation, combining seven layered safety controls with a baseline-aware test…. | frontier-preprint |
| Lee2026AgenticProofProperty | [Agentic Proof and Property-Based Testing via Property-Templates in Data-Intensive Computing](<https://arxiv.org/abs/2607.09072>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | This paper investigates recurring property patterns in Apache Spark. | frontier-preprint |
| Lee2026AgenticVulnerabilityReasoning | [Agentic Vulnerability Reasoning on COTS Binaries](<https://arxiv.org/abs/2605.05000>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Motivated by this question, we build SLYP, a REACT-style pipeline for end-to-end vulnerability discovery and validation of COTS binaries. | frontier-preprint |
| Litvak2026SystemPromptIs | [The System Prompt Is the Attack Surface: How LLM Agent Configuration Shapes Security and Creates Exploitable Vulnerabilities](<https://arxiv.org/abs/2603.25056>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Present PhishNChips, a study of 11 models under 10 prompt strategies, showing that prompt-model interaction is a first-order security variable: a single model's phishing…. | frontier-preprint |
| Ma2026MaestroMultiAgent | [MAESTRO: Multi-Agent Evaluation Suite for Testing, Reliability, and Observability](<https://arxiv.org/abs/2601.00481>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Present MAESTRO, an evaluation suite for the testing, reliability, and observability of LLM-based MAS. | frontier-preprint |
| Meng2026EviactEvidenceAction | [EviACT: An Evidence-to-Action Framework for Agentic Program Repair](<https://arxiv.org/abs/2605.27238>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Propose EviACT (Evidence-to-Action), an agentic APR framework that coordinates three evidence-driven guardrails across repair stages. | frontier-preprint |
| Prinos2026StableAgenticControl | [Stable Agentic Control: Tool-Mediated LLM Architecture for Autonomous Cyber Defense](<https://arxiv.org/abs/2605.03034>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Motivated by the operational needs of security operations centers (SOCs) that must configure endpoint detection and response (EDR) policies under adversarial pressure, we present…. | frontier-preprint |
| Qian2026MalaikaUnderstandingMalware | [Malaika: Understanding Malware through Tri-Grounded Agentic Reasoning](<https://arxiv.org/abs/2607.09179>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | To study this hypothesis, we present Malaika, a multi-agent framework that operationalizes the three grounding mechanisms through analyst-inspired reasoning, tool-mediated evidence localization, and retrieval-based…. | frontier-preprint |
| Rehan2026TestDrivenAi | [Test-Driven AI Agent Definition (TDAD): Compiling Tool-Using Agents from Behavioral Specifications](<https://arxiv.org/abs/2603.08806>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Present Test-Driven AI Agent Definition (TDAD), a methodology that treats agent prompts as compiled artifacts: engineers provide behavioral specifications, a coding agent converts them…. | frontier-preprint |
| Sajadi2026TraceviewInteractiveVisualization | [TraceView: Interactive Visualization of Agentic Program Repair Trajectories](<https://arxiv.org/abs/2606.22110>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | To help developers address these challenges, we present TraceView, an interactive tool for labeling and visualizing repair trajectories from APR systems. | frontier-preprint |
| Salim2026TokenomicsQuantifyingWhere | [Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering](<https://arxiv.org/abs/2601.14470>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | To address this, we conduct an analysis of token consumption patterns in an LLM-MA system within the Software Development Life Cycle (SDLC), aiming to…. | frontier-preprint |
| Wu2026EvodrcSelfEvolving | [EvoDRC: A Self-Evolving Agentic Framework for Automated DRC Violation Repair](<https://arxiv.org/abs/2607.20019>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Present EvoDRC, a skill-evolution framework for agentic block-level DRC repair. | frontier-preprint |
| Xia2026IdlenessIsRelative | [Idleness is Relative: Exploiting Tool-Call Idle Windows for Offloading in Agentic Systems with MORI](<https://arxiv.org/abs/2606.00866>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Present MORI, an agent serving system that solves the above problem. | frontier-preprint |
| Yoo2026MkevolveModularMulti | [MKEvolve: A Modular Multi-Agent Framework for Kernel Code Generation](<https://arxiv.org/abs/2607.20501>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Present MKEvolve (Modular Kernel Evolve), a framework that iteratively co-evolves a modular decomposition of complex PyTorch modules and the LLM-generated kernel for each submodule…. | frontier-preprint |
| Zhu2026PaiEconClaude | [pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assisted Economic Theory Development](<https://arxiv.org/abs/2607.21268>) | 2026 | arXiv / frontier-preprint | Testing Debugging And Observability | Evaluate the architecture on five matched economic-theory tasks against an ungated baseline. | frontier-preprint |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
