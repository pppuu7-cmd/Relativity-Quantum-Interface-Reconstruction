# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 183**

## Scientific state in one sentence

RQIR now uses a split-invariant joint relation protocol rather than treating an off-shell Ward/transverse decomposition as observable: the finite comparison object is `Y=(K2_rows,S_soft2_full_rows)`, exact quadratic calibration is eliminated first, and only the full source-completed cubic response of parameter combinations in `ker(dK/dtheta)` enters the comparator quotient. On the current six rows the nonlocal quadratic tangent is exactly compensable by the local dimension-12 polynomial kernel basis, so the next required data are the corresponding local-quadratic and nonlocal full soft2 cubic completions.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged through Iteration 183. Do not raise readiness for workload alone.

## Frozen rules

- Repository/recovery is source of truth.
- Unsupported comparator coordinates are BLOCKED, never zero-filled.
- Exact hard constraints precede nuisance profiling/Fisher.
- `ANSATZ-003` must not be created before a nonzero residual survives fixed C3/C4/C5/nonlocal/asymptotic-safety subtraction.
- Fisher/resources remain forbidden until then.
- Metric CTP convention remains `h_±=r±a/2` with factorial-normalized cubic vertices.
- For general nonzero-`K2` comparators, the authoritative relation object is the joint source-completed `(K2,S_soft2)` protocol; the older conceptual `W[K2]+R:B` split is internal bookkeeping only.

## Retained local/C4 authority

### Local C5 zero-K2 cubic sector — Iteration 178

On the six frozen null-soft rows, the target-independent curvature-cubic subset through dimension 12 reduces to

`Riemann3_soft2 * {1,(-q^2),(q^2)^2,(-q^2)^3}`

with physics-aware rank `4/6`. The frozen numerical/extrapolation envelope is `5.2625580e-6`. Ricci-chain null-soft columns are exact protocol zeros.

### C4 — Iterations 179–180

Fixed dRGT at `m^2=0.04` is `BLOCKED_C4_NULL_SOFT_PROTOCOL_MISMATCH`, not FAIL. The strongest compatible local/unitary single-massless-spin-2 control merges with the same local C5 massless-spin-2 EFT boundary at the frozen order and adds no independent rank.

## Nonlocal/comparator relation development

### Iteration 181 — six-row nonlocal resolution audit

Representative exponential soft-limit scalar shapes appended to the local rank-4 soft span yield fifth singular values only `4.19e-8` to `8.33e-7`, all below the frozen `5.2626e-6` error envelope. Current six-row `q^2` leverage is therefore a resolution risk; this is near-degeneracy, not exact identity.

### Iteration 182 — off-shell split ambiguity

For nonzero `K2`, the schematic split

`Gamma_soft=W[K2]+Rlin:B`

has a transverse repartition freedom. A nonzero Riemann-symmetry shift can be moved between `W` and `B` while leaving the full vertex and pure-gauge Ward tests unchanged. Finite certificate: decomposition shift norm `0.24556`, compensated raw-vertex change `5.55e-17`.

Therefore a raw cubic tensor plus an arbitrary off-shell `W/P_T` convention must not be promoted as a physical comparator direction.

### Iteration 183 — split-invariant joint K2/soft2 conditioning

Freeze directly source-completed observables

`Y=(K2_rows,S_soft2_full_rows)`.

For parameter tangent blocks

`A=dK/dtheta`, `B=dS/dtheta`,

exact quadratic calibration requires

`A delta_theta=0`.

If `N_A` spans `ker(A)`, the allowed calibrated cubic comparator span is

`B_cond=B N_A`.

This is invariant under internal Ward/transverse repartition; numerical split test discrepancy is `4.44e-16`.

On the six frozen hard invariants `x=q^2`, the local quadratic inverse-kernel basis through the dimension-12 convention

`[x,x^2,x^3,x^4,x^5,x^6]`

has rank `6/6` and condition number `2.3982e7`. Appending the fixed nonlocal lambda tangent

`dK_NL/dlambda=x^2 exp(x)`

keeps row rank 6 and creates one parameter-space null direction. Normalized nonlocal coefficient `+1` is compensated by local coefficients approximately

`[3.72282e-5,-1.00059168,-0.99612543,-0.51334123,-0.14137283,-0.06615095]`,

with quadratic null residual `1.65e-16`.

Thus the physical nonlocal discriminator is the **full soft2 cubic response of this K2-preserving parameter combination**.

Retain:

- `REL-NG-001 — JOINT_K2_SOFT2_HARD_CONDITIONING_IS_INVARIANT_UNDER_INTERNAL_WARD_TRANSVERSE_REPARTITION`;
- `C5-NG-010 — LOCAL_QUADRATIC_EFT_SOFT2_COMPLETIONS_ARE_REQUIRED_WHEN_THEIR_K2_DIRECTIONS_COMPENSATE_NONLOCAL_CALIBRATION`;
- `NL-NG-006 — SIX_ROW_NONLOCAL_K2_TANGENT_HAS_AN_EXACT_LOCAL_POLYNOMIAL_COMPENSATION_DIRECTION_AT_FROZEN_DIMENSION12_RESOLUTION`;
- `NG-FUNNEL-041 — CONDITION_FULL_SOURCE_COMPLETED_SOFT2_ON_CALIBRATED_K2_INSTEAD_OF_PROMOTING_AN_OFFSHELL_W_B_SPLIT`.

## Comparator status

### C3

Supported lower-order PQCG pieces remain authoritative. Ordered metric-CTP / full soft2 completion remains `BLOCKED_C3_CTP_ORDERED_COMPLETION`.

### C4

Current compatible massless-spin-2 boundary adds no independent direction; massive dRGT remains a separate protocol.

### C5

The zero-`K2` curvature-cubic soft sector is rank 4. The **quadratic EFT directions used in K2 calibration now require their source-completed soft2 cubic completions**; they are the immediate local gap.

### Nonlocal

`QG-NL-EXP-001` full cubic is fixed in principle, including the Frechet insertion. Its raw soft2 column is necessary but must be combined with the local quadratic soft2 compensation columns according to the Iteration-183 hard-calibration null vector.

### Asymptotic safety

Real-time/source-completed three-point data remain BLOCKED. When available they must enter the same joint `(K2,S_soft2)` protocol rather than an arbitrary off-shell `W/B` split.

## Candidate state

No robust Candidate Gravity residual exists yet.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Current Iteration-183 authority files

- `analysis/joint_k2_soft2_conditioning_iteration183.py`
- `results/joint_k2_soft2_conditioning_iteration183.json`
- `candidate_gravity/JOINT_K2_SOFT2_CONDITIONING_ITERATION183.md`
- `research_log/2026-08-31_iteration_183_joint_k2_soft2_conditioning.md`
- `recovery/RECOVERY_DELTA_ITERATION_183.md`

## Immediate next scientific priority — Iteration 184

Compute the source-completed `O(k_soft^2)` cubic response columns of the local **quadratic** C5 EFT directions used in the six-row `K2` compensation:

1. `R_mn R^mn` and derivative descendants `R_mn Box^n R^mn` through the frozen dimension-12 order;
2. include common EH/normalization cubic response consistently if that direction participates in hard calibration;
3. validate each with the full source-completed Ward identity, not isolated cubic transversality;
4. compute the full `QG-NL-EXP-001` soft2 lambda tangent from the same parent action including Frechet variation;
5. combine the columns using the Iteration-183 K2-null vector to obtain the single calibrated nonlocal cubic direction;
6. compare this direction with the zero-`K2` rank-4 local curvature-cubic span and the frozen numerical envelope;
7. only after that proceed to AS and C3 closure.

No `ANSATZ-003`, Fisher or resources before a nonzero residual survives the full fixed comparator quotient.
