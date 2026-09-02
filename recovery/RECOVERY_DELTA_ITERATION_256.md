# RECOVERY DELTA — Candidate Gravity Iteration 256

**Date:** 2026-09-02  
**Authoritative iteration:** 256  
**MODEL_READINESS: 24%**

## Delta from Iteration 255

The planned cubic Ward orientation has been corrected before full numerator assembly.

Starting from the frozen exact factorization

`U1 = Nhat^-1 W A Nhat^-1`,

`Nhat = W N_orb`,

`A = R.(D R).E`,

and the symmetric orbit metric `N_orb`, define

`Q=N_orb^-1=Nhat^-1 W`.

Then exactly

`U1 W = Q A Q`.

Iteration 253 established that the complete `A` is symmetric in its gauge indices. Therefore the correct inherited relation is

`U1 W = W U1^T`,

not ordinary `U1=U1^T`.

Freeze:

`PASS_SCOPED_U1_WEIGHTED_WARD_ORIENTATION_IDENTITY`

and

`NO_ORDINARY_U1_SYMMETRY_WARD_FAIL`.

A deterministic matrix certificate gives weighted-relation residual `2.26e-17`, while the ordinary `U1` symmetry residual is generically nonzero (`2.13e-2`). Thus an ordinary-symmetry Ward test would be capable of generating a false consistency FAIL.

For

`Q=Q0+tQ1+t^2Q2+...`,

`A=tA1+t^2A2+t^3A3+...`,

with `A3=K0E3+K1E2+K2E1`, the complete cubic weighted coefficient is

`B3=[U1 W]_3 = Q0A3Q0 + Q1A2Q0 + Q0A2Q1 + Q2A1Q0 + Q0A1Q2 + Q1A1Q1`.

This six-term partition is now the authoritative cubic Ward assembly target.

Retain umbrella blocker:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

`BLOCKED_NOT_ZERO`.

This remains operational/derivational BLOCKED, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or a novelty certificate.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 255: **0 percentage points**. The exact Ward orientation and cubic assembly bookkeeping closed, but no physical comparator coordinate or robust residual closed a rubric block. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Build same-parent `Q0,Q1,Q2` and `A1,A2,A3`, assemble the six-term `B3=[U1 W]_3`, and require weighted pairwise-transpose/index/TT checks. The `A3` block must contain the complete `K0E3+K1E2+K2E1`. Do not test ordinary `U1` symmetry. Tensor reduction/heavy integration remains downstream of this gate.