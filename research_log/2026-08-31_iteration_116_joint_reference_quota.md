# RQIR Research Log — Iteration 116

**Date:** 2026-08-31

## Question

How should same-state reference wall time be counted when one physical acquisition simultaneously constrains common transfer gain and one or more calibration-layer nuisance coordinates?

## Result

For nuisance requirement matrix `H_*>=0` and one joint reference Fisher-rate matrix `K_ref>0`, the exact minimum wall time is

`T_ref,* = lambda_max(K_ref^-1/2 H_* K_ref^-1/2)`.

For diagonal independent quotas this reduces to

`T_joint=max_i h_i/r_i`,

whereas non-overlapping dedicated campaigns require

`T_sep=sum_i h_i/r_i`.

Thus `1<=T_sep/T_joint<=n` for `n` simultaneous scalar quotas. The full matrix must be retained: with `K=[[1,.8],[.8,1]]` and `H=I`, the exact required time is `5`, not the diagonal-only value `1`.

For several distinct campaigns:

`min sum_k t_k` subject to `sum_k t_k K_k >= H_*`, `t_k>=0`.

This is an SDP with dual `max tr(H_*Y)` subject to `Y>=0`, `tr(K_kY)<=1`.

## Labels

- **RESOURCE-082:** single joint-block generalized-eigenvalue quota theorem.
- **RESOURCE-083:** multi-reference no-double-counting SDP.
- **RESOURCE-084:** simultaneous-reference saving bound.
- **NG-073:** marginal rates cannot replace a correlated joint Fisher matrix.
- **CAL-023:** one physical record receives one wall-clock charge.

## Reproducibility

`analysis/joint_reference_quota_iteration116.py` verifies diagonal reduction, the simultaneous-saving bound, correlated counterexample, coordinate invariance and Loewner monotonicity.

## Readiness snapshot

Project-management estimates, not statistical quantities:

- Paper III scientific-content readiness: **89%**.
- Paper III submission readiness: **70%**.
- Repository readiness to begin a concrete Candidate-Gravity model: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**; QG-001…QG-010 remain unpassed by any concrete dynamics.

## Next gate

Derive a rank/span certificate for the four-real same-state dual-tone observation versus the common-gain plus seven-layer calibration subspace. Repeating an unchanged rank-deficient Jacobian cannot create missing Fisher directions.
