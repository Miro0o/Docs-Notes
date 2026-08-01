---
ai-generated: true
last-reviewed: 2026-07-30
---

# Code Review, Change Governance, and Traceability

Back: [Academic Status](Academic-Status.md)

Scope: review-comment generation and validation, issue-to-change linkage, change rationale and provenance, and governance mechanisms that help people audit ordinary software changes. Security-first review and vulnerability triage belong in the sibling security dossier.

## Status

This is an emerging but distinct software-engineering line. The research target is not merely a plausible comment or patch: it is review evidence grounded in the full change context, traceable links between intent and implementation, and accountable decisions that survive repository evolution.

## Canonical Papers

| Key | Paper | Year | Venue / evidence | Contribution | Label |
| --- | --- | ---: | --- | --- | --- |
| Zeng2026SWRBench | [SWR-Bench: Assessing LLM Performance in Real-World Code Review Comment Generation](https://conf.researchr.org/details/fse-2026/fse-2026-research-papers/78/SWR-Bench-Assessing-LLM-Performance-in-Real-World-Code-Review-Comment-Generation) | 2026 | FSE Research Papers / official program | Curates 1,000 manually verified pull requests with project context and structured ground truth for human-aligned review-comment evaluation. | Official program / Evaluation |
| Akhavan2026LinkAnchor | [LinkAnchor: An Autonomous LLM-Based Agent for Issue-to-Commit Link Recovery](https://doi.org/10.1145/3808191) | 2026 | FSE/PACMSE / DOI | Uses lazy context acquisition to recover traceability links and resolving commit chains across issue trackers and repositories. | Published |

## Evaluation Checklist

- preserve the pull request, issue, repository revision, discussion, and linked-artifact context;
- separate comment relevance, factuality, actionability, and defect-finding value;
- compare against human review history without treating one reviewer comment as a complete oracle;
- measure false-positive review burden, duplicate comments, and missed high-impact issues;
- evaluate link recovery with temporal splits, ambiguous commits, and independently checked traces;
- record provenance, rationale, approval, and override paths for generated recommendations.

## Related Evidence and Routing

- [StackEval](Program-Comprehension-Search-Retrieval-Documentation-And-APIs.md) includes code-review assistance within a broader coding-assistance benchmark; its full record remains on the comprehension shelf.
- [FeatureBench](Software-Agents-And-Repository-Engineering.md) evaluates repository feature changes; this shelf owns the human and governance layer around accepting and tracing those changes.
- Cross-cutting reviewer workload, trust, and accountability questions remain in the [shared Human Factor](../../LLM-Software-Security-Research-Dossier-2026/Human-Factor.md).
- Review whose primary goal is vulnerability discovery, secure patch acceptance, or exploitability assessment belongs in the [software-security dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md).

## Research Gaps

- executable or causal oracles for whether a review comment prevents a defect;
- multi-reviewer disagreement and project-specific review norms;
- traceability that remains correct after rebases, squashes, backports, and issue migration;
- accountable review of agent-generated changes at realistic volume;
- longitudinal evidence on review debt and future maintenance.

<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->
## Generated Canonical Corpus Rows

The builder maintains this block from the shared screening and mapping ledgers. Hand-written rows and analysis above remain authoritative where present.

### Formal Venue Papers

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Tanzil2024ChatgptIncorrectnessDetection | [ChatGPT Incorrectness Detection in Software Reviews.](<https://doi.org/10.1145/3597503.3639194>) | 2024 | ICSE / proceedings | Code Review Change Governance And Traceability | Introduces or evaluates chatGPT Incorrectness Detection in Software Reviews; abstract-level contribution review remains pending. | formal-venue |

### Frontier Preprints

| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |
| --- | --- | ---: | --- | --- | --- | --- |
| Capilla2026TowardsSupportingQuality | [Towards Supporting Quality Architecture Evaluation with LLM Tools](<https://arxiv.org/abs/2603.28914>) | 2026 | arXiv / frontier-preprint | Code Review Change Governance And Traceability | To reduce this effort and make the assessment and selection of scenarios more efficient, in this research we propose the use of LLMs to…. | frontier-preprint |
| GilPereira2026SlrmentorLlmBased | [SLRMentor: An LLM-Based Tool Supporting Learning of SLR in Software Engineering](<https://arxiv.org/abs/2606.07831>) | 2026 | arXiv / frontier-preprint | Code Review Change Governance And Traceability | This paper presents SLRMentor, a conversational assistant designed to support both learning about the systematic literature review process and the execution of planning activities…. | frontier-preprint |
| Kumar2026BiggerIsnT | [Bigger Isn't Always Better: A Comparative Evaluation of LLMs for Automated Code Review](<https://arxiv.org/abs/2606.15689>) | 2026 | arXiv / frontier-preprint | Code Review Change Governance And Traceability | Present a systematic evaluation of five large language models on automated code review, comparing Claude Sonnet 4.6, Claude Haiku 4.5, GPT-5.4 mini, Minimax M2.7…. | frontier-preprint |
| Ulurmak2026EvalsafetygapHybridSurvey | [EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures](<https://arxiv.org/abs/2606.30219>) | 2026 | arXiv / frontier-preprint | Code Review Change Governance And Traceability | This paper presents a systematic survey and conceptual synthesis of the shared measurement problem underlying large language model (LLM) evaluation and AI safety: benchmark…. | frontier-preprint |
| Yang2026PaftPreservationAware | [PAFT: Preservation Aware Fine-Tuning for Minimal-Edit Program Repair](<https://arxiv.org/abs/2604.03113>) | 2026 | arXiv / frontier-preprint | Code Review Change Governance And Traceability | Propose PAFT, a preservation-aware fine-tuning method for minimal-edit program repair. | frontier-preprint |

<!-- END GENERATED CANONICAL CORPUS ROWS -->
