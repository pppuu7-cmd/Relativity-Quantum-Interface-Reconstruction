# RQIR Recovery Delta — Iteration 012

**Date:** 2026-08-29

Apply this delta after `docs/RECOVERY_GUIDE.md` v1.0 and Iteration 011.

## New result: physical Fisher resource budget

Main document: `docs/PHYSICAL_FISHER_RESOURCE_BUDGET.md`.

Reproducibility code: `analysis/physical_resource_budget_iteration012.py`.

Current operational calibration remains the Iteration-011 balanced Toy009 geometry:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- `s_min=1.9995404e-3`;
- rank `24/25`.

The 24 abstract calibration rows decompose into 1 trace, 1 source-energy, 14 potential-mean, and 8 symmetrized-covariance rows.

Updated scalar-gamma D1 Fisher thresholds on this current geometry, with effectively perfect hidden-amplitude preparation calibration:

- 50% retention: `gamma ~2.83e4`;
- 80%: `~6.85e5`;
- 90%: `~1.58e6`;
- 95%: `~3.38e6`.

These values supersede use of the older Toy010 gamma table as the current operational resource proxy.

## New retained rules

### RQIR-CAL-004 — conditioning is not a sufficient resource proxy

`1/s_min^2` estimates a weak-conditioning information scale but does not determine profiled detector Fisher. Alignment of weak calibration singular vectors with detector nuisance tangents matters.

### RQIR-RESOURCE-001 — coherence and repetition are distinct resources

With repeatable independent source preparations, total Fisher can accumulate over many shots while source coherence is only required over each preparation/evolution/readout cycle. Long campaign duration primarily creates preparation reproducibility and drift-control requirements.

## Critical negative correction

Do **not** interpret scalar `gamma` as a number of experimental measurements.

The old model `F_C=gamma A_norm^T A_norm` assigns identical row-normalized information to physically heterogeneous observables. A physical model must use row-specific covariance/Fisher weights:

`F_C=A^T Sigma_C^-1 A`

or

`F_C=sum_i N_i I_i^(1) a_i a_i^T`.

Mean-like Gaussian rows have single-shot Fisher `(dmu/dtheta)^2/sigma^2`; Gaussian variance rows have `0.5(d ln V/dtheta)^2`. Trace and source energy belong to separate source-metrology layers.

## Illustrative resource mapping

For detector SNR `rho_D=5`, `S_D=25`.

Hidden-amplitude preparation calibration for 90% detector-information retention requires physical `C_a=225`, so `N_prep=225/xi_prep^2` for standardized per-shot source-metrology sensitivity `xi_prep`.

Current 90% scalar-gamma proxy corresponds to `~3.95e7` normalized Fisher units per row. Treating the 22 gravitational rows as identical only for orientation gives total shots:

- `xi=1`: `~8.70e8`;
- `xi=10`: `~8.70e6`;
- `xi=100`: `~8.70e4`.

These are diagnostics, not hardware forecasts.

Largest stored phase `4.99085` gives a minimum coherent span `T_coh >= 0.7943/f_gap`, before readout/dead-time additions.

## Exact next gate

Replace scalar gamma by heterogeneous physical covariance and minimize total wall-clock/source-preparation cost at fixed profiled `F_beta|theta`. Distinguish at least source normalization, source energy, potential means, covariance/noise estimates, hidden-amplitude tomography, and common preparation drift. Then apply separate D1 and D2 detector noise laws.
