# RQIR Candidate Gravity Research Log — Iteration 195

Date: 2026-08-31

## Goal

Construct the supported prospective comparator quotient on `RQIR-WITHHELD-NULLSOFT-12-v2` using the exact joint `(K2,S_soft2)` logic, without transferring the old six-row conditioned nonlocal direction and without zero-filling blocked AS/C3 coordinates.

## Result

The hard matrix for the six local quadratic C5 directions plus the fixed nonlocal lambda tangent is

`A7=[x,x^2,...,x^6,x^2 exp(x)]`.

On the 12 prospectively frozen rows:

- rank = `7/7`;
- smallest singular value = `1.3903845821e-7`;
- condition number = `2.0493465781e7`.

Embedding the four exact zero-K2 curvature-cubic parameters gives an 11-parameter hard matrix of rank 7 and exact nullity 4. The exact hard-preserving nullspace is supported only on those four curvature-cubic parameters. In particular, the fixed nonlocal lambda direction does not survive exact K2 calibration on withheld v2.

The conditional supported soft2 nuisance is therefore the Iteration-194 rank-4 local C5 basis. Its quotient complement has dimension 8 before AS/C3 completion.

## Scope guard

The hard block is strongly ill-conditioned. This is exact algebraic independence, not finite-noise identifiability. No Fisher/resource calculation is authorized.

AS and C3 remain BLOCKED, not zero.

## Status

✅ Supported prospective joint quotient: resolved scoped.

✅ Exact K2-preserving nonlocal nuisance: absent on withheld v2.

🟡 AS real-time/source-completed relation: BLOCKED.

🟡 C3 ordered nonlinear relation: BLOCKED.

❌ Candidate residual: not tested.

❌ `ANSATZ-003`: not created.

`MODEL_READINESS: 24%`

Readiness unchanged: comparator foundation remains `24/25`; the final point is not earned while AS/C3 are unresolved and no candidate residual exists.

## Next gate

Run target-independent robustness of both the rank-4 conditional C5 soft2 span and the rank-7 hard K2 span under preregistered row deletions / row-family perturbations. Preserve the distinction between exact rank and numerical conditioning. Do not use any candidate target.
