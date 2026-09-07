# RQIR Candidate Gravity — Recovery Delta Iteration 536

Date: 2026-09-07

## Authority advanced
Iteration 536 adds an exact, diagnostic-only three-level truncation-error component inversion for the already frozen BASE/HALF/QUARTER central4 hierarchy.

With `X_h=D+A+B+C+O(h^10)`, `A=a h^4`, `B=b h^6`, `C=c h^8`, and `d1=BASE-HALF`, `d2=HALF-QUARTER`:

- `Ahat=(-16 d1+1024 d2)/45 = A-(17/64)C+O(h^10)`;
- `Bhat=(256 d1-4096 d2)/189 = B+(425/336)C+O(h^10)`;
- the Iteration-533 diagnostic `R3=(BASE-80 HALF+1024 QUARTER)/945` obeys `R3=D+C/1344+O(h^10)`.

Classification: `PASS_ITER424_THREE_LEVEL_H4_H6_ERROR_COMPONENT_INVERSION_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

Reproducible code: `candidate_gravity/code/iteration536_iter424_three_level_error_component_exact_audit.py`.
Machine-readable authority: `candidate_gravity/results/iteration536_iter424_three_level_error_component_exact_audit.json`.

## Scope/guardrails
This is an exact structural/truncation diagnostic under the existing smooth central4 expansion. It changes no dynamics, mass nodes, precision, thresholds, successor order, or Iteration-424 physical acceptance clause. It cannot rescue a failing physical gate or promote index 2.

No Candidate-Gravity consistency FAIL is generated. No exact comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate is claimed. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.

## Active computation
Canonical QUARTER rank2 run `34102627559`, job `101680313500`, remains the unique authorized heavy computation. It was still `in_progress` at this iteration's live inspection. No duplicate was launched.

## Authority ledger
Physical/operator authority: Iteration 411.
Physical blocker: Iteration 421, unresolved `[2]`.
BASE/HALF support: Iteration 523 (`32/32`).
BASE/HALF assembly: Iteration 527.
Quarter manifest: Iteration 529.
Three-level Gram: Iteration 530.
Normalized conditioning: Iteration 531.
Quarter successor order: Iteration 532.
Truncation diagnostic: Iteration 533.
Quarter rank1 raw-consumption: Iteration 534.
Rank2 launch: Iteration 535.
Three-level h4/h6 error-component inversion: Iteration 536.
Latest authoritative research iteration: Iteration 536.

MODEL_READINESS: 24%
Readiness change: 0 percentage points. The truncation diagnostic layer is stricter, but no additional stable model-level rubric sector is complete.

## Exact next gate
Wait for canonical rank2 run `34102627559` to terminate, then raw-consume its artifact fail-closed. Raw-valid PASS authorizes only rank3 `(-1.25e-6,-2.5e-6)` from the Iteration-532 frozen order.
