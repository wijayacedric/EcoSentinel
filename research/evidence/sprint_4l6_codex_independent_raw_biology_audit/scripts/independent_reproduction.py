#!/usr/bin/env python3
"""Independent, read-only reproduction of selected Sprint 4L.5 Mendota findings.

Uses Python's standard library only. Reads the original EDI entity and EML,
then writes results only below this Sprint 4L.6 directory. It never changes
Sprint 4L.5 outputs or the source data.
"""
from __future__ import annotations
import csv, hashlib, json, math, re, statistics
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RAW = ROOT / "research/evidence/sprint_4l_mendota_biology_audit/acquisition/88.31/North_Temperate_Lakes_LTER_-_Phytoplankton_-_Madison_Lakes_Area__f2de15b2fff6ae962a04c150c0a1c510.dat"
EML = RAW.with_name("metadata_88.31.xml")
OUT = Path(__file__).resolve().parents[1] / "reproduction"
EXPECTED = ["lakeid","year4","sampledate","sta","depth_range","division","taxa_name","gald","cells_per_nu","nu_per_ml","cells_per_ml","biovolume_conc","biomass_conc","relative_total_biovolume","genus"]
NUMERIC = EXPECTED[7:14]
LAKES = ["ME","MO","WI","FI"]

def digest(p, alg):
    h=hashlib.new(alg)
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
def quantile(xs,p):
    ys=sorted(xs)
    if not ys: return None
    x=(len(ys)-1)*p; lo=math.floor(x); hi=math.ceil(x)
    return ys[lo] if lo==hi else ys[lo]*(hi-x)+ys[hi]*(x-lo)
def group_by(rows, fn):
    d=defaultdict(list)
    for r in rows: d[fn(r)].append(r)
    return d

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    raw=RAW.read_bytes()
    with RAW.open('r',encoding='utf-8',newline='') as f:
        reader=csv.DictReader(f)
        header=reader.fieldnames
        rows=list(reader)
    lengths=Counter()
    # Independently inspect CSV record arity using csv.reader (rather than DictReader only).
    with RAW.open('r',encoding='utf-8',newline='') as f:
        rr=csv.reader(f)
        hdr=next(rr)
        for rec in rr: lengths[len(rec)]+=1
    dates={r['lakeid']:set() for r in rows}
    date_rows=defaultdict(list)
    year_mismatch=[]
    depth=Counter(); station=Counter(); division=Counter(); taxa_all=set(); genus_all=set(); taxa_nonblank=set(); genus_nonblank=set()
    blank_taxa=blank_genus=0; trailing=double_space=0; genus_mismatch=0; unresolved=set(); unresolved_records=0
    bylake=Counter(); vals={v:[] for v in NUMERIC}; val_lake={v:defaultdict(list) for v in NUMERIC}; zeros=Counter()
    exact=Counter(); taxon_key=defaultdict(list); raw_taxon_key=defaultdict(list)
    for r in rows:
        lake=r['lakeid']; d=datetime.strptime(r['sampledate'],'%Y-%m-%d').date()
        dates[lake].add(d); date_rows[lake,d].append(r); bylake[lake]+=1
        if int(r['year4'])!=d.year: year_mismatch.append(r)
        depth[lake,r['depth_range']]+=1; station[lake,r['sta']]+=1; division[r['division']]+=1
        t=r['taxa_name'].strip(); g=r['genus'].strip()
        taxa_all.add(t); genus_all.add(g)
        if not t: blank_taxa+=1
        else: taxa_nonblank.add(t)
        if not g: blank_genus+=1
        else: genus_nonblank.add(g)
        if r['taxa_name'] != r['taxa_name'].rstrip(): trailing+=1
        if '  ' in r['taxa_name']: double_space+=1
        first=t.split()[0] if t else ''
        if g and first and first.casefold()!=g.casefold(): genus_mismatch+=1
        if re.search(r'\b(sp\.?|spp\.?|var\.?|cf\.?|aff\.?|unidentified|unknown)\b',t,re.I):
            unresolved.add(t); unresolved_records+=1
        for v in NUMERIC:
            x=float(r[v]); vals[v].append(x); val_lake[v][lake].append(x)
            if x==0: zeros[v,lake]+=1
        exact[tuple(r[k] for k in EXPECTED)]+=1
        key=(lake,d,r['sta'],r['depth_range'],t)
        taxon_key[key].append(r)
        raw_taxon_key[(lake,d,r['sta'],r['depth_range'],r['taxa_name'])].append(r)
    all_dates=sorted(set(d for ds in dates.values() for d in ds))
    gap_stats={}
    for lake in LAKES:
        ds=sorted(dates.get(lake,set())); gaps=[(ds[i+1]-ds[i]).days for i in range(len(ds)-1)]
        gap_stats[lake]={'date_count':len(ds),'first':ds[0].isoformat() if ds else None,'last':ds[-1].isoformat() if ds else None,
                         'n_gaps':len(gaps),'min':min(gaps) if gaps else None,'median':statistics.median(gaps) if gaps else None,
                         'mean':statistics.mean(gaps) if gaps else None,'max':max(gaps) if gaps else None,
                         'gaps_ge30':sum(x>=30 for x in gaps),'gaps_ge60':sum(x>=60 for x in gaps),'gaps_ge90':sum(x>=90 for x in gaps),
                         'gaps_ge365':sum(x>=365 for x in gaps)}
    annual={}
    byyear=defaultdict(set)
    for lake,ds in dates.items():
        for d in ds: byyear[lake,d.year].add(d)
    for y in sorted({y for _,y in byyear}):
        ds=sorted(byyear['ME',y]); gaps=[(ds[i+1]-ds[i]).days for i in range(len(ds)-1)]
        annual[str(y)]={'dates':len(ds),'first':ds[0].isoformat() if ds else None,'last':ds[-1].isoformat() if ds else None,
                        'months':sorted({x.month for x in ds}),'max_gap':max(gaps) if gaps else None}
    qstats={}
    for v,xs in vals.items():
        qstats[v]={'n':len(xs),'missing':sum(not r[v].strip() for r in rows),'zeros':sum(x==0 for x in xs),'negatives':sum(x<0 for x in xs),
                    'min':min(xs),'p01':quantile(xs,.01),'p25':quantile(xs,.25),'median':statistics.median(xs),'p75':quantile(xs,.75),
                    'p95':quantile(xs,.95),'p99':quantile(xs,.99),'max':max(xs),'mean':statistics.mean(xs)}
    # Arithmetic checks
    cell_errors=[]; biomass_abs=[]; biomass_rel=[]; biomass_zero_bio=[]
    for r in rows:
        cn=float(r['cells_per_nu'])*float(r['nu_per_ml']); c=float(r['cells_per_ml'])
        if cn: cell_errors.append(abs(c-cn)/abs(cn))
        b=float(r['biovolume_conc']); m=float(r['biomass_conc']); expected=b*1e-6
        if b>0:
            biomass_abs.append(abs(m-expected)); biomass_rel.append(abs(m-expected)/expected if expected else 0)
        if m==0 and b>0: biomass_zero_bio.append(r)
    # Relative bvol arithmetic and alternative grouping definitions.
    group_defs={
        'lake_date_station_depth':lambda r:(r['lakeid'],r['sampledate'],r['sta'],r['depth_range']),
        'lake_date_depth':lambda r:(r['lakeid'],r['sampledate'],r['depth_range']),
        'lake_date_station':lambda r:(r['lakeid'],r['sampledate'],r['sta']),
        'lake_date':lambda r:(r['lakeid'],r['sampledate'])}
    rel_group_stats={}; rel_detail={}
    for name,fn in group_defs.items():
        gs=group_by(rows,fn); sums=[]
        for k,rs in gs.items(): sums.append(sum(float(r['relative_total_biovolume']) for r in rs))
        rel_group_stats[name]={'group_count':len(gs),'n_near_100_99_101':sum(99<=x<=101 for x in sums),
                               'n_approx_200_199_201':sum(199<=x<=201 for x in sums),'n_zero':sum(x==0 for x in sums),
                               'n_other':sum(not(99<=x<=101 or 199<=x<=201 or x==0) for x in sums),
                               'min_sum':min(sums),'max_sum':max(sums)}
        if name=='lake_date_station_depth':
            for k,rs in gs.items():
                s=sum(float(r['relative_total_biovolume']) for r in rs)
                if not(99<=s<=101):
                    rel_detail['|'.join(k)]={'n':len(rs),'sum_relative':s,'sum_biovolume':sum(float(r['biovolume_conc']) for r in rs),
                                              'max_relative':max(float(r['relative_total_biovolume']) for r in rs),
                                              'max_taxa':max(rs,key=lambda r:float(r['relative_total_biovolume']))['taxa_name']}
    # duplicate concepts
    exact_dups={k:n for k,n in exact.items() if n>1}
    key_groups={k:rs for k,rs in taxon_key.items() if len(rs)>1}
    raw_groups={k:rs for k,rs in raw_taxon_key.items() if len(rs)>1}
    samekey={'cleaned_taxon':{'groups':len(key_groups),'rows':sum(len(v) for v in key_groups.values()),'excess_rows':sum(len(v)-1 for v in key_groups.values()),
                              'groups_distinct_cells':sum(len({r['cells_per_ml'] for r in v})>1 for v in key_groups.values()),
                              'groups_distinct_biovolume':sum(len({r['biovolume_conc'] for r in v})>1 for v in key_groups.values())},
             'raw_taxon':{'groups':len(raw_groups),'rows':sum(len(v) for v in raw_groups.values()),'excess_rows':sum(len(v)-1 for v in raw_groups.values())},
             'exact_rows':sum(n for n in exact_dups.values()),'exact_duplicate_groups':len(exact_dups),
             'exact_duplicate_excess_rows':sum(n-1 for n in exact_dups.values()),'exact_duplicate_dates':sorted({k[2] for k in exact_dups})}
    # Biology anomalies
    zero_biomass_rows=[{'lakeid':r['lakeid'],'sampledate':r['sampledate'],'taxa_name':r['taxa_name'],'division':r['division'],
                        'biovolume':float(r['biovolume_conc']),'biomass':float(r['biomass_conc']),'expected_biomass':float(r['biovolume_conc'])*1e-6}
                       for r in biomass_zero_bio]
    cell_zero=[r for r in rows if float(r['cells_per_ml'])==0 and float(r['biovolume_conc'])>0]
    # Grouped proportions of biovolume; aggregate by exact key and inspect taxon records.
    coel=[r for r in rows if r['lakeid']=='ME' and r['sampledate']=='2011-07-25' and 'Coelastrum reticulatum' in r['taxa_name']]
    anomaly_key=('ME','2011-07-25','1','0-8m')
    anomaly_group=group_by(rows,group_defs['lake_date_station_depth'])[anomaly_key]
    mismatch=[]
    for r in rows:
        t=r['taxa_name'].strip(); g=r['genus'].strip(); first=t.split()[0] if t else ''
        if g and first and first.casefold()!=g.casefold(): mismatch.append(r)
    pre={r['taxa_name'].strip() for r in rows if r['sampledate']<'2013-02-01'}
    post={r['taxa_name'].strip() for r in rows if r['sampledate']>='2013-02-01'}
    mstats={
        'raw_bytes':len(raw),'md5':digest(RAW,'md5'),'sha256':digest(RAW,'sha256'),'header':header,'header_matches':header==EXPECTED,
        'row_count':len(rows),'row_arity_counts':{str(k):v for k,v in sorted(lengths.items())},'year_date_mismatches':len(year_mismatch),
        'overall_dates':len(all_dates),'overall_first':all_dates[0].isoformat(),'overall_last':all_dates[-1].isoformat(),
        'lake_records':dict(Counter(r['lakeid'] for r in rows)),'lake_unique_dates':{k:len(v) for k,v in dates.items()},'gap_stats':gap_stats,'ME_annual':annual,
        'depth_counts':{f'{k[0]}|{k[1]}':n for k,n in depth.items()},'station_counts':{f'{k[0]}|{k[1]}':n for k,n in station.items()},
        'blank_taxa_records':blank_taxa,'blank_genus_records':blank_genus,'distinct_taxa_with_blank':len(taxa_all),'distinct_nonblank_taxa':len(taxa_nonblank),
        'distinct_genera_with_blank':len(genus_all),'distinct_nonblank_genera':len(genus_nonblank),'division_counts':dict(division),
        'trailing_space_rows':trailing,'double_space_rows':double_space,'nonblank_genus_first_token_mismatches':genus_mismatch,
        'unresolved_unique_names_regex':len(unresolved),'unresolved_records_regex':unresolved_records,'pre2013_names_with_blank':len(pre),'post2013_names_with_blank':len(post),
        'only_pre2013':len(pre-post),'only_post2013':len(post-pre),'numeric_quality':qstats,
        'cells_formula_n_nonzero_denominator':len(cell_errors),'cells_formula_max_relative_error':max(cell_errors),
        'biomass_formula_bvol_times_1e-6_n_positive_bvol':len(biomass_rel),'biomass_formula_abs_error_max':max(biomass_abs),
        'biomass_formula_rel_error_median':statistics.median(biomass_rel),'biomass_zero_positive_bvol_count':len(zero_biomass_rows),
        'biomass_zero_positive_bvol_minmax':[min(x['biovolume'] for x in zero_biomass_rows),max(x['biovolume'] for x in zero_biomass_rows)],
        'zero_biomass_values':zero_biomass_rows,'zero_cells_positive_bvol_count':len(cell_zero),
        'relative_group_stats':rel_group_stats,'relative_group_anomalies':rel_detail,
        'same_taxon_groups':samekey,'Coelastrum_row':coel,'Coelastrum_group_n':len(anomaly_group),
        'Coelastrum_group_biovolume_sum':sum(float(r['biovolume_conc']) for r in anomaly_group),
        'Coelastrum_group_relative_sum':sum(float(r['relative_total_biovolume']) for r in anomaly_group),
        'Coelastrum_group_rows':[{k:r[k] for k in EXPECTED} for r in anomaly_group],
        'genus_mismatch_examples':[{k:r[k] for k in ['sampledate','taxa_name','genus','division']} for r in mismatch[:10]],
    }
    (OUT/'INDEPENDENT_REPRODUCTION_SUMMARY.json').write_text(json.dumps(mstats,indent=2,ensure_ascii=False),encoding='utf-8')
    (OUT/'ANNUAL_ME_SAMPLE_DATES.csv').write_text('year,unique_dates,first_date,last_date,months,max_gap_days\n'+''.join(f"{y},{a['dates']},{a['first']},{a['last']},\"{'|'.join(map(str,a['months']))}\",{a['max_gap']}\n" for y,a in annual.items()),encoding='utf-8')
    with (OUT/'ZERO_BIOMASS_CASES.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(zero_biomass_rows[0].keys()));w.writeheader();w.writerows(zero_biomass_rows)
    with (OUT/'RELATIVE_GROUP_ANOMALIES.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=['group_key','n','sum_relative','sum_biovolume','max_relative','max_taxa']);w.writeheader()
        for k,v in rel_detail.items():w.writerow({'group_key':k,**v})
    # Preserve complete row context for the anomalous sample and auditable repeated-key inventory.
    with (OUT/'COELASTRUM_SAMPLE_2011-07-25.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=EXPECTED);w.writeheader();w.writerows(anomaly_group)
    with (OUT/'REPEATED_TAXON_KEY_GROUPS.csv').open('w',newline='',encoding='utf-8') as f:
        fields=['lakeid','sampledate','sta','depth_range','taxa_name_clean','n_records','n_distinct_cells_per_ml','n_distinct_biovolume_conc','exact_duplicate_rows']
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for key,rs in sorted(key_groups.items(),key=lambda kv:tuple(map(str,kv[0]))):
            w.writerow({'lakeid':key[0],'sampledate':key[1].isoformat(),'sta':key[2],'depth_range':key[3],
                        'taxa_name_clean':key[4],'n_records':len(rs),
                        'n_distinct_cells_per_ml':len({x['cells_per_ml'] for x in rs}),
                        'n_distinct_biovolume_conc':len({x['biovolume_conc'] for x in rs}),
                        'exact_duplicate_rows':sum(max(0,n-1) for n in Counter(tuple(x[k] for k in EXPECTED) for x in rs).values())})
    print(json.dumps({k:mstats[k] for k in ['raw_bytes','sha256','row_count','row_arity_counts','lake_records','lake_unique_dates','gap_stats','distinct_taxa_with_blank','distinct_nonblank_taxa','distinct_genera_with_blank','distinct_nonblank_genera','nonblank_genus_first_token_mismatches','relative_group_stats','same_taxon_groups','biomass_zero_positive_bvol_count','zero_cells_positive_bvol_count','Coelastrum_row']},indent=2))
if __name__=='__main__': main()
