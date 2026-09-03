# RQIR Research Log — Iteration 299

**Date:** 2026-09-03

**Result:** `PASS_EXACT_EVANESCENT_POLE_SENSITIVITY_PROMOTION_RULE__FINITE_SAME_PARENT_REMAINDER_STILL_BLOCKED`

**MODEL_READINESS: 24%** — unchanged. This iteration closes a regulator/promotion-rule ambiguity but does not create a comparator-subtracted residual or close a readiness rubric point.

Iteration 297 identified that the live `Tr U1` numerical reducer combines a four-dimensional numerator oracle with a `D=4-2 epsilon` loop measure. Iteration 299 converted that observation into an exact Laurent promotion theorem.

For `delta=D-4`, `N=sum_j N_j delta^j`, `M=sum_k A_k delta^k`, one has `C_r=sum_j N_j A_{r-j}`. Hence a simple-pole residue `C_-1=N0 A_-1` is insensitive to unknown evanescent numerator coefficients, whereas the finite coefficient `C_0=N0 A_0+N1 A_-1` is not. For a double pole, even the subleading single-pole coefficient contains `N1 A_-2`.

This justifies a fail-closed rule: never zero-fill invisible evanescent numerator terms; promote the highest Laurent pole when protected, but do not promote a finite remainder through a nonzero pole without the necessary D-dimensional numerator continuation or explicit scheme conversion. A pole-free discontinuity is not obstructed by this specific mixing mechanism at that order.

Validated Actions provenance: run `33700556512`, job `100478719987`, artifact `9873345427`, digest `sha256:e01b2e24de344944675819c3af1cd3b6d8f2a41ddff5dba9c592b1173ac428f1`, head `ae442b799fd1834e9a41cc20012b667cccddac88`. The Iteration-298 validator found exactly one top-level JSON object with sentinel `299`; scientific JSON SHA-256 `735c4806e3780434410a343bfea0e8497a7d2e00b51f2967cc008a31004a47f9`.

Next: apply this promotion rule to the corrected Iteration-296 bubble run; then attack the same-parent D-dimensional numerator/scheme interface before promoting a complete finite C5 coordinate.
