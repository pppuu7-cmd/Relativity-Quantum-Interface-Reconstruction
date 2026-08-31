# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 184**

## Scientific state in one sentence

RQIR now uses the split-invariant joint relation `Y=(K2_rows,S_soft2_full_rows)` with exact quadratic calibration applied before comparator profiling. The zero-K2 curvature-cubic local C5 sector has rank 4; EH and the first local quadratic curvature soft2 completions make the **raw** six-row cubic space full rank, but these quadratic parameters have no independent motion after exact K2 calibration and only re-enter in fixed compensation combinations with nonlocal/AS K2 changes. The remaining local task is the covariant `R_mn Box^n R^mn`, n=2..4, soft2 ladder before a calibrated nonlocal direction can be formed.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged through Iteration 184. Do not raise readiness for workload alone.

## Frozen rules

- Repository/recovery is source of truth.
- Unsupported comparator coordinates are BLOCKED, never zero-filled.
- Exact hard constraints precede nuisance profiling/Fisher.
- `ANSATZ-003` must not be created before a nonzero residual survives fixed C3/C4/C5/nonlocal/asymptotic-safety subtraction.
- Fisher/resources remain forbidden until then.
- Metric CTP convention: `h_±=r±a/2` with factorial-normalized cubic vertices.
- For general nonzero-`K2` comparators, the authoritative relation observable is joint source-completed `(K2,S_soft2)`; an internal off-shell Ward/transverse split is not a physical coordinate.

## Retained pre-184 authority

### Zero-K2 local curvature-cubic sector — Iteration 178

On the six frozen physical null-soft rows, the target-independent local curvature-cubic subset through dimension 12 reduces to

`Riemann3_soft2 * {1,(-q^2),(q^2)^2,(-q^2)^3}`

with physics-aware rank `4/6`. Ricci-chain null-soft columns are exact protocol zeros. Frozen extrapolation/error envelope: `5.2625580e-6`.

### C4 — Iterations 179–180

Fixed nonzero-mass dRGT is null-soft protocol-incompatible, not a FAIL. The strongest compatible local/unitary single-massless-spin-2 C4 control merges with the local C5 massless-spin-2 EFT boundary at the frozen order.

### Nonlocal — Iterations 181–182

`QG-NL-EXP-001` is fixed by

`S ~ ∫ sqrt(-g)[R+G_mn F(Box)R^mn]`, `F(Box)=(exp(-lambda Box)-1)/Box`.

Its cubic includes the mandatory Frechet insertion. Representative exponential scalar shapes are near-degenerate with the local finite-row polynomial span below the Iteration-178 error envelope. Iteration 182 further proved that a raw nonlocal cubic cannot be assigned a physical off-shell `B_T` through an arbitrary `W[K2]` split.

### Split-invariant relation protocol — Iteration 183

Freeze

`Y=(K2_rows,S_soft2_full_rows)`.

For parameter tangent blocks `A=dK/dtheta`, `B=dS/dtheta`, exact calibration requires `A delta_theta=0`; if `N_A` spans `ker(A)`, the calibrated cubic comparator span is

`B_cond=B N_A`.

The local quadratic inverse-kernel basis `[x,x^2,x^3,x^4,x^5,x^6]` has rank `6/6` on the six hard rows. Appending the nonlocal lambda tangent `x^2 exp(x)` keeps row rank 6 and creates one parameter null direction. With nonlocal coefficient normalized to +1, the local K2-compensation coefficients are approximately

`[3.72282e-5,-1.00059168,-0.99612543,-0.51334123,-0.14137283,-0.06615095]`.

Thus the relevant nonlocal discriminator is the **full cubic soft2 response of this K2-preserving parameter combination**.

## Iteration 184 — first local quadratic C5 soft2 bridge

Use the same six null-soft TT rows and extract the amputated cubic `O(k_soft^2)` coefficient by a symmetric soft second difference plus two Richardson levels.

New columns:

### EH/common normalization

`[1.5075719591,0.2125004724,2.8203238064,-1.9851779883,-0.1902862337,0.5362481602]`

max convergence error `1.66e-7`.

### `R_mn R^mn`

`[-1.7423297741,-0.1323560370,-3.3439158197,1.3579882480,0.2206726509,0.2169373627]`

max error `1.83e-7`.

### `R_mn Box R^mn`

`[1.5754151008,0.0489981406,2.5059613346,-0.6443314817,-0.2558359645,-0.3828535821]`

max error `2.92e-7`.

Source-completed Ward residual reduction factors on the new soft family:

- Ricci2: `4.000076`;
- RicciBoxRicci: `4.000001`.

Status: `PASS_SCOPED`.

### Raw rank versus calibrated rank

Starting from the zero-K2 rank-4 curvature-cubic span:

- add EH soft2 -> raw rank 5;
- add Ricci2 soft2 -> raw rank 6/6;
- add RicciBoxRicci -> raw rank remains 6.

Final raw singular values:

`[6.23544511,2.17522779,1.08511093,0.09623304,0.04245038,7.53404e-4]`.

This is **not** hard-conditioned comparator saturation. The six local quadratic K2 directions themselves have rank 6/6, hence their exact-calibration parameter nullspace is zero. Their soft2 cubic columns cannot move independently after K2 calibration; they re-enter only as fixed compensation pieces for a nonlocal/AS K2 variation.

Retain:

- `C5-NG-011 — EH_AND_RICCI2_SOFT2_COLUMNS_COMPLETE_THE_RAW_SIX_ROW_LOCAL_C5_SOFT2_RANK_BUT_NOT_THE_HARD_CONDITIONED_SPAN`;
- `REL-NG-002 — RAW_CUBIC_ROW_SATURATION_BY_PARAMETERS_ELIMINATED_BY_EXACT_K2_CALIBRATION_IS_NOT_CONDITIONED_COMPARATOR_SATURATION`;
- `C5-NG-012 — HIGHER_QUADRATIC_DERIVATIVE_SOFT2_COLUMNS_MUST_BE_DERIVED_COVARIANTLY_AND_NOT_INFERRED_FROM_N0_N1`.

## Comparator status

### C3

Ordered metric-CTP / full soft2 completion remains `BLOCKED_C3_CTP_ORDERED_COMPLETION`.

### C4

Compatible massless-spin-2 boundary adds no independent direction; massive dRGT remains outside the null-soft protocol.

### C5

Zero-K2 curvature-cubic sector is complete at the declared local subset; local quadratic soft2 bridge is now instantiated for EH, n=0 and n=1 Ricci-Box directions. Still required: n=2,3,4 covariant soft2 completions.

### Nonlocal

Full `QG-NL-EXP-001` soft2 lambda tangent remains to be computed and combined with **all** local quadratic compensation soft2 columns using the Iteration-183 K2-null vector.

### Asymptotic safety

Real-time/source-completed three-point data remain BLOCKED and must eventually enter the same joint `(K2,S_soft2)` protocol.

## Candidate state

No robust Candidate Gravity residual exists yet.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Current Iteration-184 authority files

- `analysis/c5_local_quadratic_soft2_bridge_iteration184.py`
- `results/c5_local_quadratic_soft2_bridge_iteration184.json`
- `candidate_gravity/C5_LOCAL_QUADRATIC_SOFT2_BRIDGE_ITERATION184.md`
- `research_log/2026-08-31_iteration_184_c5_local_quadratic_soft2_bridge.md`
- `recovery/RECOVERY_DELTA_ITERATION_184.md`

## Immediate next scientific priority — Iteration 185

Develop and validate the covariant cubic soft2 operator calculus for

`R_mn Box^n R^mn`, `n=2,3,4`,

on the exact same six rows. Do not infer these columns from n=0/1 by simple momentum multiplication. Then compute the full nonlocal lambda soft2 tangent including Frechet variation and form the single K2-preserving calibrated nonlocal direction. Compare only that conditioned direction against the zero-K2 curvature-cubic span and numerical envelope. After nonlocal closure, proceed to AS and C3.

No `ANSATZ-003`, Fisher or resources before full quotient survival.
