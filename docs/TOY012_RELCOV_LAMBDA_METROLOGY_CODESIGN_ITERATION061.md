# RQIR Iteration 061 — Toy012 Relational-Covariance / Lambda / Source-Metrology Co-Design

**Date:** 2026-08-30  
**Status:** canonical resource lower-envelope result; no hardware or new-physics claim.

> Numbering note: a parallel preliminary wall-clock Iteration 060 was committed first. The deeper calculation developed concurrently is therefore canonically Iteration 061. Its full implementation remains in the provisional module `analysis/toy012_relcov_lambda_metrology_codesign_iteration060.py`; the canonical entry point is `analysis/toy012_relcov_lambda_metrology_codesign_iteration061.py`.

## Result

The eight centered **base relational-covariance** rows cannot be treated as a free/common block once total wall clock is optimized. Iteration 061 jointly varies

`(relational-covariance subset, calibration exposure lambda, independent C_alpha)`

while retaining 14 relational means and 14 direct-force means.

At 100 Hz, `p=0.5`, 1-ms overhead, one 14-row same-time-dual-probe mean family costs

`T_mean,family(xi=1) ~= 26.0220 h`.

The conservative two-family baseline is

`T_mean = 26.0220 h * (xi_rel^-2 + xi_force^-2)`

per unit `lambda`.

### RQIR-RESOURCE-028 — base covariance is an active wall-clock variable

At `lambda=1`, natural shared-endpoint covariance lower bounds are

- `(2,4,5,6)`, `rho^2=2`: `>19.8303 h`;
- `(1,2,3,4,5,6)`, `rho^2=3`: `>29.7454 h`;
- all eight, `rho^2=6`: `>59.4909 h`.

At fixed `lambda=1`, fewer than three relational-covariance rows cannot reach `F_beta|theta=0.90` even with perfectly known alpha. This is only a finite-resource statement: with perfect alpha the minimum exposure is approximately `9.01e4, 8.04, 3.31, 0.862, 0.270, ..., 0.247` for k=0,1,2,3,4,...,8.

### RQIR-CAL-018 — graph-cost saturation

Row count is not the physical cost. The six-row set

`(1,2,3,4,5,6)`

has `rho^2=3`, the same current graph floor as relevant five-row blocks, but carries more useful nuisance Fisher. At `lambda=1` it needs `C_alpha~13.80774`.

An extra row can therefore improve inference without increasing the **current graph lower bound** if the endpoint spectral radius does not increase. This is not a claim that the extra hardware channel is literally free.

### RQIR-RESOURCE-029 — joint auxiliary co-optimization

The correct auxiliary objective is

`T_aux,S(lambda)=lambda[T_mean+T_cov,S]+C_alpha,S(lambda)/R_alpha`.

Thus fixed-`lambda` phase diagrams can select the wrong architecture.

At the current reference source-metrology rate

`R_alpha=2.20253e-5 s^-1`,

and equal relational/force mean sensitivity:

| `xi` | winning covariance set | `rho^2` | optimal `lambda` | `C_alpha` | `T_aux` |
|---:|---|---:|---:|---:|---:|
| 1.0 | `(1,2,3,4,5,6)` | 3 | `~0.9523` | `~14.10` | `~255.69 h` |
| 1.5 | `(2,4,5,6)` | 2 | `~1.3744` | `~13.21` | `~225.70 h` |
| 3.0 | `(2,4,5,6)` | 2 | `~1.7546` | `~12.22` | `~199.02 h` |

The equal-`xi` transition near this `R_alpha` lies close to

`xi ~= 1.48`.

In a broad numerical scan of the current lower-bound model (`xi~0.75–10`, `R_alpha~1e-6–1e-3 s^-1`), only these two graph topologies appeared on the lower envelope. This is a numerical result, not a theorem outside the scanned domain.

Fast independent source metrology can make `lambda<1` optimal: for the four-row set at `xi=3`, representative optimized values are roughly

- `R_alpha=1e-5`: `lambda~2.68`, `C_alpha~10.97`, `T_aux~373 h`;
- `2.20e-5`: `lambda~1.75`, `C_alpha~12.22`, `~199 h`;
- `1e-4`: `lambda~0.91`, `C_alpha~15.8`, `~67 h`;
- `2e-4`: `lambda~0.71`, `C_alpha~18.4`, `~44 h`;
- `1e-3`: `lambda~0.46`, `C_alpha~28.6`, `~20 h`.

So calibration exposure, covariance topology and independent source Fisher are genuinely substitutable resources.

## Limitation

All covariance times remain optimistic lower bounds. Finite-reference potential/noise reconstruction and nonstationary/noncommuting covariance gates NG-011/014/015 remain active. A physical detector-output likelihood can only decide the final SI cost.

## Reproducibility

Canonical entry point:

`analysis/toy012_relcov_lambda_metrology_codesign_iteration061.py`

Implementation module retained for exact reproduction:

`analysis/toy012_relcov_lambda_metrology_codesign_iteration060.py`

## Next gate

Add the **absolute D2 science Fisher rate**. Use Toy012's measured dimensionless science-information ratio `~0.21617` relative to Toy009 and the explicit equivalent-force ASD formula to derive a parametric science-vs-auxiliary crossover in `(mass product, force ASD, duty)` without selecting a fictitious apparatus.
