# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 297**

Repository commits, validated Actions artifacts and recovery material are source of truth. Do not reconstruct state from stale chat.

## Current scientific state

### Iterations 291–295 — weight-completed timelike TrU1 authority

Iteration 291 proved `U1=B Y_down`, so the old weighted-kernel proxy `tr(B3)` is not the cubic effective-action coefficient when the trace weight is background dependent. Iterations 292–293 established the exact denominator census and full family structural reconstruction. Iteration 294 showed the actual weight-completed `[Tr U1]_{sab}` is nonzero across the tested timelike translation-closed slice. Iteration 295 then reconstructed all eight non-scaleless numerator families directly from the timelike parent/oracle at `s=0.016`.

Iteration-295 numerical authority:

- primitive branches: `36`;
- non-scaleless families: `8`;
- primitive/direct residual: `6.485922909860165e-13`;
- maximum held-out reconstruction error: `4.842076903979733e-09`;
- maximum oracle imaginary contamination: `0.0`.

Freeze:

`PASS_DIRECT_TIMELIKE_S0016_WEIGHT_COMPLETED_TRU1_ALL_FAMILY_NUMERATOR_RECONSTRUCTION`.

### Iteration 296 — direct timelike bubble DR reduction is computationally active

A dedicated reducer and GitHub Actions workflow were added for ordinary/raised bubble families of the actual timelike `Tr U1`. It explicitly does not import the obsolete Iteration-289 weighted-kernel pole. At the time Iteration 297 was closed, the Iteration-296 Action was still running and was not duplicated. Therefore no numerical Iteration-296 PASS is promoted here until its artifact/raw epsilon scans are audited.

### Iteration 297 — DR numerator-continuation interface audit

Static audit of the Iteration-296 reducer establishes that the numerator is represented in four loop-momentum components and acted on by a four-dimensional Minkowski Laplacian, while scalar loop integration is analytically continued to `D=4-2 epsilon`.

This is a definite **4D-numerator / D-dimensional-measure prescription**, but the repository does not yet contain an authoritative same-parent D-dimensional continuation of the numerator algebra or an explicit finite conversion map to the comparator convention.

Four-dimensional numerator samples cannot identify evanescent structures such as `mu^2=-l_{[-2 epsilon]}^2`. Their absence from the Iteration-295 4D oracle is therefore non-identifiability of the evanescent sector, not an exact-zero certificate. Such terms can affect finite rational/local DR pieces.

Freeze:

`PASS_SCOPED_DR_NUMERATOR_CONTINUATION_INTERFACE_AUDIT__FULL_FINITE_REMAINDER_BLOCKED_BY_EVANESCENT_SCHEME_AUTHORITY`.

Guardrail:

`DO_NOT_PROMOTE_4D_ORACLE_DR_FINITE_REMAINDER_TO_SCHEME_INDEPENDENT_SAME_PARENT_RESULT_WITHOUT_EVANESCENT_CONTINUATION_OR_EXPLICIT_SCHEME_CONVERSION`.

This does **not** invalidate the active Iteration-296 discontinuity calculation. Its `+i0/-i0` cut/log result may be audited and used in the explicitly declared 4D-numerator/D-measure prescription. What is blocked is promotion of a complete finite same-parent covariant DR remainder without regulator-scheme authority.

This is operational/regulator `BLOCKED`, not Candidate consistency FAIL, exact comparator identity, near-degeneracy, or novelty certificate.

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

1. `BLOCKED_ACTIVE_ITERATION296_TIMELIKE_TRU1_BUBBLE_DR_RESULT_AUDIT`.
2. `BLOCKED_FULL_FINITE_DR_REMAINDER_UNTIL_EVANESCENT_NUMERATOR_CONTINUATION_OR_EXPLICIT_SCHEME_CONVERSION`.
3. Downstream: complete direct-timelike triangle reduction, combine all eight `e=1,c=2` families, remaining `e=0/e=2` pieces, source/Ward/contact completion, Lorentzian comparator quotient.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 295: **0 percentage points**. Iteration 297 prevents a regulator-scheme overclaim but does not yet close an additional readiness block.

## Retained guardrails

- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- Do not promote weighted-kernel `tr(B3)` coefficients or the Iteration-289 proxy pole to `Tr U1` authority.
- Do not subtract `-8 M_Born` from a 1PI/comparator intermediate without an explicit matched source-observable map.
- Reconstruct timelike numerator coefficients directly from the same parent dynamics; do not rotate denominators only.
- Do not interpret absence of evanescent terms in a 4D loop oracle as an exact-zero statement.
- Blind heavy full-C5 remains unauthorized.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Iteration 297 authority files

- `candidate_gravity/C5_DR_NUMERATOR_CONTINUATION_AUDIT_ITERATION297.md`
- `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_297.md`
- `research_log/2026-09-03_iteration_297_dr_numerator_continuation_audit.md`

## Exact next gate

1. Consume/audit the already-running Iteration-296 bubble Action when complete: scalar calibration, branch conjugacy, raw epsilon scans, Laurent stability and family discontinuities.
2. Scope its cut/log result explicitly to the implemented 4D-numerator/D-measure prescription.
3. Before promoting a complete finite remainder, freeze either a same-parent D-dimensional numerator continuation or an explicit finite scheme-conversion/counterterm map.
4. Reduce the direct-timelike triangle families in the same declared prescription and combine all eight `e=1,c=2` families.
5. Continue active `e=2,c<=1` and determinant `e=0,c<=3`, then linked source/Ward/contact completion and the fixed comparator quotient.
