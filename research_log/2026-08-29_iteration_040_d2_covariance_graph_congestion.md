# RQIR Research Log — Iteration 040

**Date:** 2026-08-29  
**Target:** determine whether adding covariance rows remains resource-beneficial once the actual shared-endpoint graph controls the per-shot covariance Fisher ceiling.

## Confirmed subset geometry

Centered Iteration-034 results at `y_ref=-4`, `lambda=1`:

- best4 `(0,1,3,7)`: `F_beta~0.899477`, `C_alpha*=0.0500614`;
- best5 `(0,1,3,6,7)`: `F_beta~0.903527`, `C_alpha*=0`;
- all8: `F_beta~0.905293`, `C_alpha*=0`.

## Graph-congestion result

For a natural uniform cross-covariance edge encoding, full-hypercube positivity gives per-edge Fisher ceiling

`K_edge < 1/rho(A_G)^2`.

The endpoint graph spectral costs are:

- best4: `rho^2=2`, `K_edge<1/2`, `N>1.180254e6`;
- best5: `rho^2=3.61803399`, `K_edge<0.2763932`, `N>2.135100e6`;
- all8: `rho^2=6`, `K_edge<1/6`, `N>3.540762e6`.

This is **RQIR-RESOURCE-015 — covariance graph congestion**: adding a jointly acquired covariance row can reduce the allowed per-shot Fisher of the entire edge set by increasing endpoint-graph spectral radius.

## Best4 + prep versus best5

The fifth row removes only residual `C_alpha=0.0500614`, equal to `~0.58943` accepted single-branch source-metrology copy equivalents.

But the ideal covariance-cycle lower bound rises by `~9.54846e5` trajectories.

Best5 can beat best4 + minimal source metrology only if

`(pC etaC/pP etaP)*(tP/tC) > ~1.61996e6`.

At 100 Hz and equal efficiencies, using only the coherence floor `tC>=7.94319 ms`, this needs `tP>~3.57 h`; with `1 ms` readout/dead time, `>~4.02 h`.

Therefore at the fixed 90% target, best4 plus a tiny independent source prior is strongly favored over best5 in the natural cross-covariance trajectory unless source verification is extremely slow.

## Best5 versus all8

Both have `C_alpha*=0` and exceed 90%, but all8 has a larger graph-congestion cycle lower bound. For the fixed 90% covariance-only objective, all8 is therefore resource-dominated by best5 under this architecture.

## Files

- `analysis/d2_covariance_graph_congestion_iteration040.py`
- `docs/D2_COVARIANCE_GRAPH_CONGESTION.md`
- `recovery/RECOVERY_DELTA_ITERATION_040.md`

## Next gate

Build a joint mean+covariance trajectory likelihood. The covariance-only path is now strongly bounded; the complementary D2 branch can become competitive only if the same coherent trajectory earns substantial force-mean/control Fisher or if a different measurement class changes the graph/Fisher limits.
