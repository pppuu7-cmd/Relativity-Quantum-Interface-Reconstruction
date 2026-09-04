# Iteration 421 Final Recovery Delta

**Date:** 2026-09-04  
**MODEL_READINESS:** 24% (unchanged)  
**Physical target:** double-double index 2 / class 3 / `q^2=-1`  
**Raw-valid result:** `BLOCKED_CONVERGENCE`  
**Run:** 33871920373  
**Job:** 101019660127  
**Artifact:** 9942128452  
**Artifact digest:** `sha256:d75c5063b81e02872fe1255421c62e0679de22ae13fce7e2013358eba73152ff`  
**Raw scientific JSON SHA-256:** `c297cb15b707ef59b9d940c159a1fcb7e9f3a1e64135ccebc077b48a869f5e20`

## Result

The repaired collision-safe symmetric-cross gate completed with a valid raw authority audit. It is not an operational failure. The physical coordinate remains blocked and is not promoted.

Diagnostic primary estimate only (not authority):

`D_s Tr(U1^2)[index 2] ~= +0.0035843041850530683`.

Frozen acceptance failures:

- `max_stability_scaled = 2.2720400683804223e-05 > 2e-05`;
- `max_required_fit_residual_scaled = 2.585665489102237e-05 > 2e-05`.

Everything else relevant to execution/representation passed strongly:

- max direct original-integrand cross-check `2.0658997659274425e-09 < 2e-06`;
- max polynomial heldout error `7.852876335312509e-16 < 2e-06`;
- max affine-denominator error `2.220446049250313e-16 < 2e-11`;
- max radial Richardson error `5.29849601693666e-15 < 5e-4`;
- max design condition number `362.20107548262695 < 1000`;
- synthetic-oracle absolute error `1.6653345369377348e-16 < 1e-12`.

Thus this is a narrow convergence/representation block, not evidence that the physical integrand or cut support is invalid.

## Consequence

The prospectively frozen Iteration-424 high-precision fallback is now authorized. Frozen exact15 Iteration 412 remains blocked because index 2 still lacks a raw-valid `CONVERGED` coordinate. No zero fill is allowed.

Iteration 427 was frozen before this result and gives an exact non-promoting chain reduction for the complete frozen function. Because Iteration 424 explicitly freezes the same mass nodes/steps, its authority path must preserve those nodes. Iteration 427 is therefore an independent factorized cross-check / implementation aid unless an implementation can use the exact reduction while literally preserving the frozen-node contract.

## Immediate next gates

1. Continue the already launched Iteration-426 phi-mean 16-vs-32 diagnostic.
2. Implement Iteration-424 true 80/120-digit fixed-node fallback with the complete frozen `F(u,v)`; do not upgrade only the affine moments because Iteration 422 already excluded them as the dominant arithmetic source.
3. Use Iteration-427 exact kinematic reduction as an independent factorized consistency oracle.
4. Promote index 2 only if the prospectively frozen physical, tensor-fit, direct-integrand and cross-precision conditions all pass under raw workflow authority.
