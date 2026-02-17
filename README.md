# Hallucitation Detection

A Python pipeline for detecting and analyzing patterns of AI-hallucinated citations in published academic papers.

**Project site**: https://jzstafura-lab.github.io/hallucitation-detection/

## Research Questions

**RQ1 — Expertise**: Are hallucinated citations more likely when an author cites outside their primary domain of expertise?

**RQ2 — Domain Velocity**: Do fields with faster publication cycles produce higher hallucination rates than slower-moving fields?

**RQ3 — Location**: Do hallucinated citations cluster in particular sections of a paper (e.g., Related Work vs. Methods)?

## Pipeline Overview

The workflow is divided into four sequential phases:

| Phase | Description | Mode |
|-------|-------------|------|
| 0 — Collection | Stratified sampling and PDF acquisition across target venues | Semi-automated |
| 1 — Extraction | Citation extraction from PDFs; CrossRef verification; GPTZero scoring | Automated |
| 2 — Coding | Manual coding of author expertise and citation characteristics | Manual |
| 3 — Analysis | Hypothesis testing and visualisation | Automated |

## Repository Structure

```
hallucitation-detection/
│
├── config.py                    # Paths, API settings, coding scheme constants
├── data_templates.py            # Generates empty CSV templates
├── setup.py                     # One-time project initialisation
├── utils.py                     # Shared utilities (API calls, PDF extraction, parsing)
├── requirements.txt
│
├── phase_0_collection/
│   ├── paper_collection_helper.py   # Venue paper-list templates and API helpers
│   ├── sampling_tracker.py          # Stratified random sampling (seeded)
│   ├── batch_download.py            # Automated PDF downloading
│   └── QUICKSTART_COLLECTION.py     # End-to-end interactive walkthrough
│
├── phase_1_automated/
│   └── phase1_automated_processing.py  # Citation extraction + hallucination detection
│
├── phase_2_coding/
│   └── phase2_manual_coding.py      # Interactive coding interface + progress tracker
│
├── phase_3_analysis/
│   └── phase3_analysis.py           # Statistical tests and figure generation
│
├── data/
│   ├── pdfs/                        # Downloaded PDFs — not versioned (see .gitignore)
│   └── output/                      # Generated CSVs and figures — not versioned
│
├── docs/
│   ├── CODING_GUIDE.md              # Manual coding procedures and decision rules
│   └── DATA_DICTIONARY.md           # Schema for all output CSV files
│
├── tests/
│   ├── test_utils.py
│   └── test_phase1.py
│
└── logs/                            # Processing logs — not versioned
```

## Getting Started

### 1. Clone and install dependencies

```bash
git clone https://github.com/JZStafura-Lab/hallucitation-detection.git
cd hallucitation-detection
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure API credentials

Create a `config_local.py` file (excluded from version control):

```python
# config_local.py
GPTZERO_API_KEY  = "your_key_here"
CROSSREF_EMAIL   = "you@example.com"
```

Or export as environment variables:

```bash
export GPTZERO_API_KEY="your_key_here"
export CROSSREF_EMAIL="you@example.com"
```

### 3. Initialise the project

```bash
python setup.py
```

This creates the `data/` directory structure and empty CSV templates.

---

## Phase 0 — Paper Collection

Target: a stratified random sample of ~300–400 papers drawn across venues representing fields with different publication velocities.

```bash
# Full interactive walkthrough
python phase_0_collection/QUICKSTART_COLLECTION.py

# Or step-by-step
python phase_0_collection/paper_collection_helper.py   # build venue templates
python phase_0_collection/sampling_tracker.py          # draw random sample
python phase_0_collection/batch_download.py            # download PDFs
```

**Outputs**:
- `data/output/sample_tracking.csv` — master sample with download status
- `data/pdfs/<venue>/` — downloaded PDFs organised by venue

---

## Phase 1 — Automated Processing

For each sampled PDF: extract citations, verify against CrossRef, score with GPTZero, and pre-populate the manual coding template.

```python
from phase_1_automated.phase1_automated_processing import process_batch
from pathlib import Path

process_batch(
    pdf_directory=Path("data/pdfs/venue_name"),
    domain="FieldName",
    venue="Venue Year",
    year=2024,
)
```

**Outputs**:
- `data/output/paper_metadata.csv`
- `data/output/citations_extracted.csv`
- `data/output/hallucination_coding.csv` (pre-populated template for Phase 2)

---

## Phase 2 — Manual Coding

Code author expertise (per paper) and citation characteristics (per flagged citation).
See [`docs/CODING_GUIDE.md`](docs/CODING_GUIDE.md) for decision rules.

```python
from phase_2_coding.phase2_manual_coding import interactive_coding_session
interactive_coding_session()
```

**Estimated effort**: ~20 min/paper (expertise) + ~5 min/flagged citation

---

## Phase 3 — Statistical Analysis

```python
from phase_3_analysis.phase3_analysis import HallucinationAnalyzer
HallucinationAnalyzer().run_full_analysis()
```

**Outputs**: hypothesis test results (console) + figures in `data/output/figures/`

---

## Data Files

See [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md) for full schema documentation.

Note: `data/` is excluded from version control. Raw PDFs and output CSVs are stored locally only.

---

## Tests

```bash
pytest tests/
```

---

## Citation

Pre-print / paper forthcoming. Citation details will be added upon publication.

## License

Code is released under the MIT License. See `LICENSE` for details.

## Contact

[JAB Lab](https://jzstafura-lab.github.io) · [LinkedIn](https://www.linkedin.com/in/jzstafura)
