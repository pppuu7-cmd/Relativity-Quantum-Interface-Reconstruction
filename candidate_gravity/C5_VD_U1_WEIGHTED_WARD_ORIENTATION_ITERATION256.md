# RQIR Candidate Gravity — Iteration 256

## Exact weighted Ward orientation for `U1` and cubic assembly map

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Frozen parent

Continue from authoritative Iteration 255 with exactly the same `D=4`, `Lambda=0`, `a=-1/2` Vilkovisky parent, field convention, orbit metric and gauge-weight convention. Keep the Iteration-252 exact factorization

`U1 = Nhat^-1 W A Nhat^-1`,

where

`A_{gamma delta}[E] = R^i_gamma (D_i R^j_delta) E_j`,

`Nhat = W N_orb`, and `N_orb` is the symmetric orbit metric.

No observable, ansatz or comparator convention is changed.

## Why this audit is upstream-critical

Iteration 253 correctly proved that the exact Ward identity makes the complete kernel `A[E]` symmetric in its two gauge/orbit indices, with the cubic coefficient

`A3 = K0 E3 + K1 E2 + K2 E1`.

However, that does **not** by itself imply ordinary matrix symmetry of `U1`, because `U1` is dressed asymmetrically by `Nhat^-1` and `W`. Therefore a future test of `U1-U1^T` would be an invalid Ward gate and could produce a false consistency FAIL.

## Exact weighted identity

From Iteration 252,

`Nhat = W N_orb`,

so

`Nhat^-1 W = N_orb^-1 := Q`,

and

`Nhat^-1 = Q W^-1`.

Therefore

`U1 W = Q A Q`.

Since the orbit metric `N_orb` is symmetric, `Q=N_orb^-1` is symmetric. Iteration 253 gives `A=A^T`. Hence

`(U1 W)^T = Q A Q = U1 W`.

Equivalently,

`U1 W = W U1^T`.

This is the correct weighted self-adjoint/Ward orientation inherited from the same parent. Ordinary `U1=U1^T` is neither required nor generally true.

Freeze the guardrail

`NO_ORDINARY_U1_SYMMETRY_WARD_FAIL`.

and the scoped exact result

`PASS_SCOPED_U1_WEIGHTED_WARD_ORIENTATION_IDENTITY`.

## Cubic coefficient map

Write

`Q(t)=Q0+t Q1+t^2 Q2+...`,

`A(t)=t A1+t^2 A2+t^3 A3+...`,

with

`A3 = K0E3 + K1E2 + K2E1`.

Then the complete cubic coefficient of the weighted object `B:=U1 W=Q A Q` is

`B3 = Q0 A3 Q0`

`   + Q1 A2 Q0 + Q0 A2 Q1`

`   + Q2 A1 Q0 + Q0 A1 Q2`

`   + Q1 A1 Q1`.

This is a six-term exhaustive partition. If `Qn=Qn^T` and `An=An^T`, the second/fourth terms form transpose pairs and the first and last are individually symmetric. Thus the correct cubic Ward check is naturally organized as a weighted pairwise-transpose certificate.

## Consequence for the Iteration-255 assembly plan

The Iteration-252 four-term expression in `Ghat=Nhat^-1`, `W`, and `A` remains algebraically correct. But for Ward testing it is safer and simpler to regroup it through

`Q = Ghat W = N_orb^-1`.

At first background order,

`delta Q = delta(Ghat W) = (delta Ghat) W0 + Ghat0 (delta W)`.

Thus the explicit `delta W` term is not an independent Ward structure after weighting; it combines with the left resolvent variation into `delta Q`. This avoids a possible double-counting or false asymmetry diagnosis when the full cubic numerator is assembled.

The same caution applies to the right factor after multiplying `U1` by `W`: its variation must be tracked as the right `Q` variation in the weighted object.

## Deterministic certificate

A reproducible random-matrix test uses symmetric positive-definite `N_orb` and `W`, and symmetric `A`. It finds:

- `max|Nhat^-1 W - N_orb^-1| = 1.39e-16`;
- `max|U1 W - N_orb^-1 A N_orb^-1| = 5.55e-17`;
- weighted symmetry residual `max|U1 W - W U1^T| = 2.26e-17`;
- ordinary symmetry residual `max|U1-U1^T| = 2.13e-2`.

So ordinary `U1` symmetry demonstrably fails in a generic valid matrix realization while the exact weighted identity holds to machine precision.

## Scientific classification

This iteration prevents a false future consistency FAIL and supplies a stricter assembly orientation. It is **not** a C5 comparator coordinate, exact comparator identity, Candidate Gravity residual, near-degeneracy result, or regime-specific non-identifiability result.

Retain

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and

`BLOCKED_NOT_ZERO`.

The blocker is now narrower and better posed: assemble the cubic **weighted** object `B3=[U1 W]_3` in the `Q A Q` basis, with the complete `A3=K0E3+K1E2+K2E1`, then run pairwise transpose/index/TT checks before tensor integration.

## Reproducibility

- `candidate_gravity/code/iteration256_vd_u1_weighted_ward_orientation.py`
- `candidate_gravity/results/iteration256_vd_u1_weighted_ward_orientation.json`

## Readiness

MODEL_READINESS: 24%

Change from Iteration 255: **0 percentage points**. A potentially invalid Ward gate was eliminated and the exact weighted cubic assembly was frozen, but no physical comparator coordinate or robust nonzero residual closed a readiness-rubric block.

## Exact next gate — Iteration 257

Construct `Q0,Q1,Q2` from the same orbit metric/resolvent convention and `A1,A2,A3` from the same parent, with `A3=K0E3+K1E2+K2E1`. Assemble all six terms of `B3=[U1 W]_3`, require the exact weighted pairwise-transpose/index/TT certificate, and only then proceed to tensor reduction. Do not test ordinary `U1` symmetry. Do not launch heavy integration, Fisher/resources, or create `ANSATZ-003` before a nonzero physical comparator residual exists.