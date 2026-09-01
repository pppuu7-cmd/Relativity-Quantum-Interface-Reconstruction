# Research log — RQIR Candidate Gravity Iteration 232

Date: 2026-09-01

MODEL_READINESS: 24%

Started from repository authority: `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, Iteration-231 recovery delta/research log, recent commits, and current Actions state. Authoritative front was Iteration 231 and there were no active workflow runs.

Iteration 232 freezes an explicit published pure-Einstein Vilkovisky operator convention from Giacchini–de Paula Netto–Shapiro, Phys. Rev. D 102, 106006 (2020), arXiv:2006.04217. The field-space metric parameter is fixed by Vilkovisky's prescription to `a=-1/2`; in D=4 this is nondegenerate because the singular value is `-1/D=-1/4`. In the nonsingular DeWitt gauge, `a=-1/2` makes both the local graviton operator `H=-(1 Box+Pi)` and FP ghost operator `N^alpha_beta=delta^alpha_beta Box+R^alpha_beta` minimal Laplace type.

This closes the narrow question left by Iteration 231: a same-paper, same-convention minimal local graviton+ghost operator pair can indeed be frozen.

However, the full one-loop Vilkovisky unique action in the same authority also contains connection/gauge-orbit correction traces `U1`, `U2`, and `U1^2`. These are required for the off-shell gauge/parametrization completion. The published calculation evaluates them only to the local background-dimension order needed for the UV pole; it does not provide a finite third-order nonlocal curvature form-factor map for the complete trace set. Therefore generic CPT3 cannot be applied only to `H,N` and promoted as the unique off-shell C5 comparator.

The known divergent unit-test target is frozen from Eq. (60): coefficients `53/45` for `Riemann^2`, `-61/90` for `Ricci^2`, `25/36` for `R^2`, `8` for `Lambda R`, and `12` for `Lambda^2`, with the published common overall pole factor.

New substatus: `BLOCKED_COMPLETE_VD_CONNECTION_TRACE_TO_FINITE_CPT3_MAP` under `BLOCKED_C5_VD_NONLOCAL_CUBIC_SPECIALIZATION`.

Retain `C5-CUT-016`, `C5-CUT-017`, `C5-CUT-018`, `REL-NG-012`, `NG-FUNNEL-088` as defined in `candidate_gravity/C5_VD_OPERATOR_FREEZE_ITERATION232.md`.

No heavy finite CPT3 job was launched because omitting the Vilkovisky connection traces would violate the frozen off-shell authority rule. No Candidate Gravity residual. No `ANSATZ-003`. No Fisher/resources.

MODEL_READINESS: 24%

Readiness change: 0 percentage points. Comparator foundation remains `24/25`; robust unique residual remains `0/20`. The local operator convention is now frozen, but the complete finite unique-action C5 coordinate is still blocked.

Next gate: audit whether generalized Schwinger–DeWitt/CPT machinery supplies finite nonlocal third-order form factors for the specific composite `U1`, `U2`, `U1^2` trace structures in the same pure-Einstein convention. If not, freeze this blocker and return to AS rather than inventing a connection representative.
