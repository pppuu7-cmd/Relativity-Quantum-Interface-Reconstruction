# Recovery Delta — Iteration 420

**Date:** 2026-09-04  
**MODEL_READINESS:** 24%  
**Physical/operator authority:** Iteration 411  
**Structural authority:** Iteration 410  
**Latest validated numerical-method diagnosis:** Iteration 415  
**Active diagnostic computation:** Iteration 419

## Scientific purpose

Iteration 420 prospectively freezes the interpretation of the Iteration-419 cancellation/roundoff diagnostics before the raw Iteration-419 result is consumed. This prevents post-hoc selection between a binary64 summation explanation and a deeper fixed-mass evaluation/derivative-representation explanation.

The target remains double-double global index 2 / class 3 / `q^2=-1`, physically `BLOCKED_CONVERGENCE`. Iteration 413 gives the authoritative negative numerical discrepancy `2.769196909034482e-04 > 2e-05`; its diagnostic physical value is not authority.

## Frozen decision rule

Define a materially explanatory binary64 scale as 25% of the raw Iteration-413 discrepancy:

`0.25 * 2.769196909034482e-04 = 6.922992272586205e-05`.

After raw-valid Iteration 419:

1. If either `max_binary64_roundoff_bound_scaled` or `max_naive_vs_compensated_scaled_delta` is at least `6.922992272586205e-05`, classify binary64 cancellation as materially capable of explaining the observed instability and proceed to an algebraically identical higher-precision evaluation of the same frozen mass nodes and central4×central4 derivative. No smaller `h` is authorized.
2. If both metrics lie below that prospective threshold, classify binary64 summation alone as insufficient to explain the instability and audit conditioning inside the fixed-mass `analytic_sphere_G` evaluation itself (kinematics, degree-4 reconstruction, affine-denominator recurrence, radial extrapolation), again using an algebraically equivalent higher-precision path and no smaller `h`.

Under either branch Iteration 419 and Iteration 420 remain diagnostic/methodological only and cannot promote index 2. Physical promotion still requires a later raw-valid `CONVERGED` high-precision/algebraically-equivalent representation with the unchanged `2e-5` threshold and the existing structural/direct-original-integrand checks.

## Guardrails

No threshold weakening, no angular-grid escalation, no new smaller mass step, no zero fill, no Source/Born subtraction, no `ANSATZ-003`, no Fisher/resources. Frozen Iteration-412 exact15 assembly remains blocked until index 2 obtains physical authority.

## Readiness

Comparator foundation `24/25`; robust unique residual `0/20`; frozen parent dynamics/ANSATZ `0/20`; consistency/positivity/Ward/causality `0/15`; identifiability/Fisher `0/10`; resource/experiment closure `0/10`.

Readiness change from the previous estimate: `0` percentage points. This iteration removes post-hoc interpretive freedom but closes no additional stable readiness-rubric component.

MODEL_READINESS: 24%
