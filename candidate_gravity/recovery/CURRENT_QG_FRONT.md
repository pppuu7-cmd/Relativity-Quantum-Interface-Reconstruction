# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 306**

Repository commits, schema-validated Actions artifacts and recovery material are source of truth. A green workflow conclusion alone is never scientific authority. A failed workflow is not a scientific FAIL unless its raw diagnostic artifact survives and identifies the violated frozen threshold.

## Current scientific state

### Iterations 291–295 — direct timelike weight-completed TrU1 numerator authority

Iteration 295 reconstructs all eight non-scaleless direct-timelike `[Tr U1]_{sab}` numerator families at frozen `s=0.016` from the same parent/oracle: 36 primitive branches, 8 families, primitive/direct residual `6.485922909860165e-13`, maximum held-out relative error `4.842076903979733e-09`, no oracle imaginary contamination.

Freeze:

`PASS_DIRECT_TIMELIKE_S0016_WEIGHT_COMPLETED_TRU1_ALL_FAMILY_NUMERATOR_RECONSTRUCTION`.

### Iterations 296/298/300–302 — corrected bubble-cut authority

The original Iteration-296 green run was rejected by Iteration 298 because its artifact lacked sentinel 296. The repaired fail-closed run `33700626052` / job `100478933598` / artifact `9873542469` is schema-valid and freezes the four bubble-family DR/Laurent reduction. Iteration 301 proves HV-like evanescent bubble layers through `mu^4` are null in the normalized cut, and Iteration 302 promotes the four bubble-family normalized-cut subsector within that scope. Full finite amplitude remains unpromoted.

### Iterations 303–304 — triangle evanescent obstruction closed for D_s

Iteration 303 counts exactly 274 raw hidden HV-like polynomial coefficients beyond the four-dimensional triangle oracle layer. They are structurally non-identifiable from 4D samples and are not zero-filled.

Iteration 304 proves that every relevant hidden `mu^(2r)` triangle layer is cut-null in the normalized common timelike discontinuity under the frozen HV-like barred-external-state convention, assuming regular same-parent D-dimensional coefficients near `D=4`.

Validated Iteration-304 provenance:

- run `33702437466`
- job `100484390001`
- artifact `9873994705`, digest `sha256:3e5ea9c01327c47483664258162aaf1780615c8baf86433cb9db49426905ca18`
- head `477e957511eb7e7051ecf0d8b61d14f279cd30dc`
- scientific JSON SHA-256 `27efdba75eee39591ed5be0d2a766627c8fb1bf38af901a7aa823c441fd1086d`
- exactly one top-level JSON object, sentinel `304`, validator PASS.

Numerical screens: 21 hidden tensor cases; max shifted-master cut `1/epsilon` residue `8.606328628868795e-09`; max hidden evanescent cut limit `8.606328628868795e-09`; hard-edge swap covariance residual `1.8705037518884637e-12`; ordinary triangle calibration residual `1.0668019356785408e-08`.

Freeze:

`PASS_HV_TRIANGLE_EVANESCENT_CUT_PROTECTION_ALL_274_HIDDEN_POLYNOMIAL_COEFFICIENTS_CUT_NULL_WITHIN_SCOPE`.

This certificate protects the CUT only. It does not assert that the 274 coefficients vanish and does not promote a scheme-independent full finite amplitude.

### Iteration 306 — failed direct-305 diagnostic-observability audit

A second direct-timelike Iteration305 workflow run `33702862824` / job `100485680662` at head `11e593ea1ff3b3e49043e14fb4ee76c22fe1006d` failed in the scientific reduction step. Its validator and artifact-upload steps were skipped.

Static execution-contract audit identifies the reproducibility defect: the reducer computes raw epsilon scans, Laurent fits, scalar and raised-triangle calibrations, quadrature/conjugacy diagnostics and a `passed` Boolean, builds the result object, but executes `assert passed,result` before printing JSON. Under workflow `set -euo pipefail`, a failed frozen threshold therefore destroys the diagnostic artifact before validation/upload.

Freeze:

`FAIL_OPERATIONAL_ITERATION305_DIRECT_TRIANGLE_RUN_DROPS_SCIENTIFIC_DIAGNOSTICS_ON_THRESHOLD_FAILURE`.

This is operational/reproducibility FAIL only. It is not a Candidate Gravity consistency FAIL and does not authorize any triangle coefficient or tell us which frozen threshold failed.

## Frozen timelike kinematics

At the current `s=0.016` row:

- `k_s^2=0`
- `k_s.k_a=-0.1`
- `k_a^2=-0.016`
- `k_b=-(k_s+k_a)`
- `k_b^2=-0.216`

Linked physical target:

`T_cut = D_s Gamma3_ret,soft - W[D_s K2]`.

## Active C5 sectors

Iteration 246 already proves the generic connection `e=3,c=0` null-soft trilinear sector vanishes; do not reopen it.

Active pieces:

- determinant `e=0,c<=3`
- connection `e=1,c<=2` — current weight-completed `Tr U1` route
- connection `e=2,c<=1`

## Running process

The original Iteration305 workflow remains the active independent scientific process:

- workflow `rqir-iteration305-timelike-tru1-visible-triangle-cut`
- run `33702724483`
- head `7bed9233515782f7a81b9fe0d1f14e1ec57a6aa7`
- last checked status: `in_progress`
- task: integrate the four actual visible direct-timelike ordinary/raised triangle numerator families from Iteration 295 with analytic-continuation-safe Beta/2F1 tensor reduction, raw epsilon scans, branch conjugacy and Laurent fits.

Do not duplicate this run.

## Current blockers / downstream

1. Consume and validate Iteration305 run `33702724483`; workflow status alone is insufficient.
2. Do not classify failed direct run `33702862824` as scientific FAIL because its raw metrics were not preserved.
3. If the active run also fails without schema-valid diagnostics, repair execution so a diagnostic JSON with `scientific_gate_pass=false` is uploaded before the final nonzero scientific exit status; rerun exactly once without changing thresholds.
4. If triangle cut passes, combine validated four bubble + four triangle normalized-cut coefficients to freeze complete `e=1,c=2` weight-completed `Tr U1` cut subsector.
5. Then continue remaining `e=2,c<=1` and determinant `e=0,c<=3` pieces.
6. Source/Ward/contact completion and matched `K2` bridge remain required before any source/Born subtraction.
7. Only then perform the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
8. Full finite-amplitude scheme authority remains separately blocked unless a same-parent D-dimensional numerator continuation or explicit scheme-conversion/counterterm map is frozen.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

No readiness points are added by Iteration306 because it closes a scientific-classification/reproducibility prerequisite rather than a rubric block. Change from previous assessment: `0 pp`.

## Retained guardrails

- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- Do not promote weighted-kernel `tr(B3)` or Iteration-289 proxy coefficients/poles to actual `Tr U1` authority.
- Do not subtract `-8 M_Born` from a 1PI/comparator intermediate without an explicit matched source-observable map.
- Hidden evanescent coefficients are not zero; Iterations 301/304 are cut-protection statements only.
- Do not accept a green Action without expected sentinel/schema validation and raw artifact audit.
- Do not accept a failed Action as scientific FAIL unless a schema-valid diagnostic artifact preserves the violated frozen threshold and raw metrics.
- Fail-closed scientific execution must preserve evidence for both PASS and BLOCKED outcomes; authority promotion may fail after artifact upload.
- Blind heavy full-C5 remains unauthorized.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Exact next gate

Consume Iteration305 run `33702724483` without duplication. If it yields a schema-valid artifact and the prospective calibration, parameter-polynomial fit, branch-conjugacy and Laurent gates pass, freeze the four visible triangle normalized-cut coefficients and immediately perform the eight-family `e=1,c=2 Tr U1` cut-combination authority gate. If it fails without preserving diagnostics, first repair the execution contract so raw metrics are always uploaded, then rerun exactly once and preserve the first violated frozen threshold without weakening it.
