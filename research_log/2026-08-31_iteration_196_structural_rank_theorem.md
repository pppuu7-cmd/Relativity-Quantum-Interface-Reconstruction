# RQIR Candidate Gravity Research Log — Iteration 196

Date: 2026-08-31

## Goal

Test whether the Iteration-195 hard rank-7 and conditional soft2 rank-4 statements are artifacts of the particular withheld-v2 row set.

## Hard K2 theorem

After factoring the positive row factor `x`, the hard functions are

`{1,x,x^2,x^3,x^4,x^5,x exp(x)}`.

Leading Wronskians:

`1,1,2,12,288,34560,34560(x+6)exp(x)`.

Therefore the full Wronskian is strictly positive for `x>0`, and the family is an extended complete Chebyshev system on the positive interval. Any seven distinct positive nodes give rank 7.

All 792 seven-row subsets of the current 12-row protocol pass rank 7 numerically. Worst conditioning remains severe (`cond~1.5493e11`, `smin~5.2872e-12`), so exact rank is not finite-noise identifiability.

## Conditional soft2 theorem

`V4=diag(r0)[1,-x,x^2,-x^3]`.

All current `x` are distinct and all `r0` are nonzero. Every four-row determinant is therefore a nonzero row factor times a Vandermonde determinant. Any four current rows have rank 4; all 495 four-row subsets pass numerically.

## Status

✅ Hard K2 rank 7: structural for any seven distinct positive x nodes in the frozen function family.

✅ Conditional local C5 soft2 rank 4: structural on current nonzero-r0 distinct-x rows.

🟡 Hard K2 conditioning: severe near-degeneracy remains.

🟡 AS: BLOCKED, not zero.

🟡 C3: BLOCKED, not zero.

❌ Candidate residual: not tested.

❌ `ANSATZ-003`: not created.

`MODEL_READINESS: 24%`

Readiness unchanged: comparator geometry is stronger, but the final comparator-foundation point remains blocked by AS/C3 authority completion.

## Next gate

Construct a target-independent prospective hard-row design that improves conditioning of the rank-7 hard K2 block while staying inside the declared physical/derivative domain. Freeze the design rule before any candidate evaluation. Preserve withheld-v2 as authority rather than rewriting it.
