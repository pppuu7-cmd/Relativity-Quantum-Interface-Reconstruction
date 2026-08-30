# RQIR Recovery Delta — Iteration 082

**Date:** 2026-08-30  
**Authority:** append to `docs/RECOVERY_GUIDE.md` / `recovery/CURRENT_FRONT.md` when reconstructing the current Paper-III front.

## New externally anchored apparatus gate

Iteration 082 tested a real levitated-force sensor rather than importing an illustrative ASD.

External detector anchor (Liang et al., Fundamental Research 3, 57–62 (2023), DOI 10.1016/j.fmre.2022.09.021):

- mechanical resonance `~193.8 kHz`;
- feedback-cooled damping/linewidth scale `19.60 +/- 6.54 Hz` in the cited high-vacuum data;
- force sensitivity `6.33 +/- 1.62 zN/sqrt(Hz)`;
- best single measured force sensitivity `4.34 zN/sqrt(Hz)`;
- Allan-optimal time `~2751 s`;
- stable force resolution `166.40 +/- 55.48 yN`.

Do **not** apply this ASD to arbitrary RQIR frequencies.

## RQIR-NG-033 — single-resonance two-band incompatibility

Current RQIR D2 identifiability retains `n=2` and `n=4` bands and profiles a relative spectral-tilt nuisance. The surviving information obeys

`S_eff = 4 P2 P4/(P2+P4)`,

so losing either band sends `S_eff -> 0`.

For a `193.8 kHz` single resonance:

- align `n=2`: `f_gap=96.9 kHz`, other band `f4=387.6 kHz`, about `9888` linewidth scales away;
- align `n=4`: `f_gap=48.45 kHz`, other band `f2=96.9 kHz`, about `4944` linewidth scales away.

Therefore a record on-resonance force ASD does not by itself instantiate `R_beta` for the two-band RQIR likelihood. A direct substitution at both bands would overstate Fisher.

## Stability implication

The measured Allan optimum confirms that short-time PSD and long-time stability must remain separate resources. Do not extrapolate the best ASD indefinitely with `1/sqrt(T)` after the apparatus enters its stability-limited regime.

## Admissible next apparatus closure

Require one of:

1. two simultaneous mechanical modes/channels with measured transfer plus PSD/cross-PSD at both RQIR harmonics;
2. a calibrated broadband equivalent-force PSD spanning both bands;
3. a sequential-retuning joint likelihood with explicit relock duty, inter-setting gain/timing drift, calibration transfer uncertainty and source reproducibility.

Until then, NG-030 Toy009/Toy014 robust apparatus dominance remains open.

## Files

- `analysis/external_d2_frequency_compatibility_iteration082.py`
- `docs/PAPER_III_EXTERNAL_D2_FREQUENCY_COMPATIBILITY_ITERATION082.md`
- `research_log/2026-08-30_iteration_082_external_d2_frequency_compatibility.md`
