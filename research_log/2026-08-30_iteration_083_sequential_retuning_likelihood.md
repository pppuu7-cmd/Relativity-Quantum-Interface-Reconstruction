# RQIR Research Log — Iteration 083

**Date:** 2026-08-30

## Goal

Follow the Iteration-082 single-resonance incompatibility by deriving the correct minimal likelihood for a narrowband detector that is sequentially retuned between the two retained RQIR harmonics.

## Result

For whitened science informations `P2,P4`, independent retuned-setting gain nuisances `g2,g4`, and independent gain-reference Fisher `C2,C4`, profiling gives

`F_beta = P2 C2/(P2+C2) + P4 C4/(P4+C4)`.

New **RQIR-NG-034**: if the two retuned configurations have independent unconstrained gains (`C2=C4=0`), then `F_beta=0` regardless of science exposure. Measuring both harmonics sequentially does not reproduce the simultaneous two-band spectral-tilt discriminator unless inter-setting gain/reference structure is physically supplied.

For each isolated setting, retaining fraction `r` requires `C_i=[r/(1-r)]P_i`; therefore 90/95/99% retention requires gain-reference Fisher equal to 9/19/99 times that setting's science information.

## Decision

Sequential retuning is admissible only with per-setting measured transfer/PSD, gain/relock reference Fisher, timing/phase recertification, source reproducibility and relock/stability duty. A simultaneous dual-mode/broadband detector remains preferred because it can preserve a genuinely shared likelihood.

## Reproduce

`python analysis/sequential_retuning_gain_profile_iteration083.py`

## Document

`docs/PAPER_III_SEQUENTIAL_RETUNING_LIKELIHOOD_ITERATION083.md`
