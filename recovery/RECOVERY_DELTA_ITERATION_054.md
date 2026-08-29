# RQIR Recovery Delta — Iteration 054

**Date:** 2026-08-30

Apply this delta after canonical Iteration 053 / Toy011.

## New retained result

Toy011's exact nearest-neighbour source construction survives centered hard-constrained statistical identifiability, but current sampled local candidates are not yet resource-competitive with Toy009.

### Absolute two-band detector signal relative to Toy009

- local response candidate: D1 `0.14047`, D2 `0.17069`;
- local conditioning candidate: D1 `0.05119`, D2 `0.08417`.

At equal detector noise this corresponds to D2 science-integration penalties of about `5.86x` and `11.88x`.

### Normalized centered calibration cost

D2 optimized 14-mean + 8-centered-covariance cost ratios:

- local response / Toy009: `34.5982x`;
- local conditioning / Toy009: `10.0953x`.

D1 ratios:

- local response: `68.9330x`;
- local conditioning: `20.2949x`.

These are row-normalized geometry/resource ratios, not SI-hour predictions.

### Source metrology

Fractional-amplitude QFI per accepted copy:

- Toy009 `0.08493239`;
- local response `0.09081397`;
- local conditioning `0.08115776`.

Thus locality does not destroy fundamental source-amplitude distinguishability.

Energy-population Fisher:

- local response `0.003193808`;
- local conditioning `0.002828162`.

Ramsey rate coefficient `max F_alpha(phi)/phi`:

- Toy009 `0.002523439`;
- local response `0.000671217` (`0.2660x` Toy009);
- local conditioning `0.001058523` (`0.4195x`).

### Nuisance profile

With each source's own optimized D2 centered calibration, `C_alpha90(lambda)` stays close across sources. At `lambda=1.10`:

- Toy009 `100.80`;
- local response `108.52`;
- local conditioning `110.75`.

At `lambda=2.0`:

- `18.18`, `18.96`, `19.25`.

Therefore there is no new catastrophic beta/source-amplitude degeneracy caused by nearest-neighbour locality.

## New rule

**RQIR-RESOURCE-025 — locality multi-resource tradeoff**

Local-source candidates must be scored by total profiled information per wall time. Absolute detector signal, normalized calibration burden and physically accessible source-metrology rate are independent axes and can favor different points.

## Baseline decision

Do **not** replace Toy009 with Toy011 yet. Keep Toy009 as the statistical/resource baseline and Toy011 as the physicality-constrained branch.

## Next continuation step

Search the exact-spectrum nearest-neighbour manifold again, but rank candidates with a score that includes centered D2 calibration cost and absolute D2 signal from the start. The target is a candidate that substantially improves the present `10.1x` calibration penalty without losing another order of magnitude in raw D2 signal. Preserve QFI/Ramsey source-metrology rate as secondary Pareto diagnostics.