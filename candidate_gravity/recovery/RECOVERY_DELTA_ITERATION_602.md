# Recovery Delta — Iteration 602

Date: 2026-09-08

## Authoritative change
Iteration 602 reran the full frozen Iter596 nonlinear source Ward gate after Iter601 independently corrected and raw-validated the scalar endpoint matrix realization. The only production change relative to Iter599 was the endpoint covariance realization `Delta G - R G - G L`, with `R_rc=xi.p_c` and `L_rc=-xi.p_r` for `p_r=p_c+q`. The Iter596 five Ward classes, Iter588 fixture, all 13 source families, symmetric per-gauge scalar route, FD steps and tolerances were unchanged.

Canonical provenance:
- evaluator commit `703eaf4635ed2b0ad82a2da51b350e1b51d9a8a2`;
- workflow/head commit `c3b5d0f796e32be0999e09224031e54b4d494742`;
- run `34240030976`, job `102107522186`;
- artifact `10061578531`, digest `sha256:09f7ef6a98327abff416d46b32a99bfec599a9b68d04edacd91c019ce3436d56`;
- raw `result.json` SHA-256 `2897821038b495562d316c56ea40bf051b969a258ece5a2ee2bddc944981d138`;
- raw `authority_audit.json` SHA-256 `5cd7f4fa2f59e250d896d06862bfb079cfe27bec0cffe5b0c1d02b73890b71cb`.

Classification:
`FAIL_RAW_CONSUMED_FULL_SOURCE_LEVEL_NONLINEAR_WARD_WITH_ITER601_ENDPOINT_REALIZATION__PRESERVED_NEGATIVE_RESULT`.

## What closed
- All 12 mandatory one-leg Iter587 anchors pass after Iter601 endpoint correction: max abs residual `6.88338845912217e-15 <= 2e-11`.
- Iter594 13-family cubic assembly implementation cross-check remains PASS: match errors `5.767843750358048e-08` and `4.4987911188010266e-08`, both `<=2e-5`.
- Nine of twelve full Ward rows have no threshold failure. `s/xi3` is `2.54e-14`; the largest `a` row is `4.93e-12`; the largest `b` row is `1.17e-12`.

## Frozen negative result
Only `s/xi0`, `s/xi1`, `s/xi2` fail. Their last absolute residuals are respectively:
- `0.006096828631513357`;
- `0.0035599485158516048`;
- `0.0035599485212443388`.

They simultaneously fail the frozen convergence criterion. Example `s/xi0` real FD sequence at `(2e-2,1e-2,5e-3)` is
`1.5524867089244463 -> 1.78613555509661e-05 -> -0.0049883971870925`, with last-step `0.00607858101621395 >> 2e-5`.

Therefore Iter602 is preserved as a scientific negative frozen-gate result, but these three rows are not yet stable model-level Ward-violation evidence. Their finite Fourier-lattice realization sensitivity must be diagnosed before interpretation. No threshold may be weakened and the Iter602 result may not be retroactively promoted.

## Next gate
Iteration603 is a separately frozen **diagnostic-only / non-promoting** radius study at `LAT_R=3,4,5`, holding physical fixture, source families, endpoint realization, FD steps and Ward thresholds unchanged. Its only role is to distinguish finite-lattice boundary sensitivity from radius-stable negative evidence. Any later production rerun requires a new prospective contract; Iter603 itself cannot promote Iter602.

No Source/Born subtraction, source-to-Iter582 mapping, comparator quotient, ANSATZ-003, Fisher or resources are authorized.

MODEL_READINESS: 24%
