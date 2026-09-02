# Recovery Delta — Iteration 291

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%

## New authoritative correction

The weighted kernel used throughout Iterations 260–289 is

`B = U1 W = Q A Q`.

The actual effective-action insertion is

`U1 = B W^{-1} = B Y_down`,

with `Y_down=sqrt(|g|) g`.

Therefore the mixed cubic effective-action trace is not `tr(B3)`. It contains `B3Y0`, all three routed `B2Y1` partitions, and all three routed `B1Y2` partitions.

At the frozen Iteration-273 translation-closed checkpoint:

- old proxy `tr(B3)=0.9605914180462887`;
- `tr(B3Y0)=0.1071384536577547`;
- weight dressing `=0.6977901599155829`;
- complete `[Tr U1]_{sab}=0.8049286135733377`.

Freeze:

`PASS_EXACT_U1_TRACE_WEIGHT_COMPLETION_FORMULA_AND_B3_EOM_DEGREE_PROVENANCE`.

## Scope of old results

Iterations 278–289 remain valid weighted-kernel B diagnostics. Their scalar trace/tensor/pole results must not be used as coefficients of the actual `Tr U1` effective-action sector before weight completion.

In particular, the old weighted-kernel triangle pole `-0.061289813814603585/epsilon` is no longer the pole authority for `Tr U1`; its physical A/B IR classification is deferred until the complete trace is reduced.

## EOM-degree distinction

`B3=[U1W]_{h^3}` has background degree 3 but EOM degree 1. It belongs to the `e=1,c=2` connection sector.

It is distinct from the EOM-degree-three composite sector

`+(i/2)Tr(U1U2) - (i/6)Tr(U1^3)`.

The complete finite-R3 connection still needs e=1,c=2; e=2,c=1; e=3,c=0 sectors separately.

## Current blocker

`BLOCKED_P_DEPENDENT_COMPLETE_TR_U1_E1C2_NUMERATOR_AND_REDUCTION_AFTER_WEIGHT_COMPLETION`.

## Next

Iteration 292: construct the p-dependent complete `[Tr U1]_{sab}` oracle, recanonicalize denominator families and numerator degree bounds, then repeat complete reconstruction/tensor/Laurent reduction. Only after that return to source/Ward/Born-IR classification.

No Candidate Gravity residual exists. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.
