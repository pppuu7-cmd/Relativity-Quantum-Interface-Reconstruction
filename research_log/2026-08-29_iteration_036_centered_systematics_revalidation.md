# RQIR Research Log — Iteration 036

**Date:** 2026-08-29  
**Target:** revalidate low-rank timing/geometry/additive control requirements after the Iteration-034 centered-noise correction.

## Result

RQIR-NG-006 survives. With no independent control priors, profiled `F_beta|theta` remains numerical zero for both D1 and D2 even at `100x` gravitational calibration exposure.

Using the same conservative 10%-row-sigma construction on the centered likelihood:

### D1

- `sigma(delta tau) ~=6.94360e-3`;
- timing at 100 Hz: `~11.0511 us`;
- `sigma(b_mean) ~=8.88857e-5`;
- `sigma(b_cov) ~=1.26818e-4`;
- restored `F_beta|theta ~=0.899915`.

### D2

- `sigma(delta tau) ~=5.77425e-3`;
- timing at 100 Hz: `~9.19001 us`;
- `sigma(b_mean) ~=7.39168e-5`;
- `sigma(b_cov) ~=1.30175e-4`;
- restored `F_beta|theta ~=0.899893`.

These replace the old raw-second-moment `9.47 us` / `8.01 us` timing numbers as the current centered-likelihood first-order benchmark.

## Raw centered-offset ranges

D1:

- mean `3.396e-5` to `1.219e-4`;
- centered covariance `7.750e-6` to `8.109e-5`.

D2:

- mean `2.824e-5` to `1.014e-4`;
- centered covariance `7.955e-6` to `8.323e-5`.

SI conversion still requires the physical readout Jacobian.

## Updated transparent drift cadence

With `sigma_event=10 us`, `sigma_ref=target/3`, acceptance `0.5`, coherence-floor shot time and `1 ms` dead time:

- reference block: `~0.131812 s` D1, `~0.190604 s` D2;
- at `D=100 us^2/h`: cadence `~2.17114 h` D1, `~1.50145 h` D2;
- at `D=1000 us^2/h`: `~13.03 min` D1, `~9.01 min` D2;
- equal-diffusion cadence ratio D2/D1 `~0.69155`.

RQIR-NG-007 remains unchanged.

## Files

- `analysis/centered_systematics_revalidation_iteration036.py`
- `docs/CENTERED_SYSTEMATICS_REVALIDATION.md`
- `recovery/RECOVERY_DELTA_ITERATION_036.md`

## Next gate

Use the centered priors inside a phase-referenced D2 covariance measurement likelihood for rows `(0,1,3,7)`. The remaining dominant unknown is detector-output covariance transduction/backaction Fisher, not first-order timing statistics.
