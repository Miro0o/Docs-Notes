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
    FORMAL_ADJUDICATIONS,
    FRONTIER_ADJUDICATIONS,
    GENERATED_SHELF_BEGIN,
    GENERATED_SHELF_END,
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

    mapping_by_identity = {
        (row["dossier"], row["citation_key"]): row for row in mappings
    }
    shelf_occurrences: dict[
        tuple[str, str], list[tuple[str, str, bool]]
    ] = defaultdict(list)
    generated_shelf_rows = 0
    layer_heading = {
        "### Formal Venue Papers": "formal-venue",
        "### Frontier Preprints": "frontier-preprint",
        "### Supplementary or Out-of-Ledger Evidence": "supplementary",
    }
    row_re = re.compile(r"^\|\s*([A-Za-z0-9_.:-]+)\s*\|")
    for dossier, directory in DOSSIERS.items():
        for path in sorted((directory / "Academic-Status").rglob("*.md")):
            generated = False
            current_layer = ""
            relative = path.relative_to(directory).as_posix()
            for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
                if line == GENERATED_SHELF_BEGIN:
                    if generated:
                        error(errors, f"nested generated shelf marker: {dossier}/{relative}")
                    generated = True
                    current_layer = ""
                    continue
                if line == GENERATED_SHELF_END:
                    if not generated:
                        error(errors, f"unmatched generated shelf end marker: {dossier}/{relative}")
                    generated = False
                    current_layer = ""
                    continue
                if generated and line in layer_heading:
                    current_layer = layer_heading[line]
                    continue
                match = row_re.match(line)
                if not match:
                    continue
                key = match.group(1)
                if key not in map_keys[dossier]:
                    continue
                shelf_occurrences[(dossier, key)].append(
                    (relative, current_layer, generated)
                )
                if generated:
                    generated_shelf_rows += 1
            if generated:
                error(errors, f"unclosed generated shelf marker: {dossier}/{relative}")

    for identity, row in mapping_by_identity.items():
        dossier, key = identity
        shelf_path = DOSSIERS[dossier] / row["shelf"]
        if not shelf_path.is_file():
            error(errors, f"mapping shelf does not exist: {dossier}/{key}: {row['shelf']}")
            continue
        occurrences = shelf_occurrences.get(identity, [])
        if len(occurrences) != 1:
            error(
                errors,
                f"canonical Academic-Status row count {len(occurrences)}: {dossier}/{key}",
            )
            continue
        relative, layer, generated = occurrences[0]
        if relative != row["shelf"]:
            error(
                errors,
                f"canonical row on wrong shelf: {dossier}/{key}: {relative} != {row['shelf']}",
            )
        if generated and layer != row["evidence_layer"]:
            error(
                errors,
                f"generated row in wrong evidence section: {dossier}/{key}: {layer} != {row['evidence_layer']}",
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

    active_shelf_keys = {
        row["citation_key"]
        for row in mappings
        if row["evidence_layer"] in {"formal-venue", "frontier-preprint"}
    }
    for ledger_name, rows in (
        ("formal", screening),
        ("frontier", frontier_screening),
    ):
        for row in rows:
            if row["decision"] != "include" and row["citation_key"] in active_shelf_keys:
                error(
                    errors,
                    f"{ledger_name} {row['decision']} row appears as active Academic-Status evidence: {row['citation_key']}",
                )

    adjudication_rows = read_csv(FORMAL_ADJUDICATIONS) + read_csv(FRONTIER_ADJUDICATIONS)
    human_adjudications = sum(bool(row.get("decision")) for row in adjudication_rows)
    checked_links = validate_links(errors)
    report = {
        "status": "pass" if not errors else "fail",
        "errors": len(errors),
        "source_corpus_exhaustiveness": "exhaustive-for-records-returned-by-declared-sources",
        "formal_records": len(exhaustive),
        "screened_formal_records": len(screened),
        "frontier_2026_query_candidates": len(exhaustive_frontier_2026),
        "frontier_2026_screened_includes": frontier_decisions["include"],
        "frontier_records": len(frontier),
        "mapping_rows": len(mappings),
        "academic_shelf_rows": sum(len(rows) for rows in shelf_occurrences.values()),
        "generated_academic_shelf_rows": generated_shelf_rows,
        "human_adjudications": human_adjudications,
        "formal_candidates_unresolved": sum(
            row["decision"] == "candidate" for row in screening
        ),
        "frontier_candidates_unresolved": frontier_decisions["candidate"],
        "screening_completeness": "incomplete"
        if any(row["decision"] == "candidate" for row in screening)
        or frontier_decisions["candidate"]
        else "complete",
        "mapping_completeness": "structurally-complete; manual-content-audit-incomplete",
        "manifest_rows": len(manifest),
        "pending_venue_years": sum(
            row["publication_status"] == "pending" for row in manifest
        ),
        "count_discrepancy_venue_years": sum(
            row["publication_status"] == "count-discrepancy" for row in manifest
        ),
        "non_pending_without_independent_official_count": sum(
            row["publication_status"] != "pending"
            and "independent official count unavailable" in row["reconciliation"]
            for row in manifest
        ),
        "unresolved_author_normalization_records": sum(
            int(match.group(1))
            for row in manifest
            if (
                match := re.search(
                    r"(\d+) program records retain author-normalization sentinel",
                    row["unresolved_metadata"],
                )
            )
        ),
        "local_links_checked": checked_links,
    }
    (CORPUS_DIR / "validation-report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
