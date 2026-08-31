# RQIR Candidate Gravity Research Log — Iteration 163

**Date:** 2026-08-31  
**MODEL_READINESS: 22%**

## Question

Does the scoped dRGT `alpha3` residual from Iteration 157 survive the explicit expanded local C5 ordered-response basis completed through Iteration 162?

## Calculation

Frozen six-probe comparator columns:

`[EH,Ricci^3,Riemann^3,Ricci^2_full,Ricci Box Ricci_full,dRGT_shared_reference]`.

Frozen targets: dRGT `alpha3` and `alpha4` tangents.

Four fixed conditioning conventions were audited: raw, base-row L2, EH absolute-floor, and dRGT-reference absolute-floor.

All comparator matrices have rank `6/6`. Projection residuals of both targets are numerical zero at `~1e-14` absolute scale. The best-conditioned audit has `s_min/s_max=5.500461215995698e-3`; raw has `4.2957925700833976e-4`. This is full finite-row saturation, not merely a numerically tiny one-dimensional residual.

## Result

`C4-NG-004 — EXPANDED_LOCAL_C5_SPAN_ABSORBS_DRGT_NONLINEAR_TANGENT_ON_SIX_TT_PROBES`.

Classification: **REGIME_SPECIFIC_NON_IDENTIFIABILITY / FINITE_PROTOCOL_SATURATION**.

Iteration 157 remains a valid scoped result relative to its smaller comparator base, but its `alpha3` residual is **not stable under the required expanded fixed comparator quotient** and is therefore not authoritative for candidate promotion.

Retain new funnel rule:

`NG-FUNNEL-020 — SIX_ROW_TT_PROTOCOL_SATURATED_BY_FIXED_C5_PLUS_SHARED_BOUNDARY`.

No exact theory identity is claimed. No dRGT consistency FAIL is claimed.

## Readiness change

`MODEL_READINESS: 22%`, down from `24%` in Iteration 162.

Stable-rubric accounting:

- comparator foundation `22/25` — +1 because the expanded C4/C5 quotient is now explicitly recomputed and classified;
- robust unique residual `0/20` — down from `3/20` because the only previously scoped promotable `alpha3` residual is absorbed by the expanded fixed C5 quotient;
- frozen parent dynamics/ANSATZ `0/20`;
- candidate consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

The decrease is scientific, not a loss of infrastructure: the funnel has correctly removed a residual that did not survive a stronger fixed comparator basis.

## Gate discipline

- no `ANSATZ-003`;
- no Fisher;
- no resource calculation;
- no post-hoc weakening of C5;
- no zero-filling of BLOCKED C3/nonlocal/AS rows.

## Exact next gate

Iteration 164: freeze an **enriched observable protocol** with more independent rows than the currently saturated six-TT space, while preserving all existing comparator definitions and parameter conventions. Priority is an independently specified non-TT/helicity-sensitive block (or additional source-completed off-shell triplets if that is the first derivable block). Recompute fixed comparator ranks first; only then test any candidate target residual.
