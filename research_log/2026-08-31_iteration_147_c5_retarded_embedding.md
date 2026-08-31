# RQIR Research Log — Iteration 147

**Date:** 2026-08-31  
**Branch:** Candidate Gravity / fixed C5 retarded comparator  
**Promotion decision:** no `ANSATZ-003` frozen

## Starting authority

Iteration 146 provided a rank-10/10 local-EFT on-shell four-graviton tangent and retained `NG-FUNNEL-006`: an on-shell amplitude tangent is not yet the ordered RQIR `chi^(2)R` tangent.

## Literature check

The retarded-response step was checked against standard perturbative-gravity and Schwinger–Keldysh results. Perturbative gravity supplies the de-Donder propagator and nonlinear graviton vertices; in-in/SK formulations of gravitational initial-value observables generate retarded propagation rather than a Feynman boundary-value prescription. Nonlinear response theory identifies higher response functions with fully retarded ordered objects. These support the causal architecture used below but do not supply the missing finite RQIR projector convention automatically.

## Frozen CTP convention

- D=4 Minkowski background;
- interacting in-vacuum adiabatically connected to the free graviton vacuum;
- de Donder gauge for perturbative evaluation;
- conserved physical source projections;
- linear source coupling `S_J = integral J_A h^A`;
- same Einstein–Hilbert + local parity-even EFT dynamics/order as Iteration 146;
- response legs use the retarded/in-in prescription.

## Derived tree-level result

With equation of motion

`K h + 1/2 V[h,h] + J = 0`,

one has

`h^(1)=-G_R J`

and the exact tree-level second response

`chi2R_A;BC(p;q,r)=-(2pi)^4 delta4(p-q-r) G_R,AA'(p) Gamma3^A'_{B'C'}(p,-q,-r) G_R^B'_B(q) G_R^C'_C(r)`.

This fixes the correct C5 tree-level object to be evaluated for the post-Gaussian comparator.

## New negative/blocking result

**NG-FUNNEL-007 — ON_SHELL_4PT_KINEMATICS_DO_NOT_FIX_OFF_SHELL_RETARDED_3PT.**

The Iteration-146 frozen data `(s,t,u,phi)` describe an on-shell 2-to-2 four-graviton amplitude. They do not uniquely determine the off-shell 1-output/2-input response data required by `chi2R`: `p^2,q^2,r^2`, energy routing, three conserved tensor projectors, smearing/window normalization, or the scalar `chi2R_even/odd` map.

Therefore no numerical `V_C5^(chi2R)` rank is assigned. The state is `BLOCKED_PROTOCOL_UNDERSPECIFIED`, not zero and not a C5 consistency FAIL.

## Other rows

`N2`, `C3sym`, and loop/nonanalytic C5 contributions remain BLOCKED pending derivation in the same CTP and renormalization convention.

## Reproducibility

- `analysis/c5_retarded_embedding_iteration147.py`;
- `results/c5_retarded_embedding_iteration147.json`;
- `candidate_gravity/C5_RETARDED_EMBEDDING_ITERATION147.md`.

## Consequence

No algebraic residual exists after a complete fixed comparator quotient. Fisher/resources remain forbidden and `ANSATZ-003` remains withheld.

## Next gate

Iteration 148: freeze explicit finite off-shell conserved-source/projector/smearing coordinates for `chi2R_even/odd`, evaluate the EH plus contributing local-EFT cubic vertex contractions, perform a Ward/gauge-null test, and compute the first actual C5 retarded rank/SVD certificate.
