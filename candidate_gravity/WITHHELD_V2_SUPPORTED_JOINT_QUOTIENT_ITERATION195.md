# RQIR Candidate Gravity — Iteration 195

## Prospective supported joint quotient on withheld v2

Protocol: `RQIR-WITHHELD-NULLSOFT-12-v2`.

This iteration constructs the physically supported part of the joint relation

`Y=(K2_rows,S_soft2_full_rows)`

without importing the old six-row conditioned nonlocal vector and without zero-filling AS/C3.

### Parameter block

Use the supported comparator parameters

`theta=(c1,...,c6,lambda_NL,g0,...,g3)`.

- `c1..c6`: local quadratic C5 hard-kernel directions `x..x^6`;
- `lambda_NL`: fixed `QG-NL-EXP-001` hard-kernel tangent `x^2 exp(x)`;
- `g0..g3`: zero-K2 local curvature-cubic directions with soft2 map
  `Riemann3_soft2*{1,-x,x^2,-x^3}`.

### Exact hard calibration

The 12x7 matrix

`A7=[x,x^2,...,x^6,x^2 exp(x)]`

has rank `7/7` on the prospectively frozen rows. Its singular values are

`[2.8493798857,0.5309790379,0.1020649319,0.0103815328,7.7026471e-4,3.8080540e-5,1.3903846e-7]`.

Thus the full hard matrix

`A_full=[A7,0_(12x4)]`

has rank 7 in 11 parameters and exact nullity 4. Since `A7` has full column rank, every exact hard-preserving variation satisfies

`delta c1=...=delta c6=delta lambda_NL=0`.

The exact nullspace is therefore supported only on `(g0,...,g3)`.

This is stronger than the original six-row result: the old K2-preserving local+nonlocal compensation does not transfer to withheld v2.

### Conditional soft2 nuisance

After imposing the exact hard constraint, the supported conditional soft2 nuisance map is just

`V4=Riemann3_soft2*{1,-x,x^2,-x^3}`,

with rank `4/12`. The orthogonal supported quotient therefore has dimension `8` before unresolved AS/C3 completion.

### Conditioning caveat

The full-rank hard matrix is strongly ill-conditioned:

`cond(A7)=2.0493466e7`.

Therefore the statement above is an **exact algebraic hard-constraint result**, not a finite-noise identifiability result. If K2 is later treated with finite calibration uncertainty rather than as an exact hard constraint, the near-degenerate direction must be propagated explicitly before Fisher/resource work.

### Comparator boundary

- AS: `BLOCKED_AS_REALTIME_RELATION_COMPLETION`, not zero.
- C3: `BLOCKED_C3_CTP_ORDERED_COMPLETION`, not zero.
- C4 massless compatible boundary remains inside local C5 at the frozen scope.

No candidate is evaluated in this iteration.

### Retained results

- `REL-NG-010 — FULL_COLUMN_RANK_WITHHELD_K2_MATRIX_ELIMINATES_ALL_SUPPORTED_QUADRATIC_AND_NONLOCAL_PARAMETER_VARIATIONS_UNDER_EXACT_HARD_CALIBRATION`.
- `C5-NG-015 — AFTER_EXACT_WITHHELD_K2_CALIBRATION_THE_SUPPORTED_CONDITIONAL_SOFT2_NUISANCE_IS_THE_RANK4_ZERO_K2_CURVATURE_CUBIC_SECTOR`.
- `NUM-NG-009 — WITHHELD_K2_INDEPENDENCE_IS_EXACT_ALGEBRAIC_BUT_STRONGLY_ILL_CONDITIONED_AND_MUST_NOT_BE_CONFUSED_WITH_FINITE_NOISE_IDENTIFIABILITY`.
- `NG-FUNNEL-049 — BLOCKED_AS_C3_COLUMNS_MUST_REMAIN_OUTSIDE_THE_SUPPORTED_QUOTIENT_RATHER_THAN_BE_ZERO_FILLED`.

`MODEL_READINESS: 24%` — unchanged. Comparator geometry is more explicit, but AS/C3 still prevent full comparator closure and no unique candidate residual exists.
