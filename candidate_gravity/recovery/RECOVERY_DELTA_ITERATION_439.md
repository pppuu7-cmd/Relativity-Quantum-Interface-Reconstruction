# RECOVERY DELTA — ITERATION 439

**Status at allocation:** prospectively frozen diagnostic; result not yet consumed.  
**Authority target:** Iteration-270 binary64 `Acoef` signed-sum conditioning only.  
**MODEL_READINESS:** 24% at launch.

## Frozen object

All seven nonempty `LEGS` subsets at `M=POS`, `p=P0`, unchanged `h1=1e-4`, `h2=5e-4`, `h3=1e-3`; exactly 26 signed `A_finite` nodes.

For each component, measure `sum(abs(nodes))/abs(signed_sum)` before the `(2h)^n` derivative denominator, and independently reconstruct parent `Acoef`.

## Frozen validity rule

- all node and Acoef values finite;
- exactly 26 nodes and 7 subsets;
- explicit signed-sum Acoef vs parent Acoef scaled discrepancy `<=1e-12`.

Cancellation amplification has no physical pass/fail ceiling here; it is diagnostic localization only.

No physical promotion, no threshold/step change, no zero fill, no `ANSATZ003`, no Fisher/resource claims.
