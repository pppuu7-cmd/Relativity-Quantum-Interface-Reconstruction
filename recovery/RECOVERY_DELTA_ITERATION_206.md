# Recovery Delta — RQIR Iteration 206

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Previous front

Iteration 205 replaced finite analytic soft2 novelty with the linked nonanalytic coordinate

`T_cut = D Gamma3_ret,soft - W[D K2]`.

The local analytic C5 derivative tower is exact-null under D, but the physical C5 loop positive control remained open.

## New authority result

A controlled third-order one-loop formal route exists:

- Barvinsky–Gusev–Zhytnikov–Vilkovisky covariant perturbation theory computes the generic one-loop effective action to third order in curvature, including third-order nonlocal form factors and generalized spectral representations;
- Barvinsky–Vilkovisky expectation-value technology supplies a special Euclidean-to-Lorentzian analytic continuation giving causal in-vacuum effective equations.

Thus the C5 cut blocker is not `NO_CAUSAL_NONLOCAL_FORMALISM`.

## New gauge/parametrization guardrail

Ordinary off-shell quantum-GR effective action depends on gauge fixing and parametrization of the quantum metric. Modern Vilkovisky–DeWitt/unique-effective-action calculations explicitly verify gauge/parametrization independence of the unique construction in 4D Einstein gravity.

Therefore a gauge-dependent background-field `Gamma3` may not be inserted directly into RQIR as a physical comparator.

Allowed routes:

1. use a Vilkovisky–DeWitt/unique effective action specialization; or
2. construct an explicitly gauge-invariant/source-completed retarded observable whose gauge/parametrization dependence cancels.

## Remaining C5 implementation blocker

`BLOCKED_C5_GRAVITON_GHOST_CPT3_SPECIALIZATION_AND_GAUGE_SAFE_RQIR_PROJECTION`:

1. specialize generic covariant perturbation theory to the pure Einstein graviton Hessian and Faddeev–Popov ghosts;
2. include the unique-effective-action connection or otherwise demonstrate physical gauge independence;
3. obtain the actual 4D third-order nonlocal form-factor combination;
4. map to the fixed source-completed metric convention;
5. take the causal in-vacuum retarded continuation and timelike discontinuity;
6. compute `D Gamma3_ret,soft - W[D K2]`.

## Retained results

- `C5-CUT-001 — THIRD_ORDER_NONLOCAL_ONE_LOOP_FORM_FACTOR_AND_SPECTRAL_FORMALISM_EXISTS_FOR_GRAVITATING_FIELDS`;
- `C5-CUT-002 — CAUSAL_IN_VACUUM_EFFECTIVE_EQUATIONS_HAVE_A_CONTROLLED_EUCLIDEAN_TO_LORENTZIAN_CONTINUATION_ROUTE`;
- `C5-CUT-003 — OFFSHELL_QUANTUM_GRAVITY_VERTEX_REQUIRES_GAUGE_PARAMETRIZATION_SAFE_UNIQUE_OR_PHYSICAL_SOURCE_PROJECTION`;
- `NG-FUNNEL-062 — C5_LINKED_CUT_BLOCKER_IS_NOW_PURE_GRAVITY_GRAVITON_GHOST_SPECIALIZATION_PLUS_GAUGE_SAFE_SOURCE_COMPLETED_RQIR_PROJECTION`.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

Comparator foundation remains `23/25`; no unique residual, ANSATZ, Fisher or resource points.

## Exact restart instruction

Resume at **Iteration 207 — gauge-safe pure-gravity C5 cut specialization design**.

Required order:

1. audit whether published third-order nonlocal/unique-effective-action results already contain the pure-gravity specialization;
2. otherwise freeze the graviton+ghost operator and Vilkovisky–DeWitt connection data required to specialize the generic form factors;
3. reduce the invariant set using the physical null-soft TT / source-completed protocol before heavy symbolic computation;
4. define a reproducible implementation plan and only then decide whether GitHub Actions/heavy symbolic algebra is justified;
5. continue C4/AS/C3 cut comparator authority audits independently.

No `ANSATZ-003`, Fisher or resources.
