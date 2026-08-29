# RQIR Recovery Delta — Iteration 022

**Date:** 2026-08-29

## State entering this iteration

Iteration 021 had a correct hard-constrained wall-clock optimizer but still required external rates `R_M`, `R_C`, and reference-control rates. A unique SI-time optimum was therefore underdetermined.

## New retained formulas

### D1 mean calibration
At binary phase-readout quadrature,
`I_phi = C^2` per accepted event. For row transduction `k_i=dphi/du_i`,

`R_M,i = p_acc C_i^2 k_i^2 / t_cycle`.

### Gaussian covariance/noise calibration
Per independent Gaussian sample,
`I_ab = 1/2 Tr(Sigma^-1 Sigma_,a Sigma^-1 Sigma_,b)`.
For a scalar unit log-variance coordinate, `I=1/2`; with about `2BT` real independent modes,

`R_C ~= duty * B * k_C^2`.

### D2 mean calibration
Use the one-sided force-PSD/template form

`I_i = 4 integral |dh_i/du_i|^2/S_F df`,

with duty/live-time normalization kept explicit.

### Timing reference
For `delta_tau = omega_gap delta_t` and event timestamp RMS `sigma_t,event`,

`R_tau = p_acc/[t_cycle (omega_gap sigma_t,event)^2]`.

To reach a physical target `sigma_t,target`,

`T_tau = t_cycle/p_acc * (sigma_t,event/sigma_t,target)^2`.

The explicit gap frequency cancels under consistent unit conversion.

### Additive/gain references
`R_b = p_acc/(t_cycle sigma_b,event^2)`.

For fractional gain with known-reference event SNR `rho_g`,
`R_g = p_acc rho_g^2/t_cycle`.

## New retained principles

- **RQIR-RESOURCE-006:** nuisance-coordinate normalization cannot by itself create a physical wall-time cost; reference cost is set by physical event precision, cycle/acceptance and the required physical prior.
- **RQIR-DRIFT-002:** high-rate white timing-reference statistics do not certify long-run timing stability. Once white information is cheap, low-frequency/common-mode drift is the relevant gate.

## Transparent benchmarks only

Using current corrected row weights, `f_gap=100 Hz`, `tau_max=4.99085067`, `1 ms` extra dead time and `p_acc=0.5`:

- coherence floor ~`7.94 ms`;
- D1 unit-coupling (`C=0.66`, `k=1 rad/unit`) sequential 14-row mean calibration ~`275 h`;
- D2 corrected mean weights under the same deliberately artificial readout benchmark ~`386 h`;
- 8 sequential covariance rows at `B=1 kHz`, unit log-variance sensitivity ~`2.08 h` D1 and `2.07 h` D2.

These are not hardware predictions. They demonstrate why equal dimensionless Fisher weights do not imply equal wall-time costs.

## Current frontier

Next: replace independent white timing/additive priors by colored drift PSD / Allan-variance models, derive required recalibration cadence across the D1/D2 acquisition campaign, and insert its time cost into the Iteration-021 optimizer.
