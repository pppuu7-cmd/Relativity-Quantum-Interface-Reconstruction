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
- QUARTER rank4 raw authority: **Iteration 545**, raw-valid PASS.
- QUARTER rank5 raw authority: **Iteration 548**, raw-valid PASS.
- QUARTER rank6 raw authority: **Iteration 550**, `PASS_RAW_CONSUMED_ITER424_QUARTER_SUPPORT_RANK6_MP80_MP120__NON_PROMOTING`.
- Three-level exact diagnostics retained: **Iterations 530–533, 536–537, 540–541, 543–544, 546–547, 549**; diagnostic-only, non-promoting.
- Latest authoritative research iteration: **Iteration 550**.

## Iteration 550 — rank6 raw-valid PASS
Canonical run `34146191135`, job `101818626977`, artifact `10028800076`, artifact digest `sha256:e50ed9622c2c10b47eb04953188a18b013a5c6f95a0caff30a39d25c9545f623`, head `873974adf2d406dff3ce49b6e155aa1b3b455065`.

Frozen rank6 coordinate `(-1.25e-6,+2.5e-6)` passed `80/80` finite samples, max scaled MP80↔MP120 discrepancy `2.76319909084802609340098697215e-80 <= 1e-30`, and max radial Richardson scaled error `2.56242664756055591440075169484e-15 <= 5e-4`.

Raw `result.json` SHA-256: `9a402fc89400b1d5a1e5e8fc888bc4dee87500e53a8371688d3f2b15e8c56192`. Raw `authority_audit.json` SHA-256: `fb95460b6c94c49be1487013d0b8602fcb9d31e7645e2f46127e146ab77898fe`. Audit records `scientific_authority_pass=true` and the same result hash.

New QUARTER support closure is **6/12**. Including four exact HALF-overlap corners, authoritative full QUARTER-grid coordinate coverage is **10/16 = 62.5%**. This does not promote physical index 2.

Raw-consumption commit: `61af909e0edb9adc4ee001e3dbeb17333c578130`.

## Retained diagnostic authority
Iterations 530–533, 536–537, 540–541, 543–544, 546–547, 549 remain exact numerical/truncation diagnostics only. They do not replace any frozen Iteration-424 physical clause, do not promote physical index 2, and do not establish Candidate-Gravity consistency, comparator identity, model-level non-identifiability, physical identifiability, or novelty. Iteration 549 specifically establishes only regime-specific non-identifiability of validating the three-level `h^4+h^6` truncation hypothesis from those same three levels.

## Active heavy computation — rank7
Exactly one successor is authorized and running:
- rank: **7/12**;
- coordinate: `u=+1.25e-6`, `v=-2.5e-6`;
- run: `34150468757`;
- job: `101831505133`;
- raw-consumption commit: `61af909e0edb9adc4ee001e3dbeb17333c578130`;
- stage commit: `1c7fca57de0d576128ba55c35b575c42c864bf89`;
- workflow commit: `86000d96b322859d8475579410eb755924926e7f`;
- head/trigger commit: `a4fa8c7cc215d1b0c1c156339d9865d12abd2558`;
- live state at Iteration-550 inspection: `in_progress`, scientific stage running; raw audit/upload pending.

No duplicate rank7 heavy run is authorized. Workflow green alone must not be accepted; raw artifact consumption is mandatory before rank7 authority.

## Frozen Iteration-532 QUARTER order
1. `(-2.5e-6,-1.25e-6)` — raw PASS at Iteration 534
2. `(-2.5e-6,+1.25e-6)` — raw PASS at Iteration 538
3. `(-1.25e-6,-2.5e-6)` — raw PASS at Iteration 542
4. `(-1.25e-6,-1.25e-6)` — raw PASS at Iteration 545
5. `(-1.25e-6,+1.25e-6)` — raw PASS at Iteration 548
6. `(-1.25e-6,+2.5e-6)` — raw PASS at Iteration 550
7. `(+1.25e-6,-2.5e-6)` — running
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

Readiness change: **0 percentage points**. Iteration 550 closes one additional non-promoting QUARTER support coordinate but no stable rubric sector closes.

## Exact next gate
After rank7 terminal completion: fail-closed raw-consume run `34150468757`. Only raw-valid PASS authorizes frozen rank8 `(+1.25e-6,-1.25e-6)`. Scientific FAIL/BLOCKED stops advancement; operational failure permits only minimal rank7 repair.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy retry. No unsupported `u<->v` substitution. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated until a concrete residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
