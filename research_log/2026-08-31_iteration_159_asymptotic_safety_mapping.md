# RQIR Research Log — Iteration 159

**Date:** 2026-08-31  
**Comparator:** `AS-FRG-TT-001`

## Starting point

Authoritative Iteration 158 fixed the first weakly-nonlocal comparator block and the stable model-readiness rubric. Its exact restart instruction preferred one explicit asymptotic-safety vertex truncation if the nonlocal cubic response was not yet ready.

## Literature checked

- Pawlowski & Tränkle, arXiv:2309.17043: momentum-dependent graviton correlation functions, reconstructed diffeomorphism-invariant effective action, TT n-point projection at a momentum-symmetric Euclidean point, curvature form factors.
- Denz, Pawlowski & Reichert, arXiv:1612.07315: systematic vertex expansion and apparent convergence.
- Chiesa, Pawlowski & Reichert, arXiv:2603.10168: fully momentum-dependent scalar-graviton vertex with nontrivial analytic continuation used for scattering; useful continuation cross-check but not the missing pure three-graviton RQIR vertex.

## Fixed comparator

`AS-FRG-TT-001` is the specific published TT vertex/effective-action truncation, not the broad `asymptotic safety` program label.

Supported published content includes Euclidean TT two-point momentum dependence, symmetric-point TT three-/four-point information, and reconstructed curvature-squared form factors.

## RQIR mapping test

The frozen RQIR `chi2R` protocol requires six unequal off-shell triplets and an ordered Lorentzian retarded three-graviton response with source completion.

The published symmetric-point coefficient `gamma_g^(3)(p)` is only a one-variable projection and does not determine the full off-symmetric `Gamma_3(p,q,r)` needed on those six triplets. Euclidean effective-action information also does not by itself select the required ordered retarded `i0` prescription.

Therefore no honest numerical `V_AS^(chi2R)` can be produced from the published symmetric-point data alone without adding an interpolation/analytic-continuation convention not fixed by the comparator.

## New retained result

`AS-NG-001 — SYMMETRIC_POINT_EUCLIDEAN_VERTEX_NOT_RETARDED_OFFSHELL_TANGENT`.

Classification: `OPERATIONAL_BLOCKED / PROTOCOL_MISMATCH`.

Retain guardrail:

`NG-FUNNEL-016 — EUCLIDEAN_SYMMETRIC_VERTEX_REQUIRES_EXPLICIT_RETARDED_OFFSHELL_COMPLETION`.

This is not a consistency FAIL, exact identity, near-degeneracy, or zero tangent.

## BLOCKED

- six-probe AS `chi2R_even/odd`;
- source-completed AS nonlinear Ward test;
- AS `N2/C3sym`;
- full AS quotient.

No `ANSATZ-003`; no Fisher/resources.

## Stable readiness rubric

`MODEL_READINESS: 22%`

No change from authoritative Iteration 158. The comparator is now concretely specified, but the exact post-Gaussian response required for the quotient remains blocked, so no weighted block is materially closed.

- comparator foundation: `19/25`;
- unique residual discovery: `3/20`;
- frozen parent dynamics/ANSATZ: `0/20`;
- consistency/positivity/Ward/causality: `0/15`;
- identifiability/Fisher: `0/10`;
- resource/experiment closure: `0/10`.

## Next gate — Iteration 160

Audit the reconstructed covariant form factors/effective action of arXiv:2309.17043 to determine whether they contain sufficient action-level information to derive the required off-symmetric cubic TT vertex directly. If yes, derive and map it; if not, freeze `BLOCKED_AS_ACTION_DATA_INSUFFICIENT` and do not invent the missing vertex.
