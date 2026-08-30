# RQIR Recovery Delta — Iteration 102

**Date:** 2026-08-30  
**Parent front:** Iteration 101.

## What changed

Same-state dual-tone transfer calibration is now inserted directly into the science Fisher through a joint nuisance profile.

## RESOURCE-055 — transfer-gain Schur closure

For science derivative `s`, science metric `W`, transfer nuisance map `D`, and injected-calibration Fisher `C`,

`F_beta|g = s^T W s - s^T W D (D^T W D + C)^-1 D^T W s`.

## NG-056 — unconstrained per-band gains erase common amplitude

If two independent transfer gains span the science amplitude direction and `C=0`, then `F_beta|g=0`. More science exposure does not remove this exact detector-transduction degeneracy.

## STAT-003 — Gaussian mean/covariance orthogonality

In a standard multivariate Gaussian whose mean and covariance parameters are separate, a pure covariance parameter such as `rho` has zero expected Fisher cross block with a pure mean parameter. Its uncertainty changes the robust science metric and characterization cost; it is not the same Schur nuisance as a multiplicative gain.

**NG-057:** this separation is conditional and can fail for beta-dependent covariance, non-Gaussian/cyclostationary likelihoods, shared transfer/whitening parameters, or robust active-set changes.

## RESOURCE-056 — exact balanced wall-clock split

For symmetric raw band rate `r`, correlation `rho`, separate science time `T_sci`, and simultaneous per-gain transfer-calibration rate `c` during `T_cal`,

`F = 2 c r T_cal T_sci/[c T_cal(1+rho)+r T_sci]`.

With

`R_s=2r/(1+rho)`, `R_c=2c`,

`1/F = 1/(R_s T_sci)+1/(R_c T_cal)`.

For target `F_*=Z^2`:

`T_sci/T_cal=sqrt(R_c/R_s)`,

`T_total^min=F_*[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

Relative to perfect transfer calibration,

`P=[1+sqrt(R_s/R_c)]^2`.

Useful separate-time thresholds:

- `P<=1.10`: `R_c/R_s>=419.76`;
- `P<=1.25`: `R_c/R_s>=71.78`;
- `P<=2`: `R_c/R_s>=5.828`.

## Files

- `analysis/joint_science_transfer_profile_iteration102.py`
- `docs/PAPER_III_JOINT_SCIENCE_TRANSFER_PROFILE_ITERATION102.md`
- `research_log/2026-08-30_iteration_102_joint_science_transfer_profile.md`

## Immediate next gate

Move from the balanced scalar slice to the full four-real-component complex `f,2f` likelihood. Include transfer amplitude/phase, temporal covariance uncertainty, spectral tilt, and a shared budget across transfer calibration and all seven source/calibration layers. Optimize detector/calibration wall clock before adding `T_src` and duty. Do not start Toy015 unless the remaining dominant marginal cost is source-dependent.
