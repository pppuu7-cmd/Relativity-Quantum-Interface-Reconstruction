# RQIR Recovery Delta — Iteration 035

**Date:** 2026-08-29

## New measurement-class correction

The current Toy009 hidden states are not stationary:

`||[rho_+,H]||_F = ||[rho_-,H]||_F ~=0.2406721121`.

For probe-0 centered force covariance,

`Delta N(TR,0) ~= -8.4506285e-4`,

but

`Delta N(TR+1,1) ~= -4.7918338e-3`.

A common shift of both times changes the covariance substantially, so the current calibration rows are phase-referenced two-time observables, not stationary scalar PSD coordinates.

**RQIR-NG-014 — stationary-PSD mismatch obstruction:** do not assign the stationary `q_cov=eta B kappa^2` rate to the present rows without a demonstrated stationary/cyclostationary reduction.

## Ordering gate

The high-value force-covariance rows `(0,1,3,7)` are built from noncommuting source operators. Their commutator Frobenius norms are approximately

`0.52119, 0.006055, 0.015717, 0.011633`.

**RQIR-NG-015 — source-correlator/output-covariance identification obstruction:** detector-output covariance is not automatically the source symmetrized quantum correlator for noncommuting source observables. Measurement transfer, ordering and backaction must be explicit.

## Physical rate replacement

For one independent real Gaussian phase-referenced detector-output vector sample,

`I_ij^(shot) = (d_i mu)^T Sigma^-1 (d_j mu) + 1/2 Tr[Sigma^-1 Sigma_,i Sigma^-1 Sigma_,j]`.

With cycle time `t_C`, acceptance `p_C` and information efficiency `eta_C`,

`q_ij = p_C eta_C I_ij^(shot)/t_C`.

**RQIR-RESOURCE-012 — phase-referenced covariance Fisher rate.**

Stationary spectral Fisher is retained only as a special case.

## Coordinate-correct break-even

Using Iteration-034 `F_Q^(alpha)~=0.0849323916` and centered row thresholds:

- best first four covariance rows require
  `I_cov^(shot)*(pC etaC/pP etaP)*(tP/tC) > ~4.4502e4`;
- fifth row after the first four requires
  `> ~1.0012e6`.

This is now the preferred apparatus-neutral screening condition.

## Reproducibility

- `analysis/nonstationary_covariance_measurement_gate_iteration035.py`
- `docs/NONSTATIONARY_COVARIANCE_MEASUREMENT_GATE.md`
- `research_log/2026-08-29_iteration_035_nonstationary_covariance_measurement.md`

## Next action

Construct a phase-referenced repeated-shot D2 detector-output likelihood for rows `(0,1,3,7)`. Include the mean sector, covariance transduction, detector imprecision, backaction/cross-noise and independent source-preparation metrology in one profiled Fisher. Only then assign SI covariance time or compare against the fully force-native branch.
