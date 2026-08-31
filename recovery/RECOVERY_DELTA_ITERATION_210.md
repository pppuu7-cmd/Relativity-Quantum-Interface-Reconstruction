# Recovery Delta — RQIR Iteration 210

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Previous front

Iteration 209 established that the 4D one-loop soft sector is polyhomogeneous and requires explicit regular + log-soft coordinates rather than a pure-Taylor `soft2` coefficient.

## New authoritative result

The one-loop basis through `n=2`

`[1, L, z, zL, z^2, z^2L]`

has been implemented and validated on a target-independent 12-point geometric soft grid with dynamic range 128.

Numerical certificate:

- shape `12x6`;
- rank `6/6`;
- condition number `4264.620104188085`;
- exact synthetic regular+log coefficient recovery relative error `1.2766e-14`;
- exact synthetic fit relative residual `4.1873e-16`;
- equal-parameter-count pure-Taylor degree-five fit leaves relative residual `0.01905923234` (~1.91%).

Deterministic perturbation audit shows approximately `10^3` amplification from relative input perturbation to coefficient error on the chosen direction (`1e-8 -> 1.02e-5`, `1e-6 -> 1.02e-3`). This is protocol conditioning, not Fisher analysis.

## Classification

- regular+log soft basis: `PASS_SCOPED_NUMERICAL_PROTOCOL`;
- pure-Taylor replacement: `FAIL_TO_REPRESENT_LOG_CONTROL` on the frozen grid;
- physical C5 loop import: still open;
- candidate residual: none.

## Retained results

- `NUM-NG-015 — TWELVE_POINT_DYNAMIC_RANGE_128_GRID_RESOLVES_THE_SIX_COLUMN_ONE_LOOP_REGULAR_PLUS_LOG_SOFT_BASIS`;
- `SOFT-NG-007 — PURE_TAYLOR_BASIS_WITH_EQUAL_PARAMETER_COUNT_LEAVES_PERCENT_LEVEL_RESIDUAL_ON_A_LOG_SOFT_CONTROL`;
- `NUM-NG-016 — LOG_SOFT_COEFFICIENT_EXTRACTION_HAS_NONTRIVIAL_CONDITIONING_AND_REQUIRES_A_DECLARED_NUMERICAL_ERROR_ENVELOPE`;
- `NG-FUNNEL-067 — LOOP_SOFT_PROTOCOL_MUST_VALIDATE_REGULAR_LOG_SEPARATION_BEFORE_PHYSICAL_COMPARATOR_IMPORT`.

## Readiness

`MODEL_READINESS: 23%`, unchanged. The numerical protocol is ready, but no physical comparator block or Candidate Gravity residual has closed.

## Exact restart instruction

Resume at **Iteration 211 — first physical regular+log cut control**.

Import one fixed standard-QG nonanalytic expression into the finite-epsilon extractor. Preferred options, in order:

1. an explicitly IR-subtracted/hard on-shell pure-Einstein four-graviton control whose soft/log content can be evaluated without regulator ambiguity;
2. an inclusive IR-safe graviton-scattering observable mapped to the same finite-epsilon convention;
3. if neither is executable without additional convention work, freeze the required subtraction/inclusive definition and classify the physical import as BLOCKED rather than fabricating a coefficient.

Do not replace the off-shell/source-completed `T_cut` by the S-matrix anchor. Do not create `ANSATZ-003`. Fisher/resources remain forbidden.
