# RQIR Candidate Gravity — Recovery Delta Iteration 387

**Date:** 2026-09-04  
**Status:** SCOPED ANALYTIC REGULARIZATION-AUTHORITY RESULT  
**MODEL_READINESS: 24%**

## Question

Iteration 297 correctly blocked promotion of the **full finite same-parent DR remainder** because the four-dimensional numerator oracle does not determine genuinely evanescent numerator structures such as `mu^2=-l_perp^2` or explicit `D-4` traces. Does that ambiguity also invalidate the already raw-validated hard-channel determinant **discontinuity** of Iteration 383?

For the frozen one-loop determinant ordinary two-particle sector and the three off-shell coordinates

`q^2 = {-1, -0.34, -0.14}`,

the answer is **no, within the stated scoped assumptions**.

Freeze:

`PASS_SCOPED_EVANESCENT_AMBIGUITY_DOES_NOT_CHANGE_FROZEN_HARD_BRANCH_DISCONTINUITY__FULL_FINITE_REMAINDER_STILL_BLOCKED`.

## Why

Decompose the D-dimensional loop momentum into its four-dimensional and extra-dimensional pieces. Powers of

`mu^2=-l_perp^2`

map to dimension-shifted one-loop integrals multiplied by factors containing `D-4=-2 epsilon`. The same is true for explicit evanescent metric/numerator traces: a genuinely missing term relative to the strict 4D numerator oracle carries at least one factor vanishing as `epsilon->0`.

Standard one-loop dimensional-regularization / unitarity authority identifies precisely these pieces with the rational `R2`-type completion. Relevant references include:

- Gnendiger et al., *To d, or not to d: recent developments and comparisons of regularization schemes*, Eur. Phys. J. C 77, 471 (2017), DOI `10.1140/epjc/s10052-017-5023-2`: powers of `mu^2` generate dimension-shifted integrals and are responsible for rational one-loop terms;
- Buccioni et al., *OpenLoops 2*, Eur. Phys. J. C 79, 866 (2019): the `(D-4)` numerator remainder is isolated as the `R2` rational contribution while the four-dimensional numerator part is integrated with D-dimensional denominators;
- standard one-loop unitarity reviews: four-dimensional cuts reconstruct the logarithmic/polylogarithmic branch-cut part while rational terms require separate completion.

In the frozen determinant fixture all external virtualities are nonzero. Therefore the scoped ordinary bubble/triangle masters do not sit on a massless external soft/collinear IR configuration. At one loop, the evanescent `O(epsilon)` factor can survive at `epsilon^0` only by multiplying a UV `1/epsilon` pole. The UV pole residue is local in the external momenta, so the surviving finite completion is rational/local. Its finite nonlocal/logarithmic part is multiplied by `O(epsilon)` and vanishes in the limit.

Hence the missing evanescent completion has no hard logarithmic/polylogarithmic branch cut at the three frozen nonzero coordinates. In the repository convention,

`D_s F = Disc_s F/(2*pi*i)`,

its contribution to the frozen hard-channel `D_s` is zero.

## Consequence for Iteration 383

Iteration 383 may now be interpreted as the complete **ordinary-simple determinant hard absorptive vector with respect to the evanescent numerator ambiguity covered by Iteration 297**, not merely as a value inside one arbitrary 4D-numerator/D-measure finite scheme.

The vector remains:

- `q^2=-1`: `D_s Gamma_det=-0.002357789063884683 i`;
- `q^2=-0.34`: `D_s Gamma_det=+0.001462759351572654 i`;
- `q^2=-0.14`: `D_s Gamma_det=+0.0012389565044298413 i`.

No distinct `q^2` coordinates are summed.

## What remains blocked

Iteration 297 is **not superseded for the full finite determinant**. The rational/local finite completion itself remains scheme/continuation dependent until a same-parent D-dimensional numerator or explicit scheme conversion is supplied.

This result also must not be exported without a new audit to:

- external on-shell/IR-singular kinematics;
- a multi-loop problem with higher pole structure;
- a different parent numerator continuation;
- a claim about the full finite amplitude rather than its hard branch discontinuity.

## Readiness

`MODEL_READINESS: 24%`.

Change: `0 pp`. A determinant-discontinuity regularization ambiguity is removed, but no complete comparator bucket or robust residual closes.

## Exact next gate

Treat Iteration 383 as the frozen ordinary-simple determinant hard absorptive vector under this scoped theorem. Keep the full finite-DR rational/local remainder separately BLOCKED. Continue the active `e=2` repeated-cut closures (381/384/385); no new determinant heavy computation is presently required for the hard discontinuity.
