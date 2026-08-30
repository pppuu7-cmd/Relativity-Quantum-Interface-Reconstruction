# RQIR Recovery Delta — Iteration 067

**Date:** 2026-08-30

## Retained advance

Iteration 067 bridges the spectral-tilt-profiled D2 science metric to physical detector repetition/SNR language without falsely assigning wall-clock seconds to a normalized Fisher coordinate.

From Iteration 065:

- `S_eff,013=2.4438110707e-5`;
- `S_eff,013/S_eff,009=0.04228407350`;
- hence `S_eff,009=5.779507196013e-4`.

For one statistically independent detector cycle define

`q=2|alpha|Gamma_G/sigma_phi`,

with `Gamma_G=G m_s m_p T_D/(hbar L_0)` and `sigma_phi` the per-cycle demodulated quadrature uncertainty in the same whitened coordinate used for `S_eff`.

Then

`F_beta|tilt,cycle=q^2 S_eff`,

and for target Gaussian significance `Z`,

`N_sci=Z^2/(q^2 S_eff)`.

At `Z=5`, `q=10`:

- Toy009: `N_sci=432.56283195`;
- Toy013: `N_sci=10229.92337654`;
- ratio `23.6495663`.

This reproduces the Iteration-066 science-exposure penalty as a cycle-count penalty under common detector leverage.

## New gate

**RQIR-NG-027:** detector SNR is not a wall-clock resource until the acquisition likelihood is declared. A demodulated `sigma_phi` cannot be treated as single-shot noise unless cycle duration, estimator bandwidth/window, acceptance, dead time and inter-cycle covariance are specified. Otherwise averaging may be double counted.

For independent white cycles only,

`T_sci >= N_sci (t_cycle+t_dead)/p_accept`.

## What remains open

The calibration numerator in Iteration-066 `x=T_cal,009/T_sci,009` still lacks a common physical per-cycle transduction/ASD map. Next derive direct-force and relational-mean calibration Fisher per the same detector cycle and then evaluate `x` without mixing normalized and SI coordinates.

Do not promote Toy013. NG-005, NG-006, NG-023, NG-026 and all gauge/conservation/QFT/relativistic consistency gates remain active.
