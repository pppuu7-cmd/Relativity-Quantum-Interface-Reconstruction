# RQIR Candidate Gravity — Iteration 330

Date: 2026-09-03

## Result

`FAIL_SCOPED_GATE_DESIGN_CLOSED_TARGET_INCORRECTLY_REQUIRED_NONZERO__PHYSICAL_NUMERATOR_MAPS_PASS`

Validated Action run `33742740272`, job `100608154572`, artifact `9888378042`, digest `sha256:368ea05e9fbef3ec4c3aa9907290aebfc8f208e97bf07f3d2744269bf2541c76`.

The fail-closed workflow preserved a schema-valid scientific JSON before final enforcement. All 13 physical cubic routes were assembled from frozen Iteration-312 weights, Iteration-324 shifted routing and Iteration-329 common-parent H/N. Canonical family census was `1 singleton + 3 bubbles + 1 signed-affine triangle`. Held-out denominator-map and route-specific numerator reconstruction errors were respectively `1.1102230246251565e-16` and `1.3877787807814457e-17`, far below the frozen `5e-10` threshold.

The only failed condition was an auxiliary meta-check applying `qdiff_nonzero` to every nonzero subindex including the full target `(1,1,1)`. On the exact closed triad, `q(1,1,1)=q1+q2+q3=0` by construction. Nonzero external denominator differences are required only for proper nonzero subindices. Therefore Iteration 330 is preserved as a scoped gate-design FAIL, not rewritten into a PASS.

This is not a Candidate Gravity consistency FAIL, H/N kernel FAIL, comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty result.

MODEL_READINESS: 24%

Change from Iteration 329: `0 pp`. No stable readiness-rubric bucket or robust comparator-subtracted residual closed.

## Exact next gate

Issue a new gate version changing only the logically incorrect proper-subindex meta-check. Parent dynamics, topology weights, loop maps, held-out points and numerical threshold must remain frozen.
