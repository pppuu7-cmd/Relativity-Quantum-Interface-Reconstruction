# RQIR Candidate Gravity — Iteration 315

Date: 2026-09-03

MODEL_READINESS: 24%

Iteration 315 derives the same-parent ghost sublayer from the frozen minimal FP operator `N^alpha_beta = delta^alpha_beta Box + R^alpha_beta` at `D=4, Lambda=0, a=-1/2`, around `g=eta+kappa h`.

Validated provenance: run `33713975395`, head `4997efbcf4ce198cad98a047ae1bc2dc10390513`, code `389dc70eb76770fd36b89f0a662730df3f56c501`, artifact `9877851387`, digest `sha256:644413a787083f35916eb7f22454cf7163c0a64fdcd25b095c5d637cfd302115`, scientific JSON SHA-256 `0e31d3a123ceb45b5c305e0a68b78712b59abad6d3febc24a9033c263a21c826`, one top-level object, sentinel `315`.

Freeze:
`PASS_GHOST_N123_GEOMETRIC_RECURSION_PRINCIPAL_PLUS_RICCI__COVARIANT_BOX_CONNECTION_ROUTING_REMAINS_BLOCKED`.

Validated maximum absolute errors by order n=0..3 are `[8.283688954807686e-12, 9.73450209329485e-11, 1.1025703905076512e-4, 6.288007404791074e-4]`, all below the frozen thresholds `[1e-9, 2e-6, 2e-3, 2.0]`.

The derived contract covers inverse-metric recursion, Levi-Civita connection recursion, Ricci recursion, mixed Ricci, and the ghost principal symbol. It does NOT yet include the full vector covariant-Box connection routing, so the full physical `N1/N2/N3` is still BLOCKED. Graviton `H1/H2/H3` remains BLOCKED.

Iteration 316 was already launched as the dependent covariant-Box routing gate and completed with workflow failure before schema audit or artifact upload. Because no schema-valid diagnostic artifact exists, that event is classified only as operational failure, not scientific FAIL; frozen thresholds are not weakened.

Exact next gate: repair the Iteration-316 execution contract so failure preserves raw diagnostics and a schema-valid result, then perform exactly one rerun of the full routed vector covariant-Box ghost completion. Only after that sublayer passes may the determinant branch advance to graviton `H1/H2/H3`.

MODEL_READINESS: 24%
Change from Iteration 314: `0 pp`; a ghost sublayer closed, but no readiness-rubric block or robust comparator-subtracted residual closed.
