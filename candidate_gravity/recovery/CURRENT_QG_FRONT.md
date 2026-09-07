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
- QUARTER manifest: **Iteration 529**, 16-grid with 4 exact HALF-overlap corners and 12 required new coordinates.
- Frozen 12-rank QUARTER successor order: **Iteration 532**.
- QUARTER ranks 1–10 raw authority: **Iterations 534, 538, 542, 545, 548, 550, 551, 556, 562, 565**, all raw-valid PASS and non-promoting.
- Exact routing/assembly diagnostics through **Iteration 566** remain retained and non-promoting.
- Latest authoritative research iteration: **Iteration 566**.

## Latest raw support authority — Iteration 565
Rank10 coordinate `(+1.25e-6,+2.5e-6)` raw-consumed from run `34165534613`, job `101875710349`, artifact `10034846108`, digest `sha256:707e4fffa3dddcac5eb5d7dc127afcb0afd8c13c85b99c230ea57abacdb3b97d`, head `358bcfc29494fbd615397ba72314e1e10d9e7417`.

Raw checks: `80/80` finite; MP80↔MP120 max `2.23136782466149871841320727933e-80 <= 1e-30`; radial Richardson max `2.57085585035539296413124070504e-15 <= 5e-4`. `result.json` SHA-256 `7cc11967da91eb299bd7a5c4e2c96525ff60c34ec0a4fc0f80e839c36601dc84`; `authority_audit.json` SHA-256 `10f2d13a6165e98a3aaca5cbf85be4d6293ce537c0f4271e9e13e3bbd5c8d645`.

Machine-readable authority: `candidate_gravity/results/iteration565_iter424_quarter_rank10_raw_consumption.json`.

## Iteration 566 exact assembly geometry
The frozen 4x4 QUARTER central4 mixed-derivative coefficient matrix is `C=w⊗w`, `w=[1,-8,+8,-1]`, normalization `1/(144 h^2)`.

Exact pre-registered properties:
- `rank(C)=1`;
- every row sum and column sum vanishes;
- any additive grid nuisance `F_ij=a_i+b_j+c` is annihilated exactly;
- the additive row/column nuisance subspace has dimension `7` in the 16-coordinate grid;
- common coordinate-wise bounded error gain is `9/(4 h^2)`;
- independent equal-variance standard-deviation gain is `65/(72 h^2)` and variance gain `4225/(5184 h^4)`.

Classification: `PASS_ITER424_QUARTER_FULL_STENCIL_GEOMETRY_ERROR_NORM_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`. This is stencil/assembly geometry only, not Candidate-Gravity model-level non-identifiability, near-degeneracy, comparator identity, consistency PASS/FAIL, or novelty evidence.

## QUARTER progress
Raw-closed new coordinates: **10/12 = 83.333333%**.  
Including four exact HALF-overlap corners: **14/16 = 87.5%** authoritative coordinate coverage.  
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
11. `(+2.5e-6,-1.25e-6)` — **active**
12. `(+2.5e-6,+1.25e-6)`

PASS advances only to the next listed rank. Scientific FAIL/BLOCKED stops advancement. Operational failure permits only minimal technical repair and rerun of the same rank. No result-dependent reordering/skipping, u↔v substitution, zero-fill, threshold weakening, mass-node changes or precision changes.

## Active heavy computation — rank11
Exactly one successor is active:
- coordinate `(+2.5e-6,-1.25e-6)`;
- run `34168897005`;
- job `101885271903`;
- trigger/head `7e4aeed3dc9ff1b376705d37c01156a35acdc293`;
- stage `candidate_gravity/code/post565_iter424_quarter_support_rank11_full_z_mp_stage.py`;
- workflow `.github/workflows/rqir-post565-iter424-quarter-rank11-full-z-mp.yml`.

No duplicate rank11 run is authorized. Workflow success alone is not authority. Only fail-closed raw-valid PASS may authorize rank12 `(+2.5e-6,+1.25e-6)`.

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

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy full-C5. No u↔v support substitution. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. Source/Born subtraction only in the matched observable after pole/cut-origin classification. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists.

## Exact next gate
Inspect terminal state and raw artifact of rank11 run `34168897005`, job `101885271903`. Only raw-valid PASS authorizes frozen rank12 `(+2.5e-6,+1.25e-6)`.
