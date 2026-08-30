# RQIR Research Log — Iteration 073

**Date:** 2026-08-30

## Question

After balanced Toy012 is physically demoted, does one remaining nearest-neighbour local source dominate the others on the corrected D2 resource axes?

## Result

No. Using physical two-band science-time factors, Iteration-063 spectral-tilt-profiled calibration factors, and zero-reset Ramsey source-metrology time factors, the retained local-source vectors are approximately:

- Toy011-response: `(q_s,q_c,q_p)=(6.418,21.7,3.759)`;
- Toy011-conditioning: `(12.250,8.83,2.384)`;
- Toy012-high: `(8237.33,520,0.869)`;
- Toy013-29100: `(23.650,0.1233,330.907)`.

If Toy009 is allowed, both Toy011 points are componentwise dominated by it. Under mandatory exact nearest-neighbour locality, however, Toy009 is excluded and all four local points are supported on the weighted lower envelope

`L_i=q_s+q_c x+q_p y`.

Witnesses:

- `(x,y)=(0,0)` -> Toy011-response;
- `(0.7,0)` -> Toy011-conditioning;
- `(2,0)` -> Toy013;
- `(0,6000)` -> Toy012-high.

New retained rule **RQIR-DESIGN-008 — locality-constrained Pareto plurality**: after physical detector profiling, several local sources may be genuinely optimal in different resource regimes. A single local “baseline” should not be promoted before science/calibration/source-metrology rate weights are supplied by the experiment.

Central reference axis crossovers are roughly

- at `y=0`: response -> conditioning at `x~0.453`, conditioning -> Toy013 at `x~1.309`;
- at `x=0`: response -> conditioning at `y~4.24`, conditioning -> Toy012-high at `y~5.43e3`.

These are reference geometry only because the Toy011/Toy012 calibration ratios come from finite scans and NG-029 allows source-dependent transfer/PSD/scheduling changes.

## Next

Define and execute Toy014: a physical multi-resource nearest-neighbour co-design intended to collapse the current Pareto spread. Preserve both D2 bands and a usable Ramsey/energy source-metrology channel at the cheap stage; use spectral-tilt-profiled centered calibration Fisher at the expensive stage. Do not claim a winner before deterministic execution.
