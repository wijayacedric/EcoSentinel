# Sprint 4L.6 source register

## Primary dataset and project evidence

1. **North Temperate Lakes LTER: Phytoplankton — Madison Lakes Area, ver. 31 (`knb-lter-ntl.88.31`)**. DOI: [10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9](https://doi.org/10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9). Local original CSV plus `metadata_88.31.xml`. Full raw file read; metadata field definitions and abstract inspected. Raw SHA-256 recorded in register.
2. **Sprint 4L.5 source evidence and scripts**, local project folder `research/evidence/sprint_4l5_mendota_raw_biology_audit/`. Executive report, raw/schema, biological distributions, sampling, taxonomic, duplicates, endpoints, depth, sources and three scripts inspected. Its output tables were not treated as input to independent reproduction.
3. **EcoSentinel `AGENTS.md`**, full project standard; inspected.

## External scientific and taxonomic literature

4. Hansen & Carey (2015), “Fish and Phytoplankton Exhibit Contrasting Temporal Species Abundance Patterns in a Dynamic North Temperate Lake,” PLOS ONE 10(2), e0115414, DOI [10.1371/journal.pone.0115414](https://doi.org/10.1371/journal.pone.0115414). Full methods/HTML inspected. Supports sampling method, community turnover and detection caveats.
5. North Temperate Lakes LTER, [Research Protocols](https://lter.limnology.wisc.edu/protocols/), inspected. The page reports routine biweekly summer/monthly non-summer sampling, identifies phytoplankton biovolume for ME/MO, and states protocols are being revised.
6. North Temperate Lakes LTER, [Archived protocols PDF (2023)](https://lter.limnology.wisc.edu/wp-content/uploads/sites/2029/2023/06/NTLProtocols_Archived2023.pdf), relevant sections inspected. Includes 0–8m Mendota integrated phytoplankton sampling and a PhycoTech appendix with dimensions, counting and approximate every-tenth-sample recount QA/QC. It is not proven to govern all historical 88.31 observations.
7. Wacklin, Hoffmann & Komárek (2009), “Nomenclatural validation of the genetically revised cyanobacterial genus Dolichospermum,” Fottea 9(1):59–64, DOI [10.5507/fot.2009.005](https://doi.org/10.5507/fot.2009.005). Search/bibliographic record inspected; supports genus transfer framework, not Mendota row identities.
8. Németh & Buczkó (2024), “Cyanobacteria of protected areas in Hungary until 2004,” Studia Botanica Hungarica 55(1):5–140. Full PDF inspected at [real.mtak.hu/221218](https://real.mtak.hu/221218/1/StudiaBotHung_2024_Vol_55_1_5.pdf). Taxonomic list illustrates updated/uncertain names, but geographic scope is Hungary.
9. Komárek et al. (2013), polyphasic evaluation of Limnoraphis, Fottea 13:39–52, DOI [10.5507/fot.2013.004](https://doi.org/10.5507/fot.2013.004). Full article found via university-hosted PDF; supports Limnoraphis/Lyngbya distinction.
10. LPSN, *Pseudanabaena mucicola* page, [lpsn.dsmz.de/species/pseudanabaena-mucicola](https://lpsn.dsmz.de/species/pseudanabaena-mucicola), inspected. Records name validity/status disagreement; LPSN nomenclatural scope should not be conflated with algal usage databases.
11. National Museum of Nature and Science, Japan, Freshwater Planktonic Blue-Green Algae Database, *Umezakia ovalisporum*, [kahaku.go.jp](https://www.kahaku.go.jp/research/db/botany/microalgae/aoko/database/0-8-10930.html), inspected. Lists *Aphanizomenon ovalisporum* basionym and *Chrysosporum ovalisporum* synonym under Umezakia name.
12. McGregor et al. (2023) publication details are cited by the museum database for *Umezakia ovalisporum*; full article was not inspected independently, so the museum database—not the primary article—is the direct source used here.
13. Beal et al., “Development of a sub-seasonal cyanobacteria prediction model by leveraging local and global scale predictors,” *Ecological Informatics*; [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S156898832100130X). Search-indexed full-text result inspected; direct article page returned HTTP 403. It describes a two-month July–August cyanobacteria abundance forecast, not a daily bloom-onset detector.
14. Beal et al. (2022), “Variability of summer cyanobacteria abundance: can season-ahead forecasts improve beach management?”, DOI [10.1080/10402381.2022.2084799](https://doi.org/10.1080/10402381.2022.2084799). Search-indexed record inspected; publisher page returned HTTP 403.
15. O’Brien et al. (2023), “Early warning signals have limited applicability to empirical lake data,” *Nature Communications* 14:7942, DOI [10.1038/s41467-023-43744-8](https://doi.org/10.1038/s41467-023-43744-8). Full PDF inspected. Table 2 lists a monthly Mendota series at 0–20m, May 1999–Nov 2018; methods/results compare univariate and multivariate signals and show preprocessing/resolution sensitivity. This is not the exact 88.31 0–8m observation series.
16. Existing project 4L.5 bibliography also points to studies of cyanobacterial forecasting, phycocyanin and Mendota high-frequency records; these were not all re-opened in this sprint. See scope limitation in search log.

## Source-use rule

External citations support protocol/nomenclatural context, not claims about original sample correctness. Claims tied to actual row values come from the locally hashed raw data. Claims tied to variable meaning come from package EML. Conflicting taxonomic records are reported, not resolved by selecting a convenient authority.
