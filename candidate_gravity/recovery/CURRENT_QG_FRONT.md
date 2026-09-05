# Candidate Gravity Current Front

**Updated:** 2026-09-05  
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
- Latest completed numerical mass-support authority: **Iteration 468**, raw-consuming canonical run `33968129883` as non-promoting PASS at `u=-5e-6, v=+5e-6`.
- Latest authoritative research iteration: **Iteration 469**; latest completed numerical authority remains **Iteration 468**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; occurrence denominator `32 x 5 x 16 = 2560` rows.
- Certified occurrence-weighted precision coverage: **`11/32 = 34.375%`**, i.e. **`880/2560`** row occurrences.
- Active numerical gate: run **`33973849536`**, job **`101326982817`**, Iteration-455 distinct rank 7, `u=-5e-6, v=+1e-5`, source occurrence multiplicity 1. Frozen five-z/NPHI16/radial/direct-MP80/120 conventions and thresholds are unchanged. Do not duplicate.

## Latest raw numerical authority — Iteration 468
Canonical run `33968129883`, job `101311756122`, artifact `9971336666`, artifact digest `sha256:6d502989834d91f4d02b04968a3ef156a9400321eb5dea1ec693687ec13baaec`, scientific JSON SHA-256 `220f50d31c1e9ca326c1303c3e74b39139f68fc4dbe3388450220389fef5211a`.

At `u=-5e-6, v=+5e-6`: `80/80` finite; max scaled MP80↔MP120 `3.42969575569498706166546516239e-80 <= 1e-30`; max radial Richardson scaled error `2.55777395811034909935767378004e-15 <= 5e-4`. Classification: `PASS_NEXT_MASS_NODE_FULL_Z_MP80_MP120__NON_PROMOTING`. This exact BASE/HALF overlap shares one local `F(u,v)` precision certificate while preserving distinct derivative occurrences and weights.

## Latest research closure — Iteration 469
The exact four-quartet representation from Iteration 467 now carries a two-stage cancellation decomposition. With `D=sum alpha_ab Q_ab`, define `S_quartet=sum |alpha_ab Q_ab|` and sample-level `S_sample=sum |alpha_ab| sum_signs |F|`. Exact triangle inequalities give `|D|<=S_quartet<=S_sample`. Therefore, for nonzero `D`, `kappa_sample>=kappa_quartet>=1`.

Define bounded factors `rho_parity=S_quartet/S_sample` and `rho_shell=|D|/S_quartet`. Then exactly `kappa_sample=1/(rho_parity*rho_shell)` and `kappa_quartet=1/rho_shell`. `rho_parity` diagnoses cancellation internal to the odd-odd parity quartets; `rho_shell` diagnoses cancellation among the four already-projected weighted scales. This is diagnostic/provenance only and cannot be used as physics FAIL, model non-identifiability, comparator identity, near-degeneracy, novelty evidence, or promotion. The coefficient check `sum|alpha|=9/16` recovers the frozen dimensionless sample L1 norm `9/4` after the four samples per quartet are counted.

## Retained physical authority and blocker
Timelike `Tr U2` before `+i/2` weight: `q^2=-1 -> +0.0005345424186332474`; `q^2=-0.34 -> -0.000734101259784574`; `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains blocker authority: run `33871920373`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero fill.

## Frozen numerical/assembly contracts
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic; 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459/461/463/466/468 progressively close direct-parent full-training-z mass support. Iteration 454 forbids unsupported `u<->v` deduplication. Iteration 455 freezes exact source order. Iteration 457 permits shared local precision certificates only for exact BASE/HALF coordinate overlaps while keeping derivative weights distinct.

After all 28 distinct support coordinates are locally certified, BASE and HALF central4 assemblies must be evaluated independently at MP80 and MP120. Retain `ds=-d_base`; there is no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, and report weighted local error budgets. Iteration 460 additionally requires `D`, `S_abs`, `kappa_cancel`, `B_80_120` and triangle-inequality consistency. Iteration 462 exact synthetic moment probes and Iteration 467 canonical-16 versus exact four-quartet parity-projector equivalence are mandatory implementation/provenance checks. Iteration 469 additionally requires reporting `S_quartet`, `kappa_quartet`, `rho_parity`, and `rho_shell` independently for BASE/HALF and MP80/MP120 so cancellation origin is attributed rather than conflated. Iteration 464 h4/h6 signatures are diagnostic only; Iteration 465 proves two-level truncation order is not identifiable and forbids Richardson promotion.

## Active gate
Run `33973849536`, job `101326982817`: raw-consume fail-closed at Iteration-455 distinct rank 7, `u=-5e-6, v=+1e-5`. PASS closes only that exact coordinate and permits only distinct rank 8 under the deterministic manifest and unchanged frozen conventions. BLOCKED requires localization of the first failing `z/phi/radial` sample at exactly rank 7. No later coordinate may be launched before raw consumption.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Local MP sample PASS never substitutes for assembled derivative MP closure. Large cancellation condition number is diagnostic only; Iteration 469 decomposition may localize its origin but never promotes or fails physics by itself. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
