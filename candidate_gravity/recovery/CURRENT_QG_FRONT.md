# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 200**

## Scientific state in one sentence

The supported hard-K2 family `[x,...,x^6,x^2 exp(x)]` is structurally rank 7 for any seven distinct positive hard nodes, so exact hard calibration removes the supported local-quadratic/nonlocal parameter variations; the surviving supported local C5 soft2 nuisance is rank 4, but Iteration 200 shows that its image depends strongly on the prospectively frozen TT-polarization protocol. Two independently valid v3 polarization protocols (`v3-A`, `v3-B`) have principal angles `[1.31°,70.60°,76.74°,83.66°]`, so future Candidate Gravity residuals must be polarization-robust rather than optimized against one favorable TT basis. AS and C3 remain BLOCKED; no candidate residual exists yet.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` through Iteration 200. Do not raise readiness for workload, exact rank, complement dimension, conditioning improvements, or protocol multiplication alone.

## Frozen rules

- Repository/recovery is source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Exact hard constraints precede profiling/Fisher.
- Structural rank and finite-noise conditioning are separate gates.
- TT polarization is part of the observable row definition; deterministic seeds only make a chosen polarization reproducible.
- Alternate prospectively frozen polarization protocols may not be selected post hoc after seeing a candidate residual.
- Do not create `ANSATZ-003` before a concrete residual survives fixed C3/C4/C5/nonlocal/AS subtraction and prospectively frozen cross-protocol robustness.
- Fisher/resources remain forbidden until then.
- For nonzero-K2 models use joint `(K2,S_soft2_full)`; internal Ward/transverse repartition is not an observable.
- Failed preregistered rows/protocols remain recorded as failures; no silent reseeding or deletion.

## External comparator authority boundaries

### Asymptotic safety

Modern authority supports Euclidean momentum-dependent multi-graviton/effective-action information, Lorentzian graviton spectral information, and Lorentzian/timelike scalar–graviton vertex information, but not the required Lorentzian/in-in source-completed off-shell three-graviton `O(k_soft^2)` relation in the same parent convention as K2.

Status: `BLOCKED_AS_REALTIME_RELATION_COMPLETION`, not zero and not FAIL.

### C3 PQCG

Published authority supports nonlinear covariant OM probability dynamics, symmetric post-Gaussian structure, and a linearized gravitational MSR/JD construction, but not the nonlinear metric-dependent conserved-diffusion response vertex/source-completed ordered soft2 metric relation required by RQIR.

Status: `BLOCKED_C3_CTP_ORDERED_COMPLETION`, not zero and not FAIL.

## Prospective hard/soft authority through Iteration 196

The prospectively frozen 12-row program established:

- old six-row nonlocal K2 compensation was finite-sample saturation, not theory identity;
- on >=7 distinct positive hard nodes the supported hard functions are structurally rank 7;
- after exact hard calibration the supported parameter nullspace contains only zero-K2 curvature-cubic C5 coefficients;
- local zero-K2 C5 soft2 map has rank 4 on the frozen prospective rows;
- exact rank remains separate from conditioning.

Hard structural theorem: after factoring positive x, the functions

`{1,x,x^2,x^3,x^4,x^5,x exp(x)}`

have leading Wronskians

`1,1,2,12,288,34560,34560(x+6)exp(x)`.

Hence any seven distinct positive x nodes give rank 7.

## v3 hard geometry — Iteration 197

A target-independent two-scale design used only supported hard-K2 conditioning and no candidate information. Selected scales:

`0.80` and `1.40`.

Hard x values:

`[0.324864,0.246656,0.27264,0.201792,0.256256,0.184448,0.994896,0.755384,0.83496,0.617988,0.784784,0.564872]`.

Relative to v2:

- raw hard-K2 condition improves by factor `3.2176`;
- column-normalized hard condition improves by factor `3.0705`;
- raw smallest singular value improves by factor `5.6670`.

The hard block remains near-degenerate and this is not finite-noise identifiability.

## Concurrent prospectively frozen v3 polarization protocols

A repository concurrency event produced two different deterministic seed streams on the same v3 hard q geometry. Both streams were frozen before their own cubic C5 evaluations and neither used a Candidate Gravity target. Therefore both are retained as legitimate but distinct observable protocols.

### v3-A — hourly automation branch

Seed convention based at `197000/197500`.

All 12 rows pass the geometry-only TT normalization rule. Minimum partner margin `0.8106158577`.

Local zero-K2 C5 soft2:

- rank `4/12`;
- raw condition `1038.3957`;
- column-normalized condition `981.3573`.

### v3-B — concurrent manual branch

Seed convention based at `198000/198500`.

All 12 rows pass the same acceptance class. Minimum partner margin `0.9053777009`.

Local zero-K2 C5 soft2:

- rank `4/12`;
- raw condition `4837.9565`;
- column-normalized condition `4587.3371`.

Neither branch supersedes the other.

## Iteration 200 — polarization branch reconciliation

Let `Q_A,Q_B` span the two rank-4 local-C5 nuisance images in their common twelve-row index representation. Principal angles are

`[1.307416°,70.597675°,76.740447°,83.658828°]`.

Principal cosines:

`[0.99973966,0.33219941,0.22936268,0.11044853]`.

Projector distances:

- `||P_A-P_B||_F = 2.37712349`;
- `||P_A-P_B||_2 = 0.993881845`.

Thus only one C5 direction is nearly common; the other three are strongly rotated by the change in TT polarization settings.

The horizontal union of the two alternate 4D subspaces has rank 8 in the common twelve-index representation. This is **not** eight independent C5 theory parameters; it quantifies protocol sensitivity of the four-parameter image.

If A and B were both measured as separate 24 rows with the same four coefficients, the vertical-stack diagnostic remains rank 4 with raw condition `1845.83` and column-normalized condition `1749.72`. This 24-row construction is diagnostic only and is not yet frozen as a new protocol.

Retain:

- `PROTO-NG-007 — ADMISSIBLE_TT_POLARIZATION_SETTINGS_DEFINE_DISTINCT_OBSERVABLE_PROTOCOLS_AND_MAY_NOT_BE_TREATED_AS_INTERCHANGEABLE_NUMERICAL_SEEDS`;
- `C5-NG-018 — TWO_PROSPECTIVELY_FROZEN_V3_POLARIZATION_PROTOCOLS_BOTH_HAVE_RANK4_BUT_THEIR_LOCAL_C5_NUISANCE_SUBSPACES_ARE_STRONGLY_ROTATED`;
- `REL-NG-013 — PRINCIPAL_ANGLES_SHOW_ONLY_ONE_NEAR_COMMON_C5_DIRECTION_BETWEEN_V3_A_AND_V3_B`;
- `NG-FUNNEL-054 — COMPARATOR_QUOTIENT_AUTHORITY_MUST_INCLUDE_POLARIZATION_SETTINGS_AS_PART_OF_THE_ROW_DEFINITION_BEFORE_RESIDUAL_TESTING`.

## Comparator state

- **C5 local:** rank 4 in both v3-A and v3-B, but nuisance images are strongly protocol-dependent.
- **C4:** compatible massless-spin-2 boundary remains inside local C5 at frozen scope; nonzero-mass dRGT remains null-soft protocol-incompatible.
- **Nonlocal:** fixed lambda K2 direction is structurally independent of the local polynomial hard family for >=7 distinct positive nodes and is removed by exact hard calibration.
- **AS:** `BLOCKED_AS_REALTIME_RELATION_COMPLETION`.
- **C3:** `BLOCKED_C3_CTP_ORDERED_COMPLETION`.

## Candidate state

There is still **no robust Candidate Gravity residual**.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Current authority files

Iteration 195:
- `analysis/withheld_v2_supported_joint_quotient_iteration195.py`
- `results/withheld_v2_supported_joint_quotient_iteration195.json`
- `recovery/RECOVERY_DELTA_ITERATION_195.md`

Iteration 196:
- `analysis/withheld_v2_structural_rank_theorem_iteration196.py`
- `results/withheld_v2_structural_rank_theorem_iteration196.json`
- `recovery/RECOVERY_DELTA_ITERATION_196.md`

Iteration 197 hard geometry:
- `analysis/withheld_v3_k2_conditioning_design_iteration197.py`
- `results/withheld_v3_k2_conditioning_design_iteration197.json`

v3-A authority:
- `results/withheld_v3_polarization_freeze_iteration197.json`
- `results/withheld_v3_local_c5_soft2_iteration197.json`

v3-B authority:
- `results/preregistered_withheld_v3_polarization_iteration198.json`
- `results/withheld_v3_local_c5_soft2_iteration199.json`
- `recovery/RECOVERY_DELTA_ITERATION_198.md`
- `recovery/RECOVERY_DELTA_ITERATION_199.md`

Iteration 200 reconciliation:
- `analysis/v3_polarization_branch_reconciliation_iteration200.py`
- `results/v3_polarization_branch_reconciliation_iteration200.json`
- `candidate_gravity/V3_POLARIZATION_BRANCH_RECONCILIATION_ITERATION200.md`
- `research_log/2026-08-31_iteration_200_v3_polarization_reconciliation.md`
- `recovery/RECOVERY_DELTA_ITERATION_200.md`

## Immediate next scientific priority — Iteration 201

Freeze a **cross-polarization robustness gate** before any Candidate Gravity target is instantiated:

1. preserve v3-A and v3-B unchanged as two independent validation protocols;
2. define the rule that a future supported candidate tangent must be generated from the same parent dynamics on both protocols and must leave a nonzero quotient residual in each separately after the applicable fixed comparator subtraction;
3. forbid choosing the polarization protocol after seeing candidate residual size;
4. decide prospectively whether a 24-row dual-setting protocol should be an additional validation layer or only a diagnostic; do not infer extra C5 parameters from alternate-protocol union rank;
5. keep AS/C3 explicitly BLOCKED and continue authority searches independently;
6. do not create `ANSATZ-003` or start Fisher/resources until a concrete residual survives the supported cross-polarization gate and unresolved AS/C3 are scientifically bounded.
