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
- QUARTER rank1 raw authority: **Iteration 534**, raw-valid PASS.
- QUARTER rank2 raw authority: **Iteration 538**, raw-valid PASS.
- QUARTER rank3 raw authority: **Iteration 542**, raw-valid PASS.
- QUARTER rank4 raw authority: **Iteration 545**, `PASS_RAW_CONSUMED_ITER424_QUARTER_SUPPORT_RANK4_MP80_MP120__NON_PROMOTING`.
- Three-level exact diagnostics retained: **Iterations 530–533, 536–537, 540–541, 543–544, 546–547**; diagnostic-only, non-promoting.
- Latest authoritative research iteration: **Iteration 547**.

## Iteration 545 — rank4 raw-valid PASS
Canonical run `34126397439`, job `101755969291`, artifact `10023337886`, artifact digest `sha256:5d40b3ad74539b4ef347b145ebe369b31e61dd0bd4ff6fc014e99e24ad998776`, head `0cb2f04ada4092c4d173a50276fffb36415109cf`.

Frozen rank4 coordinate `(-1.25e-6,-1.25e-6)` passed `80/80` finite samples, max scaled MP80↔MP120 discrepancy `3.3386016078648035112265066465e-80 <= 1e-30`, and max radial Richardson scaled error `2.5665078214717156908744567568e-15 <= 5e-4`.

Raw `result.json` SHA-256: `f1604ef9580be7b3a0d8b217785961d8bbb94c7e1bfa44849abe118b66816347`. Raw `authority_audit.json` SHA-256: `c728f956d8fa57254ed52e0a629c028ec1a4b62c7e22578f5a68d54d4a878567`. The artifact authority audit independently records `scientific_authority_pass=true` and the same result hash.

New QUARTER support closure is **4/12**. Including four exact HALF-overlap corners, authoritative full QUARTER-grid coordinate coverage is **8/16 = 50%**. This does not promote physical index 2.

Raw-consumption commit: `47523923fbea6d6214d033eef19a29f64160ccde`.

## Iteration 546 — exact level-error correlation contract
For the frozen three-level diagnostic define `d1=BASE-HALF`, `d2=HALF-QUARTER`, `P=64d2-d1`, `Q=d1-16d2`. With assembled level errors `e_BASE,e_HALF,e_QUARTER`, exact propagation gives

- `deltaP = -e_BASE + 65 e_HALF - 64 e_QUARTER`,
- `deltaQ = +e_BASE - 17 e_HALF + 16 e_QUARTER`.

For bounded level errors `|e_i|<=eps_i`, exact worst-case radii are

- `rho_P = eps_BASE + 65 eps_HALF + 64 eps_QUARTER`,
- `rho_Q = eps_BASE + 17 eps_HALF + 16 eps_QUARTER`.

For independent equal-variance level errors,

`Cov(P,Q)/sigma^2 = [[8322,-2130],[-2130,546]]`,

with determinant `6912>0` and correlation `-0.9992391156789705`. This is diagnostic numerical conditioning only, not Candidate-Gravity model-level near-degeneracy.

## Iteration 547 — exact P/Q innovation decorrelation contract
Iteration 547 factors the Iteration-546 equal-variance covariance exactly. Define

`R = Q + (355/1387) P`.

Then

- `Cov(P,R)=0` exactly;
- `Var(R)/sigma^2 = 1152/1387 = 0.8305695746214852...`;
- `C^{-1} sigma^2 = [[91/1152,355/1152],[355/1152,1387/1152]]`;
- the correct joint quadratic form is `chi_PQ = (91 P^2 + 710 P Q + 1387 Q^2)/(1152 sigma^2)`.

Under the frozen truncation map `P=(45/16)A`, `Q=(189/256)B`,

`R = (15975/22192) A + (189/256) B`.

Therefore R is a decorrelated numerical innovation, not a new pure truncation component or physical observable. The result prevents future joint diagnostics from double-counting the strongly anti-correlated P/Q directions as if they were independent.

Classification: `PASS_ITER424_PQ_INNOVATION_DECORRELATION_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

Machine authority: `candidate_gravity/results/iteration547_iter424_pq_innovation_decorrelation_contract.json`. Reproducible audit: `candidate_gravity/code/iteration547_iter424_pq_innovation_decorrelation_contract.py`.

## Retained diagnostic authority
Iterations 530–533, 536–537, 540–541, 543–544, 546–547 remain exact numerical/truncation diagnostics only. They do not replace any frozen Iteration-424 physical clause, do not promote physical index 2, and do not establish Candidate-Gravity consistency, comparator identity, model-level non-identifiability, identifiability, or novelty.

## Active heavy computation — rank5
Exactly one successor is authorized and running:
- rank: **5/12**;
- coordinate: `u=-1.25e-6`, `v=+1.25e-6`;
- run: `34136802871`;
- job: `101789577462`;
- raw-consumption commit: `47523923fbea6d6214d033eef19a29f64160ccde`;
- stage commit: `361fb0cc411971d159657fb3aa1ca2d39ddb9776`;
- workflow commit: `459f415a54774658b6dcf0fa7c58933361d3c2e7`;
- head/trigger commit: `02fd19d47288d865fa281d05c281071292f1bc30`;
- live state at Iteration-547 inspection: `in_progress`; scientific MP step active, raw authority audit and artifact upload pending.

No duplicate rank5 heavy run is authorized. Workflow green alone must not be accepted; raw artifact consumption is mandatory before rank5 authority.

## Frozen Iteration-532 QUARTER order
1. `(-2.5e-6,-1.25e-6)` — raw PASS at Iteration 534
2. `(-2.5e-6,+1.25e-6)` — raw PASS at Iteration 538
3. `(-1.25e-6,-2.5e-6)` — raw PASS at Iteration 542
4. `(-1.25e-6,-1.25e-6)` — raw PASS at Iteration 545
5. `(-1.25e-6,+1.25e-6)` — running
6. `(-1.25e-6,+2.5e-6)`
7. `(+1.25e-6,-2.5e-6)`
8. `(+1.25e-6,-1.25e-6)`
9. `(+1.25e-6,+1.25e-6)`
10. `(+1.25e-6,+2.5e-6)`
11. `(+2.5e-6,-1.25e-6)`
12. `(+2.5e-6,+1.25e-6)`.

PASS advances only to the next listed rank. Scientific FAIL/BLOCKED stops advancement and localizes the concrete failure under unchanged science. Operational failure permits only minimal technical repair and rerun of the same rank. Result-dependent reordering/skipping, unsupported `u<->v` substitution, zero-fill, threshold weakening, mass-node changes and precision changes are forbidden.

## Frozen Iteration-424 physical acceptance
After all 12 new QUARTER coordinates and QUARTER assembly are raw-closed, physical index 2 requires all simultaneously:
1. physical mass-step discrepancy `<=2e-5`;
2. direct original-integrand cross-check `<=2e-6`;
3. tensor-degree-(1,1) fit residual `<=2e-5`;
4. fixed-node MP80/MP120 agreement `|D_s(80)-D_s(120)|<=2e-6`;
5. finite outputs.

Only full PASS promotes index 2 and authorizes frozen exact15 continuation. A computed failing clause is a scoped scientific FAIL for this fallback route; an uncomputed clause is BLOCKED.

## Comparator blocker retained
The concrete upstream algebraic `Source/Ward/contact+K2` target and robust comparator-subtracted residual are absent. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 547 closes an exact joint numerical-error decorrelation subgate only; no stable rubric sector closes.

## Exact next gate
After rank5 terminal completion: fail-closed raw-consume run `34136802871`. Only raw-valid PASS authorizes frozen rank6 `(-1.25e-6,+2.5e-6)`. Scientific FAIL/BLOCKED stops advancement; operational failure permits only minimal rank5 repair.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy retry. No unsupported `u<->v` substitution. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated until a concrete residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
