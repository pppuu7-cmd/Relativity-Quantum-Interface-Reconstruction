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
- Full frozen Iter407 spectrum reconstruction: **574**, independently raw-consumed PASS for all three newly computable spectral numerical clauses, non-promoting because tensor11 remains unresolved.
- Exact original-Iter421 tensor11 MP-support manifest: **575**, prospectively frozen/non-promoting.
- Latest authoritative research iteration: **575**.

## Iteration574 full-spectrum raw authority
Canonical source:
- run `34179921282`
- job `101916751917`
- head `967525f318fac374124ca2a5127b82e0c771c7a2`
- artifact `10038557027`, `rqir-post573-iter424-full-spectrum-from-raw`
- artifact digest `sha256:330fc416a24935bbd1faf5f852420d179c0cd17a8bb2ba52dbae296bc00953e2`
- scientific result SHA-256 `d899623f64d98f12d19f32545e44fbcebe92ccc645f25a05b37f67a8b150a773`
- authority-audit SHA-256 `c241ae42e9255b1eeb075f9dc5232de77ec5e6107cb7a08fce8800f1d25565fe`.

Independent Iter574 consumption additionally SHA-checked **45/45** source scientific result parts: 29 BASE/HALF artifact parts covering 28 coordinates plus 16 QUARTER artifacts, with zero SHA mismatches, exact 80-row BASE/HALF merges, no duplicate `(z,phi)` samples, and exact frozen five-z/NPHI16 support.

Physical spectrum-integrated values:
- BASE `D_s = 0.000334698712595841410717689701215249442611820995807647705078125`;
- HALF `D_s = 0.0003346659700666914662690876181017074486589990556240081787109375`;
- QUARTER `D_s = 0.0003343462057176257821999865171846977318637073040008544921875`;
- MP80 and MP120 agree exactly at the retained `D_s` precision;
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

## Tensor11 mapping and exact support deficit
The independent post574 binding decision passed with classification
`MAPPING_FOUND__HIGH_PRECISION_TENSOR11_VALUE_UNCOMPUTED__NEXT_GATE_MP80_MP120`.

The original prospectively frozen Iter421 statistic is retained exactly:

`C(r,s)=[F(r,s)-F(r,-s)-F(-r,s)+F(-r,-s)]/(4rs)`

with `R=1e-5`, radius multipliers `[1,0.75,0.5,0.25]`, fit coordinates `x=(r/R)^2`, `y=(s/R)^2`, tensor degree-(1,1) basis `[1,x,y,xy]`, and `fit_residuals_scaled.tensor11 <= 2e-5`.

It requires 64 signed `F(u,v)` nodes with magnitudes `{1e-5,7.5e-6,5e-6,2.5e-6}`.

- existing raw-valid MP80/MP120 support: **28/64 = 43.75%**;
- exact missing support: **36/64 = 56.25%**;
- 28 missing nodes involve magnitude `7.5e-6`;
- 8 additional missing nodes are `1e-5 <-> 2.5e-6` cross-scale pairs.

The full missing set/order is frozen in
`candidate_gravity/contracts/iteration575_iter421_tensor11_exact_mp_support_manifest.json` before any new node result. Because all 36 are mandatory and no result can change membership/order/threshold, matrix parallelization is non-result-dependent.

## Active heavy computation — Iteration575
Exactly one tensor11 support matrix is active:
- workflow `RQIR Iter575 tensor11 missing support matrix`;
- run `34180521559`;
- head `519ceb6dc8efc3e5a9aebe86f5e6523152a4b284`;
- matrix jobs: **36**;
- `max-parallel: 18`;
- stage `candidate_gravity/code/iteration575_iter421_tensor11_missing_support_full_z_mp_stage.py`;
- each rank: exact frozen `(u,v)`, five z values, NPHI16, inherited radial Richardson nodes, direct MP80/MP120;
- per-rank gates: 80 rows, finite, MP80↔MP120 `<=1e-30`, radial Richardson `<=5e-4`.

No duplicate Iter575 matrix or individual-rank heavy run is authorized while run `34180521559` is queued/in-progress. A per-rank PASS is support-only and cannot promote physical index2.

## Exact terminal decision tree
When run `34180521559` becomes terminal:
1. fetch all 36 rank artifacts and authority audits;
2. independently verify rank↔coordinate mapping, result SHA, 80 rows, finiteness, precision/radial thresholds and exact head/provenance;
3. if any rank is scientific `BLOCKED`, preserve tensor11 BLOCKED and localize that exact frozen node without node/radius/threshold changes;
4. if all 36 ranks are raw-valid PASS, combine them with the already validated 28 MP nodes and evaluate the **unchanged original Iter421 tensor11 fit** independently at MP80 and MP120;
5. only tensor11 residual `<=2e-5`, together with the already PASS four other Iter424 clauses, can promote physical index2 and authorize exact15.

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

Readiness change: **0 percentage points**. The work materially closes the only remaining Iter424 support blocker but does not yet close a stable model-level rubric point.

## Downstream chain
BASE/HALF/QUARTER support **CLOSED** → full spectrum reconstruction **CLOSED 574** → Iter424 **4/5 PASS** → original tensor11 exact MP support **RUNNING 575** → unchanged original tensor11 fit → only 5/5 PASS may promote index2 → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc tensor11 redefinition. No raw-grid bilinear or central4-polynomial substitution for tensor11. No u↔v support substitution. No smaller h, altered original tensor11 radii/nodes, precision change or threshold weakening. Same parent dynamics/routing/numerator/sign/normalization remain mandatory. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
