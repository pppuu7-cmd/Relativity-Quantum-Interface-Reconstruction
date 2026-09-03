# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 298**

Repository commits, schema-validated Actions artifacts and recovery material are source of truth. Do not reconstruct state from stale chat. A green workflow conclusion alone is not scientific authority.

## Current scientific state

### Iterations 291–295 — weight-completed timelike TrU1 authority

Iteration 291 proved `U1=B Y_down`, so the old weighted-kernel proxy `tr(B3)` is not the cubic effective-action coefficient when the trace weight is background dependent. Iterations 292–293 established the exact denominator census and full family structural reconstruction. Iteration 294 showed the actual weight-completed `[Tr U1]_{sab}` is nonzero across the tested timelike translation-closed slice. Iteration 295 reconstructed all eight non-scaleless numerator families directly from the timelike parent/oracle at `s=0.016`.

Iteration-295 numerical authority remains:

- primitive branches: `36`;
- non-scaleless families: `8`;
- primitive/direct residual: `6.485922909860165e-13`;
- maximum held-out reconstruction error: `4.842076903979733e-09`;
- maximum oracle imaginary contamination: `0.0`.

Freeze:

`PASS_DIRECT_TIMELIKE_S0016_WEIGHT_COMPLETED_TRU1_ALL_FAMILY_NUMERATOR_RECONSTRUCTION`.

### Iteration 297 — DR numerator-continuation interface audit remains frozen

The Iteration-296 reducer represents the numerator in four loop-momentum components and applies a four-dimensional Minkowski Laplacian, while scalar loop integration is analytically continued to `D=4-2 epsilon`.

This defines a 4D-numerator / D-dimensional-measure prescription. The repository still lacks an authoritative same-parent D-dimensional continuation of numerator algebra or explicit finite scheme conversion to the comparator convention. Four-dimensional oracle samples cannot identify evanescent structures such as `mu^2=-l_{[-2 epsilon]}^2`; therefore their absence is non-identifiability of the evanescent sector, not an exact-zero certificate.

Freeze:

`PASS_SCOPED_DR_NUMERATOR_CONTINUATION_INTERFACE_AUDIT__FULL_FINITE_REMAINDER_BLOCKED_BY_EVANESCENT_SCHEME_AUTHORITY`.

Guardrail:

`DO_NOT_PROMOTE_4D_ORACLE_DR_FINITE_REMAINDER_TO_SCHEME_INDEPENDENT_SAME_PARENT_RESULT_WITHOUT_EVANESCENT_CONTINUATION_OR_EXPLICIT_SCHEME_CONVERSION`.

This is operational/regulator `BLOCKED`, not Candidate consistency FAIL, exact comparator identity, near-degeneracy, or novelty certificate.

### Iteration 298 — completed Iteration-296 Action fails scientific artifact authority

The previously active Iteration-296 GitHub Action has completed with workflow conclusion `success`, but the persisted artifact does not contain the expected Iteration-296 final scientific payload.

Audited provenance:

- workflow run: `33693775575`;
- job: `100458128185`;
- artifact: `9871204017`;
- workflow commit: `f49474b77fb7f1682c3365dd0854b6cb19a5e7ef`;
- artifact member: `iteration296_result.json`;
- bytes: `103185`;
- SHA-256: `99af1466a132d8c116b2ef5f8466fb67dbdd53e857e93a088ff53d4d577b3a7a`.

A complete repeated JSON decode finds exactly three concatenated top-level payloads with iteration sentinels

`[270, 273, 295]`.

The required `iteration = 296` payload is absent. Therefore no Iteration-296 bubble discontinuity, Laurent coefficient, IR pole, or finite remainder from this run is promoted.

Freeze:

`FAIL_OPERATIONAL_ITERATION296_ARTIFACT_MISSING_EXPECTED_FINAL_RESULT_SCHEMA`.

Classification: **operational/reproducibility FAIL** only. This is not Candidate Gravity consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty statement.

New guardrail:

`DO_NOT_ACCEPT_GREEN_ACTION_AS_SCIENTIFIC_PASS_WITHOUT_EXPECTED_ITERATION_SENTINEL_AND_SCHEMA_VALIDATION`.

A fail-closed validator is now committed at:

`candidate_gravity/code/iteration298_validate_action_result.py`.

It accepts a scientific result only if there is exactly one top-level JSON object and its iteration sentinel equals the expected iteration. Concatenated JSON emitted by imports is detected and rejected.

The exact underlying Python termination mechanism of the failed Iteration-296 scientific artifact is not inferred from the artifact alone. That inference is unnecessary for the authority decision.

## Frozen timelike kinematics

At the current `s=0.016` row:

- `k_s^2=0`;
- `k_s.k_a=-0.1`;
- `k_a^2=-0.016`;
- `k_b=-(k_s+k_a)`;
- `k_b^2=-0.216`.

The linked physical target remains

`T_cut = D_s Gamma3_ret,soft - W[D_s K2]`.

## Active C5 sectors

Iteration 246 already proves the generic connection `e=3,c=0` null-soft trilinear sector vanishes through exact `E^(1)[h_soft]=0`; do not reopen it.

Active pieces remain:

- determinant `e=0,c<=3`;
- connection `e=1,c<=2` — current weight-completed `Tr U1` route;
- connection `e=2,c<=1`.

## Current blockers

1. `BLOCKED_VALIDATED_TIMELIKE_TRU1_BUBBLE_DR_RESULT` — the prior green run is not scientific numerical authority.
2. `BLOCKED_FULL_FINITE_DR_REMAINDER_UNTIL_EVANESCENT_NUMERATOR_CONTINUATION_OR_EXPLICIT_SCHEME_CONVERSION` — retained independently from Iteration 297.
3. Downstream: direct-timelike triangle reduction, combine all eight `e=1,c=2` families, remaining `e=0/e=2` pieces, source/Ward/contact completion, Lorentzian comparator quotient.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 297: **0 percentage points**. Iteration 298 prevents invalid numerical evidence from entering authority but closes no model-readiness block.

## Retained guardrails

- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- Do not promote weighted-kernel `tr(B3)` coefficients or the Iteration-289 proxy pole to `Tr U1` authority.
- Do not subtract `-8 M_Born` from a 1PI/comparator intermediate without an explicit matched source-observable map.
- Reconstruct timelike numerator coefficients directly from the same parent dynamics; do not rotate denominators only.
- Do not interpret absence of evanescent terms in a 4D loop oracle as an exact-zero statement.
- Do not accept a green GitHub Action as a scientific PASS unless its persisted artifact is schema-valid and carries the expected iteration sentinel.
- Blind heavy full-C5 remains unauthorized.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Iteration 298 authority files

- `candidate_gravity/C5_ACTION_ARTIFACT_AUTHORITY_AUDIT_ITERATION298.md`
- `candidate_gravity/results/iteration298_action_artifact_authority_audit.json`
- `candidate_gravity/code/iteration298_validate_action_result.py`
- `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_298.md`
- `research_log/2026-09-03_iteration_298_action_artifact_authority_audit.md`

## Exact next gate

1. Repair the Iteration-296 bubble execution path before any scientific rerun: use fail-closed shell execution (`set -euo pipefail` or equivalent), write the final scientific JSON directly to a dedicated file rather than treating mixed stdout as authority, and validate exactly one expected iteration sentinel before artifact upload.
2. Run one corrected direct-timelike `Tr U1` bubble DR calculation. Accept it only after the Iteration-298 schema validator passes.
3. Then audit scalar calibration, retarded/advanced conjugacy, raw epsilon scans, Laurent stability and family discontinuities, explicitly scoped to the implemented 4D-numerator/D-measure prescription.
4. Before promoting a complete finite remainder, freeze either a same-parent D-dimensional numerator continuation or an explicit finite scheme-conversion/counterterm map.
5. Only then reduce direct-timelike triangle families, combine all eight `e=1,c=2` families, continue `e=2,c<=1` and determinant `e=0,c<=3`, and proceed to linked source/Ward/contact completion and the fixed comparator quotient.
