# RQIR Candidate Gravity research log — Iteration 256

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Started from authoritative Iteration 255 after reading `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_255.md`, the Iteration-255 research log, recent commits, and GitHub Actions. Actions reported zero workflow runs, so no computation was duplicated.

## Work performed

1. Re-audited the Iteration-252 exact factorization `U1=Nhat^-1 W A Nhat^-1` with `Nhat=W N_orb` and the Iteration-253 Ward identity for `A=R.(D R).E`.
2. Identified that the planned ordinary symmetry test on `U1` would be too strong: `A=A^T` does not imply `U1=U1^T` because the ghost/orbit factors are not symmetrically placed in that representation.
3. Derived the exact weighted object

`U1 W = Q A Q`, `Q=N_orb^-1=Nhat^-1 W`.

Since `Q=Q^T` and `A=A^T`, the correct inherited relation is

`U1 W = W U1^T`.

4. Derived the exhaustive cubic coefficient

`B3=[U1 W]_3 = Q0 A3 Q0 + Q1 A2 Q0 + Q0 A2 Q1 + Q2 A1 Q0 + Q0 A1 Q2 + Q1 A1 Q1`,

with `A3=K0E3+K1E2+K2E1`.
5. Added a deterministic matrix certificate. It reproduces the weighted identity to machine precision while ordinary `U1` symmetry fails generically:
   - `max|Nhat^-1 W-N_orb^-1|=1.39e-16`;
   - `max|U1 W-N_orb^-1 A N_orb^-1|=5.55e-17`;
   - `max|U1 W-W U1^T|=2.26e-17`;
   - `max|U1-U1^T|=2.13e-2`.

Freeze:

`PASS_SCOPED_U1_WEIGHTED_WARD_ORIENTATION_IDENTITY`

and guardrail

`NO_ORDINARY_U1_SYMMETRY_WARD_FAIL`.

This is not a physical comparator coordinate, not an exact comparator identity, not a Candidate Gravity residual, not near-degeneracy, not regime-specific non-identifiability, and not a consistency FAIL. It corrects the orientation of the future cubic Ward gate.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and `BLOCKED_NOT_ZERO`.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 255: **0 percentage points**. A false Ward gate was eliminated and the exact weighted cubic assembly was frozen, but comparator foundation remains `24/25`, robust unique residual remains `0/20`, and no readiness-rubric block closed.

## Exact next gate

Construct `Q0,Q1,Q2` and `A1,A2,A3` in the same frozen parent convention, with `A3=K0E3+K1E2+K2E1`; assemble all six terms of `B3=[U1 W]_3`; require weighted pairwise-transpose/index/TT checks before tensor reduction. Do not test ordinary `U1` symmetry and do not launch heavy integration, Fisher/resources, or `ANSATZ-003`.