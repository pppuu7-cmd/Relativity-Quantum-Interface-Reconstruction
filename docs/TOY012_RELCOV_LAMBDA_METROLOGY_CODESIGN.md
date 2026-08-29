# RQIR Iteration 060 — Toy012 Relational-Covariance / Calibration / Source-Metrology Co-Design

**Date:** 2026-08-30  
**Scope:** balanced Toy012 complementary D2 branch after Iteration 059.  
**Status:** physical-resource lower-envelope calculation; no hardware forecast and no new-physics claim.

## 1. Problem exposed by total-wall-clock accounting

Iteration 057 varied *additional force covariance* while keeping all eight centered **relational covariance** rows as a common block. That was adequate for comparing force-covariance additions, but it hides a large common wall-clock term.

For a total resource budget the eight base covariance rows must themselves be design variables.

Iteration 060 therefore fixes the 28 mean rows

- 14 finite-reference relational means;
- 14 direct-force means,

and jointly varies

`(relational-covariance subset, calibration exposure lambda, independent C_alpha)`.

The target remains

`F_beta|theta = 0.90`.

## 2. Mean scheduling on Toy012

The Toy012 phases shorten the seven-layer evolution bundle relative to Toy009:

`sum_j t_j ~= 31.7525 ms`

at a 100-Hz gap, while

`t_max ~= 8.39577 ms`.

With `p=0.5` and `1 ms` readout/dead time, one 14-row same-time-dual-probe mean family costs

`T_mean,family(xi=1) ~= 26.0220 h`.

The conservative RESOURCE-016 baseline treats relational and force means as independent campaigns, so

`T_mean = 26.0220 h * (xi_rel^-2 + xi_force^-2)`

per unit calibration exposure `lambda`.

For equal sensitivities:

- `xi=1`: `~52.04 h`;
- `xi=2`: `~13.01 h`;
- `xi=3`: `~5.78 h`;
- `xi=5`: `~2.08 h`;
- `xi=10`: `~0.520 h`.

These are transparent scheduling lower bounds, not detector forecasts.

## 3. Base relational covariance is not free

At `lambda=1`, the best subset by minimum required source prior is

| number of base relational-cov rows | best subset | required `C_alpha` |
|---:|---|---:|
| 0 | — | cannot reach 0.90 even for known alpha |
| 1 | — | cannot reach 0.90 even for known alpha |
| 2 | — | cannot reach 0.90 even for known alpha |
| 3 | `(4,5,6)` | `113.3908` |
| 4 | `(2,4,5,6)` | `15.06194` |
| 5 | `(2,3,4,5,6)` | `13.81948` |
| 6 | `(0,2,3,4,5,6)` | `13.75431` |
| 7 | `(0,1,2,3,4,5,6)` | `13.74020` |
| 8 | all | `13.66941` |

This does **not** mean three covariance rows are fundamentally necessary. With perfect source-amplitude knowledge, fewer covariance rows can reach 90% if calibration exposure is increased. The minimum `lambda` values are approximately

- k0: `9.01e4`;
- k1: `8.04`;
- k2: `3.31`;
- k3: `0.862`;
- k4: `0.270`;
- k8: `0.247`.

The correct statement is therefore resource-based, not rank-based.

### RQIR-RESOURCE-028 — base covariance is an active wall-clock variable

> A covariance block that is common to several algebraic branch comparisons is not a common constant in total wall-clock optimization. Its acquisition time must be exposed and traded against source metrology and calibration exposure.

## 4. Endpoint-graph cost changes subset ordering

Using the natural phase-referenced Gaussian cross-covariance lower bound,

`N_cov >= lambda * gamma_cov * rho(A_G)^2`.

At `lambda=1`, `100 Hz`, `p=0.5`, and 1-ms overhead:

- `(2,4,5,6)`, `rho^2=2`: `T_cov > 19.8303 h`;
- a six-row set `(1,2,3,4,5,6)`, `rho^2=3`: `T_cov > 29.7454 h`;
- all eight, `rho^2=6`: `T_cov > 59.4909 h`.

A notable effect is that the six-row set `(1,2,3,4,5,6)` has the **same graph spectral-radius floor** as several five-row sets while carrying more useful Fisher. At `lambda=1` it requires

`C_alpha ~= 13.80774`.

So cardinality alone is the wrong resource metric.

### RQIR-CAL-018 — graph-cost saturation

> Adding an observable can improve nuisance closure without increasing the current shared-endpoint covariance lower bound if it does not increase the endpoint graph spectral radius. Covariance subsets must therefore be selected by physical graph/resource cost, not by row count.

This is a statement about the declared lower-bound measurement architecture, not proof that an additional physical channel is literally free in hardware.

## 5. Fixed `lambda=1` phase diagrams are not resource optima

The total auxiliary lower-bound objective is

`T_aux,S(lambda) = lambda [T_mean + T_cov,S] + C_alpha,S(lambda)/R_alpha`.

Thus `lambda`, source prior and covariance topology must be optimized together.

### RQIR-RESOURCE-029 — joint auxiliary co-optimization

> Calibration exposure, independent source-metrology Fisher and covariance topology are substitutable resources. Fixing `lambda=1` before comparing experimental branches can select the wrong architecture.

At the Iteration-057 source-metrology reference rate

`R_alpha = 2.20253e-5 s^-1`,

the global 256-subset search gives a simple practical transition for equal relational/force mean sensitivities.

### Weak mean readout: `xi ~= 1`

Best set:

`(1,2,3,4,5,6)`, `rho^2=3`.

Optimum approximately

- `lambda ~= 0.9523`;
- `C_alpha ~= 14.10`;
- auxiliary lower-bound time `~255.69 h`.

Here mean calibration is expensive, so the extra covariance information is worth its larger graph cost.

### Moderate mean readout: `xi ~= 1.5`

Best set switches to

`(2,4,5,6)`, `rho^2=2`.

Optimum approximately

- `lambda ~= 1.3744`;
- `C_alpha ~= 13.21`;
- `T_aux ~225.70 h`.

### `xi ~= 3`

The same four-row set remains optimal, but the correct resource optimum is **not** `lambda=1`:

- `lambda ~= 1.7546`;
- `C_alpha ~= 12.2169`;
- `T_aux ~199.02 h`.

At the same `R_alpha` the crossover between the six-row and four-row graph occurs near

`boxed: xi ~= 1.48`

for equal mean sensitivities in the present benchmark.

## 6. Underexposure can also be optimal

When independent source metrology becomes faster, the optimum moves in the opposite direction. For the four-row set with `xi=3`, representative values are

| `R_alpha [s^-1]` | optimal `lambda` | optimal `C_alpha` | `T_aux` |
|---:|---:|---:|---:|
| `1e-5` | `~2.68` | `~10.97` | `~373 h` |
| `2.20e-5` | `~1.75` | `~12.22` | `~199 h` |
| `1e-4` | `~0.91` | `~15.8` | `~67 h` |
| `2e-4` | `~0.71` | `~18.4` | `~44 h` |
| `1e-3` | `~0.46` | `~28.6` | `~20 h` |

So sufficiently fast source metrology makes it rational to **underexpose gravitational calibration** and buy more independent source Fisher instead.

Conversely, for extremely slow source metrology the optimizer overexposes calibration until `C_alpha` tends to zero.

## 7. Scientific interpretation

The source-amplitude problem and covariance problem are no longer separate modules. The useful experimental quantity is a lower envelope in a joint resource space:

`(mean SNR, covariance topology, lambda, source-copy Fisher rate)`.

For the current Toy012 benchmark, only two covariance topologies dominate a broad tested region (`xi~0.75–10`, `R_alpha~1e-6–1e-3 s^-1`):

- four-row `(2,4,5,6)` with `rho^2=2`;
- six-row `(1,2,3,4,5,6)` with `rho^2=3`.

This numerical dominance is not a theorem outside the tested domain or outside the current covariance lower-bound model.

## 8. Remaining physical caveat

All covariance times above remain **lower bounds**. Relational potential/noise is reconstructed through a finite-reference force architecture, so NG-011, NG-014 and NG-015 still apply. A physical transduction likelihood may only increase these costs.

Therefore the result is already useful for eliminating dominated designs, but it is not yet a complete apparatus forecast.

## 9. Reproducibility

Code:

`analysis/toy012_relcov_lambda_metrology_codesign_iteration060.py`

The script reconstructs Toy012, enumerates all 256 base-relational-covariance subsets, computes hard/finite-noise Fisher, graph cost, perfect-source minimum exposure and representative full `(subset,lambda,C_alpha)` wall-clock optima.

## 10. Next gate

The remaining total-wall-clock term with the largest uncertainty is the **science D2 rate in SI units**. The next iteration should combine

- the optimized auxiliary lower envelope from this iteration;
- Iteration-059 control priors;
- Toy012 absolute D2 signal ratio `0.21617`;
- the physical D2 force-PSD formula;

and derive the source-mass / probe-mass / force-ASD surface at which science integration overtakes auxiliary calibration.

This should remain parametric until a specific apparatus is declared.
