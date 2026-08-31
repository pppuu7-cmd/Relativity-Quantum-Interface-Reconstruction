# RQIR Candidate Gravity Research Log — Iteration 164

**Date:** 2026-08-31  
**MODEL_READINESS: 23%**

## Question

Does the Iteration-163 six-row saturation persist when the same declared C4/C5 dynamics are evaluated on independently frozen additional TT off-shell triplets?

## Pre-target row freeze

Six legacy rows are retained.  Six new rows are generated from RNG seed `164031` using only spacelike kinematic acceptance:

`0.18 <= p^2,q^2,r^2 <= 1.05`, spatial `|cos(q,r)|<=0.82`, invariant ratio `max/min<=4`.

The first six accepted rows (after 16 proposals) are used.  New polarization seeds are `2000+3*i+leg`.  Target residuals do not enter the generator or acceptance rule.

## Provenance correction

Iteration 163 mislabeled the two target arrays as `alpha3,alpha4`.  Comparison with the frozen Iteration-156 authority shows that they are exactly `d/d log(m^2)` and `d/d alpha3`.  `alpha4` remains cubic-TT blind.  The numerical six-row saturation certificate is unchanged.

## Calculation

Enriched fixed matrix:

`M12=[EH,Ricci^3,Riemann^3,Ricci^2_full,Ricci Box Ricci_full,dRGT_shared_reference]`, shape `12x6`.

Targets:

`T=[dRGT_dlogm2,dRGT_dalpha3]`.

All four fixed row-conditioning audits retain `rank(M12)=6`; with both target columns `rank([M12,T])=8`.

Residual fraction ranges:

- `dlogm2`: `7.4567e-4 ... 4.7412e-3`;
- `dalpha3`: `6.7428e-3 ... 9.1427e-2`.

Raw residual fractions are `1.47853845e-3` and `3.90347997e-2`.

Progressive target-independent row addition yields combined rank 7 after one added row and rank 8 from two through six added rows.

## Result

`C4-NG-005 — SIX_ROW_SATURATION_DOES_NOT_PERSIST_UNDER_TARGET_INDEPENDENT_TT_ROW_ENRICHMENT`.

`C4-NG-006 — DRGT_DLOGM2_DIRECTION_IS_NEAR_DEGENERATE_AFTER_ENRICHED_LOCAL_C5_QUOTIENT`.

`NG-FUNNEL-021 — PROTOCOL_SATURATION_MUST_BE_TESTED_FOR_STABILITY_UNDER_PRE_FROZEN_ROW_ENRICHMENT`.

`PROVENANCE-CORR-001 — ITERATION163 TARGET LABELS ARE DLOGM2 AND DALPHA3; ALPHA4 REMAINS CUBIC_TT BLIND`.

Classification of `dalpha3`: **SCOPED ALGEBRAIC RESIDUAL ONLY**, not promotable novelty.  The full enriched C3/nonlocal/AS/C5 comparator quotient is not yet closed.

## Readiness change

`MODEL_READINESS: 23%`, up from 22%.

- comparator foundation `23/25` (+1);
- robust unique residual `0/20`;
- parent dynamics `0/20`;
- consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

The residual category remains zero because blocked comparator columns cannot be treated as zero.

## Gate discipline

- no `ANSATZ-003`;
- no Fisher/resources;
- preserve the six-row saturation as a scoped historical result;
- correct its target labels in all forward-facing summaries;
- do not claim `alpha4` was tested in cubic TT;
- do not promote the enriched `alpha3` residual before the full comparator quotient.

## Exact next gate

Iteration 165: instantiate or sharply classify the missing comparator content on the **same frozen 12 rows**.  The C3 tree ordered-response boundary is already the EH direction after Newton calibration; next priority is a causal nonlocal/asymptotic-safety ordered-response completion that does not invent an unsupported Green-function prescription.  If unavailable, record the causal blocker and advance the strongest other fixed comparator component.  Only a residual surviving the complete enriched quotient can reopen candidate-parent design.
