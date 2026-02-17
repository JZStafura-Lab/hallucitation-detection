"""
Configuration and constants for the hallucination detection pipeline.

Copy this file to config_local.py and add credentials there,
or set the corresponding environment variables.
config_local.py is excluded from version control.
"""

import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
PDF_DIR = DATA_DIR / "pdfs"
OUTPUT_DIR = DATA_DIR / "output"
FIGURES_DIR = OUTPUT_DIR / "figures"
LOGS_DIR = PROJECT_ROOT / "logs"

# ---------------------------------------------------------------------------
# API credentials  (override via environment variables or config_local.py)
# ---------------------------------------------------------------------------
GPTZERO_API_KEY: str = os.getenv("GPTZERO_API_KEY", "")
CROSSREF_EMAIL: str = os.getenv("CROSSREF_EMAIL", "your.email@example.com")

# Endpoints
GPTZERO_ENDPOINT = "https://api.gptzero.me/v2/predict/files"
GPTZERO_SCAN_ENDPOINT = "https://api.gptzero.me/v2/predict/text"

# ---------------------------------------------------------------------------
# Network / retry settings
# ---------------------------------------------------------------------------
MAX_RETRIES: int = 3
RETRY_DELAY: float = 5.0   # seconds between retries
API_TIMEOUT: int = 60       # seconds before request timeout
DOWNLOAD_DELAY: float = 1.0 # seconds between PDF download requests

# ---------------------------------------------------------------------------
# Detection thresholds
# ---------------------------------------------------------------------------
HALLUCINATION_THRESHOLD: float = 0.7  # minimum probability to flag a citation

# ---------------------------------------------------------------------------
# Domain taxonomy
# ---------------------------------------------------------------------------
DOMAINS: list[str] = [
    "NLP/Language Models",
    "Computer Vision",
    "Robotics/Embodied AI",
    "ML Theory/Optimization",
    "Reinforcement Learning",
    "Graphs/Networks",
    "Biomedical/Computational Biology",
    "Economics/Finance",
    "Political Science",
    "Sociology",
    "Psychology/Cognitive Science",
    "Other",
]

# Venue → broad domain bucket (add venues as the study grows)
VENUE_DOMAIN_MAP: dict[str, str] = {
    # entries populated during setup — see docs/VENUES.md
}

# ---------------------------------------------------------------------------
# Coding scheme
# ---------------------------------------------------------------------------
CITATION_ROLES: dict[str, str] = {
    "B": "Background",
    "M": "Methods",
    "R": "Related Work",
    "E": "Empirical",
    "T": "Theoretical",
}

EXPERTISE_LEVELS: dict[int, str] = {
    0: "Core",
    1: "Adjacent",
    2: "Distant",
}

RECENCY_CATEGORIES: dict[int, str] = {
    0: "Very Recent (0–1 yr)",
    1: "Recent (2–5 yr)",
    2: "Moderate (6–10 yr)",
    3: "Old (11+ yr)",
    4: "Future (impossible date)",
}

# ---------------------------------------------------------------------------
# Section detection patterns (regex applied to extracted plain-text)
# ---------------------------------------------------------------------------
SECTION_PATTERNS: dict[str, str] = {
    "introduction":   r"(?i)(?:^|\n)\s*(?:\d+\.?\s*)?introduction",
    "related_work":   r"(?i)(?:^|\n)\s*(?:\d+\.?\s*)?(?:related work|literature review|background)",
    "methods":        r"(?i)(?:^|\n)\s*(?:\d+\.?\s*)?(?:methods?|methodology|approach|model|algorithm)",
    "results":        r"(?i)(?:^|\n)\s*(?:\d+\.?\s*)?(?:results?|experiments?|evaluation)",
    "discussion":     r"(?i)(?:^|\n)\s*(?:\d+\.?\s*)?(?:discussion|conclusion|future work)",
}
