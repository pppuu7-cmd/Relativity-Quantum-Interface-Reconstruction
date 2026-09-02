# RQIR Research Log — Iteration 294

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%

## Question

Does the actual weight-completed cubic `Tr U1` insertion remain nonzero on the positive timelike hard-channel slice once the old `tr(B3)` proxy is replaced by `Tr(B Y_down)`?

## Result

Yes, as a scoped fixed-loop-momentum numerator certificate.

Across `s=0.004,...,0.032`, the complete trace is positive and ranges from `0.88125485` to `1.61889698`. Step stability is at the few-parts-in-10^6 level.

At `s=0.016`, the actual trace is `1.0786279385`, whereas the old proxy is `-20.4584735467`. The trace-weight completion therefore changes the numerical and sign structure qualitatively.

## Consequence

Do not reuse weighted-kernel proxy tensor/pole coefficients for the effective-action trace. Reconstruct numerator coefficients directly on the timelike cut slice before evaluating `+/- i0` loop discontinuities.

## Classification

`PASS_SCOPED_TIMELIKE_TRANSLATION_CLOSED_WEIGHT_COMPLETED_TRU1_NONZERO_ALL_ROWS`.

No Candidate Gravity residual is declared.
