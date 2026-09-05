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
- Latest completed numerical mass-support authority: **Iteration 473**, raw-consuming canonical run `33980045356` as non-promoting PASS at `u=+5e-6, v=-1e-5`.
- Latest authoritative research iteration: **Iteration 473**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; occurrence denominator `32 x 5 x 16 = 2560` rows.
- Certified occurrence-weighted precision coverage: **`13/32 = 40.625%`**, i.e. **`1040/2560`** row occurrences.
- Active numerical gate: Iteration-455 distinct rank 9, `u=+5e-6, v=-5e-6`, source occurrence multiplicity 2; canonical run `33983416847` has been launched under unchanged frozen five-z/NPHI16/radial/direct-MP80/120 conventions and thresholds. Do not duplicate.

## Latest raw numerical authority — Iteration 473
Canonical run `33980045356`, job `101343539742`, artifact `9974359345`, artifact digest `sha256:119fa95d1d86780c1b0e281eb2403b9d229717bd12cf940d8c0acb4a6da87d50`, scientific JSON SHA-256 `c65576e782850d9060ec6549ba0158ea10257ce4289e4bc72fbf43e5f16ae21d`.

At `u=+5e-6, v=-1e-5`: `80/80` finite; max scaled MP80↔MP120 `2.50535867256002728371956691164e-80 <= 1e-30`; max radial Richardson scaled error `2.55352643477510396069343790579e-15 <= 5e-4`. Classification: `PASS_NEXT_MASS_NODE_FULL_Z_MP80_MP120__NON_PROMOTING`. This closes only the local mass-support precision certificate and does not promote physical double-double index 2.

## Latest research closure — Iteration 472
Iteration 472 closes the exact implication between local MP sample precision and the already-frozen assembled derivative MP gate. For `delta_i=F80_i-F120_i`, `s_i=max(1,|F80_i|,|F120_i|)`, local `e_i=|delta_i|/s_i`, and `E=sum_i |w_i|s_i`, if all `e_i<=eps_local` then exact triangle inequality gives `|DeltaD|<=B_sample_delta<=eps_local E`. Therefore a sufficient assembled condition is `eps_local E/max(1,|D80|,|D120|)<=tau`, with frozen `tau=2e-6`. An exact equal-and-opposite central4 weight counterexample (`+4/9,-4/9`, `F120=(10^30,10^30)`, `F80=(10^30+1,10^30-1)`) has both local scaled discrepancies `<=1e-30` but assembled scaled discrepancy `8/9`; hence local PASS alone can never substitute for assembled MP closure. Classification: `PASS_LOCAL_TO_ASSEMBLED_MP_SUFFICIENCY_CONTRACT__NON_PROMOTING`. Failure to establish assembled precision is provenance/conditioning `BLOCKED` or unproven, never physics FAIL. No estimator or threshold changed.

## Retained physical authority and blocker
Timelike `Tr U2` before `+i/2` weight: `q^2=-1 -> +0.0005345424186332474`; `q^2=-0.34 -> -0.000734101259784574`; `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains blocker authority: run `33871920373`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero fill.

## Frozen numerical/assembly contracts
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic; 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459/461/463/466/468/470/473 progressively close direct-parent full-training-z mass support. Iteration 454 forbids unsupported `u<->v` deduplication. Iteration 455 freezes exact source order. Iteration 457 permits shared local precision certificates only for exact BASE/HALF coordinate overlaps while keeping derivative weights distinct.

After all 28 distinct support coordinates are locally certified, BASE and HALF central4 assemblies must be evaluated independently at MP80 and MP120. Retain `ds=-d_base`; there is no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, and report weighted local error budgets. Iteration 460 additionally requires `D`, `S_abs`, `kappa_cancel`, `B_80_120` and triangle-inequality consistency. Iteration 462 exact synthetic moment probes and Iteration 467 canonical-16 versus exact four-quartet parity-projector equivalence are mandatory implementation/provenance checks. Iteration 469 requires `S_quartet`, `kappa_quartet`, `rho_parity`, and `rho_shell` independently for BASE/HALF and MP80/MP120 so value cancellation origin is attributed rather than conflated. Iteration 471 additionally requires `B_quartet_delta`, `rho_precision_parity`, and `rho_precision_shell` for the MP80↔MP120 discrepancy itself, with `|DeltaD|<=B_quartet_delta<=B_sample_delta`. Iteration 472 proves local scaled MP sample PASS does not imply assembled MP closure; future assembly must evaluate the exact weighted discrepancy bound or verify `eps_local E/max(1,|D80|,|D120|)<=2e-6`. Iteration 464 h4/h6 signatures are diagnostic only; Iteration 465 proves two-level truncation order is not identifiable and forbids Richardson promotion.

## Active gate
Iteration-455 distinct rank 9: `u=+5e-6, v=-5e-6`, multiplicity 2. Canonical run `33983416847` is the sole active/queued numerical gate. Raw-consume fail-closed after completion. PASS closes only that exact coordinate and permits only distinct rank 10 under the deterministic manifest and unchanged frozen conventions. BLOCKED requires localization of the first failing `z/phi/radial` sample at exactly rank 9. No later coordinate may launch beforehand.

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
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Local MP sample PASS never substitutes for assembled derivative MP closure; Iteration 472 gives an exact counterexample and sufficient weighted-envelope condition. Large cancellation condition number is diagnostic only; Iteration 469/471 decompositions may localize its origin but never promote or fail physics by themselves. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
