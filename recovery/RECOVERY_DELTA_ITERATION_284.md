# RECOVERY DELTA — ITERATION 284

## Authority
Source-of-truth front before this iteration: Iteration 283. `CURRENT_QG_FRONT`, latest recovery delta, latest research log, recent commits and GitHub Actions were checked. No active Action run was present.

## New result
Canonical loop translation is now frozen at the numerator level: repeated denominator `(p+v)^2` is mapped to `l^2` by `p=l-v`, and the identical substitution must be applied to each primitive numerator before sector summation. This affine shift exactly preserves the Iteration-283 degree ceilings: degree <=4 for raised bubbles and <=6 for raised triangles.

The corresponding finite Lorentz bases have dimensions 9 and 50. On the actual translation-closed kinematics, deterministic disjoint training/held-out sample matrices are full rank for every non-scaleless canonical sector: bubble-a 9/9, bubble-b 9/9, and all three raised-triangle sectors 50/50. The triangle external two-vector Gram determinant is `-0.01` in every canonical sector.

Freeze:
`PASS_EXACT_CANONICAL_SHIFT_DEGREE_PRESERVATION_AND_FULL_RANK_RECONSTRUCTION_DESIGN`.

Guardrail:
`DO_NOT_INTERPRET_FULL_RANK_SAMPLING_AS_NUMERATOR_RECONSTRUCTION; ACTUAL SAME_PARENT PRIMITIVE_NUMERATOR_ORACLE_VALUES_AND_HELD_OUT_RESIDUALS_ARE_STILL_REQUIRED`.

## Current blocker
`BLOCKED_ACTUAL_CANONICAL_SHIFTED_SAME_PARENT_NUMERATOR_ORACLE_AND_HELDOUT_RECONSTRUCTION`.

Operational BLOCKED only. This is not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, nor a novelty certificate.

## Readiness
MODEL_READINESS: 24%

Change from previous recorded estimate: 0 percentage points. Comparator foundation remains 24/25; robust unique residual remains 0/20. The reconstruction design is now finite and full rank, but the physical sector coefficient functions and comparator-subtracted residual remain absent.

## Exact next gate
Evaluate denominator-stripped primitive numerator matrices from the frozen same-parent N1/N2/A1/A2/A3 dynamics after the canonical loop shifts; sector-sum only after shifting; solve the bubble 9-dimensional and triangle 50-dimensional systems with QR/SVD; validate on held-out loop momenta against the finite-difference envelope. Tensor/IBP reduction is authorized only after this validation. Source/Ward/contact completion, Lorentzian comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream/forbidden.
