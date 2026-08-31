# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 185**

## Scientific state in one sentence

RQIR uses the split-invariant joint relation `Y=(K2_rows,S_soft2_full_rows)` with exact quadratic calibration before comparator profiling. The zero-K2 curvature-cubic local C5 sector has rank 4 on six null-soft TT rows; Iteration 185 now completes the entire dimension-12 local quadratic compensation bridge through `R_mn Box^4 R^mn` with covariant action-level soft2 columns and machine-precision source-completed Ward checks. The exact next object is the full `QG-NL-EXP-001` lambda soft2 tangent, which must be combined with the fixed local K2-compensation vector before any nonlocal rank/novelty claim.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged through Iteration 185. Do not raise readiness for workload alone.

## Frozen rules

- Repository/recovery is source of truth.
- Unsupported comparator coordinates are BLOCKED, never zero-filled.
- Exact hard constraints precede nuisance profiling/Fisher.
- `ANSATZ-003` must not be created before a nonzero residual survives fixed C3/C4/C5/nonlocal/asymptotic-safety subtraction.
- Fisher/resources remain forbidden until then.
- Metric CTP convention: `h_±=r±a/2` with factorial-normalized cubic vertices.
- For nonzero-K2 comparators the physical relation observable is joint source-completed `(K2,S_soft2)`; an internal off-shell Ward/transverse split is not a physical coordinate.
- Higher-derivative covariant cubic columns may not be inferred by row-wise multiplication of lower-order columns by powers of `q^2`.

## Retained authority before Iteration 185

### Zero-K2 local curvature-cubic sector — Iteration 178

On the six frozen physical null-soft rows the target-independent local curvature-cubic subset through dimension 12 reduces to

`Riemann3_soft2 * {1,(-q^2),(q^2)^2,(-q^2)^3}`

with physics-aware rank `4/6`. Ricci-chain null-soft columns are exact protocol zeros. Frozen extrapolation/error envelope: `5.2625580e-6`.

### C4 — Iterations 179–180

Fixed nonzero-mass dRGT is null-soft protocol-incompatible, not a FAIL. The strongest compatible local/unitary single-massless-spin-2 C4 control merges with the local C5 massless-spin-2 EFT boundary at the frozen order.

### Nonlocal definition and resolution — Iterations 181–183

`QG-NL-EXP-001` is fixed by

`S ~ ∫ sqrt(-g)[R + G_mn F(Box) R^mn]`, `F(Box)=(exp(-lambda Box)-1)/Box`.

Representative exponential scalar shapes are near-degenerate with the finite-row local polynomial span below the Iteration-178 error envelope, but this is not an exact comparator identity.

Iteration 182 showed that a raw nonlocal cubic cannot be assigned a physical off-shell `B_T` by an arbitrary `W[K2]` split.

Iteration 183 therefore froze the split-invariant relation

`Y=(K2_rows,S_soft2_full_rows)`.

For parameter tangent blocks `A=dK/dtheta`, `B=dS/dtheta`, exact calibration requires `A delta_theta=0`; if `N_A` spans `ker(A)`, the calibrated cubic comparator span is `B_cond=B N_A`.

The six-row local quadratic inverse-kernel basis `[x,x^2,x^3,x^4,x^5,x^6]` has rank `6/6`. Appending the nonlocal lambda tangent `x^2 exp(x)` keeps row rank 6 and creates one parameter null direction. With nonlocal coefficient normalized to +1, the exact null vector local part is

`[3.7228200179970815e-05,-1.0005916758017337,-0.9961254264296668,-0.5133412288524085,-0.1413728259742054,-0.06615094900201549]`.

Thus the discriminator is the full cubic soft2 response of this K2-preserving parameter combination.

### First local quadratic soft2 bridge — Iteration 184

Iteration 184 computed EH, `R_mn R^mn` and `R_mn Box R^mn` soft2 columns. EH plus Ricci2 made the raw six-row cubic matrix full rank, but this was not calibrated saturation because the associated local K2 directions have no independent motion after exact K2 calibration.

## Iteration 185 — complete local quadratic C5 soft2 bridge

A formal multilinear plane-wave expansion through cubic order now supplies a recursive fully covariant rank-2 d'Alembertian. This includes connection, inverse-metric and operator/Frechet-like variations internal to each local `Box^n` operator and removes the need for nested position-space finite differencing.

On the same six rows:

### `R_mn Box^2 R^mn`

`[-1.1165183849,-0.0138751458,-1.6820857577,0.2756448325,0.2663354180,0.2728910445]`

### `R_mn Box^3 R^mn`

`[0.7133600700,0.0017605282,1.0529592750,-0.1111297369,-0.2235239287,-0.1459711976]`

### `R_mn Box^4 R^mn`

`[-0.4308356613,0.0013520156,-0.6274976618,0.0431046862,0.1618211492,0.0674407295]`

Maximum soft extrapolation error is `3.04e-10`.

Source-completed Ward residuals for n=2,3,4 are machine-level: maximum relative residual `<5.3e-14`. Status: `PASS_MACHINE_PRECISION_SCOPED`.

The formal n=0/1 cross-check shifts Iteration-184 values by at most `2.30e-7` and `6.54e-7`. This is not a physics FAIL: the older quoted error tracked only soft Richardson convergence and omitted nested finite-position derivative discretization. Use the formal Iteration-185 values for subsequent compensation.

### Complete local K2-preserving compensation soft2 piece

Ordering local directions as

`[EH,Ricci2,RicciBoxRicci,RicciBox2Ricci,RicciBox3Ricci,RicciBox4Ricci]`,

the Iteration-183 exact null coefficients give

`S_soft2_local_comp = [0.6749106619,0.0904184173,1.6058813167,-0.8456710924,-0.0817908525,0.0404129788]`.

This vector is frozen for the next nonlocal calculation.

Retain:

- `C5-NG-013 — COVARIANT_RICCI_BOX2_TO_BOX4_SOFT2_LADDER_IS_NONTRIVIAL_AND_NOT_GENERATED_BY_ROW_WISE_Q2_MULTIPLICATION`;
- `NUM-NG-003 — NESTED_POSITION_SPACE_DIFFERENCING_CAN_UNDERSTATE_TOTAL_OPERATOR_CALCULUS_ERROR_EVEN_WHEN_SOFT_RICHARDSON_ERROR_IS_SMALL`;
- `REL-NG-003 — DIMENSION12_LOCAL_K2_COMPENSATION_NOW_HAS_A_COMPLETE_SOURCE_COMPLETED_SOFT2_VECTOR`.

## Comparator status

### C3

Ordered metric-CTP / full soft2 completion remains `BLOCKED_C3_CTP_ORDERED_COMPLETION`.

### C4

Compatible massless-spin-2 boundary adds no independent direction in the current protocol; massive dRGT remains outside the null-soft protocol.

### C5

Zero-K2 curvature-cubic sector is complete at the declared local subset. The local quadratic dimension-12 soft2 bridge is now complete for EH plus `R_mn Box^n R^mn`, n=0..4.

### Nonlocal

Full `QG-NL-EXP-001` lambda soft2 tangent at frozen lambda=1 remains BLOCKED until computed from the parent action including exponential operator/Frechet variation. Once available, add the fixed local compensation vector before quotienting.

### Asymptotic safety

Real-time/source-completed three-point data remain BLOCKED and must enter the same joint `(K2,S_soft2)` protocol.

## Candidate state

No robust Candidate Gravity residual exists yet.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Current Iteration-185 authority files

- `analysis/c5_local_quadratic_soft2_completion_iteration185.py`
- `results/c5_local_quadratic_soft2_completion_iteration185.json`
- `candidate_gravity/C5_LOCAL_QUADRATIC_SOFT2_COMPLETION_ITERATION185.md`
- `research_log/2026-08-31_iteration_185_c5_local_quadratic_soft2_completion.md`
- `recovery/RECOVERY_DELTA_ITERATION_185.md`

## Immediate next scientific priority — Iteration 186

Compute the full source-completed `QG-NL-EXP-001` lambda soft2 tangent at lambda=1 from the same fixed parent action, including the variation of the exponential form factor / covariant Box operator. Then add the frozen local compensation soft2 vector so all six K2 rows remain exactly calibrated. Project only that single conditioned nonlocal direction against the zero-K2 curvature-cubic rank-4 span and compare the residual to the frozen `5.2625580e-6` numerical envelope.

If the conditioned residual is sub-envelope, classify near-degeneracy/resolution insufficiency and widen the hard-row lever arm target-independently before any novelty promotion. If resolvable, continue to AS and C3 relation quotients. No `ANSATZ-003`, Fisher or resources before full quotient survival.
