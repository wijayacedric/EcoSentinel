import importlib.util
from pathlib import Path

import pandas as pd


def load_quality_module(repo_root: Path):
    script = repo_root / "src" / "quality_audit.py"
    spec = importlib.util.spec_from_file_location("quality_audit_gate1", script)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


def write_csv(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False)


def make_fixture_project(tmp_path: Path) -> Path:
    project = tmp_path / "project"
    raw = project / "data" / "raw" / "buffalo_pound" / "fixture"
    # Year 2014: 5 rows, 10-min intervals
    write_csv(raw / "BPBuoyData_2014_Cleaned.csv", [
        {"DateTime": "2014-06-01 00:00:00", "Bat_V": 12.0, "TempShallow_C": 10.0, "TempShallow_C_Flag": "", "pHShallow": 8.0, "pHShallow_Flag": "", "TurbShallow_NTU+": 1.0, "TurbShallow_NTU+_Flag": "B7"},
        {"DateTime": "2014-06-01 00:10:00", "Bat_V": 12.0, "TempShallow_C": None, "TempShallow_C_Flag": "M", "pHShallow": 8.1, "pHShallow_Flag": "", "TurbShallow_NTU+": 1.1, "TurbShallow_NTU+_Flag": "B7"},
        {"DateTime": "2014-06-01 00:20:00", "Bat_V": 12.0, "TempShallow_C": 99.0, "TempShallow_C_Flag": "C", "pHShallow": None, "pHShallow_Flag": "M", "TurbShallow_NTU+": 1.2, "TurbShallow_NTU+_Flag": ""},
        {"DateTime": "2014-06-01 00:30:00", "Bat_V": 12.0, "TempShallow_C": 11.0, "TempShallow_C_Flag": "", "pHShallow": 8.2, "pHShallow_Flag": "A6", "TurbShallow_NTU+": None, "TurbShallow_NTU+_Flag": "M"},
        {"DateTime": "2014-06-01 00:40:00", "Bat_V": 12.0, "TempShallow_C": 12.0, "TempShallow_C_Flag": "", "pHShallow": 8.3, "pHShallow_Flag": "", "TurbShallow_NTU+": 1.3, "TurbShallow_NTU+_Flag": "B6"},
    ])
    # Year 2015: 3 rows, independent
    write_csv(raw / "BPBuoyData_2015_Cleaned.csv", [
        {"DateTime": "2015-05-01 00:00:00", "Bat_V": 12.0, "TempShallow_C": 9.0, "TempShallow_C_Flag": "", "pHShallow": 7.9, "pHShallow_Flag": ""},
        {"DateTime": "2015-05-01 00:10:00", "Bat_V": 12.0, "TempShallow_C": None, "TempShallow_C_Flag": "M", "pHShallow": 8.0, "pHShallow_Flag": ""},
        {"DateTime": "2015-05-01 00:20:00", "Bat_V": 12.0, "TempShallow_C": 9.5, "TempShallow_C_Flag": "", "pHShallow": None, "pHShallow_Flag": "C"},
    ])
    return project


def run_audit(tmp_path: Path):
    repo = Path(__file__).resolve().parents[1]
    mod = load_quality_module(repo)
    project = make_fixture_project(tmp_path)
    mod.main(project)
    out = project / "results" / "tables"
    return {p.name: pd.read_csv(p) for p in out.glob("*.csv")}


def test_each_year_processed_independently(tmp_path):
    tables = run_audit(tmp_path)
    ys = tables["year_summary.csv"].sort_values("year")
    assert ys["year"].astype(int).tolist() == [2014, 2015]
    assert ys.loc[ys["year"] == 2014, "rows"].iloc[0] == 5
    assert ys.loc[ys["year"] == 2015, "rows"].iloc[0] == 3
    # 2015 has no TurbShallow_NTU+ column - should not appear as 2015 rows
    rel = tables["sensor_reliability_by_year.csv"]
    assert set(rel.loc[rel["year"] == 2015, "measurement"]) == {"TempShallow_C", "pHShallow"}


def test_no_year_omitted_or_duplicated(tmp_path):
    tables = run_audit(tmp_path)
    ys = tables["year_summary.csv"]
    assert ys["year"].astype(int).tolist() == sorted(ys["year"].astype(int).tolist())
    assert ys["year"].duplicated().sum() == 0
    rel = tables["sensor_reliability_by_year.csv"]
    # each measurement-year pair unique
    assert rel.duplicated(subset=["year", "measurement"]).sum() == 0


def test_measurement_reliability_hand_calculated(tmp_path):
    tables = run_audit(tmp_path)
    rel = tables["sensor_reliability_by_year.csv"]
    row = rel[(rel["year"] == 2014) & (rel["measurement"] == "TempShallow_C")].iloc[0]
    # values: [10.0, NaN(M), 99.0(C), 11.0, 12.0]
    assert row["total_rows"] == 5
    assert row["non_missing_readings"] == 4
    assert row["missing_readings"] == 1
    assert row["M_flag_count"] == 1
    assert row["C_flag_count"] == 1
    assert row["candidate_usable_readings"] == 3  # excludes M and C
    assert abs(row["availability_percent"] - 80.0) < 1e-6
    assert abs(row["candidate_usable_percent"] - 60.0) < 1e-6


def test_quality_flags_counted_correctly(tmp_path):
    tables = run_audit(tmp_path)
    flags = tables["quality_flag_summary.csv"]
    turb_b7 = flags[(flags["year"] == 2014) & (flags["measurement"] == "TurbShallow_NTU+") & (flags["flag"] == "B7")]
    assert len(turb_b7) == 1
    assert int(turb_b7.iloc[0]["count"]) == 2
    ph_a6 = flags[(flags["year"] == 2014) & (flags["measurement"] == "pHShallow") & (flags["flag"] == "A6")]
    assert int(ph_a6.iloc[0]["count"]) == 1


def test_missing_data_periods_and_gaps(tmp_path):
    tables = run_audit(tmp_path)
    gaps = tables["missing_data_periods.csv"]
    temp_gaps = gaps[(gaps["year"] == 2014) & (gaps["measurement"] == "TempShallow_C")]
    # row2 is NaN+M, row3 is value+C -> two consecutive invalid rows = one gap
    assert len(temp_gaps) == 1
    assert int(temp_gaps.iloc[0]["consecutive_invalid_readings"]) == 2
    assert temp_gaps.iloc[0]["start"] == "2014-06-01 00:10:00"
    assert temp_gaps.iloc[0]["end"] == "2014-06-01 00:20:00"
    assert temp_gaps.iloc[0]["elapsed_between_invalid_readings_minutes"] == 10
    assert "does not estimate the full outage boundary" in temp_gaps.iloc[0]["duration_note"]


def test_flag_measurement_crosschecks(tmp_path):
    tables = run_audit(tmp_path)
    x = tables["flag_measurement_crosscheck.csv"]
    row = x[(x["year"] == 2014) & (x["measurement"] == "TempShallow_C")].iloc[0]
    assert int(row["missing_value_without_M_flag"]) == 0
    assert int(row["M_flag_with_nonmissing_value"]) == 0
    assert int(row["C_flag_with_nonmissing_value"]) == 1  # 99.0 flagged C
    assert int(row["missing_value_with_M_flag"]) == 1


def test_generated_reports_have_expected_structure(tmp_path):
    tables = run_audit(tmp_path)
    expected = {
        "year_summary.csv",
        "sensor_reliability_by_year.csv",
        "quality_flag_summary.csv",
        "missing_data_periods.csv",
        "flag_measurement_crosscheck.csv",
        "flag_definitions.csv",
    }
    assert expected.issubset(set(tables.keys()))
    for name in expected:
        assert len(tables[name]) > 0
    # year coverage
    for name in expected - {"flag_definitions.csv"}:
        assert set(tables[name]["year"].astype(int).unique()) == {2014, 2015}


def test_flag_definitions_preserve_metadata_meaning(tmp_path):
    tables = run_audit(tmp_path)
    definitions = tables["flag_definitions.csv"].set_index("flag")["definition"]
    assert "sensor may have been removed" in definitions["M"]
    assert "not detected by" in definitions["A5"]
    assert "shallow and deep in 2017" in definitions["A6"]
    assert "after site visit" in definitions["B7"]
