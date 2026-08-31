# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 180**

## Scientific state in one sentence

The search is in source-completed, two-point-amputated, Ward-subtracted transverse null-soft three-point space. The frozen local-C5 cubic subset through dimension 12 occupies a physics-aware rank-4 span on six `B_T` rows; fixed nonzero-mass dRGT is physically incompatible with the null-soft pole, while the strongest compatible local/unitary massless-spin-2 C4 control merges exactly with the same C5 soft boundary at the frozen order. The next discriminator is the fixed covariant nonlocal parent action.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged through Iteration 180. Do not raise readiness for workload alone.

## Frozen rules

- Repository/recovery is source of truth.
- Unsupported comparator coordinates are BLOCKED, never zero-filled.
- Hard consistency constraints precede profiling/Fisher.
- `ANSATZ-003` must not be created before a nonzero residual survives fixed C3/C4/C5/nonlocal/asymptotic-safety subtraction.
- Fisher/resources remain forbidden until then.
- Iteration-166 `A_odd` means the frequency-odd imaginary part of linear `chi1R`.
- Iteration-171 metric CTP convention is `h_±=r±a/2` with factorial-normalized cubic vertices.
- Retain `PROVENANCE-CORR-001`.

## Historical authority retained

### Spacelike TT through Iteration 165

The target-independent local C5 dimension-12 basis spans the frozen 12-row finite spacelike TT protocol (`rank=12/12`) and absorbs corrected dRGT tangents. This is finite-protocol saturation, not theory identity.

### Timelike absorptive Iterations 166–170

Local Hermitian tree EFT is absorptively zero off pole; leading massless one-loop C5 is constant shape; the conservative next massless envelope is `span{x,x log x}`. Standalone positive linear spectral novelty is closed by exact C4 positive-norm mediator-continuum equivalence.

### Linked CTP Iterations 171–174

Two-point amputation removes external-leg spectral dressing. Generic closed-unitary cubic structure obeys `Gamma_aar=0`, `Gamma_aaa=Gamma_arr/4`; this is shared quantum structure. PQCG ordered cubic completion is `BLOCKED_C3_CTP_ORDERED_COMPLETION`. The fixed exponential nonlocal parent contains a genuine Frechet operator-insertion cubic term, but the old coarse unitary+scalar-Ward relation map is too weak.

## Soft-transverse authority

### Iteration 175 — Ward-subtracted transverse carrier

Freeze

`Gamma3_soft = W[K2] + Rlin_soft : B3 + higher-soft-order`,

and six physical coordinates

`B_T(i)=P_T[Gamma_arr(i)-W_i[K2]]`.

The physical null plus-TT soft Riemann scales as `k_soft^2`; pure gauge gives zero.

### Iteration 176 — compatibility guard

Finite off-shell cubic response does not determine soft2. Old finite columns cannot be relabeled as `B_T`.

### Iteration 177 — first local-C5 action-level columns

On the six frozen rows, null-TT soft Ricci vanishes exactly. Hence `Ricci^3` is protocol-zero while cyclic `Riemann^3` survives. Two-operator rank is `1/2`.

### Iteration 178 — local-C5 dimension-12 completion

For the authorized cubic subset through dimension 12:

- `B_T[Ricci3]=0`;
- `B_T[RicciChain Box^n]=0`, `n=1,2,3`;
- `B_T[Ricci Ricci Riemann]=B_T[Riemann3]/12`;
- `B_T[RiemannChain Box^n]=(2/3)(-q_i^2)^n B_T[Riemann3]`, `n=1,2,3`.

The nine declared operator columns reduce to four physical basis vectors

`Riemann3 * {1, (-q^2), (q^2)^2, (-q^2)^3}`.

Physics-aware rank: `4/6`.

Singular values:

`[2.0192478812, 0.0752839640, 0.0037576657, 4.7032262e-5]`.

A fifth blind numerical singular value is below the `5.2626e-6` extrapolation/error envelope and is removed by exact identities.

Retain `C5-NG-009`, `SOFT-NG-005`, `NUM-NG-001`.

### Iteration 179 — dRGT protocol mismatch

`C4-DRGT-001` is frozen at `m^2=0.04`. At physical null soft momentum,

`K2_dRGT(k_soft)=k_soft^2+m^2=0.04 != 0`.

Thus the null leg is not the physical dRGT soft pole. Status:

`BLOCKED_C4_NULL_SOFT_PROTOCOL_MISMATCH`.

Do not zero-fill. Do not call this a consistency FAIL or exclusion of massive gravity. At formal `m^2->0` in the scoped TT block the dRGT-specific nonderivative cubic coefficient vanishes and the boundary approaches the shared EH TT structure, but this is not the frozen comparator point.

Retain `C4-NG-009`, `SOFT-NG-006`, `C4-NG-010`.

### Iteration 180 — compatible massless-spin-2 C4 boundary

Freeze the strongest compatible finite C4 control under scoped assumptions:

- one local unitary massless spin-2 field;
- conserved/universal stress coupling;
- self-consistent nonlinear parent dynamics;
- local EFT freedom through the same dimension-12 `B_T` order.

Soft-gauge consistency and standard consistent-deformation/self-coupling results place this control on the same Einstein-type/local-EFT massless-spin-2 boundary represented by C5. Local EFT modifications of sub-subleading soft structure are already admitted in C5.

Finite boundary certificate:

`rank(V_C5)=4`,

`rank(V_C4_massless)=4`,

`rank([V_C5,V_C4_massless])=4`,

with exact zero residual by the frozen boundary construction.

Classification:

`SCOPED_EXACT_BOUNDARY_MERGER_WITH_C5_LOCAL_MASSLESS_SPIN2_EFT`.

This does not exclude all C4 hidden sectors. It states that an otherwise identical consistent massless-spin-2 parent dynamics cannot be distinguished by merely relabeling it an ordinary mediator.

Retain:

- `C4-NG-011 — CONSISTENT_LOCAL_MASSLESS_SPIN2_MEDIATOR_CONTROL_MERGES_WITH_C5_SOFT_BOUNDARY_AT_FROZEN_ORDER`;
- `SOFT-NG-007 — SEMANTIC_GRAVITY_VS_MEDIATOR_LABEL_IS_NOT_AN_OPERATIONAL_DISCRIMINATOR_WHEN_PARENT_DYNAMICS_AND_SOURCE_MAP_COINCIDE`;
- `NG-FUNNEL-038 — C4_NULL_SOFT_CONTROL_SPLITS_INTO_PROTOCOL_INCOMPATIBLE_MASSIVE_CASE_OR_C5_BOUNDARY_MASSLESS_CASE_UNDER_SCOPED_ASSUMPTIONS`.

## Comparator status

### C3

Supported lower-order PQCG pieces remain authoritative. Ordered metric-CTP and transverse `B_T` completion remain BLOCKED because nonlinear conserved diffusion and an explicit MSR-to-metric-CTP map are not fixed.

### C4

For this physical null-soft carrier, fixed nonzero-mass dRGT is protocol-incompatible, while the strongest compatible local/unitary single-massless-spin-2 control adds no independent direction beyond C5 at the frozen order. Other mediator classes remain outside this scoped merger and require explicit testing if they can reproduce the tensor observable.

### C5

The authorized local cubic subset through dimension 12 occupies rank `4/6`.

### Nonlocal

`QG-NL-EXP-001` fixes its tree cubic in principle, including the Frechet insertion. Its `B_T` projection is now the immediate next gate.

### Asymptotic safety

Two-point spectral information is calibrated external-leg data. Real-time/source-completed three-point transverse completion remains BLOCKED.

## Candidate state

There is still **no robust Candidate Gravity residual**.

The two-dimensional algebraic complement after local C5/C4-boundary subtraction remains provisional.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Current authority files

### Iteration 178
- `analysis/c5_soft_transverse_dimension12_iteration178.py`
- `results/c5_soft_transverse_dimension12_iteration178.json`
- `candidate_gravity/C5_SOFT_TRANSVERSE_DIMENSION12_ITERATION178.md`
- `recovery/RECOVERY_DELTA_ITERATION_178.md`

### Iteration 179
- `analysis/c4_drgt_null_soft_compatibility_iteration179.py`
- `results/c4_drgt_null_soft_compatibility_iteration179.json`
- `candidate_gravity/C4_DRGT_NULL_SOFT_COMPATIBILITY_ITERATION179.md`
- `recovery/RECOVERY_DELTA_ITERATION_179.md`

### Iteration 180
- `analysis/c4_massless_spin2_boundary_iteration180.py`
- `results/c4_massless_spin2_boundary_iteration180.json`
- `candidate_gravity/C4_MASSLESS_SPIN2_BOUNDARY_ITERATION180.md`
- `research_log/2026-08-31_iteration_180_c4_massless_spin2_boundary.md`
- `recovery/RECOVERY_DELTA_ITERATION_180.md`

## Immediate next scientific priority — Iteration 181

Project the already-fixed covariant nonlocal comparator `QG-NL-EXP-001` into the exact same six null-soft TT `B_T` rows.

Required order:

1. derive/evaluate the cubic vertex from the full parent action, including the Frechet `delta F(Box)` insertion;
2. use the same source convention, soft family, hard rows and Ward subtraction;
3. test whether the fixed nonlocal column enlarges the current rank-4 C5/C4-boundary span to rank 5 or 6;
4. if its Lorentzian/retarded continuation is not fixed at the required order, mark the missing piece BLOCKED rather than zero-fill;
5. after nonlocal, address fixed asymptotic-safety real-time transverse completion and the C3 ordered/transverse boundary;
6. no `ANSATZ-003`, Fisher or resources until a nonzero residual survives the full fixed comparator quotient.
