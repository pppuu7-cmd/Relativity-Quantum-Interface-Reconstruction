# RQIR Candidate Gravity — Research Log Iteration 433

Iteration 432 completed as a non-promoting source/provenance closure. Its workflow bound the recursive Iteration-270 roots `Q0/Q1/Asub/y_down`; artifact `9945106288` was uploaded under run `33894344918`. Physical authority did not change.

Actions were then idle (`queued=0`, `in_progress=0`), so the next scientifically allowed deepest-first sub-gate was created: 80/120-digit closure for Iteration-270 `Q0` and `y_down` at frozen representative inputs. The first run `33898986792` failed operationally before artifact creation because `mpmath` was absent on the runner; this is not a scientific FAIL. The only repair was pinning/installing `mpmath==1.3.0`, commit `adc50099868ca12b8ece13590163acf5fb7d6490`.

The repaired run `33899067536`, job `101108587795`, is active. Acceptance is prospective and unchanged: 80-vs-120 digit discrepancy `<=1e-40`, binary64-parent reproduction `<=1e-12`, finite outputs. This gate is diagnostic-only and cannot promote index 2.

If raw-valid PASS, the next independent layer is `Q1/N1` 80/120-digit closure, followed only afterward by `Asub/Acoef/A_finite`. No outward 368/370 precision claim is allowed before those parent layers are closed.

`MODEL_READINESS: 24%`
