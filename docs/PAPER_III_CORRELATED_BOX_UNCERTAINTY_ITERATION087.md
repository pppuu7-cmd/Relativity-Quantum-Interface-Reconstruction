# RQIR Iteration 087 — Exact Box-Uncertainty Lower Bound for Correlated Dual-Band Fisher

**Date:** 2026-08-30  
**Status:** Paper-III robustness gate; not an apparatus forecast and not a new-physics claim.

## 1. Purpose

Iteration 086 corrected the correlated-band design law and showed that anti-correlation can create a finite optimum. That makes nominal-rate optimization insufficient: Paper III needs a conservative `R_beta` lower bound after uncertainty in both raw band rates and cross-correlation is propagated.

Assume declared independent intervals

`r2 in [r2_lo,r2_hi]`,

`r4 in [r4_lo,r4_hi]`,

`rho in [rho_lo,rho_hi]`,

with positive rates and `-1<rho_lo<=rho_hi<1`.

Use the retained exact likelihood

`R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`.

## 2. Correlation monotonicity

At fixed positive `r2,r4`,

`d R_beta/d rho = -8 (r2 r4)^(3/2)/D^2 < 0`,

where

`D=r2+r4+2 rho sqrt(r2 r4)>0`.

Therefore the worst correlation in an interval is always

`rho=rho_hi`.

This remains true whether the nominal correlation is positive or negative.

## 3. No interior rate minimum

Fix `r4=b` and write

`t=sqrt(r2/b)`.

Then

`R_beta/b = 4 t^2/(t^2+1+2 rho t)`

with derivative

`8 t(1+rho t)/(t^2+1+2 rho t)^2`.

For `rho>=0`, the slice is monotone increasing. For `rho<0`, its only interior stationary point is the finite maximum from Iteration 086.

Hence a one-dimensional slice has no interior minimum. Applying the same argument in the other rate coordinate means the exact minimum over a rectangular rate uncertainty set occurs at a rate corner.

## 4. RQIR-RESOURCE-040 — exact interval-robust lower envelope

For box uncertainty, the exact conservative science rate is

`boxed{R_beta^lower = min R_beta(r2,r4,rho_hi)}`

over only the four combinations

`r2 in {r2_lo,r2_hi}`,

`r4 in {r4_lo,r4_hi}`.

No dense scan or Monte Carlo is required for this uncertainty model.

This result is exact for independent interval bounds. It does not replace a correlated statistical uncertainty set for measured spectral matrices; if the rate/correlation estimates have joint covariance or physical PSD constraints, that more informative uncertainty set should be propagated directly.

## 5. RQIR-NG-037 — nominal anti-correlation gain is not a robust certificate

A nominal negative `rho` can strongly improve the best-fit `R_beta`, but the robust value is controlled by the **largest allowed rho**, not the nominal or most negative value.

If the uncertainty interval crosses zero, the worst case may lose essentially all of the nominal anti-correlation advantage.

Transparent example:

`r2 in [0.8,1.2]`,

`r4 in [3,5]`.

If

`rho in [-0.6,-0.4]`,

the exact robust lower rate is

`R_beta^lower = 3.7490549317691566`,

attained at `(r2,r4,rho)=(0.8,3,-0.4)`.

If only the correlation uncertainty is widened to

`rho in [-0.6,+0.1]`,

the robust lower rate drops to

`R_beta^lower = 2.3358581142019457`.

Thus a detector cannot claim anti-correlation resource credit unless the cross-PSD sign and magnitude remain bounded tightly enough over the relevant campaign.

## 6. Relation to NG-030 robust architecture dominance

NG-030 requires conservative nonoverlap of total wall-clock intervals.

Iteration 087 supplies the detector-side ingredient:

`T_sci^upper = Z^2/R_beta^lower`.

The same philosophy must be used for calibration and source metrology:

- use lower Fisher-rate bounds for all seven `R_cal,j`;
- use a lower bound on independent `R_src`;
- use an upper bound on control/reference duty;
- propagate correlations when those resource estimates are not independent.

Only then is `T_total^upper` suitable for Toy009/Toy014 robust dominance.

## 7. Numerical regression

`analysis/correlated_box_uncertainty_iteration087.py` checks:

- the exact two transparent examples above;
- monotonic decrease of `R_beta` with increasing `rho`;
- 200 random uncertainty boxes with 2000 random interior samples each, verifying no interior sample falls below the analytic corner bound;
- exact corner construction of the lower envelope.

The code uses a fixed seed `20260830`.

## 8. Scope

This is a local Gaussian two-sufficient-channel result. It assumes the uncertainty box is itself a valid summary of the measured spectral-matrix uncertainty and remains inside the ordinary positive-definite domain.

Near-singular or strongly correlated spectral-matrix estimates should use their full joint confidence region/eigenvalue constraints rather than independent boxes.

## 9. Next gate

The science-rate robustness algebra is now sufficient for a declared apparatus input. The next highest-value Paper-III step is to propagate the **same uncertainty-safe rate construction through the seven same-time dual-probe calibration layers**, producing conservative `R_cal,j^lower`, `H_cal^lower`, and a calibration wall-clock upper bound. Then combine with `R_src^lower` and duty to evaluate NG-030 robust Toy009/Toy014 dominance.
