# Recovery Delta — RQIR Candidate Gravity Iteration 198

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## New authority

The Iteration-197 K2 geometry at scales `0.80/1.40` now has a prospectively frozen cubic polarization protocol:

`RQIR-WITHHELD-NULLSOFT-12-v3`.

Uniform geometry-only seed rule:

- hard start `198000+1000*row`;
- partner start `198500+1000*row`;
- hard accept `abs(raw TT norm)>=0.25`;
- partner accept `min abs(raw TT norm)>=0.25` with constant sign on the 81-point `epsilon in [-0.01,0.01]` grid.

All 12 rows pass before any v3 cubic comparator or candidate evaluation.

- minimum hard absolute norm `0.2544562328`;
- minimum partner margin `0.9053777009`.

## Guardrail

The seed freeze is geometry-only. No cubic amplitude, soft2 residual, candidate ansatz or future target may retroactively alter these seeds.

## Candidate/comparator state

- v3 cubic C5 evaluation is now authorized.
- AS: BLOCKED, not zero.
- C3: BLOCKED, not zero.
- Candidate residual: not tested.
- `ANSATZ-003`: NOT CREATED.
- Fisher/resources: FORBIDDEN.

## Authority files

- `analysis/preregistered_withheld_v3_polarization_iteration198.py`
- `results/preregistered_withheld_v3_polarization_iteration198.json`
- `candidate_gravity/WITHHELD_V3_POLARIZATION_FREEZE_ITERATION198.md`
- `research_log/2026-08-31_iteration_198_v3_polarization_freeze.md`

## Next gate

Evaluate zero-K2 local C5 soft2 on the frozen v3 geometry and compare joint hard/soft conditioning with v2.
