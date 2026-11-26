#!/usr/bin/env python3
"""Supplemental raw-data tables for Sprint 4L.5 (read-only)."""
import csv, re
from collections import defaultdict, Counter
from pathlib import Path

RAW=Path('research/evidence/sprint_4l_mendota_biology_audit/acquisition/88.31/North_Temperate_Lakes_LTER_-_Phytoplankton_-_Madison_Lakes_Area__f2de15b2fff6ae962a04c150c0a1c510.dat')
OUT=Path('research/evidence/sprint_4l5_mendota_raw_biology_audit/tables')
rows=list(csv.DictReader(open(RAW,newline='',encoding='utf-8')))

# Mendota cyanobacteria annual coverage
g=defaultdict(lambda: {'dates':set(),'records':0,'cy_records':0,'bio':0.0,'cy_bio':0.0,'cy_samples':defaultdict(float),'sample_bio':defaultdict(float)})
for r in rows:
    if r['lakeid']!='ME': continue
    y=int(r['year4']); d=r['sampledate']; rec=g[y]
    rec['dates'].add(d); rec['records']+=1
    rec['bio']+=float(r['biovolume_conc']); rec['sample_bio'][d]+=float(r['biovolume_conc'])
    if r['division']=='Cyanophyta':
        rec['cy_records']+=1; rec['cy_bio']+=float(r['biovolume_conc']); rec['cy_samples'][d]+=float(r['biovolume_conc'])
out=[]
for y,rec in sorted(g.items()):
    shares=[100*rec['cy_samples'][d]/rec['sample_bio'][d] for d in rec['dates'] if rec['sample_bio'][d]>0]
    shares_sorted=sorted(shares)
    med=shares_sorted[len(shares_sorted)//2] if shares_sorted else ''
    out.append({'year':y,'records':rec['records'],'unique_dates':len(rec['dates']),
                'cyanophyta_records':rec['cy_records'],'total_biovolume_um3_per_ml':round(rec['bio'],3),
                'cyanophyta_biovolume_um3_per_ml':round(rec['cy_bio'],3),
                'cyanophyta_biovolume_share_pct':round(100*rec['cy_bio']/rec['bio'],3) if rec['bio'] else '',
                'median_sample_cyanophyta_share_pct':round(med,3) if med!='' else ''})
with (OUT/'MENDOTA_CYANOBACTERIA_COVERAGE.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

# Taxonomic resolution by year
tax=defaultdict(lambda: {'records':0,'taxa':set(),'genera':set(),'blank_taxa':0,'blank_genus':0,'unresolved':0,'cy':0})
for r in rows:
    y=int(r['year4']); x=tax[y]; x['records']+=1
    t=r['taxa_name'].strip(); gen=r['genus'].strip()
    if t: x['taxa'].add(t)
    else: x['blank_taxa']+=1
    if gen: x['genera'].add(gen)
    else: x['blank_genus']+=1
    if re.search(r'\b(sp\.?|spp\.?|var\.?|cf\.?|aff\.?|unidentified|unknown)\b',t,re.I): x['unresolved']+=1
    if r['division']=='Cyanophyta': x['cy']+=1
out=[]
for y,x in sorted(tax.items()):
    out.append({'year':y,'records':x['records'],'distinct_taxa':len(x['taxa']),'distinct_genera':len(x['genera']),
                'blank_taxa_records':x['blank_taxa'],'blank_genus_records':x['blank_genus'],
                'unresolved_or_infraspecific_records':x['unresolved'],'cyanophyta_records':x['cy']})
with (OUT/'TAXONOMIC_RESOLUTION_BY_YEAR.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

# Formatting variants: names that differ only by sp/sp./space/case
def norm(s):
    s=s.casefold().strip()
    s=re.sub(r'\bsp\s*\.?\s*(\d+)\b',r'sp\1',s)
    s=re.sub(r'[^a-z0-9]+',' ',s)
    s=re.sub(r'\s+',' ',s).strip()
    return s
variants=defaultdict(lambda: {'names':set(),'records':0})
for r in rows:
    t=r['taxa_name'].strip()
    if not t: continue
    k=norm(t); variants[k]['names'].add(t); variants[k]['records']+=1
out=[]
for k,v in variants.items():
    if len(v['names'])>1:
        out.append({'normalized_candidate':k,'variant_names':'|'.join(sorted(v['names'])),'total_records':v['records']})
with (OUT/'TAXONOMIC_FORMATTING_VARIANTS.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['normalized_candidate','variant_names','total_records']); w.writeheader(); w.writerows(out)

# Relative total anomalies
g=defaultdict(list)
for r in rows: g[(r['lakeid'],r['sampledate'],r['sta'],r['depth_range'])].append(r)
out=[]
for k,rs in g.items():
    s=sum(float(x['relative_total_biovolume']) for x in rs)
    if not (99 <= s <= 101):
        out.append({'lakeid':k[0],'sampledate':k[1],'sta':k[2],'depth_range':k[3],'n_rows':len(rs),
                    'sum_relative_total_biovolume':round(s,3),
                    'sum_biovolume_um3_per_ml':round(sum(float(x['biovolume_conc']) for x in rs),3),
                    'max_relative_value':round(max(float(x['relative_total_biovolume']) for x in rs),3)})
with (OUT/'RELATIVE_TOTAL_ANOMALIES.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

# Zero/inconsistency summary
checks={
 'biomass_zero_biovolume_positive':lambda r: float(r['biomass_conc'])==0 and float(r['biovolume_conc'])>0,
 'biovolume_zero_biomass_positive':lambda r: float(r['biovolume_conc'])==0 and float(r['biomass_conc'])>0,
 'cells_zero_biovolume_positive':lambda r: float(r['cells_per_ml'])==0 and float(r['biovolume_conc'])>0,
 'gald_zero':lambda r: float(r['gald'])==0,
 'relative_zero_biovolume_positive':lambda r: float(r['relative_total_biovolume'])==0 and float(r['biovolume_conc'])>0,
}
out=[]
for name,fn in checks.items():
    sub=[r for r in rows if fn(r)]
    out.append({'check':name,'records':len(sub),'lakes':','.join(sorted({r['lakeid'] for r in sub})),
                'min_value':min((float(r['biovolume_conc']) for r in sub),default=''),
                'max_value':max((float(r['biovolume_conc']) for r in sub),default='')})
with (OUT/'ZERO_INCONSISTENCY_SUMMARY.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['check','records','lakes','min_value','max_value']); w.writeheader(); w.writerows(out)

# Depth anomalies summary
anom=[]
for r in rows:
    if (r['lakeid']=='ME' and r['depth_range']!='0-8m') or (r['lakeid']=='MO' and r['depth_range']!='0-2m'):
        anom.append(r)
g=Counter((r['lakeid'],r['depth_range'],r['sampledate']) for r in anom)
out=[{'lakeid':k[0],'depth_range':k[1],'sampledate':k[2],'records':v} for k,v in sorted(g.items())]
with (OUT/'DEPTH_ANOMALY_ROWS.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['lakeid','depth_range','sampledate','records']); w.writeheader(); w.writerows(out)

# Division composition
div=defaultdict(lambda: {'records':0,'taxa':set(),'bio':0.0,'mass':0.0})
for r in rows:
    d=r['division']; x=div[d]; x['records']+=1; x['taxa'].add(r['taxa_name'].strip()); x['bio']+=float(r['biovolume_conc']); x['mass']+=float(r['biomass_conc'])
totbio=sum(x['bio'] for x in div.values()); totmass=sum(x['mass'] for x in div.values())
out=[]
for d,x in sorted(div.items(),key=lambda kv:kv[1]['bio'],reverse=True):
    out.append({'division':d,'records':x['records'],'distinct_taxa':len(x['taxa']),
                'biovolume_sum_um3_per_ml':round(x['bio'],3),'biovolume_share_pct':round(100*x['bio']/totbio,3),
                'biomass_sum_mg_per_l':round(x['mass'],3),'biomass_share_pct':round(100*x['mass']/totmass,3)})
with (OUT/'DIVISION_COMPOSITION.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
print('supplemental tables written')
