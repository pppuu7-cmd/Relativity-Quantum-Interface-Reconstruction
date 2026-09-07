# Candidate Gravity Current Front

**Updated:** 2026-09-07  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: **Iteration 411**.
- Latest raw-valid physical blocker: **Iteration 421 — `BLOCKED_CONVERGENCE`**, unresolved double-double index 2 / class 3 / `q^2=-1`; exact unresolved physical set `[2]`.
- BASE/HALF local mass support: **Iteration 523**, `32/32 = 100% = 2560/2560` across 28 distinct coordinates.
- Independent BASE/HALF MP80/MP120 assembly: **Iteration 527**, raw-valid PASS, non-promoting.
- QUARTER exact support manifest: **Iteration 529** — 16-grid, 4 exact HALF-overlap corners, 12 new coordinates required.
- Full 12-rank QUARTER successor order prospectively frozen: **Iteration 532**.
- QUARTER ranks 1–7 raw authority: **Iterations 534, 538, 542, 545, 548, 550, 551**, all raw-valid PASS and non-promoting.
- Three-level exact diagnostics retained: **Iterations 530–533, 536–537, 540–541, 543–544, 546–547, 549**; diagnostic-only, non-promoting.
- u↔v non-equivalence authority: **Iteration 552**, `PASS_ITER424_UV_SWAP_NON_EQUIVALENCE_RANK1_RANK3__DIAGNOSTIC_ONLY_NON_PROMOTING`.
- Latest authoritative research iteration: **Iteration 552**.

## Iteration 551 — rank7 raw-valid PASS
Canonical run `34150468757`, job `101831505133`, artifact `10030205964`, artifact digest `sha256:5a859a373d9d52a9c16df0b3b314c945933b90357602070da685f13cfcf05e00`, head `a4fa8c7cc215d1b0c1c156339d9865d12abd2558`.

Frozen rank7 coordinate `(+1.25e-6,-2.5e-6)` passed `80/80` finite samples. Max scaled MP80↔MP120 discrepancy `2.76361789774773626392827156649e-80 <= 1e-30`; max radial Richardson scaled error `2.56569009619190897634187577318e-15 <= 5e-4`.

Raw `result.json` SHA-256 `eb4d389813c6620c2436e8f1abe91e24625398163e2e01e5282d68addc80d98f`; raw `authority_audit.json` SHA-256 `59c21724191108b56b21d99623e7741a0161e08eb47d08a8d06d6f1201d75e3c`. Audit binds the same result hash and records `scientific_authority_pass=true`.

New QUARTER support closure is **7/12 = 58.333333333333336%**. Including four exact HALF-overlap corners, authoritative full QUARTER-grid coordinate coverage is **11/16 = 68.75%**. Physical index2 is not promoted.

Machine-readable authority: `candidate_gravity/results/iteration551_iter424_quarter_rank7_raw_consumption.json`.

## Active heavy computation — rank8
Exactly one successor is authorized and running:
- rank: **8/12**;
- coordinate: `u=+1.25e-6`, `v=-1.25e-6`;
- run: `34153849866`;
- job: `101841466120`;
- head/trigger commit: `b1ec70bd5cab311921e514e31594b1476f1381ce`;
- latest live state: setup/checkout/Python/dependencies complete; scientific full-z MP stage active; raw audit/upload pending;
- principal-stage completion: **4/7 ≈ 57.1%**. No trustworthy within-stage percentage is exposed.

No duplicate rank8 heavy run is authorized. Workflow success alone must not be accepted; raw artifact consumption is mandatory.

## Iteration 552 — u↔v swap non-equivalence
Already raw-consumed rank1 `(-2.5e-6,-1.25e-6)` and rank3 `(-1.25e-6,-2.5e-6)` were compared row-by-row using their original authoritative artifacts. All 80 rows align exactly in z/phi. MP120 real values differ in **80/80** rows.

Observed swap discrepancy:
- minimum absolute real difference ≈ `8.07090e-13`;
- maximum absolute real difference ≈ `2.67304e-10`;
- maximum relative-to-local-value difference ≈ `1.12203e-4`;
- the smallest discrepancy is ≈ `4.61e3` times the larger corresponding pairwise radial-error estimate;
- the strongest discrepancy/error separation is ≈ `3.26e6`.

The source geometry explains the non-equivalence exactly. For fixed `s=-q^2`,
`lambda=s^2+u^2+v^2-2su-2sv-2uv` and `rho=sqrt(lambda)/(2 sqrt(s))` are symmetric under u↔v, but
`alpha=-(s+u-v)/(2s)` is not. In fact,
`alpha(u,v)-alpha(v,u)=(v-u)/s`.
The routed physical point `p=-a+alpha*q+rho*unit(z,phi)` therefore changes under a swap whenever `u!=v`.

Consequences:
- universal u↔v equality is rejected for the current parent implementation;
- the Iteration-532 `NO_UV_SYMMETRY_SUBSTITUTION` guardrail is positively justified;
- no remaining rank may be skipped or replaced by a swapped partner;
- this is not a Candidate-Gravity consistency FAIL and does not promote physical index2.

Machine-readable authority: `candidate_gravity/results/iteration552_iter424_uv_swap_non_equivalence_audit.json`.

## Frozen Iteration-532 QUARTER order
1. `(-2.5e-6,-1.25e-6)` — raw PASS at Iteration 534
2. `(-2.5e-6,+1.25e-6)` — raw PASS at Iteration 538
3. `(-1.25e-6,-2.5e-6)` — raw PASS at Iteration 542
4. `(-1.25e-6,-1.25e-6)` — raw PASS at Iteration 545
5. `(-1.25e-6,+1.25e-6)` — raw PASS at Iteration 548
6. `(-1.25e-6,+2.5e-6)` — raw PASS at Iteration 550
7. `(+1.25e-6,-2.5e-6)` — raw PASS at Iteration 551
8. `(+1.25e-6,-1.25e-6)` — running
9. `(+1.25e-6,+1.25e-6)`
10. `(+1.25e-6,+2.5e-6)`
11. `(+2.5e-6,-1.25e-6)`
12. `(+2.5e-6,+1.25e-6)`.

PASS advances only to the next listed rank. Scientific FAIL/BLOCKED stops advancement and localizes the concrete failure under unchanged science. Operational failure permits only minimal technical repair and rerun of the same rank. Result-dependent reordering/skipping, u↔v substitution, zero-fill, threshold weakening, mass-node changes and precision changes are forbidden.

## Retained three-level diagnostic lessons
- Iteration 530: exact BASE/HALF/QUARTER central4 Gram has row rank 3.
- Iteration 531: normalized three-level stencil geometry is well-conditioned, scale-free `kappa_2≈1.04378`.
- Iteration 533: central4 truncation begins at formal `O(h^4)`; three-level Richardson formulas are diagnostic only.
- Iteration 536: exact h4/h6 component estimators are available, but h8 aliases into them.
- Iteration 537: unscaled h4/h6 inversion is invertible with `kappa_2≈42.78`; this is diagnostic conditioning, not model-level near-degeneracy.
- Iteration 540: pure h4/h6/h8 difference ratios are 16/64/256; ratio violations imply cancellation and/or omitted orders, not Candidate-Gravity failure.
- Iteration 541: three-level extrapolator `R3` has modest noise amplification only (`L2` std factor ≈1.0869; uniform L1 factor ≈1.1693).
- Iteration 544: ratio-free P/Q sign-cone inference is fail-closed under bounded level errors.
- Iteration 546: P/Q diagnostic errors are strongly anti-correlated under equal independent level variance (`rho≈-0.999239`), so naive double-counting is forbidden.
- Iteration 547: an exact decorrelated innovation exists for that diagnostic error model.
- Iteration 549: with only BASE/HALF/QUARTER, `X_s=D+A s^4+B s^6` is saturated (3 observations, 3 parameters, zero residual degrees of freedom). Thus the same three levels cannot provide a goodness-of-fit test for absence of h8/higher contamination. This is regime-specific diagnostic non-identifiability only; no extra h=1/8 run is authorized by it.

## Frozen Iteration-424 physical acceptance
After all 12 new QUARTER coordinates and QUARTER assembly are raw-closed, physical index2 requires all simultaneously:
1. physical mass-step discrepancy `<=2e-5`;
2. direct original-integrand cross-check `<=2e-6`;
3. tensor-degree-(1,1) fit residual `<=2e-5`;
4. fixed-node MP80/MP120 agreement `|D_s(80)-D_s(120)|<=2e-6`;
5. finite outputs.

Only full PASS promotes physical index2 and authorizes frozen exact15 continuation. A computed failing clause is a scoped scientific FAIL for this fallback route; an uncomputed clause is BLOCKED.

## Comparator blocker retained
The concrete upstream algebraic `Source/Ward/contact+K2` target and robust comparator-subtracted residual remain absent. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Seven new QUARTER coordinates are raw-closed and a false symmetry shortcut is ruled out, but no additional stable model-level rubric sector is complete.

## Exact downstream chain
BASE/HALF support **CLOSED 523** → provenance **CLOSED 526** → BASE/HALF assembly **CLOSED 527** → QUARTER manifest **529** → ranks1–7 **RAW PASS through 551** → rank8 **RUNNING** → ranks9–12 in frozen order → QUARTER assembly → unchanged Iteration-424 five-clause physical reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy retry. No u↔v support substitution. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated until a concrete residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.

## Exact next gate
Raw-consume canonical rank8 run `34153849866` after terminal completion. Only raw-valid PASS authorizes frozen rank9 `(+1.25e-6,+1.25e-6)`.
