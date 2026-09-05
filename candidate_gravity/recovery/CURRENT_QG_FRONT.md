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
- Latest completed numerical mass-support authority: **Iteration 475**, raw-consuming canonical rank-9 run `33983416847` as non-promoting PASS at `u=+5e-6, v=-5e-6`.
- Latest authoritative research iteration: **Iteration 479**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; occurrence denominator `32 x 5 x 16 = 2560` rows.
- Certified occurrence-weighted precision coverage: **`15/32 = 46.875%`**, i.e. **`1200/2560`** row occurrences.
- Frozen Iteration-455 rank 10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the initial baseline and is already included in coverage. It must not be launched again.
- Active numerical gate: Iteration-455 distinct rank 11, `u=+5e-6, v=+1e-5`, source occurrence multiplicity 1; canonical run `33989317870`, job `101368577097`, remains `in_progress` and is the sole permitted heavy numerical gate under unchanged frozen five-z/NPHI16/radial/direct-MP80/120 conventions and thresholds. Do not duplicate.

## Latest raw numerical authority — Iteration 475
Canonical rank-9 run `33983416847`, job `101352576616`, artifact `9975782294`, artifact digest `sha256:a0e4d481dd4b34addf7a11316730dee3240e7843f12b586307f40608c08e15c5`, scientific JSON SHA-256 `533e5ab27c3631c25023e30ee70fecdb3bd845c18015cc6cf277ea42fd3ea8d8`.

At `u=+5e-6, v=-5e-6`: `80/80` finite; max scaled MP80↔MP120 `2.91451824771117558020302499753e-80 <= 1e-30`; max radial Richardson scaled error `2.55741734246055448980134948906e-15 <= 5e-4`. Classification: `PASS_NEXT_MASS_NODE_FULL_Z_MP80_MP120__NON_PROMOTING`. This closes only the local mass-support precision certificate and does not promote physical double-double index 2.

## Manifest correction retained in authority
The frozen Iteration-455 manifest, not stale prospective wording, determines coordinate state. Rank 10 `(+5e-6,+5e-6)` was `CERTIFIED` before the sequential queue and contributed multiplicity 2 to the initial certified baseline. Therefore after rank-9 PASS the next scientifically allowed untested coordinate is rank 11 `(+5e-6,+1e-5)`, multiplicity 1. Re-running rank 10 would be a duplicate heavy calculation and is forbidden.

## Latest precision/provenance closure — Iteration 479
Post-478 aligned transverse-basis MP run `33992301400`, artifact `9977002318`, was raw-consumed from the downloaded Actions artifact rather than accepted from workflow colour. Artifact digest `sha256:34ec19c65bd9fdd97643f5b80142176d3487298219cb4671d5396dc9719d8026`; workflow head `48cdcf4302df279fa8241197e71d398b58c9fa1f`; scientific JSON SHA-256 `e718a1e78b1a16923ff51ba56b8788be46b64d62e33c75e531f97b2e49927740`.

At frozen double-double index 2 / class 3 / `q^2=-1`, the complete Iteration-407 transverse and aligned `(e1,e2,e3)` basis was reconstructed from the frozen physical source shifts independently at MP80 and MP120. All values were finite. Max scaled MP80↔MP120 basis discrepancy was `1.64877120019418172037013725225e-81 <= 1e-30`; scaled MP80↔MP120 `q^2` discrepancy was `0.0`; MP80 Gram max error `2.10843958864610464486971481025e-81`; MP120 Gram max error `1.93629595742465913640901531664e-121`; MP120 q-orthogonality max residual `0.0`. Max binary64↔MP120 aligned-basis drift was `1.75599155637895150960715164062e-16`, non-material relative to retained diagnostic `2e-6` assembly and `2e-5` physical reference scales.

Classification: `PASS_ALIGNED_TRANSVERSE_BASIS_MP80_MP120__BINARY_DRIFT_DIAGNOSTIC_ONLY_NON_PROMOTING`.

Scope is precision/provenance only at the repository-declared frozen source-shift fixture. This closes the aligned-basis arithmetic precision boundary left open by Iteration 478, but it does not certify final full-F assembly, does not promote physical double-double index 2, and does not create a comparator/novelty/identifiability conclusion. `ANSATZ-003` remains uncreated and Fisher/resources remain forbidden.

## Retained Iteration 478 geometry closure
Iteration 478 raw-consumed post-477 frozen-basis geometry MP run `33992073492`, job `101375971739`, artifact `9976943399`. Artifact digest `sha256:8b853b49a040d4f0eef99b0aaeedd427f657b8fda47dc49707b639566977f473`; scientific JSON SHA-256 `77a334ba3de6812c0bb3b37bd403fb7e71884c5a27de13bdf31cc46f01b1f614`.

Across all 28 distinct mass coordinates, five training-z, NPHI16, three radial h values and both radial signs (`13440` point samples), all geometry arithmetic values were finite. Max MP80↔MP120 scaled discrepancy was `3.2476704251336853442545536696e-81 <= 1e-30`. Max binary64↔MP120 scaled geometry drift was `3.55401690420536569154467606735e-16`, non-material relative to diagnostic `2e-6` assembly and `2e-5` physical reference scales. Classification: `PASS_FROZEN_BASIS_GEOMETRY_ARITHMETIC_MP80_MP120__BINARY_DRIFT_DIAGNOSTIC_ONLY_NON_PROMOTING`.

## Retained physical authority and blocker
Timelike `Tr U2` before `+i/2` weight: `q^2=-1 -> +0.0005345424186332474`; `q^2=-0.34 -> -0.000734101259784574`; `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains blocker authority: run `33871920373`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero fill.

## Frozen numerical/assembly contracts
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic; 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459/461/463/466/468/470/473/475 progressively close direct-parent full-training-z mass support. Iteration 454 forbids unsupported `u<->v` deduplication. Iteration 455 freezes exact source order and coordinate states. Iteration 457 permits shared local precision certificates only for exact BASE/HALF coordinate overlaps while keeping derivative weights distinct.

After all 28 distinct support coordinates are locally certified, BASE and HALF central4 assemblies must be evaluated independently at MP80 and MP120. Retain `ds=-d_base`; there is no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, and report weighted local error budgets. Iteration 460 requires `D`, `S_abs`, `kappa_cancel`, `B_80_120` and triangle-inequality consistency. Iteration 462 exact synthetic moment probes and Iteration 467 canonical-16 versus exact four-quartet parity-projector equivalence are mandatory implementation/provenance checks. Iteration 469 requires `S_quartet`, `kappa_quartet`, `rho_parity`, and `rho_shell` independently for BASE/HALF and MP80/MP120. Iteration 471 additionally requires `B_quartet_delta`, `rho_precision_parity`, and `rho_precision_shell` for the MP80↔MP120 discrepancy itself, with `|DeltaD|<=B_quartet_delta<=B_sample_delta`. Iteration 472 proves local scaled MP sample PASS does not imply assembled MP closure and requires exact weighted-discrepancy evaluation or the sufficient envelope test. Iteration 474 additionally requires double-centering `DeltaF_int=P DeltaF P`, raw/double-centered `DeltaD` equality up to arithmetic roundoff, and the Frobenius bound. Iteration 476 proves only the Frobenius component parallel to `cc^T` can change the derivative. Iteration 477 gives an exact four-quartet implementation of that rank-1 sensitive certificate: future assembly should verify canonical-16, quartet, odd-odd and rank-1 forms agree without identifying `Q12` and `Q21`. Iteration 478 closes frozen-basis geometry arithmetic MP80/120 precision at the stated decimal-input scope. Iteration 479 closes MP80/120 reconstruction of the transverse/aligned Iteration-407 basis from the frozen physical source shifts and quantifies binary64 basis drift as negligible at retained diagnostic scales. Iteration 464 h4/h6 signatures are diagnostic only; Iteration 465 proves two-level truncation order is not identifiable and forbids Richardson promotion.

## Active gate
Iteration-455 distinct rank 11: `u=+5e-6, v=+1e-5`, multiplicity 1. Canonical run `33989317870`, job `101368577097`, remains active. This is the first untested deterministic manifest coordinate after raw-valid rank 9 because rank 10 is already certified. Raw-consume fail-closed after completion. PASS closes only this exact coordinate and permits only the next UNTESTED manifest coordinate; BLOCKED requires localization of the first failing `z/phi/radial` sample at exactly rank 11.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 479 closes a real aligned-basis precision/provenance subgate but closes no additional stable readiness-rubric component.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Local MP sample PASS never substitutes for assembled derivative MP closure. Large cancellation condition number is diagnostic only. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
