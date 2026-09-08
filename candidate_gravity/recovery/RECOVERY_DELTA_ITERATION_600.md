# Recovery Delta — Iteration 600

Date: 2026-09-08
MODEL_READINESS: 24%

## Authority
Iter599 prospectively repaired the Iter597 route mismatch: for every gauge singleton `g`, both mandatory anchor and full Ward rows use exactly `p=-q_g/2`, `p'=+q_g/2`. K3 + all six K1/K2 placements + all six ordered K1^3 chains, both spectator Lie terms, both endpoint terms, exact Iter588 fixture, and inherited pre-result thresholds were retained unchanged.

Canonical corrected run: `34236758448`, job `102096346284`, head `491f55d9f88b2d40f7e737108f2dfc24bfe3f6e4`, artifact `10060216987`, digest `sha256:577bb2d4a8f56f24f86aecdfb4abc6e9616d0a9a28bfb3bae40330505b0eed3d`. The artifact was fail-closed consumed by run `34237037608`; committed raw result SHA-256 `9bafe4cf47c35e8a5e2537d94605e5f0e54345bc28ef03af16c9b7e3675ac855`.

## Iter600 authority correction
Iter599 reported full-Ward numerical failures, but its mandatory one-leg matrix anchor also fails the frozen Iter596 reduction requirement. Anchor tolerance is `2e-11`; observed examples include:
- `s/xi0 = 2.083333333333334`;
- `a/xi0 = 0.4395604395604424`;
- `a/xi1 = a/xi2 = 0.1098901098901106`;
- `b/xi0 = 0.7407407407407341`;
- `b/xi1 = b/xi2 = 0.1234567901234587`.

Iter596 states that failure of spectator-free reduction to Iter587 invalidates numerical nonlinear Ward evaluation. Therefore the Iter599 cubic rows (`max |W| = 0.13675071724815208`, `max last-step = 0.006078581018494812`) are preserved as diagnostics, **not** promoted to Candidate-Gravity consistency FAIL authority.

Classification: `BLOCKED_ITER599_FULL_WARD_NUMBERS_NONAUTHORITATIVE_BECAUSE_MANDATORY_ITER587_ANCHOR_FAILS__ENDPOINT_COVARIANCE_REALIZATION_DIAGNOSIS_REQUIRED`.

No frozen threshold or family content is weakened. Source/Born subtraction and source-to-Iter582 mapping remain NOT_PERFORMED. ANSATZ-003 and Fisher/resources remain forbidden.

## Exact next gate
Derive and prospectively freeze the scalar endpoint/covariance matrix realization directly from `Delta_xi phi(k)=int xi(l)(k-l)_rho phi(k-l)`, with explicit row/column momentum orientation and endpoint signs. Require the resulting one-leg matrix identity to reproduce Iter587 exactly on all three frozen symmetric routes before any cubic Ward rerun.

Readiness change from Iter598: 0 percentage points. This iteration identifies and localizes an implementation/authority blocker but closes no new model-level readiness rubric sector.
