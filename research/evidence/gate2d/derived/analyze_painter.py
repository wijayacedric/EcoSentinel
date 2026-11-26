import csv, json, math, os, statistics
from collections import defaultdict, Counter
base='research/evidence/gate2d/painter_2022_borealis'
outdir='research/evidence/gate2d/derived'
os.makedirs(outdir, exist_ok=True)

def read_csv(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

def ffloat(x):
    try:
        if x is None: return None
        x=x.strip()
        if x=='' or x.lower() in {'na','nan','null'}: return None
        return float(x)
    except Exception:
        return None

summary={}
for year, fn in [(2018,'BP_PhytoTax_2018_KP.csv'), (2019,'BP_PhytoTax_2019_KP.csv')]:
    rows=read_csv(os.path.join(base,fn))
    by_doy=defaultdict(list)
    for r in rows: by_doy[int(float(r['DOY']))].append(r)
    dates=[]
    for doy in sorted(by_doy):
        rs=by_doy[doy]
        total=sum(ffloat(r.get('Biomass_mg_m3')) or 0 for r in rs)
        cyano=sum(ffloat(r.get('Biomass_mg_m3')) or 0 for r in rs if (r.get('Group') or '').strip().lower()=='cyanophyte')
        taxa=len(set((r.get('Species_Name') or '').strip() for r in rs))
        cyano_taxa=len(set((r.get('Species_Name') or '').strip() for r in rs if (r.get('Group') or '').strip().lower()=='cyanophyte'))
        reps=sorted(set((r.get('REP') or '').strip() for r in rs if 'REP' in r))
        sample_ids=sorted(set((r.get('Sample_ID') or '').strip() for r in rs if r.get('Sample_ID')))
        locs=sorted(set((r.get('Location') or '').strip() for r in rs))
        depths=sorted(set((r.get('Depth') or '').strip() for r in rs))
        dates.append({
            'year':year,'DOY':doy,'n_rows':len(rs),'n_taxa':taxa,'n_cyano_taxa':cyano_taxa,
            'total_biomass_mg_m3':round(total,3),'cyano_biomass_mg_m3':round(cyano,3),
            'cyano_prop':round((cyano/total) if total else 0,4),
            'sample_ids':sample_ids,'reps':reps,'locations':locs,'depths':depths
        })
    # gaps
    gaps=[]
    for a,b in zip(dates,dates[1:]): gaps.append(b['DOY']-a['DOY'])
    summary[str(year)]={'n_dates':len(dates),'doys':[d['DOY'] for d in dates],'gaps_days':gaps,
                        'min_gap':min(gaps) if gaps else None,'max_gap':max(gaps) if gaps else None,
                        'median_gap':statistics.median(gaps) if gaps else None,'dates':dates}

# 2019-07-17 detail
rows19=read_csv(os.path.join(base,'BP_PhytoTax_2019_KP.csv'))
d198=[r for r in rows19 if int(float(r['DOY']))==198]
summary['anomaly_2019_07_17']={
    'doy':198,'n_rows':len(d198),
    'sample_fields':sorted(d198[0].keys()) if d198 else [],
    'rows':[{
        'Sample_ID':r.get('Sample_ID'),'Location':r.get('Location'),'Depth':r.get('Depth'),'DOY':r.get('DOY'),'REP':r.get('REP'),
        'Species_Code':r.get('Species_Code'),'Species_Name':r.get('Species_Name'),'Cell_Density_L':r.get('Cell_Density_L'),
        'Biomass_mg_m3':r.get('Biomass_mg_m3'),'Group':r.get('Group'),'Phylum':r.get('Phylum'),'name_code':r.get('name_code')
    } for r in d198]
}

# compare group biomass files for 2019 DOY 198
for year, fn in [(2018,'BP_GroupsBiomass_2018_KP.csv'), (2019,'BP_GroupsBiomass_2019_KP.csv')]:
    g=read_csv(os.path.join(base,fn))
    key=str(year)+'_group_198'
    summary[key]=[r for r in g if str(int(float(r['DOY'])))=='198']

# toxins 2019 around 07-17 (messy encoding/format - read as raw text only)
with open(os.path.join(base,'BP_2019_toxins_0.8.csv'), encoding='latin-1', errors='replace') as f:
    tox19_lines=f.readlines()
summary['tox_2019_lines_with_2019-07-17']=[ln[:300] for ln in tox19_lines if '2019-07-17' in ln or '17/07/2019' in ln][:10]
summary['tox_2019_total_lines']=len(tox19_lines)
with open(os.path.join(base,'BP_2018_toxins_0.8m.csv'), encoding='latin-1', errors='replace') as f:
    tox18_lines=f.readlines()
summary['tox_2018_total_lines']=len(tox18_lines)
summary['tox_2018_lines_with_2018_dates_sample']=[ln[:200] for ln in tox18_lines[:5]]

# nutrients file
nut=read_csv(os.path.join(base,'Nutrients_Biomass_BP_clean.csv'))
summary['nutrients_rows']=len(nut)
summary['nutrients_fields']=list(nut[0].keys()) if nut else []
summary['nutrients_preview']=nut[:3]

with open(os.path.join(outdir,'painter_summary.json'),'w') as f:
    json.dump(summary,f,indent=2)
print('wrote', os.path.join(outdir,'painter_summary.json'))
for y in ['2018','2019']:
    d=summary[y]
    print(y,'n_dates',d['n_dates'],'gaps',d['min_gap'],d['median_gap'],d['max_gap'])
