# Recovery Delta — RQIR Iteration 150

**Date:** 2026-08-31  
**Authoritative change:** first explicit local tree C5 nonlinear-response tangent computed in the frozen Iteration-149 off-shell protocol.

## Previous front

Iteration 149 froze the metric/source convention and finite TT probe layer but left the local C5 response at `BLOCKED_VERTEX_IMPLEMENTATION`.

## New result

The EH cubic TT response is now implemented directly from the unreduced `sqrt(-g) g Gamma Gamma` action density for three off-shell plane-wave modes. Two explicit covariant curvature-cubic directions were added in the same physical metric convention:

- `Tr(Ricci^3)`;
- cyclic `Riemann^3`.

On the six frozen probes the resulting local tangent has shape `6x2`, rank `2/2`, singular values `[4.83562189, 1.10930485]`, and `s_min/s_max=0.2294027268`.

EH permutation asymmetry is below `8.13e-14`. The largest final finite-difference halving-step change before Richardson extrapolation is `9.22e-6`.

Authorities:

- `analysis/c5_cubic_response_iteration150.py`;
- `results/c5_cubic_response_iteration150.json`;
- `candidate_gravity/C5_CUBIC_RESPONSE_ITERATION150.md`;
- `research_log/2026-08-31_iteration_150_c5_cubic_response.md`.

## New retained rule

### NG-FUNNEL-010 — OFFSHELL_VERTEX_LONGITUDINAL_NULL_IS_NOT_THE_WARD_IDENTITY

A standalone off-shell three-vertex need not vanish when one leg is replaced by a longitudinal pure-gauge tensor. The correct gravitational Ward-Takahashi/Slavnov-Taylor relation includes inverse-propagator and source/contact contributions. Therefore a nonzero isolated replacement is not a consistency FAIL.

Classification: methodological correction / `BLOCKED_WARD_TAKAHASHI_COMPLETION`.

## Exact restart instruction

Resume at **Iteration 151**:

1. derive the correct off-shell gravitational Ward-Takahashi identity in the same `g=eta+kappa h` and source convention;
2. implement the required inverse-propagator/contact/source pieces for the EH sub-block;
3. validate the completed identity numerically on the six frozen probes;
4. if PASS, extend the local C5 tangent beyond the first two curvature-cubic directions or move to the first fixed C3 comparator tangent;
5. keep higher-dimension unsupported and loop/nonanalytic columns explicitly BLOCKED.

No Fisher/resources and no `ANSATZ-003` before a nonzero residual survives the full fixed comparator quotient.
