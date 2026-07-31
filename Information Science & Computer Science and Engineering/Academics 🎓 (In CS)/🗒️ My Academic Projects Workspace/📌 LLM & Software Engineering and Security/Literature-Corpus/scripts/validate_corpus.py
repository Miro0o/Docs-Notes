#!/usr/bin/env python3
"""Validate corpus identities, BibTeX, mappings, manifest, and local links."""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote, urlparse

from build_corpus import (
    CORPUS_DIR,
    DOSSIERS,
    BIB_NAMES,
    PROJECT_DIR,
    VENUES,
    YEARS,
    identity_tokens,
    normalize_title,
    parse_bib_entries,
)


def error(errors: list[str], message: str) -> None:
    errors.append(message)
    print("ERROR:", message, file=sys.stderr)


def validate_bib(path: Path, errors: list[str]) -> list:
    records = parse_bib_entries(path)
    if not records:
        error(errors, f"{path}: no BibTeX records parsed")
        return []
    keys = Counter(record.key for record in records)
    for key, count in keys.items():
        if count > 1:
            error(errors, f"{path}: duplicate key {key} ({count})")
    identity_owner: dict[str, str] = {}
    for record in records:
        if not record.title or not record.author or not record.year:
            error(errors, f"{path}: {record.key} lacks title/author/year")
        if record.year < 1900 or record.year > 2026:
            error(errors, f"{path}: {record.key} has invalid year {record.year}")
        if record.url and urlparse(record.url).scheme not in {"http", "https"}:
            error(errors, f"{path}: {record.key} has invalid URL {record.url}")
        if record.doi and re.search(r"doi\.org/", record.doi, re.I):
            error(errors, f"{path}: {record.key} DOI field contains URL")
        for token in identity_tokens(record):
            if token in identity_owner:
                error(errors, f"{path}: duplicate identity {token}: {identity_owner[token]} / {record.key}")
            identity_owner[token] = record.key
    return records


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_links(errors: list[str]) -> int:
    checked = 0
    # CommonMark destinations may contain balanced parentheses (many paths in
    # this knowledge base do).  Support one nested level plus angle-bracket
    # destinations instead of truncating at the first closing parenthesis.
    link_re = re.compile(r"\[[^\]]+\]\((<[^>]+>|(?:[^()]|\([^()]*\))*)\)")
    for path in PROJECT_DIR.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in link_re.finditer(text):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target = target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            # Ignore template/wiki syntax and media formats not maintained by this corpus.
            if "{{" in target or "}}" in target:
                continue
            resolved = (path.parent / unquote(target)).resolve()
            checked += 1
            if not resolved.exists():
                error(errors, f"broken local link in {path.relative_to(PROJECT_DIR)}: {target}")
    return checked


def main() -> int:
    errors: list[str] = []
    exhaustive = validate_bib(CORPUS_DIR / "exhaustive-formal-venues.bib", errors)
    screened = validate_bib(CORPUS_DIR / "screened-formal-venues.bib", errors)
    exhaustive_frontier_2026 = validate_bib(
        CORPUS_DIR / "exhaustive-frontier-preprints-2026.bib", errors
    )
    frontier = validate_bib(CORPUS_DIR / "screened-frontier-preprints.bib", errors)
    dossier_records = {
        dossier: validate_bib(directory / BIB_NAMES[dossier], errors)
        for dossier, directory in DOSSIERS.items()
    }

    exhaustive_titles = {record.norm_title for record in exhaustive}
    screened_titles = {record.norm_title for record in screened}
    frontier_titles = {record.norm_title for record in frontier}
    missing = screened_titles - exhaustive_titles
    for title in sorted(missing):
        error(errors, f"screened formal title absent from exhaustive corpus: {title}")
    overlap = frontier_titles & exhaustive_titles
    for title in sorted(overlap):
        error(errors, f"frontier title also appears as formal venue: {title}")

    manifest = read_csv(CORPUS_DIR / "venue-year-manifest.csv")
    expected_cells = {(venue, str(year)) for venue in VENUES for year in YEARS}
    actual_cells = {(row["venue"], row["year"]) for row in manifest}
    if expected_cells != actual_cells:
        error(errors, f"manifest cells differ: missing={expected_cells - actual_cells}, extra={actual_cells - expected_cells}")
    for row in manifest:
        status = row["publication_status"]
        collected = int(row["collected_count"])
        if status == "pending" and collected != 0:
            error(errors, f"pending manifest row has records: {row['venue']} {row['year']}")
        if status != "pending" and collected == 0:
            error(errors, f"non-pending manifest row is empty: {row['venue']} {row['year']}")
        if not row["official_source_url"]:
            error(errors, f"manifest row lacks official source: {row['venue']} {row['year']}")

    mappings = read_csv(CORPUS_DIR / "dossier-mapping.csv")
    map_keys: dict[str, set[str]] = defaultdict(set)
    canonical_counts = Counter()
    for row in mappings:
        dossier = row["dossier"]
        key = row["citation_key"]
        map_keys[dossier].add(key)
        canonical_counts[(dossier, key)] += 1
        if row["evidence_layer"] not in {"formal-venue", "frontier-preprint", "supplementary"}:
            error(errors, f"invalid evidence layer: {dossier}/{key}")
        if row["canonical"] != "yes":
            error(errors, f"non-canonical mapping row in canonical table: {dossier}/{key}")
    for identity, count in canonical_counts.items():
        if count != 1:
            error(errors, f"canonical mapping count {count}: {identity[0]}/{identity[1]}")
    for dossier, records in dossier_records.items():
        bib_keys = {record.key for record in records}
        if bib_keys != map_keys[dossier]:
            error(
                errors,
                f"{dossier}: BibTeX/mapping mismatch missing_map={bib_keys-map_keys[dossier]} missing_bib={map_keys[dossier]-bib_keys}",
            )

    screening = read_csv(CORPUS_DIR / "screening.csv")
    screening_keys = {row["citation_key"] for row in screening}
    if screening_keys != {record.key for record in exhaustive}:
        error(errors, "screening table is not a one-row-per-formal-record ledger")
    for row in screening:
        if row["decision"] == "include" and row["citation_key"] not in {record.key for record in screened}:
            error(errors, f"included screening row absent from screened BibTeX: {row['citation_key']}")

    frontier_manifest = json.loads(
        (CORPUS_DIR / "frontier-query-manifest-2026.json").read_text(encoding="utf-8")
    )
    frontier_screening = read_csv(CORPUS_DIR / "frontier-screening-2026.csv")
    candidate_keys = {record.key for record in exhaustive_frontier_2026}
    frontier_screening_keys = {row["citation_key"] for row in frontier_screening}
    if candidate_keys != frontier_screening_keys:
        error(errors, "frontier screening is not a one-row-per-normalized-candidate ledger")
    if len(exhaustive_frontier_2026) != frontier_manifest["normalized_candidates"]:
        error(errors, "frontier manifest normalized-candidate count differs from BibTeX")
    if (
        frontier_manifest["raw_query_result_sum"]
        - frontier_manifest["cross_query_identity_overlap"]
        - frontier_manifest["normalization_deduplications"]
        != frontier_manifest["normalized_candidates"]
    ):
        error(errors, "frontier manifest query/deduplication reconciliation is inconsistent")
    frontier_decisions = Counter(row["decision"] for row in frontier_screening)
    if dict(frontier_decisions) != frontier_manifest["decision_counts"]:
        error(errors, "frontier manifest decision counts differ from the screening ledger")
    screened_frontier_arxiv = {record.arxiv for record in frontier if record.arxiv}
    for row in frontier_screening:
        if row["decision"] == "include" and row["arxiv_id"] not in screened_frontier_arxiv:
            error(
                errors,
                f"included frontier row absent from screened frontier BibTeX: {row['arxiv_id']}",
            )

    checked_links = validate_links(errors)
    report = {
        "status": "pass" if not errors else "fail",
        "errors": len(errors),
        "formal_records": len(exhaustive),
        "screened_formal_records": len(screened),
        "frontier_2026_query_candidates": len(exhaustive_frontier_2026),
        "frontier_2026_screened_includes": frontier_decisions["include"],
        "frontier_records": len(frontier),
        "mapping_rows": len(mappings),
        "manifest_rows": len(manifest),
        "local_links_checked": checked_links,
    }
    (CORPUS_DIR / "validation-report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
