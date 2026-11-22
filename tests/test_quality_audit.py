from pathlib import Path
import subprocess
import sys

import pandas as pd


def test_quality_audit_generates_expected_tables():
    repo = Path(__file__).resolve().parents[1]
    script = repo / "src" / "quality_audit.py"
    result = subprocess.run(
        [sys.executable, str(script), "--project-dir", str(repo)],
        cwd=str(repo),
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, f"stdout:\n{result.stdout}\n\nstderr:\n{result.stderr}"

    tables = repo / "results" / "tables"
    expected = [
        "year_summary.csv",
        "sensor_reliability_by_year.csv",
        "quality_flag_summary.csv",
        "missing_data_periods.csv",
        "flag_measurement_crosscheck.csv",
        "flag_definitions.csv",
    ]
    for name in expected:
        p = tables / name
        assert p.exists(), f"Missing {name}"
        df = pd.read_csv(p)
        assert len(df) > 0, f"{name} is empty"
        if "year" in df.columns:
            years = set(df["year"].astype(int).tolist())
            assert years == {2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021}
