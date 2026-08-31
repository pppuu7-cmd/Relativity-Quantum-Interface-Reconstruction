# Recovery Delta — RQIR Iteration 152

**Date:** 2026-08-31  
**Authoritative change:** both existing local curvature-cubic C5 columns now pass their correct operator-specific completed Ward/diffeomorphism validation on the frozen six-probe protocol.

## Previous front
Iteration 151 closed the Einstein-Hilbert off-shell Ward/source-contact blocker but left the two curvature-cubic columns as `PASS_SCOPED_TT_ONLY` pending their own validation.

## New result
For `Tr(Ricci^3)` and cyclic `Riemann^3` about flat space, the operator-specific quadratic term vanishes. Therefore the cubic diffeomorphism identity reduces to `B3[L_xi,e2,e3]=0` for each gauge-replaced leg.

Across all six frozen probes and all three legs:
- max `|R^(1)[L_xi]| = 2.220446049250313e-16`;
- max `|Riemann^(1)[L_xi]| = 5.551115123125783e-17`;
- max `|B3_Ricci3| = 2.4454568146171362e-17`;
- max `|B3_Riemann3| = 7.549184413398274e-17`.

Both columns are therefore `PASS_SCOPED`; the existing local `V_C5^(chi2R)` remains shape `6x2`, rank `2/2`, and is upgraded to `PASS_SCOPED_WARD_VALIDATED`.

Authorities:
- `analysis/c5_curvature_cubic_ward_iteration152.py`;
- `results/c5_curvature_cubic_ward_iteration152.json`;
- `candidate_gravity/C5_CURVATURE_CUBIC_WARD_ITERATION152.md`;
- `research_log/2026-08-31_iteration_152_c5_curvature_cubic_ward.md`.

## Exact restart instruction
Resume at **Iteration 153**:
1. instantiate the first fixed finite C3 comparator tangent, not a class-capability mask;
2. freeze one explicit covariant classical-quantum stochastic action, parameter convention, state/noise prescription and post-Gaussian coordinate map;
3. derive all supported `J/N/chiR/C3/chi2R/soft/Ward` entries from that one dynamics and mark unsupported objects BLOCKED, never zero by assumption;
4. do not start Fisher/resources or `ANSATZ-003` before a nonzero algebraic residual survives fixed C3/C4/C5/nonlocal/AS quotienting.
