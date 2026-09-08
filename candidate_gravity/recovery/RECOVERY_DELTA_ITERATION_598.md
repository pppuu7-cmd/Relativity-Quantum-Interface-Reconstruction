# Recovery Delta — Iteration 598

Date: 2026-09-08
MODEL_READINESS: 24%

## Authority
Iter597 raw artifact from run `34230641155`, job `102075596468`, artifact `10057686995` was independently downloaded and hashed. Its negative numerical rows are preserved, but Iter598 proves the implementation did **not** instantiate the prospectively frozen Iter596 scalar routing: both the mandatory one-leg anchor and the full Ward rows looped over arbitrary `PROBES`, while Iter596 requires per-gauge symmetric route `p=-q_g/2`, `p'=+q_g/2`.

Canonical Iter598: run `34236177851`, job `102094351910`, head `f65c23ab46f5b4571a6fc9ce5cb39d958fd0109a`, artifact `10059929340`, digest `sha256:abf81c0cc102980501618516d0dfe4e7117958af6063c53af9acffc67107fade`; raw result SHA-256 `0ba9032dc076fb7b5b420e99cdc293df839365eb97610e395c7c7cc7d7a0a291`; raw audit SHA-256 `e868c8fb917c2be3b37faced7c005569d9cad2c7c733221703fec835ce2b62f7`.

Classification: `BLOCKED_ITER597_IMPLEMENTATION_DOES_NOT_INSTANTIATE_FROZEN_ITER596_ROUTE__NEGATIVE_NUMBERS_PRESERVED_NONAUTHORITATIVE`.

## Consequence
Do not promote Iter597 to nonlinear Ward PASS/FAIL authority for the frozen contract. Do not weaken Iter596. Do not discard Iter597 numbers; retain them as diagnostics of the implemented off-contract object.

## Exact next gate
Repair the evaluator prospectively so the mandatory one-leg reduction and full nonlinear Ward rows use exact per-gauge symmetric scalar routing while retaining K3 + all six K1/K2 + all six ordered K1^3 families, both spectator Lie terms, both endpoint terms, and the already-frozen thresholds. Then run and raw-consume that corrected full Ward gate.

Source/Born subtraction remains NOT_PERFORMED. ANSATZ-003, Fisher/resources remain forbidden.
