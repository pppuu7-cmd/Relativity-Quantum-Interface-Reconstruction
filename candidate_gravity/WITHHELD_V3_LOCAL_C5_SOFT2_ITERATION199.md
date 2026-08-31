# RQIR Candidate Gravity — Iteration 199

## Local C5 soft2 on the frozen v3 protocol

Using the Iteration-198 frozen v3 polarization seeds, evaluate the exact leading soft2 coefficient of the cyclic `Riemann^3` operator at `(k0,q,-q)` and generate the local zero-K2 dimension-12 basis

`V4 = Riemann3_soft2*{1,-q^2,q^4,-q^6}`.

### Result

On v3:

- rank `4/12`;
- singular values `[15.21154610,1.46670783,0.08703714,0.00314421]`;
- raw condition number `4837.9565`;
- column-normalized condition number `4587.3371`;
- algebraic complement dimension before blocked AS/C3 completion: `8`.

Thus the same local C5 rank survives, but its numerical geometry changes strongly.

### Hard-vs-soft conditioning tradeoff

Relative to withheld-v2:

- v3 hard-K2 raw condition is better by factor `3.2176`;
- v3 hard-K2 column-normalized condition is better by factor `3.0705`;
- v3 local C5 soft2 raw condition is **worse** by factor `4.8399`;
- v3 local C5 soft2 column-normalized condition is **worse** by factor `8.1797`.

Therefore v2 and v3 are not totally ordered. v3 is better for hard K2 separation but worse for the conditional local-C5 soft2 basis.

### Consequence

A future prospective protocol may not optimize only the hard block. The design objective must be frozen on the **full joint quotient geometry**, or at minimum use an explicit multi-objective criterion that treats hard and conditional-soft conditioning separately. No candidate residual may enter that design.

### Retained results

- `C5-NG-017 — WITHHELD_V3_ZERO_K2_LOCAL_C5_SOFT2_SPAN_REMAINS_RANK4`.
- `NUM-NG-013 — HARD_K2_CONDITIONING_IMPROVEMENT_CAN_WORSEN_CONDITIONAL_SOFT2_CONDITIONING`.
- `PROTO-NG-006 — V2_AND_V3_FORM_A_CONDITIONING_TRADEOFF_NOT_A_TOTAL_ORDER`.
- `NG-FUNNEL-053 — PROSPECTIVE_PROTOCOL_DESIGN_MUST_CONTROL_THE_FULL_JOINT_QUOTIENT_NOT_ONE_BLOCK_IN_ISOLATION`.

AS and C3 remain BLOCKED, not zero. No candidate is tested.

`MODEL_READINESS: 24%` — unchanged.
