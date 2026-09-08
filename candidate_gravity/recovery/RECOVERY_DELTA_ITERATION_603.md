# Recovery Delta — Iteration 603

Date: 2026-09-08

## Authoritative change
Iteration 603 is a diagnostic-only, non-promoting lattice-radius study of the three nonconvergent `s/xi0..2` rows from the preserved Iter602 frozen nonlinear Ward FAIL. It changes only the finite Fourier lattice radius `LAT_R=3,4,5`; physical fixture, Iter601 endpoint realization, all 13 source families, symmetric scalar route, FD steps `(2e-2,1e-2,5e-3)`, Ward thresholds and normalization are unchanged.

Canonical provenance:
- run `34240339709`, job `102108562629`;
- head `fcd8f27a6d72bb139bf3fc0f05eb1a74f51efbcf`;
- artifact `10061784026`, digest `sha256:fb1755978a482279325a711e2995e58c3040a64721deb529bf59a16baf3326e6`;
- raw `result.json` SHA-256 `44d1266cffaf4d4579f10a3eb0e72efe0dcd90a5f4a429eeabcc7f00ebd67d3d`;
- raw audit `PASS_DIAGNOSTIC_RAW_AUDIT_ITER603`, `failures=[]`.

Classification:
`PASS_RAW_CONSUMED_DIAGNOSTIC_ITER602_S_ROWS_STRONGLY_LATTICE_RADIUS_SENSITIVE__NON_PROMOTING`.

## What the raw artifact shows
The three problematic `s` rows collapse strongly as the nested lattice is enlarged:
- `s/xi0`: `R3=1.9380458271129164e-2`, `R4=1.0196848568956602e-3`, `R5=1.5196560757667354e-11`;
- `s/xi1`: `R3=1.0434355326722732e-2`, `R4=6.105927532745819e-4`, `R5=3.5860703739940693e-12`;
- `s/xi2`: `R3=1.0434355320073186e-2`, `R4=6.105927523541254e-4`, `R5=3.2329975781283642e-12`.

The `R3/R5` ratios are approximately `1.28e9`, `2.91e9`, and `3.23e9`. At `R=5`, `s/xi3=5.62e-15` and the maximum of every other row is `5.64e-12`.

## Scientific interpretation
This is strong evidence that the three Iter602 nonconvergent rows are sensitive to the finite-lattice realization/boundary rather than radius-stable negative evidence. It does **not** erase, weaken or promote Iter602: the frozen Iter602 result remains historical scientific FAIL. Iter603 itself is explicitly non-promoting and cannot be used as a model PASS.

The large `K` condition estimates in the `s` sector (`~7.7e17–1.2e18`) also forbid treating one apparently small radius result as sufficient authority. A prospective boundary/convergence rule must be frozen before any production rerun, with fail-closed `BLOCKED_CONVERGENCE` if the rule is not met.

## Exact next gate
Iteration 604 must prospectively freeze a finite-lattice boundary/convergence contract derived from the unchanged continuum Ward identity. The contract must predefine nested radii, unchanged FD/Ward thresholds, a radius-stability criterion and a fail-closed outcome before seeing any new production Ward result. Only after raw-valid Iter604 may an adaptive production rerun be launched.

No Source/Born subtraction, source-to-Iter582 mapping, comparator quotient, `ANSATZ-003`, Fisher or resources are authorized.

MODEL_READINESS: 24%
