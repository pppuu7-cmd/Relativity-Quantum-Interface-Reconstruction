# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 201**

## Scientific state in one sentence

The supported hard-K2 family is structurally rank 7 for any seven distinct positive hard nodes, exact hard calibration removes the supported local-quadratic/nonlocal variations, and the surviving supported local C5 soft2 nuisance is rank 4; however its image is strongly dependent on the frozen TT-polarization protocol. Two independently prospectively frozen v3 protocols (`v3-A`, `v3-B`) have principal angles `[1.31°,70.60°,76.74°,83.66°]`. Iteration 201 therefore freezes a cross-polarization anti-overfitting gate: a future candidate must derive both protocol tangents from the same parent dynamics and same parameter convention and must leave a supported nonzero residual in each protocol separately. AS and C3 remain BLOCKED; no candidate residual exists yet.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` through Iteration 201. Do not increase readiness for workload, exact rank, complement dimension, conditioning improvements, or protocol multiplication alone.

## Frozen rules

- Repository/recovery is source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Exact hard constraints precede profiling/Fisher.
- Structural rank and finite-noise conditioning are separate gates.
- TT polarization is part of the observable row definition; deterministic seeds only make a chosen polarization reproducible.
- Alternate prospectively frozen polarization protocols may not be selected, reseeded, reweighted, or dropped after seeing candidate residuals.
- A future candidate must use one parent dynamics and one parameter convention across all frozen validation protocols.
- Do not create `ANSATZ-003` before a concrete residual survives fixed C3/C4/C5/nonlocal/AS subtraction and the frozen cross-polarization gate.
- Fisher/resources remain forbidden until then.

## Supported hard-K2 authority

For the local quadratic C5 directions plus the fixed nonlocal `QG-NL-EXP-001` lambda direction, the hard functions are

`[x,x^2,x^3,x^4,x^5,x^6,x^2 exp(x)]`.

After factoring the positive row factor x, the collocation family is

`{1,x,x^2,x^3,x^4,x^5,x exp(x)}`.

Its leading Wronskians are

`1,1,2,12,288,34560,34560(x+6)exp(x)`.

Hence the family is an extended complete Chebyshev system on `x>0`: any seven distinct positive hard nodes give exact rank 7. The old six-row local/nonlocal K2 compensation is finite-sample saturation, not theory identity.

Under exact hard calibration the supported hard-preserving parameter nullspace contains only the zero-K2 curvature-cubic C5 coefficients. This is an exact algebraic statement, not finite-noise identifiability.

## v3 hard geometry

A target-independent comparator-only conditioning design selected scale factors `0.80` and `1.40` on the six base hard q-vectors.

Hard x values:

`[0.324864,0.246656,0.27264,0.201792,0.256256,0.184448,0.994896,0.755384,0.83496,0.617988,0.784784,0.564872]`.

Relative to withheld-v2:

- raw hard-K2 condition improves by factor `3.2176`;
- column-normalized hard condition improves by factor `3.0705`;
- raw smallest singular value improves by factor `5.6670`.

The hard block remains near-degenerate. No Fisher/resource inference is authorized.

## External comparator authority boundaries

### Asymptotic safety

Current authority still does not supply the required Lorentzian/in-in source-completed off-shell three-graviton `O(k_soft^2)` relation in the same parent convention as K2.

Status: `BLOCKED_AS_REALTIME_RELATION_COMPLETION`, not zero and not FAIL.

### C3 PQCG

Current authority still does not fix the nonlinear metric-dependent conserved-diffusion response vertex/source-completed ordered soft2 metric relation required by RQIR.

Status: `BLOCKED_C3_CTP_ORDERED_COMPLETION`, not zero and not FAIL.

## v3-A / v3-B polarization authority — Iteration 200

A repository concurrency event produced two different deterministic seed streams on the same v3 hard-q geometry. Both were frozen before their own cubic C5 evaluation and neither used Candidate Gravity information. Preserve both as valid but distinct observable protocols.

### v3-A

Hourly automation branch, seed convention based at `197000/197500`.

- all 12 rows pass geometry-only TT conditioning;
- minimum partner margin `0.8106158577`;
- local zero-K2 C5 soft2 rank `4/12`;
- raw condition `1038.3957`;
- column-normalized condition `981.3573`.

### v3-B

Concurrent manual branch, seed convention based at `198000/198500`.

- all 12 rows pass the same acceptance class;
- minimum partner margin `0.9053777009`;
- local zero-K2 C5 soft2 rank `4/12`;
- raw condition `4837.9565`;
- column-normalized condition `4587.3371`.

Neither supersedes the other.

Principal angles between their rank-4 local-C5 nuisance images:

`[1.307416°,70.597675°,76.740447°,83.658828°]`.

Projector distances:

- Frobenius `2.37712349`;
- operator norm `0.993881845`.

Only one nuisance direction is nearly common; the other three are strongly rotated. The alternate-subspace union has rank 8 in the common 12-index representation, but this is a protocol-sensitivity diagnostic, **not** eight C5 theory parameters.

A diagnostic 24-row vertical stack using the same four C5 coefficients remains rank 4 with raw condition `1845.83` and column-normalized condition `1749.72`; it is not frozen as a replacement protocol.

Retain `PROTO-NG-007`, `C5-NG-018`, `REL-NG-013`, `NG-FUNNEL-054`.

## Iteration 201 — frozen cross-polarization robustness gate

Before any promotable candidate is instantiated, preserve `v3-A` and `v3-B` as separate validation protocols.

A future candidate must declare one parent dynamics and one candidate parameter convention and derive

`b_A = dY_A/dbeta | beta=0`,

`b_B = dY_B/dbeta | beta=0`

from that same dynamics and same `beta` convention. Independent `beta_A` and `beta_B` fits merely to force both protocols to pass are forbidden.

For each protocol separately:

1. construct only the physically authorized comparator/nuisance map in that protocol's row coordinates;
2. impose exact hard constraints before profiling/Fisher;
3. compute the supported quotient residual;
4. require a nonzero residual above the declared numerical/model error envelope.

Frozen classification rule:

- pass only A or only B -> `POLARIZATION_SPECIFIC_IDENTIFICATION_INSUFFICIENT_FOR_PROMOTION`;
- pass A and B while AS/C3 remain unresolved -> `CROSS_POLARIZATION_SUPPORTED_BUT_COMPARATOR_INCOMPLETE`;
- pass A and B after full fixed comparator closure -> eligible for later candidate consistency gates, not automatically new physics.

A future combined multi-setting protocol may be an additional validation layer but may not hide failure of the separately frozen A/B gate unless a new protocol version is preregistered before candidate construction.

Retain:

- `PROTO-NG-008 — CANDIDATE_PROMOTION_REQUIRES_SEPARATE_PASS_ON_TWO_PROSPECTIVELY_FROZEN_TT_POLARIZATION_PROTOCOLS`;
- `REL-NG-014 — SAME_PARENT_DYNAMICS_AND_SINGLE_PARAMETER_CONVENTION_MUST_GENERATE_BOTH_PROTOCOL_SPECIFIC_TANGENTS`;
- `NG-FUNNEL-055 — POLARIZATION_SPECIFIC_RESIDUAL_IS_NOT_A_ROBUST_CANDIDATE_GRAVITY_DISCRIMINATOR`;
- `NG-FUNNEL-056 — COMBINED_MULTI_SETTING_LIKELIHOOD_MAY_NOT_HIDE_FAILURE_OF_A_PREREGISTERED_CROSS_PROTOCOL_GATE`.

## Comparator state

- **C5 local:** rank 4 in both v3-A and v3-B, with strongly rotated nuisance images.
- **C4:** compatible massless-spin-2 boundary remains inside local C5 at frozen scope; nonzero-mass dRGT remains null-soft protocol-incompatible.
- **Nonlocal:** fixed lambda hard direction is structurally independent of the local polynomial family for >=7 distinct positive nodes and is removed by exact hard calibration.
- **AS:** `BLOCKED_AS_REALTIME_RELATION_COMPLETION`.
- **C3:** `BLOCKED_C3_CTP_ORDERED_COMPLETION`.

## Candidate state

No robust Candidate Gravity residual exists yet.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Latest authority files

- `analysis/withheld_v2_supported_joint_quotient_iteration195.py`
- `results/withheld_v2_supported_joint_quotient_iteration195.json`
- `analysis/withheld_v2_structural_rank_theorem_iteration196.py`
- `results/withheld_v2_structural_rank_theorem_iteration196.json`
- `analysis/withheld_v3_k2_conditioning_design_iteration197.py`
- `results/withheld_v3_k2_conditioning_design_iteration197.json`
- `results/withheld_v3_polarization_freeze_iteration197.json`  # v3-A
- `results/withheld_v3_local_c5_soft2_iteration197.json`       # v3-A
- `results/preregistered_withheld_v3_polarization_iteration198.json` # v3-B
- `results/withheld_v3_local_c5_soft2_iteration199.json`             # v3-B
- `analysis/v3_polarization_branch_reconciliation_iteration200.py`
- `results/v3_polarization_branch_reconciliation_iteration200.json`
- `recovery/RECOVERY_DELTA_ITERATION_200.md`
- `candidate_gravity/CROSS_POLARIZATION_ROBUSTNESS_GATE_ITERATION201.md`
- `research_log/2026-08-31_iteration_201_cross_polarization_gate.md`
- `recovery/RECOVERY_DELTA_ITERATION_201.md`

## Immediate next scientific priority — Iteration 202

Return to the remaining comparator-foundation gap while preserving the frozen cross-polarization gate:

1. continue fixed AS real-time/source-completed authority audit;
2. continue fixed C3 nonlinear ordered-response authority/derivation audit;
3. if exact missing rows remain unavailable, investigate only scientifically derived bounded comparator relations from the parent dynamics — never broad class masks and never zero-filling;
4. independently derive protocol-level numerical/model error envelopes needed eventually to decide `r_A!=0` and `r_B!=0`, but do not run Fisher/resources;
5. do not create `ANSATZ-003` until a concrete target survives both polarization protocols and the unresolved AS/C3 issue is scientifically bounded.
