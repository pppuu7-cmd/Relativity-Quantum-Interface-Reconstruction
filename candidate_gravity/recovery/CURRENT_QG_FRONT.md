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
- Latest completed numerical mass-support authority: **Iteration 520**, raw-consumed frozen rank26 `(u,v)=(+5e-6,-2.5e-6)`, HALF local index 13, multiplicity 1.
- Latest authoritative research iteration: **Iteration 522**.
- Certified occurrence-weighted precision coverage: **`31/32 = 96.875% = 2480/2560`** row occurrences.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16. Frozen rank10 `(+5e-6,+5e-6)`, multiplicity 2, was already certified in Iteration 455 and must not be relaunched.

## Latest numerical authority — Iteration 520 rank26
Canonical rank26 `(u,v)=(+5e-6,-2.5e-6)`, HALF local index 13, multiplicity 1: run `34071968236`, job `101590847259`, artifact `10002375956`, head `4104d245ffa76525bfd30cdaf2a75cb210a0cd5c`.

Classification: `PASS_RAW_CONSUMED_MANIFEST_RANK26_FULL_Z_MP80_MP120__NON_PROMOTING`.

Artifact digest `sha256:5714cfcabdeefcabc4e8a9fbda9b9a22765a34ec9c5f0fba8ce6aeaa73c1c424`; scientific JSON SHA-256 `0e721e877be906bebffce0b4285b5ef0e808075dea69d63fac91d201cb681b08`; authority-audit SHA-256 `fb9e340bf65569ef74c04846a3bc4b0d8305ee55c9ad903a6029d43a60068356`.

Observed: `80/80` finite; max scaled MP80↔MP120 `3.16665900627325950036239838644e-80 <= 1e-30`; max radial Richardson scaled error `2.56450944838430094958318814512e-15 <= 5e-4`.

Machine-readable raw consumption: `candidate_gravity/results/post519_rank26_raw_consumption.json`, commit `6915f52883166ed140f7d4d0ab4bc9ecf84ee6b5`. This advances local precision support only; it does not promote physical index 2, assembled BASE/HALF closure, robust residual, ansatz authority, comparator novelty, or readiness.

## Active heavy gate — rank27
Frozen final untested support coordinate rank27 is `(u,v)=(+5e-6,+2.5e-6)`, HALF local index 14, multiplicity 1. Stage `candidate_gravity/code/post519_manifest_rank27_full_z_mp_stage.py`, commit `338233a1547730e6d59149fe486e78476cbb556f`; workflow `.github/workflows/rqir-post519-manifest-rank27-full-z-mp.yml`, commit `60a496cc1e878b830a95c465c278c044fd456667`; trigger/head `d122d18783fca2e6626555d906df48724c8110c5`.

Canonical run **`34078407905`**, job **`101608912613`**, is **in_progress**. Do not duplicate and do not assign scientific PASS before raw artifact consumption.

If rank27 raw-valid PASS, local support closure becomes `32/32 = 100% = 2560/2560` and the next gate is frozen independent BASE/HALF MP80/120 assembly. If BLOCKED, stop support progression and localize the first failing `z/phi/radial` sample without changing frozen dynamics, support order, thresholds, MP levels, radial hs, or angular grid.

## Exact assembly authority — Iterations 510–522
Iteration 510 established exact BASE/HALF row independence: `rank([W_BASE,W_HALF])=2`; `W_DELTA=W_BASE-W_HALF` adds no independent row. Exact Gram matrix `G=[[4225/5184,4/81],[4/81,4225/324]]`, determinant `5948843/559872`.

Iteration 511 established iid shared-node numerical covariance: `Cov(BASE,HALF)=(4/81)sigma^2/h^4`, correlation `64/4225`, `Var(BASE-HALF)=(23771/1728)sigma^2/h^4`.

Iteration 512 quantified exact Gram eigenvalues `(71825±sqrt(4016652769))/10368`, Gram condition number about `16.0041618209`, assembly singular-value condition number about `4.00052019379`.

Iteration 514 established distribution-free deterministic bounds `|delta BASE| <= (9/4) epsilon/h^2`, `|delta HALF| <= 9 epsilon/h^2`, and union-aggregated `|delta(BASE-HALF)| <= (397/36) epsilon/h^2`.

Iteration 516 generalized independent coordinate-error covariance to arbitrary variances `v_p>=0`: `Cov(BASE,HALF)=h^-4 (1/81) sum_shared v_p >=0`; each shared discrepancy coefficient is `25/144`.

Iteration 518 generalized to arbitrary PSD covariance `Sigma` over all 28 coordinates: `C_A=h^-4 A Sigma A^T` is PSD and `Var(BASE-HALF)=h^-4(w_BASE-w_HALF)^T Sigma (w_BASE-w_HALF)`. Under correlated PSD noise the BASE/HALF cross-covariance may have either sign.

Iteration 519 established the exact sufficient local-scaled→assembled-MP envelope contract. With local `eps=1e-30`, frozen assembled `tau=2e-6`, and `h=5e-6`, `sum_i|w_i|S_i<=5e13` is sufficient for assembled MP PASS, but local scaled PASS alone does not imply assembled PASS. The independent assembly gate remains mandatory.

Iteration 521 sharpened the same interval model to an exact minimax statement: if `|e_i|<=eps*S_i`, then `sup_box |delta A| = eps*h^-2 sum_i |w_i|S_i`, attained by sign alignment. Thus the Iteration-519 weighted envelope is the sharp universal worst-case radius under the stated coordinate-wise interval constraints; no smaller universal bound is valid without extra structure. This still does not replace direct assembled MP evaluation.

Iteration 522 established the exact midpoint form of the frozen assembled scaled metric. For `M=(A80+A120)/2` and `d=|A80-A120|`, `max(|A80|,|A120|)=|M|+d/2`, hence `scaled=d/max(1,|M|+d/2)`. At frozen `tau=2e-6=1/500000`, floor-branch PASS is `d<=tau`, while amplitude-branch PASS is exactly `d<=(2/999999)|M|`. For fixed midpoint magnitude and numerator radius `0<=d<=R`, exact worst-case transfer is `R/max(1,|M|+R/2)`. This is an audit/re-expression of the frozen metric and does not replace direct independent assembly.

These are numerical/provenance authorities only and create no physical covariance claim, consistency verdict, comparator identity, non-identifiability, near-degeneracy, novelty certificate, threshold change, or Fisher authorization.

## Retained comparator and physical blockers
Iteration 504 remains `BLOCKED_FIXED_COMPARATOR_QUOTIENT_UPSTREAM_TARGET_NOT_ASSEMBLED__NON_PROMOTING`: concrete upstream algebraic target is not assembled, so comparator identity/rank loss/near-degeneracy/novelty remain unevaluable. BLOCKED is not scientific FAIL.

Frozen timelike `Tr U1^2` census remains 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per `q^2`. Iteration 421 run `33871920373` remains raw-valid `BLOCKED_CONVERGENCE`; diagnostic index-2 value is not authority and no zero-fill is allowed. Max physical stability scaled `2.2720400683804223e-05` and max required fit residual scaled `2.585665489102237e-05` exceed frozen `2e-05`; thresholds are not weakened.

## Frozen numerical/assembly contract
After all 28 distinct support coordinates are locally certified, evaluate BASE and HALF central4 assemblies independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Local MP PASS never substitutes for assembled derivative closure.

The frozen Iteration-424 high-precision fallback remains downstream of complete support closure and independent BASE/HALF assembly. It preserves the same mass nodes and parent dynamics and forbids smaller `h`, angular-grid escalation, threshold weakening, zero fill, or support-gate bypass.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 522 closed an exact assembly-metric subgate but no additional stable-rubric sector.

## Exact downstream chain
Rank27 raw consumption → complete support closure → independent BASE/HALF MP80/120 assembly → frozen Iteration-424 reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Exact BASE/HALF coordinate overlap may share local sampled precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
