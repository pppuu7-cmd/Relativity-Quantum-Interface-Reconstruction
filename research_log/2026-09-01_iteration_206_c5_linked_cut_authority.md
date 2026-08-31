# RQIR Research Log — Iteration 206

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Starting point

Iteration 205 froze `T_cut = D Gamma3_ret,soft - W[D K2]`, which exactly eliminates local analytic EFT towers but requires quantum-loop comparator cuts.

## Authority audit

The C5 positive control is not blocked by absence of generic third-order one-loop technology:

- covariant perturbation theory exists through curvature-cubed order;
- all generic third-order nonlocal form factors and spectral representations are available;
- a controlled Euclidean-to-Lorentzian in-vacuum/retarded continuation principle exists for expectation-value equations.

## Gauge/parametrization guardrail

Ordinary off-shell quantum-GR effective action depends strongly on gauge fixing and metric parametrization. The Vilkovisky–DeWitt unique effective action provides the gauge/parametrization-safe route; alternatively the final RQIR observable must be explicitly gauge-invariant/source-completed before comparison.

Therefore no arbitrary background-gauge cubic effective vertex can be inserted as a physical C5 RQIR column.

## Remaining implementation chain

1. pure Einstein graviton Hessian + FP ghost specialization;
2. gauge/parametrization-safe unique or explicitly physical source projection;
3. actual 4D nonlocal third-order form-factor combination;
4. causal in-vacuum continuation;
5. timelike discontinuity and executable Ward link to the same K2.

## Retained results

- `C5-CUT-001` generic third-order nonlocal/spectral formalism supported;
- `C5-CUT-002` causal in-vacuum continuation principle supported;
- `C5-CUT-003` gauge-safe off-shell projection required;
- `NG-FUNNEL-062` blocker narrowed to pure-gravity graviton+ghost specialization plus gauge-safe source-completed RQIR projection.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

## Next gate

Iteration 207: freeze the gauge-safe pure-gravity specialization route and reduce the third-order invariant set using the null-soft TT protocol before any heavy symbolic calculation.
