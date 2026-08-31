# Recovery Delta — RQIR Iteration 169

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Previous front

Iteration 168 proved that the complete leading one-massless-loop curvature-squared C5 TT absorptive sector is a one-dimensional constant shape removed by the Iteration-167 constant quotient.

## New scientific result

Gravity EFT power counting freezes the next absorptive order `O(p^6)` to contributions from:

1. tree six-derivative local operators;
2. one-loop diagrams with one four-derivative insertion;
3. two-loop EH diagrams.

The tree local sector is off-pole absorptively zero.

For the frozen one-scale massless timelike two-point problem, use a conservative renormalized log envelope through degree two. After two EH propagators and the frequency-odd imaginary projection, the next-order C5 shape family is contained in

`span{s, s log(s/mu^2)}`.

With `x=s/s_max`, combine this with the already-profiled leading constant direction:

`B=[1,x,x log x]`.

On the eight frozen rows:

- rank `3`;
- condition number `18.2955469`;
- residual shape dimension `5`;
- maximum orthogonality error `1.67e-16`.

A target-independent NNLO-style capacity family `[x^2,x^2 log x,x^2 log^2 x]` retains rank `3/3` in the remainder.

## Retained results

- `C5-NG-006 — NEXT_ORDER_P6_MASSLESS_TT_ABSORPTIVE_ENVELOPE_IS_SPAN_X_XLOGX`;
- `ABS-SHAPE-004 — PROFILING_CONSTANT_X_XLOGX_LEAVES_FIVE_TIMELIKE_SHAPE_DIMENSIONS`;
- `NG-FUNNEL-029 — ORDER_BY_ORDER_LOOP_SHAPE_ENVELOPES_MUST_BE_PROFILED_BEFORE_CANDIDATE_RESIDUAL`.

## Comparator boundary

The five-dimensional remainder is not a Candidate Gravity residual. Still BLOCKED, never zero-filled:

- finite-frequency Lorentzian AS spectral column;
- massive/hidden thresholds;
- C3 diffusion/MSR loop absorptive response;
- C4 loop/helicity thresholds;
- nonlocal Lorentzian CTP loops;
- `O(p^8)` and higher C5 shapes.

Public-source audit of the Pawlowski–Reichert–Wessely spectral calculation found equations, numerical method and tolerances, but no authoritative precision spectral data/code sufficient for a finite-frequency eight-row column. Plot digitization is forbidden as a promotion-quality comparator.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

Comparator foundation remains `24/25`; robust unique residual remains `0/20`; parent dynamics, candidate consistency, Fisher and resources remain zero.

## Exact restart instruction

Resume at **Iteration 170**.

Priority:

1. audit all physical thresholds that can enter the frozen `s in [0.004,0.032] M_Pl^2` timelike window for fixed C3/C4/C5/nonlocal comparator content;
2. distinguish known effectively massless thresholds from genuinely unknown C4/hidden-mediator freedom;
3. if threshold families can be bounded away or mapped into a finite shape envelope, add them to the five-dimensional quotient;
4. in parallel investigate a controlled reproduction route for the published Lorentzian AS spectral flow rather than visual digitization;
5. do not create `ANSATZ-003` until a nonzero residual survives these steps.
