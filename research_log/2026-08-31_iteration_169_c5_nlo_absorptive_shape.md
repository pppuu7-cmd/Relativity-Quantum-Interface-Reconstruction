# RQIR Research Log — Iteration 169

**Date:** 2026-08-31  
**Branch:** Candidate Gravity / timelike absorptive shape funnel  
**MODEL_READINESS: 24%**

## Starting point

Iteration 168 established that the complete leading one-massless-loop curvature-squared C5 TT absorptive response is one-dimensional constant shape and is removed by the Iteration-167 quotient.

## Question

What shape freedom is already authorized by standard gravitational EFT at the next order before any Candidate Gravity residual is considered?

## EFT-order freeze

Use gravitational power counting

`P = 2 + 2L + sum_v(d_v-2)`.

At `O(p^6)` the relevant classes are:

- tree six-derivative local terms;
- one loop with one four-derivative insertion;
- two-loop EH.

Tree local terms are absorptively zero off pole.

For the one-scale massless two-point sector, a conservative renormalized two-loop envelope contains retarded logarithms through degree two. After two EH propagators and the frequency-odd imaginary projection, the entire next-order shape envelope is contained in

`span{s, s log(s/mu^2)}`.

Scale changes only mix these directions.

## Numerical finite quotient

Use the eight pre-frozen rows `s_i=0.004 i`, `i=1..8`, and `x=s/s_max`.

Profile basis:

`[1, x, x log x]`.

Certificate:

- rank `3`;
- singular values `[3.3352971464,0.7871654345,0.1823010356]`;
- condition number `18.2955469`;
- profile orthogonality error `1.67e-16`;
- residual shape dimension `5`.

Higher-order capacity test `[x^2,x^2 log x,x^2 log^2 x]` survives with rank `3/3`.

## Retained results

- `C5-NG-006 — NEXT_ORDER_P6_MASSLESS_TT_ABSORPTIVE_ENVELOPE_IS_SPAN_X_XLOGX`;
- `ABS-SHAPE-004 — PROFILING_CONSTANT_X_XLOGX_LEAVES_FIVE_TIMELIKE_SHAPE_DIMENSIONS`;
- `NG-FUNNEL-029 — ORDER_BY_ORDER_LOOP_SHAPE_ENVELOPES_MUST_BE_PROFILED_BEFORE_CANDIDATE_RESIDUAL`.

## AS data audit

Search of the public 2026 Pawlowski–Reichert–Wessely spectral-function publication and related pages found the flow equations, iteration strategy and numerical quadrature tolerances, but no public precision spectral table or production code sufficient to build an authoritative eight-row finite-frequency comparator column.

Do not digitize the plot and call it exact data.

Status remains:

`AS finite-frequency = BLOCKED_NUMERICAL_SPECTRAL_DATA_OR_CONTROLLED_REPRODUCTION`.

## Readiness

`MODEL_READINESS: 24%` — unchanged from Iteration 168.

Reason: the NLO C5 comparator uncertainty is now finite and structured, but the last comparator-foundation point remains blocked by finite-frequency AS and threshold/loop alternatives. Robust Candidate Gravity residual remains `0/20`.

## Next gate

Iteration 170 should prioritize a theorem-level threshold audit of the frozen timelike window and/or a controlled reproduction path for `AS-LOR-SPEC-002` finite-frequency spectral data. Only after the known comparator occupancy of the five-dimensional NLO-null shape space is bounded should any candidate direction be proposed.
