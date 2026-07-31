---
ai-generated: true
last-reviewed: 2026-07-31
---

# Shared Literature Corpus

This directory is the reproducible evidence layer shared by the three research dossiers:

- [LLM → software/code](../LLM-Software-Research-Dossier-2026/LLM-Software-Research-Dossier-2026.md)
- [software engineering for LLM/agent systems](../Software-For-LLM-Agent-Systems-Research-Dossier-2026/Software-For-LLM-Agent-Systems-Research-Dossier-2026.md)
- [LLM and software security](../LLM-Software-Security-Research-Dossier-2026/LLM-Software-Security-Research-Dossier-2026.md)

The snapshot is frozen at **2026-07-31**. It covers archival research papers from 2024 through the cutoff at the venue ledger below and a separately declared 2026 arXiv frontier-query universe. A `pending` cell means that a complete public archival program was not available by the cutoff; it is not a zero-paper claim.

## Artifacts

| Artifact | Purpose |
| --- | --- |
| [Exhaustive formal-venue BibTeX](exhaustive-formal-venues.bib) | Every collected archival record in the defined venue/year ledger, including papers unrelated to the dossiers |
| [Screened formal BibTeX](screened-formal-venues.bib) | Formal papers adjudicated relevant to at least one dossier |
| [Exhaustive 2026 frontier-query BibTeX](exhaustive-frontier-preprints-2026.bib) | Every normalized arXiv record returned by the declared 2026 cs.SE/cs.CR/cs.PL/cs.OS LLM/foundation-model query |
| [Screened frontier BibTeX](screened-frontier-preprints.bib) | Verified public preprints retained separately from formal venue evidence |
| [2026 frontier query manifest](frontier-query-manifest-2026.json) | Exact API query, time/category boundary, raw and normalized counts, decision counts, and scope limitation |
| [2026 frontier screening ledger](frontier-screening-2026.csv) | One title/abstract and publication-status decision for every normalized frontier-query record |
| [Venue-year manifest](venue-year-manifest.csv) | Official and metadata sources, status, expected/collected counts, reconciliation, and unresolved metadata |
| [Screening ledger](screening.csv) | One decision row for every formal record, including candidates still requiring abstract review |
| [Dossier mapping](dossier-mapping.csv) | One canonical per-dossier row with shelf, role, contribution, source/status, and evidence layer |
| [Taxonomy audit](taxonomy-audit.csv) | Research question, inclusion/exclusion boundary, coverage count, and retirement/replacement status per shelf |
| [Coverage counts](coverage-counts.md) | Human-readable per-venue/year result and pending cells |
| [Deduplication log](deduplication-log.csv) | Identity/title collisions resolved during normalization |
| [Build summary](build-summary.json) | Machine-readable headline counts |
| [Validation report](validation-report.json) | Last acceptance-test result |

## Venue Ledger

- Security: IEEE S&P, USENIX Security, ACM CCS, NDSS
- Software engineering: ICSE, FSE/PACMSE, ASE, ISSTA
- Programming languages: POPL/PACMPL, PLDI/PACMPL, OOPSLA/PACMPL, ICFP/PACMPL
- Artificial intelligence: NeurIPS, ICML, ICLR, AAAI
- Systems: OSDI, SOSP, EuroSys, USENIX ATC, FAST, and adjacent ASPLOS

ACL-family, MLSys, NSDI, ICSA, journals, and pre-2024 papers may remain in dossier bibliographies only as `supplementary` or `out-of-ledger`; they are not counted as formal-ledger coverage.

## Completeness Boundary

The formal bibliography is exhaustive for the records collected from the declared sources in the 60 venue-years with a public proceedings or accepted-paper program. It is **not** an unconditional claim that every paper from every possible source has been recovered:

- six 2026 venue-years remain `pending`;
- ICLR 2025 and 2026 retain recorded count discrepancies;
- many venue-years have normalized proceedings metadata but no independent official count to reconcile against;
- ICML 2026 retains unresolved author-normalization metadata;
- 125 formal high-recall records still require abstract adjudication before dossier inclusion or exclusion is final.

The manifest records these limits explicitly. Accordingly, the formal source corpus is substantially exhaustive within the declared ledger, while the relevance mapping is not yet fully human-adjudicated.

## 2026 Frontier Sweep

The reproducible arXiv sweep covers first-posted records from 2026-01-01 through 2026-07-31 using two declared query universes:

- a broad LLM/foundation-model query over `cs.SE`, `cs.CR`, `cs.PL`, and `cs.OS`;
- a title-focused software, security, and agent-systems spillover query over `cs.AI`, `cs.CL`, and `cs.LG`.

| Stage | Count |
| --- | ---: |
| Raw query-result sum | 6,636 |
| Cross-query identity overlap | 1,077 |
| Unique query identities | 5,559 |
| Normalized candidate identities | 5,558 |
| High-confidence dossier-relevant frontier records | 2,556 |
| Ambiguous primary-object candidates requiring review | 560 |
| Superseded by a formal-ledger identity/title | 321 |
| Publication/acceptance metadata: supplementary or off-ledger | 721 |
| Withdrawn | 6 |
| Other out-of-boundary/background mentions | 1,394 |

The combined screened frontier bibliography contains 2,574 records: 2,560 from 2026, nine from 2025, and five from 2024. The four additional 2026 records were preserved from the earlier manually curated bibliographies but fall outside the two declared queries.

This is exhaustive for the exact queries recorded in the manifest. It is not exhaustive for every possible synonym, arXiv category, non-arXiv institutional repository, or author-hosted manuscript. Those sources require additional query manifests rather than being silently folded into this count.

## Rebuild

From the dossier parent directory:

```sh
python3 Literature-Corpus/scripts/build_corpus.py --refresh
python3 Literature-Corpus/scripts/validate_corpus.py
```

The builder uses only the Python standard library. Raw downloads are cached in `.cache/` and are deliberately not committed. A no-`--refresh` run is deterministic against that cache.

## Screening Semantics

Formal pass 1 applies high-recall title signals for LLMs, software/code, agent systems, and security. Existing manually reviewed dossier identities are preserved. Direct title conjunctions are included; ambiguous high-recall records remain `candidate` with `needs-abstract-review`, rather than being silently included or excluded. Pass 2 evidence and the rationale are recorded in `screening.csv`.

The screened formal BibTeX contains only `include` decisions. Candidate rows do not enter a dossier until an abstract/paper adjudication changes their decision. This makes incompleteness visible and prevents an unreviewed title match from being presented as established evidence.

Frontier screening uses titles, abstract leads, arXiv comments, DOI/journal metadata, and formal-corpus identities. A record enters the screened frontier only when the title names a dossier research object and the title or abstract lead establishes the LLM/agentic method. Records with an LLM-explicit title but only an abstract-level dossier object remain in the 560-row manual-review queue.

## Evidence and Identity Policy

Official proceedings/programs are the publication-status authority. DBLP supplies normalized proceedings metadata when available. DOI, DBLP identity, arXiv identity, and normalized title are deduplication keys. A verified venue version supersedes its preprint in formal coverage, while a retained supplementary record may preserve the arXiv identifier.

Evidence labels are:

- `formal-venue`: proceedings paper or official accepted-program record in the venue ledger;
- `frontier-preprint`: verified public preprint without a superseding formal identity;
- `supplementary` / `out-of-ledger`: useful pre-2024, journal, or adjacent evidence not counted toward formal coverage.

Officially accepted 2026 records may lack final pages or DOI data. They are labeled `accepted-program`; sentinel author metadata is permitted only where the official bulk program omitted authors, and the unresolved count is disclosed in the manifest.
