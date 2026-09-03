# RQIR Candidate Gravity — Iterations 311–312

Date: 2026-09-03

MODEL_READINESS: 24%

Iteration 311 preserved a valid diagnostic artifact but failed its small-|t| degree-6 polynomial-fit audit. Inspection shows numerical ill-conditioning of the cubic extraction rather than evidence against the exact logdet expansion. The failure remains recorded and is not relabelled PASS.

Iteration 312 independently re-audits the same frozen cubic identity with 80-digit arithmetic, a symmetric cubic-coefficient stencil and Richardson cancellation of the leading O(h^2) contamination.

Validated Iteration-312 provenance: run `33710153241`, job `100507684815`, head `18dbff26a90266d3d21848263176d3015537e048`, artifact `9876618078`, artifact digest `sha256:5ca0bc6d200a0c8e48f4a799f695442970b9b4f53406fca7f515732ca7d43bca`, scientific JSON SHA-256 `ec5ff14b1944cafb76f31faeb6f6e6861516efb90ff0f4f84ff68f742c121553`; sentinel 312 and authority schema PASS.

Frozen coefficient:

`Tr(G0 H3) - 1/2 Tr(G0 H1 G0 H2) - 1/2 Tr(G0 H2 G0 H1) + 1/3 Tr((G0 H1)^3)`.

Classification:

`PASS_DETERMINANT_E0C3_EXACT_CUBIC_LOGDET_OPERATOR_TOPOLOGY_HIGH_PRECISION_AUDIT__PHYSICAL_COMPONENTS_REMAIN_BLOCKED`.

The high-precision cubic residual is approximately `3.56e-11` against a `1e-9` threshold. Same-parent graviton H1/H2/H3 and ghost N1/N2/N3 component kernels are not supplied by this gate and remain BLOCKED rather than zero-filled. No candidate residual is produced.

Exact next gate: repository-authority inventory for those physical component formulas/routing, with explicit provenance or typed BLOCKED output.

MODEL_READINESS: 24% — unchanged.
