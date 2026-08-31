# Candidate Gravity — Iteration 162: full local curvature-squared C5 ordered tangent

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Status:** scoped six-probe local C5 ordered-response block extended and Ward validated

## Objective

Iteration 161 established action-level inclusion of the strict local-IR asymptotic-safety operators inside the complete local C5 EFT family. Iteration 162 turns the relevant part of that structural statement into an explicit finite RQIR response certificate on the same six off-shell TT probes used since Iteration 149.

Operators tested:

- `R_mn R^mn`;
- `R^2`;
- `R_mn Box R^mn`;
- `R Box R`.

## 1. Why the Iteration-150 formula is insufficient here

The Iteration-150 `R^3` operators have no quadratic term about flat space, so their first-order response tangent is generated only by their new cubic vertex.

Curvature-squared operators are different. They change both the quadratic inverse propagator and the cubic vertex. For

`chi2R ~ Gamma3 G_R(p) G_R(q) G_R(r)`,

the first derivative with respect to a Wilson coefficient `c` is

`d chi2R/dc = (d Gamma3/dc) Gp Gq Gr`

`              - Gamma3 Gp Gq Gr * sum_i (d K_i/dc)/K_EH,i`.

Therefore a cubic-vertex-only column is incomplete.

Retained result:

**C5-NG-001 — CURVATURE_SQUARED_RESPONSE_REQUIRES_PROPAGATOR_INSERTIONS.**

More generally:

**NG-FUNNEL-019 — LOWER_DERIVATIVE_KERNEL_DEFORMATIONS_REQUIRE_FULL_RESPONSE_TANGENT.**

Whenever a candidate/comparator parameter changes `K2` as well as `Gamma3`, the RQIR tangent must differentiate the complete response rather than only the higher vertex.

## 2. Unreduced action calculation

The calculation uses the same frozen data as Iterations 149–152:

- `g=eta+kappa h`, with stripped common `kappa` normalization;
- six fixed spacelike momentum triplets;
- the same TT projectors and random deterministic polarization seeds;
- the same Gaussian windows;
- the same scalarized retarded propagator convention.

Full metric curvature is computed directly from plane-wave metric jets. `Ricci Box Ricci` and `R Box R` are evaluated in their integration-by-parts covariant representatives using covariant derivatives of the curvature. No on-shell/EOM reduction is made.

Authority:

- `analysis/c5_curvature_squared_retarded_tangent_iteration162.py`;
- `results/c5_curvature_squared_retarded_tangent_iteration162.json`.

## 3. Quadratic-kernel ratios

On the frozen TT legs the operator-specific quadratic kernels satisfy, in the stripped action convention,

`deltaK_Ricci2 / K_EH = -k^2`,

`deltaK_RicciBoxRicci / K_EH = +(k^2)^2`.

These measured numerical ratios agree with the analytic TT structure to numerical precision.

For the scalar-curvature directions, TT transversality and tracelessness imply

`R^(1)[h_TT]=0`.

Hence both `R^2` and `R Box R` have zero quadratic TT tangent and zero trilinear pure-TT cubic tangent at this order.

Finite-difference Richardson artifacts are below

- `7.20e-10` in the `R^2` response column;
- `6.09e-10` in the `R Box R` response column.

They are therefore classified as exact scoped TT blindness, not as tiny physical responses.

Retained result:

**C5-NG-002 — SCALAR_CURVATURE_SQUARED_DIRECTIONS_TT_CUBIC_BLIND.**

This blindness applies only to the present pure-TT ordered-response protocol. It does not remove `R^2` or `R Box R` from the complete off-shell/non-TT C5 family.

## 4. Full nonzero response columns

After the required propagator insertions the two new six-probe columns are

`V_Ricci2 = (`

`  2.0304860047420306,`
`  0.41172109362668774,`
` -3.2456600083419325,`
`-13.33479437694205,`
`  4.019028239246117,`
` -2.003363928391969`
`)`,

and

`V_RicciBoxRicci = (`

`-2.205477099600005,`
`-0.9302576050305512,`
`-1.1238094089110584,`
` 5.558096521344366,`
`-1.8978074447048878,`
` 0.5425052369944467`
`)`.

The propagator-insertion contribution is numerically material, and on several probes it is larger than the direct cubic-vertex contribution. This confirms that the full-tangent correction is not a cosmetic refinement.

## 5. Rank certificate

Previous implemented local ordered-response base:

`[EH, Ricci^3, Riemann^3]`

has rank

`3`.

Adding the two nonzero curvature-squared full tangents gives

`rank = 5` on six probes.

Singular values:

`(24.63377907944624, 7.550268804107893, 1.4449862637712527, 0.354728220748978, 0.030175033336541635)`.

Thus the current implemented local C5 ordered-response family occupies five independent directions in the six-dimensional finite TT protocol.

The two new columns have only modest residuals against the older three-column base. Under three invertible row normalizations the residual fractions range approximately

- `Ricci^2`: `1.73% ... 3.86%`;
- `Ricci Box Ricci`: `1.05% ... 4.75%`.

They are nevertheless algebraically independent and must be retained as comparator directions. Their small conditional residual is a warning that the six-row protocol is becoming close to saturation.

## 6. Ward/source-completion checks

Because `Ricci^2` and `Ricci Box Ricci` have quadratic terms, the correct operator-specific cubic Ward identity is source/contact completed:

`B3[L_xi,e2,e3] + B2[Lie_xi e2,e3] + B2[e2,Lie_xi e3] = 0`.

For both nonzero directions the maximum absolute residual falls by a factor of approximately four whenever the finite-difference step is halved, exactly as expected for the central stencil.

Finest-step maximum residuals:

- `Ricci^2`: `4.62e-7`, max relative `4.53e-6`;
- `Ricci Box Ricci`: `1.68e-7`, max relative `1.51e-5`.

Permutation errors of the trilinear action coefficients are below `7e-14`.

Classification:

- `Ricci^2`: `PASS_SCOPED_WARD_VALIDATED`;
- `Ricci Box Ricci`: `PASS_SCOPED_WARD_VALIDATED`.

For `R^2` and `R Box R`, the pure-TT tangent is analytically zero because every linear scalar-curvature leg vanishes; the numerical zero-convergence diagnostic is consistent with that result.

## 7. Readiness

`MODEL_READINESS: 24%` — increased from 23% by one point.

Accounting:

- comparator foundation `21/25`;
- robust unique residual `3/20`;
- parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

The point is awarded because the local C5 ordered comparator gained two explicit independent source-completed/Ward-validated directions and two additional operators were classified as scoped TT blind.

## 8. Immediate implication

Earlier C4/dRGT residuals were computed against the smaller local C5 base. They must now be re-quotiented against the expanded rank-5 C5 ordered-response span before any surviving dRGT direction can be treated as a meaningful comparator residual.

This is the highest-value next gate for Iteration 163.
