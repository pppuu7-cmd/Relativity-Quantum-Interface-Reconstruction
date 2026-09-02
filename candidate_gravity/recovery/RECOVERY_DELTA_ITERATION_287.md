# Recovery Delta — Iteration 287

**Date:** 2026-09-02  
**MODEL_READINESS:** 24%

## New frozen result

The complete actual-oracle raised-bubble numerators have now been tensor-reduced in dimensional regularization.

For `N(l)/[(l^2)^2((l+q)^2)]`, normalized by `i*pi^(D/2)` and with `D_q log_R(-q^2)=1`:

- bubble-a (`q^2=0.41`): `C_a=-0.1247249362037728`;
- bubble-b (`q^2=0.21`): `C_b=+0.10231503679645079`.

Both are nonzero and loop-reflection invariant with residual `0.0`.

Freeze:

`PASS_COMPLETE_70_MONOMIAL_BUBBLE_TENSOR_MOMENT_REDUCTION_NONZERO`.

## Superseded exploratory value

Do not reuse the earlier exploratory bubble-a estimate `-0.64977`. It was obtained before the Iteration-285 discovery that the denominator-only numerator basis was incomplete. The authoritative complete-basis value is `-0.1247249362037728` in the Iteration-287 normalization.

## DR sanity checks

- scalar numerator -> `1/q^2` exactly;
- `l^2` numerator -> `-1` logarithmic coefficient;
- `(l^2)^2` numerator -> scaleless, numerical residue `-1.39e-17`.

## Current blocker

`BLOCKED_COMPLETE_TRIANGLE_TENSOR_REDUCTION_AND_SOURCE_WARD_CONTACT_COMPLETION`.

## Next gate

Iteration 288 reduces all three complete 210-monomial raised-triangle numerators. Calibration: numerator `l^2` must cancel the repeated propagator and reproduce the same ordinary one-null two-mass triangle cut for all three routings. After that, separate triangle double-log content from induced single-log bubble content before assembling the full C5 hard-channel cut.

No Candidate Gravity residual exists. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.
