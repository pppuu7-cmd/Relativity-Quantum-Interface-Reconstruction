# Candidate Gravity Recovery Delta — Iteration 405

Date: 2026-09-04

MODEL_READINESS: 24%

## Newly consumed raw authority

Iteration 399 run `33828617524` completed and its raw artifact `9921602344` was inspected independently of workflow colour. Channel 5 / class 8 / `q^2=-0.14` is `CONVERGED`: `D_s TrU1^2 double-double = 0.000119747535002548`, scaled convergence error `1.8393013149631406e-7`, authority audit PASS, result SHA-256 `63cf00714ce2c17abc5c0d9a223b5698df889c7d8586adac80c1cc74f5407e87`, artifact digest `sha256:94e6a21b6f5609ac97b4ad7ea945d69745c8e9ceae8d805b850220aca96ea686`. This closes the former operational gap at double-double index 5; indices 2,4,11 remain `BLOCKED_CONVERGENCE` and are not used in q2 sums.

Iteration 400 run `33829453920` completed. All four previously missing repeated-U2 indices 14,15,16,17 have nonempty raw artifacts, PASS authority audits, `CONVERGED` status, Iteration-392 topology-mask consistency and unchanged `2e-5` convergence threshold. Their high-grid operator-coordinate values are:

- 14, `q^2=-0.34`: `-0.00011341677230793501`, artifact `9921511851`, result SHA `428652214fb6b9a4e35d475e1a26faca7a63af23eb2351050bd0bf6f1ca30fea`;
- 15, `q^2=-0.14`: `-0.00019874443441835922`, artifact `9921509155`, result SHA `4b2db87614344511346a7d429a774ee013cd8b2c1caeba0bc0e27dfd97a7f53d`;
- 16, `q^2=-0.14`: `+0.0006290774853610352`, artifact `9921545387`, result SHA `bfa3e6421ba5f53bdd051e6ac4dc6be2eea66f8881563159082346d11f850f77`;
- 17, `q^2=-1`: `+0.00006894241423070089`, artifact `9921530148`, result SHA `4eda197f9a7367498ba5bb48248b6bf0579104fc6a814bd9d8a88ef7ed138003`.

Combining these only diagnostically with the frozen Iteration-404 44/48 preassembly gives the expected exact-48 repeated-cut q2 sums `-1: 0.0004825971545254671`, `-0.34: -0.0005645318371195369`, `-0.14: -0.0014213811702222749`. These sums are not promoted until Iteration 405 raw artifact/audit passes.

## Active gate

Iteration 405 exact-48 fail-closed assembly was created from the frozen Iteration-404 manifest plus exact raw provenance for Iteration-400 records 14-17. Workflow run `33832181526`, head `069ea4ad388f73998a8bca3f594d496f13710637`, is active. It requires exactly one `CONVERGED` record for every index 0..47 and keeps the `+i/2` effective-action weight separate.

Iteration 401 structural analytic-azimuth oracle run `33830352712` is independently in progress and is not duplicated.

## Guardrails

Unsupported remains BLOCKED; no zero fill. Distinct q2 buckets remain separate. No effective-action weight folding before operator-coordinate closure. No Source/Born subtraction. No `ANSATZ-003`. No Fisher/resources. No blind full-C5.

## Next gate

If Iteration 405 raw authority passes, form complete `Tr U2` q2 coordinates by adding Iteration-366 repeated-family simple-simple to exact repeated-cut values (Iteration-361 ordinary-simple is zero), still without `+i/2`. In parallel consume Iteration 401; if its structure oracle passes, apply the exact Iteration-403 mass-stencil commutation architecture separately to unresolved double-double channels 2,4,11 with held-out original-integrand checks and unchanged threshold.

MODEL_READINESS: 24%
