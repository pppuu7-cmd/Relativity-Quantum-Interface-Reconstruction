# Recovery Delta — RQIR Iteration 149

**Date:** 2026-08-31  
**Authoritative change:** source/observable completion and finite Ward-safe off-shell probe protocol are now frozen; the remaining local C5 blocker is explicit cubic-vertex implementation.

## Previous front

Iteration 148 proved that an on-shell/EOM-reduced basis is not automatically a basis-independent off-shell response basis and set `V_C5^(chi2R)` to `BLOCKED_SOURCE_COMPLETION`.

## New result

The off-shell comparator now uses:

- physical metric `g_mn=eta_mn+kappa h_mn`;
- conserved stress-tensor source derived from a covariant matter action;
- EOM reduction undone off shell;
- Iteration-147 interacting-vacuum retarded/in-in convention;
- six fixed spacelike triplets with `p=q+r`, all away from poles;
- Gaussian windows `(tau,L)=(0.8,0.6)`;
- transverse-traceless spin-2 projectors on every leg.

Numerical regression:

- max `|k.P2| = 1.2533377113932431e-16`;
- max trace `2.636779683484747e-16`;
- max idempotence error `3.3306690738754696e-16`.

Authorities:

- `analysis/c5_source_completed_protocol_iteration149.py`;
- `results/c5_source_completed_protocol_iteration149.json`;
- `candidate_gravity/C5_SOURCE_COMPLETED_PROTOCOL_ITERATION149.md`;
- `research_log/2026-08-31_iteration_149_c5_source_completed_protocol.md`.

## New retained rule

### NG-FUNNEL-009 — PROJECTOR_PASS_IS_NOT_VERTEX_CERTIFICATE

A Ward-safe source-completed probe protocol does not by itself determine the nonlinear C5 vertex. The physical retarded tangent remains uncomputed until the explicit unreduced EH + local-EFT cubic response is implemented and validated.

Classification: `BLOCKED_VERTEX_IMPLEMENTATION`, not rank zero and not C5 consistency FAIL.

## Exact restart instruction

Resume at **Iteration 150**:

1. implement the unreduced EH cubic graviton vertex in the frozen metric/source convention;
2. add the lowest nontrivial local curvature-cubic directions without importing on-shell EOM reduction;
3. contract on the six Iteration-149 triplets with the conserved projectors/windows;
4. run longitudinal replacement/Ward null checks;
5. check field-coordinate/source-completion covariance;
6. compute the first scoped `V_C5^(chi2R)` rank/SVD;
7. leave unsupported higher-dimension and loop/nonanalytic directions explicitly BLOCKED.

No Fisher/resources and no `ANSATZ-003` before a nonzero algebraic residual survives the fixed comparator quotient.
