# Recovery Delta — RQIR Iteration 162

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Authoritative change:** explicit local C5 ordered-response block extended from rank 3 to rank 5 on the six frozen TT probes.

## New authorities

- `analysis/c5_curvature_squared_retarded_tangent_iteration162.py`;
- `results/c5_curvature_squared_retarded_tangent_iteration162.json`;
- `candidate_gravity/C5_CURVATURE_SQUARED_TANGENT_ITERATION162.md`;
- `research_log/2026-08-31_iteration_162_c5_curvature_squared_full_tangent.md`;
- `recovery/RECOVERY_DELTA_ITERATION_162.md`.

## Scientific correction

Curvature-squared operators modify `K2` as well as `Gamma3`. Therefore their first-order nonlinear response tangent contains both the new cubic vertex and three propagator-insertion terms.

Do not reuse the `R^3` rule `tangent = cubic vertex only` for lower-order operators.

Retained:

- `C5-NG-001 — CURVATURE_SQUARED_RESPONSE_REQUIRES_PROPAGATOR_INSERTIONS`;
- `NG-FUNNEL-019 — LOWER_DERIVATIVE_KERNEL_DEFORMATIONS_REQUIRE_FULL_RESPONSE_TANGENT`.

## New C5 columns

In the frozen TT convention:

- `deltaK_Ricci2/K_EH = -k^2`;
- `deltaK_RicciBoxRicci/K_EH = +(k^2)^2`.

Full response tangents:

`V_Ricci2=(2.0304860047420306,0.41172109362668774,-3.2456600083419325,-13.33479437694205,4.019028239246117,-2.003363928391969)`.

`V_RicciBoxRicci=(-2.205477099600005,-0.9302576050305512,-1.1238094089110584,5.558096521344366,-1.8978074447048878,0.5425052369944467)`.

Existing implemented base `[EH,Ricci^3,Riemann^3]` rank `3`.

Extended implemented local ordered block rank:

`5/6`.

Singular values:

`(24.63377907944624,7.550268804107893,1.4449862637712527,0.354728220748978,0.030175033336541635)`.

## TT-blind scalar-curvature directions

`R^(1)[h_TT]=0` exactly.

Therefore `R^2` and `R Box R` are exact zero directions in this pure-TT cubic protocol at the tested order. Numerical Richardson artifacts are < `7.2e-10`.

Retained:

`C5-NG-002 — SCALAR_CURVATURE_SQUARED_DIRECTIONS_TT_CUBIC_BLIND`.

Do not interpret this as absence in non-TT/full off-shell C5.

## Ward status

`Ricci^2` and `Ricci Box Ricci` pass the operator-specific source/contact-completed Ward identity with central-stencil `~4x` residual reduction per step halving.

Finest maximum residuals:

- Ricci2: `4.6168e-7` absolute, `4.5328e-6` relative;
- RicciBoxRicci: `1.6787e-7` absolute, `1.5058e-5` relative.

Both: `PASS_SCOPED_WARD_VALIDATED`.

## Readiness

`MODEL_READINESS: 24%` — up by one point.

Accounting:

- comparator foundation `21/25`;
- robust unique residual `3/20`;
- parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

## Exact restart instruction

Resume at **Iteration 163**.

Recompute the fixed dRGT C4 quotient using the expanded local C5 base

`[EH,Ricci^3,Riemann^3,Ricci^2_full,RicciBoxRicci_full]`

and the same nuisance/row-conditioning checks used in Iteration 157.

The earlier dRGT mass/alpha3 residuals were conditioned on the smaller rank-3 local C5 block and are no longer authoritative for promotion decisions.

If the expanded C5 span absorbs the dRGT residual, record a comparator-degeneracy update. If a one-dimensional residual remains, quantify conditioning before any further use.

No `ANSATZ-003`, Fisher or resources yet.
