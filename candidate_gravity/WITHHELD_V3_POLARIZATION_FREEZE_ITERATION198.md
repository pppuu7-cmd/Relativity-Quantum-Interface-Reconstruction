# RQIR Candidate Gravity — Iteration 198

## Prospective v3 cubic polarization freeze

Parent hard kinematics: `RQIR-WITHHELD-NULLSOFT-12-v3-K2-FROZEN`, scales `0.80` and `1.40`.

Before any v3 cubic comparator or candidate calculation, apply one geometry-only rule to all 12 rows:

- deterministic hard seed start `198000+1000*row`;
- deterministic partner seed start `198500+1000*row`;
- scan seeds upward by one;
- hard accept if `abs(raw TT norm)>=0.25`;
- partner accept if `min abs(raw TT norm)>=0.25` and its sign is constant on the 81-point `epsilon in [-0.01,0.01]` grid.

All 12 rows pass.

- minimum hard absolute raw norm: `0.2544562328`;
- minimum partner margin: `0.9053777009`.

No soft2 amplitude, comparator cubic output, candidate residual or future ansatz was used to choose seeds.

### Retained results

- `PROTO-NG-005 — V3_GEOMETRY_ONLY_DENSE_GRID_POLARIZATION_ACCEPTANCE_FROZEN_BEFORE_CUBIC_EVALUATION`.
- `NUM-NG-012 — ALL_12_V3_ROWS_PASS_WITH_MIN_PARTNER_TT_NORM_MARGIN_ABOVE_0P90`.
- `NG-FUNNEL-052 — CONDITIONING_DESIGNED_ROWS_REQUIRE_INDEPENDENT_PROSPECTIVE_POLARIZATION_FREEZE_BEFORE_CUBIC_USE`.

`MODEL_READINESS: 24%` — unchanged.
