# RQIR Recovery Delta — Iteration 039

**Date:** 2026-08-29

## New confirmed result

The best four centered D2 force-covariance rows `(0,1,3,7)` reuse detector endpoints. They involve only six unique phase/probe outputs and form two degree-two stars in the covariance graph.

For the natural cross-covariance-only Gaussian encoding, full-hypercube positivity requires edge amplitude `a<1/sqrt(2)`. The per-row covariance Fisher is therefore `<1/2` per accepted shared trajectory.

This is **RQIR-NG-018 — shared-endpoint covariance bound**.

It is stricter than the generic Iteration-038 six-output trace bound because the covariance directions share central detector variables.

## Resource consequence

At centered `gamma_cov~0.590127e6`, the ideal accepted shared-trajectory count is

`N_joint>1.180254e6`

for the four-row block at `lambda=1`.

The same four rows save only `Delta C_alpha~4.5050486`, equal to about `53.04` accepted single-branch source-metrology copy equivalents at `F_Q^(alpha)=0.0849323916`.

Hence equal-efficiency covariance/preparation break-even requires

`t_P/t_C>~2.22510e4`.

The latest endpoint is phase `4.99085067`, so at `100 Hz` `t_C>=7.94319 ms`. The source-metrology cycle must therefore exceed about `176.74 s` before overhead, or `198.99 s` with `1 ms` detector dead/readout time, for covariance-only substitution even to be possible under the ideal graph model.

## Reproducibility

- `analysis/d2_covariance_endpoint_graph_iteration039.py`
- `docs/D2_COVARIANCE_ENDPOINT_GRAPH.md`
- `research_log/2026-08-29_iteration_039_d2_covariance_endpoint_graph.md`

## Next action

Build a joint mean+covariance likelihood on the same six phase/probe endpoints. Shared cycles should be credited simultaneously for endpoint force means and covariance information; timing/additive/imprecision/backaction nuisance directions must be profiled in the same Fisher.
