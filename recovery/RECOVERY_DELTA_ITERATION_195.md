# Recovery Delta — RQIR Candidate Gravity Iteration 195

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## New authority

Prospective protocol remains `RQIR-WITHHELD-NULLSOFT-12-v2`.

Supported parameter block:

`theta=(c1,...,c6,lambda_NL,g0,...,g3)`.

Hard K2 matrix for `(c1..c6,lambda_NL)`:

`A7=[x,x^2,...,x^6,x^2 exp(x)]`.

On the 12 frozen rows:

- `rank(A7)=7`;
- singular values `[2.8493798857,0.5309790379,0.1020649319,0.0103815328,7.7026471e-4,3.8080540e-5,1.3903846e-7]`;
- condition number `2.0493466e7`.

Full 11-parameter hard matrix is `[A7,0_(12x4)]`, rank 7, exact nullity 4. Because A7 is full column rank, the exact hard-preserving parameter nullspace contains only the four zero-K2 curvature-cubic C5 directions `g0..g3`. The nonlocal lambda parameter is not an exact K2-preserving nuisance on withheld v2.

Conditional supported soft2 nuisance after exact hard calibration is exactly the Iteration-194 basis

`V4=Riemann3_soft2*{1,-x,x^2,-x^3}`

with rank 4/12. Supported soft2 complement dimension is 8 before blocked AS/C3 completion.

## Critical caveat

The hard K2 separation is strongly near-degenerate numerically (`cond~2.05e7`). Retain exact algebraic hard-constraint language only. Do not promote this to finite-noise identifiability. If K2 is later softened into a measured calibration, its uncertainty must be propagated explicitly before Fisher.

## Comparator status

- C5 local: supported conditional rank 4/12.
- C4 compatible massless boundary: inside C5 at this scope.
- Nonlocal QG-NL-EXP-001: excluded from the exact hard-preserving nullspace on withheld v2.
- AS: `BLOCKED_AS_REALTIME_RELATION_COMPLETION`, not zero.
- C3: `BLOCKED_C3_CTP_ORDERED_COMPLETION`, not zero.

## Candidate status

No candidate residual has been evaluated.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Authority files

- `analysis/withheld_v2_supported_joint_quotient_iteration195.py`
- `results/withheld_v2_supported_joint_quotient_iteration195.json`
- `candidate_gravity/WITHHELD_V2_SUPPORTED_JOINT_QUOTIENT_ITERATION195.md`
- `research_log/2026-08-31_iteration_195_withheld_v2_supported_joint_quotient.md`

## Next

Target-independent robustness of the hard rank-7 block and conditional soft2 rank-4 block under row deletion / geometry perturbation, while preserving exact-rank versus conditioning distinction.
