# Candidate Gravity Research Log — Iteration 362 (active)

Date: 2026-09-03

Iteration 362 is the fail-closed method-validation gate authorized by Iterations 359 and 361. It does not integrate any physical repeated-pole U2 channel. It validates the unique-double-pole auxiliary-mass derivative prescription with the same `i0` against an independent smooth-test-function direct regularized distribution oracle.

Frozen identity: `1/(D+i0)^2 = - d/d(mu^2)[1/(D+mu^2+i0)]|_{mu^2=0}`. The independent sign oracle uses `Disc[(x+i0)^-2] = 2*pi*i*delta'(x)`, acting on a smooth test function as `-2*pi*i*phi'(0)`.

The implementation compares a central auxiliary-mass derivative against the analytic distribution action and independently compares a direct finite-eta squared-pole discontinuity integral with Richardson extrapolation. Thresholds are fixed before the run; failure leaves physical repeated-pole integration BLOCKED.

Code commit: `a07e846729b6a90fcf14a625108e3a57e3cc575f`. Workflow head: `160acc4351a5e0e2d42569fb8f6b702b7dbe25a7`.

Active Actions run: `33800631629`, workflow `rqir-iteration362-u2-repeated-pole-distributional-oracle`.

Scientific authority remains Iteration 361 until raw Iteration-362 artifact and sentinel/schema audit validation.

MODEL_READINESS: 24%