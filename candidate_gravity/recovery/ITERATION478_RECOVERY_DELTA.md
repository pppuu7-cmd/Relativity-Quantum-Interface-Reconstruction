# Iteration 478 Recovery Delta

Date: 2026-09-06

## Authority retained
Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421 (`BLOCKED_CONVERGENCE`), exact unresolved physical set `[2]`. Iteration 475 remains latest completed numerical mass-support authority. Certified occurrence-weighted mass precision coverage remains `15/32 = 46.875%` (`1200/2560`).

## New raw-valid research/provenance authority
Completed post-477 frozen-basis geometry MP run `33992073492`, job `101375971739`, artifact `9976943399` was raw-consumed rather than inferred from workflow colour.

Artifact digest: `sha256:8b853b49a040d4f0eef99b0aaeedd427f657b8fda47dc49707b639566977f473`.
Scientific JSON SHA-256: `77a334ba3de6812c0bb3b37bd403fb7e71884c5a27de13bdf31cc46f01b1f614`.

Across all 28 distinct mass coordinates, five training-z values, NPHI16, three radial h values and both radial signs (`13440` samples):
- all finite;
- max MP80↔MP120 scaled geometry discrepancy `3.2476704251336853442545536696e-81 <= 1e-30`;
- max binary64↔MP120 scaled geometry drift `3.55401690420536569154467606735e-16`;
- binary geometry drift is non-material relative to diagnostic `2e-6` and `2e-5` reference scales.

Classification: `PASS_FROZEN_BASIS_GEOMETRY_ARITHMETIC_MP80_MP120__BINARY_DRIFT_DIAGNOSTIC_ONLY_NON_PROMOTING`.

Scope is deliberately narrow: arithmetic for `alpha,rho,beta,p,cc,aa` using frozen Iteration431/407 source vectors/basis treated as exact decimal inputs. This does not certify arbitrary-precision reconstruction of `e1,e2,e3` or upstream vectors, does not certify final full-F assembly, and does not promote physical double-double index 2.

## Active heavy gate / anti-idle state
Canonical Iteration-455 distinct rank 11, `u=+5e-6, v=+1e-5`, run `33989317870`, job `101368577097`, remained `in_progress` at consume time on the scientific MP stage. It is the sole permitted heavy numerical gate and was not duplicated.

Raw-consume rank 11 fail-closed after completion. PASS permits only the next UNTESTED frozen Iteration-455 manifest coordinate. BLOCKED requires localization of the first failing rank-11 `z/phi/radial` sample without changing thresholds, precision, dynamics, routing or support order.

`ANSATZ-003` remains uncreated. Comparator-subtracted residual and Fisher/resources remain BLOCKED.

MODEL_READINESS: 24%

Readiness change: **0 percentage points**.
