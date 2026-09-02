# Candidate Gravity C5 — Iteration 287 bubble tensor-moment reduction

**Date:** 2026-09-02  
**MODEL_READINESS:** **24%**

## Purpose

Reduce the complete degree-`<=4` / 70-monomial actual-oracle raised-bubble numerators from Iterations 285–286 against

`1 / [(l^2)^2 ((l+q)^2)]`

and extract the coefficient multiplying the retarded logarithm in the convention

`D_q log_R(-q^2)=1`.

## Result

Both non-scaleless hard bubbles survive complete tensor-moment reduction:

- bubble-a, `q^2=0.41`:
  `C_a = -0.1247249362037728`;
- bubble-b, `q^2=0.21`:
  `C_b = +0.10231503679645079`.

The two coefficients have opposite sign and are individually nonzero.

Loop reflection is exact at the reported precision:

- bubble-a residual: `0.0`;
- bubble-b residual: `0.0`.

Held-out reconstruction remains controlled:

- bubble-a relative max residual: `7.52e-10`;
- bubble-b relative max residual: `3.24e-9`.

Dimensional-regularization sanity checks:

- scalar numerator gives `1/q^2` exactly;
- numerator `l^2` gives coefficient `-1`;
- numerator `(l^2)^2` reduces to a scaleless tadpole and gives `-1.39e-17` numerically.

Freeze:

`PASS_COMPLETE_70_MONOMIAL_BUBBLE_TENSOR_MOMENT_REDUCTION_NONZERO`.

The earlier exploratory bubble-a estimate `-0.64977` is superseded and must not be reused. It preceded the Iteration-285 discovery that the denominator-only numerator basis was incomplete.

## Scope

These are scalar orbit-trace same-parent C5 bubble cut coefficients only. They are not yet the complete three-point hard-channel discontinuity, not source/Ward/contact completed, not the linked `T_cut`, and not a comparator-subtracted Candidate Gravity residual.

## Current blocker

`BLOCKED_COMPLETE_TRIANGLE_TENSOR_REDUCTION_AND_SOURCE_WARD_CONTACT_COMPLETION`.

## Next gate — Iteration 288

Reduce all three complete degree-`<=6` / 210-monomial raised-triangle sectors in the same normalization, preserving the canonical repeated propagator and the one-null-leg two-mass triangle branch structure. Extract the scalar triangle plus induced bubble cut coefficients and verify routing/reflection consistency before assembling the full C5 hard-channel cut.
