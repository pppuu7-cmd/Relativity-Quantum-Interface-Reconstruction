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
- Latest authoritative research iteration: **Iteration 510**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; denominator `32 x 5 x 16 = 2560` row occurrences.
- Certified occurrence-weighted precision coverage: **`27/32 = 84.375%`**, i.e. **`2160/2560`** row occurrences.
- Frozen rank10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the Iteration-455 baseline and must not be relaunched.

## Latest numerical authority — Iteration 509 rank22
Canonical rank22 `(u,v)=(+2.5e-6,-5e-6)`, HALF local index 8, multiplicity 1: run `34053331578`, job `101540723619`, artifact `9996510520`, head SHA `3c50345c19fff8e41b8333921ff25a6cbf7dbc38`.

Raw-consumed classification: `PASS_RAW_CONSUMED_MANIFEST_RANK22_FULL_Z_MP80_MP120__NON_PROMOTING`.

Artifact digest: `sha256:3370f13c34c2060616f6311f594107526948656c365dbcf623c4e3435a15fc17`. Scientific JSON SHA-256: `311c15e99d71dbf38529a248d5b2cd99c89d6d656e098d58370c61aa214feba0`. Authority-audit SHA-256: `bf9b139e7dc810d55cf811f88169a6fcf032885a172449e6904cf3cfec544610`.

Observed: `80/80` finite; max scaled MP80↔MP120 `3.83354568012384696441586399316e-80 <= 1e-30`; max radial Richardson scaled error `2.56445151996503781362143041011e-15 <= 5e-4`.

This advances local precision support only. It does not promote physical index 2, assembled BASE/HALF authority, robust residual, ansatz authority, comparator novelty, or readiness.

Machine-readable raw-consumption record: `candidate_gravity/results/post508_rank22_raw_consumption.json`.

## Active heavy gate — rank23
The frozen Iteration-455 manifest and Iteration-507 preregistration identify rank23 `(u,v)=(+2.5e-6,-2.5e-6)`, HALF local index 9, multiplicity 1, as the sole authorized heavy support gate after rank22 raw PASS.

Reproducible stage: `candidate_gravity/code/post509_manifest_rank23_full_z_mp_stage.py`. Workflow: `.github/workflows/rqir-post509-manifest-rank23-full-z-mp.yml`. Trigger/head commit: `c4cb2a2bf294c550260ce1163abd392a9a039707`.

Canonical run **`34058694183`**, job **`101555199703`**, is **`in_progress`**. Do not duplicate this run and do not assign scientific PASS before raw artifact consumption.

If rank23 raw-valid PASS, certified support becomes `28/32 = 87.5%`, and only rank24 `(+2.5e-6,+2.5e-6)`, HALF local index 10, multiplicity 1, may follow. If BLOCKED, stop suffix progression and localize the first failing `z/phi/radial` sample without changing frozen dynamics, support order, thresholds, MP levels, radial hs, or angular grid.

## Frozen remaining suffix
- rank23 `(+2.5e-6,-2.5e-6)`, HALF local index 9;
- rank24 `(+2.5e-6,+2.5e-6)`, HALF local index 10;
- rank25 `(+2.5e-6,+5e-6)`, HALF local index 11;
- rank26 `(+5e-6,-2.5e-6)`, HALF local index 13;
- rank27 `(+5e-6,+2.5e-6)`, HALF local index 14.

Conditional occurrence-weighted coverage after sequential future raw-valid PASS is preregistered as: rank23 `28/32=87.500%`; rank24 `29/32=90.625%`; rank25 `30/32=93.750%`; rank26 `31/32=96.875%`; rank27 `32/32=100%`. These are arithmetic consequences only and are not PASS claims for unfinished ranks.

## Iteration 510 — exact BASE/HALF assembly linear independence
Classification: `PASS_BASE_HALF_ASSEMBLY_LINEAR_INDEPENDENCE_EXACT__NON_PROMOTING`.

On the exact 28-coordinate BASE/HALF union, rational row reduction gives `rank([W_BASE,W_HALF])=2`. Adding the retained discrepancy row `W_DELTA=W_BASE-W_HALF` leaves the rank exactly 2, so the two-row assembly map has nullity 26. The exact Gram matrix is `[[4225/5184,4/81],[4/81,4225/324]]` with positive determinant `5948843/559872`; 12 BASE-only and 12 HALF-only nonzero nodes give an explicit independence witness.

Operational consequence: BASE and HALF must remain independently assembled, but BASE-minus-HALF is a derived consistency diagnostic and must never be counted as a third statistically independent observable/constraint or used to create extra Fisher rank. Its frozen threshold remains mandatory and unchanged.

Reproducible audit: `candidate_gravity/code/iteration510_base_half_assembly_linear_independence_exact_audit.py`. Machine-readable result: `candidate_gravity/results/iteration510_base_half_assembly_linear_independence_exact_audit.json`.

## Retained comparator preflight authority
Iteration 504 remains `BLOCKED_FIXED_COMPARATOR_QUOTIENT_UPSTREAM_TARGET_NOT_ASSEMBLED__NON_PROMOTING`. The concrete upstream algebraic target is not yet assembled, so comparator identity, rank loss, near-degeneracy, and novelty are not currently evaluable. This is operational BLOCKED, not scientific FAIL.

## Retained physical blocker
Frozen timelike `Tr U1^2` census remains 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per `q^2`. Iteration 421 run `33871920373` remains raw-valid `BLOCKED_CONVERGENCE`; diagnostic index-2 value is not authority. No zero-fill.

Max physical stability scaled `2.2720400683804223e-05` and max required fit residual scaled `2.585665489102237e-05` narrowly exceed their frozen `2e-05` limits, while structural, design-conditioning, analytic-denominator, radial and direct-original-integrand crosschecks remain healthy. Thresholds are not weakened.

## Frozen numerical/assembly contract
After all 28 distinct support coordinates are locally certified, evaluate BASE and HALF central4 assemblies independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Local MP PASS never substitutes for assembled derivative closure.

The frozen Iteration-424 high-precision fallback remains downstream of complete support closure and independent BASE/HALF assembly. It preserves the same mass nodes and parent dynamics, forbids smaller `h`, angular-grid escalation, threshold weakening and zero fill, and does not authorize bypassing ranks 23–27.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 510 closes an exact assembly linear-algebra guardrail, but no additional stable-rubric Candidate-Gravity component is complete.

## Exact downstream chain
After complete support closure: independent BASE/HALF MP80/120 assembly → frozen Iteration-424 reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Exact BASE/HALF coordinate overlap may share the local sampled precision certificate but never the derivative weight. BASE-minus-HALF is a derived diagnostic of the two independent BASE/HALF assembly rows and must not be counted as a third independent observable or Fisher constraint. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
