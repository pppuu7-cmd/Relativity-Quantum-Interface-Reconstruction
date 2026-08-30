# RQIR Research Log — Iteration 077

**Date:** 2026-08-30

## Question

What is the minimal physically measurable apparatus information needed to decide among Toy009, Toy014 and Toy013 after the physical Fisher-rate closure and timing-control audit, without inventing an absolute detector ASD?

## Result

For each source architecture `i`, retain primitive measured inputs

- nuisance-profiled detector science rate `R_beta,i`;
- seven same-time dual-probe matrix calibration rates `R_cal,i,j`;
- independent source-metrology rate `R_src,i` including preparation/reset/readout/acceptance/visibility;
- timing/reference duty `d_i`.

At fixed `Z` and source-amplitude retention target `r`, define

`C_prep=[r/(1-r)]Z^2`,

`x_i=gamma_i R_beta,i/Z^2 sum_j 1/R_cal,i,j`,

`y_i=C_prep R_beta,i/(Z^2 R_src,i)`,

`m_i=1/(1-d_i)`.

Then the complete payload wall clock compresses to

`T_total,i = m_i (Z^2/R_beta,i) (1+x_i+y_i)`.

New retained result **RQIR-RESOURCE-036 — minimal apparatus-rate certificate**: after the physical likelihood and profile are fixed, current architecture selection needs only `(R_beta,x,y,d)` per branch; the seven calibration rates remain mandatory audit inputs but compress to `x` for wall-clock branch selection.

The general pairwise condition is

`q_s(i/k) (m_i/m_k) (1+x_i+y_i) < 1+x_k+y_k`,

where `q_s(i/k)=R_beta,k/R_beta,i` is itself measured/derived from the physical profiled likelihood.

Regression checks reproduce the retained shared-kernel special cases exactly:

- Toy014 vs Toy009: `y > 7.6895205385 + 7.5421347000 x`;
- Toy013 vs Toy014: `x > 5.9842386660 + 98.2399220663 y`.

At `Z=5`, `r=0.90`, `C_prep=225` exactly (floating representation aside).

## Sensitivity result

Writing `P=T_sci+T_cal+T_src`, the log-rate elasticities are simply the wall-clock fractions:

- `d ln P/d ln R_beta = -T_sci/P`;
- `d ln P/d ln R_src = -T_src/P`;
- `d ln P/d ln R_cal,j = -T_cal,j/P`.

Thus apparatus characterization should prioritize the rate carrying the largest total-time weight rather than whichever primitive observable looks experimentally easiest.

## Negative/guardrail result

New **RQIR-NG-030**: a nominal architecture crossing is not a retained decision if rate/duty uncertainty intervals overlap. Require conservative robust dominance `T_i^upper < T_k^lower`, or retain the branch choice as unresolved. The code implements a conservative independent-bounds version; a concrete apparatus may later use correlated uncertainty propagation.

## Decision

Do not launch Toy015 automatically. First instantiate/measure the rate certificate for Toy009/Toy014/Toy013. A broader source search is warranted only if the measured certificate shows a source-dependent wall-clock bottleneck that source co-design can improve.

## Reproduce

`python analysis/apparatus_certificate_iteration077.py`

## Next

Build the first repository-backed apparatus model that supplies `R_beta`, the seven full matrix `R_cal,j`, `R_src`, and control duty for at least Toy009 and Toy014. Keep PSD/transduction/source reset explicit and source-specific; do not substitute arbitrary absolute ASD values merely to force a forecast.
