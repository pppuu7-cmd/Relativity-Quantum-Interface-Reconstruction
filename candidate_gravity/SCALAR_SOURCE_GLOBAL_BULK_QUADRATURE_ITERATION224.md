# RQIR Candidate Gravity — Iteration 224

## MSSC-001 global bulk hard-remainder convergence audit

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Frozen authority entering this iteration

Iteration 222 fixed the two connected-source collinear residues to

`R_in = R_out = -8 M_Born`

in one stripped normalization, without fitting any cap-regulated integral. Iteration 223 then established that the pointwise Born-subtracted cap-shell contribution vanishes as `delta^2` across five scattering angles, both independent external linear spin-2 polarizations, and both collinear directions.

This iteration does **not** alter that subtraction.

## Global bulk test

The already-subtracted hard kernel is

`I_hard(n) = I_cut(n) - R/(1+n_z) - R/(1-n·n_out)`.

Two deterministic angular decompositions were compared:

1. Gauss-Legendre in `mu=cos(theta)` times periodic midpoint sampling in `phi` in the laboratory chart;
2. the same tensor rule after a fixed prospective `y`-rotation by `0.371 rad`.

Both use resolutions `N={12,16,20}` with `N_phi=2N` and omit exact caps of radius `delta={0.08,0.04}` around the two already-certified collinear points. The omitted contribution is controlled separately by the Iteration-223 `delta^2` result.

## Result

The two chart sequences do not yet approach a common finite bulk value uniformly over the frozen five-angle/two-polarization family.

At the finest tested grid, the relative chart disagreement ranges from

`3.099967107e-4`

to

`1.381947503e-1`.

The worst row is `theta_ext=0.45`, external cross polarization, `delta=0.04`:

- lab chart: `49.0040889813`;
- rotated chart: `56.8621379324`;
- relative disagreement: `13.819475%`.

Some rows already agree at the `1e-3` level, showing that the obstruction is not a universal divergence. Other rows remain strongly chart/resolution sensitive. Therefore freezing a single global hard-remainder number now would be numerically unjustified.

## Classification

`BLOCKED_NUMERICAL_BULK_HARD_REMAINDER`

This is an **operational/numerical BLOCKED result**, not:

- a consistency FAIL of `MSSC-001`;
- an exact comparator identity;
- a physics divergence claim;
- near-degeneracy;
- Candidate Gravity novelty.

The local IR completion from Iteration 223 remains valid.

## Retained labels

- `NUM-NG-013 — TWO_FIXED_ANGULAR_DECOMPOSITIONS_DO_NOT_YET_CONVERGE_TO_A_COMMON_MSSC001_GLOBAL_HARD_REMAINDER_ON_THE_TESTED_GRIDS`;
- `SRC-CUT-005 — LOCAL_DELTA2_CAP_COMPLETION_DOES_NOT_GUARANTEE_GLOBAL_BULK_QUADRATURE_STABILITY`;
- `NG-FUNNEL-080 — A_COORDINATE_DEPENDENT_BULK_NUMBER_MUST_NOT_BE_FROZEN_AS_A_PHYSICAL_COMPARATOR_REMAINDER`.

## Next gate

Use a singularity-adapted domain decomposition rather than increasing a global tensor-product grid blindly:

1. keep the two Born-fixed cap neighborhoods in their own local polar charts;
2. integrate the smooth cap-excised bulk with two genuinely independent high-order cubatures;
3. add back the separately controlled local-cap contribution/extrapolation;
4. require a common numerical envelope before freezing any finite source hard remainder.

No `ANSATZ-003`. No Fisher/resources.
