# Sprint 4L.8 Source Register

**Date:** 2026-11-24T09:34:03.677381+00:00

| ID | Source | Path/URL | Type | Inspected | Use |
|---|---|---|---|---|---|
| S01 | AGENTS.md | /Users/cedricbw/Documents/EcoSentinel/AGENTS.md | Governance | Full | Standards |
| S02 | Acquisition script | research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py | Project code | Full | Auth/acquire behavior |
| S03 | Auth test | research/evidence/sprint_4l3d_existing_key_authentication/scripts/test_existing_key.py | Project code | Full | Local/auth classification |
| S04 | 4L.3C access report | research/evidence/sprint_4l3c_edi_access_investigation/ | Project evidence | Full | Prior access blocker |
| S05 | 4L.7 metadata audit | research/evidence/sprint_4l7_mendota_daily_sensor_audit/ | Project evidence | Full | Daily entity metadata |
| S06 | EDI IAM guide | https://edirepository.org/user-guides/iam | Official docs | Prior full | Key/token flow |
| S07 | IAM token API | https://auth.edirepository.org/auth/ui/api-docs/token | Official docs | Prior full | `POST /auth/v1/key` |
| S08 | DataONE CN sysmeta | cn.dataone.org/cn/v2/meta/...cba9ed... | Repository metadata | Current | Size/SHA-1/replica |
| S09 | NTL HF page | https://lter.limnology.wisc.edu/high-frequency-data/ | Official docs | Prior full | 129/130 context |
| S10 | YSI EXO2 | https://www.ysi.com/exo2 | Manufacturer | Prior full | Sensor capabilities |
| S11 | Turner Cyclops-7F | https://www.turnerdesigns.com/cyclops-7f-submersible-fluorometer | Manufacturer | Prior full | Sensor limitations |

No source establishes that the key is invalid; none supports bypassing authentication.
