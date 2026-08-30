# RQIR Research Log — Iteration 067

**Date:** 2026-08-30

## What was done

Continued directly from Iteration 066 without reopening closed Toy searches. Converted the physical spectral-tilt-profiled D2 science metric into an explicit independent-cycle Fisher/repetition-count bridge.

## Inputs

- Toy013 `S_eff=2.4438110707e-5`;
- Toy013/Toy009 `S_eff` ratio `0.04228407350`.

Therefore Toy009 `S_eff=5.779507196013e-4`.

## Result

With per-independent-cycle whitened detector leverage

`q=2|alpha|Gamma_G/sigma_phi`,

`F_beta|tilt,cycle=q^2 S_eff`, so

`N_sci=Z^2/(q^2 S_eff)`.

At `Z=5`, `q=10`: Toy009 requires `432.5628` independent cycles and Toy013 `10229.9234`; the ratio is `23.6495663`, exactly matching the Iteration-066 science-exposure penalty.

## Negative/resource gate

Retain **RQIR-NG-027**: a demodulated detector uncertainty is not a physical shot/noise-time resource unless the acquisition likelihood declares cycle duration, estimator bandwidth/window, acceptance/dead time and inter-cycle covariance. Otherwise an already averaged `sigma_phi` may be misread as single-shot noise and averaging is double counted.

No new-physics claim. NG-005, NG-006, NG-023, NG-026 and all consistency gates remain active.

## Reproducibility

- `analysis/d2_detector_cycle_snr_bridge_iteration067.py`
- `docs/D2_DETECTOR_CYCLE_SNR_BRIDGE_ITERATION067.md`

## Next

Derive direct-force and relational-mean calibration Fisher per the same declared detector cycle/ASD coordinate. This is the missing bridge needed to turn Iteration-066 `x=T_cal/T_sci` into an apparatus-consistent number rather than a normalized Fisher proxy.
