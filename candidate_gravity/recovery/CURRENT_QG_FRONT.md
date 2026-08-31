# Candidate Gravity Current Front

**Updated:** 2026-09-01  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 197**

## Scientific state in one sentence

The joint source-completed relation `Y=(K2_rows,S_soft2_full_rows)` remains authoritative. The supported hard-K2 family `[x,...,x^6,x^2 exp(x)]` has structural rank 7 for any seven distinct positive hard nodes; Iteration 197 prospectively improves its finite-noise conditioning with target-independent v3 row scales, freezes one uniform polarization acceptance rule before cubic evaluation, and verifies that the supported zero-K2 local C5 curvature-cubic soft2 nuisance remains rank 4/12. AS and C3 ordered nonlinear relation data remain honest BLOCKED authorities, so no Candidate Gravity residual exists yet.

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
- Comparator-conditioning design may use fixed comparator geometry only, never future candidate residuals.
- Do not create `ANSATZ-003` before a concrete residual survives fixed C3/C4/C5/nonlocal/AS subtraction and prospectively frozen robustness rows.
- Fisher/resources remain forbidden until then.
- For nonzero-K2 models use joint `(K2,S_soft2_full)`; internal Ward/transverse repartition is not an observable.
- Failed preregistered rows/protocols remain recorded as failures; no silent reseeding or deletion.

## External comparator authority boundaries

### Asymptotic safety
Modern authority supports Euclidean momentum-dependent multi-graviton/effective-action information, Lorentzian graviton spectral information, and Lorentzian/timelike scalar–graviton vertex information, but not the required Lorentzian/in-in source-completed off-shell three-graviton `O(k_soft^2)` relation in the same parent convention as K2.

Status: `BLOCKED_AS_REALTIME_RELATION_COMPLETION`, not zero and not FAIL.

### C3 PQCG
Published authority supports nonlinear covariant OM probability dynamics, symmetric post-Gaussian structure, and a linearized gravitational MSR/JD construction, but not the nonlinear metric-dependent conserved diffusion response vertex/source-completed ordered soft2 metric relation required by RQIR.

Status: `BLOCKED_C3_CTP_ORDERED_COMPLETION`, not zero and not FAIL.

## Prospective withheld history — Iterations 190–196

- v1 was prospectively frozen before candidate testing; Iteration 191 showed `rank([x,...,x^6])=6` and `rank([x,...,x^6,x^2 exp(x)])=7`, proving the old six-row nonlocal compensation was finite-sample saturation, not theory identity.
- Iteration 192 preserved a preregistered cubic polarization failure rather than silently reseeding it.
- Iteration 193 froze v2 with one geometry-only seed rule; all 12 rows pass.
- Iteration 194 found local zero-K2 C5 curvature-cubic soft2 rank `4/12`.
- Iteration 195 showed exact hard calibration leaves only the four zero-K2 curvature-cubic parameters in the supported hard-preserving nullspace.
- Iteration 196 proved hard rank 7 structurally by the ECT/Wronskian result and local soft2 rank 4 by the row-scaled Vandermonde determinant. It also exposed severe numerical conditioning despite exact rank.

## Iteration 197 — completed v3 conditioning + cubic geometry + local C5 check

### Target-independent K2 design
A preregistered two-scale grid was searched using only the supported hard comparator `[x,...,x^6,x^2 exp(x)]` within `0.10<=x<=1.00`. No candidate, soft2, residual or left-null information was used.

Selected scales: `0.80` and `1.40`.

Selected x values:
`[0.324864,0.246656,0.27264,0.201792,0.256256,0.184448,0.994896,0.755384,0.83496,0.617988,0.784784,0.564872]`.

Hard-K2 conditioning:
- rank `7/7`;
- raw condition `2.04935e7 -> 6.36910e6`, improvement factor `3.2176`;
- column-normalized condition improvement factor `3.0705`;
- raw smallest singular value gain factor `5.6670`.

Classification: `IMPROVED_BUT_STILL_NEAR_DEGENERATE`. This is not finite-noise identifiability.

### Prospective polarization freeze
Before any cubic comparator evaluation, one geometry-only rule was applied to all 12 v3 rows:
- hard `abs(raw TT norm)>=0.25`;
- partner `min abs(raw TT norm)>=0.25` and constant sign on 81 epsilon points over `[-0.01,0.01]`.

All 12 rows pass. Minimum partner margin: `0.8106158577`.

### Local C5 soft2 evaluation after freeze
The exact leading cyclic `Riemann^3` soft2 coefficient gives

`V4 = Riemann3_soft2 * {1,-x,x^2,-x^3}`.

On v3:
- rank `4/12`;
- singular values `[6.1707923546,0.8674945113,0.1119400053,0.00594262129]`;
- condition number `1038.3957`;
- algebraic complement dimension `8` before blocked AS/C3 completion.

Retain `NUM-NG-011`, `PROTO-NG-005`, `NUM-NG-012`, `C5-NG-017`, `REL-NG-012`, `NG-FUNNEL-052`.

## Comparator state

- **C5 local:** supported conditional zero-K2 curvature-cubic soft2 rank `4/12` on v3.
- **C4:** compatible massless-spin-2 boundary remains inside local C5 at frozen scope; nonzero-mass dRGT remains null-soft protocol-incompatible.
- **Nonlocal:** fixed lambda K2 direction is structurally independent of the local polynomial hard family for any seven distinct positive nodes and is removed by exact hard calibration on prospective >=7-node blocks.
- **AS:** `BLOCKED_AS_REALTIME_RELATION_COMPLETION`.
- **C3:** `BLOCKED_C3_CTP_ORDERED_COMPLETION`.

## Candidate state

There is still **no robust Candidate Gravity residual**.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Current authority files

Iteration 197:
- `analysis/withheld_v3_k2_conditioning_design_iteration197.py`
- `results/withheld_v3_k2_conditioning_design_iteration197.json`
- `analysis/withheld_v3_polarization_freeze_iteration197.py`
- `results/withheld_v3_polarization_freeze_iteration197.json`
- `analysis/withheld_v3_local_c5_soft2_iteration197.py`
- `results/withheld_v3_local_c5_soft2_iteration197.json`
- `candidate_gravity/WITHHELD_V3_CONDITIONING_AND_C5_ITERATION197.md`
- `research_log/2026-09-01_iteration_197_withheld_v3_conditioning_and_c5.md`
- `recovery/RECOVERY_DELTA_ITERATION_197.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION197.md`

## Immediate next scientific priority — Iteration 198

Freeze a comparator-only **finite-noise conditioning acceptance criterion** for the v3 hard-K2 calibration, without running Fisher and without using any Candidate Gravity target:

1. define one explicit dimensionless column-scaling convention for the seven supported hard directions;
2. define a preregistered perturbation/error envelope tied to numerical/comparator authority rather than future experiment forecasts;
3. propagate that envelope through the hard calibration solve to a parameter-amplification bound;
4. classify v3 as operationally acceptable or still near-degenerate under that frozen criterion;
5. if it fails, redesign the hard-node domain prospectively using comparator-only information; if it passes, freeze v3 and return to AS/C3 authority closure;
6. keep AS/C3 BLOCKED; do not create `ANSATZ-003` or start Fisher/resources.
