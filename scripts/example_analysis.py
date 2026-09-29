from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
RESULTS_DIR = ROOT / "results"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def main():
    """Minimal example for a reproducible research workflow."""
    input_file = RAW_DIR / "example.csv"

    if not input_file.exists():
        print(f"No input file found: {input_file}")
        print("Add a CSV file named example.csv to data/raw/ and rerun.")
        return

    df = pd.read_csv(input_file)

    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nMissing values:")
    print(df.isna().sum())

    summary = df.describe(include="all")
    output_file = RESULTS_DIR / "example_summary.csv"
    summary.to_csv(output_file)

    print(f"\nSummary saved to: {output_file}")


if __name__ == "__main__":
    main()
