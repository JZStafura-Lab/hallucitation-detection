# Data Dictionary

Describes all CSV files produced by the pipeline. All files live in `data/output/`.

---

## sample_tracking.csv

Master file of all papers in the stratified random sample.

| Field | Type | Description |
|-------|------|-------------|
| Paper_ID | string | Unique identifier (P0001 …) |
| Venue | string | Publication venue |
| Domain_Category | string | Broad field bucket |
| Title | string | Paper title |
| Authors | string | Full author list |
| ArXiv_ID | string | arXiv identifier if applicable |
| DOI | string | DOI if available |
| PDF_URL | string | Source URL |
| Download_Status | string | pending \| downloaded \| failed \| manual_required |
| Local_PDF_Path | string | Relative path to local PDF |
| Sampling_Stratum | string | Stratum used in stratified sampling |
| Sampling_Seed | int | RNG seed for reproducibility |
| Notes | string | Free-text notes |

---

## paper_metadata.csv

One row per paper; populated by Phase 1.

| Field | Type | Description |
|-------|------|-------------|
| Paper_ID | string | Links to sample_tracking |
| Domain_Category | string | Broad field bucket |
| Venue | string | Publication venue |
| Publication_Year | int | Year of publication |
| Title | string | Paper title |
| Authors | string | Full author list |
| Processing_Status | string | pending \| processed \| error |

---

## citations_extracted.csv

One row per extracted citation; populated by Phase 1.

| Field | Type | Description |
|-------|------|-------------|
| Citation_ID | string | P0001_C001, P0001_C002 … |
| Paper_ID | string | Links to paper_metadata |
| Citation_Text | string | Raw citation string |
| Citation_Year | int | Extracted publication year |
| Authors_Cited | string | Cited authors |
| Title_Cited | string | Cited paper title |
| Is_Hallucinated | int | 0=Real, 1=Hallucinated, -1=Uncertain |
| Verification_Method | string | CrossRef \| GoogleScholar \| Manual |
| CrossRef_Score | float | CrossRef relevance score |
| GPTZero_Score | float | GPTZero AI-probability score (0–1) |
| Section_Location_Auto | string | Auto-detected paper section |
| Context_Sentence | string | Surrounding sentence |

---

## author_expertise_coding.csv

One row per paper with flagged citations; populated in Phase 2A.

| Field | Type | Description |
|-------|------|-------------|
| Paper_ID | string | Links to paper_metadata |
| Key_Author_1 | string | First key author name |
| Key_Author_1_Domain | string | Author's primary domain |
| Key_Author_1_Top_Papers | string | Author's most-cited works |
| Key_Author_2 | string | Second key author name |
| Key_Author_2_Domain | string | Author's primary domain |
| Key_Author_2_Top_Papers | string | Author's most-cited works |
| Paper_Domain | string | Paper's primary domain |
| Expertise_Match | int | 0=Core, 1=Adjacent, 2=Distant |
| Notes | string | Free-text notes |
| Coding_Time_Minutes | float | Time spent on this paper |
| Coder_ID | string | Identifies the coder |

---

## hallucination_coding.csv

One row per flagged citation; populated in Phase 2B.

| Field | Type | Description |
|-------|------|-------------|
| Citation_ID | string | Links to citations_extracted |
| Paper_ID | string | Links to paper_metadata |
| Citation_Domain | string | Domain of the cited work |
| Citation_Role | string | B \| M \| R \| E \| T |
| Distance_from_Paper | int | 0=Core, 1=Peripheral (auto-calculated) |
| Recency_Category | int | 0–4 (auto-calculated) |
| Temporal_Distance | int | Years between paper and cited work |
| Notes | string | Free-text notes |
| Coding_Time_Minutes | float | Time spent on this citation |
| Coder_ID | string | Identifies the coder |
