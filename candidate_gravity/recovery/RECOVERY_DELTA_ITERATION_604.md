# Recovery Delta — Iteration 604

Date: 2026-09-08

Iteration 604 prospectively froze the finite-lattice boundary/convergence rule before any new production Ward result and is now independently raw-consumed PASS, contract-only/non-residual.

Canonical provenance:
- run `34242971065`;
- head `e745984401f6e572f8077a2e4ecff222f73c4728`;
- artifact `10062757495`, digest `sha256:5457f02b088800b849afce2d21e099435e99cb3f450173f3d6da8e686b4a8895`;
- raw `result.json` SHA-256 `f6c926e16f8205dc6c4fc3e8c67afcf0b2dd91eff09aab8371fd6eb0687fa909`;
- raw `authority_audit.json` SHA-256 `98bc03c661f4b219e26e5e19aef48af2048f0624f89eba038c6eecd3e4c1d639`;
- raw audit `PASS_RAW_AUDIT_ITER604_PROSPECTIVE_LATTICE_CONTRACT`, `failures=[]`.

Frozen production rule: radii `R=4,5,6`; original FD steps `(2e-2,1e-2,5e-3)`; unchanged Ward absolute tolerance `2e-6`; unchanged final FD-step tolerance `2e-5`; separate `|W_R6-W_R5|<=2e-6`; all 12 one-leg anchors `<=2e-11` at R5/R6; complete 13-family assembly cross-check `<=2e-5`. Radius/FD nonconvergence is fail-closed `BLOCKED_CONVERGENCE`; a converged above-threshold row is `FAIL_WARD`. No condition-number waiver is permitted.

Iter602 remains preserved historical FAIL and Iter603 remains diagnostic/non-promoting. Iter604 does not change MODEL_READINESS.

Exact next gate: Iter605 production rerun of the unchanged full source-level nonlinear Ward identity under this contract, followed by independent raw artifact consumption.

No Source/Born subtraction, source-to-Iter582 mapping, comparator quotient, ANSATZ-003 or Fisher/resources are authorized.

MODEL_READINESS: 24%
