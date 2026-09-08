# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **580**.
- Historical physical/operator authority before higher-precision closure: **Iteration 411**.
- Historical raw-valid blocker: **Iteration 421 — `BLOCKED_CONVERGENCE`**, index2/class3/`q^2=-1`; retained as provenance, but its unresolved set is now resolved by the frozen higher-precision gate.
- Post-Iteration580 unresolved physical set: **`[]`**.
- Iter424 frozen high-precision decision: **5/5 PASS**.
- Iter580 classification: `PASS_ITER421_TENSOR11_MP80_MP120__ITER424_5_OF_5_PASS__PHYSICAL_INDEX2_NUMERICAL_BLOCKER_CLOSED`.
- Physical index2 numerical promotion is authorized by the frozen decision tree. Iter580 does **not** invent a new promoted-value estimator; downstream exact15 must use the pre-existing frozen promotion/value/normalization rule.

## Provenance chain
- BASE/HALF support CLOSED 523; raw-valid assembly 527.
- QUARTER support CLOSED 12/12; full 16/16 grid raw-closed through 571.
- complete QUARTER pre-spectral sample-layer assembly 572 — PASS scoped/non-promoting.
- frozen-clause authority mapping 573 — PASS scoped/non-promoting.
- full frozen Iter407 spectrum reconstruction 574 — PASS for mass-step, MP80↔MP120 and finiteness clauses.
- exact original-Iter421 tensor11 support manifest 575 — frozen before missing-node results.
- design/orbit identifiability 576 — PASS scoped/non-promoting.
- leverage/single-orbit robustness 577 — PASS scoped/non-promoting.
- PRESS leverage robustness 578 — PASS scoped/non-promoting.
- Iter579 all-36 fail-closed raw consumption — **36/36 PASS**.
- Iter580 unchanged original tensor11 at MP80/MP120 — **PASS**, closing Iter424 5/5.

## Iter579 raw authority
Source matrix:
- run `34180521559`, head `519ceb6dc8efc3e5a9aebe86f5e6523152a4b284`, 36 frozen ranks.

Canonical independent raw-consumer:
- run `34193625381`, head `4ab0443fd0a35d23749516a0cc44c56305a472b2`;
- artifact `10043065789`, `rqir-iter579-tensor11-all36-raw-consumption`;
- artifact digest `sha256:79273045e5821cc4cdea4127d610a32070cfc83e68d2011e076a264b6d654445`;
- `all_36_raw_valid_pass=true`;
- max MP80↔MP120 scaled discrepancy `5.4701756121638164e-80 <= 1e-30`;
- max radial Richardson scaled error `2.5748066807357275e-15 <= 5e-4`.

The earlier raw-consumer run `34193494429` failed operationally only because of artifact-layout discovery. Minimal repair changed no scientific criterion; that operational failure is not a scientific FAIL.

## Iter580 unchanged tensor11 authority
Frozen observable:

`C(r,s)=[F(r,s)-F(r,-s)-F(-r,s)+F(-r,-s)]/(4rs)`

with `R=1e-5`, multipliers `[1,0.75,0.5,0.25]`, `x=(r/R)^2`, `y=(s/R)^2`, basis `[1,x,y,xy]`, exact Iter407 index2 spectrum pipeline, and the original Iter420 least-squares residual definition

`max|pred-y| / max(1,max|y|,max|pred|)`.

Complete support: **64/64 raw-valid MP nodes** = 28 pre-existing + 36 Iter575/579.

Observed:
- MP80 tensor11 residual `1.341057348963658e-8`;
- MP120 tensor11 residual `1.341057348963658e-8`;
- frozen threshold `2e-5`;
- threshold margin factor `1491.3605309613044`.

Parent-dynamics validation reproduces Iter574 BASE/HALF values:
- BASE `D_s = 0.000334698712595841410717689701215...`;
- HALF `D_s = 0.000334665970066691466269087618102...`.

## Frozen Iteration424 five-clause decision
1. physical mass-step discrepancy `<=2e-5` — **PASS**, observed `3.1976434906568407e-7`.
2. direct original-integrand crosscheck `<=2e-6` — **PASS**, inherited exact parent representation from raw-valid Iter421, observed `2.0658997659274425e-9`.
3. tensor degree-(1,1) fit residual `<=2e-5` — **PASS**, observed `1.341057348963658e-8` at MP80 and MP120.
4. identical-node `|D_s(80)-D_s(120)|<=2e-6` — **PASS**, observed `0.0` at retained precision.
5. finite outputs — **PASS**.

Therefore Iter424 is **5/5 PASS**. This closes the historical numerical convergence blocker for physical index2 and authorizes the frozen exact15 gate.

## Strict scientific classification
This is a **numerical physical-gate PASS**, not Candidate-Gravity consistency PASS, not exact comparator identity, not regime-specific model non-identifiability, not near-degeneracy, and not a novelty certificate.

Concrete upstream algebraic `Source/Ward/contact+K2` target and robust comparator-subtracted residual remain absent. Therefore fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remains **operationally BLOCKED**. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden until a nonzero algebraic residual exists.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change from Iter579: **0 percentage points**. The important index2 numerical blocker closed, but no additional complete model-level rubric sector closed.

## Exact next gate
Execute the **already-frozen Iteration412 exact15 assembly** using the newly unblocked/promotable physical index2 under the pre-existing promotion/value/normalization rule. Do not select a new estimator post hoc. After exact15, continue through full `Tr U1^2` → `D_s Gamma_{e=2}` → concrete `Source/Ward/contact+K2` → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc tensor11 redefinition, no u↔v substitution, no smaller h, altered radii/nodes/precision, threshold weakening or ansatz tuning. One declared parent dynamics/routing/numerator/sign/normalization convention remains mandatory. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
