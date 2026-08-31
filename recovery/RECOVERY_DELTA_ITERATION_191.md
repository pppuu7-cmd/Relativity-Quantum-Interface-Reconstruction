# Recovery Delta — RQIR Iteration 191

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## New result

On the prospectively frozen twelve withheld hard rows, the fixed local quadratic C5 matrix `[x,...,x^6]` has rank 6 and appending `x^2 exp(x)` raises the rank to 7.

A 70-digit first-seven-row minor is nonzero (`1.08954106917884588546e-28`), so the rank increase is certified beyond floating-point SVD alone.

The original six-row exact nonlocal/local K2 compensation is therefore a finite-sample saturation result. It does not survive the withheld extension.

## Consequence

For the frozen seven-parameter local-quadratic + nonlocal-lambda block, the exact `delta K2=0` hard constraint has no nontrivial parameter null direction on the withheld rows. The old conditioned nonlocal soft2 nuisance direction cannot simply be carried over.

No candidate has been tested.

Retain `NL-NG-006`, `REL-NG-008`, `NG-FUNNEL-046`.

## Restart

Compute the zero-K2 local curvature-cubic C5 span on the same withheld rows, then assess its rank/conditioning before any future candidate evaluation.
