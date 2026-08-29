# RQIR Recovery Delta — Iteration 038

**Date:** 2026-08-29

## New confirmed results

A multi-parameter positivity bound was derived for shared phase-referenced Gaussian covariance acquisition.

For

`Sigma(u)=Sigma0+sum_i u_i Sigma_i`, `u_i in [-1,1]`,

with whitened derivatives `H_i`, positivity on the full hypercube implies

`Tr K < m/2`, `lambda_min(K)<m/(2q)`

for `K_ij=1/2 Tr(H_i H_j)`.

This is **RQIR-NG-017 — multi-parameter covariance information budget**.

For four simultaneously measured covariance coordinates with an eight-dimensional output, the weakest-direction per-shot covariance Fisher is `<1`.

A disjoint traceless block construction approaches this bound with `K~I_4`.

## Resource result

At centered D2 `gamma_cov~0.590127e6`, an ideal `m=8` joint output therefore needs more than `5.90127e5` accepted cycles at `lambda=1`. Four separate near-optimal bivariate campaigns would cost about four times more cycles at equal cycle duration/efficiency.

**RQIR-RESOURCE-014:** shared-shot speedup is dimension-limited; for the present `q=4,m=8` architecture the ideal cycle-count gain approaches four, not an arbitrary factor.

The best four centered force-covariance rows save `Delta C_alpha~4.5050486`, equal to only `~53.04` accepted single-branch source-metrology copy equivalents at `F_Q^(alpha)=0.0849323916`.

Thus the ideal shared covariance route requires, at equal efficiency,

`t_P/t_C > ~1.11255e4`.

The joint row set reaches `tau_max=4.99085067`, giving `T_C>=7.94319 ms` at 100 Hz before overhead. Therefore covariance can only beat preparation if the accepted source-metrology cycle is longer than about `88.37 s`; with `1 ms` dead/readout time the threshold is about `99.50 s`.

## Nuisance design rule

A common variance/imprecision-scale nuisance is Fisher-orthogonal to the explicit traceless block encoding and does not reduce its Fisher at the nominal point. An unknown covariance nuisance aligned with one source covariance derivative removes that direction exactly after profiling.

**RQIR-CAL-014 — covariance Fisher-orthogonality:** encode source covariance derivatives in detector covariance directions orthogonal, in the covariance Fisher metric, to dominant imprecision/backaction/cross-noise nuisance derivatives.

## Reproducibility

- `analysis/d2_shared_shot_covariance_budget_iteration038.py`
- `docs/D2_SHARED_SHOT_COVARIANCE_BUDGET.md`
- `research_log/2026-08-29_iteration_038_d2_shared_shot_covariance_budget.md`

## Next action

Use the actual endpoint structure of rows `(0,1,3,7)` to determine the minimum shared detector-output dimension and update the positivity/resource bound. Then move to a joint mean+covariance detector likelihood rather than treating covariance as a separate campaign.
