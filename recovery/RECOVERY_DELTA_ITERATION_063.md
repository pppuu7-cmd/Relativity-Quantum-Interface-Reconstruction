# RQIR Recovery Delta — Iteration 063

**Date:** 2026-08-30

Apply after Iteration 062.

## New retained rule

**RQIR-CAL-019 — physical detector nuisance belongs inside calibration co-design.**

For equal-whitened D2 bands use detector signal score

`s=(Re G2,Im G2,Re G4,Im G4)`

and relative spectral-tilt nuisance

`t=(Re G2,Im G2,-Re G4,-Im G4)`.

Profiling tilt gives exactly

`F_beta|tilt=4|G2|^2|G4|^2/(|G2|^2+|G4|^2)`.

Normalize source/calibration Fisher only after applying this physical detector metric if the intended D2 likelihood contains the tilt nuisance.

Re-optimized centered NP3 calibration cost ratios are approximately:

- Toy009: `1`;
- Toy011 response: `21.7`;
- Toy011 conditioning: `8.8`;
- Toy012 balanced: `4.7e4`;
- Toy012 high-response: `5.2e2`.

Therefore the old balanced Toy012 `~1.06x Toy009` calibration claim is **not** valid for the physical spectral-profiled D2 likelihood. Retain it only as an abstract Euclidean detector-geometry result.

Toy012 stays a locality existence/design example, not the physical source baseline.

## Reproduction

Run `analysis/d2_spectral_tilt_profiled_calibration_iteration063.py`.

## Next gate

Construct Toy013 with the detector likelihood inside the objective:

1. exact nearest-neighbour Jacobi-chain source;
2. positive hidden pair and rank-24 NP3 null;
3. preserve both n=2 and n=4 D2 bands using physical `S_eff`;
4. audit Pareto survivors with spectral-tilt-profiled centered calibration cost;
5. then source QFI/Ramsey and complementary D2 branches.
