# Recovery Delta — RQIR Iteration 244

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Previous front

Iteration 243 proved that only EOM degree `e<=3` can contribute to the frozen Minkowski, `Lambda=0`, finite one-loop `O(R^3)` C5 target, but left the exact cubic reduced Vilkovisky coefficients unresolved.

## New authority closure

Cho–Kantowski general VD reduction gives the unique-action insertion sequence through `O(E^5)`. Under cyclic trace equivalence it equals

`-1/2 Tr log(1 - U1 + U2)`.

In the frozen 4D convention anchored to Giacchini–de Paula Netto–Shapiro Eq. (14),

`Gamma_conn = +(i/2) Tr log(1 - U1 + U2)`.

Therefore

`Gamma_conn^(3) = +(i/2) Tr(U1 U2) - (i/6) Tr(U1^3)`.

No independent primitive `U3` is required in the reduced cubic EOM sector; the Iteration-243 placeholder is superseded.

## Classification

`PASS_EXACT_VD_OEPS3_INSERTION_SERIES_IDENTITY`.

Current blocker:

`BLOCKED_COMPOSITE_U1_U2_TRACES_TO_FINITE_CPT3_MASTER_MAP_AND_PURE_GRAVITY_PROJECTION`.

This is operational/authority BLOCKED, not zero, not consistency FAIL, and not an exact comparator identity.

## Readiness

`MODEL_READINESS: 24%` — unchanged. The insertion-series coefficient gap closes, but comparator foundation remains incomplete and no robust unique residual exists.

## Restart

Iteration 245:

1. freeze `U1,U2` inverse-operator definitions in the same convention;
2. count primitive ghost/graviton Green operators in each required trace before cancellations;
3. test direct applicability of standard single-operator CPT3;
4. if it fails, construct the minimal Minkowski resolvent expansion needed through total `R^3`;
5. keep full heavy CPT3 and Fisher forbidden.
