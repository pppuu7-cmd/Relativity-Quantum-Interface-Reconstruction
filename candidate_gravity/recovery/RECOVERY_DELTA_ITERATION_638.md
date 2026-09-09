# RECOVERY DELTA — Iteration 638

Date: 2026-09-09

Authoritative predecessor: Iter637, which raw-validly left the Iter636 exact-fixture anchor BLOCKED under a committed-JSON-only selector.

Iter638 audits committed same-parent code provenance and uniquely recovers the frozen three-mode fixture. Iter368 explicitly fixes `LEGS=('s','a','b')` and vectors `q_s=(1,0,0,0)`, `q_a=(-0.4,0.1,0.1,0)`, `q_b=(-0.6,-0.1,-0.1,0)`. Iter588 explicitly re-executes the Iter368 setup prefix and inherits `M=ns['M']`, binding that fixture through the Iter582 parent chain rather than retyping kinematics. In physical `+---` signature this yields `(s0,t0,u0)=(1,0.14,0.34)` with exact momentum closure.

Classification: `PASS_ITER638_UNIQUE_SAME_PARENT_EXACT_FIXTURE_ANCHOR_RECOVERED_FROM_COMMITTED_CODE__NON_RESIDUAL`.

Raw authority: run `34293646233`, job `102285415240`, head `1bdc8fb40a4f369c006c7f42f4d368a71cb0166f`, artifact `10082281625`, digest `sha256:95ed469a705250ea341873d493dec4eb04c199c674c091cefdf07b11072c297e`; independent raw consumption gives result SHA-256 `cbf27355a5d3a6bc83163cebf889188b526cb1699ef6e299190bf296de72e0ec`, audit SHA-256 `ee011c75cf6c8390ddd682607ebc626744975e01a84ad171a653ee8078e29dc6`, `failures=[]`.

Run `34293593003` is non-authoritative implementation noise: its evaluator passed, but its audit used exact floating equality for `u0`. The canonical V2 changed only that audit comparison to `abs_tol=2e-15`; no scientific inputs or acceptance gates changed.

Frozen guardrails: all 13 source families retained; `zero_fill=false`; Candidate values unused; Source/Born subtraction `NOT_PERFORMED`; native projection `NOT_PERFORMED`; no comparator quotient; no ANSATZ-003; no Fisher/resources.

MODEL_READINESS: 24%
Readiness change: 0 percentage points.

Exact next gate: Iter639 evaluates the already prospectively frozen Iter636 scalar-denominator geometry at fixed `t0=0.14`, `u0=0.34`, `m_phi=0.7`: K1/K2 equal-mass bubble threshold in the s-channel and K1^3 equal-mass triangle leading Landau determinant with positive-Feynman-parameter support. Negative/no-positive-support results must be retained; no native projection or Source/Born subtraction is authorized by this gate alone.
