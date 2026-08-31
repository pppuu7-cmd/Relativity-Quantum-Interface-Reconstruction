# AS-FRG-TT-001 — asymptotic-safety FRG TT vertex comparator

**Frozen in:** Iteration 159  
**Status:** concrete literature comparator; RQIR retarded mapping BLOCKED  
**Not a Candidate Gravity ansatz.**

## Literature authority

Primary fixed source:

- J. M. Pawlowski and J. Tränkle, *Effective action and black hole solutions in asymptotically safe quantum gravity*, arXiv:2309.17043.

Supporting convergence/vertex-expansion source:

- T. Denz, J. M. Pawlowski and M. Reichert, *Towards apparent convergence in asymptotically safe quantum gravity*, arXiv:1612.07315.

Recent continuation/scattering cross-check:

- A. P. Chiesa, J. M. Pawlowski and M. Reichert, *Towards Two-to-Two Scattering of Scalars in Asymptotically Safe Quantum Gravity*, arXiv:2603.10168.

## Fixed published truncation content

The 2023 construction reconstructs a diffeomorphism-invariant background effective action from momentum-dependent graviton correlation functions. In a curvature expansion around flat Euclidean space it retains momentum-dependent curvature-squared form factors, schematically

`Gamma[g] = ... + R f_R2(Delta) R + R_mn f_Ricci2(Delta) R^mn + ...`.

The TT two-point function is parametrised by a momentum-dependent wave function, and the completely TT n-point vertices are projected at the momentum-symmetric point as

`Gamma_tt^(n)(p_vec)=gamma_g^(n)(p) T_R,tt^(n)(p_vec)`.

The paper uses the fluctuation/background relation through an approximate Nielsen-identity mapping and reconstructs the covariant effective action.

## Why this is a concrete comparator

This is not the broad label `asymptotic safety`. The frozen comparator is specifically the published TT vertex/effective-action truncation and its stated projection convention.

Supported objects:

- Euclidean TT two-point momentum dependence;
- Euclidean TT three-/four-point symmetric-point information;
- reconstructed curvature-squared form factors within the published truncation.

## RQIR mapping boundary

The frozen RQIR post-Gaussian protocol uses six unequal off-shell triplets `(p,q,r)` inherited from Iteration 149 and requires an ordered Lorentzian retarded `chi2R` with a fixed source map and energy routing.

A one-variable symmetric-point coefficient `gamma_g^(3)(p)` does not determine the full off-symmetric three-variable tensor vertex

`Gamma_3(p,q,r)`

on those six triplets. In addition, Euclidean effective-action data do not by themselves select the RQIR retarded `i0` prescription for the required ordered response.

The 2026 scalar-scattering work demonstrates that analytic continuation can be carried out for a fully momentum-dependent scalar-graviton vertex, but it does not provide the missing source-completed pure three-graviton retarded vertex on the RQIR six-triplet protocol.

Therefore the following are forbidden without a new published or explicitly derived continuation/interpolation prescription:

- evaluating `chi2R_even/odd` on the six frozen triplets;
- treating symmetric-point `gamma_g^(3)(p)` as if it were `Gamma_3(p,q,r)`;
- zero-filling unsupported tensor components;
- adding a Fisher column from the published symmetric-point curve.

## Retained result

`AS-NG-001 — SYMMETRIC_POINT_EUCLIDEAN_VERTEX_NOT_RETARDED_OFFSHELL_TANGENT`.

Classification: **OPERATIONAL BLOCKED / PROTOCOL MISMATCH**, not a consistency failure of asymptotic safety and not evidence of theory identity.

Retain funnel guardrail:

`NG-FUNNEL-016 — EUCLIDEAN_SYMMETRIC_VERTEX_REQUIRES_EXPLICIT_RETARDED_OFFSHELL_COMPLETION`.

## Current status

- AS Euclidean TT comparator: `FIXED_SCOPED`;
- AS two-point form-factor content: `SUPPORTED_EUCLIDEAN`;
- AS six-probe `chi2R`: `BLOCKED_OFFSYMMETRIC_RETARDED_MAP`;
- AS `N2/C3sym`: `BLOCKED`;
- full AS quotient: `BLOCKED`;
- `ANSATZ-003`: `NOT_CREATED`;
- Fisher/resources: `FORBIDDEN`.
