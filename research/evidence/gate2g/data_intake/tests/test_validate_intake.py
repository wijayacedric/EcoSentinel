import json, subprocess, sys, tempfile, hashlib
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[5]
SCRIPT = ROOT / 'research/evidence/gate2g/scripts/validate_intake.py'
FIXTURE = Path(__file__).resolve().parent / 'synthetic_biological_sample.csv'


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


class TestValidateIntake(unittest.TestCase):
    def run_validator(self, inp, out, kind='biological'):
        return subprocess.run([sys.executable, str(SCRIPT), str(inp), '--kind', kind, '--out', str(out)], cwd=ROOT, capture_output=True, text=True)

    def test_synthetic_fixture_validates_and_source_unchanged(self):
        before = sha256(FIXTURE)
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / 'report.json'
            r = self.run_validator(FIXTURE, out)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            report = json.loads(out.read_text())
            self.assertEqual(report['status'], 'ok')
            self.assertEqual(report['sha256'], before)
            self.assertIn('rows', report['summary'])
            self.assertFalse(report['errors'])
        self.assertEqual(sha256(FIXTURE), before)

    def test_missing_required_fields_warns(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / 'bad.csv'
            p.write_text('sample_id,notes\nA,B\n', encoding='utf-8')
            out = Path(td) / 'r.json'
            r = self.run_validator(p, out)
            self.assertEqual(r.returncode, 0)
            report = json.loads(out.read_text())
            self.assertTrue(any('Missing required biological fields' in w for w in report['warnings']))

    def test_invalid_date_and_numeric_error(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / 'bad.csv'
            p.write_text('sample_date,location,depth_m,chlorophyll_a\n2024-99-01,Loc,notnum,abc\n', encoding='utf-8')
            out = Path(td) / 'r.json'
            r = self.run_validator(p, out)
            self.assertNotEqual(r.returncode, 0)
            report = json.loads(out.read_text())
            self.assertEqual(report['status'], 'error')
            self.assertTrue(any('Invalid sample_date' in e for e in report['errors']))
            self.assertTrue(any('depth_m' in e for e in report['errors']))

    def test_duplicate_rows_warn(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / 'dup.csv'
            p.write_text('sample_date,location,depth_m,sample_id,taxon_name\n2024-01-01,L,1,S1,T1\n2024-01-01,L,1,S1,T1\n', encoding='utf-8')
            out = Path(td) / 'r.json'
            r = self.run_validator(p, out)
            self.assertEqual(r.returncode, 0)
            report = json.loads(out.read_text())
            self.assertTrue(any('duplicate biological rows' in w.lower() for w in report['warnings']))

    def test_missing_file_errors(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / 'r.json'
            r = self.run_validator(Path(td)/'nope.csv', out)
            self.assertNotEqual(r.returncode, 0)
            report = json.loads(out.read_text())
            self.assertEqual(report['status'], 'error')


if __name__ == '__main__':
    unittest.main()
