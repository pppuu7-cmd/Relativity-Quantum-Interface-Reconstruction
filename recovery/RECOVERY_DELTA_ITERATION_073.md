# RQIR Recovery Delta — Iteration 073

**Date:** 2026-08-30

## Current front

Iteration 072 removed balanced Toy012 from the physical shared-kernel D2 Pareto front. Iteration 073 compares the remaining nearest-neighbour local source branches on corrected physical resource axes.

## Retained local-source vectors

Reference factors relative to Toy009:

- Toy011-response: science `~6.418`, physical calibration `~21.7`, Ramsey source time `~3.759`;
- Toy011-conditioning: `~12.250`, `~8.83`, `~2.384`;
- Toy012-high: `~8237.33`, `~520`, `~0.869`;
- Toy013 trial 29100: `23.6496`, `0.123301`, `330.907`.

Toy011/Toy012 calibration factors are finite-scan central values from Iteration 063; do not treat last digits as apparatus constants.

## New retained rule

**RQIR-DESIGN-008 — locality-constrained Pareto plurality.**

For the local-only weighted objective

`L_i(x,y)=q_s,i+q_c,i x+q_p,i y`, `x,y>=0`,

all four retained local branches attain the lower envelope in some region:

- Toy011-response at `(0,0)`;
- Toy011-conditioning at `(0.7,0)`;
- Toy013 at `(2,0)`;
- Toy012-high at `(0,6000)`.

Thus there is currently no single physically justified nearest-neighbour local baseline independent of apparatus resource weights.

If Toy009 is allowed, both Toy011 points are componentwise dominated by Toy009. Toy012-high and Toy013 remain conditional specialization branches because they respectively improve Ramsey source metrology and physical calibration.

Central reference crossovers:

- `y=0`: response -> conditioning near `x~0.453`; conditioning -> Toy013 near `x~1.309`;
- `x=0`: response -> conditioning near `y~4.24`; conditioning -> Toy012-high near `y~5.43e3`.

## Reproduce

`python analysis/local_source_physical_pareto_iteration073.py`

Primary note:

`docs/LOCAL_SOURCE_PHYSICAL_PARETO_ITERATION073.md`

## Next admissible gate

Toy014 physical multi-resource co-design. Search the exact nearest-neighbour source manifold while simultaneously protecting:

1. noncollapsed physical D2 `n=2/n=4` information;
2. spectral-tilt-profiled calibration geometry;
3. independent energy/Ramsey source-metrology accessibility.

The aim is to Pareto-dominate at least one current Toy011 local point while avoiding Toy013's source-metrology collapse and Toy012-high's science collapse. Do not record a winner before deterministic execution.
