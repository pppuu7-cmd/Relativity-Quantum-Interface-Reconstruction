# RQIR Research Log — Iteration 158

**Date:** 2026-08-31  
**Branch:** Candidate Gravity comparator funnel  
**MODEL_READINESS: 22%**

## Starting front

Iteration 157 had fixed nonlinear C3/C4/C5 comparator blocks. dRGT `alpha3` retained a scoped conditioned residual, but no Candidate Gravity residual survived a complete comparator funnel. The next required comparator was one fixed nonlocal/form-factor realization.

## Literature basis

1. Donà, Giaccari, Modesto, Rachwał & Zhu, JHEP 08 (2015) 038, arXiv:1506.04589:
   - weakly nonlocal gravity includes quadratic curvature form factors plus a separate higher-curvature potential;
   - large Ricci-form-factor classes have Einstein-Hilbert on-shell tree amplitudes by perturbative field redefinition;
   - the equivalence is on shell and does not imply equality of off-shell response.
2. Briscese, Calcagni, Modesto & Nardelli, JHEP 08 (2024) 204, arXiv:2405.14056:
   - entire nonlocal form factors admit positive spectral representations for the studied classes and can preserve the local physical spectrum;
   - interacting time-ordered/spectral structure differs from the free diagrammatic propagator and requires care in Lorentzian interpretation.

## Fixed comparator

Created `NL-WNL-001`.

Representative TT form factor:

`D_TT(k;sigma)=exp[-H(sigma k^2)]/(k^2+i0k0)`, `H(z)=z^2`, `sigma0=1`.

Independent local potential:

`V=lambda_Ricci3 Tr(Ricci^3)+lambda_Riemann3 cyclic(Riemann^3)`.

Parameters:

`(log sigma,lambda_Ricci3,lambda_Riemann3)`.

## Linear finite result

Six output momenta from the Iteration-149 spacelike protocol were used with the same `(tau,L)=(0.8,0.6)` Gaussian window.

Common-gain plus form-factor tangent:

- rank `2`;
- singular values `[3.3576236639554855,0.6000359203875203]`;
- `smin/smax=0.17870850948216196`;
- `log sigma` residual fraction after projecting a common response gain: `0.3996471300114534`.

Interpretation: a known nonlocal form factor can generate a substantial finite response-shape direction. This is comparator structure, not candidate novelty.

## Nonlinear potential result

The two chosen potential derivatives reuse the already explicit and Ward-validated local C5 `Ricci^3/Riemann^3` response columns.

Residual norms against the current C5 `R^3` span:

- `4.73e-16`;
- `1.91e-15`.

So these potential directions add no new nonlinear span beyond current C5.

## New retained results

### `NL-NG-001 — FORM_FACTOR_DOES_NOT_FIX_NONLINEAR_RESPONSE`

A quadratic form factor leaves independent higher-curvature potential coefficients invisible at two-point level. A form-factor label is therefore not a complete nonlinear comparator.

### `NL-NG-002 — LOCAL_CUBIC_POTENTIAL_ALREADY_IN_C5_SPAN`

For the two frozen cubic potential directions, the resulting nonlinear response is exactly contained in the existing local C5 comparator span.

### `NG-FUNNEL-015 — FIX_PROPAGATOR_AND_INTERACTION_POTENTIAL_SEPARATELY`

A finite nonlocal comparator must freeze form factor, interaction potential, physical source/metric convention and off-shell retarded map independently.

## Blockers

- form-factor-induced nonlocal cubic `chi2R`: `BLOCKED_NONLOCAL_CUBIC_VERTEX_IMPLEMENTATION`;
- full Lorentzian nonlocal causal completion: BLOCKED;
- nonlocal quantum-state `N2/C3sym`: BLOCKED;
- full nonlocal comparator quotient: BLOCKED.

No blocked row is set to zero.

## Model readiness

Previous formal baseline (Iteration 157): `20%`.

**MODEL_READINESS: 22%**.

Reason for +2 points: comparator foundation increased from `17/25` to `19/25` by adding a fixed partial nonlocal comparator. No credit is given to unique residual, parent dynamics, candidate consistency, Fisher or resources because none of those gates closed.

## Next gate — Iteration 159

Prefer a concrete asymptotic-safety vertex truncation as the next independent strong quantum comparator, unless the form-factor-induced cubic nonlocal vertex can be completed cleanly without delaying comparator breadth. The next calculation must remain finite and parameterized; no program-level capability mask.
