#!/usr/bin/env python3
"""Build the frozen 2024--2026 formal-venue and dossier literature snapshot.

The script intentionally uses only the Python standard library.  Raw downloads
are cached under Literature-Corpus/.cache (ignored by git); normalized records,
the venue manifest, screening decisions, and dossier maps are checked in.

Usage:
    python3 Literature-Corpus/scripts/build_corpus.py --refresh
    python3 Literature-Corpus/scripts/build_corpus.py

The snapshot cutoff is 2026-07-31.  A venue-year with no public archival
program is emitted as ``pending`` rather than as a zero-paper edition.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Iterable
from urllib.parse import quote, unquote, urlencode, urljoin, urlparse


SNAPSHOT_DATE = "2026-07-31"
SCRIPT_DIR = Path(__file__).resolve().parent
CORPUS_DIR = SCRIPT_DIR.parent
PROJECT_DIR = CORPUS_DIR.parent
CACHE_DIR = CORPUS_DIR / ".cache"
FORMAL_ADJUDICATIONS = CORPUS_DIR / "formal-adjudications.csv"
FRONTIER_ADJUDICATIONS = CORPUS_DIR / "frontier-adjudications-2026.csv"

GENERATED_SHELF_BEGIN = "<!-- BEGIN GENERATED CANONICAL CORPUS ROWS -->"
GENERATED_SHELF_END = "<!-- END GENERATED CANONICAL CORPUS ROWS -->"

DOSSIERS = {
    "llm-software": PROJECT_DIR / "LLM-Software-Research-Dossier-2026",
    "software-for-llm": PROJECT_DIR / "Software-For-LLM-Agent-Systems-Research-Dossier-2026",
    "llm-security": PROJECT_DIR / "LLM-Software-Security-Research-Dossier-2026",
}

BIB_NAMES = {
    "llm-software": "LLM-Software-Research-Dossier-2026.bib",
    "software-for-llm": "Software-For-LLM-Agent-Systems-Research-Dossier-2026.bib",
    "llm-security": "LLM-Software-Security-Research-Dossier-2026.bib",
}

# Four baseline security-BibTeX anchors are intentionally bibliography-only.
# Every other baseline key has a canonical Markdown row and is recovered from
# that row when a generated dossier BibTeX is used as the next build input.
LEGACY_UNMAPPED_KEYS = {
    "Li2024CoSec",
    "Liang2025CKGLLM",
    "Zeng2024PromSec",
    "Zhao2025WebPoCStudy",
}

AREA_BY_VENUE = {
    "IEEE S&P": "Security",
    "USENIX Security": "Security",
    "ACM CCS": "Security",
    "NDSS": "Security",
    "ICSE": "Software Engineering",
    "FSE/PACMSE": "Software Engineering",
    "ASE": "Software Engineering",
    "ISSTA": "Software Engineering",
    "POPL/PACMPL": "Programming Languages",
    "PLDI/PACMPL": "Programming Languages",
    "OOPSLA/PACMPL": "Programming Languages",
    "ICFP/PACMPL": "Programming Languages",
    "NeurIPS": "Artificial Intelligence",
    "ICML": "Artificial Intelligence",
    "ICLR": "Artificial Intelligence",
    "AAAI": "Artificial Intelligence",
    "OSDI": "Systems",
    "SOSP": "Systems",
    "EuroSys": "Systems",
    "USENIX ATC": "Systems",
    "FAST": "Systems",
    "ASPLOS": "Systems",
}

VENUES = list(AREA_BY_VENUE)
YEARS = (2024, 2025, 2026)

FRONTIER_2026_QUERY = (
    'submittedDate:[202601010000 TO 202607312359] AND '
    '(cat:cs.SE OR cat:cs.CR OR cat:cs.PL OR cat:cs.OS) AND '
    '(all:"large language model" OR all:LLM OR all:"generative AI" '
    'OR all:"foundation model")'
)
FRONTIER_2026_SPILLOVER_QUERY = (
    'submittedDate:[202601010000 TO 202607312359] AND '
    '(cat:cs.AI OR cat:cs.CL OR cat:cs.LG) AND '
    '(all:"large language model" OR all:LLM OR all:"generative AI" '
    'OR all:"foundation model") AND '
    '((ti:software OR ti:code OR ti:coding OR ti:programming OR ti:developer '
    'OR ti:repository OR ti:compiler OR ti:testing OR ti:debugging OR ti:repair) '
    'OR (ti:cyber OR ti:vulnerability OR ti:malware OR ti:exploit OR ti:fuzzing '
    'OR ti:"prompt injection" OR ti:"supply chain" OR ti:MCP) '
    'OR ((ti:agentic OR ti:"LLM agent" OR ti:"language model agent") AND '
    '(ti:runtime OR ti:workflow OR ti:orchestration OR ti:testing OR ti:debugging '
    'OR ti:observability OR ti:architecture OR ti:protocol)))'
)
FRONTIER_2026_QUERIES = (
    ("core-categories", FRONTIER_2026_QUERY, ("cs.SE", "cs.CR", "cs.PL", "cs.OS")),
    (
        "ai-cl-lg-title-spillover",
        FRONTIER_2026_SPILLOVER_QUERY,
        ("cs.AI", "cs.CL", "cs.LG"),
    ),
)
FRONTIER_PAGE_SIZE = 500
FRONTIER_API_URL = "https://arxiv.org/api/query"

EXCLUDED_TRACK_RE = re.compile(
    r"\b(workshop|tutorial|poster|demo(?:nstration)?|doctoral|student research|"
    r"journal[- ]first|industry|industrial|invited|keynote|panel|companion|"
    r"new ideas|emerging results|src|artifact evaluation|education track|"
    r"blue sky|technical brief|late breaking)\b",
    re.I,
)
EXCLUDED_TITLE_RE = re.compile(
    r"^(preface|foreword|message from|conference report|front matter|"
    r"proceedings cover|title page|list of organizers)\b",
    re.I,
)

DIRECT_LLM_RE = re.compile(
    r"\b(large language model(?:s)?|language model(?:s)? for code|"
    r"code language model(?:s)?|llm(?:s)?|gpt(?:-\d+)?|chatgpt|"
    r"generative ai|foundation model(?:s)? for (?:code|software)|"
    r"ai coding|coding assistant(?:s)?|copilot)\b",
    re.I,
)
SOFTWARE_RE = re.compile(
    r"\b(code|coding|program(?:s|ming)?|software|developers?|repositories|github|"
    r"compil(?:e|er|ers|ation|ations|ing)|debug(?:ger|gers|ged|ging)?|bugs?|"
    r"repair(?:s|ed|ing)?|patch(?:es|ed|ing)?|test(?:ing|s)?|fuzz(?:ing|er|ers)?|"
    r"refactor(?:s|ed|ing)?|apis?|binar(?:y|ies)|decompil(?:e|er|ation|ing)|"
    r"reverse engineer(?:ing)?|formaliz(?:e|ed|ing|ation)|proofs?|theorems?|"
    r"verif(?:y|ied|ication)|specif(?:y|ied|ication)|requirements?|"
    r"documentation|configurations?|devops|kernels?|operating systems?|cloud|"
    r"packages?|dependencies|dependency)\b",
    re.I,
)
SECURITY_RE = re.compile(
    r"\b(secur(?:ity|e|ing)|vulnerab(?:le|ility|ilities)|"
    r"exploit(?:s|ed|ing|ation)?|malware|attacks?|defen[cs](?:e|ive)|privacy|"
    r"taint(?:ed|ing)?|pentest(?:ing)?|phishing|incidents?|soc|threats?|cves?|"
    r"weakness(?:es)?|jailbreak(?:s|ing)?|prompt injection|supply chain|"
    r"backdoors?|firmware)\b",
    re.I,
)
AGENT_SYSTEM_RE = re.compile(
    r"\b(agent(?:ic|s)? (?:system|software|application|workflow|runtime|"
    r"framework|testing|debugging|observability|orchestration)|prompt program|"
    r"language model program|llm application|llm system|tool[- ]using|"
    r"structured generation|constrained generation|schema|contract|"
    r"multi-agent (?:system|workflow)|rag (?:system|application)|"
    r"context management|agent protocol)\b",
    re.I,
)
HIGH_RECALL_RE = re.compile(
    r"\b(large language|llm|gpt|chatgpt|generative ai|foundation model|"
    r"coding assistant|software agent|code agent|repository agent|"
    r"program synthesis|neural program|prompt program|language model program|"
    r"agentic|multi-agent|tool[- ]use|retrieval.augmented generation|rag)\b",
    re.I,
)
FRONTIER_AGENT_RE = re.compile(
    r"\b(agentic|llm agent|language[- ]model agent|code agent|software agent|"
    r"repository agent|multi-agent|tool[- ](?:use|using|augmented)|mcp|"
    r"agent (?:system|framework|runtime|workflow|orchestration|architecture|"
    r"testing|debugging|observability|protocol)|rag system|"
    r"retrieval.augmented generation system|aiware|agentware)\b",
    re.I,
)
FRONTIER_SECURITY_OBJECT_RE = re.compile(
    r"\b(code|coding|software|repositories|repository|developers?|cyber|"
    r"vulnerab(?:le|ility|ilities)|cves?|cwes?|exploit(?:s|ed|ing|ation)?|"
    r"malware|fuzz(?:ing|er|ers)?|patch(?:es|ed|ing)?|binar(?:y|ies)|"
    r"decompil(?:e|er|ation|ing)|reverse engineer(?:ing)?|firmware|kernels?|"
    r"operating systems?|packages?|dependencies|dependency|supply chain|prompt injection|"
    r"rag|retrieval.augmented generation|agent|tool[- ]use|mcp|pentest|soc|"
    r"incident response|threat intelligence|security rule)\b",
    re.I,
)
FRONTIER_ACCEPTED_RE = re.compile(
    r"\b(accepted (?:at|to|by)|to appear (?:at|in)|published (?:at|in))\b",
    re.I,
)
FRONTIER_PRIMARY_SOFTWARE_RE = re.compile(
    r"\b(source code|code (?:generation|completion|translation|repair|review|"
    r"analysis|search|retrieval|summari[sz]ation)|coding|software|developers?|"
    r"repositories|repository|github|compil(?:e|er|ation|ing)|"
    r"debug(?:ger|ged|ging)?|bugs?|program repair|patch(?:es|ed|ing)?|"
    r"unit tests?|software tests?|fuzz(?:ing|er)?|refactor(?:ing)?|apis?|"
    r"binar(?:y|ies)|decompil(?:e|er|ation|ing)|reverse engineering|"
    r"proof assistant|theorem prover|program verification|requirements? "
    r"engineering|devops|kernels?|operating systems?|package dependencies|"
    r"software supply chain)\b",
    re.I,
)
FRONTIER_PRIMARY_SECURITY_RE = re.compile(
    r"\b(cyber(?:security)?|software security|code security|vulnerab(?:le|ility|ilities)|"
    r"cves?|cwes?|malware|fuzz(?:ing|er)?|pentest(?:ing)?|penetration testing|"
    r"exploit(?:s|ed|ing|ation)?|prompt injection|tool injection|rag poisoning|"
    r"retrieval poisoning|agent security|agentic security|security of (?:llm|ai) "
    r"(?:agents?|systems?|applications?)|supply.chain attack|app(?:lication)? rce)\b",
    re.I,
)
FRONTIER_PRIMARY_AGENT_ENGINEERING_RE = re.compile(
    r"\b(agent|agentic|llm|language.model|rag|retrieval.augmented generation)"
    r".{0,35}\b(runtime|framework|workflow|orchestrat(?:ion|or)|architecture|"
    r"protocol|observability|debugging|testing|platform|sandbox|isolation|"
    r"deployment|tool(?:ing| use)|mcp|memory system|context management)\b|"
    r"\b(runtime|framework|workflow|orchestrat(?:ion|or)|architecture|protocol|"
    r"observability|debugging|testing|platform|sandbox|isolation|deployment|"
    r"tool(?:ing| use)|mcp|memory system|context management).{0,35}"
    r"\b(agent|agentic|llm|language.model|rag|retrieval.augmented generation)\b",
    re.I,
)
FRONTIER_NON_DOSSIER_PRIMARY_RE = re.compile(
    r"\b(medical|medicine|clinical|diagnos(?:is|tic)|disease|patient|"
    r"health(?:care)?|protein|drug|"
    r"molecular|genom(?:e|ic)|biolog(?:y|ical)|radiolog(?:y|ical)|"
    r"image|vision|video|robot(?:s|ics)?|autonomous driving|vehicle|navigation|"
    r"recommender|recommendation|financial?|education|tutor|social media|"
    r"misinformation|weather|climate|agricultur(?:e|al)|chemistry|"
    r"police|policing|law enforcement|social vulnerability|"
    r"test[- ]time (?:scaling|compute|adaptation|training|inference))\b",
    re.I,
)

SHELF_RULES = {
    "llm-security": [
        (r"fuzz|dynamic analys|harness|mutator", "Academic-Status/Security-Analysis/Program-Analysis.md"),
        (r"static analys|taint|symbolic|concolic|binary|decompil|malware", "Academic-Status/Security-Analysis/Program-Analysis.md"),
        (r"repair|patch", "Academic-Status/Vulnerability-Lifecycle/Security-Repair-And-Patch-Validation.md"),
        (r"detect|triage|vulnerab|cve|weakness", "Academic-Status/Vulnerability-Lifecycle/Detection-Triage-And-Reasoning.md"),
        (r"pentest|ctf|offensive|exploit", "Academic-Status/Cyber-Operations/Offensive-CTF-And-Pentesting.md"),
        (r"soc|incident|threat|defensive", "Academic-Status/Cyber-Operations/Defensive-SOC-And-CTI.md"),
        (r"kernel|firmware|operating system|embedded|driver", "Academic-Status/Systems-And-OS-Security/Systems-And-OS-Security.md"),
        (r"package|dependency|supply chain|coding assistant", "Academic-Status/Security-Of-LLM-Software/Coding-Dependency-And-Supply-Chain.md"),
        (r"agent|rag|prompt injection|tool|mcp", "Academic-Status/Security-Of-LLM-Software/App-RAG-Agent-And-Tool-Runtimes.md"),
        (r"benchmark|evaluation|dataset", "Academic-Status/Cross-Cutting/Security-Benchmarks-And-Evaluation.md"),
        (r"survey|systemati[sz]", "Academic-Status/Cross-Cutting/Surveys-And-Systematization.md"),
    ],
    "software-for-llm": [
        (r"language|dsl|programming model|prompt program", "Academic-Status/Languages-DSLs-And-Programming-Models.md"),
        (r"contract|schema|structured|protocol|type", "Academic-Status/Types-Contracts-And-Structured-Interaction.md"),
        (r"compiler|runtime|workflow|orchestrat|schedule", "Academic-Status/Compilers-Runtimes-And-Workflow-Orchestration.md"),
        (r"test|debug|observ|trace|failure", "Academic-Status/Testing-Debugging-And-Observability.md"),
        (r"architect|evolution|operation|deploy|maintain", "Academic-Status/Architecture-Evolution-And-Operations.md"),
        (r"benchmark|survey|dataset|evaluation", "Academic-Status/Benchmarks-And-Surveys.md"),
    ],
    "llm-software": [
        (r"train|adapt|data|representation|embedding|code model", "Academic-Status/Code-Model-Training-Adaptation-Data-And-Representation.md"),
        (r"generat|completion|translat|transpil", "Academic-Status/Code-Generation-Completion-And-Translation.md"),
        (r"agent|repository|issue resol|swe-bench", "Academic-Status/Software-Agents-And-Repository-Engineering.md"),
        (r"review|traceability|governance|pull request", "Academic-Status/Code-Review-Change-Governance-And-Traceability.md"),
        (r"comprehension|retriev|search|document|api", "Academic-Status/Program-Comprehension-Search-Retrieval-Documentation-And-APIs.md"),
        (r"binary|decompil|reverse engineer", "Academic-Status/Program-Understanding-Binary-Analysis-Decompilation-And-Reverse-Engineering.md"),
        (r"proof|theorem|formaliz", "Academic-Status/Formalization-Proof-Engineering-And-Verified-Reasoning.md"),
        (r"analys|specification|verification|reasoning", "Academic-Status/Program-Analysis-Specification-Verification-And-Reasoning.md"),
        (r"test|debug|repair|bug", "Academic-Status/Testing-Debugging-And-General-Repair.md"),
        (r"performance|optim|compil", "Academic-Status/Performance-Optimization-And-Compilation.md"),
        (r"requirement|design|maint|evolution|migration|architecture", "Academic-Status/Requirements-Design-Maintenance-And-Evolution.md"),
        (r"refactor|technical debt|code smell|quality", "Academic-Status/Quality-Refactoring-Technical-Debt-And-Code-Smells.md"),
        (r"system|kernel|cloud|infrastructure|configuration|devops", "Academic-Status/Systems-OS-Cloud-And-Infrastructure-Software.md"),
        (r"education|developer|human|ui|ux|collabor", "Academic-Status/Human-Facing-Software-UI-UX-Education-And-Developer-Experience.md"),
        (r"domain|scientific|low.resource|data software", "Academic-Status/Domain-Specific-Low-Resource-Scientific-And-Data-Software.md"),
        (r"benchmark|dataset|evaluation", "Academic-Status/Benchmarks-Datasets-And-Evaluation.md"),
        (r"survey|systemati[sz]", "Academic-Status/Surveys-And-Systematization.md"),
    ],
}

DEFAULT_SHELF = {
    "llm-software": "Academic-Status/Code-Generation-Completion-And-Translation.md",
    "software-for-llm": "Academic-Status/Architecture-Evolution-And-Operations.md",
    "llm-security": "Academic-Status/Security-Analysis/Program-Analysis.md",
}


@dataclass
class Source:
    kind: str
    url: str
    filter_number: tuple[str, ...] = ()
    base_url: str = ""
    extra_urls: tuple[str, ...] = ()


@dataclass
class VenueYear:
    venue: str
    year: int
    official_url: str
    sources: list[Source] = field(default_factory=list)
    expected_count: int | None = None
    status_if_missing: str = "pending"
    note: str = ""


@dataclass
class Record:
    key: str = ""
    entry_type: str = "inproceedings"
    title: str = ""
    author: str = ""
    year: int = 0
    venue: str = ""
    area: str = ""
    booktitle: str = ""
    journal: str = ""
    volume: str = ""
    number: str = ""
    pages: str = ""
    publisher: str = ""
    doi: str = ""
    arxiv: str = ""
    url: str = ""
    dblp_key: str = ""
    source_url: str = ""
    source_kind: str = ""
    publication_status: str = "proceedings"
    track: str = ""
    abstract: str = ""
    comment: str = ""
    categories: tuple[str, ...] = ()
    keywords: set[str] = field(default_factory=set)
    raw_fields: dict[str, str] = field(default_factory=dict)

    @property
    def norm_title(self) -> str:
        return normalize_title(self.title)


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def strip_tags(value: str) -> str:
    return normalize_space(re.sub(r"<[^>]+>", " ", value or ""))


def normalize_title(value: str) -> str:
    value = unicodedata.normalize("NFKD", strip_tags(value)).casefold()
    value = re.sub(r"[\W_]+", "", value)
    return value


def ascii_token(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^A-Za-z0-9]+", "", value)


def bib_escape(value: str) -> str:
    # BibTeX braced values support nested braces and LaTeX commands directly.
    # Escaping them here is not only unnecessary: reparsing a generated dossier
    # bibliography and writing it again would double every backslash.
    return normalize_space(value)


def bib_unescape_generated(value: str) -> str:
    """Repair legacy generated values whose escapes doubled on every rebuild."""

    value = re.sub(r"\\+", r"\\", value or "")
    return value.replace(r"\{", "{").replace(r"\}", "}")


def source_cache_name(url: str) -> str:
    parsed = urlparse(url)
    stem = re.sub(r"[^A-Za-z0-9._-]+", "_", (parsed.netloc + parsed.path).strip("/"))
    digest = hashlib.sha1(url.encode()).hexdigest()[:10]
    suffix = Path(parsed.path).suffix or ".html"
    return f"{stem[:100]}-{digest}{suffix}"


def fetch(url: str, refresh: bool, delay: float = 0.7) -> Path:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    target = CACHE_DIR / source_cache_name(url)
    if target.exists() and target.stat().st_size and not refresh:
        return target
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "miniWorldModel-literature-audit/1.0",
            "Accept": "application/json, application/xml, text/html;q=0.9, */*;q=0.8",
        },
    )
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                data = response.read()
            if not data:
                raise RuntimeError(f"empty response: {url}")
            target.write_bytes(data)
            time.sleep(delay)
            return target
        except (urllib.error.URLError, TimeoutError, RuntimeError) as exc:
            last_error = exc
            time.sleep(2 ** attempt)
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def dblp_url(slug: str, page: str) -> str:
    return f"https://dblp.org/db/conf/{slug}/{page}.xml"


def journal_url(slug: str, page: str) -> str:
    return f"https://dblp.org/db/journals/{slug}/{page}.xml"


def build_venue_years() -> list[VenueYear]:
    official = {
        "IEEE S&P": "https://www.ieee-security.org/TC/SP-Index.html",
        "USENIX Security": "https://www.usenix.org/conferences/byname/108",
        "ACM CCS": "https://www.sigsac.org/ccs.html",
        "NDSS": "https://www.ndss-symposium.org/",
        "ICSE": "https://conf.researchr.org/series/icse",
        "FSE/PACMSE": "https://conf.researchr.org/series/fse",
        "ASE": "https://conf.researchr.org/series/ase",
        "ISSTA": "https://conf.researchr.org/series/issta",
        "POPL/PACMPL": "https://poplconf.org/",
        "PLDI/PACMPL": "https://pldi.sigplan.org/",
        "OOPSLA/PACMPL": "https://2026.splashcon.org/track/splash-2026-oopsla",
        "ICFP/PACMPL": "https://icfpconference.org/",
        "NeurIPS": "https://proceedings.neurips.cc/",
        "ICML": "https://icml.cc/",
        "ICLR": "https://iclr.cc/",
        "AAAI": "https://aaai.org/conference/aaai/",
        "OSDI": "https://www.usenix.org/conferences/byname/179",
        "SOSP": "https://sigops.org/s/conferences/sosp/",
        "EuroSys": "https://www.eurosys.org/",
        "USENIX ATC": "https://www.usenix.org/conferences/byname/131",
        "FAST": "https://www.usenix.org/conferences/byname/178",
        "ASPLOS": "https://www.asplos-conference.org/",
    }
    rows = [VenueYear(v, y, official[v]) for v in VENUES for y in YEARS]
    by = {(r.venue, r.year): r for r in rows}

    def add(venue: str, year: int, kind: str, url: str, **kwargs: object) -> None:
        by[(venue, year)].sources.append(Source(kind, url, **kwargs))

    for y in YEARS:
        add("IEEE S&P", y, "dblp", dblp_url("sp", f"sp{y}"))
        add("NDSS", y, "dblp", dblp_url("ndss", f"ndss{y}"))
        add("AAAI", y, "dblp", dblp_url("aaai", f"aaai{y}"))
        add("FAST", y, "dblp", dblp_url("fast", f"fast{y}"))

    for y in (2024, 2025):
        add("USENIX Security", y, "dblp", dblp_url("uss", f"uss{y}"))
        add("ACM CCS", y, "dblp", dblp_url("ccs", f"ccs{y}"))
        add("ICSE", y, "dblp", dblp_url("icse", f"icse{y}"))
        add("NeurIPS", y, "dblp", dblp_url("nips", f"neurips{y}"))
        add("OSDI", y, "dblp", dblp_url("osdi", f"osdi{y}"))
        add("SOSP", y, "dblp", dblp_url("sosp", f"sosp{y}"))
        add("EuroSys", y, "dblp", dblp_url("eurosys", f"eurosys{y}"))
        add("USENIX ATC", y, "dblp", dblp_url("usenix", f"usenix{y}"))

    add("ASE", 2024, "dblp", dblp_url("kbse", "ase2024"))
    add(
        "ASE",
        2025,
        "researchr",
        "https://conf.researchr.org/track/ase-2025/ase-2025-papers",
    )
    by[("ASE", 2025)].official_url = "https://conf.researchr.org/track/ase-2025/ase-2025-papers"

    add("ICML", 2024, "pmlr", "https://proceedings.mlr.press/v235/")
    add("ICML", 2025, "pmlr", "https://proceedings.mlr.press/v267/")

    for y, expected in ((2024, 2260), (2025, 3704)):
        add(
            "ICLR",
            y,
            "iclr_json",
            f"https://iclr.cc/static/virtual/data/iclr-{y}-orals-posters.json",
        )
        by[("ICLR", y)].official_url = f"https://iclr.cc/virtual/{y}/papers.html"
        by[("ICLR", y)].expected_count = expected

    add("FSE/PACMSE", 2024, "dblp", journal_url("pacmse", "pacmse1"), filter_number=("FSE",))
    add("FSE/PACMSE", 2025, "dblp", journal_url("pacmse", "pacmse2"), filter_number=("FSE",))
    add("ISSTA", 2024, "dblp", dblp_url("issta", "issta2024"))
    add("ISSTA", 2025, "dblp", journal_url("pacmse", "pacmse2"), filter_number=("ISSTA",))

    pacmpl = {2024: "pacmpl8", 2025: "pacmpl9", 2026: "pacmpl10"}
    for y in YEARS:
        add("POPL/PACMPL", y, "dblp", journal_url("pacmpl", pacmpl[y]), filter_number=("POPL",))
    for y in (2024, 2025):
        add("PLDI/PACMPL", y, "dblp", journal_url("pacmpl", pacmpl[y]), filter_number=("PLDI",))
        add("OOPSLA/PACMPL", y, "dblp", journal_url("pacmpl", pacmpl[y]), filter_number=("OOPSLA1", "OOPSLA2"))
        add("ICFP/PACMPL", y, "dblp", journal_url("pacmpl", pacmpl[y]), filter_number=("ICFP",))

    asplos_pages = {
        2024: ("asplos2024-1", "asplos2024-2", "asplos2024-3", "asplos2024-4"),
        2025: ("asplos2025-1", "asplos2025-2", "asplos2025-3"),
        2026: ("asplos2026-1", "asplos2026-2"),
    }
    for y, pages in asplos_pages.items():
        for page in pages:
            add("ASPLOS", y, "dblp", dblp_url("asplos", page))

    researchr = {
        "ICSE": "https://conf.researchr.org/track/icse-2026/icse-2026-research-track",
        "FSE/PACMSE": "https://conf.researchr.org/track/fse-2026/fse-2026-research-papers",
        "ISSTA": "https://conf.researchr.org/track/issta-2026/issta-2026-research-papers",
        "PLDI/PACMPL": "https://pldi26.sigplan.org/track/pldi-2026-papers",
        "ICFP/PACMPL": "https://conf.researchr.org/track/icfp-2026/icfp-2026-icfp-papers",
    }
    for venue, url in researchr.items():
        add(venue, 2026, "researchr", url)
        by[(venue, 2026)].official_url = url

    add("ICLR", 2026, "iclr_json", "https://iclr.cc/static/virtual/data/iclr-2026-orals-posters.json")
    by[("ICLR", 2026)].official_url = "https://iclr.cc/virtual/2026/papers.html"
    by[("ICLR", 2026)].expected_count = 5357
    by[("ICLR", 2026)].note = "Official fact sheet reports 5,357; title deduplication may expose feed discrepancies."

    add(
        "ICML",
        2026,
        "icml_program",
        "https://icml.cc/virtual/2026/papers.html",
        extra_urls=("https://icml.cc/static/virtual/data/icml-2026-orals-posters.json",),
    )
    by[("ICML", 2026)].official_url = "https://icml.cc/virtual/2026/papers.html"

    add("EuroSys", 2026, "eurosys", "https://2026.eurosys.org/papers.html")
    by[("EuroSys", 2026)].official_url = "https://2026.eurosys.org/papers.html"
    by[("EuroSys", 2026)].note = "Official page combines both submission periods; earlier first-period reports list 59 papers."

    add("OSDI", 2026, "usenix", "https://www.usenix.org/conference/osdi26/technical-sessions")
    by[("OSDI", 2026)].official_url = "https://www.usenix.org/conference/osdi26/technical-sessions"
    by[("OSDI", 2026)].note = (
        "Official technical-sessions page also contains a keynote; the parser "
        "retains only archival research-paper sessions."
    )

    add("USENIX Security", 2026, "usenix", "https://www.usenix.org/conference/usenixsecurity26/technical-sessions")
    by[("USENIX Security", 2026)].official_url = "https://www.usenix.org/conference/usenixsecurity26/technical-sessions"
    by[("USENIX Security", 2026)].note = (
        "Official technical-sessions page also contains the non-archival Enigma "
        "track; the parser retains only refereed research-paper sessions."
    )

    by[("OOPSLA/PACMPL", 2026)].note = "No complete public archival issue/program located by the cutoff."
    by[("NeurIPS", 2026)].note = "Reviews were in progress at the cutoff; no accepted-paper program."
    by[("ACM CCS", 2026)].note = "No complete accepted-paper program located by the cutoff."
    by[("ASE", 2026)].note = "The archival research program was not public by the cutoff."
    by[("SOSP", 2026)].note = "No complete accepted-paper program located by the cutoff."
    by[("USENIX ATC", 2026)].note = "No public archival program by the cutoff; venue transition remains unresolved."
    return rows


def element_text(element: ET.Element | None) -> str:
    if element is None:
        return ""
    return normalize_space("".join(element.itertext()))


def parse_dblp(path: Path, spec: VenueYear, source: Source) -> list[Record]:
    root = ET.parse(path).getroot()
    records: list[Record] = []

    def walk(node: ET.Element, section: str = "") -> None:
        current = section
        for child in node:
            tag = child.tag.rsplit("}", 1)[-1]
            if tag in {"h2", "h3"}:
                current = element_text(child)
                continue
            if tag == "r":
                paper = next(
                    (candidate for candidate in child if candidate.tag.rsplit("}", 1)[-1] in {"article", "inproceedings"}),
                    None,
                )
                if paper is not None:
                    record = record_from_dblp_element(paper, spec, source, current)
                    if record is not None:
                        records.append(record)
                continue
            walk(child, current)

    walk(root)
    return records


def record_from_dblp_element(
    paper: ET.Element, spec: VenueYear, source: Source, section: str
) -> Record | None:
    values: dict[str, list[str]] = defaultdict(list)
    for child in paper:
        values[child.tag.rsplit("}", 1)[-1]].append(element_text(child))
    title = values["title"][0] if values["title"] else ""
    if not title or EXCLUDED_TITLE_RE.search(title) or EXCLUDED_TRACK_RE.search(section):
        return None
    number = values["number"][0] if values["number"] else ""
    if source.filter_number and number not in source.filter_number:
        return None
    try:
        year = int(values["year"][0])
    except (ValueError, IndexError):
        year = spec.year
    if year != spec.year:
        return None
    if spec.venue == "AAAI" and not is_aaai_archival_track(
        section, values["pages"][0] if values["pages"] else ""
    ):
        return None
    ee_values = values.get("ee", [])
    doi = ""
    for candidate in ee_values:
        match = re.search(r"(?:doi\.org/|doi:)(10\.\d{4,9}/\S+)", candidate, re.I)
        if match:
            doi = match.group(1).rstrip(".,)")
            break
    url = next((value for value in ee_values if value.startswith("http")), "")
    dblp_key = paper.attrib.get("key", "")
    if not url and dblp_key:
        url = f"https://dblp.org/rec/{dblp_key}"
    entry_type = paper.tag.rsplit("}", 1)[-1]
    author = " and ".join(values.get("author", []))
    return Record(
        entry_type=entry_type,
        title=title,
        author=author,
        year=year,
        venue=spec.venue,
        area=AREA_BY_VENUE[spec.venue],
        booktitle=values["booktitle"][0] if values["booktitle"] else (spec.venue if entry_type == "inproceedings" else ""),
        journal=values["journal"][0] if values["journal"] else "",
        volume=values["volume"][0] if values["volume"] else "",
        number=number,
        pages=values["pages"][0] if values["pages"] else "",
        publisher=values["publisher"][0] if values["publisher"] else "",
        doi=doi,
        url=url,
        dblp_key=dblp_key,
        source_url=source.url,
        source_kind="DBLP TOC",
        publication_status="proceedings",
        track=section,
        keywords={"formal-venue"},
    )


def page_span(pages: str) -> int:
    values = [int(value) for value in re.findall(r"\d+", pages or "")]
    return values[-1] - values[0] + 1 if len(values) >= 2 else 0


def is_aaai_archival_track(section: str, pages: str) -> bool:
    """Keep AAAI technical/special research, not colocated or presentation tracks.

    Some 2025/2026 DBLP volume headings combine AI-for-Social-Impact full
    research papers with short Senior Member presentations.  The full papers
    are seven or more pages; the presentation summaries are shorter.
    """
    if re.match(r"(?:AAAI )?Technical Tracks?\b", section, re.I):
        return True
    if re.search(r"Special Track (?:on )?AI Alignment", section, re.I):
        return True
    if re.search(r"AI for Social Impact", section, re.I):
        return page_span(pages) >= 7
    return False


def parse_researchr(path: Path, spec: VenueYear, source: Source) -> list[Record]:
    text = path.read_text(encoding="utf-8", errors="replace")
    rows = re.findall(
        r'<tr>.*?<a href="#" data-event-modal="([^"]+)">(.*?)</a>'
        r'<div class="prog-track">(.*?)</div><div class="performers">(.*?)</div>.*?</td></tr>',
        text,
        re.S,
    )
    records: list[Record] = []
    seen: set[str] = set()
    for event_id, raw_title, raw_track, raw_authors in rows:
        title = strip_tags(raw_title)
        track = strip_tags(raw_track)
        if not title or normalize_title(title) in seen:
            continue
        if EXCLUDED_TRACK_RE.search(track) or EXCLUDED_TITLE_RE.search(title):
            continue
        if spec.venue == "ICFP/PACMPL" and re.search(r"\((?:Functional Pearl|Experience Report)\)", title, re.I):
            continue
        authors = [
            strip_tags(value)
            for value in re.findall(r'class="navigate">(.*?)</a>', raw_authors, re.S)
            if strip_tags(value)
        ]
        seen.add(normalize_title(title))
        records.append(
            Record(
                title=title,
                author=" and ".join(authors) or f"{spec.venue} {spec.year} program record",
                year=spec.year,
                venue=spec.venue,
                area=AREA_BY_VENUE[spec.venue],
                booktitle=spec.venue,
                url=f"{source.url}#event-{event_id}",
                source_url=source.url,
                source_kind="official accepted-paper program",
                publication_status="accepted-program",
                track=track,
                keywords={"formal-venue", "accepted-program"},
            )
        )
    return records


def parse_iclr_json(path: Path, spec: VenueYear, source: Source) -> list[Record]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    results = payload.get("results", payload if isinstance(payload, list) else [])
    grouped: dict[str, dict] = {}
    for item in results:
        if item.get("sourceurl") != f"https://openreview.net/group?id=ICLR.cc/{spec.year}/Conference":
            continue
        norm = normalize_title(item.get("name", ""))
        if not norm:
            continue
        previous = grouped.get(norm)
        if previous is None or item.get("eventtype", "").casefold() == "poster":
            grouped[norm] = item
    records: list[Record] = []
    for item in grouped.values():
        authors = [author.get("fullname", "") for author in item.get("authors", [])]
        records.append(
            Record(
                title=normalize_space(item.get("name", "")),
                author=" and ".join(filter(None, authors)),
                year=spec.year,
                venue=spec.venue,
                area=AREA_BY_VENUE[spec.venue],
                booktitle="International Conference on Learning Representations",
                url=item.get("paper_url") or urljoin("https://iclr.cc", item.get("virtualsite_url", "")),
                source_url=source.url,
                source_kind="official conference JSON",
                publication_status="accepted-program",
                track=item.get("decision", ""),
                keywords={"formal-venue", "accepted-program"},
            )
        )
    return records


def parse_pmlr(path: Path, spec: VenueYear, source: Source) -> list[Record]:
    text = path.read_text(encoding="utf-8", errors="replace")
    blocks = re.findall(r'<div class="paper">(.*?)</div>', text, re.S)
    records: list[Record] = []
    for block in blocks:
        title_match = re.search(r'<p class="title">(.*?)</p>', block, re.S)
        authors_match = re.search(r'<span class="authors">(.*?)</span>', block, re.S)
        info_match = re.search(r'<span class="info">(.*?)</span>', block, re.S)
        url_match = re.search(r'\[<a href="([^"]+)">abs</a>\]', block, re.S)
        if not title_match or not authors_match or not url_match:
            continue
        title = strip_tags(title_match.group(1))
        authors = [
            normalize_space(value)
            for value in re.split(r",|&nbsp;", strip_tags(authors_match.group(1)))
            if normalize_space(value)
        ]
        info = strip_tags(info_match.group(1)) if info_match else ""
        pages_match = re.search(r"PMLR\s+\d+:([0-9-]+)", info)
        volume_match = re.search(r"PMLR\s+(\d+)", info)
        records.append(
            Record(
                title=title,
                author=" and ".join(authors),
                year=spec.year,
                venue=spec.venue,
                area=AREA_BY_VENUE[spec.venue],
                booktitle=f"International Conference on Machine Learning",
                volume=volume_match.group(1) if volume_match else "",
                pages=pages_match.group(1) if pages_match else "",
                url=html.unescape(url_match.group(1)),
                source_url=source.url,
                source_kind="official PMLR proceedings",
                publication_status="proceedings",
                track="main conference proceedings",
                keywords={"formal-venue"},
            )
        )
    return records


def parse_icml_program(
    path: Path, spec: VenueYear, source: Source, refresh: bool
) -> list[Record]:
    text = path.read_text(encoding="utf-8", errors="replace")
    links = re.findall(
        r'<li><a href="(/virtual/2026/(?:poster|oral|spotlight)/\d+)">(.*?)</a></li>',
        text,
        re.S,
    )
    authors_by_title: dict[str, str] = {}
    if source.extra_urls:
        try:
            json_path = fetch(source.extra_urls[0], refresh)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            for item in payload.get("results", []):
                if item.get("sourceurl") != "https://openreview.net/group?id=ICML.cc/2026/Conference":
                    continue
                authors_by_title[normalize_title(item.get("name", ""))] = " and ".join(
                    author.get("fullname", "") for author in item.get("authors", []) if author.get("fullname")
                )
        except RuntimeError:
            pass
    records: list[Record] = []
    seen: set[str] = set()
    for href, raw_title in links:
        title = strip_tags(raw_title)
        norm = normalize_title(title)
        if not norm or norm in seen or title.casefold().startswith("position:"):
            continue
        seen.add(norm)
        records.append(
            Record(
                title=title,
                author=authors_by_title.get(norm) or "ICML 2026 program record (authors pending normalization)",
                year=spec.year,
                venue=spec.venue,
                area=AREA_BY_VENUE[spec.venue],
                booktitle="International Conference on Machine Learning",
                url=urljoin("https://icml.cc", href),
                source_url=source.url,
                source_kind="official conference program",
                publication_status="accepted-program",
                track="main conference; position papers excluded by title/track",
                keywords={"formal-venue", "accepted-program"},
            )
        )
    return records


def parse_eurosys(path: Path, spec: VenueYear, source: Source) -> list[Record]:
    text = path.read_text(encoding="utf-8", errors="replace")
    rows = re.findall(
        r"<tr>\s*<td><a href=\"([^\"]+)\">(.*?)</a></td>\s*<td>(.*?)</td>\s*</tr>",
        text,
        re.S,
    )
    records: list[Record] = []
    for url, raw_title, raw_authors in rows:
        title = strip_tags(raw_title)
        author_text = strip_tags(raw_authors)
        authors = [
            normalize_space(match)
            for match in re.findall(r"(?:^|,\s*)([^(),]+?)\s*\([^)]*\)", author_text)
        ]
        doi_match = re.search(r"doi\.org/(10\.\d{4,9}/\S+)", url, re.I)
        records.append(
            Record(
                title=title,
                author=" and ".join(authors) or "EuroSys 2026 program record",
                year=spec.year,
                venue=spec.venue,
                area=AREA_BY_VENUE[spec.venue],
                booktitle="European Conference on Computer Systems",
                doi=doi_match.group(1) if doi_match else "",
                url=url,
                source_url=source.url,
                source_kind="official accepted-paper page",
                publication_status="proceedings" if doi_match else "accepted-program",
                keywords={"formal-venue"} | ({"accepted-program"} if not doi_match else set()),
            )
        )
    return records


def parse_usenix(path: Path, spec: VenueYear, source: Source) -> list[Record]:
    text = path.read_text(encoding="utf-8", errors="replace")
    blocks: list[str] = []
    session_chunks = re.split(
        r'(?=<article[^>]+class="node node-session view-mode-schedule")',
        text,
    )[1:]
    excluded_session_re = re.compile(
        r"\b(enigma|keynote|test of time|award|discussion|panel|poster)\b",
        re.I,
    )
    for session in session_chunks:
        session_title_match = re.search(r"<h2>(.*?)</h2>", session, re.S)
        session_title = (
            strip_tags(session_title_match.group(1)) if session_title_match else ""
        )
        if excluded_session_re.search(session_title):
            continue
        blocks.extend(
            re.findall(
                r'<article[^>]+class="node node-paper view-mode-schedule".*?</article>',
                session,
                re.S,
            )
        )
    records: list[Record] = []
    seen: set[str] = set()
    for block in blocks:
        title_match = re.search(r"<h2>\s*<a href=\"([^\"]+)\">(.*?)</a>\s*</h2>", block, re.S)
        people_match = re.search(
            r"field-name-field-paper-people-text.*?<p>(.*?)</p>", block, re.S
        )
        if not title_match:
            continue
        title = strip_tags(title_match.group(2))
        norm = normalize_title(title)
        if not norm or norm in seen:
            continue
        seen.add(norm)
        raw_people = people_match.group(1) if people_match else ""
        author_chunks = re.findall(r"(?:^|</em>)\s*([^<]+?),\s*<em>", raw_people)
        authors: list[str] = []
        for chunk in author_chunks:
            chunk = strip_tags(chunk).strip(" ,;")
            for name in re.split(r"\s+(?:and|&)\s+|,\s+(?=[A-Z][A-Za-z.'’-]+\s+[A-Z])", chunk):
                name = normalize_space(name).strip(" ,;")
                if name:
                    authors.append(name)
        href = urljoin("https://www.usenix.org", html.unescape(title_match.group(1)))
        records.append(
            Record(
                title=title,
                author=" and ".join(authors) or f"{spec.venue} {spec.year} program record",
                year=spec.year,
                venue=spec.venue,
                area=AREA_BY_VENUE[spec.venue],
                booktitle=spec.venue,
                url=href,
                source_url=source.url,
                source_kind="official technical-sessions page",
                publication_status="proceedings",
                keywords={"formal-venue"},
            )
        )
    return records


def frontier_page_url(start: int, query: str = FRONTIER_2026_QUERY) -> str:
    return FRONTIER_API_URL + "?" + urlencode(
        {
            "search_query": query,
            "start": start,
            "max_results": FRONTIER_PAGE_SIZE,
            "sortBy": "submittedDate",
            "sortOrder": "ascending",
        }
    )


def parse_arxiv_frontier_page(
    path: Path, query: str = FRONTIER_2026_QUERY
) -> tuple[list[Record], int]:
    namespaces = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom",
        "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
    }
    root = ET.parse(path).getroot()
    try:
        total = int(root.findtext("opensearch:totalResults", "0", namespaces))
    except ValueError:
        total = 0
    records: list[Record] = []
    for entry in root.findall("atom:entry", namespaces):
        raw_id = entry.findtext("atom:id", "", namespaces)
        arxiv_match = re.search(r"/abs/([^v/?]+)", raw_id)
        if not arxiv_match:
            continue
        arxiv_id = arxiv_match.group(1)
        published = entry.findtext("atom:published", "", namespaces)
        if not published.startswith("2026-"):
            continue
        authors = [
            normalize_space(author.findtext("atom:name", "", namespaces))
            for author in entry.findall("atom:author", namespaces)
        ]
        categories = tuple(
            category.get("term", "")
            for category in entry.findall("atom:category", namespaces)
            if category.get("term")
        )
        doi = entry.findtext("arxiv:doi", "", namespaces)
        journal_ref = entry.findtext("arxiv:journal_ref", "", namespaces)
        comment = entry.findtext("arxiv:comment", "", namespaces)
        records.append(
            Record(
                entry_type="misc",
                title=entry.findtext("atom:title", "", namespaces),
                author=" and ".join(author for author in authors if author),
                year=2026,
                venue="arXiv",
                area="Frontier preprint",
                booktitle="arXiv",
                doi=normalize_space(doi),
                arxiv=arxiv_id,
                url=f"https://arxiv.org/abs/{arxiv_id}",
                source_url=frontier_page_url(0, query),
                source_kind="official arXiv API",
                publication_status="frontier-candidate",
                track=";".join(categories),
                abstract=entry.findtext("atom:summary", "", namespaces),
                comment=comment,
                categories=categories,
                keywords={"frontier-candidate", "arxiv-2026"},
                raw_fields={"journal_ref": journal_ref, "published": published},
            )
        )
    return records, total


def collect_arxiv_frontier_2026(refresh: bool) -> tuple[list[Record], dict[str, object]]:
    query_rows: list[dict[str, object]] = []
    all_query_records: list[Record] = []
    for name, query, categories in FRONTIER_2026_QUERIES:
        first_path = fetch(frontier_page_url(0, query), refresh, delay=3.0)
        first_records, total = parse_arxiv_frontier_page(first_path, query)
        if not total:
            raise RuntimeError(f"arXiv frontier query {name} returned no totalResults")
        query_records = list(first_records)
        for start in range(FRONTIER_PAGE_SIZE, total, FRONTIER_PAGE_SIZE):
            path = fetch(frontier_page_url(start, query), refresh, delay=3.0)
            page_records, page_total = parse_arxiv_frontier_page(path, query)
            if page_total != total:
                raise RuntimeError(
                    f"arXiv frontier pagination for {name} changed totalResults: "
                    f"{total} -> {page_total}"
                )
            query_records.extend(page_records)
        query_by_arxiv = {record.arxiv: record for record in query_records}
        if len(query_by_arxiv) != total:
            raise RuntimeError(
                f"arXiv frontier query {name} expected {total} identities but "
                f"normalized {len(query_by_arxiv)}"
            )
        all_query_records.extend(query_by_arxiv.values())
        query_rows.append(
            {
                "name": name,
                "query": query,
                "categories": list(categories),
                "query_results": total,
            }
        )
    by_arxiv: dict[str, Record] = {}
    for record in all_query_records:
        by_arxiv.setdefault(record.arxiv, record)
    unique_query_identities = len(by_arxiv)
    records, _ = deduplicate(by_arxiv.values())
    return records, {
        "snapshot_date": SNAPSHOT_DATE,
        "source": FRONTIER_API_URL,
        "queries": query_rows,
        "first_posted_from": "2026-01-01T00:00:00Z",
        "first_posted_through": "2026-07-31T23:59:59Z",
        "raw_query_result_sum": sum(row["query_results"] for row in query_rows),
        "cross_query_identity_overlap": len(all_query_records) - unique_query_identities,
        "unique_query_identities": unique_query_identities,
        "normalization_deduplications": unique_query_identities - len(records),
        "page_size": FRONTIER_PAGE_SIZE,
        "retrieval_date": SNAPSHOT_DATE,
        "scope_note": (
            "Exhaustive for the two declared arXiv query universes, not for every "
            "repository or every synonym that may describe LLM-related work."
        ),
    }


PARSERS = {
    "dblp": parse_dblp,
    "researchr": parse_researchr,
    "iclr_json": parse_iclr_json,
    "pmlr": parse_pmlr,
    "eurosys": parse_eurosys,
    "usenix": parse_usenix,
}


def parse_source(
    source: Source, spec: VenueYear, refresh: bool
) -> tuple[list[Record], str]:
    try:
        path = fetch(source.url, refresh)
        if source.kind == "icml_program":
            return parse_icml_program(path, spec, source, refresh), ""
        parser = PARSERS[source.kind]
        return parser(path, spec, source), ""
    except (RuntimeError, ET.ParseError, json.JSONDecodeError, OSError) as exc:
        return [], str(exc)


def parse_bib_entries(path: Path) -> list[Record]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    entries: list[Record] = []
    cursor = 0
    entry_re = re.compile(r"@([A-Za-z]+)\s*[{(]\s*([^,\s]+)\s*,")
    while True:
        match = entry_re.search(text, cursor)
        if not match:
            break
        if match.group(1).casefold() in {"comment", "string", "preamble"}:
            cursor = match.end()
            continue
        start = match.start()
        body_start = match.end()
        depth = 1
        index = body_start
        while index < len(text) and depth:
            if text[index] == "{":
                depth += 1
            elif text[index] == "}":
                depth -= 1
            index += 1
        raw = text[start:index]
        fields = parse_bib_fields(raw[raw.find(",") + 1 : -1])
        try:
            year = int(re.sub(r"\D", "", fields.get("year", "0"))[:4] or 0)
        except ValueError:
            year = 0
        url = fields.get("url", "")
        arxiv = fields.get("eprint", "")
        if not arxiv:
            arxiv_match = re.search(r"arxiv\.(?:org/(?:abs|pdf)/|)(\d{4}\.\d{4,5})", url, re.I)
            arxiv = arxiv_match.group(1) if arxiv_match else ""
        entries.append(
            Record(
                key=match.group(2),
                entry_type=match.group(1).casefold(),
                title=fields.get("title", ""),
                author=fields.get("author", ""),
                year=year,
                booktitle=fields.get("booktitle", ""),
                journal=fields.get("journal", ""),
                volume=fields.get("volume", ""),
                number=fields.get("number", ""),
                pages=fields.get("pages", ""),
                publisher=fields.get("publisher", ""),
                doi=fields.get("doi", ""),
                arxiv=arxiv,
                url=url,
                raw_fields=fields,
            )
        )
        cursor = index
    return entries


def parse_bib_fields(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    index = 0
    while index < len(body):
        match = re.search(r"([A-Za-z][A-Za-z0-9_-]*)\s*=\s*", body[index:])
        if not match:
            break
        name = match.group(1).casefold()
        value_start = index + match.end()
        if value_start >= len(body):
            break
        opener = body[value_start]
        if opener == "{":
            depth = 1
            pos = value_start + 1
            while pos < len(body) and depth:
                if body[pos] == "{" and (pos == 0 or body[pos - 1] != "\\"):
                    depth += 1
                elif body[pos] == "}" and (pos == 0 or body[pos - 1] != "\\"):
                    depth -= 1
                pos += 1
            value = body[value_start + 1 : pos - 1]
        elif opener == '"':
            pos = value_start + 1
            while pos < len(body):
                if body[pos] == '"' and body[pos - 1] != "\\":
                    break
                pos += 1
            value = body[value_start + 1 : pos]
            pos += 1
        else:
            end = body.find(",", value_start)
            pos = len(body) if end < 0 else end
            value = body[value_start:pos]
        fields[name] = bib_unescape_generated(normalize_space(value))
        index = pos
    return fields


def collect_existing() -> tuple[dict[str, list[Record]], dict[str, str], dict[str, set[str]]]:
    by_dossier: dict[str, list[Record]] = {}
    preserved_keys: dict[str, str] = {}
    membership: dict[str, set[str]] = defaultdict(set)
    shelf_keys = {
        dossier: {
            key for (mapped_dossier, key) in extract_existing_shelves() if mapped_dossier == dossier
        }
        for dossier in DOSSIERS
    }
    for dossier, directory in DOSSIERS.items():
        bib_path = directory / BIB_NAMES[dossier]
        records = parse_bib_entries(bib_path)
        header = bib_path.read_text(encoding="utf-8", errors="replace")[:300] if bib_path.exists() else ""
        if "Exhaustive mapped bibliography" in header:
            records = [
                record
                for record in records
                if record.key in shelf_keys[dossier] or record.key in LEGACY_UNMAPPED_KEYS
            ]
        by_dossier[dossier] = records
        for record in records:
            if not record.norm_title:
                continue
            preserved_keys.setdefault(record.norm_title, record.key)
            membership[record.norm_title].add(dossier)
    return by_dossier, preserved_keys, membership


def stable_key(record: Record, preserved: dict[str, str], used: set[str]) -> str:
    if record.norm_title in preserved and preserved[record.norm_title] not in used:
        key = preserved[record.norm_title]
    else:
        first_author = record.author.split(" and ", 1)[0]
        surname = first_author.split(",")[0].split()[-1] if first_author else record.venue.split()[0]
        surname = ascii_token(surname) or "Anon"
        words = [
            ascii_token(word).title()
            for word in re.findall(r"[A-Za-z0-9]+", strip_tags(record.title))
            if word.casefold() not in {"a", "an", "the", "of", "for", "to", "with", "and", "in", "on"}
        ]
        key = f"{surname}{record.year}{''.join(words[:3]) or 'Paper'}"
    if key in used:
        key += hashlib.sha1((record.title + record.author).encode()).hexdigest()[:7]
    used.add(key)
    return key


def identity_tokens(record: Record) -> set[str]:
    tokens = {f"title:{record.norm_title}"}
    if record.doi:
        tokens.add("doi:" + record.doi.casefold().strip())
    if record.dblp_key:
        tokens.add("dblp:" + record.dblp_key.casefold())
    if record.arxiv:
        tokens.add("arxiv:" + record.arxiv.casefold())
    return {token for token in tokens if not token.endswith(":")}


def deduplicate(records: Iterable[Record]) -> tuple[list[Record], list[tuple[str, str, str]]]:
    kept: list[Record] = []
    identity_to_index: dict[str, int] = {}
    duplicates: list[tuple[str, str, str]] = []
    for record in records:
        matches = {
            identity_to_index[token]
            for token in identity_tokens(record)
            if token in identity_to_index
        }
        if not matches:
            index = len(kept)
            kept.append(record)
            for token in identity_tokens(record):
                identity_to_index[token] = index
            continue
        index = min(matches)
        existing = kept[index]
        duplicates.append((record.title, existing.title, "identity/title"))
        if existing.publication_status != "proceedings" and record.publication_status == "proceedings":
            record.key = existing.key
            kept[index] = record
            existing = record
        for token in identity_tokens(existing) | identity_tokens(record):
            identity_to_index[token] = index
    return kept, duplicates


def screening_decision(record: Record, existing_membership: dict[str, set[str]]) -> tuple[str, str]:
    title = strip_tags(record.title)
    if record.norm_title in existing_membership:
        return "include", "identity matches a manually mapped dossier record"
    if (
        FRONTIER_NON_DOSSIER_PRIMARY_RE.search(title)
        and (DIRECT_LLM_RE.search(title) or HIGH_RECALL_RE.search(title))
        and (SOFTWARE_RE.search(title) or SECURITY_RE.search(title) or AGENT_SYSTEM_RE.search(title))
    ):
        return (
            "candidate",
            "title also names a medical, biological, social, vision, robotics, or model-method primary object; abstract/manual adjudication must establish a dossier research object",
        )
    if DIRECT_LLM_RE.search(title) and (SOFTWARE_RE.search(title) or SECURITY_RE.search(title) or AGENT_SYSTEM_RE.search(title)):
        return "include", "direct LLM/model signal plus software/security/agent-system object in title"
    if HIGH_RECALL_RE.search(title) and (SOFTWARE_RE.search(title) or SECURITY_RE.search(title)):
        return "candidate", "high-recall title signal; abstract/manual adjudication still required"
    return "exclude", "title lacks a dossier-specific LLM/software/security conjunction"


def frontier_screening_decision(
    record: Record, formal_identity_tokens: set[str]
) -> tuple[str, str, str]:
    if identity_tokens(record) & formal_identity_tokens:
        return (
            "exclude",
            "a formal-ledger venue version supersedes this preprint identity/title",
            "formal-supersession",
        )
    if not record.author or re.search(r"\banonymous\b", record.author, re.I):
        return "exclude", "anonymous or missing-author record", "metadata-review"
    if re.search(r"\bwithdrawn\b", record.comment, re.I):
        return "exclude", "arXiv comment marks the record withdrawn", "metadata-review"
    if re.search(r"\brejected (?:from|by|at)\b", record.comment, re.I):
        return "exclude", "arXiv comment identifies a rejected-only record", "metadata-review"
    if record.raw_fields.get("journal_ref") or record.doi or FRONTIER_ACCEPTED_RE.search(record.comment):
        return (
            "exclude",
            "publication/acceptance metadata makes this supplementary or off-ledger rather than frontier",
            "publication-metadata-review",
        )
    title = strip_tags(record.title)
    abstract = strip_tags(record.abstract)
    lead = abstract[:500]
    title_llm = bool(DIRECT_LLM_RE.search(title) or HIGH_RECALL_RE.search(title))
    lead_llm = bool(DIRECT_LLM_RE.search(title + " " + lead) or HIGH_RECALL_RE.search(title + " " + lead))
    title_domain = bool(
        FRONTIER_PRIMARY_SOFTWARE_RE.search(title)
        or FRONTIER_PRIMARY_SECURITY_RE.search(title)
        or FRONTIER_PRIMARY_AGENT_ENGINEERING_RE.search(title)
    )
    lead_domain = bool(
        FRONTIER_PRIMARY_SOFTWARE_RE.search(title + " " + abstract[:800])
        or FRONTIER_PRIMARY_SECURITY_RE.search(title + " " + abstract[:800])
        or FRONTIER_PRIMARY_AGENT_ENGINEERING_RE.search(title + " " + abstract[:800])
    )
    if (
        FRONTIER_NON_DOSSIER_PRIMARY_RE.search(title)
        and (title_llm or title_domain)
    ):
        return (
            "candidate",
            "title establishes a medical, biological, vision, robotics, or other potentially non-dossier primary object; manual review must show that software/agent engineering or cyber security is primary",
            "needs-primary-object-review",
        )
    if title_domain and lead_llm:
        return (
            "include",
            "title names a dossier research object and the title/abstract lead establishes the LLM or agentic method",
            "title-and-abstract",
        )
    if title_llm and lead_domain:
        return (
            "candidate",
            "LLM is explicit in the title but the dossier object appears only in the abstract; manual primary-object review required",
            "needs-primary-object-review",
        )
    return (
        "exclude",
        "LLM/foundation-model mention is background or the primary research object falls outside the dossiers",
        "title-and-abstract",
    )


def assign_dossiers(record: Record, membership: dict[str, set[str]]) -> set[str]:
    if record.norm_title in membership:
        return set(membership[record.norm_title])
    title = strip_tags(record.title)
    if SECURITY_RE.search(title):
        return {"llm-security"}
    if AGENT_SYSTEM_RE.search(title):
        return {"software-for-llm"}
    return {"llm-software"}


def assign_frontier_dossiers(record: Record) -> set[str]:
    title = strip_tags(record.title)
    abstract_lead = strip_tags(record.abstract)[:800]
    assignments: set[str] = set()
    if SECURITY_RE.search(title) or (
        "cs.CR" in record.categories and SECURITY_RE.search(abstract_lead)
    ):
        assignments.add("llm-security")
    if FRONTIER_AGENT_RE.search(title) or AGENT_SYSTEM_RE.search(title):
        assignments.add("software-for-llm")
    if SOFTWARE_RE.search(title):
        assignments.add("llm-software")
    if not assignments:
        assignments.add("llm-security" if "cs.CR" in record.categories else "llm-software")
    return assignments


def choose_shelf(dossier: str, text: str) -> str:
    for pattern, shelf in SHELF_RULES[dossier]:
        if re.search(pattern, text, re.I):
            return shelf
    return DEFAULT_SHELF[dossier]


def concise_contribution(record: Record) -> str:
    title = strip_tags(record.title).rstrip(".")
    abstract = strip_tags(record.abstract)
    if abstract:
        sentences = re.split(r"(?<=[.!?])\s+", abstract)
        contribution_signal = re.compile(
            r"\b(we (?:introduce|propose|present|develop|build|design|evaluate|"
            r"investigate|study|conduct|construct|release)|this (?:paper|work) "
            r"(?:introduces|proposes|presents|develops|builds|designs|evaluates|"
            r"investigates|studies)|our (?:method|system|framework|benchmark|"
            r"dataset|study|analysis|approach))\b",
            re.I,
        )
        selected = next(
            (sentence for sentence in sentences if contribution_signal.search(sentence)),
            sentences[0] if sentences else "",
        )
        selected = re.sub(
            r"^(?:in this (?:paper|work),?\s+|here,?\s+)?we\s+",
            "",
            selected,
            flags=re.I,
        )
        if selected:
            selected = selected[0].upper() + selected[1:]
            words = selected.split()
            if len(words) > 24:
                selected = " ".join(words[:24]).rstrip(",:;") + "…"
            return selected.rstrip(".") + "."
    if re.search(r"\b(benchmark|dataset|evaluation|evaluating|empirical)\b", title, re.I):
        verb = "Benchmarks or evaluates"
    elif re.search(r"\b(survey|systematic|taxonomy|mapping study|review)\b", title, re.I):
        verb = "Systematizes"
    elif re.search(r"\b(test|debug|repair|detect|analysis|verification)\b", title, re.I):
        verb = "Studies"
    else:
        verb = "Introduces or evaluates"
    if len(title) > 180:
        title = title[:177].rstrip() + "…"
    return f"{verb} {title[0].lower() + title[1:] if title else 'the mapped research object'}; abstract-level contribution review remains pending."


def bib_entry(record: Record) -> str:
    fields: list[tuple[str, str]] = []
    fields.append(("author", record.author or f"{record.venue} {record.year} program record"))
    fields.append(("title", record.title))
    if record.entry_type == "article" or record.journal:
        fields.append(("journal", record.journal or record.venue))
    else:
        fields.append(("booktitle", record.booktitle or record.venue))
    fields.append(("year", str(record.year)))
    for name in ("volume", "number", "pages", "publisher"):
        value = getattr(record, name)
        if value:
            fields.append((name, value))
    if record.doi:
        fields.append(("doi", record.doi))
    if record.arxiv:
        fields.extend((("eprint", record.arxiv), ("archiveprefix", "arXiv")))
    if record.url:
        fields.append(("url", record.url))
    if record.dblp_key:
        fields.append(("dblp", record.dblp_key))
    fields.append(("keywords", ", ".join(sorted(record.keywords))))
    body = ",\n".join(f"  {name} = {{{bib_escape(value)}}}" for name, value in fields)
    return f"@{record.entry_type}{{{record.key},\n{body}\n}}\n"


def write_bib(path: Path, records: Iterable[Record], heading: str) -> None:
    ordered = sorted(records, key=lambda r: (r.year, r.venue, r.key.casefold()))
    text = (
        f"% {heading}\n"
        f"% Snapshot cutoff: {SNAPSHOT_DATE}. Generated by scripts/build_corpus.py.\n"
        "% Do not hand-edit generated entries; update sources or screening decisions.\n\n"
        + "\n".join(bib_entry(record) for record in ordered)
    )
    path.write_text(text, encoding="utf-8")


def record_from_existing(record: Record, dossier: str, formal_by_title: dict[str, Record]) -> Record:
    if record.norm_title in formal_by_title:
        formal = replace(
            formal_by_title[record.norm_title],
            keywords=set(formal_by_title[record.norm_title].keywords),
            raw_fields=dict(formal_by_title[record.norm_title].raw_fields),
        )
        formal.key = record.key
        formal.keywords.add("formal-venue")
        return formal
    record.venue = record.booktitle or record.journal or "Supplementary/out-of-ledger"
    record.area = "Supplementary"
    record.source_kind = "preserved dossier bibliography"
    if record.arxiv and record.year >= 2024:
        record.publication_status = "frontier-preprint"
        record.keywords = {"frontier-preprint"}
    else:
        record.publication_status = "supplementary"
        record.keywords = {"supplementary", "out-of-ledger"}
    if not record.url and record.doi:
        record.url = "https://doi.org/" + record.doi
    return record


def write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def read_adjudications(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    result: dict[str, dict[str, str]] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row_number, row in enumerate(csv.DictReader(handle), start=2):
            decision = row.get("decision", "").strip()
            if not decision:
                continue
            if decision not in {"include", "exclude"}:
                raise ValueError(f"{path}:{row_number}: decision must be include or exclude")
            reason = row.get("reason", "").strip()
            evidence_source = row.get("evidence_source", "").strip()
            reviewed_on = row.get("reviewed_on", "").strip()
            if not reason or not evidence_source or not reviewed_on:
                raise ValueError(
                    f"{path}:{row_number}: reason, evidence_source, and reviewed_on are required"
                )
            dossiers = {
                item.strip()
                for item in row.get("dossiers", "").split(";")
                if item.strip()
            }
            if not dossiers <= set(DOSSIERS):
                raise ValueError(f"{path}:{row_number}: unknown dossier assignment")
            if decision == "include" and not dossiers:
                raise ValueError(f"{path}:{row_number}: include decision requires a dossier")
            if decision == "exclude" and dossiers:
                raise ValueError(f"{path}:{row_number}: exclude decision cannot assign a dossier")
            identities = []
            if row.get("citation_key", "").strip():
                identities.append("key:" + row["citation_key"].strip())
            if row.get("arxiv_id", "").strip():
                identities.append("arxiv:" + row["arxiv_id"].strip().casefold())
            if row.get("title", "").strip():
                identities.append("title:" + normalize_title(row["title"]))
            if not identities:
                raise ValueError(f"{path}:{row_number}: no record identity supplied")
            normalized = dict(row)
            normalized["decision"] = decision
            normalized["reason"] = reason
            normalized["dossiers"] = ";".join(sorted(dossiers))
            for identity in identities:
                if identity in result:
                    raise ValueError(f"{path}:{row_number}: duplicate adjudication identity {identity}")
                result[identity] = normalized
    return result


def find_adjudication(
    record: Record, adjudications: dict[str, dict[str, str]]
) -> dict[str, str] | None:
    identities = [f"key:{record.key}", f"title:{record.norm_title}"]
    if record.arxiv:
        identities.insert(1, "arxiv:" + record.arxiv.casefold())
    matches = {id(adjudications[identity]): adjudications[identity] for identity in identities if identity in adjudications}
    if len(matches) > 1:
        raise ValueError(f"conflicting adjudications for {record.key}: {record.title}")
    return next(iter(matches.values()), None)


def write_manifest(rows: list[dict[str, object]]) -> None:
    fields = [
        "area",
        "venue",
        "year",
        "publication_status",
        "expected_count",
        "collected_count",
        "retrieval_date",
        "official_source_url",
        "metadata_source_urls",
        "reconciliation",
        "unresolved_metadata",
    ]
    write_csv(CORPUS_DIR / "venue-year-manifest.csv", fields, rows)
    (CORPUS_DIR / "venue-year-manifest.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def extract_existing_shelves() -> dict[tuple[str, str], tuple[str, str, str]]:
    result: dict[tuple[str, str], tuple[str, str, str]] = {}
    for dossier, directory in DOSSIERS.items():
        for path in (directory / "Academic-Status").rglob("*.md"):
            text = path.read_text(encoding="utf-8", errors="replace")
            if GENERATED_SHELF_BEGIN in text:
                before, remainder = text.split(GENERATED_SHELF_BEGIN, 1)
                if GENERATED_SHELF_END not in remainder:
                    raise ValueError(f"{path}: generated shelf block lacks an end marker")
                _, after = remainder.split(GENERATED_SHELF_END, 1)
                text = before + after
            for line in text.splitlines():
                if not line.startswith("|") or line.startswith("| ---"):
                    continue
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if len(cells) < 5 or not re.fullmatch(r"[A-Za-z0-9_.:-]+", cells[0]):
                    continue
                key = cells[0]
                contribution = cells[-2] if len(cells) >= 6 else ""
                label = cells[-1]
                result[(dossier, key)] = (
                    path.relative_to(directory).as_posix(),
                    strip_tags(contribution),
                    strip_tags(label),
                )
    return result


def write_canonical_maps(
    mappings: list[dict[str, str]], dossier_records: dict[str, list[Record]]
) -> None:
    by_dossier: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in mappings:
        by_dossier[row["dossier"]].append(row)
    records_by_key = {
        dossier: {record.key: record for record in records}
        for dossier, records in dossier_records.items()
    }
    for dossier, directory in DOSSIERS.items():
        lines = [
            "---",
            "ai-generated: true",
            f"last-reviewed: {SNAPSHOT_DATE}",
            "---",
            "",
            "# Canonical Corpus Map",
            "",
            "Back: [Dossier home](%s)"
            % (
                "LLM-Software-Research-Dossier-2026.md"
                if dossier == "llm-software"
                else "Software-For-LLM-Agent-Systems-Research-Dossier-2026.md"
                if dossier == "software-for-llm"
                else "LLM-Software-Security-Research-Dossier-2026.md"
            ),
            "",
            "This generated map is the auditable bridge between the shared 2024–2026 corpus, "
            "the dossier BibTeX, and the materialized academic shelves. A record has one "
            "canonical row per dossier; generated shelf blocks preserve hand-written prose, "
            "and secondary shelves should link by citation key.",
            "",
        ]
        grouped: dict[str, dict[str, list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
        for row in by_dossier[dossier]:
            grouped[row["shelf"]][row["evidence_layer"]].append(row)
        for shelf in sorted(grouped):
            shelf_name = Path(shelf).stem.replace("-", " ")
            encoded = quote(shelf, safe="/")
            lines.extend((f"## [{shelf_name}]({encoded})", ""))
            for layer in ("formal-venue", "frontier-preprint", "supplementary"):
                rows = grouped[shelf].get(layer, [])
                if not rows:
                    continue
                lines.extend(
                    (
                        f"### {layer.replace('-', ' ').title()}",
                        "",
                        "| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence |",
                        "| --- | --- | ---: | --- | --- | --- | --- |",
                    )
                )
                for row in sorted(rows, key=lambda item: (item["year"], item["citation_key"])):
                    record = records_by_key[dossier].get(row["citation_key"])
                    title = record.title if record else row["title"]
                    url = record.url if record else row["url"]
                    lines.append(
                        "| {key} | [{title}]({url}) | {year} | {source} | {role} | {contribution} | {evidence} |".format(
                            key=row["citation_key"],
                            title=title.replace("|", r"\|"),
                            url=url,
                            year=row["year"],
                            source=row["verified_source_status"].replace("|", r"\|"),
                            role=row["research_role"].replace("|", r"\|"),
                            contribution=row["contribution"].replace("|", r"\|"),
                            evidence=layer,
                        )
                    )
                lines.append("")
        (directory / "Canonical-Corpus-Map.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def render_academic_shelves(
    mappings: list[dict[str, str]], dossier_records: dict[str, list[Record]]
) -> None:
    """Materialize non-hand-written mappings without touching hand-written prose.

    Existing full rows remain authoritative. Every other mapping is rendered
    inside a stable generated block on its canonical shelf, separated by
    evidence layer. On the next build, extract_existing_shelves deliberately
    ignores these blocks so generated rows cannot masquerade as manual review.
    """

    manual_rows = extract_existing_shelves()
    manual_keys = {
        dossier: {
            key for mapped_dossier, key in manual_rows if mapped_dossier == dossier
        }
        for dossier in DOSSIERS
    }
    records_by_key = {
        dossier: {record.key: record for record in records}
        for dossier, records in dossier_records.items()
    }
    grouped: dict[tuple[str, str], dict[str, list[dict[str, str]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for row in mappings:
        if row["citation_key"] in manual_keys[row["dossier"]]:
            continue
        grouped[(row["dossier"], row["shelf"])][row["evidence_layer"]].append(row)

    for dossier, directory in DOSSIERS.items():
        shelf_root = directory / "Academic-Status"
        for path in sorted(shelf_root.rglob("*.md")):
            if path.name == "Academic-Status.md":
                continue
            relative = path.relative_to(directory).as_posix()
            text = path.read_text(encoding="utf-8", errors="replace")
            if GENERATED_SHELF_BEGIN in text:
                before, remainder = text.split(GENERATED_SHELF_BEGIN, 1)
                if GENERATED_SHELF_END not in remainder:
                    raise ValueError(f"{path}: generated shelf block lacks an end marker")
                _, after = remainder.split(GENERATED_SHELF_END, 1)
                text = before.rstrip("\n")
                if after.strip():
                    text += "\n\n" + after.strip("\n")
            else:
                text = text.rstrip("\n")

            layers = grouped.get((dossier, relative), {})
            generated_lines = [
                GENERATED_SHELF_BEGIN,
                "## Generated Canonical Corpus Rows",
                "",
                "The builder maintains this block from the shared screening and mapping ledgers. "
                "Hand-written rows and analysis above remain authoritative where present.",
                "",
            ]
            rendered = 0
            for layer, heading in (
                ("formal-venue", "Formal Venue Papers"),
                ("frontier-preprint", "Frontier Preprints"),
                ("supplementary", "Supplementary or Out-of-Ledger Evidence"),
            ):
                rows = layers.get(layer, [])
                if not rows:
                    continue
                generated_lines.extend(
                    (
                        f"### {heading}",
                        "",
                        "| Key | Paper | Year | Verified source/status | Research role | Contribution | Evidence label |",
                        "| --- | --- | ---: | --- | --- | --- | --- |",
                    )
                )
                for row in sorted(rows, key=lambda item: (item["year"], item["citation_key"])):
                    record = records_by_key[dossier].get(row["citation_key"])
                    title = (record.title if record else row["title"]).replace("|", r"\|")
                    url = record.url if record else row["url"]
                    paper = f"[{title}](<{url}>)" if url else title
                    generated_lines.append(
                        "| {key} | {paper} | {year} | {source} | {role} | {contribution} | {evidence} |".format(
                            key=row["citation_key"],
                            paper=paper,
                            year=row["year"],
                            source=row["verified_source_status"].replace("|", r"\|"),
                            role=row["research_role"].replace("|", r"\|"),
                            contribution=row["contribution"].replace("|", r"\|"),
                            evidence=layer,
                        )
                    )
                    rendered += 1
                generated_lines.append("")
            if rendered:
                generated_lines.append(GENERATED_SHELF_END)
                text += "\n\n" + "\n".join(generated_lines).rstrip()
            path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_taxonomy_audit(mappings: list[dict[str, str]]) -> None:
    counts = Counter((row["dossier"], row["shelf"]) for row in mappings)
    rows: list[dict[str, object]] = []
    for dossier, directory in DOSSIERS.items():
        for shelf_path in sorted((directory / "Academic-Status").rglob("*.md")):
            if shelf_path.name == "Academic-Status.md":
                continue
            rel = shelf_path.relative_to(directory).as_posix()
            text = shelf_path.read_text(encoding="utf-8", errors="replace")
            scope_match = re.search(r"^Scope:\s*(.+)$", text, re.M)
            scope = normalize_space(scope_match.group(1)) if scope_match else "Scope statement requires maintenance."
            rows.append(
                {
                    "dossier": dossier,
                    "shelf": rel,
                    "primary_research_question": scope,
                    "inclusion_boundary": scope,
                    "exclusion_boundary": "Use the sibling dossier when the primary research object crosses the documented direction/security boundary.",
                    "mapped_literature_count": counts[(dossier, rel)],
                    "audit_status": "active" if counts[(dossier, rel)] else "coverage-gap",
                    "replacement_link": "",
                }
            )
    write_csv(
        CORPUS_DIR / "taxonomy-audit.csv",
        [
            "dossier",
            "shelf",
            "primary_research_question",
            "inclusion_boundary",
            "exclusion_boundary",
            "mapped_literature_count",
            "audit_status",
            "replacement_link",
        ],
        rows,
    )


def write_counts(manifest: list[dict[str, object]]) -> None:
    lines = [
        "# Formal Venue Coverage Counts",
        "",
        f"Snapshot cutoff: **{SNAPSHOT_DATE}**.",
        "",
        "Counts are archival records after track/front-matter filtering and title/identity "
        "deduplication. `pending` means that a complete public archival program was not "
        "available by the cutoff; it never means zero accepted papers.",
        "",
        "| Area | Venue | Year | Status | Expected | Collected | Reconciliation / unresolved metadata |",
        "| --- | --- | ---: | --- | ---: | ---: | --- |",
    ]
    for row in manifest:
        lines.append(
            "| {area} | {venue} | {year} | {status} | {expected} | {collected} | {note} |".format(
                area=row["area"],
                venue=row["venue"],
                year=row["year"],
                status=row["publication_status"],
                expected=row["expected_count"] if row["expected_count"] != "" else "—",
                collected=row["collected_count"],
                note=(str(row["reconciliation"]) + "; " + str(row["unresolved_metadata"])).strip("; ").replace("|", r"\|"),
            )
        )
    (CORPUS_DIR / "coverage-counts.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="refresh all remote source snapshots")
    args = parser.parse_args()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    formal_adjudications = read_adjudications(FORMAL_ADJUDICATIONS)
    frontier_adjudications = read_adjudications(FRONTIER_ADJUDICATIONS)
    existing_by_dossier, preserved_keys, existing_membership = collect_existing()
    specs = build_venue_years()
    all_records: list[Record] = []
    manifest_rows: list[dict[str, object]] = []

    for spec in specs:
        venue_records: list[Record] = []
        errors: list[str] = []
        for source in spec.sources:
            records, error = parse_source(source, spec, args.refresh)
            venue_records.extend(records)
            if error:
                errors.append(error)
        venue_records, _ = deduplicate(venue_records)
        collected = len(venue_records)
        expected = spec.expected_count if spec.expected_count is not None else (collected or None)
        if collected:
            if expected is not None and expected != collected:
                status = "count-discrepancy"
                reconciliation = f"expected {expected} from official count; normalized source yielded {collected}"
            else:
                status = (
                    "accepted-program"
                    if any(record.publication_status == "accepted-program" for record in venue_records)
                    else "proceedings"
                )
                reconciliation = "normalized metadata count reconciled; independent official count unavailable" if spec.expected_count is None else "official and normalized counts agree"
        else:
            status = spec.status_if_missing
            reconciliation = "no complete public archival program available by cutoff"
        unresolved = "; ".join(filter(None, [spec.note, *errors]))
        if spec.venue == "ICML" and spec.year == 2026 and collected:
            pending_authors = sum("authors pending normalization" in r.author for r in venue_records)
            unresolved = "; ".join(filter(None, [unresolved, f"{pending_authors} program records retain author-normalization sentinel"]))
        manifest_rows.append(
            {
                "area": AREA_BY_VENUE[spec.venue],
                "venue": spec.venue,
                "year": spec.year,
                "publication_status": status,
                "expected_count": expected if expected is not None else "",
                "collected_count": collected,
                "retrieval_date": SNAPSHOT_DATE,
                "official_source_url": spec.official_url,
                "metadata_source_urls": " | ".join(source.url for source in spec.sources),
                "reconciliation": reconciliation,
                "unresolved_metadata": unresolved,
            }
        )
        all_records.extend(venue_records)
        print(f"{spec.venue} {spec.year}: {status} ({collected})", file=sys.stderr)

    formal_records, duplicate_rows = deduplicate(all_records)
    used_keys: set[str] = set()
    for record in formal_records:
        record.key = stable_key(record, preserved_keys, used_keys)

    formal_by_title = {record.norm_title: record for record in formal_records}
    formal_identity_tokens = set().union(
        *(identity_tokens(record) for record in formal_records)
    )
    frontier_candidates, frontier_query_manifest = collect_arxiv_frontier_2026(args.refresh)
    frontier_used_keys = set(used_keys)
    for record in frontier_candidates:
        record.key = stable_key(record, preserved_keys, frontier_used_keys)
    frontier_screening_rows: list[dict[str, object]] = []
    screened_frontier_2026: list[Record] = []
    dossier_frontier: dict[str, list[Record]] = defaultdict(list)
    for record in frontier_candidates:
        decision, reason, evidence = frontier_screening_decision(
            record, formal_identity_tokens
        )
        adjudication = find_adjudication(record, frontier_adjudications)
        if adjudication:
            decision = adjudication["decision"]
            reason = adjudication["reason"]
            evidence = "manual-abstract-or-paper-review"
            assignments = {
                item for item in adjudication["dossiers"].split(";") if item
            }
            review_status = "human-adjudicated"
        else:
            assignments = assign_frontier_dossiers(record) if decision == "include" else set()
            review_status = (
                "needs-primary-object-review"
                if decision == "candidate"
                else "automated-title-abstract-screening"
            )
        frontier_screening_rows.append(
            {
                "citation_key": record.key,
                "arxiv_id": record.arxiv,
                "title": record.title,
                "year": record.year,
                "categories": ";".join(record.categories),
                "published": record.raw_fields.get("published", ""),
                "decision": decision,
                "reason": reason,
                "pass2_evidence": evidence,
                "dossiers": ";".join(sorted(assignments)),
                "formal_supersession": "yes" if evidence == "formal-supersession" else "no",
                "review_status": review_status,
                "url": record.url,
            }
        )
        if decision != "include":
            continue
        record.publication_status = "frontier-preprint"
        record.keywords = {"frontier-preprint", "arxiv-2026"}
        screened_frontier_2026.append(record)
        for dossier in assignments:
            dossier_frontier[dossier].append(record)

    screening_rows: list[dict[str, object]] = []
    screened_formal: list[Record] = []
    dossier_formal: dict[str, list[Record]] = defaultdict(list)
    mapping_rows: list[dict[str, str]] = []
    existing_shelves = extract_existing_shelves()

    for record in formal_records:
        decision, reason = screening_decision(record, existing_membership)
        adjudication = find_adjudication(record, formal_adjudications)
        if adjudication:
            decision = adjudication["decision"]
            reason = adjudication["reason"]
            assignments = {
                item for item in adjudication["dossiers"].split(";") if item
            }
            pass2_evidence = "manual-abstract-or-paper-review"
            review_status = "human-adjudicated"
        else:
            assignments = assign_dossiers(record, existing_membership) if decision == "include" else set()
            manually_mapped = record.norm_title in existing_membership
            pass2_evidence = (
                "manual-existing-map"
                if manually_mapped
                else "automated-title-rule"
                if decision == "include"
                else "not-inspected"
            )
            review_status = (
                "human-adjudicated"
                if manually_mapped
                else "needs-abstract-review"
                if decision == "candidate"
                else "automated-title-screening"
            )
        screening_rows.append(
            {
                "citation_key": record.key,
                "title": record.title,
                "venue": record.venue,
                "year": record.year,
                "pass1_title_signal": "yes" if HIGH_RECALL_RE.search(record.title) else "no",
                "pass2_evidence": pass2_evidence,
                "decision": decision,
                "reason": reason,
                "dossiers": ";".join(sorted(assignments)),
                "review_status": review_status,
            }
        )
        if decision != "include":
            continue
        screened_formal.append(record)
        for dossier in assignments:
            dossier_formal[dossier].append(record)

    dossier_records: dict[str, list[Record]] = {}
    frontier_by_title: dict[str, Record] = {}
    for dossier, existing_records in existing_by_dossier.items():
        merged: list[Record] = []
        seen_titles: set[str] = set()
        for current in existing_records:
            normalized = record_from_existing(current, dossier, formal_by_title)
            if normalized.norm_title in seen_titles:
                continue
            seen_titles.add(normalized.norm_title)
            merged.append(normalized)
            if normalized.publication_status == "frontier-preprint":
                frontier_by_title.setdefault(normalized.norm_title, normalized)
        for formal in dossier_formal[dossier]:
            if formal.norm_title in seen_titles:
                continue
            seen_titles.add(formal.norm_title)
            merged.append(formal)
        for frontier in dossier_frontier[dossier]:
            if frontier.norm_title in seen_titles:
                continue
            seen_titles.add(frontier.norm_title)
            merged.append(frontier)
        dossier_records[dossier], _ = deduplicate(merged)
    for frontier in screened_frontier_2026:
        frontier_by_title.setdefault(frontier.norm_title, frontier)
    unique_frontier, _ = deduplicate(frontier_by_title.values())
    frontier_by_title = {record.norm_title: record for record in unique_frontier}

    # Re-key dossier records consistently and build one canonical mapping per dossier.
    formal_key_by_title = {record.norm_title: record.key for record in formal_records}
    for dossier, records in dossier_records.items():
        dossier_used: set[str] = set()
        for record in records:
            if record.norm_title in formal_key_by_title and record.key not in preserved_keys.values():
                record.key = formal_key_by_title[record.norm_title]
            if not record.key:
                record.key = stable_key(record, preserved_keys, dossier_used)
            elif record.key in dossier_used:
                record.key += hashlib.sha1(record.title.encode()).hexdigest()[:7]
            dossier_used.add(record.key)
            evidence = (
                "formal-venue"
                if record.publication_status in {"proceedings", "accepted-program"}
                else "frontier-preprint"
                if record.publication_status == "frontier-preprint"
                else "supplementary"
            )
            record.keywords.discard("formal-venue")
            record.keywords.add(evidence)
            existing_map = existing_shelves.get((dossier, record.key))
            mapping_adjudication = find_adjudication(record, formal_adjudications)
            if mapping_adjudication is None:
                mapping_adjudication = find_adjudication(record, frontier_adjudications)
            adjudicated_shelf = (
                mapping_adjudication.get("shelf", "").strip()
                if mapping_adjudication
                else ""
            )
            shelf = (
                existing_map[0]
                if existing_map
                else adjudicated_shelf
                if adjudicated_shelf
                else choose_shelf(dossier, record.title + " " + record.abstract[:1200])
            )
            if not (DOSSIERS[dossier] / shelf).is_file():
                raise ValueError(
                    f"canonical shelf does not exist for {dossier}/{record.key}: {shelf}"
                )
            adjudicated_contribution = (
                mapping_adjudication.get("contribution", "").strip()
                if mapping_adjudication
                else ""
            )
            contribution = (
                existing_map[1]
                if existing_map and existing_map[1]
                else adjudicated_contribution
                if adjudicated_contribution
                else concise_contribution(record)
            )
            label = existing_map[2] if existing_map and existing_map[2] else (
                "Published" if record.publication_status == "proceedings" else
                "Accepted/program record" if record.publication_status == "accepted-program" else
                "Frontier" if evidence == "frontier-preprint" else "Supplementary"
            )
            mapping_rows.append(
                {
                    "dossier": dossier,
                    "citation_key": record.key,
                    "title": record.title,
                    "year": str(record.year),
                    "url": record.url,
                    "verified_source_status": f"{record.venue} / {record.publication_status}",
                    "research_role": Path(shelf).stem.replace("-", " "),
                    "contribution": contribution,
                    "evidence_layer": evidence,
                    "canonical": "yes",
                    "shelf": shelf,
                    "label": label,
                }
            )

    write_bib(
        CORPUS_DIR / "exhaustive-formal-venues.bib",
        formal_records,
        "Exhaustive in-scope formal-venue corpus",
    )
    write_bib(
        CORPUS_DIR / "screened-formal-venues.bib",
        screened_formal,
        "Screened formal-venue papers relevant to at least one dossier",
    )
    write_bib(
        CORPUS_DIR / "screened-frontier-preprints.bib",
        frontier_by_title.values(),
        "Screened public frontier preprints relevant to at least one dossier",
    )
    write_bib(
        CORPUS_DIR / "exhaustive-frontier-preprints-2026.bib",
        frontier_candidates,
        "Exhaustive arXiv 2026 candidate universe for the declared frontier query",
    )
    for dossier, records in dossier_records.items():
        write_bib(
            DOSSIERS[dossier] / BIB_NAMES[dossier],
            records,
            f"Exhaustive mapped bibliography for {dossier}",
        )

    write_manifest(manifest_rows)
    write_counts(manifest_rows)
    write_csv(
        CORPUS_DIR / "screening.csv",
        [
            "citation_key",
            "title",
            "venue",
            "year",
            "pass1_title_signal",
            "pass2_evidence",
            "decision",
            "reason",
            "dossiers",
            "review_status",
        ],
        screening_rows,
    )
    write_csv(
        CORPUS_DIR / "dossier-mapping.csv",
        [
            "dossier",
            "citation_key",
            "title",
            "year",
            "url",
            "verified_source_status",
            "research_role",
            "contribution",
            "evidence_layer",
            "canonical",
            "shelf",
            "label",
        ],
        mapping_rows,
    )
    write_csv(
        CORPUS_DIR / "frontier-screening-2026.csv",
        [
            "citation_key",
            "arxiv_id",
            "title",
            "year",
            "categories",
            "published",
            "decision",
            "reason",
            "pass2_evidence",
            "dossiers",
            "formal_supersession",
            "review_status",
            "url",
        ],
        frontier_screening_rows,
    )
    frontier_query_manifest.update(
        {
            "screening_policy": {
                "automatic_include_boundary": (
                    "title must name a primary ordinary-software/code, software/cyber-"
                    "security, or LLM/agent-system engineering object; generic agent, "
                    "API, testing, or security mentions are insufficient"
                ),
                "non_dossier_domain_policy": (
                    "medical, biological, vision, robotics, and other domain-first "
                    "titles remain candidates unless manually adjudicated"
                ),
                "manual_override_file": FRONTIER_ADJUDICATIONS.name,
            },
            "normalized_candidates": len(frontier_candidates),
            "screened_include": len(screened_frontier_2026),
            "screened_candidate": sum(
                row["decision"] == "candidate" for row in frontier_screening_rows
            ),
            "screened_exclude": sum(
                row["decision"] == "exclude" for row in frontier_screening_rows
            ),
            "formal_supersessions": sum(
                row["formal_supersession"] == "yes" for row in frontier_screening_rows
            ),
            "decision_counts": dict(
                Counter(row["decision"] for row in frontier_screening_rows)
            ),
            "human_adjudications": sum(
                row["review_status"] == "human-adjudicated"
                for row in frontier_screening_rows
            ),
        }
    )
    (CORPUS_DIR / "frontier-query-manifest-2026.json").write_text(
        json.dumps(frontier_query_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_csv(
        CORPUS_DIR / "deduplication-log.csv",
        ["discarded_title", "kept_title", "reason"],
        (
            {"discarded_title": discarded, "kept_title": kept, "reason": reason}
            for discarded, kept, reason in duplicate_rows
        ),
    )
    write_taxonomy_audit(mapping_rows)
    write_canonical_maps(mapping_rows, dossier_records)
    render_academic_shelves(mapping_rows, dossier_records)
    summary = {
        "snapshot_date": SNAPSHOT_DATE,
        "formal_records": len(formal_records),
        "screened_formal_records": len(screened_formal),
        "frontier_preprints": len(frontier_by_title),
        "frontier_2026_query_candidates": len(frontier_candidates),
        "frontier_2026_screened": len(screened_frontier_2026),
        "frontier_2026_candidates_needing_review": frontier_query_manifest[
            "screened_candidate"
        ],
        "frontier_2026_formal_supersessions": frontier_query_manifest[
            "formal_supersessions"
        ],
        "dossier_records": {dossier: len(records) for dossier, records in dossier_records.items()},
        "screening": dict(Counter(row["decision"] for row in screening_rows)),
        "pending_venue_years": [
            f"{row['venue']} {row['year']}"
            for row in manifest_rows
            if row["publication_status"] == "pending"
        ],
    }
    (CORPUS_DIR / "build-summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
