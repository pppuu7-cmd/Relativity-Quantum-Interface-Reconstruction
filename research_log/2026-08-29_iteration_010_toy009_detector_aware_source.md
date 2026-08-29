# RQIR Research Log — Iteration 010

**Date:** 2026-08-29  
**Topic:** detector-aware source redesign and D1 switch-count reduction  
**Labels:** `DRV`, `NUM`, `NEG`, `OPEN`

## Target

After Iterations 008–009 established detector branches D1/D2 and the D1 control-window bottleneck, test whether the five-level source itself can be redesigned for detector-level Fisher information without sacrificing the finite NP3 calibration properties of Toy 007.

## Step A — low-switch D1 control

The old Toy 007 bounded lock-in used eight sign changes per source period. A direct piecewise-constant search over alternating-sign sequences showed:

- four switches can retain most of the useful two-band response;
- six switches can approach the best eight-switch Fisher value;
- fewer switches reduce cumulative contrast penalties `c^(2 N_sw)`.

This motivated including switch count in the source/detector design vector rather than treating it as an afterthought.

## Step B — detector-only NP2 source scan

Fixed energy spectrum:

`E=(1,2,3,4,6)`.

Scanned 5000 real-symmetric source operators with seed `20260829`, positive Newtonian embedding, `r_max<=6`, and minimum site spacing `>=0.1`.

Best joint D1/D2 NP2 candidate occurs at trial `2641` and gives relative ideal two-band Fisher proxies:

- D1: `x5.36249`;
- D2: `x4.17414`.

However, when the inherited Toy 007 NP3 calibration pattern is imposed:

- `eta_R ~= 0.02990`;
- normalized `s_min ~= 2.61e-4`;
- condition number `~1.75e4`;
- resulting NP3 detector response is below the Toy 007 baseline.

**NEG result:** optimizing source response before calibration can produce a large apparent gain that is projected away by the calibration geometry.

## Step C — NP3-constrained source scan

A second 5000-trial scan with seed `314159` applies the full fixed Toy 007 finite calibration pattern to every candidate before ranking detector response.

Acceptance required both

`eta_R >= eta_R(Toy007)`

and

`s_min >= s_min(Toy007)`.

Only one candidate in the scan satisfies both non-degradation conditions: trial `811`.

Accepted Toy 009 source radii:

`(1.00000, 1.60090, 1.77911, 2.60901, 5.90724)`.

The fixed finite calibration still gives rank `24/25` and one exact null direction.

State eigenvalues remain positive:

- rho+: `(0.12000, 0.17296, 0.19541, 0.24624, 0.26539)`;
- rho-: `(0.13461, 0.15376, 0.20459, 0.22704, 0.28000)`.

Selected equality residuals are below `6e-16`.

At the inherited response time:

- matched mean `~0.547860`;
- matched centered N00 `~0.0132606`;
- `D00+ ~= -0.0120850`;
- `D00- ~= +0.0120850`.

Calibration geometry improves:

- `eta_R ~= 0.568823` versus `0.457682`;
- `s_min ~= 1.5122e-3` versus `1.4629e-3`;
- condition `~3.03e3` versus `~3.18e3`.

Detector-level source information improves:

- D1 two-band `S_eff`: `x1.22184`;
- D2 two-band `S_eff`: `x1.40358`.

This is the first simultaneous Pareto improvement over the Toy 007 NP3 baseline in D1, D2, eta_R and conditioning.

## Step D — Toy 009 D1 low-switch windows

Toy 009 response harmonics:

`H2 ~= -0.00167587 + i 0.00792491`

`H4 ~= +0.00434188 + i 0.00995421`.

Four-switch pi-periodic sensitivity:

- `a ~= 0.912594`;
- `|W2| ~= 0.50363`;
- `|W4| ~= 0.30807`;
- Fisher ratio vs Toy007 eight-switch bounded window: `1.12746`.

Six-switch sensitivity intervals:

`(0.26890, 0.92358, 1.02555, 2.11605, 1.02554, 0.92358)`.

- `|W2| ~= 0.45974`;
- `|W4| ~= 0.36382`;
- Fisher ratio vs Toy007 eight-switch bounded window: `1.23731`.

Thus Toy 009 gives both higher Fisher information and fewer hard switches.

Using the same prior D1 scaling assumptions, illustrative mass-product thresholds become approximately:

- four switch: `7.63e-29 kg^2`, equal-mass `8.73e-15 kg`;
- six switch: `7.28e-29 kg^2`, equal-mass `8.53e-15 kg`.

These remain scaling illustrations only.

For D2, the same optimistic force-noise benchmark rescales from `2.40e-18 kg^2` to approximately `2.03e-18 kg^2`.

## External-method check

Current quantum-sensing literature includes continuous phased dynamical decoupling and heterodyne/lock-in protocols using continuous control and discrete phase changes. Therefore RQIR does not claim time-dependent lock-in sensitivity engineering as new physics. The RQIR-specific point is joint source/calibration/gravity/detector optimization for the ordered-response interface discriminator.

## New design rule

`RQIR-DESIGN-001`: optimize source and inference geometry jointly.

A candidate source is not ranked before applying calibration/null-or-Fisher geometry and the detector transfer. Large pre-calibration response gains can be spurious from the final inference point of view.

## Files

- `docs/TOY_MODEL_009_DETECTOR_AWARE_SOURCE_OPTIMIZATION.md`
- `analysis/toy009_detector_aware_source_search.py`
- `analysis/d1_low_switch_toy009.py`

## Next gate

1. Jointly re-optimize Toy 009 second-probe position and calibration times rather than inheriting Toy 007 settings.
2. Replace the exact eta/s_min guard by detector-covariance profiled Fisher during the search itself.
3. Test continuous/phase-modulated D1 sensitivity against four/six hard-switch protocols under the same bandwidth/contrast budget.
4. Preserve the full relativistic/source+apparatus stress-energy embedding as an open fundamental gate.
