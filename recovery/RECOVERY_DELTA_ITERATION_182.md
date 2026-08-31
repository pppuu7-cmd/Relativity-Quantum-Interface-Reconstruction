# Recovery Delta — RQIR Iteration 182

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Previous authoritative front

Iteration 181. Local C5 occupies rank 4/6 in the six-row null-soft `B_T` protocol; compatible massless-spin-2 C4 adds no direction, massive dRGT is protocol-incompatible, and the fixed exponential nonlocal comparator remained blocked. Representative exponential scalar shapes were below the existing `B_T` numerical resolution envelope.

## New result

Before attempting the full `QG-NL-EXP-001` tensor cubic expansion, Iteration 182 audits the definition of the Ward-subtracted observable.

The repository had frozen

`B_T=P_T[Gamma_arr-W[K2]]`

conceptually, but had not implemented an executable source-completed `W[K2]` or explicit numerical `P_T`.

This is harmless for Iterations 177–178 because their curvature-cubic operator directions have `K2_operator=0`, so their operator-specific `W[K2]=0` exactly.

For `QG-NL-EXP-001`, `K2!=0`, so a raw cubic tensor coefficient is not by itself a unique `B_T` coordinate.

## Exact ambiguity certificate

A transverse Riemann-symmetry shift

`W -> W + Rlin:C`,

`B -> B-C`

leaves the raw cubic vertex unchanged while also preserving soft-gauge Ward checks because `Rlin[gauge]=0`.

Numerical certificate:

- pure-gauge soft Riemann norm `1.5700924587e-16`;
- physical TT soft Riemann norm `2.0`;
- nonzero decomposition shift norm `0.2455605832`;
- compensated raw-vertex change `5.5511151231e-17`.

## Retained results

- `SOFT-NG-008 — TRANSVERSE_RIEMANN_SHIFT_IS_INVISIBLE_TO_WARD_CONSTRAINTS_UNTIL_W_K2_CONVENTION_IS_FIXED`;
- `NL-NG-005 — FULL_NONLOCAL_RAW_CUBIC_IS_NECESSARY_BUT_NOT_SUFFICIENT_FOR_B_T_WHEN_K2_IS_NONZERO`;
- `NG-FUNNEL-040 — EXECUTABLE_SOURCE_COMPLETED_WARD_SUBTRACTION_MUST_PRECEDE_NONLOCAL_OR_AS_B_T_RANK_PROMOTION`.

## Classification

`QG-NL-EXP-001 B_T = BLOCKED_EXECUTABLE_SOURCE_COMPLETED_WARD_SUBTRACTION_NOT_YET_FROZEN`.

This is not FAIL, not zero, not exact comparator identity, and not novelty.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

Comparator foundation remains `24/25`. The remaining point requires a common executable relation map and a finite-enough full C3/C4/C5/nonlocal/AS quotient.

## Exact restart instruction

Resume at **Iteration 183 — executable source-completed off-shell Ward projector**.

Required order:

1. derive `W[K2]` for one soft graviton plus two off-shell conserved-TT hard source legs in the fixed physical metric/source convention;
2. define the `O(k_soft^2)` transverse tensor complement/projector `P_T` on the same six frozen rows;
3. validate the full source-completed Ward identity and field/source bookkeeping;
4. validate the projector on EH/local cases with known limits;
5. only then compute the full `QG-NL-EXP-001` cubic tensor including the Frechet term and extract its physical `B_T`;
6. reuse the same executable projector for AS;
7. preserve C3 unsupported ordered/transverse pieces as BLOCKED until explicitly closed.

No `ANSATZ-003`, Fisher or resources before a full fixed comparator-quotient residual survives.
