# Recovery Delta — RQIR Candidate Gravity Iteration 200

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Concurrency reconciliation

Two independent research paths froze different deterministic TT polarization streams on the same v3 hard q geometry before their own cubic C5 evaluations:

- `v3-A`: hourly automation, seed rule based at 197000/197500;
- `v3-B`: concurrent manual continuation, seed rule based at 198000/198500.

Both satisfy the same geometry-only acceptance class and neither used a candidate target. Preserve both. Do not select one post hoc and do not overwrite either result.

## C5 comparison

Both local zero-K2 C5 soft2 maps have rank `4/12`.

- v3-A raw condition `1038.3957`, column-normalized `981.3573`.
- v3-B raw condition `4837.9565`, column-normalized `4587.3371`.

Principal angles between the two rank-4 column spaces:

`[1.307416°, 70.597675°, 76.740447°, 83.658828°]`.

Projector distances:

- Frobenius `2.37712349`;
- operator norm `0.993881845`.

The union of alternate subspaces has rank 8 in the common 12-row index representation. This is a protocol-sensitivity diagnostic, **not** eight independent C5 theory parameters.

If both settings are stacked as 24 measured rows with the same four coefficients, the map remains rank 4; diagnostic raw condition `1845.83`, column-normalized `1749.72`. This stacked protocol is not frozen here.

## Interpretation guardrail

TT polarization setting is part of the observable row definition. The deterministic seed only makes that setting reproducible. Different accepted seeds need not produce the same C5 nuisance subspace.

Future candidate claims may not choose whichever branch gives a better residual after seeing the target. A polarization-robust candidate must survive separately frozen protocols (at least v3-A and v3-B) or a new multi-polarization protocol frozen before candidate construction.

## Comparator/candidate state

- C5: rank 4 in both v3-A and v3-B, with strongly rotated nuisance images.
- Nonlocal hard separation: structural rank 7 still applies; hard q nodes are identical across A/B.
- AS: BLOCKED, not zero.
- C3: BLOCKED, not zero.
- Candidate residual: not tested.
- `ANSATZ-003`: NOT CREATED.
- Fisher/resources: FORBIDDEN.

## Authority files

- `analysis/v3_polarization_branch_reconciliation_iteration200.py`
- `results/v3_polarization_branch_reconciliation_iteration200.json`
- `candidate_gravity/V3_POLARIZATION_BRANCH_RECONCILIATION_ITERATION200.md`
- `research_log/2026-08-31_iteration_200_v3_polarization_reconciliation.md`

## Next gate

Freeze a multi-protocol polarization-robustness acceptance rule before any candidate target is instantiated. Do not horizontally merge alternate protocol subspaces as independent theory parameters.
