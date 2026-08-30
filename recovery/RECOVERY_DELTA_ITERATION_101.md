# RQIR Recovery Delta — Iteration 101

**Date:** 2026-08-30  
**Parent front:** Iteration 100.

## What changed

Paper III advanced from a generic same-platform spatial cross-spectrum to a concrete **same-state temporal `f,2f` calibration protocol**.

A search of the same UCL experimental family confirmed useful mode-frequency/control and harmonic-force/block-averaging capability, but did not expose a public dataset that directly supplies the RQIR temporal `f,2f` input-force covariance and two-tone transfer in one science state. Therefore the next cut was derived as an engineering protocol rather than filled with stitched literature values.

## RESOURCE-053 — finite-window temporal covariance

For same-record demodulated bands,

`C_24 = integral dnu/(2 pi) S_y(nu) W_2^*(nu) W_4(nu)`.

For white noise and a rectangular window,

`c_24=exp[-i pi fT] sinc(fT)`.

## DESIGN-011 — integer-cycle white-noise null

If `T=M/f`, integer `M!=0`, the white-noise overlap between `f` and `2f` vanishes exactly.

## NG-054 — orthogonal bins do not certify `rho=0`

Colored/nonstationary/window-leaked/shared-nuisance noise can retain finite cross-band covariance. A deterministic AR(1) finite-block regression gives `|corr|~=0.03655` for lag coefficient `0.8` despite orthogonal DFT bins.

## RESOURCE-054 — correlation-retention target

For fixed raw rates,

`R_beta=4r2r4/[r2+r4+2rho sqrt(r2r4)]`.

For balanced bands, nominal `rho0=0`, and required retained science fraction `q=0.90`:

`rho_hi <= 1/9 ~= 0.111111`.

For ideal independent real bivariate Gaussian blocks with marginal variances profiled,

`I_rho=1/(1-rho^2)^2`.

At `z=1.96`, the transparent lower bound is

`N_rho>=312` independent blocks.

The Gosling `T_b=3.3 ms` value implies `1.0296 s` only as an illustrative raw block-time scale, not as an RQIR apparatus forecast.

## CAL-021 — same-state dual-tone transfer Fisher

Inject known forces at `f` and `2f` in the science operating state and use the same demodulation filters. For the four-real-component output vector,

`F_cal=J_chi^T Sigma_z^-1 J_chi`.

The calibration must share feedback, trap, gain, window and sampling state with science or include an explicit uncertain state-transfer model.

For a conservative common fractional transfer-amplitude error `epsilon_g`, retaining fraction `q` requires

`epsilon_g<=1-sqrt(q)`.

At `q=.90`, `epsilon_g<=0.0513167`.

With one-block fractional-transfer Fisher `SNR_inj^2` and `z=1.96`:

`N*SNR_inj^2>=1458.80`.

Examples: SNR 10 -> 15 blocks; SNR 5 -> 59 blocks.

## NG-055 — dual-tone linearity gate

Calibration Fisher cannot be credited if high-amplitude injection drives actuator/detector/feedback nonlinearities that generate harmonics or intermodulation absent from the weak science signal.

## Reproducibility note

`analysis/crossover_value_of_information_iteration094.py` was corrected so source-rate interval contractions use the correct monotonic active endpoints. The published Iteration-094 formulas and leverage numbers are unchanged.

Parallel-numbering duplicate drafts were removed before recording this delta.

## Files

- `analysis/same_state_f2f_calibration_protocol_iteration101.py`
- `docs/PAPER_III_SAME_STATE_F2F_CALIBRATION_PROTOCOL_ITERATION101.md`
- `research_log/2026-08-30_iteration_101_same_state_f2f_calibration_protocol.md`

## Immediate next gate

Construct one joint science + injected-transfer likelihood with transfer amplitude/phase and temporal `rho` inside the nuisance vector. Compute `F_beta|transfer,rho` and optimize calibration/science block allocation in physical wall time. This determines whether cross-covariance, transfer calibration, or science exposure is the active detector bottleneck. Do not open Toy015 unless the residual bottleneck is demonstrated to be source-dependent.
