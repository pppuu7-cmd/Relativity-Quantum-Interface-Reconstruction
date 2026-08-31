# RQIR Research Log — Iteration 162

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Starting point

Iteration 161 proved that the strict local-IR asymptotic-safety operators are structurally inside the complete local C5 EFT family. The explicit six-probe local C5 ordered block, however, still contained only `EH + Ricci^3 + Riemann^3`.

Iteration 162 derives the full first-order ordered-response tangents for the local curvature-squared/derivative operators relevant to that IR sector.

## Critical correction to the naive calculation

For an operator that changes the quadratic kernel, differentiating only the cubic vertex is incomplete.

With

`chi2R ~ Gamma3 Gp Gq Gr`,

one needs

`d chi2R = dGamma3 GpGqGr - Gamma3 GpGqGr sum_i(dK_i/K_i)`.

`Ricci^2` and `Ricci Box Ricci` have nonzero TT quadratic terms. Their propagator-insertion contributions are numerically substantial and sometimes larger than their direct cubic contribution.

Retained:

- `C5-NG-001 — CURVATURE_SQUARED_RESPONSE_REQUIRES_PROPAGATOR_INSERTIONS`;
- `NG-FUNNEL-019 — LOWER_DERIVATIVE_KERNEL_DEFORMATIONS_REQUIRE_FULL_RESPONSE_TANGENT`.

## Results

Analytic/numerical TT kernel ratios:

- `Ricci^2`: `deltaK/K_EH = -k^2`;
- `Ricci Box Ricci`: `deltaK/K_EH = +(k^2)^2`.

Full six-probe tangents:

`Ricci^2 = (2.0304860047420306, 0.41172109362668774, -3.2456600083419325, -13.33479437694205, 4.019028239246117, -2.003363928391969)`.

`Ricci Box Ricci = (-2.205477099600005, -0.9302576050305512, -1.1238094089110584, 5.558096521344366, -1.8978074447048878, 0.5425052369944467)`.

The previous implemented local ordered base `[EH,Ricci^3,Riemann^3]` has rank `3`. Adding these two full tangents gives rank `5/6` with singular values

`(24.63377907944624, 7.550268804107893, 1.4449862637712527, 0.354728220748978, 0.030175033336541635)`.

## Scalar-curvature blindness

For a pure TT leg around flat space,

`R^(1)=0`.

Therefore `R^2` and `R Box R` have exact zero quadratic and pure-TT cubic tangents at this order. Richardson response artifacts are below `7.2e-10`.

Retained:

`C5-NG-002 — SCALAR_CURVATURE_SQUARED_DIRECTIONS_TT_CUBIC_BLIND`.

This is scoped TT-protocol blindness, not removal of those operators from the complete off-shell C5 family.

## Ward validation

Operator-specific source/contact-completed identity:

`B3[L_xi,e2,e3]+B2[Lie_xi e2,e3]+B2[e2,Lie_xi e3]=0`.

Finest residuals:

- `Ricci^2`: max absolute `4.6168e-7`, max relative `4.5328e-6`;
- `Ricci Box Ricci`: max absolute `1.6787e-7`, max relative `1.5058e-5`.

Halving steps reduces maximum residuals by approximately `4x` twice for both operators. Trilinear permutation errors are below `7e-14`.

Both are `PASS_SCOPED_WARD_VALIDATED`.

## Authorities

- `analysis/c5_curvature_squared_retarded_tangent_iteration162.py`;
- `results/c5_curvature_squared_retarded_tangent_iteration162.json`;
- `candidate_gravity/C5_CURVATURE_SQUARED_TANGENT_ITERATION162.md`.

## Readiness

`MODEL_READINESS: 24%`, up from 23%.

Accounting:

- comparator foundation `21/25`;
- robust unique residual `3/20`;
- parent dynamics `0/20`;
- consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

The +1 point reflects two additional explicit independent local C5 ordered directions plus classification of two scalar-curvature directions as TT blind.

## Next gate — Iteration 163

Recompute the earlier dRGT C4 shared-boundary quotient against the now-expanded rank-5 local C5 ordered-response span. The earlier `alpha3` residual survived only against the smaller rank-3 local base and may disappear or become near-degenerate once the newly derived C5 directions are included.
