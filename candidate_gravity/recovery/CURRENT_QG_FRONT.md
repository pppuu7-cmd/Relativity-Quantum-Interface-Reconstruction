# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: **Iteration 411**.
- Latest raw-valid physical blocker: **Iteration 421 — `BLOCKED_CONVERGENCE`**, unresolved double-double index 2 / class 3 / `q^2=-1`; unresolved physical set `[2]`.
- BASE/HALF local mass support: **Iteration 523**, `32/32 = 100% = 2560/2560` across 28 distinct coordinates.
- Independent BASE/HALF MP80/MP120 assembly: **Iteration 527**, raw-valid PASS, non-promoting.
- QUARTER manifest: **Iteration 529**, 16-grid with 4 exact HALF-overlap corners and 12 required new coordinates.
- Frozen 12-rank QUARTER successor order: **Iteration 532**.
- QUARTER ranks 1–9 raw authority: **Iterations 534, 538, 542, 545, 548, 550, 551, 556, 562**, all raw-valid PASS and non-promoting.
- Three-level diagnostics retained: **Iterations 530–533, 536–537, 540–541, 543–544, 546–547, 549**.
- u↔v routing/non-equivalence controls: **Iterations 552–555**.
- Central4 exchange/tensor/orbit controls: **Iterations 557–559**.
- Remaining-orbit tail/error contract: **Iteration 560**.
- Four-route QUARTER assembly identity and exact polynomial audit: **Iteration 561**.
- Latest authoritative research iteration: **Iteration 562**.

## QUARTER progress
Raw-closed new coordinates: **9/12 = 75%**.  
Including four exact HALF-overlap corners: **13/16 = 81.25%** authoritative coordinate coverage.  
These local support PASSes do not promote physical index2.

### Frozen order
1. `(-2.5e-6,-1.25e-6)` — PASS Iteration 534
2. `(-2.5e-6,+1.25e-6)` — PASS Iteration 538
3. `(-1.25e-6,-2.5e-6)` — PASS Iteration 542
4. `(-1.25e-6,-1.25e-6)` — PASS Iteration 545
5. `(-1.25e-6,+1.25e-6)` — PASS Iteration 548
6. `(-1.25e-6,+2.5e-6)` — PASS Iteration 550
7. `(+1.25e-6,-2.5e-6)` — PASS Iteration 551
8. `(+1.25e-6,-1.25e-6)` — PASS Iteration 556
9. `(+1.25e-6,+1.25e-6)` — PASS Iteration 562
10. `(+1.25e-6,+2.5e-6)` — **active**
11. `(+2.5e-6,-1.25e-6)`
12. `(+2.5e-6,+1.25e-6)`

PASS advances only to the next listed rank. Scientific FAIL/BLOCKED stops advancement. Operational failure permits only minimal technical repair and rerun of the same rank. No result-dependent reordering/skipping, u↔v substitution, zero-fill, threshold weakening, mass-node changes or precision changes.

## Latest raw support authority — Iteration 562
Rank9 canonical run `34160111095`, job `101859912600`, artifact `10033936398`, digest `sha256:468faa9c58ec9c3b52e9f54019179a31cc0ad22f60b19ca9b22a150769ae9089`, head `7be4b22384c6680d669e88c0fb7990ba53ceff3e`.

Coordinate `(+1.25e-6,+1.25e-6)` passed `80/80` finite samples, MP80↔MP120 max `2.87050685346696177473651157805e-80 <= 1e-30`, radial Richardson max `2.56144587232444581891553122549e-15 <= 5e-4`. `result.json` SHA-256 `63054690757baee587ef0c07cf753b3196fbdf63a42a14280c4d2ba4b665ab26` matches the authority audit; audit-file SHA-256 `db2025540fea6d733a426da750884a1293e67f3bca6d05a1fe24dfd197e69572`.

Machine-readable authority: `candidate_gravity/results/iteration562_iter424_quarter_rank9_raw_consumption.json`.

## Active heavy computation — rank10
Exactly one successor is authorized and triggered:
- coordinate `(+1.25e-6,+2.5e-6)`;
- canonical run `34165534613`;
- trigger/head `358bcfc29494fbd615397ba72314e1e10d9e7417`;
- stage `candidate_gravity/code/post562_iter424_quarter_support_rank10_full_z_mp_stage.py`;
- workflow `.github/workflows/rqir-post562-iter424-quarter-rank10-full-z-mp.yml`.

No duplicate rank10 run is authorized. Workflow success alone is not authority. Only fail-closed raw-valid PASS may authorize rank11 `(+2.5e-6,-1.25e-6)`.

## Exact assembly/routing controls retained
Frozen fixed-mass kinematics use `lambda=s^2+u^2+v^2-2su-2sv-2uv`, `rho=sqrt(lambda)/(2 sqrt(s))`, `alpha=-(s+u-v)/(2s)`. Iterations 552–555 establish u↔v non-equivalence; no support substitution follows.

Iterations 557–559 freeze exchange-even projection, tensor moment/null/norm integrity and 10-orbit coefficient bookkeeping. Iteration560 fixes the remaining-tail relation `T_rem=(E_A-E_B)/(9 h^2)` and fail-closed error propagation. Iteration561 freezes coefficient-level equality of direct tensor, sequential u→v, sequential v→u and orbit-compressed assembly on the same complete raw-valid grid. Route disagreement is an assembly/index/orientation failure, not a physical residual.

## Frozen Iteration-424 physical acceptance
After all 12 new QUARTER coordinates and QUARTER assembly are raw-closed, physical index2 requires all simultaneously:
1. physical mass-step discrepancy `<=2e-5`;
2. direct original-integrand cross-check `<=2e-6`;
3. tensor-degree-(1,1) fit residual `<=2e-5`;
4. fixed-node MP80/MP120 agreement `|D_s(80)-D_s(120)|<=2e-6`;
5. finite outputs.

Only full PASS promotes physical index2 and authorizes frozen exact15 continuation. A computed failing clause is a scoped scientific FAIL; an uncomputed clause is BLOCKED.

## Comparator blocker retained
Concrete upstream algebraic `Source/Ward/contact+K2` target and robust comparator-subtracted residual remain absent. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration562 closes one additional local QUARTER support coordinate only.

## Exact downstream chain
BASE/HALF support **CLOSED 523** → provenance **CLOSED 526** → BASE/HALF assembly **CLOSED 527** → QUARTER manifest **529** → ranks1–9 **RAW PASS through 562** → rank10 **ACTIVE** → ranks11–12 in frozen order → QUARTER assembly under exact tensor/orbit/tail/four-route controls → unchanged Iteration-424 five-clause physical reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy full-C5. No u↔v support substitution. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. Source/Born subtraction only in the matched observable after pole/cut-origin classification. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists.

## Exact next gate
Inspect terminal state and raw artifact of rank10 run `34165534613`. Only raw-valid PASS authorizes frozen rank11 `(+2.5e-6,-1.25e-6)`.
