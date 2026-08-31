# RQIR Research Log — Iteration 149

**Date:** 2026-08-31  
**Branch:** Candidate Gravity / fixed C5 off-shell comparator  
**Promotion decision:** no `ANSATZ-003` frozen

## Starting authority

Iteration 148 established `NG-FUNNEL-008`: the on-shell/EOM-reduced C5 amplitude basis cannot by itself define a basis-independent off-shell `chi2R` tangent. The next task was to remove the source/observable ambiguity before any rank claim.

## Decision

Use the physical metric `g_mn=eta_mn+kappa h_mn` and a covariant matter action `S_m[g,Psi]`; define the operational source through its conserved stress tensor. Off shell, undo the Iteration-146 EOM reduction rather than attempting to reuse the ten reduced amplitude coordinates with an incomplete contact map.

## Finite protocol

Six deterministic spacelike triplets `(p,q,r)`, `p=q+r`, were frozen away from massless poles. A Gaussian time/spatial window with `(tau,L)=(0.8,0.6)` was fixed. Every external leg is projected with the D=4 transverse-traceless spin-2 projector.

Regression results:

- max longitudinal contraction `1.2533377113932431e-16`;
- max metric trace `2.636779683484747e-16`;
- max idempotence error `3.3306690738754696e-16`;
- window weights remain finite in `[0.8381451361499129,0.9567587587766662]`.

This closes the operational probe/source ambiguity at the declared tree-level local-EFT protocol.

## New negative/guardrail result

**NG-FUNNEL-009 — PROJECTOR_PASS_IS_NOT_VERTEX_CERTIFICATE.**

Passing conservation/Ward projector tests does not instantiate the nonlinear gravity comparator tangent. The repository still lacks the complete unreduced EH + local-EFT cubic vertex in the frozen source convention. Therefore `V_C5^(chi2R)` remains `NOT_COMPUTED`, with status `BLOCKED_VERTEX_IMPLEMENTATION`.

This is not a C5 consistency FAIL and not evidence of a zero response.

## Literature check

The recent off-shell equivalence analysis by Kuntz & Liberati (arXiv:2607.12644) materially supports the operational choice: off-shell equivalence is probe/observable dependent and cannot be inferred from coordinate Green functions alone. This reinforces the Iteration-148/149 requirement to freeze the physical source map before comparing retarded response tangents.

## Consequences

- source/observable convention: FROZEN;
- finite off-shell probe set: PASS;
- Ward/projector regression: PASS;
- EH+local-EFT cubic response: BLOCKED_VERTEX_IMPLEMENTATION;
- loop/nonanalytic rows: BLOCKED;
- Fisher/resources remain forbidden;
- `ANSATZ-003` remains withheld.

## Next gate

Iteration 150: implement and validate the unreduced EH plus lowest nontrivial local curvature-cubic vertex in the frozen convention, contract it with the Iteration-149 probes, perform longitudinal null/source-completion checks, then obtain the first scoped retarded C5 tangent/rank certificate.
