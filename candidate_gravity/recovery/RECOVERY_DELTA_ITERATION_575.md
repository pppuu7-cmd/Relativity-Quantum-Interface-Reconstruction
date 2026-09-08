# Recovery Delta — Iteration 575

**Date:** 2026-09-08  
**MODEL_READINESS:** 24% (unchanged)  
**Authority:** prospective exact-support manifest + active frozen computation; non-promoting

## Incoming authority
Iteration574 raw-consumed full spectrum-integrated BASE/HALF/QUARTER reconstruction for unresolved double-double index2 / class3 / `q^2=-1`. Four of the five frozen Iteration424 clauses are PASS; the only blocker is the original Iter421 `fit_residuals_scaled.tensor11 <= 2e-5` clause.

Independent post574 binding decision authority confirms:
- the exact pre-result tensor11 mapping exists;
- the Iter421 implementation was NumPy float/complex;
- Iter424 requires the identical tensor11 observable evaluated at MP80/MP120;
- no replacement observable/design is authorized.

## Frozen Iter575 support closure
Machine contract:
`candidate_gravity/contracts/iteration575_iter421_tensor11_exact_mp_support_manifest.json`

The unchanged Iter421 design needs 64 signed `F(u,v)` nodes for magnitudes `{1e-5,7.5e-6,5e-6,2.5e-6}`.

- already raw-valid MP support: **28/64 = 43.75%**;
- exact missing set: **36/64 = 56.25%**;
- 28 missing nodes contain `|u|=7.5e-6` or `|v|=7.5e-6`;
- 8 additional missing nodes are `1e-5 <-> 2.5e-6` cross-scale pairs.

All 36 are mandatory and were frozen before any new result. Their order is the original Iter421 `F`-cache first-occurrence order. Hence parallel execution is non-result-dependent and cannot tune the scientific gate.

## Active computation
Stage:
`candidate_gravity/code/iteration575_iter421_tensor11_missing_support_full_z_mp_stage.py`

Workflow:
`.github/workflows/rqir-iteration575-tensor11-missing-support-matrix.yml`

Canonical run:
- run `34180521559`
- head `519ceb6dc8efc3e5a9aebe86f5e6523152a4b284`
- matrix jobs: **36**
- max parallel jobs: **18**
- GitHub-hosted Ubuntu 24.04

Every rank retains:
- target index2/class3/q^2=-1;
- exact original Iter421 signed F-node coordinate;
- five z nodes `[-0.86,-0.43,0,0.43,0.86]`;
- NPHI16;
- inherited radial nodes `{2e-3,1e-3,5e-4}`;
- direct parent MP80/MP120;
- `scaled MP80-vs-MP120 <= 1e-30`;
- radial Richardson `<=5e-4`;
- 80 rows and all finite.

Per-rank PASS is support-only. No rank can promote physical index2. Valid BLOCKED stops tensor11 closure; infrastructure/schema failure permits only technical repair of the same frozen node(s), never threshold/node/radius change.

## Exact next action on terminal matrix
1. Fetch all 36 rank artifacts and authority audits.
2. Verify exact rank/coordinate/head/provenance, result SHA, 80 rows, finiteness, precision/radial thresholds.
3. If any scientific BLOCKED: preserve tensor11 BLOCKED and localize exact rank; do not zero-fill or substitute.
4. If all 36 raw-valid PASS: combine with the 28 already validated MP nodes and evaluate the unchanged original Iter421 degree-(1,1) fit at MP80 and MP120.
5. Only if tensor11 residual itself is `<=2e-5` and all other Iter424 clauses remain PASS may physical index2 be promoted and exact15 authorized.

## Retained guardrails
No post-hoc tensor11 redefinition; no node/radius change; no u-v substitution; no smaller-h rescue; no threshold weakening; no zero fill; no ANSATZ-003; no Fisher/resources.

**MODEL_READINESS: 24%**
