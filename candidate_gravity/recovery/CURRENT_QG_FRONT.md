# Candidate Gravity Current Front

**Updated:** 2026-09-08  
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
- QUARTER ranks 1–8 raw authority: **Iterations 534, 538, 542, 545, 548, 550, 551, 556**, all raw-valid PASS and non-promoting.
- Three-level exact diagnostics retained: **Iterations 530–533, 536–537, 540–541, 543–544, 546–547, 549**; diagnostic-only, non-promoting.
- u↔v non-equivalence / routing diagnostics: **Iterations 552–555**.
- Exact central4 exchange-even projection / assembly-control authority: **Iteration 557**.
- Exact central4 tensor moment/null/norm integrity authority: **Iteration 558**.
- Exact QUARTER exchange-orbit closure/weight map authority: **Iteration 559**.
- Exact post-rank9 remaining-orbit tail/error contract: **Iteration 560**, `PASS_ITER424_REMAINING_ORBIT_TAIL_FAIL_CLOSED_CONTRACT_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.
- Latest authoritative research iteration: **Iteration 560**.

## QUARTER progress
Raw-closed new coordinates: **8/12 = 66.6666666667%**.
Including the four exact HALF-overlap corners, authoritative full QUARTER-grid coordinate coverage: **12/16 = 75%**.
Physical index2 remains unresolved and none of these local support PASS results alone promotes it.

### Frozen order
1. `(-2.5e-6,-1.25e-6)` — PASS Iteration 534
2. `(-2.5e-6,+1.25e-6)` — PASS Iteration 538
3. `(-1.25e-6,-2.5e-6)` — PASS Iteration 542
4. `(-1.25e-6,-1.25e-6)` — PASS Iteration 545
5. `(-1.25e-6,+1.25e-6)` — PASS Iteration 548
6. `(-1.25e-6,+2.5e-6)` — PASS Iteration 550
7. `(+1.25e-6,-2.5e-6)` — PASS Iteration 551
8. `(+1.25e-6,-1.25e-6)` — PASS Iteration 556
9. `(+1.25e-6,+1.25e-6)` — **active**
10. `(+1.25e-6,+2.5e-6)`
11. `(+2.5e-6,-1.25e-6)`
12. `(+2.5e-6,+1.25e-6)`.

PASS advances only to the next listed rank. Scientific FAIL/BLOCKED stops advancement and localizes the concrete failure under unchanged science. Operational failure permits only minimal technical repair and rerun of the same rank. Result-dependent reordering/skipping, u↔v substitution, zero-fill, threshold weakening, mass-node changes and precision changes are forbidden.

## Latest raw support authority — Iteration 556
Rank8 canonical run `34153849866`, job `101841466120`, artifact `10032056133`, digest `sha256:4ec3d3633b9bddeafd492ad6616350441515a21fed34a68794064ac45b0996bd`, head `b1ec70bd5cab311921e514e31594b1476f1381ce`.

Coordinate `(+1.25e-6,-1.25e-6)` passed `80/80` finite samples, MP80↔MP120 max `3.21415799361858209211589830142e-80 <= 1e-30`, radial Richardson max `2.56632452688472147151010572675e-15 <= 5e-4`. Machine-readable authority: `candidate_gravity/results/iteration556_iter424_quarter_rank8_raw_consumption.json`.

## Active heavy computation — rank9
Exactly one successor is active:
- coordinate `(+1.25e-6,+1.25e-6)`;
- run `34160111095`;
- job `101859912600`;
- head/trigger `7be4b22384c6680d669e88c0fb7990ba53ceff3e`;
- full-z MP80/MP120 stage in progress at Iteration560 check;
- raw audit/upload pending.

No duplicate rank9 run is authorized. Workflow success alone is not scientific authority. Only fail-closed raw-valid PASS may authorize rank10 `(+1.25e-6,+2.5e-6)`.

## Exact exchange/routing controls retained
Frozen fixed-mass kinematics use `lambda=s^2+u^2+v^2-2su-2sv-2uv`, `rho=sqrt(lambda)/(2 sqrt(s))`, `alpha=-(s+u-v)/(2s)`. Iterations 552–555 establish exact u↔v non-equivalence, including `p(u,v)=p(v,u)+[(v-u)/s]q`, and the midpoint decomposition `alpha=-1/2+d/s`, `lambda=s^2-4sm+4d^2`. No support substitution follows.

Iteration557 proves exact exchange-even projection for the frozen central4 tensor stencil. Iteration558 fixes the tensor moment/null/norm integrity contract. Iteration559 fixes the 10-orbit exchange ledger and exact coefficient sums.

## Iteration 560 — exact remaining-orbit tail contract
If rank9 raw-valid PASSes, only two exchange orbits remain incomplete:
- ranks6/11: `(-1,+2)<->(+2,-1)`, integer coefficients `+8,+8`, orbit sum `+16`;
- ranks10/12: `(+1,+2)<->(+2,+1)`, integer coefficients `-8,-8`, orbit sum `-16`.

Their combined integer coefficient is exactly zero. With orbit averages

`E_A=[F(-1,+2)+F(+2,-1)]/2`,

`E_B=[F(+1,+2)+F(+2,+1)]/2`,

the entire remaining normalized mixed-stencil contribution is exactly

`T_rem=(E_A-E_B)/(9 h^2)`.

Therefore a common constant offset across these four remaining coordinates cancels exactly. Fail-closed bounded-error propagation is

`|delta T_rem| <= (eps1+eps2+eps3+eps4)/(18 h^2)`

or, for orbit-average bounds,

`|delta T_rem| <= (eps_A+eps_B)/(9 h^2)`.

This is assembly/numerical conditioning only, not Candidate-Gravity model-level near-degeneracy or identifiability evidence. It does not authorize rank skipping, u↔v substitution, zero fill, or promotion.

Machine-readable authority: `candidate_gravity/results/iteration560_iter424_remaining_orbit_tail_contract_exact.json`.
Reproducible audit: `candidate_gravity/code/iteration560_iter424_remaining_orbit_tail_contract_exact.py`.

## Retained three-level diagnostic lessons
- Iteration530: exact three-level central4 Gram row rank 3.
- Iteration531: normalized stencil geometry well-conditioned, `kappa_2≈1.04378`.
- Iteration533: formal central4 truncation begins at `O(h^4)`.
- Iteration536: exact h4/h6 inversion exists but h8 aliases into fitted components.
- Iteration537: unscaled h4/h6 inversion `kappa_2≈42.78`.
- Iteration540: pure h4/h6/h8 difference ratios 16/64/256.
- Iteration541: R3 noise amplification modest (`L2≈1.0869`, uniform `L1≈1.1693`).
- Iteration544: ratio-free P/Q sign-cone diagnostic fail-closed under bounded errors.
- Iteration546: P/Q errors strongly anti-correlated (`rho≈-0.999239`) in the equal-independent-level-error model.
- Iteration547: exact decorrelated innovation exists for that diagnostic model.
- Iteration549: BASE/HALF/QUARTER saturate `X_s=D+A s^4+B s^6`; three levels cannot test goodness-of-fit or exclude h8+ contamination. No h=1/8 heavy computation is authorized.

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

Readiness change: **0 percentage points**. Iteration560 closes a genuine fail-closed assembly/error-propagation subgate, but no additional stable model-level rubric sector is complete.

## Exact downstream chain
BASE/HALF support **CLOSED 523** → provenance **CLOSED 526** → BASE/HALF assembly **CLOSED 527** → QUARTER manifest **529** → ranks1–8 **RAW PASS through 556** → rank9 **RUNNING** → ranks10–12 in frozen order → QUARTER assembly + exact tensor/orbit/tail controls → unchanged Iteration-424 five-clause physical reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy retry. No u↔v support substitution. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated until a concrete residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.

## Exact next gate
Inspect terminal state of rank9 run `34160111095`. Only raw-valid PASS authorizes frozen rank10 `(+1.25e-6,+2.5e-6)`.
