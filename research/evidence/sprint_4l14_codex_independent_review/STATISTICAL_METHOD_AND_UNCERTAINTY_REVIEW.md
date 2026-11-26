# Statistical Method and Uncertainty Review

## Spearman rho

Spearman rho is defensible as a simple descriptive measure if the target is monotonic rank association among eligible dates. It is not a measurement-agreement statistic and does not validate RFU as biomass. Ties and zero-heavy microscopy endpoints can reduce resolution and create many tied ranks; the protocol should report tie frequency and the number of distinct values, but not “correct” ties by jitter or transformations. Restricted range after inclusion/QC can attenuate or inflate apparent patterns.

Non-monotonic biology is plausible: taxonomic succession and pigment physiology may yield hump-shaped or phase-specific patterns. A single rho can average incompatible phases. Seasonal confounding and temporal autocorrelation are central, not secondary. A scatterplot with date/season labeling could help interpretation after authorisation; this audit created none. The planned seasonal stratification may itself be sparse and cannot identify a season effect independent of year.

The repeated-date series violate independent-observation intuition. A pooled rho still describes these observed dates, but familiar precision language is unavailable. Missing dates are potentially informative (equipment failure, fouling, open-water sampling, biological targeting) and may not be missing at random. No method here corrects that.

## Sensitivity plan

**Leave-one-year-out (Mendota):** useful influence diagnostic across observed years. It does not give sampling uncertainty or a valid confidence range. Fourteen years are not necessarily comparable or exchangeable; sensor deployment and taxonomy changes occur across period. Report the full set of omissions, not just min/max if an extreme year dominates.

**Leave-one-date-out (Buffalo Pound):** useful influence diagnostic at n unknown, particularly for 2019-07-17. It does not describe uncertainty across years, lakes or sampling protocols. With two sampled seasons, separate year summaries reveal observed difference but are not a replication-based contrast.

**Season-year block bootstrap:** remove from the current protocol unless an independent statistician justifies the estimand, exchangeability assumptions, sparse-block treatment and valid-resample rule before data analysis. Resampling non-exchangeable blocks with replacement does not become defensible merely by calling percentiles “descriptive.” It can give a false appearance of uncertainty quantification. A transparent set of LOYO and pre-specified leave-date diagnostics may be enough for an exploratory project.

**Minimum n:** deferring the overall minimum until after a count audit is understandable, but creates a risk of adapting the reporting rule to the observed n. Set an estimability principle now (what precision or rank resolution would be scientifically useful), without inventing a cutoff. If the reviewer cannot justify a threshold, report that an estimate is descriptive and not stable rather than use n<10 as a universal validity rule.

## Four analyses and interpretation

The four estimates are correlated and share biological dates. Even without p-values, four primaries and multiple seasonal/QC sensitivities create multiplicity of interpretation. Pre-specify one lead endpoint or label all four equal-status exploratory estimates, then report all with no “winner” selection. P1/P2 and P3/P4 are not independent confirmation.

There is measurement error in both axes: microscopy counting/identification, cell geometry and sampling; optical sensor calibration, fouling, depth, drift, pigment content, quenching and range. A simple rho treats values as exact ranks. Without replicate precision or calibration data, quantify that limitation rather than imply the association reflects sensor accuracy.

## Verdict

The revised descriptive method is more honest than the earlier bootstrap/p-value proposals, but it supports only exploratory stability descriptions. Remove the optional block-bootstrap percentile interval as currently specified. A strong rho can still be ecologically misleading due to seasonal co-trending, taxon succession, serial dependence, selection and asynchronous sampling. No correlations or sensitivity analyses were computed for this audit.

