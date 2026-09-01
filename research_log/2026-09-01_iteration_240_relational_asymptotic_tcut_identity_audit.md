# Research log — RQIR Candidate Gravity Iteration 240

Date: 2026-09-01

MODEL_READINESS: 24%

Started from repository authority at Iteration 239. Read `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_239.md`, the Iteration-239 research log and recent commits. Latest authority commit was `43fd05624cdac18ad3bd66c7e1e7647183f9aae2`. GitHub Actions reported zero workflow runs, so no duplicate computation existed.

## Scientific action

Audited relational and asymptotic pure-gravity gauge-safe observables for an **identity-preserving** route back to frozen

`T_cut = D_s Gamma3_ret,soft - W[D_s K2]`.

Current/relevant authority checked included:
- Aguilar-Gutierrez, Ferrero, Hoehn, Marchetti, arXiv:2607.21463 (2026), relational path integral and gauge-invariant frame-dependent effective actions;
- Fröb and Lima, arXiv:2303.16218, nonlinear relational metric observables in field-dependent coordinates;
- Kozameh and Depaola, arXiv:2605.06961 and arXiv:2605.06001 (2026), pure-gravity null-surface/null-infinity perturbation theory using Bondi radiative data rather than bulk/off-shell fields;
- recent null-boundary phase-space / boundary-observable work as a structural cross-check that gauge-safe asymptotic variables are boundary reduced data, not the frozen bulk metric 1PI pair.

## Result

The latest relational authority is important: it shows that gauge-invariant effective actions can be defined. However sources are coupled to **frame-dressed relational observables**. At nonlinear order these differ from bare metric variables by field-dependent coordinate/dressing terms. Functional derivatives therefore carry frame-dependent Jacobian/contact contributions. No published same-parent cubic source-reduction map was found that turns those relational derivatives into the exact frozen bare-metric `Gamma3_ret[h,h,h]` and `K2[h,h]` while preserving one retarded prescription and the same hard-channel discontinuity.

The asymptotic route is also physical but comparator-incompatible: the 2026 null-surface formulation uses Bondi shear/radiative data at null infinity, explicitly without bulk fields or off-shell propagators. Its natural analytic structure is boundary/on-shell, not the frozen bulk/source-completed hard-channel 1PI discontinuity.

Therefore neither gauge-safe route supplies an identity-preserving executable realization of frozen `T_cut` without adding a new frame/dressing/source map or redefining the observable.

Freeze:

`OPERATIONALLY_NONEXECUTABLE_WITH_CURRENT_PUBLISHED_AUTHORITY`

with

`BLOCKED_NOT_ZERO`.

Retain parent blocker:

`BLOCKED_T_CUT_NATIVE_H3_EXECUTABILITY_AT_GAUGE_SAFE_CUBIC_EFFECTIVE_ACTION_BOUNDARY`.

New labels:
- `REL-NG-020`;
- `REL-CUT-020`;
- `REL-BLOCK-005`;
- `NG-FUNNEL-096`.

This is an operational BLOCKED/current-authority result, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, a zero comparator column, or Candidate Gravity novelty.

No heavy computation launched because comparator executability is upstream. No robust Candidate Gravity residual. No `ANSATZ-003`. Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Readiness change from Iteration 239: 0 percentage points. Comparator foundation remains `24/25`; robust unique residual remains `0/20`. The final audited `T_cut` shortcut is now frozen as operationally non-executable under current published authority, but no readiness block closes.

Next gate: Iteration 241 should audit the retained Candidate Gravity funnel itself and determine whether **any** residual target remains that is algebraically nonzero and executable under already frozen comparator authority. Do not search for another proxy observable. If none exists, freeze `NO_EXECUTABLE_RESIDUAL_TARGET_UNDER_CURRENT_COMPARATOR_AUTHORITY` and separate future work into an authority-improvement program, without `ANSATZ-003` or Fisher/resources.