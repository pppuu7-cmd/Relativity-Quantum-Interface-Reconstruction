# RQIR research log — Iteration 285

**Date:** 2026-09-02

Iteration 285 evaluated the actual denominator-stripped same-parent primitive numerator oracle behind the translation-closed C5 B3 object.

The 23 primitive branches reproduce the direct B3 matrix to `1.32e-12`, with `tr B3=0.9605914097678994` and `||B3||_F=1.3106212324929962`.

A held-out reconstruction audit then found that the Iteration-283/284 denominator-only minimal bases are not complete for the actual numerator:

- bubble-a 9-column held-out relative max error: `0.9481450100`;
- bubble-b 9-column held-out relative max error: `0.6811050545`;
- triangle `(0,0.41)` 50-column held-out relative max error: `33.2055942841`.

The exact degree ceilings themselves remain valid. Conservative complete fixed-coordinate bases pass:

- bubble-a degree<=4, 70 monomials: relative max residual `9.30e-10`;
- bubble-b degree<=4, 70 monomials: relative max residual `2.22e-9`;
- triangle `(0,0.41)` degree<=6, 210 monomials: relative max residual `8.87e-11`.

Scientific interpretation: denominator topology fixes the propagator family but does not remove dependence on the null-soft momentum and TT polarization tensors from the numerator. Iterations 283-284 are corrected only at the claimed 9/50 basis-sufficiency layer; translation closure, raised bubble/triangle topology, canonical raised-index sectors and exact degree ceilings remain retained.

MODEL_READINESS remains 24%.

Next: complete 210-monomial held-out reconstruction for the other two triangle sectors and then construct an IBP/tensor-moment or explicitly complete covariant representation before extracting discontinuity coefficients.
