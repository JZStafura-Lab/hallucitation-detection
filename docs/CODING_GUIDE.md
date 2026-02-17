# Coding Guide

This document specifies the manual coding procedures for Phase 2.

## 2A — Author Expertise Coding

**Goal**: Determine how well the paper's topic aligns with each key author's demonstrated expertise.

**Steps per paper (~20 min)**:
1. Identify the two key authors (typically first and last/corresponding author).
2. Locate each author's Google Scholar or institutional profile.
3. Note their primary research domain(s) and five most-cited papers.
4. Classify the paper's own primary domain.
5. Assign **Expertise_Match** for each key author:

| Code | Label    | Criterion |
|------|----------|-----------|
| 0    | Core     | Paper domain exactly matches ≥1 author's primary domain |
| 1    | Adjacent | Related field or overlapping methods, different subarea |
| 2    | Distant  | Outside both authors' documented publication history |

Use the most lenient match across the two key authors (e.g., if one author is Core, code 0).

---

## 2B — Citation Characteristic Coding

**Goal**: Characterise each flagged citation along two dimensions.

**Steps per citation (~5 min)**:

### Citation Domain
Assign one domain from the standardised list in `config.py → DOMAINS`.

### Citation Role

| Code | Label       | Description |
|------|-------------|-------------|
| B    | Background  | General context, prior-work overview |
| M    | Methods     | Specific technique, algorithm, or tool adopted |
| R    | Related Work| Direct comparison to a similar approach |
| E    | Empirical   | Dataset, benchmark, or empirical finding cited |
| T    | Theoretical | Mathematical result, proof, or formal theorem |

### Distance_from_Paper (auto-calculated)
- **0 — Core**: Citation domain matches the paper's domain
- **1 — Peripheral**: Citation domain is outside the paper's domain

### Recency_Category (auto-calculated from publication years)

| Code | Label              |
|------|--------------------|
| 0    | Very Recent (0–1 yr) |
| 1    | Recent (2–5 yr)    |
| 2    | Moderate (6–10 yr) |
| 3    | Old (11+ yr)       |
| 4    | Future (impossible date — strong hallucination signal) |

---

## Reliability

Re-code a random 10% subsample after completing the full dataset to assess intra-rater reliability. Report Cohen's κ for Expertise_Match and Citation_Role.
