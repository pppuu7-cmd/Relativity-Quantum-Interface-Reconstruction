# Candidate Gravity — Iteration 184: first local quadratic-C5 soft2 bridge

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Status:** EH, Ricci-squared and first derivative Ricci-squared soft2 columns instantiated; higher derivative ladder still BLOCKED

## Purpose

Iteration 183 replaced the convention-dependent off-shell `W/B` split by the joint source-completed relation

`Y=(K2_rows,S_soft2_full_rows)`

with exact `K2` calibration imposed before comparator profiling.

This immediately requires the cubic soft2 completions of local quadratic EFT directions that can compensate a nonlocal/AS change of `K2`.

Iteration 184 computes the first such columns on the same six frozen physical null-soft rows.

## Observable convention

`S_soft2` is the coefficient of `O(k_soft^2)` in the **amputated action-level cubic metric kernel** in the frozen physical metric/source convention. External propagator insertions are not included here because the two-point layer is separately retained as `K2` and hard-conditioned according to Iteration 183.

Soft coefficient extraction uses the symmetric second difference

\[
D_2(h)=\frac{\Gamma(+h)+\Gamma(-h)-2\Gamma(0)}{2h^2}
\]

followed by two Richardson levels on

`h=[0.02,0.01,0.005,0.0025,0.00125]`.

This is materially more stable than the earlier one-sided polynomial extrapolation.

## New columns

### EH/common normalization soft2

`[1.5075719591, 0.2125004724, 2.8203238064, -1.9851779883, -0.1902862337, 0.5362481602]`

Maximum convergence error estimate: `1.66e-7`.

### Ricci-squared

For `R_mn R^mn`:

`[-1.7423297741, -0.1323560370, -3.3439158197, 1.3579882480, 0.2206726509, 0.2169373627]`

Maximum convergence error estimate: `1.83e-7`.

### First derivative Ricci-squared

For `R_mn Box R^mn`:

`[1.5754151008, 0.0489981406, 2.5059613346, -0.6443314817, -0.2558359645, -0.3828535821]`

Maximum convergence error estimate: `2.92e-7`.

## Ward/source-completion check

Use the same source-completed off-shell identity as Iterations 151 and 162, now on the null-soft family at finite soft momentum:

`B3[L_xi,e2,e3] + B2[Lie_xi e2,e3] + B2[e2,Lie_xi e3] = 0`.

When the metric-amplitude finite-difference step is halved:

- `R_mn R^mn`: max residual `3.12064e-7 -> 7.80145e-8`, reduction factor `4.000076`;
- `R_mn Box R^mn`: `1.19711e-7 -> 2.99278e-8`, reduction factor `4.000001`.

Classification: `PASS_SCOPED`.

## Raw soft2 rank result

The existing zero-`K2` curvature-cubic span from Iteration 178 has rank 4.

Appending the EH soft2 column gives rank 5.

Appending `R_mn R^mn` gives raw row rank

\[
\boxed{6/6}.
\]

Adding `R_mn Box R^mn` keeps rank 6. Final raw singular values are

`[6.23544511, 2.17522779, 1.08511093, 0.09623304, 0.04245038, 7.53404e-4]`.

This **must not** be interpreted as conditioned comparator saturation.

## Why raw rank 6 is not the relevant RQIR quotient

The six local quadratic inverse-kernel directions `[x,x^2,...,x^6]` already have rank `6/6` on the six calibrated `K2` rows. Therefore

`ker(dK_local/dtheta)=0`.

After exact `K2` calibration, none of those local quadratic parameters can move independently. Their cubic columns re-enter only as fixed compensation pieces when a nonlocal/AS parameter changes `K2` and a local combination cancels that change.

Hence

`raw S_soft2 rank = 6`

does **not** imply

`hard-conditioned comparator rank = 6`.

Retain:

`REL-NG-002 — RAW_CUBIC_ROW_SATURATION_BY_PARAMETERS_ELIMINATED_BY_EXACT_K2_CALIBRATION_IS_NOT_CONDITIONED_COMPARATOR_SATURATION`.

## Remaining local quadratic ladder

The frozen quadratic TT EFT basis through dimension 12 also contains

- `R_mn Box^2 R^mn`;
- `R_mn Box^3 R^mn`;
- `R_mn Box^4 R^mn`.

Their cubic soft2 completions cannot be inferred by simply multiplying the `n=0` or `n=1` column by powers of `q^2`. Covariant derivatives, connection terms and variation of the Box operator contribute at cubic order.

Retain:

`C5-NG-012 — HIGHER_QUADRATIC_DERIVATIVE_SOFT2_COLUMNS_MUST_BE_DERIVED_COVARIANTLY_AND_NOT_INFERRED_FROM_N0_N1`.

## Retained scientific result

`C5-NG-011 — EH_AND_RICCI2_SOFT2_COLUMNS_COMPLETE_THE_RAW_SIX_ROW_LOCAL_C5_SOFT2_RANK_BUT_NOT_THE_HARD_CONDITIONED_SPAN`.

This confirms that the joint calibration step is not optional: ignoring it would falsely declare the six-row protocol saturated before the actual relation quotient is formed.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

This iteration closes real comparator calculations but not the final comparator-foundation milestone. Higher derivative compensation, full nonlocal soft2, AS, and C3 remain open.

## Exact next gate — Iteration 185

Develop/validate the covariant operator calculus for `R_mn Box^n R^mn`, `n=2,3,4`, at cubic soft2 order. Only then combine all six local quadratic cubic columns with the full nonlocal lambda soft2 column using the Iteration-183 `K2` null vector.
