# Recovery Delta — RQIR Candidate Gravity Iteration 201

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Frozen cross-polarization candidate gate

Preserve `v3-A` and `v3-B` as separate prospectively frozen validation protocols on the same hard q geometry.

A future candidate must use one parent dynamics and one candidate parameter convention to generate both protocol-specific tangents `b_A` and `b_B`.

For each protocol separately:

1. build only the physically authorized comparator/nuisance map in that protocol's row coordinates;
2. impose exact hard constraints before any profiling/Fisher step;
3. compute the supported algebraic quotient residual;
4. require the residual to be nonzero above the declared numerical/model error envelope.

Both A and B must pass. Passing only one is classified `POLARIZATION_SPECIFIC_IDENTIFICATION_INSUFFICIENT_FOR_PROMOTION`.

Do not fit independent candidate parameters to A and B merely to force a pass. Do not choose, reseed, reweight or drop a polarization protocol after candidate residuals are known.

A future 24-row dual-setting protocol may be an additional validation layer but may not substitute for the separately frozen A/B pass rule unless a replacement protocol is prospectively versioned before candidate construction.

## Comparator/candidate state

- C5: rank-4 local nuisance in each frozen polarization protocol; images strongly rotated.
- Nonlocal hard separation: structurally rank 7 on the frozen hard family.
- AS: BLOCKED, not zero.
- C3: BLOCKED, not zero.
- Candidate residual: NOT TESTED.
- `ANSATZ-003`: NOT CREATED.
- Fisher/resources: FORBIDDEN.

## Authority files

- `candidate_gravity/CROSS_POLARIZATION_ROBUSTNESS_GATE_ITERATION201.md`
- `research_log/2026-08-31_iteration_201_cross_polarization_gate.md`

## Next gate

Return to comparator-foundation closure: continue fixed AS/C3 authority/derivation audits independently. If exact rows remain unavailable, investigate only scientifically derived bounded comparator relations; do not reintroduce broad class masks or zero-fill missing coordinates.
