# RQIR Research Log — Iteration 218

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Starting point

Iteration 217 established that the on-shell graviton S-matrix restriction is non-invertible for the off-shell/source-completed nonanalytic cubic cut. A physical source model is therefore required.

## Frozen source model

`MSSC-001`:

`S_phi = -1/2 int sqrt(-g) [ g^{mu nu} partial_mu phi partial_nu phi + m^2 phi^2 ]`.

The one-graviton scalar vertex obeys

`k_mu V^{mu nu}=(p'^2-m^2)p^nu-(p^2-m^2)p'^nu`.

Numerical audit:

- max off-shell identity error `4.44e-16`;
- on-shell source transversality error `1.14e-16`.

## Same-dynamics nonlinear rule

All `h^n phi^2` source/contact vertices are fixed by this same covariant action. Independent tuning of the nonlinear source completion is forbidden.

At two-graviton order, do not test the `hh phi phi` contact alone. Gauge invariance belongs to the **full scalar + two-graviton tree amplitude**, which combines the source contacts/exchange structures dictated by the same gravity+matter dynamics.

## Authority route

The known two-massive-scalar/multi-graviton tree amplitudes provide a compact amplitude-level implementation route using scalar-gluon amplitudes and KLT. This avoids treating individually gauge-dependent diagram pieces as separate observables.

## Retained

- `SRC-NG-001`;
- `SRC-NG-002`;
- `NG-FUNNEL-075`.

## Readiness

`MODEL_READINESS: 23%` — unchanged.

## Next gate

Iteration 219: instantiate the full gauge-invariant `2 scalar + 2 graviton` tree amplitude from the published KLT construction, verify both graviton Ward tests and graviton-exchange symmetry, and freeze it as the first nonlinear dynamical-source building block for a physical source unitarity cut.
