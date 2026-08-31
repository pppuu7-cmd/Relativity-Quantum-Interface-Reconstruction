# RQIR Candidate Gravity Research Log — Iteration 165

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Question

Does the Iteration-164 enriched dRGT residual survive target-independent completion of the local C5 cubic TT basis through the already-frozen dimension-12 cutoff?

## Frozen construction

Keep all 12 Iteration-164 TT rows unchanged. Starting from the five pure-C5 columns already present, add the mixed `Ricci Ricci Riemann` cubic invariant and `Box^n`, `n=1,2,3`, descendants of the existing Ricci-chain and Riemann-chain cubic invariants. No target residual enters operator selection, row generation, conditioning, or stopping.

## Result

The resulting local-C5 matrix has shape `12x12` and rank `12/12`. Raw `s_min/s_max=2.8317567788e-6`. The corrected dRGT targets are both absorbed at machine precision: raw relative residuals are approximately `1.18e-15` for `d/d log(m^2)` and `8.68e-15` for `d/d alpha3`.

Scoped gauge/Ward tests for all new cubic directions pass at machine precision, with largest tested residual below `2.22e-16` for the underlying linearized curvature gauge null and below `6.15e-17` for the new cubic forms.

## Classification

`C5-NG-003 — DIMENSION12_LOCAL_C5_CUBIC_SUBSET_SATURATES_ENRICHED_12ROW_TT_PROTOCOL`.

`C4-NG-007 — ITERATION164_DRGT_RESIDUAL_ABSORBED_BY_TARGET_INDEPENDENT_DIMENSION12_C5_COMPLETION`.

`NG-FUNNEL-022 — FINITE_PROTOCOL_RESIDUAL_MUST_SURVIVE_THEORY_AUTHORIZED_COMPARATOR_BASIS_COMPLETION`.

`NG-FUNNEL-023 — ONCE_ONE_AUTHORIZED_COMPARATOR_SPANS_THE_FINITE_ROW_SPACE ADDITIONAL BLOCKED COMPARATORS CANNOT RESTORE A RESIDUAL IN THAT SAME SPACE`.

This is finite-protocol saturation / regime-specific non-identifiability, not an exact dRGT=C5 identity and not a dRGT consistency FAIL.

The Iteration-164 `dalpha3` residual remains a valid historical residual against the smaller basis but has no promotion status after this completion.

## Gate discipline

No `ANSATZ-003`. No Fisher/resources. BLOCKED C3/nonlocal/AS columns remain BLOCKED; they are simply unnecessary to prove zero orthogonal residual inside a row space already spanned by an authorized C5 subset.

## Readiness change

`MODEL_READINESS: 24%`, up from 23%.

- comparator foundation `24/25` (+1);
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

The +1 reflects closure of a real comparator-basis gap. No residual points are awarded.

## Exact next gate

Iteration 166: leave the saturated 12-row TT space using a target-independent observable extension. Freeze >12 rows and/or an independently defined source-completed non-TT/helicity block before reading dRGT residuals; then recompute the fixed local C5 rank and only afterward the target quotient.