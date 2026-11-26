# Stage 1 Competition Suitability Assessment

**Sprint:** 4L.19  
**Question:** Is the narrowed Stage 1 study suitable for a SciFest@College 2027 entry, assuming the scientific and governance conditions are met?  
**Status:** Assessment only. **D-14 remains OUTSTANDING — NOT APPROVED.**  
**Important:** This is not a rules-compliance determination. Official rules must be checked for the specific venue and year, and a written licence/competition review is still required.

---

## 1. What the official rules actually say

The following points were checked against the SciFest@College 2027 entry page and the provisional 2027 student rules PDF on 2026-11-25.

### 1.1 Eligibility and entry

- Entrants must be second-level students **born after 1 May 2008**, attending school or being home-schooled in Ireland (including Northern Ireland).
- A student may enter **one project**; a school may enter many.
- Projects may be **individual** or **group** (maximum 3 students).
- Categories include **Life Sciences**, **Physical Sciences** and **Technology**.
- A student may not enter the same project in more than one venue in a given year.
- Entry forms for 2027 are not yet available; the closing date for SciFest@College 2027 is **Thursday 11 March 2027**.

### 1.2 What must be brought on the day

- A **Project Report Book**.
- A **Visual Display**.
- Display board size varies by venue; the venue informs entrants.
- Brand names/sponsors should be avoided on the display where possible; references belong in the report book.

### 1.3 Conduct and acknowledgement

- **Plagiarism is strictly prohibited.**
- Work carried out in an institution other than the school, or under supervision other than the teacher’s, must be acknowledged in the report book, including the supervisor’s name, contact details and institution.
- A Participation Consent and Media Release form must be signed; a parent/guardian must also sign if the entrant is under 18.
- SciFest may use photographs/video/sound recordings of participants, including the student’s name, project title, prize information and school, in print and online media.

### 1.4 What the rules do **not** say

- No public judging rubric or marking scheme was verified in this sprint. Do not invent one.
- The rules do not state that a project must be novel, must produce a positive result, or must use a particular statistical method.
- The rules do not grant an automatic educational exception to dataset licences.
- The rules do not resolve whether a CC BY-NC-SA 4.0 dataset can be adapted and displayed in the specific competition context.

**Consequence:** the competition assessment below distinguishes **official entry requirements** from **general scientific-presentation judgement**. It does not claim to apply an official judging rubric.

---

## 2. Scientific validity

| Criterion | Assessment | Reason |
|---|---|---|
| Clear question | **Moderate** | The narrowed question is clear, but it is a measurement audit rather than an ecological hypothesis |
| Appropriate design | **Conditional** | The same-date rank association is defensible only as exploratory; the current protocol QC rules must be revised |
| Independent endpoint | **Yes, with caveats** | Microscopy is independent of the sensor, but the biomass endpoint is derived and the Mendota depth mismatch is serious |
| Appropriate statistics | **Conditional** | Spearman rho is defensible descriptively; dependence, seasonality and multiplicity must be acknowledged |
| Honest limitations | **Strong** | The project has an unusually explicit limitations and governance trail |
| Negative-result acceptance | **Strong** | The protocol explicitly allows weak/absent associations |
| Overclaiming risk | **High if not controlled** | The temptation to call it validation/early warning is real; the claims matrix prohibits it |

**Scientific validity verdict:** **Conditionally valid as an exploratory measurement audit.** It is not valid as a validation, calibration, prediction or early-warning study.

---

## 3. Originality

The detailed prior-art review is in `STAGE1_ORIGINALITY_AND_PRIOR_ART_REVIEW.md`. In summary:

- Phycocyanin fluorescence vs cyanobacteria biomass is well studied (Brient 2008; Loisa 2015; Kong 2013; Hodges 2017).
- Buffalo Pound sensor chlorophyll vs bloom biology is directly addressed by Painter et al. (2022), who found that the autumn *Planktothrix* bloom was not detected by sensor chlorophyll.
- Spearman correlation and two-lake comparisons are not novel methods.
- The modest contribution is the **pre-specified non-equivalence audit** and the **honest negative-result framing**.

**Originality verdict:** **Low to moderate.** A competition judge may see the project as a careful data audit rather than a new discovery. That is not fatal, but it limits the “innovation” narrative.

---

## 4. Technical sophistication

| Element | Level | Comment |
|---|---|---|
| Data provenance and version control | **High for a school project** | Two repositories, licences, DOIs, hashes, decision records |
| QC flag interpretation | **High** | The project correctly refuses to treat flags as simple remove/keep rules |
| Sensor understanding | **Moderate–high** | RFU vs concentration, calibration, fouling, range limits are addressed |
| Statistical method | **Low–moderate** | Spearman rho is simple; the sophistication is in the caveats, not the computation |
| Coding/analysis | **Not yet demonstrated** | Analysis is not authorised; no code has been run |
| Reproducibility | **High** | Integrity registers and manifests are strong |

**Technical sophistication verdict:** **Moderate.** The provenance/QC work is sophisticated; the statistical analysis is deliberately simple. A judge who values methodological care will see depth; a judge who values advanced modelling may see limited technical ambition.

---

## 5. Presentation potential

### Strengths

- A clear visual story: “Can a cheap fluorescence sensor tell you what the microscope sees?”
- Strong graphics: sensor vs microscopy scatterplots (if authorised), depth schematic, flag-handling flow diagram, decision tree.
- A honest “what we can and cannot conclude” panel.
- A reproducibility/integrity panel that is unusual and credible.
- A negative-result narrative: “the sensor is useful, but not a substitute for microscopy; here is where it fails.”

### Risks

- Too much governance/QC detail can overwhelm a short presentation.
- The audience may not understand RFU, biovolume, Spearman rho or detection-conditioned populations without careful visual explanation.
- A null/weak result can look like “nothing happened” unless the question and the implication are clear.
- The two-lake asymmetry may confuse the story; a Mendota-core narrative may be clearer.
- The project must not look like a data-management exercise rather than a scientific question.

**Presentation verdict:** **Potentially strong if simplified around one question and one result.** The current evidence trail is an asset for the report book, not for the poster.

---

## 6. Feasibility

| Requirement | Assessment | Comment |
|---|---|---|
| Data access | **Already local** | No new acquisition needed |
| Custodian response | **Uncertain** | P3/P4 depend on it; Mendota-only does not |
| Analysis skills | **Moderate** | Spearman and descriptive summaries are feasible; QC wrangling is the hard part |
| Time | **Tight but feasible** | Review, custody, licence and protocol revision could take weeks |
| Supervision | **Required** | External supervision must be acknowledged under SciFest rules |
| Licence/competition review | **Unresolved** | D-14 remains outstanding |
| Risk of no result | **High** | A weak/absent association is a legitimate but less exciting outcome |

**Feasibility verdict:** **Feasible for a Mendota-core study; conditional for a two-lake study.** The Buffalo Pound dependency is the main schedule risk.

---

## 7. Student contribution

SciFest prohibits plagiarism and requires acknowledgement of external supervision. The project must be able to show:

- what the student did (question, design, QC review, analysis, interpretation, writing);
- what was done by teachers/supervisors;
- what was done by the dataset authors (data collection and processing);
- what was done by any AI/software tool;
- how the student verified sources and avoided copying.

The current project has a strong decision/evidence trail, which helps demonstrate independent work. But the trail is also complex; the student must be able to explain it orally without reading from documents.

**Student-contribution verdict:** **Potentially strong if documented plainly.** Do not present the dataset authors’ work as the student’s own, and do not present the AI-assisted documentation as independent scientific discovery.

---

## 8. Competition suitability

| Dimension | Rating | Reason |
|---|---|---|
| Scientific validity | **Conditional** | Exploratory audit only; protocol revision needed |
| Originality | **Low–moderate** | Established sensor–biomass literature; modest framing contribution |
| Technical sophistication | **Moderate** | Strong provenance/QC; simple statistics |
| Presentation potential | **Moderate–high** | Clear question and graphics possible; governance detail must be simplified |
| Feasibility | **Moderate** | Mendota-core feasible; two-lake depends on custodian |
| Student contribution | **Potentially strong** | Good trail, but must be explained plainly |
| Rules compliance | **Unresolved** | D-14; licence/competition review needed |

**Overall:** **Suitable as a careful exploratory measurement audit, not as a novel sensor-validation or early-warning project.** It could be a credible Life Sciences entry if the student frames it as “what a fluorescence sensor can and cannot tell us about cyanobacteria, and why the microscope still matters.” It is less suitable if the entry depends on a “new discovery” or “AI prediction” narrative.

---

## 9. Licence and competition issues

The two datasets have different licences:

- Buffalo Pound buoy data: **CC BY 4.0** — attribution required; commercial use permitted.
- Buffalo Pound biological data: **CC BY-NC-SA 4.0** — attribution, non-commercial use, share-alike.
- Mendota NTL-LTER data: check the specific dataset licence/terms before display; do not assume.

The competition context is non-commercial, but that does not automatically resolve:

- whether a derived analysis or poster is an “adaptation” under CC BY-NC-SA 4.0;
- whether ShareAlike attaches to the poster/report or only to the dataset;
- whether SciFest’s media release and publication of project content interact with the dataset licence;
- whether the Mendota data have their own attribution/redistribution terms.

**D-14 remains OUTSTANDING — NOT APPROVED.** A written licence/competition review is required before any public display or distribution. Do not rely on an assumed educational exception.

---

## 10. Recommendation

**Proceed only if the project is framed as a bounded exploratory measurement audit with a Mendota core and, at most, conditional Buffalo Pound appendices.**

Specifically:

1. Simplify the public question to one sentence: “How well does surface fluorescence track microscopy-derived cyanobacteria abundance, and what does it fail to establish?”
2. Present the result as a descriptive rank association, not validation/calibration/prediction/early warning.
3. Keep the governance/QC evidence in the report book; put only the essential logic on the poster.
4. Use a Mendota-core narrative; treat Buffalo Pound as a conditional contrast, not a second validation.
5. Complete the licence/competition review before displaying data or derived figures.
6. Document the student’s contribution and external supervision.
7. Be prepared for a weak or null result; make the question and implication clear enough that “no strong association” is still an answer.

If the project owner wants a stronger originality/innovation narrative, the current data do not support it. The honest options are to reduce, reframe or pause — not to inflate.

**No competition entry has been prepared, submitted or discussed with an organiser. D-14 remains NOT APPROVED.**
