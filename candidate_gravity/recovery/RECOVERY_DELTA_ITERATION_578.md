# Recovery Delta — Iteration 578

**Date:** 2026-09-08  
**MODEL_READINESS:** 24% (unchanged)  
**Authority:** exact tensor11 PRESS/leverage amplification robustness audit; non-promoting

## Incoming authority
Iteration577 was the repository front. Iter424 remains 4 PASS + 1 BLOCKED; the unchanged original Iter421 tensor11 residual is the only blocked clause. Canonical frozen 36-node matrix run `34180521559` remains `in_progress` and was not duplicated.

## New exact result
For the unchanged 16-observation degree-(1,1) tensor11 fit, ordinary least-squares leave-one-out residuals obey exactly

`e_i^(LOO) = e_i/(1-h_ii)`.

Using the exact frozen-design leverages from Iter577:
- `h_min = 529/7396`;
- `h_max = 43681/66564`;
- minimum PRESS amplification = `7396/6867 ~= 1.0770350953837193`;
- maximum PRESS amplification = `66564/22883 ~= 2.9088843246077873`.

Hence no frozen symmetric-cross observation has divergent leave-one-orbit amplification, and the worst leverage-only amplification is strictly below 2.91. This does not authorize deleting any frozen observation/node and does not change the tensor11 observable, fit, precision, radii, or threshold.

Classification:
`PASS_ITER421_TENSOR11_PRESS_LEVERAGE_AMPLIFICATION_AUDIT_EXACT__NON_PROMOTING`

Reproducible artifacts:
- `candidate_gravity/code/iteration578_tensor11_press_leverage_amplification_audit.py`
- `candidate_gravity/results/iteration578_tensor11_press_leverage_amplification_audit.json`

## Retained scientific state
- Iter424: 4 PASS + 1 BLOCKED.
- tensor11: BLOCKED pending complete raw-valid MP support and unchanged original fit.
- physical index2: not promoted.
- exact15: unauthorized.
- comparator quotient: operational BLOCKED; concrete Source/Ward/contact+K2 residual absent.
- `ANSATZ-003`: uncreated.
- Fisher/resources: forbidden.

## Exact next gate
When run `34180521559` becomes terminal, fail-closed consume all 36 rank artifacts. If all are raw-valid PASS, combine with the 28 validated nodes and compute the unchanged original Iter421 tensor11 residual independently at MP80 and MP120. Only tensor11 `<=2e-5` plus the existing four PASS clauses may close Iter424 5/5 and promote physical index2.

MODEL_READINESS: 24%

Readiness change: **0 percentage points**. Iter578 closes a genuine PRESS/design-robustness subgate but no additional model-level rubric point.
