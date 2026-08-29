# RQIR Recovery Delta — Iteration 042

**Date:** 2026-08-29

## New retained results

- **RQIR-CAL-015 — same-time dual-probe pairing:** at a fixed phase `G0(t_j)` and `G1(t_j)` commute and can be co-acquired in the current model. The 14 mean rows therefore reduce to seven compatible time layers, but not one multitime QND bundle.
- **RQIR-RESOURCE-017 — phase-layer coherence accounting:** for independent phase preparations use the sum of layer-specific coherence/evolution times, not `7*t_max`; conversely do not reuse one source copy across noncommuting layers without an explicit weak/backaction model.

Current centered D2 mean target:

`gamma_mean ~=1.830265e6`.

For per-accepted-cycle standardized row sensitivity `xi_mu`, each time layer needs

`N_layer=gamma_mean/xi_mu^2`.

At 100 Hz the seven phase evolution times sum to `0.0373396341 s`; largest layer is `7.94318794 ms`.

## 100-Hz wall-time benchmark

Ideal `p=1`, no dead time, `xi_mu=1`:

- parallel dual-probe mean campaign `18.9837 h`;
- sequential probe campaign `37.9675 h`;
- Iteration-040 best4 covariance floor `2.60416 h`.

Mean-vs-covariance crossover:

- parallel `xi_mu>=2.69996`;
- sequential `xi_mu>=3.81832`.

For `p=0.5`, `dead=1 ms`:

- best4 covariance floor `5.86402 h`;
- parallel mean campaign: `45.0852 h` at `xi=1`, `11.2713 h` at `xi=2`, `5.00946 h` at `xi=3`, `1.80341 h` at `xi=5`, `0.450852 h` at `xi=10`;
- crossover `xi_mu~2.77280` parallel, `3.92134` sequential.

## Next

Build a minimal continuous weak-measurement/output model and quantify information versus source backaction for co-acquired mean+covariance trajectories.
