# RQIR Iteration 069 — Same-Time Dual-Probe Matrix-Fisher Calibration

**Date:** 2026-08-30  
**Status:** retained resource/measurement gate; no new-physics claim

## 1. Why this iteration was necessary

Iteration 068 converted the abstract mean-calibration strength `gamma` into a physical Fisher-rate expression, but deliberately left one important issue open: the two same-time probe channels in each of the seven D2 calibration layers cannot in general be treated as independent scalar SNR measurements.

Iteration 041 already established that the same-time dual-probe pair is the maximal disturbance-free grouping available in the current toy architecture. Therefore the correct next object is a **two-output likelihood with a full noise covariance/PSD matrix**.

This iteration does not reopen Toy009/Toy010/Toy012/Toy013 source searches. It only closes the acquisition-likelihood layer needed to interpret `gamma_mean` physically.

## 2. Two-output Gaussian calibration likelihood

At one stored phase, let the two row-normalized calibration coordinates be

`u=(u1,u2)`

and let the detector outputs be

`z=(z1,z2)`.

For a Gaussian single-cycle likelihood with mean Jacobian `J` and covariance `C`,

`F_layer = J^T C^{-1} J`.

The corresponding stationary one-sided spectral form is

`F_layer = 4 Re int_0^infty J(f)^dagger S_out(f)^(-1) J(f) df`,

where `S_out(f)` is the full `2x2` output/equivalent-force PSD matrix. Off-diagonal cross spectra must therefore be retained.

This is the physical matrix version of the Iteration-068 scalar relation

`I_mu = 4 int |d htilde/du|^2 / S_out df`.

## 3. Symmetric white-noise benchmark

To obtain an exact regression test without pretending to have selected a laboratory detector, take equal standardized single-channel score amplitudes `xi` and normalized noise covariance

`C = [[1,rho],[rho,1]]`,  `|rho|<1`.

Then

`J = xi I`,

and

`F_layer = xi^2/(1-rho^2) [[1,-rho],[-rho,1]]`.

Its two eigenvalues are exactly

`lambda_min = xi^2/(1+|rho|)`,

`lambda_max = xi^2/(1-|rho|)`.

Thus correlated readout does not have a single scalar "SNR penalty": one linear combination of the two calibration rows loses information while the orthogonal combination gains information.

## 4. RQIR-CAL-016 — matrix-PSD requirement for same-time dual probes

For a same-time dual-probe calibration layer, independent-row Fisher credit is valid only when the measured cross spectrum/covariance is negligible in the declared likelihood.

In general the correct block is

`F_j = 4 Re int J_j^dagger S_j^-1 J_j df`.

Adding two scalar `SNR^2` values discards cross-Fisher structure and can either overstate or understate the information in detector-relevant nuisance directions.

This is a measurement-model correction, not a new physical effect.

## 5. RQIR-RESOURCE-031 — robust correlation inflation factor

If the calibration design requires at least `gamma` Fisher in **every** direction of the two-row layer and the symmetric benchmark above applies, the accepted-cycle requirement is

`N_layer >= gamma/lambda_min`

or

`N_layer >= gamma (1+|rho|)/xi^2`.

Relative to the independent-channel limit, the robust isotropic cost inflation is therefore

`B_corr = 1+|rho|`.

This bound is specific to the declared symmetric two-channel benchmark. A real frequency-dependent transduction/PSD matrix must be integrated before using it as an apparatus forecast.

## 6. Exact numerical checks

For the retained benchmark `xi=3`:

| `rho` | `lambda_min` | robust inflation `B_corr` | Toy009 accepted layer-cycles, 7 layers | Toy012 accepted layer-cycles, 7 layers |
|---:|---:|---:|---:|---:|
| 0.00 | 9.000000 | 1.00 | 1,423,539.213 | 940,089.500 |
| 0.25 | 7.200000 | 1.25 | 1,779,424.017 | 1,175,111.875 |
| 0.50 | 6.000000 | 1.50 | 2,135,308.820 | 1,410,134.250 |
| 0.75 | 5.142857 | 1.75 | 2,491,193.624 | 1,645,156.625 |
| 0.90 | 4.736842 | 1.90 | 2,704,724.506 | 1,786,170.050 |

The `rho=0` Toy009 result exactly reproduces the Iteration-042 count after the Iteration-068 notation/resource correction:

`N_acc = 7 gamma_mean/xi^2 = 1,423,539.213`.

## 7. Wall-clock regression at the retained scheduling benchmark

Using the already-declared lower-bound scheduling assumptions

- gap frequency `100 Hz`;
- acceptance `p=0.5`;
- dead/readout time `1 ms` per layer-cycle;
- two probes acquired simultaneously within each layer;
- no extra preparation/reset time beyond the declared dead time;

we obtain for `xi=3`:

### Toy009

`T_mean(rho=0) = 5.00946094 h`,

`T_mean(rho=0.5) = 7.51419141 h`,

`T_mean(rho=0.9) = 9.51797579 h`.

### Toy012

`T_mean(rho=0) = 2.89133490 h`.

Under the same symmetric correlation model its time is multiplied by `1+|rho|`.

These are scheduling lower bounds, not apparatus forecasts. State preparation, reset, transfer calibration, colored drift, coherence failures and non-white detector noise remain additional costs.

## 8. Consequence for `x=T_cal/T_sci`

Iteration 068 gave

`x = gamma R_beta/Z^2 sum_j 1/R_mu,j`.

For a two-channel layer, `R_mu,j` must now be interpreted as a **matrix Fisher rate**. If an isotropic lower bound is needed, use the smallest relevant eigenvalue of the integrated Fisher block:

`R_mu,j^(robust) = p_j lambda_min(F_j)/tau_j`.

Therefore

`T_cal >= gamma sum_j 1/R_mu,j^(robust)`

is the correct conservative bridge to the detector wall clock.

## 9. What remains open

This iteration closes the algebraic correlation handling but does not yet select a physical detector. The next admissible gate is to insert one declared physical transduction Jacobian and one-sided equivalent-force/output PSD matrix for D2, including cross spectrum, and evaluate the seven integrated `2x2` Fisher blocks.

Only after that can the project quote an apparatus-specific `x=T_cal/T_sci` and combine it with source-metrology `y=T_src/T_sci` for the Toy009/Toy013 dominance boundary.

NG-005, NG-006, NG-023, NG-026, NG-027 and all relativistic/full-QFT/classical/stochastic consistency gates remain active.

## 10. Reproducibility

Run:

`python analysis/d2_dual_probe_matrix_fisher_iteration069.py`

The script verifies the analytic eigenvalues, reproduces the Iteration-042 `rho=0` accepted-cycle count, and checks the stated Toy009/Toy012 wall-clock benchmarks.
