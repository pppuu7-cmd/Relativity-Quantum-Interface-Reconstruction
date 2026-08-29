# RQIR Iteration 035 — Nonstationary / Ordered Covariance Measurement Gate

**Date:** 2026-08-29  
**Scope:** current Toy009/Iteration-011 D2 centered covariance resource layer.  
**Status:** measurement-model/identifiability gate; no new-physics claim.

## 1. Question

Iteration 034 corrected the physical parameter coordinate and the centered symmetrized covariance derivative. The remaining task from Iteration 033 was to attach row-specific physical covariance Fisher rates.

The simplest previous screening formula was the stationary Gaussian PSD rate

`q_cov = eta_duty B_eff kappa_eff^2`.

Before using it for the current Toy009 covariance rows, one must ask whether those rows are actually stationary detector-output PSD coordinates.

They are not, without an additional measurement construction.

## 2. Current hidden source is not stationary

The current prepared states are

`rho_+ = I/5 + EPS Delta0`,

`rho_- = I/5 - EPS Delta0`,

with `EPS=0.08`.

For the balanced Toy009/Iteration-011 hidden direction,

`||[rho_+,H]||_F = ||[rho_-,H]||_F ~= 0.2406721121`.

Thus neither state is stationary under the closed five-level Hamiltonian.

A centered two-time covariance therefore need not depend only on the time difference.

For the probe-0 force operator `G0`, the current hidden-state covariance difference gives

`Delta N_GG(TR,0) ~= -8.4506285e-4`,

whereas a common shift of both times by one dimensionless unit gives

`Delta N_GG(TR+1,1) ~= -4.7918338e-3`.

The difference is approximately

`-3.94677e-3`,

far above numerical precision.

Therefore the covariance row is a **phase-referenced two-time quantity**, not a stationary scalar PSD coordinate.

## 3. RQIR-NG-014 — stationary-PSD mismatch obstruction

> A stationary PSD Fisher rate cannot be assigned to a two-time source covariance row unless stationarity (or an explicit cyclostationary reduction) has been demonstrated for the declared prepared state and detector output.

For the current Toy009 hidden states, `[rho,H] != 0`; hence the Iteration-033 stationary `q_cov=eta B kappa^2` expression remains only a generic special-case screening formula, not the physical rate of the present covariance rows.

This does not invalidate stationary PSD methods in general. It says the current source must instead be treated through a phase-referenced/cyclostationary likelihood or another explicitly declared measurement protocol.

## 4. Operator ordering is also active

The most valuable centered force-covariance rows from Iteration 034 are `(0,1,3,7)`. Their underlying source-operator pairs do not commute.

Frobenius norms of the operator commutators are approximately:

- row `0`: `0.52118982`;
- row `1`: `0.00605486`;
- row `3`: `0.01571662`;
- row `7`: `0.01163327`.

All are nonzero.

Therefore a classical covariance of two detector numbers cannot simply be **declared** equal to the source symmetrized quantum correlator. The source-to-detector measurement dynamics must show which ordering appears and how detector imprecision, backaction and any imprecision-backaction cross-correlation enter.

### RQIR-NG-015 — source-correlator/output-covariance identification obstruction

> For noncommuting source observables, a detector-output covariance is not automatically the source symmetrized operator covariance. A physical measurement/transfer model is required before the source covariance row can be assigned detector Fisher or wall-clock cost.

This is an operational ordering requirement, not a claim that the symmetrized correlator is unmeasurable. Continuous linear measurement, weak measurement, ancilla-assisted protocols or other constructions may realize it, but the protocol has to be stated and its backaction included.

## 5. General phase-referenced repeated-shot Fisher

A safe measurement-level representation is a phase-locked detector-output vector `y` obtained once per accepted cycle, with local Gaussian model

`y ~ N(mu(u), Sigma(u))`.

For one real Gaussian vector sample, the Fisher matrix is

`I_ij^(shot) = (d_i mu)^T Sigma^-1 (d_j mu)`

`             + 1/2 Tr[Sigma^-1 Sigma_,i Sigma^-1 Sigma_,j]`.

For a covariance-only coordinate after the complete mean sector is included in the same likelihood, the second term supplies the covariance information.

With accepted-cycle probability `p_C`, information efficiency `eta_C` and cycle time `t_C`, the physical information rate is

`q_ij = p_C eta_C I_ij^(shot) / t_C`.

### RQIR-RESOURCE-012 — phase-referenced covariance Fisher rate

> For the current nonstationary covariance rows, physical resource accounting must be based on the Fisher rate of the actual phase-referenced detector-output likelihood. A stationary PSD rate is only a special limiting case.

## 6. Useful two-channel closed form

For a zero-mean bivariate Gaussian detector output with

`Sigma = [[v1,C],[C,v2]]`

and a parameter changing only the cross covariance, `s=dC/du`, the per-sample Fisher is

`I_u = s^2 (v1 v2 + C^2) / (v1 v2 - C^2)^2`.

For weak cross correlation `C~0`, this reduces to

`I_u ~ s^2/(v1 v2)`.

This makes the missing physical inputs explicit: row-specific covariance transduction `dC/du` and the actual detector-output variance/cross-noise matrix.

For a scalar variance row, the familiar result is

`I_u = 1/2 (d ln V/du)^2`

per independent real Gaussian sample.

## 7. Relation to stationary spectral Fisher

If the detector output is stationary and long-time Fourier bins are asymptotically independent complex Gaussian samples with one-sided spectral matrix `S(f)`, the corresponding rate is

`dot F_ij = eta_duty int_0^inf df Tr[S^-1 S_,i S^-1 S_,j]`

under the one-sided convention used by RQIR.

For a scalar flat log-PSD derivative `kappa=d ln S/du` over bandwidth `B`, this reduces to

`q_cov = eta_duty B kappa^2`,

recovering Iteration 022/033 as the stationary special case.

The current Toy009 rows do not yet satisfy the prerequisites for this reduction.

## 8. Coordinate-correct break-even in repeated-shot form

Iteration 034 gives the centered equal-row thresholds

- best first four force-covariance rows: `q_cov/R_P^(alpha) > 5.2397e5`;
- fifth row after those four: `> 1.1788e7`.

The coordinate-correct source QFI is

`F_Q^(alpha) ~= 0.0849323916`

per accepted single-branch preparation-metrology copy.

With

`q_cov = p_C eta_C I_cov^(shot)/t_C`,

`R_P^(alpha) = p_P eta_P F_Q^(alpha)/t_P`,

the equal-row first-four break-even becomes

`I_cov^(shot) * (p_C eta_C)/(p_P eta_P) * (t_P/t_C) > 4.4502e4`.

For the fifth row,

`... > 1.0012e6`.

Transparent equal-efficiency examples for the first four:

- `t_P/t_C=1e2` -> `I_shot > ~445`;
- `1e3` -> `> ~44.5`;
- `1e4` -> `> ~4.45`;
- `1e5` -> `> ~0.445`.

For the fifth row the corresponding thresholds are about `10012`, `1001`, `100`, and `10`.

These are not apparatus forecasts. They quantify exactly how fast/informative covariance readout must be relative to independent source metrology before covariance complementarity is a wall-clock win.

## 9. Consequence for experimental architecture

The current D2 covariance gate is no longer simply “measure a force PSD”. A viable implementation must declare at least one of:

1. a **phase-referenced repeated-shot** two-time/cross-channel detector likelihood;
2. a **cyclostationary spectral** likelihood retaining source-drive phase/harmonic indices;
3. a quantum measurement protocol that directly estimates the required symmetrized correlator and includes its backaction.

Only after this choice can the row-specific `q_i` needed by Iterations 033–034 be computed.

## 10. Reproducibility

Code:

`analysis/nonstationary_covariance_measurement_gate_iteration035.py`

The script verifies source nonstationarity, common-time-shift failure of the centered covariance, noncommutativity of the high-value covariance pairs, the general Gaussian covariance Fisher formula and the coordinate-correct cycle-rate break-even.

## 11. Next gate

The most conservative next step is a phase-referenced repeated-shot D2 model because it requires the fewest stationarity assumptions. Build a detector-output pair/cross-channel covariance matrix for the high-value rows `(0,1,3,7)`, include mean, imprecision and backaction nuisances in the same Fisher matrix, and determine whether any physically plausible per-shot information can satisfy the `4.45e4` first-four resource product without reopening the beta/source degeneracy.
