# RQIR Recovery Delta — Iteration 083

**Date:** 2026-08-30

## New likelihood gate

Iteration 083 derives the correct minimal nuisance profile for sequentially retuning one narrowband detector between the two retained RQIR science harmonics.

For raw whitened science information `P2,P4`, independent retuned-setting gain nuisances and independent gain-reference Fisher `C2,C4`, the exact profiled result is

`F_beta = P2 C2/(P2+C2) + P4 C4/(P4+C4)`.

## RQIR-NG-034

If both retuned settings have independent unconstrained gains (`C2=C4=0`), then `F_beta=0` at any science exposure. Sequential acquisition of both harmonics is not equivalent to the simultaneous two-band spectral-tilt likelihood.

For isolated per-setting retention fraction `r`, require

`C_i=[r/(1-r)]P_i`.

Thus 90%, 95%, 99% retention require `C_i/P_i = 9,19,99` respectively.

## Resource implication

Sequential retuning must include separate science times, separate gain-reference times, relock/recertification duty, timing/phase drift, calibration transfer uncertainty and source reproducibility. The single published on-resonance ASD from Iteration 082 is insufficient.

## Next priority

Prefer a simultaneous dual-mode/broadband detector with measured transfer plus PSD/cross-PSD at both bands. If none is available, construct the full sequential-retuning apparatus envelope including `R_g2,R_g4` and low-frequency drift, then combine it with `R_src` and seven `R_cal,j` before NG-030 branch dominance.

## Files

- `analysis/sequential_retuning_gain_profile_iteration083.py`
- `docs/PAPER_III_SEQUENTIAL_RETUNING_LIKELIHOOD_ITERATION083.md`
- `research_log/2026-08-30_iteration_083_sequential_retuning_likelihood.md`
