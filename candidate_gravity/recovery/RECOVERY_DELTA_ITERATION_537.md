# RQIR Candidate Gravity — Recovery Delta Iteration 537

Date: 2026-09-07

## Authority advanced
Iteration 537 adds an exact conditioning audit for the already frozen Iteration-536 h4/h6 truncation-component inversion.

For `[d1,d2]^T=M[A,B]^T` with

`M=[[15/16,63/64],[15/256,63/4096]]`,

`det(M)=-2835/65536 != 0`, and

`M^{-1}=[[-16/45,1024/45],[256/189,-4096/189]]`.

The exact unscaled Euclidean condition number in `[A,B]` coordinates is

`kappa_2(M)=sqrt((31064193+sqrt(962877176430849))/(31064193-sqrt(962877176430849)))`

`≈42.7789181466055467416`.

Classification: `PASS_ITER424_H4_H6_INVERSION_CONDITIONING_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

Reproducible code: `candidate_gravity/code/iteration537_iter424_h4_h6_inversion_conditioning_exact_audit.py`.
Machine-readable authority: `candidate_gravity/results/iteration537_iter424_h4_h6_inversion_conditioning_exact_audit.json`.

## Scope/guardrails
This is not the Iteration-531 stencil-row conditioning result. Normalized BASE/HALF/QUARTER rows remain well conditioned (`kappa_2≈1.04378`), while the separate h4/h6 coefficient inversion is more sensitive (`kappa_2≈42.78`) in the stated unscaled coefficient convention. The latter is diagnostic and coordinate/convention dependent; it is not promoted to model-level near-degeneracy.

No dynamics, parameter convention, mass nodes, precision, thresholds, successor order, or physical acceptance clauses changed. No physical promotion follows. No Candidate-Gravity consistency FAIL, exact comparator identity, regime-specific non-identifiability, model-level near-degeneracy, or novelty certificate is claimed. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.

## Active computation
Canonical QUARTER rank2 run `34102627559`, job `101680313500`, remained the unique authorized heavy computation and was still `in_progress` during this iteration. No duplicate was launched.

## Authority ledger
Physical/operator authority: Iteration 411.
Physical blocker: Iteration 421, unresolved `[2]`.
BASE/HALF support: Iteration 523 (`32/32`).
BASE/HALF assembly: Iteration 527.
Quarter manifest: Iteration 529.
Three-level Gram: Iteration 530.
Normalized stencil conditioning: Iteration 531.
Quarter successor order: Iteration 532.
Truncation diagnostic: Iteration 533.
Quarter rank1 raw-consumption: Iteration 534.
Rank2 launch: Iteration 535.
Three-level h4/h6 component inversion: Iteration 536.
H4/h6 inversion conditioning: Iteration 537.
Latest authoritative research iteration: Iteration 537.

MODEL_READINESS: 24%
Readiness change: 0 percentage points. A genuine diagnostic-conditioning subgate was closed, but no additional stable model-level rubric sector is complete.

## Exact next gate
Wait for canonical rank2 run `34102627559` to terminate, then raw-consume its artifact fail-closed. Raw-valid PASS authorizes only frozen rank3 `(-1.25e-6,-2.5e-6)` from the Iteration-532 order.
