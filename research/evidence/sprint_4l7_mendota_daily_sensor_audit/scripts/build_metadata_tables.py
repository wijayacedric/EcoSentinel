#!/usr/bin/env python3
"""Metadata-level Sprint 4L.7 tables. No raw daily sensor data are present."""
import csv, json
from pathlib import Path
from collections import Counter, defaultdict
from datetime import date
import xml.etree.ElementTree as ET

BASE=Path('research/evidence/sprint_4l7_mendota_daily_sensor_audit')
T=BASE/'tables'; T.mkdir(parents=True,exist_ok=True)
EML=Path('research/evidence/sprint_4k_mendota_authorised_access/acquisition/129.42/metadata_129.42.xml')
BIO=Path('research/evidence/sprint_4l_mendota_biology_audit/acquisition/88.31/North_Temperate_Lakes_LTER_-_Phytoplankton_-_Madison_Lakes_Area__f2de15b2fff6ae962a04c150c0a1c510.dat')

# Entity inventory from EML
ents=[]
root=ET.parse(EML).getroot()
for dt in root.iter():
    if dt.tag.split('}')[-1]!='dataTable': continue
    name=obj=size=auth=method=desc=''
    for e in dt.iter():
        t=e.tag.split('}')[-1]; tx=(e.text or '').strip()
        if t=='entityName' and tx and not name: name=tx
        if t=='objectName' and tx and not obj: obj=tx
        if t=='size' and tx and not size: size=tx
        if t=='authentication' and tx and not auth: auth=tx; method=e.attrib.get('method','')
        if t=='entityDescription' and tx and not desc: desc=tx
    ents.append((name,obj,size,method,auth,desc))
rows=[]
for name,obj,size,method,auth,desc in ents:
    if 'Daily' in name:
        rec='ACQUIRE (priority)'; reason='daily aggregates; variables relevant to EcoSentinel; smallest relevant entity'
    elif 'Hourly' in name:
        rec='DO NOT ACQUIRE this sprint'; reason='larger; daily sufficient for feasibility; retain as future option'
    elif 'High Resolution' in name:
        rec='DO NOT ACQUIRE'; reason='682 MB; not needed for daily feasibility'
    elif 'sensors' in name.lower():
        rec='ALREADY ACQUIRED'; reason='verified 1,039 B sensor inventory from Sprint 4K'
    else:
        rec='not needed'; reason=''
    rows.append({'entity_name':name,'object_name':obj,'size_bytes':size,'eml_checksum_algorithm':method,
                 'eml_checksum':auth,'resolution':'daily' if 'Daily' in name else ('hourly' if 'Hourly' in name else ('1-minute' if 'High Resolution' in name else 'inventory')),
                 'acquisition_recommendation':rec,'reason':reason,'raw_status':'already present' if 'sensors' in name.lower() else 'NOT ACQUIRED'})
with (T/'PACKAGE_AND_ENTITY_INVENTORY.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

# Variable metadata summary
vars_ = [
 ('avg_air_temp','average air temperature (2m above sfc)','celsius','C;E;H','air temperature','2006-2025 package','daily mean'),
 ('avg_rel_hum','average relative humidity (2m above sfc)','percent','C;E','relative humidity','2006-2025 package','daily mean'),
 ('avg_wind_speed','daily average wind speed (3m above sfc)','meterPerSecond','C','wind speed','2006-2025 package','daily mean'),
 ('avg_wind_dir','average wind direction (3m above sfc)','degree','C;H','wind direction','2006-2025 package','daily mean'),
 ('avg_chlor_rfu_turner','chlorophyll a (RFU), 0.5m, Turner Cyclops 7','RFU (unit not in EML)','C;H','chlorophyll proxy','2006-2019 (documented)','daily mean'),
 ('avg_chlor_rfu_ysi','chlorophyll a (RFU), 0.5m, YSI EXO2','RFU (unit not in EML)','C;H;E;G','chlorophyll proxy','2019-present (documented)','daily mean'),
 ('avg_phyco_rfu_turner','phycocyanin (RFU), 0.5m, Turner Cyclops 7','RFU (unit not in EML)','C;H','phycocyanin proxy','2006-2019 (documented)','daily mean'),
 ('avg_phyco_rfu_ysi','phycocyanin (RFU), 0.5m, YSI EXO2','RFU (unit not in EML)','C;H;E;G','phycocyanin proxy','2019-present (documented)','daily mean'),
 ('avg_par','PAR above water (2m)','micromolePerMeterSquaredPerSecond','C;H','light','2006-2025 package','daily mean'),
 ('avg_par_below','PAR below water (1m)','micromolePerMeterSquaredPerSecond','C;G','underwater light','2006-2025 package','daily mean'),
 ('avg_do_wtemp','water temperature, YSI DO sensor (0.5m)','celsius','C;H','water temperature','2006-2025 package','daily mean'),
 ('avg_do_sat','DO % saturation (0.5m)','percent','C;E;H','DO','2006-2025 package','daily mean'),
 ('avg_do_raw','DO mg/L (0.5m)','milligramPerLiter','C;E;H','DO','2006-2025 package','daily mean'),
 ('avg_pco2_ppm','CO2 (1m)','ppm (unit not explicit in EML)','C;E','pCO2','2017-present per sensor list','daily mean'),
 ('avg_ph','pH (0.5m)','dimensionless','C','pH','2019-present per sensor list','daily mean'),
 ('avg_fdom','fDOM (0.5m)','RFU/ppb QSU not explicit','C','fDOM proxy','2019-present per sensor list','daily mean'),
 ('avg_turbidity','turbidity (0.5m)','FNU (unit not explicit in EML)','C','turbidity','2019-present per sensor list','daily mean'),
 ('avg_spec_cond','specific conductance (0.5m)','uS/cm (unit not explicit in EML)','C;H','specific conductance','2006 only and 2019-present per sensor list','daily mean'),
]
out=[]
for v,d,u,fl,role,era,freq in vars_:
    out.append({'variable':v,'eml_definition':d,'eml_unit':u,'flag_codes':fl,'role':role,
                'documented_era':era,'documented_frequency':freq,
                'actual_first_valid':'NOT AVAILABLE','actual_last_valid':'NOT AVAILABLE',
                'total_observations':'NOT AVAILABLE','unique_dates':'NOT AVAILABLE',
                'missingness':'NOT AVAILABLE','longest_gap':'NOT AVAILABLE',
                'raw_status':'BLOCKED_NO_DAILY_DATA'})
with (T/'VARIABLE_COVERAGE_SUMMARY.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

# Annual variable coverage status table (explicitly not actual)
years=list(range(2006,2026))
out=[]
for v,d,u,fl,role,era,freq in vars_:
    for y in years:
        out.append({'variable':v,'year':y,'expected_package_coverage':'2006-2025',
                    'documented_era':era,'annual_counts':'NOT AVAILABLE',
                    'raw_status':'BLOCKED_NO_DAILY_DATA'})
with (T/'ANNUAL_VARIABLE_COVERAGE.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

# Sampling intervals/gaps status
with (T/'SAMPLING_INTERVALS_AND_GAPS.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['variable','interval_or_gap','value','status','note'])
    w.writerow(['ALL','N/A','NOT AVAILABLE','BLOCKED_NO_DAILY_DATA','No raw daily entity acquired; cannot compute intervals/gaps.'])

# Biology dates and metadata-level overlap
bio_dates=set()
for r in csv.DictReader(open(BIO,newline='',encoding='utf-8')):
    if r['lakeid']=='ME': bio_dates.add(r['sampledate'])
by_year=Counter(d[:4] for d in bio_dates)
overlap=[]
for y in range(1995,2021):
    n=by_year.get(str(y),0)
    if n==0: continue
    in_pkg = 2006 <= y <= 2025
    overlap.append({'year':y,'biology_dates':n,'within_129_42_package_coverage':'yes' if in_pkg else 'no',
                    'daily_sensor_records_verified':'0','same_day_valid_verified':'0',
                    'status':'BLOCKED_NO_DAILY_DATA' if in_pkg else 'outside_metadata_coverage',
                    'note':'Potential overlap only; no daily observations acquired.'})
with (T/'BIOLOGY_SENSOR_DATE_OVERLAP.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(overlap[0].keys())); w.writeheader(); w.writerows(overlap)

summary={
 'biology_dates_total':len(bio_dates),
 'biology_dates_2006_2020':sum(1 for d in bio_dates if 2006<=int(d[:4])<=2020),
 'biology_dates_before_2006':sum(1 for d in bio_dates if int(d[:4])<2006),
 'biology_dates_after_2020':sum(1 for d in bio_dates if int(d[:4])>2020),
 'daily_entity':{'object_name':'ntl129_1_v16.csv','size':490187,'md5':'eb7b3a3848b27074bac4504236ccefc3','sha1_cn':'bb1d8a281a3d580cad45549551abdbaed1ae03fe','status':'not acquired'},
 'sensor_list':{'object_name':'mendota_buoy_sensors_v3.csv','size':1039,'md5':'6e5c2a9204fe7e9e15a319a0344ebff0','status':'acquired/verified'},
 'package_coverage':'2006-2025 metadata',
}
(BASE/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
