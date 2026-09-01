# Research log — RQIR Candidate Gravity Iteration 224

Date: 2026-09-01

MODEL_READINESS: 23%

Started from repository authority: `CURRENT_QG_FRONT.md`, `RECOVERY_DELTA_ITERATION_223.md`, the latest Iteration-223 research log, recent commits, and Actions state. No active GitHub Actions were present. The authoritative scientific front was Iteration 223.

The Iteration-222 Born-fixed subtraction `R=-8 M_Born` was kept unchanged. The Iteration-223 local cap result (`delta^2` vanishing of Born-subtracted cap shells) was treated as frozen authority.

This iteration tested whether the global cap-excised `MSSC-001` hard remainder is already numerically stable. Two deterministic spherical decompositions were compared: laboratory `mu x phi` Gauss-Legendre/midpoint grids and the same rule in a fixed chart rotated by `0.371 rad`, at `N={12,16,20}` and cap radii `delta={0.08,0.04}` across five external angles and both linear spin-2 polarizations.

The finest-grid chart disagreement ranges from `3.10e-4` to `1.3819475e-1`. The worst case is `theta_ext=0.45`, cross polarization, `delta=0.04`, where the two charts give `49.0040889813` and `56.8621379324`.

Classification: `BLOCKED_NUMERICAL_BULK_HARD_REMAINDER`. This is operational/numerical BLOCKED, not a consistency FAIL, not exact comparator identity, not near-degeneracy, and not evidence for Candidate Gravity novelty. The Iteration-223 local IR completion remains retained.

Retain `NUM-NG-013`, `SRC-CUT-005`, `NG-FUNNEL-080`.

No `ANSATZ-003`. No Fisher/resources. No heavy Actions run was duplicated.

MODEL_READINESS: 23%

Readiness change: 0 percentage points. The global numerical blocker has been localized, but no model-readiness rubric block closes.

Next gate: singularity-adapted domain decomposition with the two certified cap neighborhoods treated in local polar coordinates and two independent high-order cubatures on the smooth cap-excised bulk. Freeze a finite source hard remainder only after common convergence within a declared numerical envelope.
