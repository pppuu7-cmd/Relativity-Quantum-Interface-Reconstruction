# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 182**

## Scientific state in one sentence

RQIR is in source-completed, two-point-amputated, Ward-subtracted transverse null-soft three-point space. Local C5 through dimension 12 occupies physics-aware rank 4/6; compatible massless-spin-2 C4 adds no independent direction and massive dRGT is protocol-incompatible; the fixed exponential nonlocal comparator remains unresolved because the present six-row lever arm is near-degenerate and, more fundamentally, the repository had not yet implemented an executable source-completed `W[K2]` / `P_T` subtraction for comparators with nonzero quadratic kernel.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged through Iteration 182. Do not raise readiness for workload alone.

## Frozen rules

- Repository/recovery is source of truth.
- Unsupported comparator coordinates are BLOCKED, never zero-filled.
- Hard consistency constraints precede profiling/Fisher.
- `ANSATZ-003` must not be created before a nonzero residual survives fixed C3/C4/C5/nonlocal/asymptotic-safety subtraction.
- Fisher/resources remain forbidden until then.
- Metric CTP convention: `h_±=r±a/2` with factorial-normalized cubic vertices.
- Conceptual soft coordinate: `B_T(i)=P_T[Gamma_arr(i)-W_i[K2]]` on the frozen physical null-soft plus-TT carrier.
- For any comparator with nonzero `K2`, `W[K2]` and `P_T` must be executable in the same source-completed convention before rank promotion.

## Retained authority

### Local C5 — Iteration 178

On the six frozen null-soft TT rows, the authorized cubic subset through dimension 12 reduces exactly to

`Riemann3_B_T * {1, (-q^2), (q^2)^2, (-q^2)^3}`

with physics-aware rank `4/6` and singular values

`[2.0192478812, 0.0752839640, 0.0037576657, 4.7032262e-5]`.

The frozen extrapolation/error envelope is `5.2625580e-6`. Ricci-chain soft columns are exact protocol zeros.

Retain `C5-NG-009`, `SOFT-NG-005`, `NUM-NG-001`.

### C4 — Iterations 179–180

Fixed dRGT at `m^2=0.04` is `BLOCKED_C4_NULL_SOFT_PROTOCOL_MISMATCH`; this is not a consistency FAIL. The strongest compatible local/unitary single-massless-spin-2 control merges with the C5 local-EFT soft boundary at the frozen order:

`rank(V_C5)=rank(V_C4_massless)=rank([V_C5,V_C4_massless])=4`.

Retain `C4-NG-011`, `SOFT-NG-007`, `NG-FUNNEL-038`.

### Fixed nonlocal comparator — Iterations 174, 181, 182

`QG-NL-EXP-001` is the frozen parent

`S ~ ∫ sqrt(-g) [R + G_mn F(Box) R^mn]`,

`F(Box)=(exp(-lambda Box)-1)/Box`, `lambda=1`.

Its tree cubic is fixed in principle and contains the required Frechet insertion `G1 deltaF R1`; propagator-only reasoning is insufficient.

Iteration 181 resolution audit:

- representative analytic exponential soft-limit shapes appended to the local rank-4 basis give fifth singular values only `4.19e-8` to `8.33e-7`;
- the largest is only `0.158` of the frozen Iteration-178 error envelope `5.2626e-6`;
- therefore the current six-row `q^2` lever arm nearly polynomializes those tested shapes below present numerical resolution.

Retain `NL-NG-004`, `NUM-NG-002`, `NG-FUNNEL-039`.

Iteration 182 definition audit:

The Iteration-175 implementation validates only the soft-Riemann gauge/scaling geometry. It did **not** implement an executable source-completed `W[K2]` or explicit numerical `P_T`.

This was safe for the local `R^3` operators because their operator-specific `K2=0`, hence `W[K2]=0` exactly. It is not safe for `QG-NL-EXP-001`, whose quadratic kernel is nonzero.

There is an exact transverse decomposition freedom

`W -> W + Rlin:C`,

`B -> B - C`,

which leaves the raw cubic vertex unchanged and is invisible to pure-gauge Ward tests because `Rlin[gauge]=0`.

Finite certificate:

- pure-gauge soft Riemann norm `1.5700924587e-16`;
- physical TT soft Riemann norm `2.0`;
- nonzero decomposition shift norm `0.2455605832`;
- compensated raw-vertex change `5.5511151231e-17`.

Therefore

`QG-NL-EXP-001 B_T = BLOCKED_EXECUTABLE_SOURCE_COMPLETED_WARD_SUBTRACTION_NOT_YET_FROZEN`.

Retain:

- `SOFT-NG-008 — TRANSVERSE_RIEMANN_SHIFT_IS_INVISIBLE_TO_WARD_CONSTRAINTS_UNTIL_W_K2_CONVENTION_IS_FIXED`;
- `NL-NG-005 — FULL_NONLOCAL_RAW_CUBIC_IS_NECESSARY_BUT_NOT_SUFFICIENT_FOR_B_T_WHEN_K2_IS_NONZERO`;
- `NG-FUNNEL-040 — EXECUTABLE_SOURCE_COMPLETED_WARD_SUBTRACTION_MUST_PRECEDE_NONLOCAL_OR_AS_B_T_RANK_PROMOTION`.

This is BLOCKED, not zero, not FAIL, and not exact comparator identity.

### C3

Supported lower-order PQCG pieces remain authoritative. Ordered metric-CTP/transverse completion remains `BLOCKED_C3_CTP_ORDERED_COMPLETION` because nonlinear conserved diffusion and an explicit MSR-to-metric-CTP map are not fixed.

### Asymptotic safety

Two-point spectral information is calibration/shared data. Real-time/source-completed three-point transverse completion remains BLOCKED. The executable Ward-subtraction map required by Iteration 182 must also be used before any AS `B_T` rank claim.

## Candidate state

There is still **no robust Candidate Gravity residual**. The two-dimensional algebraic complement after local C5/C4-boundary subtraction remains provisional.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Current authority files — Iteration 182

- `analysis/nonlocal_bt_ward_subtraction_gap_iteration182.py`
- `results/nonlocal_bt_ward_subtraction_gap_iteration182.json`
- `candidate_gravity/NONLOCAL_BT_WARD_SUBTRACTION_GAP_ITERATION182.md`
- `research_log/2026-08-31_iteration_182_nonlocal_bt_ward_subtraction_gap.md`
- `recovery/RECOVERY_DELTA_ITERATION_182.md`

## Immediate next scientific priority — Iteration 183

Freeze an **executable source-completed off-shell Ward projector** for one physical null soft graviton and two off-shell conserved-TT hard source legs.

Required order:

1. derive `W[K2]` from the same quadratic inverse kernel and physical metric/source coupling;
2. define the `O(k_soft^2)` transverse tensor complement/projector `P_T` on the same six frozen rows;
3. validate the exact source-completed Ward identity and field/source bookkeeping;
4. validate on EH/local cases with known limits;
5. only then compute the full `QG-NL-EXP-001` cubic tensor including the Frechet term and extract its physical `B_T`;
6. reuse the same projector for asymptotic safety;
7. preserve unsupported C3 ordered/transverse pieces as BLOCKED until explicitly closed.

No `ANSATZ-003`, Fisher or resources before a nonzero residual survives the full fixed comparator quotient.
