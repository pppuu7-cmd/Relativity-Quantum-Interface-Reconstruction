# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: **Iteration 411**.
- Historical raw-valid physical blocker: **Iteration 421 — `BLOCKED_CONVERGENCE`**, unresolved double-double index2 / class3 / `q^2=-1`; unresolved physical set `[2]`.
- BASE/HALF support: **CLOSED 523**; raw-valid pre-spectral assembly: **527**.
- QUARTER support: **12/12 new coordinates = 100%**, **16/16 full grid = 100%**, raw-closed through **571**.
- Complete QUARTER pre-spectral sample-layer assembly: **572**, PASS scoped/non-promoting.
- Frozen-clause authority mapping: **573**, PASS scoped/non-promoting.
- Full frozen Iter407 spectrum reconstruction: **574**, independently raw-consumed PASS for all three newly computable spectral numerical clauses.
- Exact original-Iter421 tensor11 MP-support manifest: **575**, prospectively frozen/non-promoting.
- Exact tensor11 support-orbit/design identifiability audit: **576**, PASS scoped/non-promoting.
- Exact tensor11 leverage/single-orbit design robustness audit: **577**, PASS scoped/non-promoting.
- Exact tensor11 PRESS/leverage amplification robustness audit: **578**, PASS scoped/non-promoting.
- Iter579 all-36 raw-consumption gate: **RUNNING after minimal operational repair; not yet scientific authority**.
- Latest authoritative research iteration: **578**.

## Iteration574 full-spectrum raw authority
Canonical source:
- run `34179921282`
- job `101916751917`
- head `967525f318fac374124ca2a5127b82e0c771c7a2`
- artifact `10038557027`, `rqir-post573-iter424-full-spectrum-from-raw`
- artifact digest `sha256:330fc416a24935bbd1faf5f852420d179c0cd17a8bb2ba52dbae296bc00953e2`
- scientific result SHA-256 `d899623f64d98f12d19f32545e44fbcebe92ccc645f25a05b37f67a8b150a773`
- authority-audit SHA-256 `c241ae42e9255b1eeb075f9dc5232de77ec5e6107cb7a08fce8800f1d25565fe`.

Physical spectrum-integrated values:
- BASE `D_s = 0.000334698712595841410717689701215249442611820995807647705078125`;
- HALF `D_s = 0.0003346659700666914662690876181017074486589990556240081787109375`;
- QUARTER `D_s = 0.0003343462057176257821999865171846977318637073040008544921875`;
- MP80 and MP120 agree exactly at retained `D_s` precision;
- BASE↔HALF scaled discrepancy `3.2742529149944449e-8`;
- HALF↔QUARTER scaled discrepancy `3.1976434906568407e-7`.

## Frozen Iteration424 five-clause decision — current status
All five remain prospectively frozen; no threshold or observable has been changed after seeing results.

1. physical mass-step discrepancy `<=2e-5` — **PASS**, observed max `3.1976434906568407e-7`.
2. direct original-integrand crosscheck `<=2e-6` — **PASS**, inherited through Iteration573 exact parent-representation identity from raw-valid Iteration421; observed inherited maximum `2.0658997659274425e-9`.
3. tensor degree-(1,1) fit residual `<=2e-5` — **BLOCKED pending identical original-Iter421 observable at MP80/MP120**.
4. identical-node `|D_s(80)-D_s(120)|<=2e-6` — **PASS**, observed max `0.0` at retained precision.
5. finite outputs — **PASS** at full spectrum-integrated level.

Thus **4/5 frozen clauses are PASS, 1/5 remains BLOCKED**. This is not full Iteration424 PASS. Physical index2 is not promoted and exact15 is not authorized yet.

## Tensor11 exact mapping/support
The original prospectively frozen Iter421 statistic remains exactly:

`C(r,s)=[F(r,s)-F(r,-s)-F(-r,s)+F(-r,-s)]/(4rs)`

with `R=1e-5`, radius multipliers `[1,0.75,0.5,0.25]`, fit coordinates `x=(r/R)^2`, `y=(s/R)^2`, tensor degree-(1,1) basis `[1,x,y,xy]`, and `fit_residuals_scaled.tensor11 <= 2e-5`.

It requires 64 signed `F(u,v)` nodes with magnitudes `{1e-5,7.5e-6,5e-6,2.5e-6}`.
- existing raw-valid MP80/MP120 support before Iter575: **28/64 = 43.75%**;
- exact frozen missing support: **36/64 = 56.25%**;
- frozen membership/order: `candidate_gravity/contracts/iteration575_iter421_tensor11_exact_mp_support_manifest.json`.

## Iteration576 design identifiability
The 64 nodes form exactly 16 complete four-sign orbits:
- 7 complete pre-existing sign-orbits = 28 nodes;
- 9 complete Iter575 sign-orbits = 36 nodes;
- old/new straddled sign-orbits = 0.

For the unchanged `[1,x,y,xy]` fit over squared multiplier coordinates `{1,9/16,1/4,1/16}`:
- observations = 16;
- parameters = 4;
- residual dof = 12;
- exact design rank = 4;
- `det(X^T X)=276922881/16777216 > 0`.

Therefore tensor11 is genuinely overdetermined and has goodness-of-fit power.

## Iteration577 leverage / single-orbit robustness
Exact one-axis leverages: `[209/258, 23/86, 89/258, 149/258]`.
For the 16 symmetric-cross observations:
- leverage sum = `4` exactly;
- minimum leverage = `529/7396 ~= 0.07152514872904273`;
- maximum leverage = `43681/66564 ~= 0.6562255874046031 < 1`;
- minimum residual-projector diagonal = `22883/66564 ~= 0.3437744125953969 > 0`.
Deleting any one observation preserves rank 4. This is design robustness only and does not authorize deleting or modifying any frozen support.

## Iteration578 PRESS / leverage amplification robustness
For ordinary least squares, `e_i^(LOO)=e_i/(1-h_ii)`.
Using only the frozen tensor11 design geometry:
- minimum leverage-only PRESS amplification = `7396/6867 ~= 1.0770350953837193`;
- maximum leverage-only PRESS amplification = `66564/22883 ~= 2.9088843246077873`.
This is design robustness only and does not evaluate the pending numerical tensor11 residual.

## Iteration575 terminal matrix and Iteration579 raw-consumption gate
The complete prospectively frozen Iter575 support matrix is now terminal:
- workflow `RQIR Iter575 tensor11 missing support matrix`;
- source run `34180521559`;
- source head `519ceb6dc8efc3e5a9aebe86f5e6523152a4b284`;
- matrix jobs: 36.

A green source workflow is not scientific authority. Therefore Iter579 performs a separate fail-closed raw-consumption of all 36 uploaded ranks before any fit is allowed.

Iter579 provenance:
- workflow `.github/workflows/rqir-iteration579-tensor11-raw-consume.yml`;
- initial workflow commit `7cfbd7e732c3a4b70117ebc3ebabdb242e4c27cc`;
- initial trigger/head `9dca6e9cfdbec2733596c6b4dfe739c30449e7fe`;
- initial run `34193494429`, job `101956184537`: **operational failure only** because the consumer assumed a nested `rank_N/` directory that `gh run download` did not preserve; it found 0/36 result paths. This is explicitly not a scientific FAIL.
- minimal repair commit `461a67f1b9e726bd84bd138567bc2177807a2e43` changes only artifact-layout discovery and also binds the actual stage field `observed.max_radial_richardson_scaled_error`; all scientific criteria are unchanged.
- repair trigger/head `4ab0443fd0a35d23749516a0cc44c56305a472b2`.
- canonical repair run `34193625381`, job `101956570225`: **in_progress** at latest check.

The repaired consumer indexes downloaded `result.json` files by the embedded frozen `original_iter421_tensor11_rank`, then independently checks exact rank↔coordinate mapping, SHA against each uploaded authority audit, exactly 80 rows, finiteness, frozen radii/precision/z/phi conventions, per-rank PASS/exit code, MP80↔MP120 `<=1e-30`, and radial Richardson `<=5e-4`. Any missing/duplicate/BLOCKED/failing rank keeps the gate BLOCKED. No zero-fill or substitution is permitted.

## Exact terminal decision tree
When run `34193625381` becomes terminal:
1. inspect its uploaded `rqir-iter579-tensor11-all36-raw-consumption` artifact, not merely workflow colour;
2. if `all_36_raw_valid_pass != true`, preserve the exact failing ranks as BLOCKED and do not fit;
3. if all 36 ranks are raw-valid PASS, combine them with the already validated 28 MP nodes and evaluate the **unchanged original Iter421 tensor11 fit** independently at MP80 and MP120;
4. only tensor11 residual `<=2e-5`, together with the already PASS four other Iter424 clauses, can promote physical index2 and authorize exact15.

## Comparator blocker retained
Concrete upstream algebraic `Source/Ward/contact+K2` target and robust comparator-subtracted residual remain absent. Comparator quotient remains operationally BLOCKED. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iter579 is a raw-authority gate and cannot raise readiness unless a stable model-level rubric point is actually closed downstream.

## Downstream chain
BASE/HALF/QUARTER support **CLOSED** → full spectrum reconstruction **CLOSED 574** → Iter424 **4/5 PASS** → original tensor11 MP support matrix **TERMINAL 575** → all-36 raw consumption **RUNNING 579** → unchanged original tensor11 fit → only 5/5 PASS may promote index2 → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc tensor11 redefinition. No raw-grid bilinear or central4-polynomial substitution for tensor11. No u↔v support substitution. No smaller h, altered original tensor11 radii/nodes, precision change or threshold weakening. Same parent dynamics/routing/numerator/sign/normalization remain mandatory. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
