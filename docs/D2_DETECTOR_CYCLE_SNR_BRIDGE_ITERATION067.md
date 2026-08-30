# RQIR Iteration 067 — D2 detector cycle/SNR bridge

**Date:** 2026-08-30  
**Status:** physical-resource bridge; no new-physics or hardware-feasibility claim.

## 1. Purpose

Iteration 066 reduced Toy013-vs-Toy009 total-time dominance to resource coordinates `x=T_cal,009/T_sci,009` and `y=T_src,009/T_sci,009`. The next required step is to convert the D2 science term into a physical repetition/SNR language without falsely assigning SI time to a normalized Fisher coordinate.

The spectral-tilt-profiled two-band source metric is

`S_eff = 4 |G2|^2 |G4|^2 / (|G2|^2+|G4|^2)`.

From Iteration 065,

- Toy013: `S_eff = 2.4438110707e-5`;
- Toy013/Toy009: `0.04228407350`.

Therefore

`S_eff,009 = 5.779507196013e-4`.

## 2. Independent-cycle detector bridge

For one declared statistically independent detector cycle, define the whitened physical leverage

`q = 2 |alpha| Gamma_G / sigma_phi`,

where `Gamma_G = G m_s m_p T_D/(hbar L_0)` and `sigma_phi` is the per-cycle demodulated quadrature noise in the same whitened coordinate used to define `S_eff`.

Then the detector-level beta Fisher per independent cycle is

`F_beta|tilt,cycle = q^2 S_eff`.

For target Gaussian significance `Z`, the white-noise independent-cycle lower bound is

`N_sci = Z^2/(q^2 S_eff)`.

At `Z=5`:

| q per independent cycle | Toy009 cycles | Toy013 cycles |
|---:|---:|---:|
| 1 | 43256.28 | 1022992.34 |
| 3 | 4806.25 | 113665.82 |
| 5 | 1730.25 | 40919.69 |
| 10 | 432.56 | 10229.92 |
| 30 | 48.06 | 1136.66 |
| 100 | 4.33 | 102.30 |

The ratio is invariant:

`N_013/N_009 = S_eff,009/S_eff,013 = 23.6495663`.

Thus Iteration 066's science-exposure penalty is now explicitly a repetition-count penalty for any common independent-cycle detector leverage `q`.

## 3. New negative/resource result — RQIR-NG-027

A quoted demodulated phase uncertainty `sigma_phi` does **not** by itself determine shot count or wall-clock time.

To call `N_sci` a physical repetition count one must state whether `sigma_phi` is:

- a single-cycle estimator variance;
- an ASD/PSD integrated over a declared estimator bandwidth;
- or an already averaged multi-cycle uncertainty.

Without cycle duration, estimator bandwidth/window, acceptance, dead time and inter-cycle covariance, using a demodulated `sigma_phi` as if it were shot noise double-counts averaging and can produce meaningless sub-one-shot requirements.

Retain **RQIR-NG-027: detector SNR is not a wall-clock resource until the acquisition likelihood is declared.**

## 4. Wall-clock lower bound once the acquisition model is declared

If cycles are independent and white-noise limited, with cycle duration `t_cyc`, dead time `t_dead` and retained-cycle probability `p`, then

`T_sci >= N_sci (t_cyc+t_dead)/p`.

This is only a lower bound. Colored drift, coherence loss, timing/additive controls and nuisance re-profiling must be added separately.

## 5. Consequence for Iteration 066

The Toy013-vs-Toy009 dominance inequality remains valid, but `x` cannot yet be assigned a physical number from the existing normalized calibration cost alone. The science denominator is now ready once a per-cycle detector likelihood is declared. The next gate is to derive the direct-force/relational calibration Fisher per the **same** detector cycle and noise PSD/ASD, so that `T_cal/T_sci` is dimensionless and apparatus-consistent.

## Reproducibility

`analysis/d2_detector_cycle_snr_bridge_iteration067.py`
