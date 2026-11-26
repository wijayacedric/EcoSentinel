#!/usr/bin/env python3
"""Build metadata-level sensor audit tables. No raw daily observations are present."""
import csv, json
from pathlib import Path
BASE=Path('research/evidence/sprint_4l7_mendota_daily_sensor_audit')
T=BASE/'tables'; T.mkdir(parents=True,exist_ok=True)

# Sensor deployment era table from 4L.1 transcription
src=Path('research/evidence/sprint_4l_sensor_inventory_audit/SENSOR_INVENTORY_TRANSCRIPTION.csv')
rows=list(csv.DictReader(src.open()))
out=[]
for r in rows:
    out.append({'sensor_row':r['row_number'],'parameter':r['parameter'],'manufacturer':r['sensor_manufacturer'],
                'model':r['sensor_model'],'date_began':r['date_began'],'date_ended':r['date_ended'],
                'documented_span':r['documented_span'],'transition_note':r['transition_or_overlap_note']})
with (T/'SENSOR_DEPLOYMENT_ERA.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

# Schema table
schema=[
 ('year4','Four-digit year','nominalYear','date','No'),
 ('sampledate','Sample Date','date','date','No'),
 ('avg_air_temp','average air temperature (2m above sfc)','celsius','meteorology','C;E;H'),
 ('avg_rel_hum','average relative humidity (2m above sfc)','percent','meteorology','C;E'),
 ('avg_wind_speed','daily average wind speed (3m above sfc)','meterPerSecond','meteorology','C'),
 ('avg_wind_dir','average wind direction (3m above sfc)','degree','meteorology','C;H'),
 ('avg_chlor_rfu_turner','chlorophyll a RFU, 0.5m, Turner Cyclops 7, 2006-2019','RFU','biological proxy','C;H'),
 ('avg_chlor_rfu_ysi','chlorophyll a RFU, 0.5m, YSI EXO2, 2019-present','RFU','biological proxy','C;H;E;G'),
 ('avg_phyco_rfu_turner','phycocyanin RFU, 0.5m, Turner Cyclops 7, 2006-2019','RFU','biological proxy','C;H'),
 ('avg_phyco_rfu_ysi','phycocyanin RFU, 0.5m, YSI EXO2, 2019-present','RFU','biological proxy','C;H;E;G'),
 ('avg_par','PAR above water (2m)','micromolePerMeterSquaredPerSecond','light','C;H'),
 ('avg_par_below','PAR below water (1m)','micromolePerMeterSquaredPerSecond','light','C;G'),
 ('avg_do_wtemp','water temperature, YSI DO sensor (0.5m)','celsius','water temperature','C;H'),
 ('avg_do_sat','DO % saturation (0.5m)','percent','DO','C;E;H'),
 ('avg_do_raw','DO mg/L (0.5m)','milligramPerLiter','DO','C;E;H'),
 ('avg_pco2_ppm','CO2 (1m)','ppm (not explicit in EML)','carbon','C;E'),
 ('avg_ph','pH (0.5m)','dimensionless','pH','C'),
 ('avg_fdom','fDOM (0.5m)','RFU/ppb QSU (not explicit in EML)','optical proxy','C'),
 ('avg_turbidity','turbidity (0.5m)','FNU (not explicit in EML)','optical','C'),
 ('avg_spec_cond','specific conductance (0.5m)','uS/cm (not explicit in EML)','conductivity','C;H'),
]
with (T/'SENSOR_SCHEMA.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['field','eml_definition','unit_or_type','role','expected_flag_codes','raw_header_verified'])
    for s in schema: w.writerow(list(s)+['NO_RAW_DAILY_FILE'])

# Flag definitions
flags=[
 ('C','Sensor off','all flag columns'),
 ('E','Sensor noisy or malfunctioning','air temp, RH, YSI chlorophyll/phycocyanin, DO sat/raw, pCO2'),
 ('H','Outside of standard range','air temp, wind dir, Turner/YSI chlorophyll/phycocyanin, PAR, DO, spec cond'),
 ('G','Sensor - suspected biofouling','YSI chlorophyll/phycocyanin, PAR below'),
]
with (T/'QC_FLAG_DEFINITIONS.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['code','definition','where_documented']); w.writerows(flags)

# Depth compatibility
depth=[
 ('avg_do_wtemp','0.5 m','water temperature','0-8 m composite','Weakly comparable','surface point vs column composite'),
 ('avg_do_sat','0.5 m','DO % saturation','0-8 m composite','Weakly comparable','surface point vs column composite'),
 ('avg_do_raw','0.5 m','DO mg/L','0-8 m composite','Weakly comparable','surface point vs column composite'),
 ('avg_ph','0.5 m','pH','0-8 m composite','Weakly comparable','surface point vs column composite'),
 ('avg_spec_cond','0.5 m','specific conductance','0-8 m composite','Weakly comparable','surface point vs column composite'),
 ('avg_turbidity','0.5 m','turbidity','0-8 m composite','Weakly comparable','surface point vs column composite'),
 ('avg_chlor_rfu_turner','0.5 m','chlorophyll RFU','0-8 m composite','Weakly comparable','proxy; sensor-specific; 2006-2019'),
 ('avg_chlor_rfu_ysi','0.5 m','chlorophyll RFU','0-8 m composite','Weakly comparable','proxy; sensor-specific; 2019+'),
 ('avg_phyco_rfu_turner','0.5 m','phycocyanin RFU','0-8 m composite','Weakly comparable','proxy; sensor-specific; 2006-2019'),
 ('avg_phyco_rfu_ysi','0.5 m','phycocyanin RFU','0-8 m composite','Weakly comparable','proxy; sensor-specific; 2019+'),
 ('avg_pco2_ppm','1 m','pCO2','0-8 m composite','Weakly comparable','single depth; no biological counterpart'),
 ('avg_par_below','1 m','underwater PAR','0-8 m composite','Weakly comparable','light context, not biomass'),
 ('avg_par','2 m above water','above-water PAR','0-8 m composite','Not comparable','atmospheric context'),
 ('meteorology','2-3 m above water','air temp/RH/wind','0-8 m composite','Not comparable','atmospheric context'),
]
with (T/'DEPTH_COMPATIBILITY.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['variable','documented_depth','measurement','biological_reference','classification','reason']); w.writeheader(); w.writerows([dict(zip(['variable','documented_depth','measurement','biological_reference','classification','reason'],r)) for r in depth])
print('tables built')
