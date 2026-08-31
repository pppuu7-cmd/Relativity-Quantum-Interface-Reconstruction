# RQIR Candidate Gravity — Iteration 196

## Structural row-robustness of the supported withheld-v2 quotient

Protocol: `RQIR-WITHHELD-NULLSOFT-12-v2`.

### 1. Hard K2 block is structurally rank 7

The frozen supported hard-kernel columns are

`[x,x^2,x^3,x^4,x^5,x^6,x^2 exp(x)]`.

For every physical row used here `x=q^2>0`, so one factor of `x` can be removed from each row without changing rank. The collocation functions become

`{1,x,x^2,x^3,x^4,x^5,x exp(x)}`.

Their leading Wronskians are

`1, 1, 2, 12, 288, 34560, 34560 (x+6) exp(x)`.

The full Wronskian is therefore strictly positive on `x>0`:

`W7(x)=34560 (x+6) exp(x) > 0`.

Hence the ordered family is an extended complete Chebyshev system on the positive interval. Consequence:

**any seven distinct positive x nodes give a nonsingular 7x7 hard-K2 collocation matrix.**

This promotes the Iteration-191 numerical rank observation to a structural statement for the frozen local-polynomial plus fixed-exponential function family. Exact local/nonlocal K2 compensation is impossible once seven distinct positive hard rows are used.

An exhaustive numerical regression over all `C(12,7)=792` seven-row subsets confirms rank 7 for every subset.

### 2. Conditioning remains a separate issue

The theorem is algebraic. It does not imply good finite-noise conditioning. Among the current seven-row subsets the worst double-precision condition number is about

`1.5493e11`,

with smallest singular value about

`5.2872e-12`.

Therefore exact rank robustness and practical identifiability remain separate gates.

### 3. Conditional C5 soft2 block is a row-scaled Vandermonde

After exact K2 calibration, the supported local C5 soft2 map is

`V4 = diag(r0) [1,-x,x^2,-x^3]`.

All twelve frozen `x` values are distinct and all twelve `r0=Riemann3_soft2` values are nonzero. For any four selected rows,

`det(V4_subset) = (product r0_i) * det([1,-x_i,x_i^2,-x_i^3])`,

which is a nonzero row-scale factor times a Vandermonde determinant. Therefore **any four current rows already have rank 4**. Every larger current subset also has rank 4.

All `C(12,4)=495` four-row subsets pass the numerical regression.

### Interpretation

- Hard local/nonlocal exact independence is structural for the frozen function family, not an accident of one row set.
- Conditional local-C5 soft2 rank 4 is likewise structurally row-robust on the current nonzero-Riemann rows.
- Neither result resolves the AS or C3 authority blockers.
- No candidate target is evaluated.
- No finite-noise Fisher/resource claim is authorized.

### Retained results

- `REL-NG-011 — LOCAL_POLYNOMIAL_PLUS_FIXED_EXPONENTIAL_K2_FAMILY_FORMS_AN_ECT_SYSTEM_AFTER_ROW_FACTORING_ON_X_POSITIVE`.
- `NUM-NG-010 — EXACT_RANK7_IS_ROW_STRUCTURAL_BUT_CAN_REMAIN_SEVERELY_ILL_CONDITIONED`.
- `C5-NG-016 — CONDITIONAL_CURVATURE_CUBIC_SOFT2_BASIS_IS_A_ROW_SCALED_VANDERMONDE_AND_ANY_FOUR_CURRENT_ROWS_HAVE_RANK4`.
- `NG-FUNNEL-050 — STRUCTURAL_RANK_ROBUSTNESS_AND_OPERATIONAL_CONDITIONING_ARE_SEPARATE_GATES`.

`MODEL_READINESS: 24%` — unchanged.
