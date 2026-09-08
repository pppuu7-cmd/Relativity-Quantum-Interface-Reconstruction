# Recovery Delta — Iteration 577

**Date:** 2026-09-08  
**MODEL_READINESS:** 24% (unchanged)  
**Authority:** exact tensor11 leverage/single-orbit design robustness audit; non-promoting

## Incoming authority
Iteration576 was the repository front. Iter424 remains 4 PASS + 1 BLOCKED; the unchanged original Iter421 tensor11 residual is the only blocked clause. Canonical frozen 36-node matrix run `34180521559` remains `in_progress` and was not duplicated.

## New exact result
The frozen 16x4 degree-(1,1) design factorizes from the one-axis 4x2 matrix with squared radius coordinates `{1,9/16,1/4,1/16}` and basis `[1,x]`. Therefore the 2D hat matrix is the tensor product of the one-axis hat matrix with itself.

Exact one-axis leverages:
- `209/258`
- `23/86`
- `89/258`
- `149/258`.

For the 16 tensor11 symmetric-cross observations:
- leverage sum = `4` exactly;
- minimum leverage = `529/7396 ~= 0.07152514872904273`;
- maximum leverage = `43681/66564 ~= 0.6562255874046031 < 1`;
- minimum diagonal residual-projector weight = `22883/66564 ~= 0.3437744125953969 > 0`.

Therefore every frozen `C(r,s)` observation has nonzero residual sensitivity. No orbit is a unit-leverage interpolation point, and deletion of any one observation preserves design rank 4. This does not authorize deleting any frozen orbit/node; all 64 signed F nodes remain mandatory.

Classification:
`PASS_ITER421_TENSOR11_LEVERAGE_SINGLE_ORBIT_ROBUSTNESS_AUDIT_EXACT__NON_PROMOTING`

Reproducible artifacts:
- `candidate_gravity/code/iteration577_tensor11_leverage_robustness_audit.py`
- `candidate_gravity/results/iteration577_tensor11_leverage_robustness_audit.json`

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

Readiness change: **0 percentage points**. Iter577 closes a genuine design-robustness subgate but no additional model-level rubric point.
