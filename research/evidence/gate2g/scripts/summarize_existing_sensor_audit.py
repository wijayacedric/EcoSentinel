#!/usr/bin/env python3
"""Summarize existing sensor audit artifacts for Gate 2G (read-only)."""
import csv, json
from datetime import datetime, timezone
from pathlib import Path
root = Path('/Users/cedricbw/Documents/EcoSentinel')
out = root/'research/evidence/gate2g/derived/sensor_audit_summary.json'

def read_csv(p):
    with open(p, newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

summary = {
  'generated_at': datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
  'inputs': {},
  'year_summary': [],
  'quality_flag_summary': [],
  'missing_data_periods_count': None,
  'measurement_availability_count': None,
  'sensor_reliability_by_year_count': None,
}
for name in ['year_summary.csv','quality_flag_summary.csv','missing_data_periods.csv','measurement_availability.csv','sensor_reliability_by_year.csv','flag_definitions.csv']:
    p = root/'results/tables'/name
    summary['inputs'][name] = {'path': str(p.relative_to(root)), 'exists': p.exists()}
    if p.exists():
        rows = read_csv(p)
        if name == 'year_summary.csv': summary['year_summary'] = rows
        elif name == 'quality_flag_summary.csv': summary['quality_flag_summary'] = rows
        elif name == 'missing_data_periods.csv': summary['missing_data_periods_count'] = len(rows)
        elif name == 'measurement_availability.csv': summary['measurement_availability_count'] = len(rows)
        elif name == 'sensor_reliability_by_year.csv': summary['sensor_reliability_by_year_count'] = len(rows)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(summary, indent=2), encoding='utf-8')
print('wrote', out)
