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
- BASE/HALF local mass support: **Iteration 523**, complete.
- Independent BASE/HALF MP80/MP120 assembly: **Iteration 527**, raw-valid PASS, non-promoting.
- QUARTER manifest: **Iteration 529**, 16-grid with 4 exact HALF-overlap corners and 12 required new coordinates.
- Frozen 12-rank QUARTER successor order: **Iteration 532**.
- QUARTER ranks 1–11 raw authority: **Iterations 534, 538, 542, 545, 548, 550, 551, 556, 562, 565, 569**, all raw-valid PASS and non-promoting.
- Exact routing/assembly/conditioning diagnostics through **Iteration 568** remain retained and non-promoting.
- Latest authoritative research iteration: **Iteration 569**.

## Latest raw support authority — Iteration 569
Rank11 coordinate `(+2.5e-6,-1.25e-6)` raw-consumed from run `34168897005`, job `101885271903`, artifact `10036490535`, digest `sha256:cb69bdb008038ea2720827027a2d038a825c090e6aad823c6dec2d4c9e36a93c`, head `7e4aeed3dc9ff1b376705d37c01156a35acdc293`.

Raw checks: `80/80` finite; MP80↔MP120 max `4.17918718237096998292577327888e-80 <= 1e-30`; radial Richardson max `2.56237524624410641222260979464e-15 <= 5e-4`. `result.json` SHA-256 `ac1b09b30e32fc17b0b45d300787bd89e2869df50edd41a85b256b578f0355ca`; `authority_audit.json` SHA-256 `7df980d2ada730d7f36b02691e0aafa9a9fa77f1cfb6abdd84e6e8cd63edbca7`.

Machine-readable authority: `candidate_gravity/results/iteration569_iter424_quarter_rank11_raw_consumption.json`.

## QUARTER progress
Raw-closed new coordinates: **11/12 = 91.666667%**.  
Including four exact HALF-overlap corners: **15/16 = 93.75%** authoritative coordinate coverage.  
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
10. `(+1.25e-6,+2.5e-6)` — PASS Iteration 565
11. `(+2.5e-6,-1.25e-6)` — PASS Iteration 569
12. `(+2.5e-6,+1.25e-6)` — **active**

PASS advances only according to the prospectively frozen order. Scientific FAIL/BLOCKED stops advancement. Operational failure permits only minimal technical repair and rerun of the same rank. No result-dependent reordering/skipping, u↔v substitution, zero-fill, threshold weakening, mass-node changes or precision changes.

## Active heavy computation — rank12
Exactly one successor is active:
- coordinate `(+2.5e-6,+1.25e-6)`;
- run `34175330006`;
- job `101903475600`;
- trigger/head `adc1288da49c1363907c2336162d344030ec47ef`;
- stage `candidate_gravity/code/post569_iter424_quarter_support_rank12_full_z_mp_stage.py`;
- workflow `.github/workflows/rqir-post569-iter424-quarter-rank12-full-z-mp.yml`;
- at first canonical check setup/checkout/Python were complete and frozen dependency installation was in progress; scientific stage/audit/upload pending.

No duplicate rank12 run is authorized. Workflow success alone is not authority. Only fail-closed raw-valid PASS closes the 12/12 new QUARTER support and authorizes full QUARTER assembly under the already frozen exact controls.

## Exact assembly/routing/conditioning controls retained
- Iterations 552–555: exact u↔v non-equivalence; no support substitution.
- Iteration 557: exchange-even projection identity for the complete matched central4 grid.
- Iteration 558: central4 tensor moment/null/norm integrity.
- Iteration 559: 10 exchange-orbit coefficient ledger.
- Iteration 560: remaining-orbit tail/error contract.
- Iteration 561: direct tensor, u→v, v→u and orbit-compressed assembly are coefficient-identical on the same complete raw-valid grid.
- Iteration 563: post-rank10 two-point tail contract.
- Iteration 564: final-pair common/differential mode decomposition; common mode is an exact stencil-null direction, but both ranks11/12 remain mandatory.
- Iteration 566: full-stencil rank-1 geometry and exact row/column nuisance annihilation.
- Iteration 567: 15-dimensional kernel of the single mixed-stencil functional; diagnostic regime-specific invisibility only, not model-level degeneracy.
- Iteration 568: iid coordinate variance leverage map; central four carry `4096/4225 ≈ 96.946746%` under equal independent numerical variances, with heteroskedastic generalization retained.

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

Readiness change: **0 percentage points**. Iteration569 closes one final-pair local support coordinate but no additional stable model-level rubric sector.

## Exact downstream chain
BASE/HALF support **CLOSED 523** → provenance **CLOSED 526** → BASE/HALF assembly **CLOSED 527** → QUARTER manifest **529** → ranks1–11 **RAW PASS through 569** → rank12 **RUNNING** → complete QUARTER raw consumption/assembly under Iterations557–568 controls → unchanged Iteration-424 five-clause physical reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy full-C5. No u↔v support substitution. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. Source/Born subtraction only in the matched observable after pole/cut-origin classification. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists.

## Exact next gate
Inspect terminal state and raw artifact of rank12 run `34175330006`, job `101903475600`. Only raw-valid PASS authorizes complete QUARTER assembly and unchanged Iteration-424 five-clause physical reevaluation.
