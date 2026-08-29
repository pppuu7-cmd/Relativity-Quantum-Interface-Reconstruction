# RQIR Recovery Delta — Iteration 037

**Date:** 2026-08-29

## New retained result

**RQIR-NG-016 — affine covariance-only Gaussian Fisher bound:** for an `m`-dimensional real Gaussian phase-referenced detector output with

`Sigma(alpha)=Sigma0+alpha Sigma1`,

if the same affine covariance model remains positive definite for `alpha in [-1,1]`, then

`I_alpha^(shot)=1/2 Tr[(Sigma0^-1 Sigma1)^2] < m/2`.

Reason: positivity of `Sigma0 +/- Sigma1` forces all eigenvalues of `Sigma0^-1/2 Sigma1 Sigma0^-1/2` to have magnitude `<1`.

Special cases:

- scalar variance output: `Ishot<0.5`;
- bivariate covariance output: `Ishot<1`.

Current first-four D2 covariance/preparation product from Iteration 035 is `~4.4502e4`. Therefore a minimal bivariate covariance-only readout needs, necessarily,

`(pC etaC/pP etaP)*(tP/tC) > 4.4502e4`.

At equal efficiency:

- `tP=1 s` -> `tC<22.47 us`;
- `tP=100 s` -> `tC<2.247 ms`;
- `tP=1e4 s` -> `tC<0.2247 s`.

The fifth-row product `~1.0012e6` is much harsher.

## New resource rule

**RQIR-RESOURCE-013 — joint covariance Fisher accounting:** if one detector cycle yields several covariance observables simultaneously, do not sum independent row times. Use the full matrix Fisher of the shared output and profile nuisances jointly.

For an `m=8` joint Gaussian covariance-only output, the generic positivity ceiling is `Ishot<4`, so the first-four product gives the weaker necessary equal-efficiency cycle ratio `tP/tC>1.11255e4`. This is only an upper-envelope bound, not an achieved detector design.

## Retained previous corrections

Do not revert:

- RQIR-NUM-002: use `F_Q^(alpha)=0.0849323916`, not `13.27068619`, against current fractional-amplitude `C_alpha`;
- RQIR-CAL-013: use centered covariance derivatives in finite-noise likelihoods;
- RQIR-NG-014/015: current Toy009 covariance rows are nonstationary and ordering-sensitive;
- centered timing priors from Iteration 036: D1 `~11.0511 us`, D2 `~9.19001 us` at 100 Hz.

## Next gate

Build a joint phase-referenced D2 output for rows `(0,1,3,7)`, derive the matrix covariance derivative and include mean/timing/additive nuisances plus imprecision/backaction. Compare the shared-shot profiled Fisher/time directly to source-preparation metrology.
