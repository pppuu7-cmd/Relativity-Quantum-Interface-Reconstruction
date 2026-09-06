# RECOVERY DELTA — ITERATION 502

Date: 2026-09-06
MODEL_READINESS: 24%

## New exact estimator/provenance authority
For frozen mixed central4, exact moment `M11=-340` gives one-dimensional h^10 coefficient `-17/1995840`. Tensor-product assembly therefore has total h^10 sector

`h^10[-17/1995840 (d_x^11 d_y+d_x d_y^11) + 1/7560 (d_x^5 d_y^7+d_x^7 d_y^5)]`.

With HALF step `h/2`, BASE-minus-HALF multiplies this sector by `1023/1024`, yielding

`h^10[-527/61931520 (d_x^11 d_y+d_x d_y^11) + 341/2580480 (d_x^5 d_y^7+d_x^7 d_y^5)]`.

Classification: `PASS_BASE_HALF_DISCREPANCY_H10_EXACT__NON_PROMOTING`.

Reproducible audit: `candidate_gravity/code/iteration502_base_half_discrepancy_h10.py`.
Result record: `candidate_gravity/results/iteration502_base_half_discrepancy_h10.txt`.

Scope: smooth-field asymptotic estimator/provenance authority only. No mode-independent Richardson identity, no frozen `ds=-d_base` change, no threshold weakening, no physical promotion, no novelty certificate.

## Active numerical gate
Canonical rank20 `(-2.5e-6,+2.5e-6)` run `34041245929` remains `in_progress`; do not duplicate. Certified occurrence-weighted support remains `24/32 = 75.000% = 1920/2560` until raw artifact consumption proves otherwise.

## Retained blockers
Physical/operator authority remains Iteration 411; blocker authority remains Iteration 421 `BLOCKED_CONVERGENCE`; unresolved set `[2]`. Robust comparator-subtracted residual absent; `ANSATZ-003` and Fisher/resources remain BLOCKED.

## Exact next gate
Raw-consume rank20 fail-closed after completion. PASS permits only the next explicit UNTESTED Iteration-455 manifest coordinate; BLOCKED requires first failing `z/phi/radial` localization without frozen-threshold changes.

MODEL_READINESS: 24%
Readiness change: 0 percentage points.
