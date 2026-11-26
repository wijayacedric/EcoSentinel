# Original Question Viability Assessment

**Research question:** Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Assessment date:** 2026-11-24

## 1. Overall classification

**Not currently viable with existing evidence.**  
**Conditionally viable only if specific missing evidence becomes available.**  
**Not realistically testable within the current project constraints without that evidence.**

The question is scientifically plausible, but the current evidence does not satisfy the requirements needed to test it. More sensor observations alone would not fix the problem.

## 2. Requirement-by-requirement assessment

| Requirement | Status | Evidence | Genuine limitation or resolvable? |
|---|---|---|---|
| **1. Biological validity** — independent biological observations can establish defensible bloom events and non-event exposure | **Not satisfied** | Independent microscopy exists (Buffalo Pound 42 dates; Mendota 402 dates), but there are **0 independently reconstructed bloom events** and **0 defensible non-bloom intervals**. Buffalo Pound has 2 biological seasons and no non-bloom sampling. Mendota has 402 dates but no event labels and was rejected for early-warning validation. | **Partly resolvable in principle, not resolved now.** Requires multi-year, independently sampled biology with event/non-event adjudication. More sensor data or proxy labels cannot solve it. |
| **2. Temporal validity** — observations can resolve onset and meaningful warning lead times | **Not satisfied** | Buffalo Pound biology: 1–16-day gaps, no sample times; Mendota: median 14-day interval, date-only. Onset is interval-censored. A few-day lead-time claim is below or near sampling uncertainty. | **Genuine limitation of existing data.** Could be reduced only with time-stamped, sub-weekly/event-triggered biological sampling; not fixable by interpolation or more sensor data. |
| **3. Measurement validity** — sensor variables are reliable, comparable and aligned with the biological endpoint | **Partially satisfied** | High-frequency sensors exist, but chlorophyll/phycocyanin are RFU proxies; Turner and YSI differ by orders of magnitude; sensors are at 0.5 m (Mendota) vs 0–8 m composite; Buffalo Pound is 0.8 m vs 0.8 m but sensor/protocol differences remain; QC flags are incomplete; unflagged values include implausible negatives. | **Partly resolvable** with documented cross-calibration, calibration/maintenance history, nighttime/quality-controlled fluorescence, and depth-resolved biology. Not resolved now. |
| **4. Evaluation validity** — fair comparison against conventional monitoring at comparable false-alarm rates with leakage-resistant validation | **Not satisfied** | No approved event/non-event exposure denominator; matched FAR cannot be estimated; no approved baseline suite or splits; Gate 2H prototype is synthetic only. | **Resolvable only after 1 and 2.** A better algorithm or more sensors cannot create the denominator. |
| **5. Statistical feasibility** — enough independent events, observations and non-event periods for meaningful evaluation | **Not satisfied** | 0 reconstructed events. Buffalo Pound: 42 date-level observations, 2 seasons. Mendota: 402 dates but 14-day, no labels; only 58/402 dates support a 7-variable Turner core, 2/402 an 11-variable YSI core. No non-event exposure. | **Genuine limitation.** More observations could help only if they include independent events, non-events, adequate temporal resolution and common sensor–biology support. More rows alone do not. |

## 3. What “more observations” would and would not solve

**Would help:**
- additional independent biological years with non-bloom season sampling;
- time-stamped, higher-frequency or event-triggered biology;
- depth-resolved microscopy or chlorophyll/phycocyanin profiles;
- documented sensor calibration/maintenance and cross-era comparisons;
- a pre-approved biological event/non-event definition.

**Would not help by itself:**
- more high-frequency sensor rows from the same site/years;
- more derived taxonomy matrices from the same samples;
- using phycocyanin/chlorophyll RFU as labels;
- interpolation of sparse biology into daily “truth”;
- matched-FAR calculations over unknown periods treated as non-bloom;
- more complex models or synthetic validation.

## 4. Current status of the original question

- **Scientifically viable with existing evidence:** **No.**
- **Viable only if specific missing evidence becomes available:** **Yes, conditionally.** The minimum evidence is a multi-year independent biological event/non-event record with adequate temporal resolution and depth alignment.
- **Not realistically testable within current constraints:** **Yes, as currently resourced.** Buffalo Pound is pending with no documented reply; Mendota is rejected for validation; no other candidate is confirmatory-ready; no new dataset search or external contact is authorised.

## 5. What would change the classification

The original question could move toward viability only if **all** of the following become available and are independently verified:

1. independent biological observations across multiple years, including non-bloom periods;
2. time-stamped, sufficiently frequent biology to bound onset/termination;
3. depth-resolved or explicitly matched biological samples;
4. a pre-approved biological-only event/non-event definition;
5. adequate independent event and non-event counts;
6. documented sensor calibration/comparability and QC;
7. a leakage-resistant, matched-FAR evaluation protocol.

Even then, the project would need to demonstrate that the relational indicators add value over strong conventional baselines. The question is not rejected as a long-term scientific question; it is rejected as a **current confirmatory project**.

## 6. Conclusion

The original question is **scientifically plausible but currently untestable**. The bottleneck is not computational sophistication; it is the absence of independent, temporally adequate biological event/non-event evidence and measurement comparability. The project should not proceed to Gate 2 or confirmatory modelling on the current evidence.
