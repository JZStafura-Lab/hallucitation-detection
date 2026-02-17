"""
Phase 1 — Automated citation extraction and hallucination detection.

For each PDF in the sample:
  1. Extract plain text (PyPDF2)
  2. Locate and parse the reference list
  3. Verify each citation against CrossRef
  4. Score each citation with GPTZero
  5. Flag citations exceeding HALLUCINATION_THRESHOLD
  6. Write outputs: paper_metadata.csv, citations_extracted.csv,
     hallucination_coding.csv (pre-populated template)

Usage:
    python phase1_automated_processing.py    # processes all pending PDFs
    from phase1_automated_processing import CitationProcessor, process_batch
"""

# TODO: implement CitationProcessor class and process_batch()
