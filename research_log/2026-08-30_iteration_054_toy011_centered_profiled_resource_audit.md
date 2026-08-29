# RQIR Research Log — Iteration 054

**Date:** 2026-08-30  
**Target:** pass Toy011 through centered hard-constrained nuisance profiling and separate local-source detector signal cost from calibration/source-metrology cost.

## Result

Toy011 locality does **not** create a new principle-level beta/source-amplitude degeneracy. The `C_alpha(lambda)` curves remain close to Toy009 after each source is given its own optimized centered calibration weights.

The important costs are elsewhere.

### Absolute detector signal

Relative D2 raw two-band Fisher proxy:

- Toy009: `1`;
- Toy011 response candidate: `0.17069`;
- Toy011 conditioning candidate: `0.08417`.

Thus equal detector noise would require about `5.86x` and `11.88x` more science integration, respectively, to recover Toy009 raw D2 Fisher.

### Normalized centered D2 calibration cost

Using 14 mean + 8 centered covariance rows and exact trace+energy elimination:

- Toy009 total normalized cost: `~3.0345e7`;
- local response: `~1.0499e9`, ratio `~34.60x`;
- local conditioning: `~3.0634e8`, ratio `~10.10x`.

D1 cost ratios are still larger: `~68.93x` and `~20.29x`.

### Source information

Full QFI in fractional amplitude coordinate:

- Toy009 `0.0849324`;
- local response `0.0908140`;
- local conditioning `0.0811578`.

So fundamental preparation distinguishability survives locality.

Simple energy-population Fisher falls to `0.00319381` and `0.00282816`, about one third of Toy009's `0.00939188`.

The QND Ramsey Fisher-rate coefficients `max F_alpha(phi)/phi` are

- Toy009 `0.00252344`;
- local response `0.000671217` (`0.266x`);
- local conditioning `0.00105852` (`0.419x`).

### Nuisance-profile stability

At D2 calibration scale `lambda=1.10`, required `C_alpha90` is

- Toy009 `~100.80`;
- local response `~108.52`;
- local conditioning `~110.75`.

At `lambda=2`, values are `~18.18`, `~18.96`, `~19.25`.

Hence the locality penalty is not a new hidden-amplitude identifiability collapse.

## New retained rule

**RQIR-RESOURCE-025 — locality multi-resource tradeoff**

A locality-constrained source must be ranked by total profiled information per wall time. Raw detector signal, normalized calibration burden and physically accessible source-metrology rate are independent resource axes and may favor different candidates.

## Decision

Do not promote Toy011 over Toy009 yet. The current conditioning-oriented local point is resource-superior to the response-oriented local point in calibration and simple Ramsey metrology, but both still pay large absolute detector-signal penalties.

## Files

- `analysis/toy011_centered_profiled_resource_audit_iteration054.py`
- `docs/TOY011_CENTERED_PROFILED_RESOURCE_AUDIT.md`
- `recovery/RECOVERY_DELTA_ITERATION_054.md`

## Next gate

Run a new exact-spectrum nearest-neighbour source/calibration co-design search with a score that explicitly contains centered D2 calibration cost and absolute D2 signal, rather than using `s_min` or raw D2 response alone. Preserve QFI/Ramsey rate as secondary Pareto axes.