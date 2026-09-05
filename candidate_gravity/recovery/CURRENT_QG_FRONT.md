# Candidate Gravity Current Front

**Updated:** 2026-09-06  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: Iteration 411.
- Latest validated structural authority: Iteration 410.
- Latest raw-valid physical blocker: Iteration 421 — `BLOCKED_CONVERGENCE`, unresolved double-double index 2 / class 3 / `q^2=-1`.
- Exact unresolved physical set: `[2]`.
- Latest completed numerical mass-support authority: **Iteration 480**, incorporating raw-consumed frozen Iteration-455 rank 11 `(u,v)=(+5e-6,+1e-5)`, multiplicity 1.
- Latest authoritative research iteration: **Iteration 480**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; occurrence denominator `32 x 5 x 16 = 2560` rows.
- Certified occurrence-weighted precision coverage: **`16/32 = 50.000%`**, i.e. **`1280/2560`** row occurrences.
- Frozen Iteration-455 rank 10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the initial baseline and must not be relaunched.

## Latest raw numerical authority — Iteration 480
Canonical rank-11 run `33989317870`, job `101368577097`, artifact `9977375478`, artifact digest `sha256:603e51865eb13242556c41700a6e9ee54b916fe18a2c2fdd9281976aadd3e71c`, scientific JSON SHA-256 `7cc7c36a6dd5fd628280f370ad68a3b93b018fc919a0948471420a6f945b8b9f`.

At `u=+5e-6, v=+1e-5`: `80/80` finite; max scaled MP80↔MP120 `2.94779472003420316940302965078e-80 <= 1e-30`; max radial Richardson scaled error `2.56155487488387492604714966234e-15 <= 5e-4`. Classification: `PASS_RAW_CONSUMED_MANIFEST_RANK11_FULL_Z_MP80_MP120__NON_PROMOTING`. This closes only the local mass-support precision certificate and does not promote physical double-double index 2.

## Iteration 480 operational provenance finding
Post-479 digest-diagnostic raw-consume run `33994982284`, job `101383835758`, failed before its scientific digest assertions because GitHub CLI lacked `GH_TOKEN`. The artifact download itself succeeded and verified digest `sha256:f022684784fcce7c27a2208baad4a9410261dddc75ab959f037fbef911dacab3`. Classification: `OPERATIONAL_BLOCKED__GH_CLI_AUTH_MISSING`, explicitly not a Candidate-Gravity consistency FAIL.

The workflow was repaired minimally in commit `b5a1f9f54ebf04eccb95d9d718d789932747f523` by adding `GH_TOKEN: ${{ github.token }}`. No scientific fixture, digest target, threshold, dynamics, support ordering or ansatz changed. The corrected digest diagnostic must be raw-consumed fail-closed before its provenance conclusion becomes authority.

## Retained Iterations 478–479 precision closures
Iteration 478 raw-consumed frozen-basis geometry MP run `33992073492`, job `101375971739`, artifact `9976943399`; all `13440` point samples finite, max MP80↔MP120 scaled discrepancy `3.2476704251336853442545536696e-81 <= 1e-30`, max binary64↔MP120 scaled geometry drift `3.55401690420536569154467606735e-16`. Classification: `PASS_FROZEN_BASIS_GEOMETRY_ARITHMETIC_MP80_MP120__BINARY_DRIFT_DIAGNOSTIC_ONLY_NON_PROMOTING`.

Iteration 479 raw-consumed aligned transverse-basis run `33992301400`, artifact `9977002318`; max scaled MP80↔MP120 basis discrepancy `1.64877120019418172037013725225e-81 <= 1e-30`, max binary64↔MP120 basis drift `1.75599155637895150960715164062e-16`. Classification: `PASS_ALIGNED_TRANSVERSE_BASIS_MP80_MP120__BINARY_DRIFT_DIAGNOSTIC_ONLY_NON_PROMOTING`.

## Retained physical authority and blocker
Timelike `Tr U2` before `+i/2` weight: `q^2=-1 -> +0.0005345424186332474`; `q^2=-0.34 -> -0.000734101259784574`; `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains blocker authority: run `33871920373`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero fill.

## Frozen numerical/assembly contracts
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic; 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459/461/463/466/468/470/473/475/480 progressively close direct-parent full-training-z mass support. Iteration 454 forbids unsupported `u<->v` deduplication. Iteration 455 freezes exact source order and coordinate states. Iteration 457 permits shared local precision certificates only for exact BASE/HALF coordinate overlaps while keeping derivative weights distinct.

After all 28 distinct support coordinates are locally certified, BASE and HALF central4 assemblies must be evaluated independently at MP80 and MP120. Retain `ds=-d_base`; there is no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, and report weighted local error budgets. Iteration 460 requires `D`, `S_abs`, `kappa_cancel`, `B_80_120` and triangle-inequality consistency. Iteration 462 exact synthetic moment probes and Iteration 467 canonical-16 versus exact four-quartet parity-projector equivalence are mandatory implementation/provenance checks. Iteration 469 requires `S_quartet`, `kappa_quartet`, `rho_parity`, and `rho_shell` independently for BASE/HALF and MP80/MP120. Iteration 471 additionally requires `B_quartet_delta`, `rho_precision_parity`, and `rho_precision_shell`, with `|DeltaD|<=B_quartet_delta<=B_sample_delta`. Iteration 472 proves local scaled MP sample PASS does not imply assembled MP closure. Iteration 474 requires double-centering `DeltaF_int=P DeltaF P`; Iteration 476 identifies the rank-1 `cc^T` sensitive mode; Iteration 477 gives the exact quartet implementation. Iteration 464 h4/h6 signatures are diagnostic only; Iteration 465 proves two-level truncation order is not identifiable and forbids Richardson promotion.

## Active gate
First, raw-consume the corrected post-479 digest diagnostic fail-closed. Separately, before any new heavy mass-support launch, re-read the frozen Iteration-455 manifest and select only the next exact `UNTESTED` coordinate after rank 11. Never infer the next coordinate by `u<->v` symmetry and never rerun certified rank 10. No heavy duplicate is permitted while the next manifest state is not explicitly established.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 480 closes rank-11 local support and localizes/repairs an operational provenance defect, but closes no additional stable readiness-rubric component.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Local MP sample PASS never substitutes for assembled derivative MP closure. Large cancellation condition number is diagnostic only. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.