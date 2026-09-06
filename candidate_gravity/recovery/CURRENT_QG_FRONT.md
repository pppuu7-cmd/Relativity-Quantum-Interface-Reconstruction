# Candidate Gravity Current Front

**Updated:** 2026-09-07  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: **Iteration 411**.
- Latest validated structural authority: **Iteration 410**.
- Latest raw-valid physical blocker: **Iteration 421 — `BLOCKED_CONVERGENCE`**, unresolved double-double index 2 / class 3 / `q^2=-1`.
- Exact unresolved physical set: **`[2]`**.
- Latest completed numerical mass-support authority: **Iteration 509**, raw-consumed frozen Iteration-455 rank22 `(u,v)=(+2.5e-6,-5e-6)`, HALF local index 8, multiplicity 1.
- Latest authoritative research iteration: **Iteration 512**.
- Certified occurrence-weighted precision coverage: **`27/32 = 84.375% = 2160/2560`** row occurrences.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16. Frozen rank10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in Iteration 455 and must not be relaunched.

## Latest numerical authority — Iteration 509 rank22
Canonical rank22 `(u,v)=(+2.5e-6,-5e-6)`, HALF local index 8, multiplicity 1: run `34053331578`, job `101540723619`, artifact `9996510520`, head SHA `3c50345c19fff8e41b8333921ff25a6cbf7dbc38`.

Classification: `PASS_RAW_CONSUMED_MANIFEST_RANK22_FULL_Z_MP80_MP120__NON_PROMOTING`. Observed `80/80` finite; max scaled MP80↔MP120 `3.83354568012384696441586399316e-80 <= 1e-30`; max radial Richardson scaled error `2.56445151996503781362143041011e-15 <= 5e-4`. Scientific JSON SHA-256 `311c15e99d71dbf38529a248d5b2cd99c89d6d656e098d58370c61aa214feba0`; authority-audit SHA-256 `bf9b139e7dc810d55cf811f88169a6fcf032885a172449e6904cf3cfec544610`.

This advances local precision support only. It does not promote physical index 2, assembled BASE/HALF authority, robust residual, ansatz authority, comparator novelty, or readiness.

## Active heavy gate — rank23
Frozen rank23 is `(u,v)=(+2.5e-6,-2.5e-6)`, HALF local index 9, multiplicity 1. Stage: `candidate_gravity/code/post509_manifest_rank23_full_z_mp_stage.py`. Workflow: `.github/workflows/rqir-post509-manifest-rank23-full-z-mp.yml`. Trigger/head `c4cb2a2bf294c550260ce1163abd392a9a039707`.

Canonical run **`34058694183`**, job **`101555199703`**, remains **`in_progress`** on `Run manifest-rank23 full-z MP stage`; queued count is zero, raw authority audit and artifact upload are pending. Do not duplicate and do not assign scientific PASS before raw artifact consumption.

Only raw-valid rank23 PASS permits rank24 `(+2.5e-6,+2.5e-6)`, HALF local index 10, multiplicity 1. If BLOCKED, stop suffix progression and localize the first failing `z/phi/radial` sample without changing frozen dynamics, support order, thresholds, MP levels, radial hs, or angular grid.

## Frozen remaining suffix
- rank23 `(+2.5e-6,-2.5e-6)`, HALF local index 9;
- rank24 `(+2.5e-6,+2.5e-6)`, HALF local index 10;
- rank25 `(+2.5e-6,+5e-6)`, HALF local index 11;
- rank26 `(+5e-6,-2.5e-6)`, HALF local index 13;
- rank27 `(+5e-6,+2.5e-6)`, HALF local index 14.

Conditional coverage after sequential raw-valid PASS is preregistered: rank23 `28/32=87.500%`; rank24 `29/32=90.625%`; rank25 `30/32=93.750%`; rank26 `31/32=96.875%`; rank27 `32/32=100%`. These are arithmetic consequences only, not PASS claims.

## Exact assembly authority — Iterations 510–512
Iteration 510: `PASS_BASE_HALF_ASSEMBLY_LINEAR_INDEPENDENCE_EXACT__NON_PROMOTING`. On the exact 28-coordinate union, `rank([W_BASE,W_HALF])=2`; adding `W_DELTA=W_BASE-W_HALF` leaves rank 2. Exact Gram matrix `G=[[4225/5184,4/81],[4/81,4225/324]]`, determinant `5948843/559872`. BASE-minus-HALF is derived and must never be counted as a third independent observable/Fisher constraint.

Iteration 511: `PASS_BASE_HALF_SHARED_NODE_COVARIANCE_EXACT__NON_PROMOTING`. Under the explicitly scoped iid equal-variance coordinate-error model, `Cov(BASE,HALF)=(4/81)sigma^2/h^4`, correlation `64/4225`, and `Var(BASE-HALF)=(23771/1728)sigma^2/h^4`. Shared-node numerical covariance must be retained; this is not physical-observable covariance authority.

Iteration 512: `AUDIT_BASE_HALF_ASSEMBLY_SINGULAR_SPECTRUM_EXACT__NON_PROMOTING`. Exact Gram eigenvalues are `(71825±sqrt(4016652769))/10368`, numerically approximately `0.81480824040386763744` and `13.0403229324356385354`. Gram condition number is approximately `16.00416182091147668`; singular-value condition number of the two-row assembly map is approximately `4.0005201937887373552`. This quantifies numerical/provenance geometry only; it creates no new frozen threshold and no physical PASS.

Reproducible Iteration-512 audit: `candidate_gravity/code/iteration512_base_half_assembly_singular_spectrum_exact_audit.py`; result `candidate_gravity/results/iteration512_base_half_assembly_singular_spectrum_exact_audit.json`; research log `candidate_gravity/research_log/2026-09-07_iteration_512.md`; recovery `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_512.md`.

## Retained comparator and physical blockers
Iteration 504 remains `BLOCKED_FIXED_COMPARATOR_QUOTIENT_UPSTREAM_TARGET_NOT_ASSEMBLED__NON_PROMOTING`: the concrete upstream algebraic target is not assembled, so comparator identity/rank loss/near-degeneracy/novelty are not evaluable. This is BLOCKED, not scientific FAIL.

Frozen timelike `Tr U1^2` census remains 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per `q^2`. Iteration 421 run `33871920373` remains raw-valid `BLOCKED_CONVERGENCE`; diagnostic index-2 value is not authority and no zero-fill is allowed. Max physical stability scaled `2.2720400683804223e-05` and max required fit residual scaled `2.585665489102237e-05` exceed frozen `2e-05`; thresholds are not weakened.

## Frozen numerical/assembly contract
After all 28 distinct support coordinates are locally certified, evaluate BASE and HALF central4 assemblies independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Local MP PASS never substitutes for assembled derivative closure.

The frozen Iteration-424 high-precision fallback remains downstream of complete support closure and independent BASE/HALF assembly. It preserves the same mass nodes and parent dynamics and forbids smaller `h`, angular-grid escalation, threshold weakening, zero fill, or bypassing ranks 23–27.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 512 strengthens exact assembly conditioning provenance but closes no additional stable-rubric Candidate-Gravity component.

## Exact downstream chain
Complete support closure → independent BASE/HALF MP80/120 assembly → frozen Iteration-424 reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Exact BASE/HALF coordinate overlap may share local sampled precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Shared BASE/HALF support coordinates induce nonzero numerical-error covariance under iid coordinate noise. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
