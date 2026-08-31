# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 177**

## Scientific state in one sentence

The search is now in source-completed, two-point-amputated, Ward-subtracted transverse soft three-point space. Iteration 177 constructs the first genuine action-level local-C5 `B_T` columns and finds that the physical null-TT soft protocol annihilates `Tr(Ricci^3)` exactly while cyclic `Riemann^3` survives, giving rank `1/2`; this is regime-specific non-identifiability, not operator absence or consistency failure.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged through Iteration 177. Comparator geometry improved, but no full comparator-subtracted residual or parent dynamics exists.

## Frozen rules

- Repository files and recovery deltas are source of truth.
- Unsupported comparator coordinates are BLOCKED, never zero-filled.
- Hard consistency constraints precede profiling/Fisher.
- `ANSATZ-003` must not be created before a nonzero residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety quotient.
- Fisher/resources remain forbidden until then.
- Preserve nomenclature: Iteration-166 `A_odd` is linear `chi1R`; Iteration-171 CTP uses `h_±=r±a/2` and factorial-normalized vertices; retain `PROVENANCE-CORR-001`.

## Historical authority retained

### Spacelike TT through Iteration 165

The dimension-12 local C5 basis spans the frozen 12-row spacelike protocol (`rank=12/12`) and absorbs corrected dRGT tangents. This is finite-protocol saturation, not an exact theory identity.

### Timelike absorptive Iterations 166–170

Local Hermitian tree EFT is absorptively zero off pole; leading massless one-loop C5 is constant shape; the conservative next massless envelope is `span{x,x log x}`. Standalone positive linear spectral novelty is closed by exact C4 mediator-continuum equivalence.

### Linked CTP Iterations 171–174

After two-point amputation external-leg dressing is removed. Generic closed-unitary cubic structure obeys `Gamma_aar=0`, `Gamma_aaa=Gamma_arr/4`; this is shared quantum structure. PQCG ordered cubic completion remains `BLOCKED_C3_CTP_ORDERED_COMPLETION`. The fixed exponential nonlocal parent `QG-NL-EXP-001` contains a genuine Frechet operator-insertion cubic term, but the old coarse unitary+Ward relation map annihilates arbitrary closed-unitary diffeomorphic tree amplitudes, so scalar WardLock is insufficient.

### Iteration 175 — soft transverse relation space

Freeze

`Gamma3_soft = W[K2] + Rlin_soft : B3 + higher-soft-order`.

`W[K2]` is shared Ward/covariantization structure fixed by the same quadratic kernel. The independent physical carrier is the transverse/nonminimal `O(k_soft^2)` structure. Define six frozen relation rows

`B_T(i)=P_T[Gamma_arr(i)-W_i[K2]]`.

### Iteration 176 — protocol compatibility

Finite off-shell Iteration-150 curvature-cubic numbers do not determine the soft2 coefficient. The exact counterfamily `f_c(eps)=f0(eps)+c eps^2(1-eps)^2` preserves soft0, soft1 and one finite point while shifting soft2. Therefore old finite numbers cannot be relabeled as `B_T`.

## Iteration 177 — first action-level local-C5 B_T columns

Reuse the same covariant parent operators from Iteration 150, but with the new frozen physical soft family

`k1=eps*(1,0,0,1)`, `k2=q_i`, `k3=-q_i-k1`,

for six target-independent hard rows and the Iteration-175 null plus-TT soft polarization.

For both curvature-cubic directions the operator expansion starts at cubic order around Minkowski, hence `K2_operator=0` and their operator-specific Ward subtraction is exactly `W[K2]=0`. Pure-gauge replacement of the soft leg leaves max absolute residue `2.82e-22`.

For the physical null-TT soft leg,

`R_mn^(1)=0`,

while `||R_mnrs^(1)||=2` at unit soft momentum. Therefore

`B_T[Tr(Ricci^3)] = 0`

**exactly in this protocol**, while cyclic `Riemann^3` gives

`[-1.6411697072, 0.0638588272, 0.8548821188, -0.1705521567, -0.3261917311, -0.1655609265]`.

Maximum independent extrapolation discrepancy is `5.27e-6`.

The first local-C5 soft-transverse matrix therefore has

`rank = 1/2`, singular values `[1.8950564368, 0]`.

Classification: **regime-specific non-identifiability**. The Ricci-cubed operator is not absent: its finite off-shell Iteration-150 column remains nonzero and authoritative in that separate protocol.

Retain:

- `C5-NG-008 — NULL_TT_SOFT_PROTOCOL_ANNIHILATES_RICCI_CUBED_B_T_BUT_NOT_CYCLIC_RIEMANN_CUBED`;
- `SOFT-NG-004 — FIRST_ACTION_LEVEL_LOCAL_C5_B_T_BASIS_HAS_RANK_ONE_ON_SIX_NULL_SOFT_TT_ROWS`;
- `NG-FUNNEL-037 — PROTOCOL_ZERO_FROM_ONSHELL_SOFT_RICCI_IS_REGIME_SPECIFIC_NOT_OPERATOR_ABSENCE`.

## Comparator status

### C3

Lower-order supported pieces remain authoritative. Ordered metric-CTP cubic and transverse `B_T` completion remain BLOCKED.

### C4

Fixed dRGT remains a scoped comparator. A fixed parent action-level projection into the new `B_T` rows is still required.

### C5

First action-level `B_T` direction is now real. The local basis is incomplete beyond the two curvature-cubic operators and must be extended target-independently through the already frozen EFT truncation before any residual claim.

### Nonlocal

`QG-NL-EXP-001` fixes its tree cubic in principle, including the Frechet insertion. Its `B_T` projection is pending after the finite local C5 basis.

### Asymptotic safety

Two-point spectral information is calibrated external-leg data. Real-time/source-completed three-point transverse completion remains BLOCKED.

## Candidate state

There is still **no robust Candidate Gravity residual**.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Current Iteration-177 authority files

- `analysis/c5_soft_transverse_columns_iteration177.py`;
- `results/c5_soft_transverse_columns_iteration177.json`;
- `candidate_gravity/C5_SOFT_TRANSVERSE_COLUMNS_ITERATION177.md`;
- `research_log/2026-08-31_iteration_177_c5_soft_transverse_columns.md`;
- `recovery/RECOVERY_DELTA_ITERATION_177.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION177.md`.

## Immediate next scientific priority — Iteration 178

Complete the target-independent local-C5 `B_T` basis through the already frozen EFT truncation as far as action-level soft projections are supported.

Required order:

1. derive derivative/curvature-cubic soft columns from their parent actions, prioritizing directions that can survive a null TT soft leg;
2. keep the six Iteration-177 rows fixed and do not optimize against a target;
3. compute rank/SVD and classify exact protocol zeros versus genuine independent directions;
4. only after local C5 is finite, add fixed C4 and `QG-NL-EXP-001` transverse columns;
5. leave C3 ordered and AS real-time columns BLOCKED unless explicitly derived;
6. no `ANSATZ-003`, Fisher or resources until a nonzero residual survives the full fixed comparator quotient.
