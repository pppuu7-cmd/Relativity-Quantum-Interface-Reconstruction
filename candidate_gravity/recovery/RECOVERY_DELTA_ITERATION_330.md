# RQIR Candidate Gravity — Recovery Delta Iteration 330

Date: 2026-09-03

## Authoritative result

`FAIL_SCOPED_GATE_DESIGN_CLOSED_TARGET_INCORRECTLY_REQUIRED_NONZERO__PHYSICAL_NUMERATOR_MAPS_PASS`

Run `33742740272`, job `100608154572`, artifact `9888378042`, digest `sha256:368ea05e9fbef3ec4c3aa9907290aebfc8f208e97bf07f3d2744269bf2541c76`.

The workflow preserved schema-valid diagnostics. All physical route maps and held-out numerator reconstructions passed; only the auxiliary nonzero-momentum assertion was malformed because it included the full closed target `(1,1,1)` whose total momentum is exactly zero.

Frozen numerical observations: 13 sequences; family census `1 singleton + 3 bubbles + 1 signed-affine triangle`; maximum denominator-map error `1.1102230246251565e-16`; maximum route reconstruction error `1.3877787807814457e-17`; unchanged threshold `5e-10`.

Typed interpretation: scoped gate-design FAIL only. Do not reinterpret as Candidate Gravity consistency FAIL or H/N failure. Preserve Iteration 330 unchanged and fix via a new gate version.

MODEL_READINESS: 24%

Change from Iteration 329: `0 pp`.

## Exact next gate

New version excluding only the full closed TARGET from the proper-subindex nonzero check, with all physics, topology, loop maps, held-out points and thresholds unchanged.
