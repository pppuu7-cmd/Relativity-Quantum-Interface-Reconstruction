# RQIR Recovery Delta — Iteration 040

**Date:** 2026-08-29

## New confirmed result

Covariance subset selection must include the spectral congestion of the shared endpoint graph.

For the natural joint cross-covariance encoding, full-hypercube positivity gives

`K_edge < 1/rho(A_G)^2`.

At `y_ref=-4`, centered `lambda=1`:

- best4 `(0,1,3,7)`: `rho^2=2`, `N>1.180254e6`, `C_alpha*=0.0500614`;
- best5 `(0,1,3,6,7)`: `rho^2=3.61803399`, `N>2.135100e6`, `C_alpha*=0`;
- all8: `rho^2=6`, `N>3.540762e6`, `C_alpha*=0`.

This is **RQIR-RESOURCE-015 — covariance graph congestion**.

## Strong 90%-target consequence

The fifth row removes only `C_alpha=0.0500614`, equivalent to about `0.58943` accepted single-branch source-metrology copies at corrected `F_Q^(alpha)`.

But adding it raises the ideal shared covariance cycle floor by about `9.54846e5` trajectories.

Thus best5 beats best4 + residual source metrology only if

`(pC etaC/pP etaP)*(tP/tC)>~1.61996e6`.

At 100 Hz, equal efficiencies and the coherence floor, this requires source-metrology cycles longer than about `3.57 h`; with `1 ms` detector overhead, about `4.02 h`.

For a fixed 90% target, all8 is resource-dominated by best5 in this covariance-only graph architecture because both need no source prior but all8 has the larger graph-congestion lower bound.

## Reproducibility

- `analysis/d2_covariance_graph_congestion_iteration040.py`
- `docs/D2_COVARIANCE_GRAPH_CONGESTION.md`
- `research_log/2026-08-29_iteration_040_d2_covariance_graph_congestion.md`

## Next action

Stop treating covariance as an isolated campaign. Build one phase-referenced joint trajectory likelihood in which the same endpoint record provides force means, selected centered covariances and control references, and profile detector imprecision/backaction/timing nuisances in one Fisher matrix.
