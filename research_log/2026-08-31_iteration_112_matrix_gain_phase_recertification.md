# RQIR Research Log — Iteration 112

**Date:** 2026-08-31

## Goal

Advance the Paper-III control front after Iteration 111 without inventing apparatus SI rates. The leading open channel is complex transfer gain/phase because Iterations 101–103 already supply the same-state injected-transfer Fisher object but not its time-domain recertification process.

## Result

Derived the exact multivariate pure-dead recertification problem.

For usable covariance budget

`S=Sigma_*-Sigma_f > 0`,

reference Fisher-rate matrix `F_ref`, drift covariance rate `Q` with `Cov_drift=tau Q/2`, and reference duration `t_ref`, require

`(t_ref F_ref)^-1 + tau Q/2 <= S`.

Whiten with

`A=S^-1/2 F_ref^-1 S^-1/2`,

`B=S^-1/2 Q S^-1/2`.

At fixed cadence `tau`,

`t_ref,min(tau)=lambda_max[(I-tau B/2)^-1/2 A (I-tau B/2)^-1/2]`.

Therefore

`RESOURCE-072:`

`r_mat*=min_tau t_ref,min(tau)/tau`, `0<tau<2/lambda_max(B)`.

This is a one-dimensional exact optimization that retains correlated gain/phase Fisher, drift and tolerance orientation.

## Regression checks

1. Scalar reduction reproduces Iteration 109:

`r*=2D/(R_ref S^2)`, `tau*=S/D`, `t_ref*=2/(R_ref S)`.

Stored numerical test (`R=3.7,D=2.3,S=0.8`):

- numerical `r*=1.94256759`;
- analytic `1.94256757`.

2. Nonorthogonal coordinate reparameterization preserves `r_mat*` to relative `~1.4e-15` in the numerical audit.

3. Orientation counterexample with identical eigenvalue spectra `eig(F)={1,100}`, `eig(Q)={1,100}`, `S=I`:

- reference Fisher aligned with fast drift: `r*~=51.005`;
- swapped orientation: `r*~=200.000`;
- penalty `~3.92x`.

Thus marginal amplitude/phase rates are insufficient.

## New gates

- **RESOURCE-072:** exact matrix recertification envelope.
- **NG-068:** correlated/shared complex gain/phase controls cannot generally be replaced by independent scalar overheads without basis/schedule dependence.
- **DESIGN-016:** co-design reference Fisher with the generalized fast-drift/tight-budget modes rather than optimizing marginal amplitude/phase SNR.
- **RESOURCE-073:** a joint gain/phase pure-dead block enters Iteration-111 headroom through `r_mat*`. Under a uniform Fisher-rate scale `F_ref -> kappa F_ref`, `r_mat* -> r_mat*/kappa`, so `kappa_req=r_mat*/K` at the architecture boundary.

## Scope

No Toy009/Toy014 apparatus winner is assigned. Physical `Q`, `Sigma_f` and likelihood-derived `Sigma_*` intervals are still absent.

If transfer references are simultaneous/Fisher-carrying, use the full RESOURCE-064 campaign scheduler instead of dead-time addition.

## Next gate

Derive the admissible complex-transfer covariance budget `Sigma_*` directly from the detector-level profiled-Fisher loss geometry of Iterations 102–103. This removes arbitrary separate amplitude/phase tolerances and leaves only the physical drift/stability process to be supplied or bounded.
