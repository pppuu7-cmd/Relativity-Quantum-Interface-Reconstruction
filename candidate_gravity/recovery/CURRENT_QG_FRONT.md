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
- Latest completed BASE/HALF local mass-support authority: **Iteration 523**, `32/32 = 100% = 2560/2560` across 28 distinct coordinates.
- Latest assembled numerical authority: **Iteration 527**, raw-valid `PASS_RAW_CONSUMED_INDEPENDENT_BASE_HALF_MP80_MP120_ASSEMBLY__NON_PROMOTING`.
- Latest exact quarter-support structural authority: **Iteration 529**, `PASS_ITER424_QUARTER_SUPPORT_MANIFEST_EXACT__NON_PROMOTING`.
- Latest exact three-level operator-geometry authority: **Iteration 530**, `PASS_ITER424_BASE_HALF_QUARTER_CENTRAL4_GRAM_FULL_RANK_EXACT__NON_PROMOTING`.
- Latest exact normalized-conditioning authority: **Iteration 531**, `PASS_ITER424_BASE_HALF_QUARTER_NORMALIZED_GRAM_WELL_CONDITIONED_EXACT__NON_PROMOTING`.
- Latest exact quarter successor-order authority: **Iteration 532**, `PASS_ITER424_QUARTER_SUCCESSOR_ORDER_PREREGISTERED_EXACT__NON_PROMOTING`.
- Latest exact truncation-diagnostic authority: **Iteration 533**, `PASS_ITER424_CENTRAL4_THREE_LEVEL_TRUNCATION_GEOMETRY_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.
- Latest authoritative research iteration: **Iteration 533**.
- Active scientific prerequisite: **frozen Iteration-424 quarter-step (`h=1.25e-6`) direct-parent MP80/MP120 support, repaired rank1 run `34094463024`, job `101654832475`, currently in progress**.
- Current heavy-task progress: **4/7 principal workflow stages complete ≈ 57.1%** at last live inspection; full-z MP stage active, raw authority audit and artifact upload pending. No trustworthy within-stage numerical percentage is exposed.
- Current Iteration-533 research task: **100% complete**.

## Iteration 533 — exact three-level truncation/convergence diagnostic
For the frozen central4 first derivative,
`D_h f = f' - h^4 f^(5)/30 - h^6 f^(7)/252 - h^8 f^(9)/4320 + O(h^10)`.
Thus the mixed tensor-product derivative has a common formal leading `O(h^4)` truncation term under sufficient smoothness. Across BASE=`h`, HALF=`h/2`, QUARTER=`h/4`, the common h4 term scales `1:1/16:1/256` and the next h6 term scales `1:1/64:1/4096`.

Prospectively frozen diagnostics, fixed before QUARTER assembly:
- `(BASE-HALF)/(HALF-QUARTER) -> 16` if the common h4 term dominates and the denominator is nonzero;
- `R_BH=(16*HALF-BASE)/15` cancels the formal common h4 term;
- `R_HQ=(16*QUARTER-HALF)/15` cancels the formal common h4 term;
- `R_3=(BASE-80*HALF+1024*QUARTER)/945` cancels the formal common h4 and h6 terms.

Machine-readable audit: `candidate_gravity/results/iteration533_iter424_three_level_truncation_geometry_exact_audit.json`.

Critical guardrail: these are diagnostic formulas only. They do not alter the frozen five-clause Iteration-424 acceptance, cannot replace physical `D_s` by Richardson/extrapolated values, cannot rescue a failed mass-step clause, and do not authorize smaller h, threshold weakening, physical promotion, ANSATZ-003, Fisher, or resources.

## Iteration 532 — exact prospective quarter successor order
The complete order of the 12 new QUARTER coordinates is frozen before the active rank1 numerical result is known. It is the exact u-major/v-major Cartesian order from the frozen quarter axis support after removing only the four exact HALF-overlap corners:

1. `(-2.5e-6,-1.25e-6)`
2. `(-2.5e-6,+1.25e-6)`
3. `(-1.25e-6,-2.5e-6)`
4. `(-1.25e-6,-1.25e-6)`
5. `(-1.25e-6,+1.25e-6)`
6. `(-1.25e-6,+2.5e-6)`
7. `(+1.25e-6,-2.5e-6)`
8. `(+1.25e-6,-1.25e-6)`
9. `(+1.25e-6,+1.25e-6)`
10. `(+1.25e-6,+2.5e-6)`
11. `(+2.5e-6,-1.25e-6)`
12. `(+2.5e-6,+1.25e-6)`.

A raw-consumed PASS permits only the next listed rank; rank12 PASS permits quarter assembly. Scientific failure/block stops successor advancement and localizes the concrete failure under unchanged science. Operational failure permits only the minimal technical repair and rerun of the same rank. Result-dependent reordering/skipping, unsupported u↔v substitution, zero-fill, threshold weakening, mass-node changes and precision changes are forbidden.

Machine-readable audit: `candidate_gravity/results/iteration532_iter424_quarter_successor_order_exact_preregistration_audit.json`.

## Iteration 531 — exact normalized three-level conditioning gate
Exact row norms are `||B||=65/72`, `||H||=65/18`, `||Q||=130/9`. Exact normalized correlations are `rho(B,H)=64/4225`, `rho(B,Q)=0`, `rho(H,Q)=64/4225`, so the normalized Gram matrix is `[[1,64/4225,0],[64/4225,1,64/4225],[0,64/4225,1]]`.

Its exact eigenvalues are `1-64*sqrt(2)/4225`, `1`, `1+64*sqrt(2)/4225`; the exact scale-free condition number is `(4225+64*sqrt(2))/(4225-64*sqrt(2)) ≈ 1.0437827450175303`. The three frozen rows are therefore nearly orthogonal after removing the declared derivative scaling.

Machine-readable audit: `candidate_gravity/results/iteration531_iter424_three_level_normalized_gram_conditioning_exact_audit.json`.

## Iteration 530 — exact BASE/HALF/QUARTER central4 Gram gate
Using the frozen tensor-product central4 axis coefficients `(1,-8,+8,-1)/12` and base-step normalization `h=5e-6`, mixed-derivative scaling factors are BASE `1`, HALF `4`, QUARTER `16`. Exact support intersections are BASE∩HALF = four `(±5e-6,±5e-6)`, HALF∩QUARTER = four `(±2.5e-6,±2.5e-6)`, and BASE∩QUARTER = empty.

The exact Gram matrix is `[[4225/5184,4/81,0],[4/81,4225/324,64/81],[0,64/81,16900/81]]` with all leading principal minors positive, hence exact row rank 3.

## Iterations 528–529 — quarter-step prerequisite and exact support audit
The frozen Iteration-424 contract fixes mass steps `{5e-6,2.5e-6,1.25e-6}` and precision levels `{80,120}`. For `h=1.25e-6`, central4 axis support is `{-2.5e-6,-1.25e-6,+1.25e-6,+2.5e-6}` and the Cartesian grid has exactly 16 coordinates. Exact intersection with certified HALF support is only the four corners with both entries in `{±2.5e-6}`; therefore exactly 12 new quarter coordinates are necessary.

Iteration-528 initial run `34094343153`, job `101654453787`, failed operationally before sampling because of stale prerequisite-key names. Commit `fda4756f58aba6dce09f3c91cf44e8cce8afbade` repaired only schema binding. Canonical repaired trigger/head is `25c4f3ff1c2bf9ef66e0e5db6ace6580da4bb08d`; repaired run `34094463024` remains the authority candidate. Raw artifact must be consumed before scientific PASS is assigned.

## Frozen Iteration-424 full acceptance after quarter support closes
Full physical reevaluation remains unchanged and requires all simultaneously:
1. physical mass-step discrepancy `<=2e-5`;
2. direct original-integrand cross-check `<=2e-6`;
3. tensor-degree-(1,1) fit residual `<=2e-5`;
4. identical fixed-node 80/120-digit agreement `|D_s(80)-D_s(120)|<=2e-6`;
5. finite outputs.

Only full PASS promotes physical index 2 and authorizes frozen exact15 continuation. A computed failing clause is a scoped scientific FAIL for this fallback route. A missing/uncomputed clause is operational BLOCKED.

## Retained Iterations 525–527 authority
Iteration 526 closed BASE/HALF historical provenance with 28 frozen coordinates backed by 29 exact artifact parts. Iteration 527 raw-consumed run `34089957999`, job `101641252363`, artifact `10006477417`. Frozen assembly: all 80 samples finite; BASE MP80↔MP120 `0.0 <= 2e-6`; HALF MP80↔MP120 `0.0 <= 2e-6`; BASE↔HALF mass-step `8.60575121785458117805036434436e-7 <= 2e-5`; row rank 2; Gram determinant `5948843/559872 > 0`; `ds=-d_base`; no Richardson promotion; no threshold weakening.

## Retained comparator and physical blockers
Iteration 504 remains `BLOCKED_FIXED_COMPARATOR_QUOTIENT_UPSTREAM_TARGET_NOT_ASSEMBLED__NON_PROMOTING`: concrete upstream algebraic `Source/Ward/contact+K2` target is absent. Robust comparator-subtracted residual is absent. Iteration 421 remains raw-valid `BLOCKED_CONVERGENCE` for physical index 2 until the frozen Iteration-424 route is actually closed.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 533 closes an exact diagnostic/preinterpretation subgate but no additional model-level rubric sector.

## Exact downstream chain
BASE/HALF local support **CLOSED at 523** → multipart provenance **CLOSED at 526** → BASE/HALF assembly **CLOSED at 527** → quarter support manifest **EXACT at 529** → three-level Gram **EXACT/full-rank at 530** → normalized conditioning **EXACT/well-conditioned at 531** → quarter successor order **EXACT/preregistered at 532** → three-level truncation diagnostic **EXACT/preregistered at 533** → repaired quarter rank1 raw-consume → prospectively fixed ranks2–12 → quarter assembly → unchanged Iteration-424 five-clause physical reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy retry. No `u<->v` support substitution without exact frozen identity. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated until a concrete residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
