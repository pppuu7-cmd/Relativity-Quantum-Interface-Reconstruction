# RQIR Research Log — Iteration 075

**Date:** 2026-08-30

## Question

Does Toy014's improved physical local-source Pareto vector survive source-specific timing/geometry/additive nuisance revalidation inside the spectral-tilt-profiled D2 likelihood?

## Result

Yes with explicit independent controls, but the mature low-rank control degeneracy remains fully active.

Using Toy014's own physical calibration optimum (`gamma_mean~5.677685e6`, `gamma_cov~2.718674e6`), four calibration systematics were added: `delta y1`, common timing/phase shift, additive mean offset, additive centered-covariance offset. The 22 source nuisances and detector spectral tilt were profiled simultaneously.

With no control priors, `F_beta|theta` remains numerically zero even at `100x` calibration exposure. Thus RQIR-NG-006 survives Toy014 and the physical detector-metric correction.

A conservative 10% control bundle gives

- `sigma(delta y1)=0.74131718`;
- `sigma(delta tau)=0.00249891877`;
- `sigma(b_mean)=4.19676208e-5`;
- `sigma(b_cov)=6.06486956e-5`.

At 100 Hz this means

`boxed: sigma_t ~= 3.97715 us`.

With the bundle, final profiled Fisher returns to `0.8999686`.

New retained rule **RQIR-CAL-020 — Toy014 control bundle is source-specific**: timing/geometry/additive tolerances must be rebuilt after source co-design in the same physical detector metric; they cannot be copied from Toy009/Toy012.

Toy014 maximum stored evolution interval at 100 Hz is `~6.81327 ms`, shorter than Toy009's `~7.943 ms` reference. Under the transparent 10-us event-jitter / p=.5 / 1-ms overhead benchmark, one timing-reference block is `~0.889 s`, but drift recertification can dominate: illustrative cadence is `~16.9 min` for `D=100 us^2/h` and `~1.69 min` for `D=1000 us^2/h`.

## Next

Add `T_ctrl` explicitly to the Iteration-071 general wall-clock closure and derive a control-aware Toy014-vs-Toy009/Toy013 surface. Keep detector PSD/transduction and drift parameters explicit rather than converting the reference benchmarks into apparatus claims.
