# RQIR Iteration 060 — Toy012 relational-covariance / source-metrology wall-clock tradeoff

**Date:** 2026-08-30

## Question

After Iteration 059 rebuilt the Toy012 control priors, which subset of the eight centered relational-covariance rows is actually worth paying for once covariance trajectories, independent source metrology and mean calibration are all charged in wall-clock units?

## Setup

Use the balanced Toy012 source and the preferred D2 architecture:

- 14 relational means;
- 14 direct-force means;
- a chosen subset of 8 centered relational-covariance rows;
- independent source-amplitude metrology supplying `C_alpha`;
- exact trace+energy elimination;
- fractional hidden-amplitude coordinate `alpha`;
- target profiled detector Fisher `F_beta|theta = 0.90`.

Resource benchmark retained from prior work:

- `f_gap = 100 Hz`;
- acceptance `p=0.5`;
- dead/readout overhead `1 ms`;
- Toy012 `gamma_mean=1.2086865e6`;
- Toy012 `gamma_cov=1.8994980e6`.

This is a lower-bound scheduling model, not an apparatus forecast. The normalized mean sensitivity `xi_mu` and source-metrology Fisher rate `R_alpha` remain explicit.

## Resource-relevant relational covariance branches

Enumeration of relational covariance subsets reproduces the prescan embedded in Iteration 059. The relevant minima by `C_alpha` are

| rows | subset | `C_alpha*` | endpoint `rho^2` | covariance lower-bound wall time |
|---:|---|---:|---:|---:|
| 4 | `(2,4,5,6)` | `15.06193956` | `2` | `19.83028348 h` |
| 5 | `(2,3,4,5,6)` | `13.81947864` | `(5+sqrt(5))/2 = 3.61803399` | `35.87331982 h` |
| 8 | all | `13.66941472` | `6` | `59.49085045 h` |

The graph factor is essential: the five-row set has a substantially higher shared-endpoint congestion penalty than the four-row set.

## Mean calibration budget

The Toy012 phase schedule has

`sum_j [t_j/(2 pi 100 Hz) + 1 ms] = 0.03875250145 s`

for one seven-layer family.

Treating relational and direct-force mean measurements conservatively as separate campaigns, but allowing the two same-time probe rows inside each family to share one phase layer,

`T_mean = 2 gamma_mean / (p xi_mu^2) sum_j cycle_j`.

Thus

- `xi_mu=1`: `52.0440 h`;
- `xi_mu=2`: `13.0110 h`;
- `xi_mu=3`: `5.78267 h`;
- `xi_mu=5`: `2.08176 h`;
- `xi_mu=10`: `0.52044 h`.

These numbers are normalized-resource benchmarks only. A physical force transduction / detector PSD is still required to map an apparatus to `xi_mu`.

## Branch crossings from source metrology

For a source-metrology Fisher rate `R_alpha`, the auxiliary lower bound is

`T_aux = T_mean + T_cov + C_alpha/R_alpha`.

At fixed `xi_mu`, the mean term cancels in branch comparisons. Therefore the wall-clock branch crossings are

- k4 -> k5 at
  `R_alpha = 2.151263806e-5 s^-1`;
- k5 -> all8 at
  `R_alpha = 1.764977970e-6 s^-1`.

This gives a new retained resource result:

## RQIR-RESOURCE-028 — covariance/source-metrology branch switching

The optimal covariance bundle is not fixed by Fisher geometry alone. It depends on the independent source-metrology Fisher rate because covariance trajectories and source-amplitude Fisher substitute for one another at different wall-clock prices.

For fast source metrology, the four-row relational covariance set is preferred. As source metrology slows below about `2.15e-5 s^-1`, the five-row set becomes cheaper despite its greater covariance congestion. Only for extremely slow source metrology, below about `1.76e-6 s^-1`, does paying for all eight relational-covariance rows become favorable among these resource-relevant branches.

Example totals at `xi_mu=3`:

| `R_alpha [s^-1]` | k4 | k5 | all8 | winner |
|---:|---:|---:|---:|---|
| `1e-4` | `67.45 h` | `80.04 h` | `103.24 h` | k4 |
| `2.2e-5` | `215.79 h` | `216.14 h` | `237.87 h` | k4 |
| `2e-5` | `234.81 h` | `233.59 h` | `255.13 h` | k5 |
| `1e-5` | `444.00 h` | `425.53 h` | `444.98 h` | k5 |
| `2e-6` | `2117.55 h` | `1961.03 h` | `1963.80 h` | k5 |
| `1e-6` | `4209.49 h` | `3880.40 h` | `3862.33 h` | all8 |

## Interpretation

This does not establish an experimentally viable apparatus and is not a new-physics claim. It closes one resource-accounting ambiguity: Toy012 covariance rows are no longer a hidden free constant.

The current leading architecture remains independent source metrology plus a sparse relational-covariance subset when source metrology is reasonably fast. The next gate is to replace `xi_mu` by a physical force-transduction / detector-noise expression and then add the absolute Toy012 science-signal time on the same mass/gap/separation/noise budget.
