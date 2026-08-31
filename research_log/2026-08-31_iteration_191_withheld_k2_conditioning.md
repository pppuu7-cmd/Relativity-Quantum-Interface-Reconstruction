# RQIR Research Log — Iteration 191

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

Applied only the comparator K2 layer to the prospectively frozen Iteration-190 withheld rows.

The local dimension-12 quadratic basis `[x,...,x^6]` remains rank 6, while appending the fixed nonlocal tangent `x^2 exp(x)` raises the rank to 7. A 70-digit nonzero 7x7 minor certifies that this is not numerical rank noise.

Therefore the exact nonlocal/local K2 compensation used on the original six rows was finite-sample saturation, not a theory identity. On the withheld block, exact K2 calibration removes that seven-parameter nonlocal+local nuisance direction rather than leaving the one-dimensional parameter null of Iteration 183.

No candidate was evaluated.

Retain `NL-NG-006`, `REL-NG-008`, `NG-FUNNEL-046`.

`MODEL_READINESS: 24%` — unchanged.
