# RQIR Candidate Gravity research log — Iteration 255

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Started from authoritative Iteration 254 after reading `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_254.md`, the Iteration-254 research log, recent commits, and GitHub Actions. Actions had zero runs, so no computation was duplicated.

## Work performed

1. Re-audited the primary Vilkovisky gravity authority, Giacchini–de Paula Netto–Shapiro, PRD 102, 106006 (2020), arXiv:2006.04217.
2. Resolved an upstream convention ambiguity: `D_i R^j_alpha` in `U1,U2` uses the Christoffel `Gamma` of the configuration-space metric; the nonlocal gauge-orbit correction `T` is a separate part of the full physical-space affine connection and is not to be inserted into this `D_i`.
3. Specialized the published field-space Christoffel to the frozen `D=4`, `Lambda=0`, `a=-1/2`, linear covariant split (`gamma1=1`, `gamma2..6=0`): `c1=-1`, `c2=1/4`, `c3=1/4`, `c4=-1/8`.
4. Derived the first background variation `deltaGamma` without changing parent dynamics or field convention.
5. Independently reconstructed the 10x10 DeWitt metric on symmetric metric components and numerically differentiated its Christoffel along a Lorentzian TT direction.

Validation: base `Gamma` mismatch `1.81e-10`; `deltaGamma` mismatch `5.82e-8` for O(1) components; analytic input-pair symmetry residual `0.0`.

Freeze:

`PASS_SCOPED_FIELDSPACE_CHRISTOFFEL_FIRST_VARIATION_AND_TT_VALIDATION`.

This closes the genuinely new geometric vertex identified in Iteration 254. It does not close the full `K1E2` numerator and cannot be promoted to a full cubic Ward result. The Iteration-253 guardrail remains exact: the first legitimate cubic Ward target is `K0E3 + K1E2 + K2E1`.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and `BLOCKED_NOT_ZERO`.

No consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate is claimed. `ANSATZ-003` was not created. Fisher/resources and heavy integration were not run.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 254: **0 percentage points**. The comparator foundation remains `24/25`; robust unique residual remains `0/20`. A scoped vertex-library element closed, but no rubric block closed.

## Next gate

Assemble the complete `E^(2)K^(1)` contribution to `Tr U1` from both `delta(Nhat^-1)` placements, `delta W`, both explicit `deltaR` pieces and the new `deltaGamma` term, all in one condensed-index convention. Perform local/index/TT checks before integration, and construct minimal `K0E3` and `K2E1` siblings before any cubic Ward PASS/FAIL.