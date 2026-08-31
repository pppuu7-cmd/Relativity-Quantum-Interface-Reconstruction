# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 197**

## Scientific state in one sentence

The joint source-completed relation `Y=(K2_rows,S_soft2_full_rows)` remains authoritative. The supported hard-K2 family `[x,...,x^6,x^2 exp(x)]` has structural rank 7 for any seven distinct positive hard nodes, so exact hard calibration removes supported quadratic/nonlocal variations; the surviving supported conditional soft2 nuisance is the structurally row-robust rank-4 zero-K2 local C5 curvature-cubic sector. Iteration 197 prospectively improves K2 conditioning with a target-independent v3 geometry, but AS and C3 ordered nonlinear relation data remain BLOCKED, so there is still no Candidate Gravity residual.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` through Iteration 197. Do not raise readiness for workload, algebraic complement dimension, exact rank, or conditioning improvements alone.

## Frozen rules

- Repository/recovery is source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Exact hard constraints precede profiling/Fisher.
- Structural rank and finite-noise conditioning are separate gates.
- Comparator-conditioning design may not use future candidate residuals.
- Do not create `ANSATZ-003` before a concrete residual survives fixed C3/C4/C5/nonlocal/AS subtraction and prospectively frozen robustness rows.
- Fisher/resources remain forbidden until then.
- For nonzero-K2 models use joint `(K2,S_soft2_full)`; internal Ward/transverse repartition is not an observable.
- Failed preregistered rows/protocols remain recorded as failures; no silent reseeding or deletion.

## Historical discovery authority

The original six-row protocol established the local C5 zero-K2 curvature-cubic span and the fixed nonlocal `QG-NL-EXP-001` comparator. Six rows were partially finite-sample saturated: local quadratic `[x,...,x^6]` could exactly compensate the nonlocal lambda K2 tangent. Iteration 186 nevertheless showed a large conditioned nonlocal soft2 comparator direction outside the local six-row C5 span. This remains discovery/comparator authority, not candidate novelty.

Detailed authority is preserved in recovery deltas through Iteration 186.

## External comparator authority boundaries

### Asymptotic safety

Modern authority supports Euclidean momentum-dependent multi-graviton/effective-action information, Lorentzian graviton spectral information, and Lorentzian/timelike scalar–graviton vertex information. It still does not provide the required Lorentzian/in-in source-completed off-shell three-graviton `O(k_soft^2)` relation in the same parent convention as K2.

Status: `BLOCKED_AS_REALTIME_RELATION_COMPLETION`, not zero and not FAIL.

### C3 PQCG

Published authority supports nonlinear covariant OM probability dynamics, symmetric post-Gaussian structure, and a linearized gravitational MSR/JD construction, but not the nonlinear metric-dependent conserved diffusion response vertex/source-completed ordered soft2 metric relation required by RQIR.

Status: `BLOCKED_C3_CTP_ORDERED_COMPLETION`, not zero and not FAIL.

## Prospective withheld-v2 authority — Iterations 190–196

`RQIR-WITHHELD-NULLSOFT-12-v1` was frozen before candidate testing using scale factors `0.75` and `1.25`. Iteration 191 found

`rank([x,...,x^6])=6`,

`rank([x,...,x^6,x^2 exp(x)])=7`,

proving that the old six-row exact local compensation was finite-sample saturation rather than a theory identity.

Iteration 192 preserved a preregistered cubic polarization-conditioning failure rather than silently repairing it. Iteration 193 froze `RQIR-WITHHELD-NULLSOFT-12-v2` with a uniform geometry-only seed acceptance rule; all 12 rows pass.

Iteration 194 computed the zero-K2 local C5 curvature-cubic soft2 basis on v2:

- rank `4/12`;
- singular values `[1.1350290414,0.1259090262,0.0173586351,0.0011354930]`;
- condition number `999.5914`.

Iteration 195 constructed the supported joint quotient. With

`theta=(c1,...,c6,lambda_NL,g0,...,g3)`

and hard matrix

`A_full=[A7,0_(12x4)]`, `A7=[x,...,x^6,x^2 exp(x)]`,

`rank(A7)=7/7`. The exact 11-parameter hard nullity is 4 and is supported only on the zero-K2 curvature-cubic parameters `g0..g3`. Therefore the supported conditional soft2 nuisance after exact hard calibration is exactly the local rank-4 C5 basis. The supported soft2 complement dimension is 8 before blocked AS/C3 completion.

Iteration 196 promoted the hard-rank observation to a structural theorem. After factoring x>0, the functions are

`{1,x,x^2,x^3,x^4,x^5,x exp(x)}`

with leading Wronskians

`1,1,2,12,288,34560,34560(x+6)exp(x)`.

Thus the family is an extended complete Chebyshev system on x>0: any seven distinct positive hard nodes give exact rank 7. The conditional soft2 basis is `diag(r0)[1,-x,x^2,-x^3]`; because current x values are distinct and r0 values nonzero, any four current rows have rank 4 by the Vandermonde determinant.

Critical guardrail: exact rank does not imply good numerical conditioning.

## Iteration 197 — target-independent hard-K2 conditioning design

A new K2-only prospective geometry is frozen **before any cubic or candidate evaluation**:

`RQIR-WITHHELD-NULLSOFT-12-v3-K2-FROZEN`.

Design rule:

- reuse the same six base hard q-vectors;
- low scale grid `0.60,0.65,...,0.90`;
- high scale grid `1.10,1.15,...,1.40`;
- internal hard-node window `0.10 <= x=q^2 <= 1.00`;
- objective: minimize the column-normalized condition number of `[x,...,x^6,x^2 exp(x)]`;
- tie-break: minimize raw condition number;
- no candidate residual, candidate amplitude, soft2 value, or left-null enters the design.

Best of 49 valid grid pairs:

`low_scale=0.80`, `high_scale=1.40`.

Selected hard x values:

`[0.324864,0.246656,0.27264,0.201792,0.256256,0.184448,0.994896,0.755384,0.83496,0.617988,0.784784,0.564872]`.

All hard/partner legs remain spacelike on the same 81-point `epsilon in [-0.01,0.01]` geometry window.

Conditioning relative to v2:

- raw condition `2.04935e7 -> 6.36910e6`, improvement factor `3.2176`;
- column-normalized condition `2.38767e7 -> 7.77614e6`, improvement factor `3.0705`;
- raw smallest singular value `1.39038e-7 -> 7.87933e-7`, gain factor `5.6670`.

Rank remains 7, but the block is still near-degenerate. This is not finite-noise identifiability.

Retain `NUM-NG-011`, `PROTO-NG-004`, `NG-FUNNEL-051`.

## Comparator state

- **C5 local:** supported conditional zero-K2 curvature-cubic soft2 rank `4/12` on withheld-v2, structurally row-robust.
- **C4:** compatible massless-spin-2 boundary remains inside local C5 at frozen scope; nonzero-mass dRGT remains null-soft protocol-incompatible.
- **Nonlocal:** fixed lambda K2 direction is structurally exact-independent of the local polynomial hard family for any seven distinct positive nodes and is removed by exact hard calibration. Six-row conditioned soft2 must not be transferred to prospective blocks.
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
- `candidate_gravity/WITHHELD_V2_SUPPORTED_JOINT_QUOTIENT_ITERATION195.md`
- `recovery/RECOVERY_DELTA_ITERATION_195.md`

Iteration 196:
- `analysis/withheld_v2_structural_rank_theorem_iteration196.py`
- `results/withheld_v2_structural_rank_theorem_iteration196.json`
- `candidate_gravity/WITHHELD_V2_STRUCTURAL_RANK_THEOREM_ITERATION196.md`
- `recovery/RECOVERY_DELTA_ITERATION_196.md`

Iteration 197:
- `analysis/withheld_v3_k2_conditioning_design_iteration197.py`
- `results/withheld_v3_k2_conditioning_design_iteration197.json`
- `candidate_gravity/WITHHELD_V3_K2_CONDITIONING_DESIGN_ITERATION197.md`
- `research_log/2026-08-31_iteration_197_withheld_v3_k2_conditioning.md`
- `recovery/RECOVERY_DELTA_ITERATION_197.md`

## Immediate next scientific priority — Iteration 198

Freeze the **v3 cubic polarization geometry before any cubic evaluation**:

1. preserve v2 and v3-K2 as immutable authority;
2. apply one uniform deterministic geometry-only seed acceptance rule to all 12 v3 rows;
3. require hard and partner TT norms to stay away from normalization zeros across the full soft epsilon window;
4. freeze the selected seeds before computing any v3 curvature-cubic or nonlocal soft2 column;
5. then evaluate the zero-K2 C5 soft2 basis on v3 and compare conditioning/quotient geometry with v2;
6. keep AS/C3 BLOCKED and do not create `ANSATZ-003` or start Fisher/resources.
