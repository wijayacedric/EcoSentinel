
from pathlib import Path

import pandas as pd

# 1. Locate the EcoSentinel project and raw dataset
PROJECT_DIR = Path.home() / "Documents" / "EcoSentinel"
DATA_DIR = PROJECT_DIR / "data" / "raw" / "buffalo_pound"

# 2. Environmental measurements we want to investigate
MEASUREMENTS = [
    "AirTemp_C",
    "WindSp_km/h",
    "PARW1_umol/s/m2",
    "TempShallow_C",
    "pHShallow",
    "ODOShallow_mg/L",
    "SpCondShallow_uS/cm",
    "TurbShallow_NTU+",
    "ChlRFUShallow_RFU",
    "BGPCShallowRFU_RFU",
    "TempDeep_C",
    "pHDeep",
    "ODODeep_mg/L",
    "SpCondDeep_uS/cm",
    "BGPCDeepRFU_RFU",
    "Temp00_C",
    "Temp01_C",
    "Temp02_C",
    "Temp03_C",
    "Temp04_C",
]

availability_results = []
flag_results = []

# 3. Find all annual Buffalo Pound CSV files
files = sorted(DATA_DIR.rglob("BPBuoyData_*_Cleaned.csv"))

if not files:
    raise FileNotFoundError(
        f"No annual CSV files found inside {DATA_DIR}"
    )

# 4. Process each annual dataset
for file in files:
    df = pd.read_csv(file)

    df["DateTime"] = pd.to_datetime(
        df["DateTime"], errors="coerce"
    )

    year = file.stem.split("_")[1]

    valid_dates = df["DateTime"].dropna()
    intervals = valid_dates.sort_values().diff().dropna()

    year_summary = {
        "year": year,
        "rows": len(df),
        "first_date": valid_dates.min(),
        "last_date": valid_dates.max(),
        "duplicate_timestamps": df["DateTime"].duplicated().sum(),
        "median_interval_minutes": (
            intervals.dt.total_seconds().median() / 60
            if not intervals.empty else None
        ),
    }

    print("\n" + "=" * 55)
    print(f"YEAR: {year}")
    print(f"Rows: {len(df):,}")
    print(
        f"Date range: {year_summary['first_date']} "
        f"to {year_summary['last_date']}"
    )
    print(
        f"Duplicate timestamps: "
        f"{year_summary['duplicate_timestamps']}"
    )
    print(
        f"Median interval: "
        f"{year_summary['median_interval_minutes']} minutes"
    )

    # 5. Calculate availability for each measurement
    print("\nMEASUREMENT AVAILABILITY")

    for column in MEASUREMENTS:
        if column not in df.columns:
            print(f"{column:<30} COLUMN NOT FOUND")
            continue

        available = df[column].notna().sum()
        percentage = available / len(df) * 100

        availability_results.append({
            "year": year,
            "measurement": column,
            "available_readings": available,
            "missing_readings": len(df) - available,
            "available_percent": round(percentage, 2),
        })

        print(
            f"{column:<30} "
            f"{percentage:>6.2f}% available"
        )

    # 6. Count quality flags
    print("\nQUALITY FLAG COUNTS")

    for column in df.columns:
        if not column.endswith("_Flag"):
            continue

        counts = (
            df[column]
            .dropna()
            .astype(str)
            .value_counts()
        )

        for flag, count in counts.items():
            flag_results.append({
                "year": year,
                "flag_column": column,
                "flag": flag,
                "count": count,
            })

# 7. Save the results as CSV reports
availability = pd.DataFrame(availability_results)
flags = pd.DataFrame(flag_results)

output_dir = PROJECT_DIR / "results" / "tables"
output_dir.mkdir(parents=True, exist_ok=True)

availability.to_csv(
    output_dir / "measurement_availability.csv",
    index=False,
)

flags.to_csv(
    output_dir / "quality_flag_counts.csv",
    index=False,
)

print("\n" + "=" * 55)
print("AVAILABILITY AUDIT COMPLETE")
print(f"Saved reports to: {output_dir}")
