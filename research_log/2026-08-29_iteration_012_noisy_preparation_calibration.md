# RQIR Research Log — Iteration 012 — Noisy Preparation + Calibration Fisher Gate

**Date:** 2026-08-29  
**Labels:** `DRV`, `NUM`, `NEG`, `OPEN`

## Goal

Replace the exact-null interpretation of Toy 010 by a local noisy Fisher model that includes:

- interface amplitude `beta`;
- uncertain amplitude `a` of the prepared source difference along the exact gravitational null direction;
- 24 orthogonal Hermitian source-state nuisance directions;
- finite row-normalized gravitational calibration information;
- independent nongravitational source-preparation information.

## New negative result — RQIR-NG-005

Because Toy 010's gravitational calibration obeys `A n=0`, the amplitude `a` along the desired null direction is invisible to that calibration.

The detector response depends locally on `beta a`, so at the nominal point

`d mu / d beta = d mu / d a`.

Without independent preparation information on `a`, profiling the source amplitude gives

`F_beta = 0`

for every tested gravitational calibration strength, including the infinite-precision limit on the 24 orthogonal directions.

Conclusion: the gravitational null experiment cannot self-calibrate the amplitude of the very hidden source direction it exploits.

## Independent preparation Fisher

Add source-preparation information `C_a` on `a` and normalize detector-only beta Fisher to `S=1`.

If all orthogonal source nuisances are perfectly known,

`F_beta = C_a/(1+C_a)`.

Therefore retaining 90% of detector information requires `C_a/S=9`, i.e. preparation-amplitude SNR about three times the detector response SNR. 95% requires `C_a/S=19`; 99% requires `99`.

## Full 24-nuisance Toy 010 Fisher

Use real/imaginary D1 response quadratures at harmonics `n=2,4` as detector data.

Row-normalized Toy 010 calibration has

`s_min ~ 2.21101e-3`

and crude inverse-squared information scale

`1/s_min^2 ~ 2.05e5`.

With effectively perfect source-amplitude preparation calibration, the full Fisher calculation requires approximate row-normalized gravitational calibration strengths:

- 50% detector-information retention: `gamma ~ 1.2e5`;
- 80%: `gamma ~ 5.0e5`;
- 90%: `gamma ~ 1.2e6`;
- 95%: `gamma ~ 2.5e6`.

With `C_a=9`, the asymptotic maximum is 90%; about 80% retention requires `gamma ~ 9e5`.

`gamma` is an abstract dimensionless information strength in the present whitened/row-normalized model, not yet an instrument SNR.

## Conditioning interpretation

Toy 009 inherited calibration:

`1/s_min^2 ~ 4.37e5`.

Toy 010:

`1/s_min^2 ~ 2.05e5`.

The improved Toy 010 conditioning reduces this crude finite-noise burden scale by a factor about `2.14`.

Thus conditioning is now connected directly to statistical resource cost rather than treated only as numerical stability.

## New operational rule — RQIR-CAL-003

A viable ordered-response experiment needs two distinct source-characterization layers:

1. gravitational/null calibration for ordinary mean/noise nuisance directions;
2. nongravitational preparation calibration for amplitude/quantum coordinates deliberately invisible to the gravitational null test.

Both are required for local identifiability of the interface parameter.

## Reproducibility

- `analysis/toy010_noisy_calibration_fisher.py`
- `docs/STATISTICAL_IDENTIFIABILITY_002_NOISY_PREPARATION_CALIBRATION.md`

## Next

Translate abstract `gamma` and `C_a` into physical measurement counts, noise PSD/shot noise and integration/coherence budgets for a concrete D1 source-preparation and gravitational-calibration protocol.
