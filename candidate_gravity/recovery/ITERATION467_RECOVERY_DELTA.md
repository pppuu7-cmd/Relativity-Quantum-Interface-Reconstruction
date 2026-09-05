# Iteration 467 Recovery Delta

Date: 2026-09-05

## Entry authority
Latest authoritative research/numerical iteration at entry: 466. Physical/operator authority remains 411. Physical blocker authority remains 421 with unresolved set `[2]`.

Canonical rank-6 run `33968129883` at `u=-5e-6, v=+5e-6` was rechecked and remains `in_progress`; no duplicate heavy run was launched.

## New exact result
Frozen central4 coefficients obey exact antisymmetry `c(-x)=-c(x)`. Therefore tensor weights obey `w(-u,v)=-w(u,v)`, `w(u,-v)=-w(u,v)`, and `w(-u,-v)=w(u,v)`.

The tensor mixed derivative consequently annihilates the even-even, even-odd, and odd-even parity sectors exactly for arbitrary stencil data and retains only the odd-odd sector. The canonical 16-term weighted sum is algebraically identical to four signed quartets over positive node magnitudes:

`F(+a,+b)-F(-a,+b)-F(+a,-b)+F(-a,-b)`

with dimensionless coefficients `4/9`, `-1/18`, `-1/18`, `1/144` for `(a,b)=(1,1),(1,2),(2,1),(2,2)` respectively, followed by the common `1/h^2` scaling.

Classification: `PASS_CENTRAL4_EXACT_ODD_ODD_PARITY_PROJECTOR__NON_PROMOTING`.

Scope is exact algebra / implementation provenance only. No `u<->v` identity is assumed or created; Iteration 454 remains binding. No support point is deduplicated. No physical estimator, dynamics, threshold, or mass-step convention changes.

After all 28 distinct support coordinates are locally certified, BASE and HALF canonical 16-term assemblies at MP80 and MP120 must additionally be cross-checked against the exact four-quartet representation. A mismatch beyond explicitly bounded arithmetic roundoff is implementation/provenance `BLOCKED`, not physics FAIL. This supplements, and does not replace, Iteration-458/460/462 gates.

Reproducible files:
- `candidate_gravity/code/iteration467_central4_parity_projector_audit.py`
- `candidate_gravity/results/iteration467_central4_parity_projector_audit.json`

`MODEL_READINESS: 24%`

Readiness change: 0 pp; exact assembly provenance strengthened, but no stable readiness-rubric component closed.

## Exact next gate
Raw-consume run `33968129883` fail-closed at Iteration-455 distinct rank 6, `u=-5e-6, v=+5e-6`. PASS permits only rank 7 `u=-5e-6, v=+1e-5`; BLOCKED requires localization of the first failing sample at rank 6. No later coordinate may be launched before raw consumption.
