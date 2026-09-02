# RQIR research log — Iteration 286

**Date:** 2026-09-02  
**MODEL_READINESS:** 24%

Iteration 286 closes the actual-oracle numerator reconstruction for every non-scaleless translation-closed C5 family while retaining all frozen parent-dynamics, routing and degree constraints from Iterations 273–285.

The two raised-triangle sectors not yet certified in Iteration 285 were reconstructed in the complete fixed-coordinate polynomial basis of total degree <=6 (210 monomials) and checked on independent held-out loop momenta:

- triangle `(0,0.21)`: rank `210/210`, condition number `6935.030221597978`, held-out relative max residual `2.7698947208544858e-11`;
- triangle `(0.21,0.41)`: rank `210/210`, condition number `8545.513087076448`, held-out relative max residual `1.0083215501606952e-11`.

Retained certificates:

- triangle `(0,0.41)`: degree<=6 / 210 basis, held-out relative max residual `8.872284498320589e-11`;
- bubble-a: degree<=4 / 70 basis, held-out relative max residual `9.296403942129201e-10`;
- bubble-b: degree<=4 / 70 basis, held-out relative max residual `2.223469270656875e-9`.

Freeze:

`PASS_COMPLETE_NONSCALELESS_ACTUAL_ORACLE_NUMERATOR_RECONSTRUCTION_ALL_BUBBLE_AND_TRIANGLE_SECTORS`.

The null raised-bubble sectors and the single squared-denominator sector remain scaleless in the frozen massless dimensional-regularization treatment. The numerator-reconstruction blocker is therefore closed.

This result is not a consistency FAIL or PASS of the Candidate Gravity model, not an exact comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate. It is a scoped completeness certificate for the pre-integration C5 numerator representation.

New operational blocker:

`BLOCKED_IBP_TENSOR_MOMENT_REDUCTION_AND_HARD_CHANNEL_COEFFICIENT_EXTRACTION`.

The next gate is to convert the validated 70/210 polynomial coefficients into tensor moments (or an explicitly complete covariant basis including the soft momentum and TT polarizations), reduce them against the frozen raised bubble/triangle families, and extract retarded logarithmic/discontinuity coefficient functions. Source/Ward/contact completion and the Lorentzian comparator quotient remain downstream.

MODEL_READINESS: 24%

Change from Iteration 285: **0 percentage points**. A real reconstruction blocker closed, but comparator foundation remains `24/25` and robust unique residual remains `0/20`; no comparator-subtracted linked observable has yet been obtained.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.
