# Candidate Gravity Recovery Delta — Iteration 408

Date: 2026-09-04

MODEL_READINESS: 24%

## Fresh source-of-truth audit

At entry, `candidate_gravity/recovery/CURRENT_QG_FRONT.md` names Iteration 406 as the latest validated Candidate Gravity authority and Iteration 407 run `33835806522` as the active physical channel-4 analytic/spectral reduction. The latest Iteration-407 recovery, research log and recent commits were read before any new work. Iteration 407 remains in progress in its scientific step and was not duplicated.

## Independent scientific step

Iteration 408 adds a STRUCTURE-ONLY oracle for the two remaining double-double blockers not covered by the raw Iteration-401 channel-4 oracle: global indices 2 (class 3, q^2=-1) and 11 (class 16, q^2=-0.34). This does not compute or promote either physical D_s value and does not assume that Iteration 407 will converge.

The oracle binds exactly the same prospectively frozen structural contract used by Iteration 401: after the two multiplicity-two cut groups, require exactly one multiplicity-one uncut denominator; align a transverse axis to its shift; directly verify denominator affinity in z and phi-independence; test Fourier tail above |m|=8; compare two independent phi phases; and fit the azimuth mean on training z nodes with held-out z validation over candidate degrees 4,6,8,10,12. Thresholds remain `2e-11` for denominator affinity and `2e-6` for phase mean, Fourier tail and held-out polynomial error. The parent physical integrand, central4 x central4 mass stencil, sign/normalization and physical `2e-5` convergence threshold are unchanged.

Code commit: `38d800418bdda1fdaa52edbb94ffc0277813aa99`. Workflow/launch commit: `66381c31d63038093f1fa1bb859fb635abe46612`. Run: `33839449598`. Until its raw artifact and independent authority audit complete, no structural PASS/FAIL is promoted.

## Authority and guardrails

Latest validated Candidate Gravity authority remains Iteration 406. Exact unresolved double-double physical set remains `[2,4,11]`. Iteration 408 cannot remove any member because it is structure-only. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No Source/Born subtraction and no threshold weakening.

MODEL_READINESS: 24%

Change: 0 pp. This iteration can only close structural executability for blockers 2 and 11; it cannot close a stable readiness-rubric bucket or create a comparator-subtracted residual.

## Exact next gate

Raw-consume Iteration 408 fail-closed. Independently raw-consume Iteration 407 when complete. Only if Iteration 407 physically converges and the corresponding blocker-2/11 structure oracle passes may the same frozen analytic/spectral physical reduction be executed separately for indices 2 and 11 with held-out original-integrand cross-checks. Otherwise preserve the scoped BLOCKED result and diagnose the failed structural or mass-step component without weakening thresholds.
