# RQIR Research Log — Iteration 205

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## New protocol

Define normalized timelike discontinuity `D=Disc/(2 pi i)` and the linked multi-point target

`T_cut = D Gamma3_ret,soft - W[D K2]`

in one source-completed convention.

## Structural advantages

1. Any local analytic polynomial/derivative tower has `D=0` inside its analytic domain, so the all-orders local interpolation blocker of Iteration 202 is eliminated by projection rather than truncation.
2. Analytic Ward/transverse repartitions `W->W+C`, `B->B-C` have `D C=0`, so the local decomposition ambiguity of Iteration 182 disappears at cut level.
3. Standalone `D K2` remains non-promotable because Iteration 170 gives exact positive-spectral C4 mediator degeneracy. Novelty must reside in the linked higher-point relation.

A toy validator confirms exact insensitivity to arbitrary local deformations and analytic repartition; it is not a physical gravity-loop calculation.

## Retained results

- `CUT-NG-001`;
- `CUT-NG-002`;
- `NG-FUNNEL-061`.

## Comparator state

- local analytic C5: exact null under D;
- C5 loop cut: required positive control, not yet instantiated;
- C4 nonlinear mediator cut: BLOCKED;
- AS real-time three-graviton cut: BLOCKED;
- C3 ordered cut: BLOCKED.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

## Next gate

Iteration 206: identify and instantiate the strongest available C5 one-loop third-order nonanalytic authority/reproduction route, preserving the distinction between Euclidean/in-out form factors and source-completed retarded/in-in RQIR observables.
