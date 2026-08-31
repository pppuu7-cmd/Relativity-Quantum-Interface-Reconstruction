# C5 Curvature-Cubic Ward Validation — Iteration 152

## Scope
This iteration validates the two explicit local curvature-cubic C5 directions introduced in Iteration 150, using the same metric convention and six frozen spacelike probes.

The operators are

- `Tr(Ricci^3)`;
- `Riemann_mn^rs Riemann_rs^ab Riemann_ab^mn`.

## Why the completed identity simplifies
Around flat space, both operators start at cubic order in the metric perturbation. Their operator-specific quadratic form therefore vanishes at this perturbative order. The cubic-order diffeomorphism identity reduces to

`B3[L_xi,e2,e3] = 0`

(and likewise for a gauge replacement on either of the other legs).

This is not the EH situation from Iteration 151: EH has a nonzero quadratic action, hence its cubic identity requires the `B2[Lie_xi e]` source/inverse-propagator completion. For the present `R^3` columns the corresponding operator-specific B2 term is absent around flat space.

## Numerical regression
For every one of the six frozen probes, each of the three legs was independently replaced by a pure linearized diffeomorphism polarization. The resulting linearized curvatures vanish to machine precision:

- max `|R^(1)_munu[L_xi]| = 2.220446049250313e-16`;
- max `|Riemann^(1)[L_xi]| = 5.551115123125783e-17`.

The cubic contractions therefore also vanish:

- max `|B3_Ricci3[L_xi,e2,e3]| = 2.4454568146171362e-17`;
- max `|B3_Riemann3[L_xi,e2,e3]| = 7.549184413398274e-17`.

## Certificate
Both existing curvature-cubic columns are **PASS_SCOPED** under the correct operator-specific completed diffeomorphism/Ward identity. Consequently the previously computed local six-probe C5 tangent

`V_C5^(chi2R)` with shape `6x2`, rank `2/2`, `smin/smax=0.2294027268`

is now **PASS_SCOPED_WARD_VALIDATED**, rather than merely TT-projected.

## Limits
This certificate does not validate unsupported higher-dimension local columns, loop/nonanalytic directions, `N2`, or `C3sym`. It also does not close the full C5 comparator quotient and does not authorize Fisher/resources or an `ANSATZ-003` promotion.

Authorities:
- `analysis/c5_curvature_cubic_ward_iteration152.py`;
- `results/c5_curvature_cubic_ward_iteration152.json`.
