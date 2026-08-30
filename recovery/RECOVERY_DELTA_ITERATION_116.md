# RQIR Recovery Delta — Iteration 116

**Date:** 2026-08-31  
**Parent front:** Iteration 115.

## New result

A shared physical reference acquisition must be credited once through its full joint Fisher matrix.

For required nuisance information `H_*>=0` and a joint reference Fisher-rate matrix `K_ref>0`,

`T_ref,* = lambda_max(K_ref^-1/2 H_* K_ref^-1/2)`.

This is RESOURCE-082.

For several physically distinct reference campaigns `K_k`,

`min sum_k t_k` subject to `sum_k t_k K_k >= H_*`, `t_k>=0`,

which is RESOURCE-083. Its SDP dual is `max tr(H_*Y)` subject to `Y>=0` and `tr(K_kY)<=1`.

For independent diagonal simultaneous quotas,

`T_joint=max_i h_i/r_i`,

while dedicated non-overlapping campaigns give

`T_sep=sum_i h_i/r_i`,

so `1<=T_sep/T_joint<=n` (RESOURCE-084).

NG-073: marginal scalar rates are insufficient for a correlated shared block. Example `K=[[1,.8],[.8,1]]`, `H=I` requires exact `T=5`, not `1`.

CAL-023: one physical record, one wall-clock charge. If a block also carries science beta information, include it once in RESOURCE-057/064 rather than adding a separate calibration time for the same acquisition.

## Readiness after Iteration 116

- Paper III scientific-content readiness: **89%**.
- Paper III submission readiness: **70%**.
- Repository readiness to begin Candidate Gravity: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Files

- `analysis/joint_reference_quota_iteration116.py`
- `docs/PAPER_III_JOINT_REFERENCE_QUOTA_ITERATION116.md`
- `research_log/2026-08-31_iteration_116_joint_reference_quota.md`

## Next gate

Derive the rank/span compatibility of the four-real dual-tone same-state reference with the common-transfer plus seven-layer calibration nuisance subspace. Repetition cannot repair a missing score direction if the Jacobian span is unchanged.
