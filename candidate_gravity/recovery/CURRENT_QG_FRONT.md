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
- u↔v non-equivalence authority: **Iteration 552**.
- independent u↔v replication/local alpha-shift response authority: **Iteration 553**, `PASS_ITER424_UV_SWAP_NON_EQUIVALENCE_REPLICATION_RANK2_RANK7__DIAGNOSTIC_ONLY_NON_PROMOTING`.
- Latest authoritative research iteration: **Iteration 553**.

## QUARTER progress
Raw-closed new coordinates: **7/12 = 58.333333333333336%**.
Including the four exact HALF-overlap corners, authoritative full QUARTER-grid coverage: **11/16 = 68.75%**.
Physical index2 remains unresolved and none of these local support PASS results alone promotes it.

### Raw-closed order
1. `(-2.5e-6,-1.25e-6)` — PASS Iteration 534
2. `(-2.5e-6,+1.25e-6)` — PASS Iteration 538
3. `(-1.25e-6,-2.5e-6)` — PASS Iteration 542
4. `(-1.25e-6,-1.25e-6)` — PASS Iteration 545
5. `(-1.25e-6,+1.25e-6)` — PASS Iteration 548
6. `(-1.25e-6,+2.5e-6)` — PASS Iteration 550
7. `(+1.25e-6,-2.5e-6)` — PASS Iteration 551
8. `(+1.25e-6,-1.25e-6)` — **active**
9. `(+1.25e-6,+1.25e-6)`
10. `(+1.25e-6,+2.5e-6)`
11. `(+2.5e-6,-1.25e-6)`
12. `(+2.5e-6,+1.25e-6)`.

PASS advances only to the next listed rank. Scientific FAIL/BLOCKED stops advancement and localizes the concrete failure under unchanged science. Operational failure permits only minimal technical repair and rerun of the same rank. Result-dependent reordering/skipping, u↔v substitution, zero-fill, threshold weakening, mass-node changes and precision changes are forbidden.

## Iteration 551 — rank7 raw-valid PASS
Canonical run `34150468757`, job `101831505133`, artifact `10030205964`, artifact digest `sha256:5a859a373d9d52a9c16df0b3b314c945933b90357602070da685f13cfcf05e00`, head `a4fa8c7cc215d1b0c1c156339d9865d12abd2558`.

Frozen rank7 `(+1.25e-6,-2.5e-6)` passed 80/80 finite samples, MP80↔MP120 max `2.76361789774773626392827156649e-80 <= 1e-30`, radial Richardson max `2.56569009619190897634187577318e-15 <= 5e-4`.

`result.json` SHA-256 `eb4d389813c6620c2436e8f1abe91e24625398163e2e01e5282d68addc80d98f`; `authority_audit.json` SHA-256 `59c21724191108b56b21d99623e7741a0161e08eb47d08a8d06d6f1201d75e3c`; audit binds the same result hash and records `scientific_authority_pass=true`.

Machine-readable authority: `candidate_gravity/results/iteration551_iter424_quarter_rank7_raw_consumption.json`.

## Active heavy computation — rank8
Exactly one successor is active:
- coordinate `(+1.25e-6,-1.25e-6)`;
- run `34153849866`;
- job `101841466120`;
- head/trigger `b1ec70bd5cab311921e514e31594b1476f1381ce`;
- latest live state: setup/checkout/Python/dependencies complete, full-z MP stage active, raw audit/upload pending;
- principal-stage completion **4/7 ≈57.1%**; no trustworthy within-stage percentage is exposed.

No duplicate rank8 run is authorized. Workflow success alone is not scientific authority.

## Iterations 552–553 — u↔v substitution ruled out and replicated
The current fixed-mass kinematics use
`lambda=s^2+u^2+v^2-2su-2sv-2uv`, `rho=sqrt(lambda)/(2 sqrt(s))`, and `alpha=-(s+u-v)/(2s)`.
`lambda` and `rho` are symmetric under u↔v, but `alpha` is not; exactly
`alpha(u,v)-alpha(v,u)=(v-u)/s`.
Since `p=-a+alpha*q+rho*unit(z,phi)`, swapped coordinates with `u!=v` are distinct routed physical points.

Iteration 552 raw-compared rank1/rank3. MP120 real values differ in 80/80 aligned z/phi rows; max absolute difference ≈`2.67304e-10`, max local relative difference ≈`1.12203e-4`; even the smallest difference is ≈`4.61e3` times the corresponding radial-error scale.

Iteration 553 independently replicated this with rank2/rank7. MP120 real values again differ in 80/80 rows; max absolute difference ≈`8.01905e-10`, max local relative difference ≈`3.36547e-4`; discrepancy/radial-error separation is at least ≈`1.388e4` and reaches ≈`9.437e6`.

The second pair has exactly three times the alpha-swap gap of the first pair. Corresponding signed raw swap differences have the same sign in 80/80 rows and scale by `2.999763...` to `3.000158...`, mean `2.999976...`. This supports the alpha-shift mechanism locally, not a general linearity theorem.

Consequences: `NO_UV_SYMMETRY_SUBSTITUTION` is evidence-backed and independently replicated. No remaining rank may be inferred from its swapped partner. These are diagnostic/provenance results, not Candidate-Gravity consistency FAILs and not physical index2 promotion.

Machine-readable authorities:
- `candidate_gravity/results/iteration552_iter424_uv_swap_non_equivalence_audit.json`
- `candidate_gravity/results/iteration553_iter424_uv_swap_replication_rank2_rank7.json`

## Retained three-level diagnostic lessons
- Iteration 530: exact three-level central4 Gram row rank 3.
- Iteration 531: normalized stencil geometry well-conditioned, scale-free `kappa_2≈1.04378`.
- Iteration 533: formal central4 truncation begins at `O(h^4)`; Richardson formulas diagnostic only.
- Iteration 536: exact h4/h6 component inversion exists but h8 aliases into fitted components.
- Iteration 537: unscaled h4/h6 inversion `kappa_2≈42.78`; diagnostic conditioning only.
- Iteration 540: pure h4/h6/h8 difference ratios 16/64/256; violations diagnose cancellation/omitted orders only.
- Iteration 541: R3 extrapolator noise amplification is modest (`L2` std factor ≈1.0869; uniform L1 factor ≈1.1693).
- Iteration 544: ratio-free P/Q sign-cone diagnostic is fail-closed under bounded errors.
- Iteration 546: P/Q errors are strongly anti-correlated in the equal-independent-level-error model (`rho≈-0.999239`), forbidding naive independent double counting.
- Iteration 547: exact decorrelated innovation exists for that diagnostic model.
- Iteration 549: three levels exactly saturate `X_s=D+A s^4+B s^6` (3 observations, 3 parameters, zero residual d.o.f.); BASE/HALF/QUARTER alone cannot test goodness-of-fit or exclude h8+ contamination. This is regime-specific diagnostic non-identifiability only and does not authorize an h=1/8 heavy run.

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

Readiness change: **0 percentage points**. Seven new QUARTER nodes are raw-closed and a false symmetry shortcut is ruled out twice, but no additional stable model-level rubric sector is complete.

## Exact downstream chain
BASE/HALF support **CLOSED 523** → provenance **CLOSED 526** → BASE/HALF assembly **CLOSED 527** → QUARTER manifest **529** → ranks1–7 **RAW PASS through 551** → rank8 **RUNNING** → ranks9–12 in frozen order → QUARTER assembly → unchanged Iteration-424 five-clause physical reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy retry. No u↔v support substitution. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated until a concrete residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.

## Exact next gate
Raw-consume canonical rank8 run `34153849866` after terminal completion. Only raw-valid PASS authorizes frozen rank9 `(+1.25e-6,+1.25e-6)`.
