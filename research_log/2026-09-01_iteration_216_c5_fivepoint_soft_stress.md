# RQIR Research Log — Iteration 216

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Starting point

Iteration 215 supplied the first physical pure-Einstein five-graviton finite cut vector after Born-fixed IR subtraction, on the frozen 12-point soft grid, with pointwise conservative numerical errors.

## Target-independent stress test

Use `F(epsilon)=epsilon I_finite(epsilon)`, `z=epsilon/epsilon_max`, `L=log(epsilon/epsilon_ref)`.

### n<=2 regular+log basis

- condition number `4264.620104`;
- relative L2 residual `2.79124e-7`;
- maximum residual / pointwise numerical error `1209.93`;
- RMS residual / pointwise error `368.37`.

Classification: `FAIL_NUMERICAL_COMPLETENESS_PHYSICAL_C5_VECTOR`.

### n<=3 regular+log basis

Add `[z^3,z^3 L]`.

- condition number `2.79550e5`;
- relative L2 residual `5.09786e-10`;
- maximum residual / pointwise error `0.637404`;
- RMS residual / pointwise error `0.246654`.

Classification: `PASS_WITHIN_DECLARED_POINTWISE_NUMERICAL_ERROR_ON_FULL_FROZEN_WINDOW`.

This is the first tested regular+log order that is numerically complete on the frozen physical vector. It is not an exact termination theorem.

## Window robustness

Relative coefficient changes vs the full 12-point n=3 fit:

- drop two largest epsilon: `5.47e-4`;
- drop two smallest epsilon: `1.27e-4`;
- drop both endpoints: `2.62e-4`;
- 8-point inner interpolation: `2.96e-3`, but the 8x8 system is extremely ill-conditioned and is not promotion evidence.

A deterministic perturbation bounded pointwise by the numerical error changes the coefficient vector by `1.17e-3`; conservative L2 bound `4.87e-3`.

## Prediction asymmetry

- fit outer ten points -> predict two smallest epsilon: max error `0.196 sigma_num`;
- fit inner ten points -> predict two largest epsilon: max error `2.16e4 sigma_num`.

Higher-order finite-soft content is genuinely present at the large-epsilon edge. Do not extrapolate a small-epsilon truncated fit over the full window and call it exact.

## Authority change

Primary C5 comparator authority is now explicitly the **12-point physical finite-cut vector plus pointwise numerical error envelope**. Regular+log coefficient vectors are compression only.

## Retained results

- `C5-CUT-016`;
- `SOFT-NG-009`;
- `NUM-NG-018`;
- `NG-FUNNEL-073`.

## External comparator audit

Fresh 2026 literature check does not close the remaining AS/C3 objects. AS now supplies timelike scalar-graviton scattering vertices, but not the required same-parent Lorentzian source-completed three-graviton cut. The 2026 PQCG stochastic-mode work explicitly linearizes around Minkowski in the gravitational MSR/JD analysis and therefore does not determine the missing nonlinear ordered cut.

## Readiness

`MODEL_READINESS: 23%` — unchanged.

No full linked C3/C4/C5/nonlocal/AS quotient exists yet. No Candidate Gravity residual. No ANSATZ-003. Fisher/resources remain forbidden.

## Next gate

Separate the **physical on-shell nonanalytic control** from the still-blocked off-shell/source-completed `T_cut` comparator. Seek either a gauge-safe construction/bound for the off-shell C5 linked cut or a relation-level observable in which the on-shell unitarity information can be imported without gauge-dependent interpolation. Continue AS/C3 authority audits in parallel.
