# RQIR Research Log — Iteration 101

**Date:** 2026-08-30

## Goal

Continue from authoritative Iteration 100 and close the next detector/calibration gate without starting Toy015: determine the minimum same-state temporal `f,2f` acquisition and injected-transfer protocol needed to turn the measured spectral-matrix capability into an RQIR input-referred force certificate.

## External follow-up

A search of the same UCL experimental family retained two complementary facts:

- Pontin et al., *Phys. Rev. Research* 5, 013013 (2023), demonstrate controlled mechanical mode frequencies/orientations and measured `S_xy(omega)`;
- Gosling et al., *Phys. Rev. Research* 6, 013129 (2024), include a harmonic force example near 149 kHz and finite force-spectrum averaging with example block length `T_b=3.3 ms`.

The public sources inspected did not provide a same-state two-tone `f,2f` force-transfer measurement plus the temporal two-band covariance required by APP-003. The literature substitution route therefore remains incomplete.

## New results

### RESOURCE-053 — finite-window temporal covariance kernel

For two demodulators on one scalar time series,

`C_24 = integral dnu/(2 pi) S_y(nu) W_2^*(nu) W_4(nu)`.

Thus center-frequency ASDs do not determine temporal band covariance.

### DESIGN-011 — integer-cycle white-noise orthogonality

For white input-referred noise and a rectangular block,

`c_24=exp[-i pi fT] sinc(fT)`.

If `T=M/f` with nonzero integer `M`, `c_24=0` exactly.

### NG-054 — Fourier-bin orthogonality is not a general `rho=0` certificate

A finite AR(1) stationary regression with 64 samples and bins `(3,6)` gives essentially zero correlation for white noise but `|corr|~=0.03655` at lag coefficient `0.8`. Colored finite-record leakage can therefore generate nonzero temporal covariance even for orthogonal DFT bins.

### RESOURCE-054 — robust correlation certification

For fixed raw rates and nominal `rho0`, requiring robust rate retention `q` gives an analytic upper bound on `rho_hi`.

For balanced bands, `rho0=0`, `q=0.90`:

`rho_hi <= 1/9 ~= 0.111111`.

For an ideal independent real bivariate Gaussian block with marginal variances profiled,

`I_rho=1/(1-rho^2)^2`.

Using `z=1.96` gives

`N_rho >= 312` independent blocks.

The Gosling `3.3 ms` block would correspond to `1.0296 s` only as an illustrative raw-integration scale; it is not an RQIR apparatus forecast.

### CAL-021 — same-state dual-tone transfer calibration

Inject known tones at `f` and `2f` in the science operating state and demodulate with the same filters. Use the joint four-real-component likelihood and full covariance:

`F_cal=J_chi^T Sigma_z^-1 J_chi`.

Transfer calibration from a different feedback/trap/gain/window state cannot be inserted without a calibrated state-transfer nuisance model.

### Transfer-amplitude target

If both raw band rates share worst fractional transfer-amplitude error `epsilon_g`, retaining fraction `q` requires

`epsilon_g <= 1-sqrt(q)`.

At `q=0.90`, `epsilon_g<=0.0513167`.

For matched one-block fractional-transfer Fisher `SNR_inj^2`, `z=1.96` requires

`N SNR_inj^2 >= 1458.80`.

Examples: SNR 10 -> 15 blocks; SNR 5 -> 59 blocks.

### NG-055 — dual-tone linearity/intermodulation gate

High-SNR `f,2f` injection only counts if actuator, detector and feedback response remain linear. Harmonic/intermodulation products from the calibration itself must be audited.

## Reproducibility correction retained

During this continuation, a pre-existing implementation error in `analysis/crossover_value_of_information_iteration094.py` was corrected: source-rate interval contractions now use the proper active endpoints (`R_lo` for the robust upper-time branch and `R_hi` for the lower-time branch). The published Iteration-094 formulas/leverage values were already based on the intended monotonic endpoints; scientific conclusions are unchanged.

Conflicting non-authoritative duplicate files that arose during parallel iteration numbering were removed before Iteration 101 was committed, preserving one authoritative chronology.

## Files

- `analysis/same_state_f2f_calibration_protocol_iteration101.py`
- `docs/PAPER_III_SAME_STATE_F2F_CALIBRATION_PROTOCOL_ITERATION101.md`
- `recovery/RECOVERY_DELTA_ITERATION_101.md`

## Next gate

Build one joint science + injected-transfer likelihood with transfer amplitude/phase and temporal `rho` inside the nuisance vector. Compute the Schur-complement science Fisher rate and optimize the split between calibration blocks and science blocks. The result should identify whether cross-covariance estimation, transfer calibration, or raw science exposure is the dominant detector cost before any Toy015 search is considered.
