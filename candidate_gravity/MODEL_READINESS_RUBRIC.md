# Candidate Gravity Model Readiness Rubric

**Frozen:** 2026-08-31, introduced at Iteration 158  
**Purpose:** keep the user-facing model-readiness percentage stable across research iterations.

This score measures readiness of the **Candidate Gravity model itself**, not readiness of the RQIR infrastructure or Papers I–III.

## Fixed 100-point rubric

| Block | Weight |
|---|---:|
| Fixed comparator foundation (C3/C4/C5/nonlocal/asymptotic-safety + nuisance/common-boundary quotient) | 25% |
| Robust unique residual discovery | 20% |
| Frozen parent dynamics / promotable ANSATZ | 20% |
| Candidate consistency: positivity, ghosts, causality, Ward/soft, required limits | 15% |
| Operational identifiability / Fisher after hard constraints | 10% |
| Resource / experiment closure | 10% |
| **Total** | **100%** |

## Scoring rules

1. Do not increase readiness merely because more calculations or files were produced.
2. Increase only when a weighted block is materially closed or narrowed.
3. A new blocker may leave the score unchanged or reduce it.
4. Comparator consistency work counts only under comparator foundation; it does not count as candidate consistency.
5. Scoped residuals from known comparators do not count as a Candidate Gravity residual.
6. `ANSATZ-003` remains 0/20 until a parent dynamics is frozen after a robust residual target survives the fixed comparator quotient.
7. Fisher/resources remain 0 until the algebraic residual gate is passed.

## Formal baseline

### Iteration 157 — `MODEL_READINESS: 20%`

- comparator foundation: **17/25** — concrete scoped C3, nonlinear dRGT C4, local nonlinear C5, and common-EH/gain conditioning exist; nonlocal/asymptotic-safety and several internal sectors remain open;
- unique residual discovery: **3/20** — quotient machinery is operational and scoped comparator residuals exist, but no Candidate Gravity residual target survives the full funnel;
- frozen parent dynamics: **0/20**;
- candidate consistency gates: **0/15**;
- identifiability/Fisher: **0/10**;
- resources/experiment: **0/10**.

The earlier conversational estimate near 35–40% mixed model-preparation infrastructure with model readiness. This frozen rubric intentionally re-baselines the model itself more conservatively and must be used from Iteration 158 onward.
