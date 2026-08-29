# RQIR Iteration 031 — Finite-Reference D2 Profiled Fisher

**Date:** 2026-08-29

## Question

Iteration 030 showed that a D2 force readout can only implement a potential calibration relationally, through `B(y)-B(y_ref)`, and that the calibration nullspace rotates as the finite reference position changes. This iteration asks the stricter identifiability question:

> If the physical Toy009 hidden source is kept fixed, does a finite relational reference actually restore `F_{beta|theta}` by giving the calibration nonzero information about the old hidden amplitude?

The source state is deliberately **not** redefined together with the calibration observable.

## Hard-constrained setup

Trace and energy are eliminated exactly as in the corrected Iteration-015/026 framework. The detector likelihood uses the corrected D2 two-band response. Parameters are

- `beta`, the detector parameter of interest;
- the fractional amplitude of the fixed Toy009 hidden source direction;
- 22 source nuisances orthogonal to that hidden direction inside the exact trace+energy subspace.

Relational mean and covariance rows are rebuilt consistently with the same finite `y_ref`. Corrected D2 weights are retained:

`gamma_mean = 2.414e6`, `gamma_cov = 0.929e6`.

## Main numerical result

Finite-reference calibration does give nonzero direct Fisher information on the old hidden amplitude. For example:

- `y_ref=-5`: amplitude calibration Fisher `~3.18167`;
- `y_ref=-10`: `~0.671908`;
- `y_ref=-100`: `~2.84860e-4`.

However, after profiling the remaining source nuisances, detector information without independent preparation metrology is still essentially lost:

| `y_ref` | `F_beta|theta` at `C_a=0` | overlap of new exact null with old hidden | detector alignment of new null |
|---:|---:|---:|---:|
| -5 | `8.1742e-5` | `0.9968101` | `0.9999573` |
| -10 | `1.2329e-5` | `0.9992856` | `0.9999936` |
| -20 | `2.2121e-6` | `0.9998904` | `0.9999988` |
| -50 | `1.4057e-7` | `0.9999943` | `0.99999992` |
| -100 | `1.2490e-8` | `0.99999953` | `0.999999993` |

Thus the finite reference breaks the **old** amplitude null, but the calibration operator retains a one-dimensional exact null that rotates into a nearby direction. That new null is even more nearly parallel to the D2 beta detector signal.

## New negative result

**RQIR-NG-012 — relational-null substitution obstruction.**

A finite-reference potential-difference calibration can acquire nonzero Fisher information about a previously hidden source amplitude while leaving the parameter of interest effectively non-identifiable, because the exact calibration null can rotate into another detector-aligned source direction.

Therefore

`I_cal(old amplitude) > 0`

does **not** imply

`F_{beta|theta} > 0`

after profiling the complete nuisance space.

This is the finite-reference analogue of RQIR-NG-010 and is a stronger warning against using one selected source amplitude as a proxy for full source identifiability.

## Preparation/calibration frontier at finite reference

At the current calibration scale `lambda=1`, the independent source-preparation Fisher required for 90% detector-information retention is approximately

- `y_ref=-4`: `C_a*=15.48`;
- `y_ref=-5`: `16.65`;
- `y_ref=-7.5`: `19.36`;
- `y_ref=-10`: `21.92`;
- `y_ref=-20`: `31.59`;
- `y_ref=-50`: `59.67`;
- `y_ref=-100`: `106.20`.

With asymptotically strong source metrology, the calibration multiplier needed for 90% retention rises from about `0.464` at `y_ref=-4` to `0.913` at `y_ref=-100`.

Hence moving the reference outward has two simultaneous costs:

1. Iteration 030: native potential-difference transduction becomes slower, approximately through the `1/L^2` rate suppression after signal saturation;
2. Iteration 031: the relational calibration geometry approaches the original NP3 null geometry, so the source-preparation requirement also grows.

The two effects point in the same resource direction rather than compensating each other.

## Interpretation

This does not disprove relational potential calibration. It shows that a finite reference is not a free cure for RQIR-NG-005. A physically implemented relational branch must still be optimized against independent source metrology, and the full profiled nuisance space—not only the old hidden amplitude—must remain in the Fisher calculation.

No new-physics claim is implied. This is a finite-dimensional Toy009 identifiability/resource result.

## Reproducibility

Code: `analysis/d2_finite_reference_profiled_fisher_iteration031.py`.

## Next gate

Use the finite-reference Fisher frontier together with the heterogeneous native rates from Iteration 030. Optimize actual normalized wall-clock cost over `(y_ref, lambda, C_a)` rather than comparing geometry and transduction separately. The result should determine whether any finite relational-potential reference remains Pareto-competitive with native-force replacement or augmented potential+force calibration before SI apparatus assumptions are inserted.
