"""
Project initialisation script.

Run once after cloning:
    python setup.py

Creates required directories and empty CSV templates.
"""

from pathlib import Path
from config import DATA_DIR, PDF_DIR, OUTPUT_DIR, FIGURES_DIR, LOGS_DIR
from data_templates import create_all_templates


def create_directories() -> None:
    dirs = [DATA_DIR, PDF_DIR, OUTPUT_DIR, FIGURES_DIR, LOGS_DIR]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {d}")


def main() -> None:
    print("=== Hallucitation Detection — Project Setup ===\n")

    print("Creating directories…")
    create_directories()

    print("\nGenerating CSV templates…")
    create_all_templates()

    print("\nSetup complete.")
    print("Next: add API keys to config_local.py (or set environment variables),")
    print("then see README.md for the full workflow.")


if __name__ == "__main__":
    main()
