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
- Latest completed numerical mass-support authority: **Iteration 517**, raw-consumed frozen rank25 `(u,v)=(+2.5e-6,+5e-6)`, HALF local index 11, multiplicity 1.
- Latest authoritative research iteration: **Iteration 517**.
- Certified occurrence-weighted precision coverage: **`30/32 = 93.750% = 2400/2560`** row occurrences.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16. Frozen rank10 `(+5e-6,+5e-6)`, multiplicity 2, was already certified in Iteration 455 and must not be relaunched.

## Latest numerical authority — Iteration 517 rank25
Canonical rank25 `(u,v)=(+2.5e-6,+5e-6)`, HALF local index 11, multiplicity 1: run `34066294587`, job `101575523337`, artifact `9999994876`, head `50c8ebade8f163366848efefa860887b0843ea45`.

Classification: `PASS_RAW_CONSUMED_MANIFEST_RANK25_FULL_Z_MP80_MP120__NON_PROMOTING`.

Artifact digest `sha256:6bd866f34a732b7327702ac7d9ffc8b29f4077ff98c6b9b87191a9ff9f1bca1d`; scientific JSON SHA-256 `09a45246492011381c979c553229b37da61687334d951b62494e171367e074b7`; authority-audit SHA-256 `6cb116d0924fb2da7a43a0d5feab4261e850ec14d0d089647ad9a6ffb3490588`.

Observed: `80/80` finite; max scaled MP80↔MP120 `2.33746055489652415419659640715e-80 <= 1e-30`; max radial Richardson scaled error `2.57346381932435712702856966978e-15 <= 5e-4`.

Machine-readable raw consumption: `candidate_gravity/results/post516_rank25_raw_consumption.json`, commit `d05ee92c2c7deac6d7d5d097183f15027b54e49c`. This advances local precision support only; it does not promote physical index 2, assembled BASE/HALF closure, robust residual, ansatz authority, comparator novelty, or readiness.

## Active heavy gate — rank26
Frozen rank26 is `(u,v)=(+5e-6,-2.5e-6)`, HALF local index 13, multiplicity 1. Stage `candidate_gravity/code/post516_manifest_rank26_full_z_mp_stage.py`, commit `ea225ab7714042db5e5273739a1133b9b6284344`; workflow `.github/workflows/rqir-post516-manifest-rank26-full-z-mp.yml`, commit `0a260be7b2d706686f19863b8dbdcef50181dfda`; trigger/head `4104d245ffa76525bfd30cdaf2a75cb210a0cd5c`.

Canonical run **`34071968236`**, job **`101590847259`**, is **queued/in_progress**. Do not duplicate and do not assign scientific PASS before raw artifact consumption.

Only raw-valid rank26 PASS permits rank27 `(+5e-6,+2.5e-6)`, HALF local index 14, multiplicity 1. If BLOCKED, stop suffix progression and localize the first failing `z/phi/radial` sample without changing frozen dynamics, support order, thresholds, MP levels, radial hs, or angular grid.

## Frozen remaining suffix
- rank26 `(+5e-6,-2.5e-6)`, HALF local index 13;
- rank27 `(+5e-6,+2.5e-6)`, HALF local index 14.

Conditional coverage after future sequential raw-valid PASS: rank26 `31/32=96.875%`; rank27 `32/32=100%`. These are arithmetic consequences only, not PASS claims.

## Exact assembly authority — Iterations 510–516
Iteration 510 established exact BASE/HALF row independence: `rank([W_BASE,W_HALF])=2`; `W_DELTA=W_BASE-W_HALF` adds no independent row. Exact Gram matrix `G=[[4225/5184,4/81],[4/81,4225/324]]`, determinant `5948843/559872`.

Iteration 511 established iid shared-node numerical covariance: `Cov(BASE,HALF)=(4/81)sigma^2/h^4`, correlation `64/4225`, `Var(BASE-HALF)=(23771/1728)sigma^2/h^4`.

Iteration 512 quantified exact Gram eigenvalues `(71825±sqrt(4016652769))/10368`, Gram condition number about `16.0041618209`, assembly singular-value condition number about `4.00052019379`.

Iteration 514 established distribution-free deterministic bounds `|delta BASE| <= (9/4) epsilon/h^2`, `|delta HALF| <= 9 epsilon/h^2`, and union-aggregated `|delta(BASE-HALF)| <= (397/36) epsilon/h^2`.

Iteration 516 generalized independent coordinate-error covariance to arbitrary variances `v_p>=0`: `Cov(BASE,HALF)=h^-4 (1/81) sum_shared v_p >=0`; each shared discrepancy coefficient is `25/144`. These are numerical/provenance authorities only and create no new threshold.

## Retained comparator and physical blockers
Iteration 504 remains `BLOCKED_FIXED_COMPARATOR_QUOTIENT_UPSTREAM_TARGET_NOT_ASSEMBLED__NON_PROMOTING`: concrete upstream algebraic target is not assembled, so comparator identity/rank loss/near-degeneracy/novelty remain unevaluable. BLOCKED is not scientific FAIL.

Frozen timelike `Tr U1^2` census remains 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per `q^2`. Iteration 421 run `33871920373` remains raw-valid `BLOCKED_CONVERGENCE`; diagnostic index-2 value is not authority and no zero-fill is allowed. Max physical stability scaled `2.2720400683804223e-05` and max required fit residual scaled `2.585665489102237e-05` exceed frozen `2e-05`; thresholds are not weakened.

## Frozen numerical/assembly contract
After all 28 distinct support coordinates are locally certified, evaluate BASE and HALF central4 assemblies independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Local MP PASS never substitutes for assembled derivative closure.

The frozen Iteration-424 high-precision fallback remains downstream of complete support closure and independent BASE/HALF assembly. It preserves the same mass nodes and parent dynamics and forbids smaller `h`, angular-grid escalation, threshold weakening, zero fill, or bypassing ranks 26–27.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 517 closed one genuine local numerical-support gate but no additional readiness-rubric sector.

## Exact downstream chain
Complete support closure → independent BASE/HALF MP80/120 assembly → frozen Iteration-424 reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Exact BASE/HALF coordinate overlap may share local sampled precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
