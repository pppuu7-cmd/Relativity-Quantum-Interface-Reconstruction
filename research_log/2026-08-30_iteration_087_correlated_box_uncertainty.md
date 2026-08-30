# RQIR Research Log — Iteration 087

**Date:** 2026-08-30

## Goal

Convert the corrected correlated dual-band science likelihood into a conservative apparatus-rate certificate under declared uncertainty intervals.

## Result

For

`R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`,

`R_beta` is strictly decreasing in `rho`. Therefore the worst correlation is always the interval upper endpoint `rho_hi`.

At fixed `rho`, each rate-coordinate slice has no interior minimum: for nonnegative correlation it is monotone, while for negative correlation its only interior stationary point is the finite maximum found in Iteration 086.

Hence for box uncertainty the exact lower bound is obtained by evaluating only the four rate corners at `rho_hi`.

New **RQIR-RESOURCE-040:** exact interval-robust dual-band lower envelope.

New **RQIR-NG-037:** a nominal anti-correlation gain is not a robust resource credit unless the upper uncertainty bound on correlation remains sufficiently negative. If the allowed correlation interval crosses zero, the conservative rate can fall sharply even when the nominal fit is favorable.

Example with `r2 in [0.8,1.2]`, `r4 in [3,5]`:

- `rho in [-0.6,-0.4]` -> robust lower `R_beta=3.7490549317691566`;
- `rho in [-0.6,0.1]` -> robust lower `R_beta=2.3358581142019457`.

For NG-030 use `T_sci^upper=Z^2/R_beta^lower`, then combine with lower calibration/source rates and upper control duty.

## Numerical regression

The deterministic code checks 200 random boxes with 2000 random interior points each and verifies no interior point falls below the analytic corner lower envelope. It also checks strict correlation monotonicity and the transparent examples.

## Reproduce

`python analysis/correlated_box_uncertainty_iteration087.py`

## Document

`docs/PAPER_III_CORRELATED_BOX_UNCERTAINTY_ITERATION087.md`
