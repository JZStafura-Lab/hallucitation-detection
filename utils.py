"""
Shared utility functions used across phases.

Covers: CrossRef lookups, GPTZero calls, PDF text extraction,
citation string parsing, and logging setup.
"""

import logging
import re
import time
from pathlib import Path
from typing import Optional

import requests

from config import (
    CROSSREF_EMAIL,
    GPTZERO_API_KEY,
    GPTZERO_SCAN_ENDPOINT,
    MAX_RETRIES,
    RETRY_DELAY,
    API_TIMEOUT,
    LOGS_DIR,
)

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

def get_logger(name: str) -> logging.Logger:
    """Return a logger that writes to both console and a file in logs/."""
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(name)
    if not logger.handlers:
        fmt = logging.Formatter("%(asctime)s  %(levelname)-8s  %(name)s  %(message)s")
        # File handler
        fh = logging.FileHandler(LOGS_DIR / f"{name}.log")
        fh.setFormatter(fmt)
        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(fmt)
        logger.addHandler(fh)
        logger.addHandler(ch)
        logger.setLevel(logging.INFO)
    return logger


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def _get_with_retry(url: str, params: dict | None = None, headers: dict | None = None) -> Optional[dict]:
    """GET request with exponential-backoff retry. Returns JSON or None."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.get(url, params=params, headers=headers, timeout=API_TIMEOUT)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as exc:
            if attempt == MAX_RETRIES:
                return None
            time.sleep(RETRY_DELAY * attempt)
    return None


# ---------------------------------------------------------------------------
# CrossRef
# ---------------------------------------------------------------------------

def crossref_lookup(title: str, year: Optional[int] = None) -> Optional[dict]:
    """
    Search CrossRef for a citation by title (and optionally year).
    Returns the top result dict, or None if not found.
    """
    params: dict = {
        "query.title": title,
        "rows": 1,
        "mailto": CROSSREF_EMAIL,
    }
    if year:
        params["filter"] = f"from-pub-date:{year},until-pub-date:{year}"

    data = _get_with_retry("https://api.crossref.org/works", params=params)
    if not data:
        return None
    items = data.get("message", {}).get("items", [])
    return items[0] if items else None


def crossref_score(result: dict) -> float:
    """Extract the relevance score from a CrossRef result item."""
    return float(result.get("score", 0.0))


# ---------------------------------------------------------------------------
# GPTZero
# ---------------------------------------------------------------------------

def gptzero_scan_text(text: str) -> Optional[float]:
    """
    Submit text to GPTZero and return the AI probability score (0–1).
    Returns None on API error.
    """
    if not GPTZERO_API_KEY:
        raise EnvironmentError("GPTZERO_API_KEY is not set.")

    headers = {
        "Authorization": f"Bearer {GPTZERO_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"document": text}

    try:
        resp = requests.post(
            GPTZERO_SCAN_ENDPOINT,
            json=payload,
            headers=headers,
            timeout=API_TIMEOUT,
        )
        resp.raise_for_status()
        data = resp.json()
        return data.get("documents", [{}])[0].get("average_generated_prob")
    except requests.RequestException:
        return None


# ---------------------------------------------------------------------------
# PDF text extraction
# ---------------------------------------------------------------------------

def extract_text_from_pdf(pdf_path: Path) -> str:
    """
    Return the full plain-text content of a PDF.
    Falls back to an empty string on extraction failure.
    """
    try:
        import PyPDF2
        with open(pdf_path, "rb") as fh:
            reader = PyPDF2.PdfReader(fh)
            pages = [page.extract_text() or "" for page in reader.pages]
        return "\n".join(pages)
    except Exception:
        return ""


# ---------------------------------------------------------------------------
# Citation string parsing
# ---------------------------------------------------------------------------

# Matches APA-style "Author, A. B. (YYYY)" or similar year patterns
_YEAR_RE = re.compile(r"\b(1[89]\d{2}|20[012]\d)\b")

def extract_year_from_citation(citation_text: str) -> Optional[int]:
    """Return the most plausible publication year from a raw citation string."""
    matches = _YEAR_RE.findall(citation_text)
    return int(matches[0]) if matches else None


def split_reference_list(raw_text: str) -> list[str]:
    """
    Naively split a reference-section block into individual citation strings.
    Assumes one reference per line or blank-line separated blocks.
    Override / extend for venue-specific formats.
    """
    # Split on blank lines first; fall back to line-by-line
    blocks = re.split(r"\n{2,}", raw_text.strip())
    if len(blocks) > 3:
        return [b.strip() for b in blocks if b.strip()]
    return [line.strip() for line in raw_text.splitlines() if line.strip()]
