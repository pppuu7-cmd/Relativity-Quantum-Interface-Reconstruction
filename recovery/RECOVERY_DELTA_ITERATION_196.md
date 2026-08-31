# Recovery Delta — RQIR Candidate Gravity Iteration 196

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Structural hard-K2 authority

Frozen hard functions:

`[x,x^2,x^3,x^4,x^5,x^6,x^2 exp(x)]`.

For `x>0`, factor one `x` from each row. The collocation family becomes

`{1,x,x^2,x^3,x^4,x^5,x exp(x)}`.

Leading Wronskians are

`1,1,2,12,288,34560,34560(x+6)exp(x)`.

The full Wronskian is strictly positive on `x>0`; the family is an extended complete Chebyshev system. Therefore any seven distinct positive hard nodes give exact rank 7. The Iteration-191/195 exact local/nonlocal K2 separation is structural for this frozen function family, not a special property of the chosen 12 rows.

Numerical regression: all `C(12,7)=792` seven-row subsets have rank 7 at the frozen tolerance. Conditioning can nevertheless become severe: worst observed condition number `1.549310734455399e11`, minimum smallest singular value `5.287161780575988e-12`.

## Structural conditional soft2 authority

After exact hard calibration:

`V4=diag(r0)[1,-x,x^2,-x^3]`.

All 12 current `x` values are distinct and all 12 `r0` values are nonzero. Any four-row determinant is a nonzero row-scale factor times a Vandermonde determinant, so any four current rows have rank 4. All `C(12,4)=495` four-row subsets pass the numerical regression.

## Guardrail

Structural rank robustness does not imply operational conditioning. Do not promote exact separation to finite-noise identifiability. Fisher/resources remain forbidden.

## Comparator/candidate state

- C5 supported conditional soft2 rank: 4.
- Nonlocal exact hard-preserving nuisance: absent for >=7 distinct positive nodes in the frozen family.
- AS: BLOCKED, not zero.
- C3: BLOCKED, not zero.
- Candidate residual: not tested.
- `ANSATZ-003`: NOT CREATED.

## Authority files

- `analysis/withheld_v2_structural_rank_theorem_iteration196.py`
- `results/withheld_v2_structural_rank_theorem_iteration196.json`
- `candidate_gravity/WITHHELD_V2_STRUCTURAL_RANK_THEOREM_ITERATION196.md`
- `research_log/2026-08-31_iteration_196_structural_rank_theorem.md`

## Next gate

Create a target-independent prospective hard-row design that improves numerical conditioning while remaining within the declared physical/derivative domain. Freeze its rule before any candidate evaluation. Do not rewrite withheld-v2.
