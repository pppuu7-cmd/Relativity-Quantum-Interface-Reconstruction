# Research log — RQIR Candidate Gravity Iteration 226

Date: 2026-09-01

MODEL_READINESS: 24%

Started from repository authority, not chat state: `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_225.md`, the Iteration-225 research log, recent commits, and GitHub Actions state. The authoritative front was Iteration 225. No active Actions runs were present.

Iteration 225's `MSSC-001` physics and numerical authority was kept frozen: source model/convention unchanged; Born-fixed subtraction `R=-8 M_Born`; singularity-adapted two-cell Voronoi cubature; conservative relative numerical envelope `3e-7`.

Iteration 226 defined the source transfer coordinate `z=-t/(4 p^2)=sin^2(theta_ext/2)` and evaluated a comparator-only forward grid `theta_ext=[0.13,0.105,0.085,0.068,0.054,0.043,0.034,0.027]` for both external linear spin-2 polarizations. No Candidate Gravity residual or ansatz data were used.

All 16 forward rows pass the frozen numerical gate. The worst relative disagreement between the two independent cubatures is `2.595262029909852e-7 < 3e-7`.

The declared six-column regular+log basis `[1,L,z,zL,z^2,z^2L]`, `L=log(z)`, was compared with an equal-parameter analytic degree-5 Taylor control. On all eight rows:

- plus: regular+log relative L2 residual `1.73176347744811e-8`; Taylor-5 `5.180431884151699e-11`;
- cross: regular+log relative L2 residual `6.991589330814055e-10`; Taylor-5 `1.6502718029550426e-12`.

The analytic control is therefore already much better than required by the frozen numerical envelope. This does not prove exact analyticity; it prevents certification of a nonzero log coefficient on this regime/window.

Conservative row-envelope propagation through the regular+log pseudoinverse gives `|b_i|/Delta b_i < 1` for every log coefficient in both polarizations. The largest ratio is the plus `b2` value `0.9745719940266064`; cross ratios are at most `0.03769973874474194`. No log coefficient is promoted.

Classification: `REGIME_SPECIFIC_NON_IDENTIFIABILITY_NO_CERTIFICATE` plus analytic-vs-log near-degeneracy inside the numerical envelope. This is not a consistency FAIL, not an exact comparator identity, and not Candidate Gravity novelty.

The separate pure-graviton positive control from Iteration 215 remains structurally different: its equal-parameter Taylor residual was `2790.180298263071` times the control's numerical envelope, so its regular+log structure is resolved. The source/control difference is not itself a Candidate Gravity residual because they are distinct observables.

Retain `SRC-CUT-007`, `SRC-CUT-008`, `REL-NG-005`, `NG-FUNNEL-082` as defined in the Iteration-226 note/certificate.

No `ANSATZ-003`. No Fisher/resources. No heavy Actions run was needed or duplicated.

MODEL_READINESS: 24%

Readiness change: 0 percentage points. Comparator foundation remains `24/25`; robust unique residual remains `0/20`; parent dynamics/ANSATZ and downstream candidate-specific blocks remain zero. The iteration resolves a classification question but does not close a new rubric point.

Next gate: return to missing comparator authority. Audit asymptotic-safety Lorentzian/in-in nonlinear linked-cut authority under the same source-completed standard. If still unavailable, retain the exact operational blocker and proceed to C3 ordered metric-CTP nonlinear completion. Never zero-fill AS/C3.
