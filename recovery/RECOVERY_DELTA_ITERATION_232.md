# Recovery Delta — RQIR Iteration 232

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## New authority

Iteration 232 starts from authoritative Iteration 231 and freezes the explicit pure-Einstein Vilkovisky operator convention of Giacchini–de Paula Netto–Shapiro, Phys. Rev. D 102, 106006 (2020), arXiv:2006.04217.

The field-space metric parameter is fixed to `a=-1/2` by Vilkovisky's prescription. In `D=4` this is nondegenerate (`-1/2 != -1/4`). In the nonsingular DeWitt gauge, the local graviton operator `H` and FP ghost operator `N` both become minimal Laplace type because the ghost nonminimal coefficient `1+2a` vanishes.

This means Iteration 231's local operator-freezing question is closed positively.

## Sharpened blocker

The complete one-loop Vilkovisky unique action from the same authority also contains connection/gauge-orbit traces `U1`, `U2`, and `U1^2`; they are required for off-shell gauge/parametrization completion. The published calculation evaluates these structures only far enough to obtain the local UV divergence, not a finite nonlocal third-order curvature form-factor map.

Retain umbrella status:

`BLOCKED_C5_VD_NONLOCAL_CUBIC_SPECIALIZATION`

and replace the previous substatus by:

`BLOCKED_COMPLETE_VD_CONNECTION_TRACE_TO_FINITE_CPT3_MAP`.

Minimal `H+N` alone is not the unique action and must not be used as a surrogate finite C5 comparator.

## Reproducible unit/convention certificate

- `candidate_gravity/code/iteration232_vd_operator_freeze_check.py`
- `candidate_gravity/results/iteration232_vd_operator_freeze_check.txt`

Frozen Eq. (60) UV-pole coefficient targets: `53/45 Riemann^2 - 61/90 Ricci^2 + 25/36 R^2 + 8 Lambda R + 12 Lambda^2`, with the common published overall pole factor.

## Retained labels

- `C5-CUT-016` — published pure-Einstein VD authority fixes a nondegenerate `a=-1/2` DeWitt convention with minimal local graviton and ghost operators;
- `C5-CUT-017` — minimal `H,N` do not equal the complete off-shell Vilkovisky one-loop operator because connection traces are required;
- `C5-CUT-018` — the minimal remaining C5 blocker is the complete VD connection-trace to finite-CPT3 map;
- `REL-NG-012` — reproducing only the graviton+ghost heat kernel is not an off-shell unique-action certificate;
- `NG-FUNNEL-088` — an `R^3` result computed from `H+N` alone cannot be promoted as the RQIR C5 unique-action comparator.

## Classification guardrails

This is an operational/scientific `BLOCKED` result, not a consistency FAIL, not exact comparator identity, not near-degeneracy, not a zero C5 column, and not Candidate Gravity novelty.

## Candidate state

- robust Candidate Gravity residual: `NONE`;
- `ANSATZ-003`: `NOT_CREATED`;
- Fisher/resources: `FORBIDDEN`;
- heavy finite CPT3 run: `NOT_AUTHORIZED`.

## Readiness

`MODEL_READINESS: 24%` — unchanged from Iteration 231. Comparator foundation remains `24/25`; robust unique residual remains `0/20`. The local operator convention is now frozen, but the complete finite C5 coordinate is not closed.

## Exact restart instruction

Iteration 233: audit Barvinsky–Vilkovisky generalized Schwinger–DeWitt/covariant perturbation theory for finite nonlocal third-order treatment of the exact `U1`, `U2`, `U1^2` composite trace structures used in the 2020 pure-Einstein unique-action reduction. If a same-convention mapping exists, first reproduce Eq. (60) before finite `R^3`; if not, freeze `BLOCKED_COMPLETE_VD_CONNECTION_TRACE_TO_FINITE_CPT3_MAP` and return to AS. Do not create `ANSATZ-003`; do not run Fisher/resources.
