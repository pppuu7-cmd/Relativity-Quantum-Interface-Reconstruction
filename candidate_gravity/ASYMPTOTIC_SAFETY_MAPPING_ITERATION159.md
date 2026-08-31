# Candidate Gravity — Iteration 159 Asymptotic-Safety Mapping

## Goal

Follow Iteration 158 by instantiating one concrete asymptotic-safety comparator with explicit momentum-dependent graviton information and test whether it can be mapped into the frozen RQIR six-probe retarded nonlinear-response protocol without arbitrary assumptions.

## Fixed comparator

`AS-FRG-TT-001`, based primarily on Pawlowski & Tränkle, arXiv:2309.17043.

The paper computes momentum-dependent graviton correlation functions with the functional renormalisation group and reconstructs a diffeomorphism-invariant effective action with curvature form factors. The completely TT n-point functions are represented at a Euclidean momentum-symmetric point by a one-variable coefficient multiplying a fixed TT tensor structure.

## Protocol comparison

RQIR's frozen nonlinear protocol uses six unequal off-shell triplets `(p,q,r)` and an ordered retarded response

`chi2R = -G_R(p) Gamma_3(p,-q,-r) G_R(q) G_R(r)`

with source completion and fixed Lorentzian energy routing.

The published symmetric-point function `gamma_g^(3)(p)` is not enough to reconstruct the full off-symmetric `Gamma_3(p,q,r)` on those triplets. A symmetric-point scalar coefficient is lower-dimensional data than the full three-momentum vertex required here.

Moreover, the published reconstruction begins from Euclidean vertices/effective action. A Wick-rotated effective action does not automatically supply the ordered retarded `i0` prescription and source-completed causal object required by the RQIR gate.

The 2026 Chiesa-Pawlowski-Reichert scalar-scattering calculation is a useful cross-check that nontrivial analytic continuation can be done when a fully momentum-dependent vertex is explicitly available, but it is a scalar-graviton vertex and does not fill the pure three-graviton RQIR object.

## Result

`AS-NG-001 — SYMMETRIC_POINT_EUCLIDEAN_VERTEX_NOT_RETARDED_OFFSHELL_TANGENT`.

Status: `OPERATIONAL_BLOCKED / PROTOCOL_MISMATCH`.

This is not:

- a consistency FAIL of asymptotic safety;
- a statement that the AS vertex is zero;
- an exact comparator identity;
- a near-degeneracy certificate.

It is an exact statement about missing information needed for the frozen RQIR map.

Retain:

`NG-FUNNEL-016 — EUCLIDEAN_SYMMETRIC_VERTEX_REQUIRES_EXPLICIT_RETARDED_OFFSHELL_COMPLETION`.

## Consequences for the comparator funnel

The asymptotic-safety class is now represented by a concrete frozen literature truncation rather than a broad label, satisfying the comparator-instantiation requirement. However its post-Gaussian RQIR tangent remains unavailable, so it cannot yet enlarge or close the numerical comparator span.

No Fisher/resources are permitted. No `ANSATZ-003` is created.

## MODEL_READINESS

`MODEL_READINESS: 22%`

No increase from authoritative Iteration 158. Comparator foundation is better specified, but the AS block remains operationally blocked at the exact quantity needed for the quotient. Under the stable rubric, work volume alone does not earn points.

Authoritative allocation retained:

- comparator foundation: `19/25`;
- unique residual discovery: `3/20`;
- frozen parent dynamics/ANSATZ: `0/20`;
- candidate consistency: `0/15`;
- identifiability/Fisher: `0/10`;
- resource/experiment closure: `0/10`.

## Exact next gate — Iteration 160

Do not invent an off-symmetric AS vertex. Instead test whether the reconstructed covariant form factors in arXiv:2309.17043 provide enough action-level information to derive the required off-symmetric cubic TT vertex directly. If yes, implement that derivation and source-completed retarded continuation on the six frozen triplets. If not, freeze `BLOCKED_AS_ACTION_DATA_INSUFFICIENT` and return to the nonlocal comparator only if its full covariant action permits an unambiguous cubic form-factor variation.
