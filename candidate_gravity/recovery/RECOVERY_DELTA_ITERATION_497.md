# RECOVERY DELTA — ITERATION 497

Date: 2026-09-06
MODEL_READINESS: 24%

## New exact assembly/provenance authority
Frozen mixed central4 coefficients obey `c(-x)=-c(x)`, hence tensor weights satisfy `w(-x,y)=-w(x,y)`, `w(x,-y)=-w(x,y)`, and `w(-x,-y)=w(x,y)` exactly.

For arbitrary sampled data define `F_oo(x,y)=[F(x,y)-F(-x,y)-F(x,-y)+F(-x,-y)]/4`. Exact coefficient comparison gives `D_h[F]=D_h[F_oo]`. Therefore every even-in-x or even-in-y sector is annihilated exactly, and the 16-sample signed assembly is exactly reducible to four positive-quadrant odd-odd orbit differences.

Classification: `PASS_CENTRAL4_ODD_ODD_PARITY_PROJECTION_EXACT__NON_PROMOTING`.

Scope is estimator/assembly provenance only. A violation is implementation/provenance `BLOCKED`, not Candidate-Gravity consistency FAIL. No frozen threshold, dynamics, source-order, BASE/HALF, or `ds=-d_base` convention changed.

Reproducible audit: `candidate_gravity/code/iteration497_central4_odd_odd_parity_projection_audit.py`.
Result: `candidate_gravity/results/iteration497_central4_odd_odd_parity_projection_audit.json`.

## Active numerical gate
Frozen manifest rank18 `(u,v)=(-2.5e-6,-5e-6)`, multiplicity 1, canonical run `34029482604`, job `101476261793`, remains `in_progress`. No duplicate heavy run was launched. Certified occurrence coverage remains `22/32 = 68.75%`, i.e. `1760/2560` rows.

## Retained blockers
Physical/operator authority remains Iteration 411. Iteration 421 remains raw-valid `BLOCKED_CONVERGENCE`, unresolved set `[2]`. Robust comparator-subtracted residual is absent. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.

## Readiness
MODEL_READINESS: 24%
Readiness change: 0 percentage points. The parity/projection gate is a real exact provenance closure but completes no new stable-rubric component.

## Exact next gate
Fail-closed raw-consume rank18 run `34029482604`. Only raw PASS permits rank19 `(-2.5e-6,-2.5e-6)` under unchanged frozen conventions; BLOCKED requires first-failure localization without threshold weakening or zero-fill.
