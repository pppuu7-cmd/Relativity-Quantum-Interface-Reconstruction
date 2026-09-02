# RQIR Research Log — Iteration 287

**Date:** 2026-09-02  
**MODEL_READINESS:** 24%

## Question

Do the two non-scaleless C5 raised-bubble sectors remain nonzero after complete actual-oracle numerator reconstruction and dimensional-regularization tensor reduction?

## Answer

Yes, within the scoped scalar orbit-trace same-parent C5 block.

Using the complete degree-4 / 70-monomial numerator basis certified after the Iteration-285 basis correction, the raised-bubble tensor-moment map gives, in the normalization

`D_q log_R(-q^2)=1`

after dividing by `i*pi^(D/2)`:

- bubble-a: `-0.1247249362037728`;
- bubble-b: `+0.10231503679645079`.

Both survive held-out reconstruction and exact loop reflection. The opposite signs mean cancellation is possible only after the remaining triangle sectors are included; neither bubble is individually zero.

## Numerical controls

- bubble-a held-out relative max: `7.52e-10`;
- bubble-b held-out relative max: `3.24e-9`;
- loop-reflection residuals: `0.0`, `0.0`;
- scalar numerator calibration: `1/q^2` exact;
- `l^2` calibration: `-1`;
- `(l^2)^2` scaleless calibration: `-1.39e-17`.

## Supersession

The earlier exploratory bubble-a number `-0.64977` is invalid as authority because it preceded the discovery that the denominator-only numerator basis was incomplete. It is superseded by the complete-basis value above.

## Classification

`PASS_COMPLETE_70_MONOMIAL_BUBBLE_TENSOR_MOMENT_REDUCTION_NONZERO`.

This is not a source-completed `T_cut` and not a Candidate Gravity residual.

## Next

Complete the three degree-6 / 210-monomial raised-triangle reductions, then assemble the full non-scaleless same-parent hard-channel cut before source/Ward/contact completion.
