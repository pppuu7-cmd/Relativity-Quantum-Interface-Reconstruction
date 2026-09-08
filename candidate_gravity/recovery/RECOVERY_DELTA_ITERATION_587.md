# Recovery Delta — Iteration 587

Date: 2026-09-08

## New authority consumed
- Iter584 mixed bilinear K2 remains raw-valid: raw `result.json` SHA256 `4ba39a78550e27575939fec03fb9a1514d43e478ca25fb354c87939ed316c76d`, `failures=[]`.
- Iter586 source-signature run `34203781256`, artifact `10046877433`: raw-valid PASS, raw result SHA256 `8e83fec148e8d0acac3578a77023890db35c070ccff38af0f44591a10cd3c8d1`.
- Iter587 off-shell-routing run `34203928999`, artifact `10046935799`: raw-valid PASS, raw result SHA256 `1fb42e1ab8e3de2ae31426297c40f9c845ddd38e08d3f3f63cd6d4381252bcfd`.

## Scientific state change
Iter586 proves the same physical Iter582 timelike buckets map from Candidate `q^2={-1,-0.34,-0.14}` under `(-+++)` to MSSC source `q^2={1,0.34,0.14}` under `(+---)`. For MSSC mass `m=0.7`, none is an on-shell equal-mass elastic transfer and all are below `4m^2=1.96`. Therefore a matched source bridge must be off-shell/source-completed. Iter585 Breit elastic calculation is retained as internally correct but is not authority for the Iter582 bridge.

Iter587 prospectively freezes the minimal symmetric no-extra-parameter routing
`q=(sqrt(s),0,0,0), p=-q/2, p'=+q/2, k=q`.
From the frozen Iter218 Ward identity,
`q_mu V^{mu nu}=(m^2-s/4)q^nu`.
Exact coefficients are `6/25`, `81/200`, `91/200` for `s=1,0.34,0.14`; maximum numerical verification error `5.551115123125783e-17`.

Classification: `PASS_PROSPECTIVE_MSSC001_SYMMETRIC_OFFSHELL_K1_ROUTING_AND_WARD_CONTRACT__NON_RESIDUAL`.

No Source/Born subtraction. No comparator quotient yet. No ANSATZ-003. Fisher/resources forbidden.

MODEL_READINESS: 24%

Readiness change: 0 percentage points. A convention/kinematic blocker and K1 routing subgate closed, but no additional full stable-rubric sector has closed.

## Exact next gate
Construct on the frozen Iter587 routing the complete same-parent MSSC-001 two-graviton source Ward object from K1 exchange plus raw-valid Iter584 K2 contact. Verify inverse-propagator longitudinal cancellation/matching before mapping to Iter582 and before the unchanged C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
