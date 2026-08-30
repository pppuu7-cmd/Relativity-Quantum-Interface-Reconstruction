# RQIR Research Log — Iteration 082

**Date:** 2026-08-30

## Goal

Advance Paper III beyond the generic apparatus-data obstruction of Iteration 081 by testing a real published levitated-force detector against the actual RQIR two-band likelihood requirements.

## External anchor

Liang et al. report an optically levitated silica-nanosphere force sensor with a resonance near 193.8 kHz, high-vacuum damping rate 19.60 +/- 6.54 Hz, force sensitivity 6.33 +/- 1.62 zN/sqrt(Hz), best measured sensitivity 4.34 zN/sqrt(Hz), Allan-optimal stability time about 2751 s, and stable force resolution 166.40 +/- 55.48 yN.

Kamba et al. (PRL 137, 050801, 2026) independently demonstrate a two-order-of-magnitude acceleration-sensitivity enhancement by rapid trap quench, but do not supply the full two-band RQIR PSD/cross-PSD and calibration likelihood.

## Result

The external ASD cannot be inserted directly into current RQIR D2 Fisher.

Current science bands are `f2=2 f_gap` and `f4=4 f_gap`. If the 193.8-kHz resonance is aligned to `n=2`, the `n=4` band lies at 387.6 kHz, about 9888 reported-linewidth scales away. If the resonance is aligned to `n=4`, the `n=2` band lies at 96.9 kHz, about 4944 linewidth scales away.

New **RQIR-NG-033**: a single narrowband resonance sensitivity cannot normalize a two-band RQIR discriminator when spectral-tilt identifiability requires nonzero whitened information in both bands. Using the best on-resonance ASD for both bands would over-credit Fisher and can falsely evade the tilt degeneracy.

The external Allan data also provide a real stability warning: short-time ASD and long-time campaign stability are distinct resources. The 2751-s Allan optimum and 166.4 yN stable resolution support retaining the RQIR-NG-007/DRIFT separation rather than extrapolating best ASD indefinitely as 1/sqrt(T).

## Decision

Do not report absolute Toy009/Toy014 hours from this single-mode detector.

Next apparatus gate: find or parameterize either (a) a two-mode detector with transfer+PSD at both harmonics, (b) a genuinely broadband equivalent-force sensor, or (c) a sequential-retuning likelihood including relock duty, inter-setting drift, calibration uncertainty and source reproducibility.

## Reproduce

`python analysis/external_d2_frequency_compatibility_iteration082.py`

## Document

`docs/PAPER_III_EXTERNAL_D2_FREQUENCY_COMPATIBILITY_ITERATION082.md`
