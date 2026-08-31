# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 181**

## Scientific state in one sentence

RQIR is in source-completed, two-point-amputated, Ward-subtracted transverse null-soft three-point space. Local C5 through dimension 12 gives a physics-aware rank-4 span on six `B_T` rows; compatible local massless-spin-2 C4 merges with that boundary, fixed massive dRGT is null-soft protocol-incompatible, and the fixed exponential nonlocal comparator is now known to face both an unimplemented tensor-Frechet projection and a strong six-row resolution near-degeneracy.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged through Iteration 181. Do not raise readiness for workload alone.

## Frozen rules

- Repository/recovery is source of truth.
- Unsupported comparator coordinates are BLOCKED, never zero-filled.
- Hard consistency constraints precede profiling/Fisher.
- `ANSATZ-003` must not be created before a nonzero residual survives fixed C3/C4/C5/nonlocal/asymptotic-safety subtraction.
- Fisher/resources remain forbidden until then.
- Metric CTP convention: `h_±=r±a/2` with factorial-normalized cubic vertices.
- `B_T(i)=P_T[Gamma_arr(i)-W_i[K2]]` on the frozen physical null-soft plus-TT carrier.

## Retained authority

### Local C5 — Iteration 178

On the six frozen null-soft TT rows, the authorized cubic subset through dimension 12 reduces exactly to

`Riemann3_B_T * {1, (-q^2), (q^2)^2, (-q^2)^3}`

with physics-aware rank `4/6` and singular values

`[2.0192478812, 0.0752839640, 0.0037576657, 4.7032262e-5]`.

The frozen extrapolation/error envelope is `5.2625580e-6`. Ricci-chain soft columns are exact protocol zeros. Retain `C5-NG-009`, `SOFT-NG-005`, `NUM-NG-001`.

### C4 — Iterations 179–180

Fixed dRGT at `m^2=0.04` is `BLOCKED_C4_NULL_SOFT_PROTOCOL_MISMATCH`; this is not a consistency FAIL. The strongest compatible local/unitary single-massless-spin-2 control merges with the C5 local-EFT soft boundary at the frozen order:

`rank(V_C5)=rank(V_C4_massless)=rank([V_C5,V_C4_massless])=4`.

Retain `C4-NG-011`, `SOFT-NG-007`, `NG-FUNNEL-038`.

### Fixed nonlocal comparator — Iterations 174 and 181

`QG-NL-EXP-001` is the frozen parent

`S ~ ∫ sqrt(-g) [R + G_mn F(Box) R^mn]`,

`F(Box)=(exp(-lambda Box)-1)/Box`, `lambda=1` in the current certificate.

Its tree cubic is fixed in principle and contains the required Frechet insertion `G1 deltaF R1`; propagator-only reasoning is insufficient.

Iteration 181 audited the exact six-row `q^2` lever arm against representative analytic exponential soft-limit shapes. When appended to the local rank-4 basis, tested fifth singular values lie between `4.19e-8` and `8.33e-7`; the maximum is only `0.158` of the frozen Iteration-178 numerical envelope. Therefore these tested analytic shapes are near-degenerate with the local polynomial span at present resolution.

Classification:

- `NL-NG-004 — CURRENT_SIX_ROW_Q2_LEVER_ARM_NEARLY_POLYNOMIALIZES_TESTED_EXPONENTIAL_FORMFACTOR_SHAPES_BELOW_B_T_ERROR_ENVELOPE`;
- `NUM-NG-002 — NONLOCAL_FIFTH_SINGULAR_VALUE_BELOW_FROZEN_EXTRAPOLATION_ENVELOPE_IS_NOT_A_PHYSICAL_RANK_CERTIFICATE`;
- `NG-FUNNEL-039 — FULL_TENSOR_FRECHET_PROJECTION_AND_RESOLUTION_MARGIN_ARE_BOTH_REQUIRED_BEFORE_NONLOCAL_B_T_RANK_PROMOTION`.

The exact nonlocal `B_T` column remains

`BLOCKED_NONLOCAL_B_T_TENSOR_FRECHET_IMPLEMENTATION_NOT_ZERO`.

This is not exact comparator identity and not consistency FAIL.

### C3

Supported lower-order PQCG pieces remain authoritative. Ordered metric-CTP/transverse completion remains `BLOCKED_C3_CTP_ORDERED_COMPLETION` because nonlinear conserved diffusion and an explicit MSR-to-metric-CTP map are not fixed.

### Asymptotic safety

Two-point spectral information is calibration/shared data. Real-time/source-completed three-point transverse completion remains BLOCKED.

## Candidate state

There is still **no robust Candidate Gravity residual**. The two-dimensional algebraic complement after local C5/C4-boundary subtraction is provisional and cannot be promoted while nonlocal/AS/C3 completion is unresolved.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Current authority files — Iteration 181

- `analysis/nonlocal_soft_transverse_resolution_audit_iteration181.py`
- `results/nonlocal_soft_transverse_resolution_audit_iteration181.json`
- `candidate_gravity/NONLOCAL_SOFT_TRANSVERSE_RESOLUTION_AUDIT_ITERATION181.md`
- `research_log/2026-08-31_iteration_181_nonlocal_soft_transverse_resolution_audit.md`
- `recovery/RECOVERY_DELTA_ITERATION_181.md`

## Immediate next scientific priority — Iteration 182

Implement the complete rank-2 tensor cubic `B_T` projection of `QG-NL-EXP-001` from the frozen parent action on the exact six rows. Include `G2 F0 R1`, `G1 F0 R2`, measure/contraction terms, and especially `G1 deltaF R1` with the exact Frechet divided-difference kernel. Compare any new singular direction against the frozen `5.2626e-6` error envelope before rank promotion. If the exact column is also sub-envelope, freeze a target-independent wider hard-`q^2` protocol before any novelty claim. No `ANSATZ-003`, Fisher or resources before full comparator quotient survival.
