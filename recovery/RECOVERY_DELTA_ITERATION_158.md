# Recovery Delta — RQIR Iteration 158

**Date:** 2026-08-31  
**Authoritative change:** first fixed weakly-nonlocal comparator sub-block added; propagator/form-factor and nonlinear interaction-potential freedom are now explicitly separated.  
**MODEL_READINESS: 22%**

## Previous front

Iteration 157 contained fixed scoped C3, nonlinear dRGT C4 and local nonlinear C5 comparators. The next missing strong comparator class was nonlocal/form-factor gravity.

## New authorities

- `candidate_gravity/MODEL_READINESS_RUBRIC.md`;
- `candidate_gravity/comparators/NL-WNL-001.md`;
- `analysis/nonlocal_formfactor_potential_iteration158.py`;
- `results/nonlocal_formfactor_potential_iteration158.json`;
- `candidate_gravity/CANDIDATE_GRAVITY_NONLOCAL_ITERATION158.md`;
- `research_log/2026-08-31_iteration_158_nonlocal_formfactor_potential.md`;
- `recovery/RECOVERY_DELTA_ITERATION_158.md`.

## Fixed comparator

`NL-WNL-001`.

Scoped TT transfer:

`D_TT(k;sigma)=exp[-(sigma k^2)^2]/(k^2+i0k0)`, with `sigma0=1`.

Independent local potential:

`V=lambda_Ricci3 Tr(Ricci^3)+lambda_Riemann3 cyclic(Riemann^3)`.

Parameter order:

`(log sigma,lambda_Ricci3,lambda_Riemann3)`.

## Numerical certificate

Six frozen output probes:

- common-gain rank: `1`;
- gain + `log sigma` rank: `2`;
- singular values `[3.3576236639554855,0.6000359203875203]`;
- `smin/smax=0.17870850948216196`;
- `log sigma` residual fraction after common gain: `0.3996471300114534`.

The two local cubic potential columns have rank `2`, but their residual norms against the existing C5 `Ricci^3/Riemann^3` span are only

`4.73e-16`, `1.91e-15`.

## Retained results

### `NL-NG-001 — FORM_FACTOR_DOES_NOT_FIX_NONLINEAR_RESPONSE`

The quadratic nonlocal form factor does not determine independent higher-curvature interaction-potential coefficients.

### `NL-NG-002 — LOCAL_CUBIC_POTENTIAL_ALREADY_IN_C5_SPAN`

The two explicitly frozen local cubic potential directions are already contained in the existing C5 local nonlinear span.

### `NG-FUNNEL-015 — FIX_PROPAGATOR_AND_INTERACTION_POTENTIAL_SEPARATELY`

A nonlocal theory label or propagator is not a complete post-Gaussian comparator. Form factor, interaction potential and source-completed off-shell causal map must be frozen separately.

## Critical blocker

The form factor itself generates nonlocal cubic and higher vertices in the covariant expansion. Their contribution to the frozen source-completed `chi2R` protocol is not yet implemented.

Therefore:

- `d chi2R/dlog sigma`: BLOCKED at the nonlocal cubic-vertex level;
- full Lorentzian nonlocal causal completion: BLOCKED;
- nonlocal `N2/C3sym`: BLOCKED;
- full nonlocal quotient: BLOCKED.

Do not zero-fill these entries.

## Readiness accounting

The stable rubric is now authoritative in `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

Iteration 157 formal baseline: `20%`.

**MODEL_READINESS: 22%**.

Only comparator-foundation credit increased (`17/25 -> 19/25`). Unique Candidate Gravity residual discovery remains `3/20`; all later model-construction and experimental blocks remain zero.

## Exact restart instruction

Resume at **Iteration 159**.

Preferred route:

1. instantiate one concrete asymptotic-safety vertex truncation with finite parameters and explicit momentum-dependent 2-/3-graviton information;
2. map only supported finite response directions into the six-probe protocol;
3. compare against common EH/gain + current C4/C5/nonlocal span;
4. if available information is insufficient for an off-shell source-completed retarded tangent, record the exact BLOCKED boundary rather than inventing a vertex;
5. alternatively complete the `NL-WNL-001` form-factor-induced cubic response only if it can be done from a fixed published action without new arbitrary choices;
6. no `ANSATZ-003`, Fisher or resources before a robust Candidate Gravity residual survives the complete fixed comparator funnel.
