# Recovery Delta — RQIR Candidate Gravity Iteration 199

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## New authority

On the prospectively frozen `RQIR-WITHHELD-NULLSOFT-12-v3` geometry, the zero-K2 local C5 curvature-cubic soft2 basis

`V4=Riemann3_soft2*{1,-q^2,q^4,-q^6}`

has:

- rank `4/12`;
- singular values `[15.21154610,1.46670783,0.08703714,0.00314421]`;
- raw condition number `4837.9565`;
- column-normalized condition number `4587.3371`;
- algebraic complement dimension `8` before blocked AS/C3 completion.

The exact leading coefficient is obtained from the trilinear linearized-Riemann contraction at `(k0,q,-q)`; no soft extrapolation is used.

## Conditioning tradeoff

Relative to v2:

- hard K2 raw condition improves by factor `3.2176`;
- hard K2 column-normalized condition improves by factor `3.0705`;
- conditional local-C5 soft2 raw condition worsens by factor `4.8399`;
- conditional local-C5 soft2 column-normalized condition worsens by factor `8.1797`.

Therefore v2 and v3 are not totally ordered. v3 is better for hard calibration but worse for conditional soft2 geometry.

## Guardrail

Future row design may not optimize only one block. Freeze a target-independent multi-objective/joint conditioning criterion before creating another prospective protocol. Candidate residuals must not enter that criterion.

## Comparator/candidate state

- C5 local soft2: rank 4 on both v2 and v3.
- Nonlocal hard tangent: exact-independent structurally; exact hard calibration removes it.
- AS: BLOCKED, not zero.
- C3: BLOCKED, not zero.
- Candidate residual: not tested.
- `ANSATZ-003`: NOT CREATED.
- Fisher/resources: FORBIDDEN.

## Authority files

- `analysis/withheld_v3_local_c5_soft2_iteration199.py`
- `results/withheld_v3_local_c5_soft2_iteration199.json`
- `candidate_gravity/WITHHELD_V3_LOCAL_C5_SOFT2_ITERATION199.md`
- `research_log/2026-08-31_iteration_199_v3_local_c5_soft2.md`

## Next gate

Freeze a candidate-independent joint/multi-objective conditioning criterion for the supported `(K2,S_soft2)` quotient and only then design or compare further prospective row sets.
