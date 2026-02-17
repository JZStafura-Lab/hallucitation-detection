"""
Creates empty CSV templates for the four main data files.

Called automatically by setup.py; can also be run standalone.
"""

import pandas as pd
from pathlib import Path
from config import OUTPUT_DIR


# ---------------------------------------------------------------------------
# Schema definitions
# ---------------------------------------------------------------------------

PAPER_METADATA_COLS = [
    "Paper_ID",           # P0001, P0002, …
    "Domain_Category",    # broad field bucket
    "Venue",              # publication venue
    "Publication_Year",
    "Title",
    "Authors",
    "Processing_Status",  # pending | processed | error
]

AUTHOR_EXPERTISE_COLS = [
    "Paper_ID",
    "Key_Author_1",
    "Key_Author_1_Domain",
    "Key_Author_1_Top_Papers",
    "Key_Author_2",
    "Key_Author_2_Domain",
    "Key_Author_2_Top_Papers",
    "Paper_Domain",
    "Expertise_Match",        # 0=Core, 1=Adjacent, 2=Distant
    "Notes",
    "Coding_Time_Minutes",
    "Coder_ID",
]

CITATIONS_EXTRACTED_COLS = [
    "Citation_ID",            # P0001_C001, …
    "Paper_ID",
    "Citation_Text",
    "Citation_Year",
    "Authors_Cited",
    "Title_Cited",
    "Is_Hallucinated",        # 0=Real, 1=Hallucinated, -1=Uncertain
    "Verification_Method",    # CrossRef | GoogleScholar | Manual
    "CrossRef_Score",
    "GPTZero_Score",
    "Section_Location_Auto",
    "Context_Sentence",
]

HALLUCINATION_CODING_COLS = [
    "Citation_ID",
    "Paper_ID",
    "Citation_Domain",
    "Citation_Role",          # B | M | R | E | T
    "Distance_from_Paper",    # 0=Core, 1=Peripheral
    "Recency_Category",       # 0–4
    "Temporal_Distance",      # years between paper and citation
    "Notes",
    "Coding_Time_Minutes",
    "Coder_ID",
]

SAMPLE_TRACKING_COLS = [
    "Paper_ID",
    "Venue",
    "Domain_Category",
    "Title",
    "Authors",
    "ArXiv_ID",
    "DOI",
    "PDF_URL",
    "Download_Status",        # pending | downloaded | failed | manual_required
    "Local_PDF_Path",
    "Sampling_Stratum",
    "Sampling_Seed",
    "Notes",
]


# ---------------------------------------------------------------------------
# Creation helpers
# ---------------------------------------------------------------------------

def _write_template(cols: list[str], filename: str) -> None:
    path = OUTPUT_DIR / filename
    if path.exists():
        print(f"  ~ {filename} already exists, skipping")
        return
    pd.DataFrame(columns=cols).to_csv(path, index=False)
    print(f"  ✓ {filename}")


def create_all_templates() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    _write_template(PAPER_METADATA_COLS,      "paper_metadata.csv")
    _write_template(AUTHOR_EXPERTISE_COLS,    "author_expertise_coding.csv")
    _write_template(CITATIONS_EXTRACTED_COLS, "citations_extracted.csv")
    _write_template(HALLUCINATION_CODING_COLS,"hallucination_coding.csv")
    _write_template(SAMPLE_TRACKING_COLS,     "sample_tracking.csv")


if __name__ == "__main__":
    create_all_templates()
