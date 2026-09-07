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
- QUARTER ranks 1–8 raw authority: **Iterations 534, 538, 542, 545, 548, 550, 551, 556**, all raw-valid PASS and non-promoting.
- Three-level exact diagnostics retained: **Iterations 530–533, 536–537, 540–541, 543–544, 546–547, 549**; diagnostic-only, non-promoting.
- u↔v non-equivalence / routing diagnostics: **Iterations 552–555**.
- Exact central4 exchange-even projection / assembly-control authority: **Iteration 557**, `PASS_ITER424_CENTRAL4_MIXED_DERIVATIVE_EXCHANGE_EVEN_PROJECTION_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.
- Latest authoritative research iteration: **Iteration 557**.

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

## Iteration 556 — rank8 raw-valid PASS
Canonical run `34153849866`, job `101841466120`, artifact `10032056133`, artifact digest `sha256:4ec3d3633b9bddeafd492ad6616350441515a21fed34a68794064ac45b0996bd`, head `b1ec70bd5cab311921e514e31594b1476f1381ce`.

Frozen rank8 `(+1.25e-6,-1.25e-6)` passed `80/80` finite samples, MP80↔MP120 max `3.21415799361858209211589830142e-80 <= 1e-30`, radial Richardson max `2.56632452688472147151010572675e-15 <= 5e-4`.

Raw `result.json` SHA-256 `8d498f746c5ee5aecb24949259227ac81731ff007ca1c8681b8169e510962cdb`; raw `authority_audit.json` SHA-256 `7416d9e1e2e2e51c9fd348092298caf11aa7f50f9db3e4e93dc412a191bb8bb7`; the audit binds the same result hash and records `scientific_authority_pass=true`.

Machine-readable authority: `candidate_gravity/results/iteration556_iter424_quarter_rank8_raw_consumption.json`.

## Active heavy computation — rank9
Exactly one successor is active:
- coordinate `(+1.25e-6,+1.25e-6)`;
- run `34160111095`;
- job `101859912600`;
- head/trigger `7be4b22384c6680d669e88c0fb7990ba53ceff3e`;
- setup/checkout/Python/dependencies complete;
- full-z MP80/MP120 stage in progress;
- raw audit/upload pending.

No duplicate rank9 run is authorized. Workflow success alone is not scientific authority. Only a fail-closed raw-valid PASS may authorize rank10 `(+1.25e-6,+2.5e-6)`.

## Iterations 552–555 — exact u↔v routing structure
The frozen fixed-mass kinematics use
`lambda=s^2+u^2+v^2-2su-2sv-2uv`, `rho=sqrt(lambda)/(2 sqrt(s))`, and `alpha=-(s+u-v)/(2s)`.

`lambda` and `rho` are symmetric under u↔v, but `alpha` is not. Iterations 552–553 established raw non-equivalence on two independent swap pairs; Iteration 554 derived the exact shift

`p(u,v)=p(v,u)+[(v-u)/s] q`.

Iteration 555 introduced `m=(u+v)/2`, `d=(v-u)/2` and derived

`alpha=-1/2+d/s`, `lambda=s^2-4sm+4d^2`,

so swapped routed points lie symmetrically about `p_mid=-a-q/2+rho(m,d^2)n` with opposite q-directed displacement. These are diagnostic/provenance results only; no support substitution is allowed.

## Iteration 557 — exact exchange-even projection of the mixed stencil
For frozen central4 first-derivative weights `w=[1,-8,8,-1]` at nodes `[-2h,-h,+h,+2h]`, the mixed derivative coefficient matrix is

`C_ij=w_i w_j/(144 h^2)`

and is exactly symmetric: `C_ij=C_ji`.

Writing the complete grid as

`E_ij=(F_ij+F_ji)/2`, `A_ij=(F_ij-F_ji)/2`,

with `A_ji=-A_ij`, gives exactly

`sum_ij C_ij A_ij=0`,

hence

`D_uv^central4[F]=D_uv^central4[E]`.

Continuous midpoint coordinates give the matching operator identity

`partial_u partial_v=(partial_m^2-partial_d^2)/4`.

This does **not** reduce the required support count: both swapped values are still needed to construct `E_ij` because Iterations 552–555 rule out equality. It does create a strong future assembly control: after full QUARTER closure, independently assemble the mixed derivative from the full grid and from exchange-even pair averages; disagreement is an implementation/indexing/weight/orientation failure.

Machine-readable authority: `candidate_gravity/results/iteration557_iter424_central4_exchange_even_projection_exact.json`.

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
- Iteration 549: three levels exactly saturate `X_s=D+A s^4+B s^6` (3 observations, 3 parameters, zero residual d.o.f.); BASE/HALF/QUARTER alone cannot test goodness-of-fit or exclude h8+ contamination. This does not authorize an h=1/8 heavy run.

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

Readiness change: **0 percentage points**. Rank8 closes another frozen support node and Iteration 557 adds an exact assembly invariant, but no additional stable model-level rubric sector is complete.

## Exact downstream chain
BASE/HALF support **CLOSED 523** → provenance **CLOSED 526** → BASE/HALF assembly **CLOSED 527** → QUARTER manifest **529** → ranks1–8 **RAW PASS through 556** → rank9 **RUNNING** → ranks10–12 in frozen order → QUARTER assembly + exchange-even control → unchanged Iteration-424 five-clause physical reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy retry. No u↔v support substitution. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated until a concrete residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.

## Exact next gate
Inspect terminal state of rank9 run `34160111095`. Only raw-valid PASS authorizes frozen rank10 `(+1.25e-6,+2.5e-6)`.
