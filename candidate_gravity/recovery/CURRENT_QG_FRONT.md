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
- Latest completed numerical mass-support authority: **Iteration 480**, raw-consumed frozen Iteration-455 rank 11 `(u,v)=(+5e-6,+1e-5)`, multiplicity 1.
- Latest authoritative research iteration: **Iteration 481**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; occurrence denominator `32 x 5 x 16 = 2560` rows.
- Certified occurrence-weighted precision coverage: **`16/32 = 50.000%`**, i.e. **`1280/2560`** row occurrences pending rank12 raw-consume.
- Frozen rank 10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the initial baseline and must not be relaunched.

## Iteration 480 numerical authority
Canonical rank-11 run `33989317870`, job `101368577097`, artifact `9977375478`, artifact digest `sha256:603e51865eb13242556c41700a6e9ee54b916fe18a2c2fdd9281976aadd3e71c`, scientific JSON SHA-256 `7cc7c36a6dd5fd628280f370ad68a3b93b018fc919a0948471420a6f945b8b9f`.

At `u=+5e-6, v=+1e-5`: `80/80` finite; max scaled MP80↔MP120 `2.94779472003420316940302965078e-80 <= 1e-30`; max radial Richardson scaled error `2.56155487488387492604714966234e-15 <= 5e-4`. Classification: `PASS_RAW_CONSUMED_MANIFEST_RANK11_FULL_Z_MP80_MP120__NON_PROMOTING`. This closes only the local mass-support precision certificate and does not promote physical double-double index 2.

## Iteration 481 active numerical gate
The frozen Iteration-455 source-order generator was re-read directly. BASE central4 coordinates are enumerated u-major/v-major before HALF, with node rule `[-2h,-h,+h,+2h]` and `BASE_H=5e-6`. Therefore the exact next UNTESTED coordinate after raw-certified rank 11 is distinct rank 12 `(u,v)=(+1e-5,-1e-5)`, multiplicity 1; this is manifest-derived and not inferred from `u<->v` symmetry.

Before launch Actions state was `0` queued / `0` in_progress. A collision-safe one-coordinate stage/workflow was added with unchanged five-z, NPHI16, radial `{0.002,0.001,0.0005}`, direct MP80/MP120 and frozen thresholds. Stage commit `8e79541391934f9d391bec811f5e51eae732633d`; workflow commit `93bd9f1c61d6499e439e15909146ee39d2d76171`; trigger/head commit `54f9fee0fea91256b5c0d1a2297aae80b1dad6e3`.

Canonical active run: `33997856739`; job: `101391409387`; initial state: `queued`. Rank12 is not scientific PASS until its uploaded raw result and embedded authority audit are checked fail-closed.

## Iteration 480 provenance closure
Initial post-479 digest-diagnostic raw-consume run `33994982284`, job `101383835758`, failed before scientific digest assertions because GitHub CLI lacked `GH_TOKEN`. Artifact download itself succeeded. Initial classification: `OPERATIONAL_BLOCKED__GH_CLI_AUTH_MISSING`, explicitly not Candidate-Gravity consistency FAIL.

A minimal workflow-only repair added `GH_TOKEN: ${{ github.token }}` in commit `b5a1f9f54ebf04eccb95d9d718d789932747f523`; no scientific fixture, threshold, source run, ansatz, dynamics or support ordering changed. Corrected run `33995476897` completed successfully and raw-consumed the diagnostic in commit `3fb99e821d0b4c45d131102032f6b0609823e7ee`.

For frozen source artifact `9961449686`, metadata digest = frozen registry digest = REST-downloaded ZIP SHA = `sha256:800fa05a9891c7cb3890d07c92bc3ab37df8ce22d94d5a2219ca5f58668e9792`. Diagnostic JSON SHA-256 `07d6ecba52c0fc76e3313cdcdb04e44fe2d7d44fe1bfbd2049048f9fff0801ae`. Classification: `PASS_ARTIFACT_METADATA_AND_REST_ZIP_SHA_BOTH_MATCH_REGISTRY__NON_PROMOTING`. This is provenance closure only, not physics promotion or novelty evidence.

## Retained precision/provenance closures
Iteration 478: frozen-basis geometry MP80/120 precision closure across all 28 distinct mass coordinates, five training-z, NPHI16 and radial samples; classification `PASS_FROZEN_BASIS_GEOMETRY_ARITHMETIC_MP80_MP120__BINARY_DRIFT_DIAGNOSTIC_ONLY_NON_PROMOTING`.

Iteration 479: transverse/aligned Iteration-407 basis reconstructed independently at MP80/MP120 from frozen physical source shifts; classification `PASS_ALIGNED_TRANSVERSE_BASIS_MP80_MP120__BINARY_DRIFT_DIAGNOSTIC_ONLY_NON_PROMOTING`.

## Retained physical authority and blocker
Timelike `Tr U2` before `+i/2` weight: `q^2=-1 -> +0.0005345424186332474`; `q^2=-0.34 -> -0.000734101259784574`; `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains blocker authority: run `33871920373`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero fill.

## Frozen numerical/assembly contracts
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic; 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459/461/463/466/468/470/473/475/480 progressively close direct-parent full-training-z mass support. Iteration 454 forbids unsupported `u<->v` deduplication. Iteration 455 freezes exact source order and coordinate states. Iteration 457 permits shared local precision certificates only for exact BASE/HALF coordinate overlaps while keeping derivative weights distinct.

After all 28 distinct support coordinates are locally certified, BASE and HALF central4 assemblies must be evaluated independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus the retained Iteration 460/462/467/469/471/472/474/476/477 provenance and conditioning contracts. Iteration 464 h4/h6 signatures remain diagnostic only; Iteration 465 proves two-level truncation order is not identifiable and forbids Richardson promotion.

## Active gate
Raw-consume canonical rank12 run `33997856739`, job `101391409387`, fail-closed. If and only if the raw artifact passes the frozen audit, certified occurrence-weighted coverage may advance by one occurrence and the next permitted heavy coordinate is frozen distinct rank 13 `(u,v)=(+1e-5,-5e-6)`, multiplicity 1. If rank12 is BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen thresholds. Do not infer alternatives by symmetry and do not run blind remaining-grid sweeps.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 481 resolves the manifest-selection blocker and launches one scientifically allowed local support gate, but no additional stable readiness-rubric component is closed.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Local MP sample PASS never substitutes for assembled derivative MP closure. Large cancellation condition number is diagnostic only. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.