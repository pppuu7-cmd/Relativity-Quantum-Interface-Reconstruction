# Research Log — Iteration 284

Authoritative front before this iteration: Iteration 283. `CURRENT_QG_FRONT`, latest recovery delta, latest research log, recent commits and GitHub Actions were checked. No active Action run was present; the only recent workflow had completed successfully.

Iteration 284 closed the interpolation geometry required before actual p-dependent same-parent numerator reconstruction. For every primitive branch with repeated denominator `(p+v)^2`, the canonical loop variable is `l=p+v`, hence the numerator must undergo the same substitution `p=l-v` before sector summation. Affine loop translation preserves the frozen numerator degree ceilings exactly: degree <=4 for raised bubbles and <=6 for raised triangles.

The finite Lorentz bases are therefore unchanged from Iteration 283: 9 monomials for each bubble sector and 50 monomials for each triangle sector. Deterministic disjoint training and held-out sample sets were constructed on the actual translation-closed kinematics. Both bubble-a and bubble-b sampling matrices have full rank 9/9 on train and held-out sets. All three canonical triangle sectors have nonzero external Gram determinant `-0.01` and full rank 50/50 on both train and held-out sets.

Freeze:

`PASS_EXACT_CANONICAL_SHIFT_DEGREE_PRESERVATION_AND_FULL_RANK_RECONSTRUCTION_DESIGN`.

Guardrail:

`DO_NOT_INTERPRET_FULL_RANK_SAMPLING_AS_NUMERATOR_RECONSTRUCTION; ACTUAL SAME_PARENT PRIMITIVE_NUMERATOR_ORACLE_VALUES_AND_HELD_OUT_RESIDUALS_ARE_STILL_REQUIRED`.

This is an exact reconstruction-design result only. It is not consistency PASS/FAIL of a candidate model, exact comparator identity, regime-specific non-identifiability, near-degeneracy, robust residual, or novelty certificate.

Current operational blocker:

`BLOCKED_ACTUAL_CANONICAL_SHIFTED_SAME_PARENT_NUMERATOR_ORACLE_AND_HELDOUT_RECONSTRUCTION`.

MODEL_READINESS: 24%

Change from previous recorded estimate: 0 percentage points. Comparator foundation remains 24/25 and robust unique residual remains 0/20. The reconstruction basis is now proven finite, canonical and full-rank on the physical closed kinematics, but no linked comparator coordinate or comparator-subtracted residual has yet been produced.

Exact next gate: evaluate the actual denominator-stripped primitive numerator matrices from the frozen same-parent N1/N2/A1/A2/A3 dynamics at the canonical shifted loop points, sum only within each bubble/triangle raised-index sector, solve the 9- and 50-dimensional coefficient systems with rank-revealing QR/SVD, and require small held-out residuals relative to the finite-difference envelope. Only after that perform tensor/IBP reduction. Source/Ward/contact completion, Lorentzian comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream/forbidden.
