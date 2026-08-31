# Recovery Delta — RQIR Iteration 163

**Date:** 2026-08-31  
**MODEL_READINESS: 22%**  
**Authoritative change:** the expanded fixed local-C5 plus shared-boundary comparator saturates all six frozen TT response rows, absorbing both scoped dRGT nonlinear target directions to numerical precision.

## New authorities

- `analysis/c4_c5_protocol_saturation_iteration163.py`;
- `results/c4_c5_protocol_saturation_iteration163.json`;
- `candidate_gravity/C4_C5_PROTOCOL_SATURATION_ITERATION163.md`;
- `research_log/2026-08-31_iteration_163_c4_c5_protocol_saturation.md`;
- `recovery/RECOVERY_DELTA_ITERATION_163.md`.

## Core certificate

Frozen comparator matrix:

`M=[EH,Ricci^3,Riemann^3,Ricci^2_full,Ricci Box Ricci_full,dRGT_shared_reference]`.

Frozen targets: dRGT `alpha3`, `alpha4`.

`rank(M)=6/6` under raw plus all three predeclared row-conditioning audits.

Raw `s_min/s_max = 4.2957925700833976e-4`.

Best-conditioned (`base_row_l2`) `s_min/s_max = 5.500461215995698e-3`.

Across all audits both target projection residuals are at numerical zero: maximum absolute residual `<3.71e-14`; maximum relative residual `<1.42e-13`.

## Scientific classification

Retain:

- `C4-NG-004 — EXPANDED_LOCAL_C5_SPAN_ABSORBS_DRGT_NONLINEAR_TANGENT_ON_SIX_TT_PROBES`;
- `NG-FUNNEL-020 — SIX_ROW_TT_PROTOCOL_SATURATED_BY_FIXED_C5_PLUS_SHARED_BOUNDARY`.

This is **finite-protocol saturation / regime-specific non-identifiability**.

It is **not** an exact theory identity, not a dRGT consistency FAIL, and not a statement about untested non-TT/helicity/nonperturbative sectors.

Iteration 157's `alpha3` residual is retained as provenance but is superseded for promotion decisions because it is not stable under the expanded fixed comparator quotient mandated by the funnel.

## Consequence for search strategy

Within exactly six current TT rows, the fixed comparator span already fills the observable space. Adding C3/nonlocal/AS nuisance columns cannot create a new orthogonal residual in those same coordinates. Therefore the bottleneck is now **observable/protocol dimensionality**, not missing nuisance columns.

Do not create `ANSATZ-003`; do not run Fisher/resources.

## Readiness

`MODEL_READINESS: 22%`, down from `24%`.

Accounting:

- comparator foundation `22/25` (+1);
- robust unique residual `0/20` (-3);
- frozen parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

The readiness decrease records the loss of the previously scoped residual under the stronger authoritative comparator quotient; infrastructure progress is intentionally not counted.

## Exact restart instruction

Resume at **Iteration 164**.

Freeze an enriched finite observable protocol with more independent rows than the saturated six-TT block, preserving all existing comparator definitions and parameter conventions. Preferred next block is non-TT/helicity-sensitive source-completed response; if not yet derivable, add independently frozen off-shell triplets from the same operational metric/source convention.

First compute the expanded comparator rank/SVD in the enriched rows. Only if a nonzero orthogonal algebraic target residual survives may candidate-parent work resume. No Fisher/resources before that.
