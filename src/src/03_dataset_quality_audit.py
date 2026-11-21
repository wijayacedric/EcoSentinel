from pathlib import Path

import pandas as pd

# --------------------------------------------------
# 1. PROJECT PATHS
# --------------------------------------------------

PROJECT_DIR = Path.home() / "Documents" / "EcoSentinel"
DATA_DIR = PROJECT_DIR / "data" / "raw" / "buffalo_pound"
OUTPUT_DIR = PROJECT_DIR / "results" / "tables"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# 2. OFFICIAL FLAG DEFINITIONS
# --------------------------------------------------

FLAG_DEFINITIONS = {
    "M": "Missing measurement",
    "C": "Faulty or unrealistic measurement",
    "A2": "PAR below sensor operating range; adjusted to zero",
    "A3": "Inverted PAR readings; requires inspection",
    "A4": "2015 underwater PAR sensor shading; use higher sensor value",
    "A5": "Unusual local rainfall event; potentially genuine",
    "A6": "Corrected specific conductivity measurement",
    "B6": "Raw specific conductivity affected by calibration issues",
    "B7": "Potential fouling-related pigment or turbidity spike",
}


# --------------------------------------------------
# 3. FIND ANNUAL DATA FILES
# --------------------------------------------------

files = sorted(DATA_DIR.rglob("BPBuoyData_*_Cleaned.csv"))

if not files:
    raise FileNotFoundError(
        f"No annual CSV files found inside {DATA_DIR}"
    )

print(f"Found {len(files)} annual datasets.")


# --------------------------------------------------
# 4. STORAGE FOR RESULTS
# --------------------------------------------------

year_results = []
sensor_results = []
flag_results = []
gap_results = []
crosscheck_results = []


# --------------------------------------------------
# 5. PROCESS EACH YEAR
# --------------------------------------------------

for file in files:

    print("\n" + "=" * 65)

    year = file.stem.split("_")[1]

    print(f"ANALYSING YEAR: {year}")

    df = pd.read_csv(file, low_memory=False)

    if "DateTime" not in df.columns:
        print(f"Skipping {year}: DateTime column missing.")
        continue

    df["DateTime"] = pd.to_datetime(
        df["DateTime"], errors="coerce"
    )

    df = df.sort_values("DateTime").reset_index(drop=True)

    valid_dates = df["DateTime"].dropna()

    intervals = (
        valid_dates.sort_values()
        .diff()
        .dropna()
    )

    expected_interval = (
        intervals.dt.total_seconds().median() / 60
        if not intervals.empty
        else None
    )

    # Identify environmental measurements automatically.
    # DateTime, battery voltage and quality flags are excluded.

    measurements = []

    for column in df.columns:

        if column in ["DateTime", "Bat_V"]:
            continue

        if column.endswith("_Flag"):
            continue

        numeric_values = pd.to_numeric(
            df[column], errors="coerce"
        )

        if numeric_values.notna().any():
            measurements.append(column)
            df[column] = numeric_values

    print(f"Rows: {len(df):,}")
    print(f"Measurements identified: {len(measurements)}")
    print(f"Expected interval: {expected_interval} minutes")


    # --------------------------------------------------
    # 6. YEAR-LEVEL DATA SUMMARY
    # --------------------------------------------------

    year_results.append({
        "year": year,
        "rows": len(df),
        "first_date": valid_dates.min(),
        "last_date": valid_dates.max(),
        "duplicate_timestamps": df["DateTime"].duplicated().sum(),
        "invalid_timestamps": df["DateTime"].isna().sum(),
        "median_interval_minutes": expected_interval,
        "measurement_count": len(measurements),
    })


    # --------------------------------------------------
    # 7. MEASUREMENT RELIABILITY
    # --------------------------------------------------
print("\nMEASUREMENT RELIABILITY")

for column in measurements:
    flag_column = f"{column}_Flag"
    values = df[column]

    if flag_column in df.columns:
        flags = (
            df[flag_column]
            .astype("string")
            .fillna("")
            .str.strip()
        )
    else:
        flags = pd.Series("", index=df.index)

    missing = values.isna()

    missing_flag = flags.eq("M")
    faulty_flag = flags.eq("C")

    b7_flag = flags.str.contains(
        r"(?:^|,\s*)B7(?:$|,)", regex=True
    )

    a6_flag = flags.str.contains(
        r"(?:^|,\s*)A6(?:$|,)", regex=True
    )

    b6_flag = flags.str.contains(
        r"(?:^|,\s*)B6(?:$|,)", regex=True
    )

    # Candidate usable readings exclude M and C.
    # Other flags are retained for separate investigation.

    candidate_usable = (
        values.notna()
        & ~missing_flag
        & ~faulty_flag
    )

    sensor_results.append({
        "year": year,
        "measurement": column,
        "total_rows": len(df),
        "non_missing_readings": int(values.notna().sum()),
        "missing_readings": int(missing.sum()),
        "candidate_usable_readings": int(candidate_usable.sum()),
               "availability_percent": float(
            values.notna().mean() * 100
        ),
        "candidate_usable_percent": float(
            candidate_usable.mean() * 100
        ),
        "B7_flag_count": int(b7_flag.sum()),
        "A6_flag_count": int(a6_flag.sum()),
        "B6_flag_count": int(b6_flag.sum()),
    })

    print(
        f"{column:<32} "
        f"{values.notna().mean() * 100:6.2f}% available"
    )

    # --------------------------------------------------
    # 8. FLAG COUNTS
    # --------------------------------------------------

       # --------------------------------------------------
    # 8. FLAG COUNTS
    # --------------------------------------------------

    if flag_column in df.columns:
        flag_counts = (
            flags[flags != ""]
            .value_counts()
        )

        for flag, count in flag_counts.items():
            flag_results.append({
                "year": year,
                "measurement": column,
                "flag": flag,
                "count": int(count),
                "definition": FLAG_DEFINITIONS.get(
                    flag, "Unknown or compound flag"
                ),
            })

    # --------------------------------------------------
    # 9. FLAG / MEASUREMENT CROSS-CHECK
    # --------------------------------------------------

    crosscheck_results.append({
        "year": year,
        "measurement": column,
        "missing_value_without_M_flag": int(
            (missing & ~missing_flag).sum()
        ),
        "M_flag_with_nonmissing_value": int(
            (missing_flag & values.notna()).sum()
        ),
        "C_flag_with_nonmissing_value": int(
            (faulty_flag & values.notna()).sum()
        ),
        "missing_value_with_M_flag": int(
            (missing & missing_flag).sum()
        ),
    })

    # --------------------------------------------------
    # 10. CONSECUTIVE INVALID-DATA PERIODS
    # --------------------------------------------------

    # A reading is invalid for this diagnostic if its
    # value is missing or its flag is M or C.
    # This does NOT delete the original measurement.

    invalid = (
        missing
        | missing_flag
        | faulty_flag
    )

    # Find consecutive runs of invalid observations.

    run_id = invalid.ne(
        invalid.shift(fill_value=False)
    ).cumsum()

    invalid_groups = df.loc[invalid].groupby(run_id[invalid])

    for _, group in invalid_groups:
        start = group["DateTime"].min()
        end = group["DateTime"].max()

        run_length = len(group)

        approximate_duration = (
            run_length * expected_interval
            if expected_interval is not None
            else None
        )

        gap_results.append({
            "year": year,
            "measurement": column,
            "start": start,
            "end": end,
            "consecutive_invalid_readings": run_length,
            "approx_duration_minutes": approximate_duration,
            "reason": "Missing value or M/C flag",
        })


# --------------------------------------------------
# 11. SAVE ALL REPORTS
# --------------------------------------------------

reports = {
    "year_summary.csv": year_results,
    "sensor_reliability_by_year.csv": sensor_results,
    "quality_flag_summary.csv": flag_results,
    "missing_data_periods.csv": gap_results,
    "flag_measurement_crosscheck.csv": crosscheck_results,
}

for filename, results in reports.items():

    pd.DataFrame(results).to_csv(
        OUTPUT_DIR / filename,
        index=False,
    )

# Save the flag definitions separately.

pd.DataFrame([
    {"flag": flag, "definition": definition}
    for flag, definition in FLAG_DEFINITIONS.items()
]).to_csv(
    OUTPUT_DIR / "flag_definitions.csv",
    index=False,
)


# --------------------------------------------------
# 12. COMPLETION
# --------------------------------------------------

print("\n" + "=" * 65)
print("ECOSENTINEL DATA QUALITY AUDIT COMPLETE")

print(f"\nReports saved in:\n{OUTPUT_DIR}")

for filename in reports:
    print(f"  - {filename}")

print("  - flag_definitions.csv")

print("\nNo original raw measurements have been modified.")
print("No observations have been automatically deleted.")