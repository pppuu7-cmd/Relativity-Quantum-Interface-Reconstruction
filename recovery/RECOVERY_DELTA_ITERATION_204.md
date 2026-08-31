# Recovery Delta — RQIR Iteration 204

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## New result

A target-independent low-energy K2 design with `x_max=0.1` demonstrates a structural tradeoff.

### EFT side

If an explicit coefficient envelope `|c_n|<=C` is declared, the dimension-12 cubic derivative remainder can be bounded by `7.4074e-5 C` on the selected nodes. A K2 polynomial tail beyond x^6 is bounded by `1.1111e-7 C`.

No value of C is assumed by RQIR; without a declared envelope there is no model-independent remainder bound.

### Distinguishability side

The analytic nonlocal tangent `x^2 exp(x)` becomes extremely near-degenerate with local `[x,...,x^6]`:

- raw condition `5.55e12`;
- normalized condition `8.95e11`;
- relative local-fit residual `3.90e-12`.

Thus deep IR controls higher powers only conditionally while destroying useful analytic shape separation.

## Retained results

- `EFT-NG-001 — DEEP_IR_IMPROVES_DERIVATIVE_REMAINDER_CONTROL_ONLY_AFTER_AN_EXPLICIT_WILSON_ENVELOPE_IS_DECLARED`;
- `REL-NG-017 — DEEP_IR_ANALYTIC_NONLOCAL_TANGENT_BECOMES_EXTREMELY_NEAR_DEGENERATE_WITH_LOCAL_C5_POLYNOMIALS`;
- `NG-FUNNEL-059 — HIGH_ENERGY_ANALYTIC_DISTINGUISHABILITY_AND_LOW_ENERGY_EFT_TRUNCATION_CONTROL_FORM_A_TRADEOFF`;
- `NG-FUNNEL-060 — PRIORITIZE_LINKED_NONANALYTIC_MULTIPOINT_RELATIONS_OVER_FINITE_ANALYTIC_SHAPE_SEARCH`.

## Readiness

`MODEL_READINESS: 23%` — unchanged.

## Exact restart instruction

Resume at **Iteration 205**.

Freeze a linked nonanalytic multi-point RQIR observable:

1. condition/amputate on the same measured two-point CTP kernel;
2. define a timelike discontinuity of a source-completed retarded three-point/second-order response coordinate;
3. local analytic EFT directions must be exact zero under the discontinuity map;
4. do not treat nonzero two-point spectral density as novelty because of the Iteration-170 C4 direct-integral no-go;
5. require a relation tying the three-point discontinuity to the same two-point spectrum/couplings/soft-Ward data;
6. instantiate C5 loop positive control and keep C4/C3/AS/nonlocal loop entries BLOCKED until physically derived.

No ANSATZ-003, Fisher or resources.
