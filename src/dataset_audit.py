
from pathlib import Path

import pandas as pd

# Locate the original Buffalo Pound dataset.
DATA_DIR = (
    Path.home()
    / "Documents"
    / "EcoSentinel"
    / "data"
    / "raw"
    / "buffalo_pound"
    / "FRDR_dataset_1095_download_621_202611201621"
)

# Find all annual CSV files.
csv_files = sorted(DATA_DIR.glob("BPBuoyData_*_Cleaned.csv"))

print("=" * 60)
print("ECOSENTINEL — BUFFALO POUND DATASET AUDIT")
print("=" * 60)

print(f"\nAnnual CSV files found: {len(csv_files)}")

for file in csv_files:
    print(f"\n{'-' * 60}")
    print(f"FILE: {file.name}")

    # Read the dataset.
    df = pd.read_csv(file, low_memory=False)

    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns):,}")

    print("\nColumn names:")
    for column in df.columns:
        print(f"  - {column}")

    print("\nFirst five rows:")
    print(df.head().to_string())

    print("\nMissing values (top 15 columns):")
    missing = df.isna().sum().sort_values(ascending=False)
    print(missing.head(15).to_string())

print("\n" + "=" * 60)
print("AUDIT COMPLETE")
print("=" * 60)
