"""
Phase 3 — Statistical analysis and visualisation.

Tests the three pre-registered research questions:
  RQ1 (Expertise)       — logistic / chi-square on Expertise_Match × Is_Hallucinated
  RQ2 (Domain Velocity) — ANOVA / Kruskal-Wallis across domain buckets
  RQ3 (Location)        — chi-square on Section_Location × Is_Hallucinated

Generates figures in data/output/figures/:
  hallucinations_by_domain.png
  expertise_distance.png
  recency_distribution.png
  section_location.png

Usage:
    python phase3_analysis.py                # run full analysis
    from phase3_analysis import HallucinationAnalyzer
"""

# TODO: implement HallucinationAnalyzer class and run_full_analysis()
