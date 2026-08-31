# Recovery Delta — RQIR Candidate Gravity Iteration 197

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## New frozen protocol state

`RQIR-WITHHELD-NULLSOFT-12-v3-K2-FROZEN` is frozen before any cubic or candidate evaluation.

Base q-vectors are unchanged. A deterministic two-scale grid was searched using only supported comparator K2 conditioning:

- low scale grid `0.60,0.65,...,0.90`;
- high scale grid `1.10,1.15,...,1.40`;
- internal design window `0.10 <= x=q^2 <= 1.00`;
- objective: minimize column-normalized condition number of `[x,x^2,...,x^6,x^2 exp(x)]`;
- tie-break: minimize raw condition number.

No candidate target, residual, soft2 amplitude or left-null was used.

Selected scales: `0.80` and `1.40`.

Selected x values:

`[0.324864,0.246656,0.27264,0.201792,0.256256,0.184448,0.994896,0.755384,0.83496,0.617988,0.784784,0.564872]`.

All partner legs remain spacelike on the 81-point `epsilon in [-0.01,0.01]` geometry window.

## Conditioning improvement relative to withheld-v2

- raw condition: `2.04935e7 -> 6.36910e6`, improvement factor `3.2176`;
- column-normalized condition: `2.38767e7 -> 7.77614e6`, improvement factor `3.0705`;
- raw smallest singular value: `1.39038e-7 -> 7.87933e-7`, gain factor `5.6670`.

Exact rank remains 7 and is already structurally guaranteed by Iteration 196. Near-degeneracy remains; finite-noise identifiability is not claimed.

## Comparator/candidate status

- C5/nonlocal hard rank: 7, structurally exact for distinct positive x.
- v3 cubic polarization geometry: NOT YET FROZEN.
- AS: BLOCKED, not zero.
- C3: BLOCKED, not zero.
- Candidate residual: not tested.
- `ANSATZ-003`: NOT CREATED.
- Fisher/resources: FORBIDDEN.

## Authority files

- `analysis/withheld_v3_k2_conditioning_design_iteration197.py`
- `results/withheld_v3_k2_conditioning_design_iteration197.json`
- `candidate_gravity/WITHHELD_V3_K2_CONDITIONING_DESIGN_ITERATION197.md`
- `research_log/2026-08-31_iteration_197_withheld_v3_k2_conditioning.md`

## Next gate

Freeze v3 cubic polarization geometry with a uniform target-independent seed acceptance rule before evaluating any cubic comparator or candidate on v3.
