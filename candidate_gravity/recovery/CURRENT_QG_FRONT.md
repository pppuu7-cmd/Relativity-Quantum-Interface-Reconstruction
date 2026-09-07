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
- QUARTER rank5 raw authority: **Iteration 548**, `PASS_RAW_CONSUMED_ITER424_QUARTER_SUPPORT_RANK5_MP80_MP120__NON_PROMOTING`.
- Three-level exact diagnostics retained: **Iterations 530–533, 536–537, 540–541, 543–544, 546–547**; diagnostic-only, non-promoting.
- Latest authoritative research iteration: **Iteration 548**.

## Iteration 548 — rank5 raw-valid PASS
Canonical run `34136802871`, job `101789577462`, artifact `10026933360`, artifact digest `sha256:e510b1a440c3c6a0db21707d6742997d42f74e439f5c5a3a291c9562ac0b8d0a`, head `02fd19d47288d865fa281d05c281071292f1bc30`.

Frozen rank5 coordinate `(-1.25e-6,+1.25e-6)` passed `80/80` finite samples, max scaled MP80↔MP120 discrepancy `2.34754600067104515864190132656e-80 <= 1e-30`, and max radial Richardson scaled error `2.56641378819230025234854520759e-15 <= 5e-4`.

Raw `result.json` SHA-256: `2f50600679f26b42662fa6f0057394b1acf76717fd1eb64d01c25377ae955a6e`. Raw `authority_audit.json` SHA-256: `73e9de02a2bb9db0409909804033dd78b0fb66aed1d576d39ead196d162ea6c7`. The audit records `scientific_authority_pass=true` and the same result hash.

New QUARTER support closure is **5/12**. Including four exact HALF-overlap corners, authoritative full QUARTER-grid coordinate coverage is **9/16 = 56.25%**. This does not promote physical index 2.

Raw-consumption commit: `69f67a4ebdbc305b5ec697ef5bdf6a62f7e54041`.

## Retained diagnostic authority
Iterations 530–533, 536–537, 540–541, 543–544, 546–547 remain exact numerical/truncation diagnostics only. They do not replace any frozen Iteration-424 physical clause, do not promote physical index 2, and do not establish Candidate-Gravity consistency, comparator identity, model-level non-identifiability, identifiability, or novelty.

## Active heavy computation — rank6
Exactly one successor is authorized and running:
- rank: **6/12**;
- coordinate: `u=-1.25e-6`, `v=+2.5e-6`;
- run: `34146191135`;
- job: `101818626977`;
- raw-consumption commit: `69f67a4ebdbc305b5ec697ef5bdf6a62f7e54041`;
- stage commit: `805981104a00df7771e9001f6dac8b2b529ad87c`;
- workflow commit: `55a02dc9f22670965ac90d674bd14eeab61eacb7`;
- head/trigger commit: `873974adf2d406dff3ce49b6e155aa1b3b455065`;
- live state at Iteration-548 inspection: `in_progress`.

No duplicate rank6 heavy run is authorized. Workflow green alone must not be accepted; raw artifact consumption is mandatory before rank6 authority.

## Frozen Iteration-532 QUARTER order
1. `(-2.5e-6,-1.25e-6)` — raw PASS at Iteration 534
2. `(-2.5e-6,+1.25e-6)` — raw PASS at Iteration 538
3. `(-1.25e-6,-2.5e-6)` — raw PASS at Iteration 542
4. `(-1.25e-6,-1.25e-6)` — raw PASS at Iteration 545
5. `(-1.25e-6,+1.25e-6)` — raw PASS at Iteration 548
6. `(-1.25e-6,+2.5e-6)` — running
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

Readiness change: **0 percentage points**. Iteration 548 closes one local QUARTER support certificate only; no stable rubric sector closes.

## Exact next gate
After rank6 terminal completion: fail-closed raw-consume run `34146191135`. Only raw-valid PASS authorizes frozen rank7 `(+1.25e-6,-2.5e-6)`. Scientific FAIL/BLOCKED stops advancement; operational failure permits only minimal rank6 repair.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy retry. No unsupported `u<->v` substitution. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated until a concrete residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
