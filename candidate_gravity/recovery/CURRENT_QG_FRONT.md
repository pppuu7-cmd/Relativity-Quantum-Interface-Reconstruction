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
- Latest completed numerical mass-support authority: **Iteration 515**, raw-consumed frozen rank24 `(u,v)=(+2.5e-6,+2.5e-6)`, HALF local index 10, multiplicity 1.
- Latest authoritative research iteration: **Iteration 516**.
- Certified occurrence-weighted precision coverage: **`29/32 = 90.625% = 2320/2560`** row occurrences.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16. Frozen rank10 `(+5e-6,+5e-6)`, multiplicity 2, was already certified in Iteration 455 and must not be relaunched.

## Latest numerical authority — Iteration 515 rank24
Canonical rank24 `(u,v)=(+2.5e-6,+2.5e-6)`, HALF local index 10, multiplicity 1: run `34063351852`, job `101567716622`, artifact `9999001385`, head `965841a77f63e30c3fd18e7ac0e495b51e7dc52f`.

Classification: `PASS_RAW_CONSUMED_MANIFEST_RANK24_FULL_Z_MP80_MP120__NON_PROMOTING`.

Artifact digest `sha256:bc7212cef5cb89cd2817726f7645199e515e28fe476d672130b3155889064b29`; scientific JSON SHA-256 `655cc19ecbdf0db078c8bd500ff7f257691a8695c1cdee28fbee65edd069e4ba`; authority-audit SHA-256 `e80f6b77c8b232b4e0db04d17975af59852dc049581073341532074039c1af81`.

Observed: `80/80` finite; max scaled MP80↔MP120 `1.83640479682421701214847913369e-80 <= 1e-30`; max radial Richardson scaled error `2.56417244121825547577146152507e-15 <= 5e-4`.

Machine-readable raw consumption: `candidate_gravity/results/post514_rank24_raw_consumption.json`. This advances local precision support only; it does not promote physical index 2, assembled BASE/HALF closure, robust residual, ansatz authority, comparator novelty, or readiness.

## Active heavy gate — rank25
Frozen rank25 is `(u,v)=(+2.5e-6,+5e-6)`, HALF local index 11, multiplicity 1. Stage `candidate_gravity/code/post515_manifest_rank25_full_z_mp_stage.py`; workflow `.github/workflows/rqir-post515-manifest-rank25-full-z-mp.yml`; trigger/head `50c8ebade8f163366848efefa860887b0843ea45`.

Canonical run **`34066294587`**, job **`101575523337`**, is **queued/in_progress**. Do not duplicate and do not assign scientific PASS before raw artifact consumption.

Only raw-valid rank25 PASS permits rank26 `(+5e-6,-2.5e-6)`, HALF local index 13, multiplicity 1. If BLOCKED, stop suffix progression and localize the first failing `z/phi/radial` sample without changing frozen dynamics, support order, thresholds, MP levels, radial hs, or angular grid.

## Frozen remaining suffix
- rank25 `(+2.5e-6,+5e-6)`, HALF local index 11;
- rank26 `(+5e-6,-2.5e-6)`, HALF local index 13;
- rank27 `(+5e-6,+2.5e-6)`, HALF local index 14.

Conditional coverage after future sequential raw-valid PASS: rank25 `30/32=93.750%`; rank26 `31/32=96.875%`; rank27 `32/32=100%`. These are arithmetic consequences only, not PASS claims.

## Exact assembly authority — Iterations 510–516
Iteration 510 established exact BASE/HALF row independence: `rank([W_BASE,W_HALF])=2`; `W_DELTA=W_BASE-W_HALF` adds no independent row. Exact Gram matrix `G=[[4225/5184,4/81],[4/81,4225/324]]`, determinant `5948843/559872`. BASE-minus-HALF is derived and never an extra Fisher constraint.

Iteration 511 established exact shared-node numerical covariance under the explicitly scoped iid equal-variance coordinate-error model: `Cov(BASE,HALF)=(4/81)sigma^2/h^4`, correlation `64/4225`, `Var(BASE-HALF)=(23771/1728)sigma^2/h^4`. This is numerical-error provenance, not physical covariance authority.

Iteration 512 quantified the exact Gram singular spectrum: eigenvalues `(71825±sqrt(4016652769))/10368`, approximately `0.81480824040386763744` and `13.0403229324356385354`; Gram condition number approximately `16.00416182091147668`, assembly singular-value condition number approximately `4.0005201937887373552`. This creates no new frozen threshold and no physical PASS.

Iteration 514 established a distribution-free deterministic assembly-error contract. If every absolute coordinate perturbation on the frozen 28-coordinate union obeys `|e_i|<=epsilon`, then `|delta BASE| <= (9/4) epsilon/h^2`, `|delta HALF| <= 9 epsilon/h^2`, and union-aggregated `|delta(BASE-HALF)| <= (397/36) epsilon/h^2`. Treating BASE/HALF separately gives the looser coefficient `45/4`; exact four-node shared-support aggregation reduces it by `2/9`, relative reduction `8/405`. Classification: `PASS_BASE_HALF_DETERMINISTIC_LINF_ERROR_OPERATOR_BOUND_EXACT__NON_PROMOTING`. This absolute bound does not turn local scaled MP discrepancies into assembled scaled discrepancies without an explicit common absolute normalization and creates no new threshold.

Iteration 516 removes the equal-variance restriction from Iteration 511 for independent coordinate errors. If `Var(e_p)=v_p>=0`, then `Var(BASE)=h^-4 sum_p w_B(p)^2 v_p`, `Var(HALF)=h^-4 sum_p w_H(p)^2 v_p`, and `Var(BASE-HALF)=h^-4 sum_p (w_B(p)-w_H(p))^2 v_p`. Only the four exact shared nodes contribute to cross-covariance, each with `w_B w_H=1/81`, so `Cov(BASE,HALF)=h^-4 (1/81) sum_shared v_p >=0`, with equality iff all four shared-node variances vanish. Each shared discrepancy coefficient is `25/144`. Classification: `PASS_BASE_HALF_HETEROSCEDASTIC_DIAGONAL_COVARIANCE_EXACT__NON_PROMOTING`. This is numerical-error provenance, not physical covariance authority, and creates no new threshold.

## Retained comparator and physical blockers
Iteration 504 remains `BLOCKED_FIXED_COMPARATOR_QUOTIENT_UPSTREAM_TARGET_NOT_ASSEMBLED__NON_PROMOTING`: concrete upstream algebraic target not assembled, so comparator identity/rank loss/near-degeneracy/novelty remain unevaluable. BLOCKED is not scientific FAIL.

Frozen timelike `Tr U1^2` census remains 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per `q^2`. Iteration 421 run `33871920373` remains raw-valid `BLOCKED_CONVERGENCE`; diagnostic index-2 value is not authority and no zero-fill is allowed. Max physical stability scaled `2.2720400683804223e-05` and max required fit residual scaled `2.585665489102237e-05` exceed frozen `2e-05`; thresholds are not weakened.

## Frozen numerical/assembly contract
After all 28 distinct support coordinates are locally certified, evaluate BASE and HALF central4 assemblies independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts. Local MP PASS never substitutes for assembled derivative closure.

The frozen Iteration-424 high-precision fallback remains downstream of complete support closure and independent BASE/HALF assembly. It preserves the same mass nodes and parent dynamics and forbids smaller `h`, angular-grid escalation, threshold weakening, zero fill, or bypassing ranks 25–27.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 516 strengthened exact numerical assembly/error-propagation provenance but completed no additional readiness-rubric sector.

## Exact downstream chain
Complete support closure → independent BASE/HALF MP80/120 assembly → frozen Iteration-424 reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Exact BASE/HALF coordinate overlap may share local sampled precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Shared BASE/HALF support coordinates induce nonzero numerical-error covariance under iid coordinate noise, and under independent heteroscedastic noise the exact covariance is `h^-4(1/81)sum_shared v_p`. Deterministic absolute assembly-error bounds cannot be substituted for assembled scaled-discrepancy gates without an explicit common absolute normalization. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
