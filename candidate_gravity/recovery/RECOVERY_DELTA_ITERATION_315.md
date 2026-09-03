# RQIR Candidate Gravity Recovery Delta — Iteration 315

Date: 2026-09-03

MODEL_READINESS: 24%

## Authoritative predecessor
Iteration 314 located all same-parent derivation prerequisites but did not derive executable determinant components.

## Iteration 315 result
The ghost determinant sublayer was derived from the frozen minimal FP operator `N^alpha_beta = delta^alpha_beta Box + R^alpha_beta` at `D=4, Lambda=0, a=-1/2`.

Validated provenance:
- run `33713975395`
- head/workflow commit `4997efbcf4ce198cad98a047ae1bc2dc10390513`
- code commit `389dc70eb76770fd36b89f0a662730df3f56c501`
- artifact `9877851387`
- artifact digest `sha256:644413a787083f35916eb7f22454cf7163c0a64fdcd25b095c5d637cfd302115`
- scientific JSON SHA-256 `0e31d3a123ceb45b5c305e0a68b78712b59abad6d3febc24a9033c263a21c826`
- one top-level JSON object, sentinel `315`.

Freeze:
`PASS_GHOST_N123_GEOMETRIC_RECURSION_PRINCIPAL_PLUS_RICCI__COVARIANT_BOX_CONNECTION_ROUTING_REMAINS_BLOCKED`.

Validated max absolute errors by order n=0..3:
`[8.283688954807686e-12, 9.73450209329485e-11, 1.1025703905076512e-4, 6.288007404791074e-4]`, all below frozen thresholds `[1e-9, 2e-6, 2e-3, 2.0]`.

Derived and validated: inverse-metric recursion, Levi-Civita connection recursion, Ricci recursion, mixed-Ricci recursion, and ghost principal symbol.

Still BLOCKED: full vector covariant-Box connection routing and therefore full routed physical `N1/N2/N3`; graviton `H1/H2/H3` unchanged BLOCKED.

Iteration 316, already launched as the dependent routing gate, failed before schema audit and artifact upload. With no schema-valid diagnostic artifact it is an operational failure only, not a scientific FAIL. Do not weaken thresholds.

## Exact next gate
Repair the Iteration-316 execution contract so that raw diagnostics and schema-valid JSON are preserved before a nonzero exit, then perform exactly one rerun of the routed vector covariant-Box completion. Only after full ghost authority passes should the determinant branch advance to graviton `H1/H2/H3`.

MODEL_READINESS: 24%
Change from Iteration 314: `0 pp`; a scoped ghost derivation sublayer closed, but no readiness-rubric component or robust comparator-subtracted residual closed.
