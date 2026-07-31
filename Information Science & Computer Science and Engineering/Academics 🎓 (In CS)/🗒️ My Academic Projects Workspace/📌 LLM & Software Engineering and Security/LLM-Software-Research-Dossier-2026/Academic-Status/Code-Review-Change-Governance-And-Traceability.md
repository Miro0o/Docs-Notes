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
- Cross-cutting reviewer workload, trust, and accountability questions remain on [Human Factor](../Human-Factor.md).
- Review whose primary goal is vulnerability discovery, secure patch acceptance, or exploitability assessment belongs in the [software-security dossier](../../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md).

## Research Gaps

- executable or causal oracles for whether a review comment prevents a defect;
- multi-reviewer disagreement and project-specific review norms;
- traceability that remains correct after rebases, squashes, backports, and issue migration;
- accountable review of agent-generated changes at realistic volume;
- longitudinal evidence on review debt and future maintenance.
