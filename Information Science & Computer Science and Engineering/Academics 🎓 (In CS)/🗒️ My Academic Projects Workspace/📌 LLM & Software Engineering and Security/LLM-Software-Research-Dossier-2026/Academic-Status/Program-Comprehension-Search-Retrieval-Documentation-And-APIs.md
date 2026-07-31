---
ai-generated: true
last-reviewed: 2026-07-30
---

# Program Comprehension, Search, Retrieval, Documentation, and APIs

Back: [Academic Status](Academic-Status.md)

Scope: non-security work in which an LLM helps a developer or software tool locate, retrieve, explain, summarize, document, or correctly call existing code. Repository issue resolution remains in [Software Agents and Repository Engineering](Software-Agents-And-Repository-Engineering.md); this page owns the information-access layer that makes such work possible.

## Status

Program comprehension is moving from flat text windows toward repository memory, code graphs, hybrid lexical-semantic retrieval, execution-aware summaries, and current API knowledge. The central evaluation question is no longer whether a description sounds plausible, but whether it retrieves the right artifact and remains faithful to code, history, dependencies, and runtime behavior.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Shah2024StackEval | [StackEval: Benchmarking LLMs in Coding Assistance](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4126a607bbe2836cb6ca0eb45b75618b-Abstract-Datasets_and_Benchmarks_Track.html) | 2024 | NeurIPS Datasets & Benchmarks / proceedings | Evaluates implementation, debugging, review, and conceptual-understanding assistance across many languages, with a recent-data companion benchmark. | Published / Evaluation |
| Fang2025EP4CS | [Enhanced Prompting Framework for Code Summarization with Large Language Models](https://doi.org/10.1145/3728949) | 2025 | ISSTA/PACMSE / DOI | Combines learned prompts with structural program information for code summarization. | Published |
| Tao2025CodeGraphModel | [Code Graph Model (CGM): A Graph-Integrated Large Language Model for Repository-Level Software Engineering Tasks](https://proceedings.neurips.cc/paper_files/paper/2025/hash/178ae4ba29022eb7bf509c2e27bc8ab8-Abstract-Conference.html) | 2025 | NeurIPS / proceedings | Integrates repository graph structure into an LLM and graph-RAG workflow for repository understanding. | Published |
| Jiang2025IssueLocalization | [Issue Localization via LLM-Driven Iterative Code Graph Searching](https://conf.researchr.org/track/ase-2025/ase-2025-papers) | 2025 | ASE Research Papers / official program | Searches a code graph iteratively to localize issue-relevant program elements. | Official program |
| Wang2026RepositoryMemory | [Improving Code Localization with Repository Memory](https://iclr.cc/virtual/2026/poster/10011159) | 2026 | ICLR Poster / official record | Builds reusable repository memory from commit history, linked issues, and evolving-component summaries. | Published |
| Kou2026APIDocumentation | [Automating API Documentation from Crowdsourced Knowledge](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Uses external developer knowledge to produce API documentation rather than relying only on model memory. | Official program |
| Yang2026UniCoR | [UniCoR: Modality Collaboration for Robust Cross-Language Hybrid Code Retrieval](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program; Distinguished Paper | Combines modalities for cross-language hybrid code retrieval. | Official program |
| Ma2026ToolInteractiveLocalization | [Enhancing Issue Localization Agent with Tool-Interactive Training](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Trains an issue-localization agent through interaction with repository tools. | Official program |
| Akram2026APIArgumentCompletion | [LLM-based API Argument Completion with Knowledge-Augmented Prompts](https://conf.researchr.org/track/icse-2026/icse-2026-research-track) | 2026 | ICSE Research Track / official program | Grounds API-argument completion in retrieved knowledge. | Official program |
| Wan2026SummaryHallucinations | [Hallucinations in LLM-based Code Summarization: Unveiling, Detection, and Mitigation](https://conf.researchr.org/track/fse-2026/fse-2026-research-papers) | 2026 | FSE Research Papers / official program | Studies factual hallucination in summaries and methods to detect and mitigate it. | Official program / Evaluation |

## Existing Foundations on Other Shelves

These records keep their existing canonical rows and are linked rather than duplicated:

- [Using an LLM to Help With Code Understanding](../Human-Factor.md) is the human-comprehension anchor.
- SpecRover, comment-consistency repair, and the ICSE 2025 code-summarization study remain under [Requirements, Design, Maintenance, and Evolution](Requirements-Design-Maintenance-And-Evolution.md).
- Repository planning and issue resolution remain under [Software Agents and Repository Engineering](Software-Agents-And-Repository-Engineering.md).

## Evaluation Checklist

- report the query, repository revision, language, and candidate search space;
- separate retrieval recall from downstream patch or answer quality;
- check summaries and documentation against code, tests, types, and current API versions;
- preserve provenance for retrieved issues, commits, documentation, and crowdsourced text;
- evaluate cross-language and cross-project transfer without hiding unsupported cases;
- measure latency, index cost, context budget, and stale-memory failure modes.

## Boundary Notes

Binary retrieval or reverse engineering belongs here only when its primary goal is general software understanding. Malware, vulnerability, exploit, or secret-oriented retrieval belongs in the [security dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md).

## Research Gaps

- faithful summaries for stateful, concurrent, and dynamically configured software;
- repository memory that updates without preserving obsolete assumptions;
- retrieval evaluation beyond SWE-bench-style issue resolution;
- multilingual documentation and cross-language API equivalence;
- provenance-aware answers that distinguish code, documentation, issue discussion, and model inference;
- comprehension support whose benefit survives delayed maintenance tasks.
