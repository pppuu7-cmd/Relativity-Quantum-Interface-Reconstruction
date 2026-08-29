# RQIR Research Log — Iteration 035

**Date:** 2026-08-29  
**Target:** determine the correct physical measurement class for the centered D2 covariance rows before assigning SI covariance Fisher rates.

## Starting point

Iteration 034 corrected both the source-QFI coordinate and the centered covariance derivative. Iteration 033's stationary PSD rate remained only a candidate physical map.

## Stationarity audit

Current hidden states satisfy

`||[rho_+,H]||_F = ||[rho_-,H]||_F ~=0.2406721121`,

so they are not stationary under the five-level source Hamiltonian.

For probe-0 force centered covariance difference:

- `Delta N(TR,0) ~= -8.4506285e-4`;
- after common time shift by 1: `Delta N(TR+1,1) ~= -4.7918338e-3`.

Therefore the current covariance rows are phase-referenced two-time quantities, not stationary scalar PSD coordinates.

New negative gate: **RQIR-NG-014 — stationary-PSD mismatch obstruction.**

## Ordering audit

The high-value force-covariance rows `(0,1,3,7)` have nonzero operator commutator Frobenius norms approximately

`0.52119, 0.006055, 0.015717, 0.011633`.

A classical detector-output covariance therefore cannot be identified with the source symmetrized quantum correlator without an explicit measurement/transfer model including ordering and backaction.

New negative gate: **RQIR-NG-015 — source-correlator/output-covariance identification obstruction.**

## Phase-referenced repeated-shot Fisher

For one real Gaussian detector-output vector sample,

`I_ij = d_i mu^T Sigma^-1 d_j mu + 1/2 Tr[Sigma^-1 Sigma_,i Sigma^-1 Sigma_,j]`.

Physical rate:

`q_ij = p_C eta_C I_ij/t_C`.

New retained rule: **RQIR-RESOURCE-012 — phase-referenced covariance Fisher rate.**

Stationary spectral Fisher remains a special case after stationarity/cyclostationarity has been demonstrated.

## Coordinate-correct break-even

Using Iteration-034 centered thresholds and `F_Q^(alpha)~=0.0849323916`:

- first four covariance rows require
  `I_shot*(pC etaC/pP etaP)*(tP/tC) > ~4.4502e4`;
- fifth row requires
  `> ~1.0012e6`.

Thus the physical viability of covariance completion depends sharply on per-cycle covariance Fisher and the preparation/covariance cycle-rate ratio.

## Files

- `analysis/nonstationary_covariance_measurement_gate_iteration035.py`
- `docs/NONSTATIONARY_COVARIANCE_MEASUREMENT_GATE.md`
- `recovery/RECOVERY_DELTA_ITERATION_035.md`

## Next gate

Build the least-assumptive phase-referenced repeated-shot D2 likelihood for rows `(0,1,3,7)`, including detector-output variance, cross-covariance transduction, imprecision/backaction and mean nuisances. Then rerun `F_beta|theta` and wall-clock break-even in the same likelihood.
