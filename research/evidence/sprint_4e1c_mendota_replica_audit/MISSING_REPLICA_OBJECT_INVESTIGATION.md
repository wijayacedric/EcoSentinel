# Missing Replica Object Investigation (Sprint 4E.1C)

**Date:** 2026-11-23T07:05:41.270436+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Object

- **PID:** `https://pasta.lternet.edu/package/data/eml/knb-lter-ntl/130/29/c7538c460f8d0cbd90ec2892b8ce3025`
- **Package:** knb-lter-ntl.130.29 (DOI 10.6073/PASTA/8CEFF296AD68FA8DA6787076E0A5D992)
- **EML entity:** North Temperate Lakes LTER - High Resolution Water Temperature - Lake Mendota - 2015
- **Temporal coverage (EML):** 2015-06-25 to 2015-09-01
- **Variables (EML):** sampledate, sampletime, depth, wtemp, flag_wtemp

## Checks performed (legitimate, no auth bypass)

| Check | Result |
|---|---|
| CN sysmeta `/cn/v2/meta/<pid>` | 404 NotFound (no system metadata) |
| CN resolve `/cn/v2/resolve/<pid>` | 404 NotFound |
| CN Solr by id/checksum fragment | numFound 0 |
| ORE membership | Present in 130.29 ORE |
| EML distribution URL | Present in 130.29 EML |

## Assessment

- **Genuine missing CN replica/index entry:** Likely yes on CN (not found by sysmeta/resolve/solr). 
- **Exists on another legitimate DataONE node?** Unknown. Authoritative MN is urn:node:LTER (gmn.lternet.edu/PASTA). Direct MN/PASTA access was previously blocked in this environment (403/login) and no authorised EDI API key is available. I did not bypass access controls.
- **Accessible alternative public distribution?** Not identified through CN. PASTA data URL is known from EML but PASTA requires auth.
- **Impact on essential variables/temporal coverage:** **Material but bounded.** The missing object covers **2015-06-25 to 2015-09-01 high-resolution water temperature** for Lake Mendota only. Other years 2006-2014, 2016-2019 are present in ORE/EML; daily/hourly aggregated files also exist in package. If 2015 HR data is needed, this gap must be resolved through authorised EDI/DataONE access.

## Conclusion

Unresolved for complete 130.29 replica. Not a reason to discard the whole package, but it prevents claiming complete verified public CN replica for 130.29.
