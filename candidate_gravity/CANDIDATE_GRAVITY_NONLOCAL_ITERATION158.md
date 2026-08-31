# Candidate Gravity — Iteration 158

## Fixed nonlocal comparator and propagator/interaction separation

**Date:** 2026-08-31  
**Comparator:** `NL-WNL-001`  
**MODEL_READINESS: 22%**

## Question

Can a strong nonlocal/form-factor gravity comparator be represented by a finite propagator deformation alone, or must its nonlinear interaction sector be frozen independently before it enters the RQIR quotient?

## Answer

The propagator alone is insufficient.

A weakly-nonlocal covariant action contains both quadratic curvature form factors and a higher-curvature interaction potential. The latter can change cubic/higher response while leaving the quadratic propagator untouched. In addition, Ricci-form-factor theories can be on-shell tree equivalent to Einstein gravity by field redefinition while still differing off shell, exactly where the RQIR retarded protocol lives.

Therefore the first fixed comparator freezes both a representative entire form factor and explicit interaction-potential coordinates.

## Frozen representative

TT propagator/transfer:

`D_TT(k;sigma)=exp[-(sigma k^2)^2]/(k^2+i0 k0)`.

Reference `sigma=1`.

Interaction potential:

`V=lambda_Ricci3 Tr(Ricci^3)+lambda_Riemann3 cyclic(Riemann^3)`.

Parameters:

`theta_NL=(log sigma,lambda_Ricci3,lambda_Riemann3)`.

## Linear six-probe result

Using the six frozen Iteration-149 output momenta and the same Gaussian window, the common-gain column plus `d/dlog sigma` has rank `2`.

Singular values:

`[3.3576236639554855,0.6000359203875203]`.

After profiling only a common linear response gain:

`||r_sigma||/||v_sigma|| = 0.3996471300114534`.

This proves a substantial finite shape direction for the known nonlocal comparator. It is not a Candidate Gravity novelty direction.

## Nonlinear potential result

The two explicit potential derivatives are exactly the already Ward-validated C5 local curvature-cubic response columns.

Their residual norms against the existing C5 `R^3` span are

`4.73e-16` and `1.91e-15`.

Thus the explicitly frozen local cubic potential adds no new nonlinear span beyond current C5.

## What remains blocked

The full covariant form factor also generates nonlocal cubic/higher vertices. Those contributions have not yet been expanded in the frozen physical metric/source, CTP/retarded and six-probe convention.

Therefore `d chi2R / d log sigma` from the nonlocal cubic vertex is `BLOCKED_NONLOCAL_CUBIC_VERTEX_IMPLEMENTATION`, never zero.

`N2/C3sym` and the full Lorentzian nonlocal CTP sector also remain BLOCKED.

## Retained results

- `NL-NG-001 — FORM_FACTOR_DOES_NOT_FIX_NONLINEAR_RESPONSE`;
- `NL-NG-002 — LOCAL_CUBIC_POTENTIAL_ALREADY_IN_C5_SPAN`;
- `NG-FUNNEL-015 — FIX_PROPAGATOR_AND_INTERACTION_POTENTIAL_SEPARATELY`.

## Readiness accounting

Formal Iteration-157 baseline under the frozen rubric: `20%`.

Iteration 158: `22%`.

- comparator foundation increases from `17/25` to `19/25` because one concrete nonlocal comparator is now partially instantiated in the same finite probe language;
- unique residual discovery remains `3/20` because the new sigma shape belongs to a known comparator and is not a Candidate Gravity residual;
- parent dynamics, candidate consistency, Fisher and resources remain `0`.

No readiness credit is awarded for the still-blocked form-factor-induced cubic response.
